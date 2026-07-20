from __future__ import annotations

import argparse
import html
import json
import os
import sys
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Iterable, Protocol
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
DEFAULT_PERSONA_DIR = ROOT / "personas"
MAX_ROUNDS = 32
MAX_TARGET_LENGTH = 10_000


class TribunalType(str, Enum):
    KNOWLEDGE = "knowledge"
    CRITIQUE = "critique"
    UI_UX = "ui_ux"
    COMPARISON = "comparison"


class HardnessLevel(str, Enum):
    LIGHT = "light"
    STANDARD = "standard"
    HARD = "hard"
    BRUTAL = "brutal"


HARDNESS_MIN_ROUNDS = {
    HardnessLevel.LIGHT: 1,
    HardnessLevel.STANDARD: 1,
    HardnessLevel.HARD: 2,
    HardnessLevel.BRUTAL: 4,
}


@dataclass(frozen=True)
class Persona:
    slug: str
    name: str
    role: str
    stance: str
    skills: list[str]
    reference_repos: list[str]
    instructions: str
    reference_input: str | None = None
    disclaimer: str | None = None


@dataclass(frozen=True)
class EngineAllocation:
    provider: str
    capacity_before: int | None
    source: str


@dataclass(frozen=True)
class JudgeRequest:
    target: str
    mode: TribunalType
    round_index: int
    judge_index: int
    persona: Persona
    routed_skills: list[str]
    notebooklm_url: str | None


@dataclass(frozen=True)
class BackendResult:
    verdict: str
    score: int
    findings: list[str]
    evidence: list[str]
    evidence_gaps: list[str]


class JudgeBackend(Protocol):
    name: str

    def evaluate(self, request: JudgeRequest) -> BackendResult: ...


@dataclass(frozen=True)
class JudgeView:
    round_index: int
    judge_index: int
    persona_slug: str
    persona: str
    role: str
    backend: str
    engine: str
    engine_source: str
    engine_capacity_before: int | None
    routed_skills: list[str]
    verdict: str
    score: int
    findings: list[str]
    evidence: list[str]
    evidence_gaps: list[str]


@dataclass(frozen=True)
class DebateSummary:
    kind: str
    recurring_failures: list[str]
    disagreements: list[str]
    strongest_points: list[str]


@dataclass(frozen=True)
class VerdictReport:
    target: str
    mode: str
    rounds: int
    requested_rounds: int
    hardness: str
    notebooklm_url: str | None
    engine_plan: list[EngineAllocation]
    judge_views: list[JudgeView]
    debate: DebateSummary
    final_verdict: str
    final_score: int
    crown: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)

    def to_markdown(self) -> str:
        safe_target = html.escape(self.target, quote=False)
        lines = [
            f"# Tribunal Verdict: {safe_target}",
            "",
            f"- Mode: `{self.mode}`",
            f"- Rounds: `{self.rounds}` effective (`{self.requested_rounds}` requested)",
            f"- Hardness: `{self.hardness}`",
            f"- NotebookLM: `{self.notebooklm_url or 'not supplied; evidence gaps must stay visible'}`",
            f"- Final score: `{self.final_score}/100`",
            f"- Crown: {self.crown}",
            "",
            "## Judge Views",
        ]
        for view in self.judge_views:
            lines.extend(
                [
                    f"### R{view.round_index} J{view.judge_index}: {view.persona} (`{view.persona_slug}`)",
                    f"- Backend: `{view.backend}`",
                    f"- Engine: `{view.engine}` from `{view.engine_source}` "
                    f"(capacity before: `{view.engine_capacity_before if view.engine_capacity_before is not None else 'unlimited local'}`)",
                    f"- Skills: {', '.join(view.routed_skills)}",
                    f"- Score: `{view.score}`",
                    f"- Verdict: {view.verdict}",
                    "- Findings:",
                    *[f"  - {item}" for item in view.findings],
                    "- Evidence:",
                    *[f"  - {item}" for item in view.evidence],
                    "- Evidence gaps:",
                    *[f"  - {item}" for item in view.evidence_gaps],
                    "",
                ]
            )
        lines.extend(
            [
                "## Post-hoc Synthesis",
                f"- Kind: `{self.debate.kind}`",
                "- This is a synthesis after isolated judgments, not an interactive agent debate.",
                "- Recurring failures:",
                *[f"  - {item}" for item in self.debate.recurring_failures],
                "- Disagreements:",
                *[f"  - {item}" for item in self.debate.disagreements],
                "- Strongest points:",
                *[f"  - {item}" for item in self.debate.strongest_points],
                "",
                "## Final Verdict",
                self.final_verdict,
            ]
        )
        return "\n".join(lines)


class EngineManager:
    def __init__(
        self,
        quota_file: str | None = None,
        quota_json: str | None = None,
        default_provider: str = "local-rules",
    ):
        if not default_provider.strip():
            raise ValueError("default provider must be a non-empty string")
        self.source = "builtin-local" if default_provider == "local-rules" else "backend-default"
        self.provider_capacities: dict[str, int | None] = {default_provider: None}
        raw = quota_json or os.environ.get("TRIBUNAL_ENGINE_QUOTAS_JSON")
        path = quota_file or os.environ.get("TRIBUNAL_ENGINE_QUOTAS_FILE")
        if raw:
            self.provider_capacities = self._parse_capacities(raw)
            self.source = "env:TRIBUNAL_ENGINE_QUOTAS_JSON"
        elif path:
            quota_path = Path(path)
            if not quota_path.is_file():
                raise ValueError(f"quota file does not exist: {path}")
            self.provider_capacities = self._parse_capacities(quota_path.read_text())
            self.source = f"file:{path}"

    @staticmethod
    def _parse_capacities(raw: str) -> dict[str, int]:
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as error:
            raise ValueError(f"quota data must be valid JSON: {error.msg}") from error
        if not isinstance(data, dict) or not data:
            raise ValueError("quota data must be a non-empty JSON object")
        parsed: dict[str, int] = {}
        for provider, capacity in data.items():
            name = str(provider).strip()
            if not name:
                raise ValueError("quota provider names must be non-empty")
            if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity < 0:
                raise ValueError(f"capacity for {name!r} must be a non-negative integer judge count")
            parsed[name] = capacity
        return parsed

    def allocate(self, count: int) -> list[EngineAllocation]:
        if count < 1:
            raise ValueError("allocation count must be >= 1")
        remaining = dict(self.provider_capacities)
        allocations: list[EngineAllocation] = []
        for _ in range(count):
            unlimited = [
                provider for provider, capacity in remaining.items() if capacity is None
            ]
            if unlimited:
                provider = sorted(unlimited)[0]
                allocations.append(EngineAllocation(provider, None, self.source))
                continue
            available = [
                (provider, capacity)
                for provider, capacity in remaining.items()
                if capacity is not None and capacity > 0
            ]
            if not available:
                raise RuntimeError(f"configured engine capacity exhausted after {len(allocations)} judge(s)")
            provider, capacity = max(available, key=lambda item: (item[1], item[0]))
            allocations.append(EngineAllocation(provider, capacity, self.source))
            remaining[provider] = capacity - 1
        return allocations


class PersonaLibrary:
    def __init__(self, persona_dir: Path = DEFAULT_PERSONA_DIR):
        self.persona_dir = persona_dir
        self.personas = self._load()

    def _load(self) -> dict[str, Persona]:
        personas: dict[str, Persona] = {}
        paths = sorted(self.persona_dir.glob("*.json"))
        if not paths:
            raise RuntimeError(f"no persona JSON files found in {self.persona_dir}")
        for path in paths:
            try:
                payload = json.loads(path.read_text())
            except json.JSONDecodeError as error:
                raise ValueError(f"invalid persona JSON in {path}: {error.msg}") from error
            if not isinstance(payload, dict):
                raise ValueError(f"invalid persona {path}: root must be a JSON object")
            text_fields = ("name", "role", "stance", "instructions")
            for field in text_fields:
                if not isinstance(payload.get(field), str) or not payload[field].strip():
                    raise ValueError(f"invalid persona {path}: `{field}` must be a non-empty string")
            list_fields = ("skills", "reference_repos")
            for field in list_fields:
                value = payload.get(field)
                if (
                    not isinstance(value, list)
                    or not value
                    or any(not isinstance(item, str) or not item.strip() for item in value)
                ):
                    raise ValueError(
                        f"invalid persona {path}: `{field}` must be a non-empty list of strings"
                    )
            reference_input = payload.get("reference_input")
            if reference_input is not None and (
                not isinstance(reference_input, str) or not reference_input.strip()
            ):
                raise ValueError(
                    f"invalid persona {path}: `reference_input` must be a non-empty string when set"
                )
            disclaimer = payload.get("disclaimer")
            if disclaimer is not None and (
                not isinstance(disclaimer, str) or not disclaimer.strip()
            ):
                raise ValueError(
                    f"invalid persona {path}: `disclaimer` must be a non-empty string when set"
                )
            reference_repos = list(payload["reference_repos"])
            for reference_repo in reference_repos:
                try:
                    validate_github_repo_url(reference_repo)
                except ValueError as error:
                    raise ValueError(
                        f"invalid persona {path}: `reference_repos` entry {reference_repo!r} "
                        "must be a bare HTTPS GitHub repository URL"
                    ) from error
            personas[path.stem] = Persona(
                slug=path.stem,
                name=payload["name"],
                role=payload["role"],
                stance=payload["stance"],
                skills=list(payload.get("skills", [])),
                reference_repos=reference_repos,
                instructions=payload.get("instructions", ""),
                reference_input=reference_input,
                disclaimer=disclaimer,
            )
        if len(personas) < 3:
            raise RuntimeError(f"need at least 3 personas in {self.persona_dir}")
        return personas

    def select(
        self,
        mode: TribunalType,
        topic: str,
        requested: Iterable[str] | None = None,
        offset: int = 0,
        count: int = 3,
    ) -> list[Persona]:
        if requested:
            names = list(requested)
            unknown = sorted(set(names).difference(self.personas))
            if unknown:
                raise ValueError(f"unknown requested persona slug(s): {', '.join(unknown)}")
            if len(set(names)) != len(names):
                raise ValueError("requested persona slugs must be unique")
            if len(names) < count:
                raise ValueError(f"requested panel needs at least {count} persona slugs")
            selected = [self.personas[name] for name in names]
            offset = offset % len(selected)
            rotated = selected[offset:] + selected[:offset]
            return rotated[:count]

        topic_l = topic.lower()
        ranked: list[tuple[int, Persona]] = []
        for persona in self.personas.values():
            haystack = " ".join(
                [persona.slug, persona.name, persona.role, persona.stance, " ".join(persona.skills)]
            ).lower()
            score = 0
            if mode == TribunalType.UI_UX:
                if persona.slug in {"ux-operator-flow", "ux-specialist", "ux-researcher", "ui-specialist", "ui-minimalist"}:
                    score += 30
                elif any(k in haystack for k in ["ui", "ux", "workflow", "ergonomics", "accessibility", "visual-design"]):
                    score += 10
            if mode == TribunalType.KNOWLEDGE:
                if persona.slug == "knowledge-analyst":
                    score += 30
                elif persona.slug in {"security-auditor", "systems-architect", "andrej-karpathy"}:
                    score += 20
                elif any(k in haystack for k in ["knowledge", "research", "fact", "audit", "evidence"]):
                    score += 8
            if mode == TribunalType.CRITIQUE:
                if persona.slug in {"systems-architect", "andrej-karpathy", "security-auditor"}:
                    score += 30
                elif any(k in haystack for k in ["karpathy", "architect", "auditor", "security", "systems"]):
                    score += 8
            if mode == TribunalType.COMPARISON and any(k in haystack for k in ["knowledge", "karpathy", "systems"]):
                score += 8
            score += sum(1 for word in topic_l.split() if word in haystack)
            ranked.append((score, persona))

        ranked.sort(key=lambda item: (item[0], item[1].slug), reverse=True)
        ordered = [persona for score, persona in ranked if score > 0]
        ordered.extend([persona for _, persona in ranked if persona not in ordered])
        if len(ordered) < count:
            raise RuntimeError(f"need at least {count} personas in {self.persona_dir}")
        offset = offset % len(ordered)
        rotated = ordered[offset:] + ordered[:offset]
        return rotated[:count]


class SkillRouter:
    BASE = ["evidence-ledger", "anti-fake-checks", "report-matrix-gate"]
    MODE_SKILLS = {
        TribunalType.KNOWLEDGE: ["web-search", "notebooklm", "primary-source-review"],
        TribunalType.CRITIQUE: ["architecture", "production-code-audit", "andrej-karpathy"],
        TribunalType.UI_UX: [
            "high-end-visual-design",
            "minimalist-ui",
            "ui-ux-pro-max",
            "design-taste-frontend",
            "web-design-guidelines",
        ],
        TribunalType.COMPARISON: ["competitive-landscape", "api-documentation", "csv-gate"],
    }

    def route(self, persona: Persona, mode: TribunalType, notebooklm_url: str | None) -> list[str]:
        skills = [*self.BASE, *self.MODE_SKILLS[mode], *persona.skills]
        if notebooklm_url:
            skills.append("notebooklm-linked")
        return sorted(set(skills))


def validate_notebooklm_url(value: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("NotebookLM URL must be a non-empty string")
    parsed = urlparse(value.strip())
    path_parts = [part for part in parsed.path.split("/") if part]
    if (
        parsed.scheme != "https"
        or parsed.hostname != "notebooklm.google.com"
        or len(path_parts) != 2
        or path_parts[0] != "notebook"
        or not path_parts[1]
    ):
        raise ValueError(
            "NotebookLM URL must match https://notebooklm.google.com/notebook/<id>"
        )
    return value.strip()


def validate_github_repo_url(value: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("GitHub repository URL must be a non-empty string")
    normalized = value.strip()
    parsed = urlparse(normalized)
    path_parts = [part for part in parsed.path.split("/") if part]
    if (
        parsed.scheme != "https"
        or parsed.hostname != "github.com"
        or len(path_parts) != 2
        or parsed.params
        or parsed.query
        or parsed.fragment
    ):
        raise ValueError("GitHub repository URL must match https://github.com/<owner>/<repo>")
    return normalized


class LocalRulesBackend:
    name = "local-rules"

    MODE_FINDINGS = {
        TribunalType.KNOWLEDGE: [
            "Primary-source coverage and claim-level citations are required before correctness can pass.",
            "A dated metadata snapshot must be distinguished from facts verified in the source corpus.",
        ],
        TribunalType.CRITIQUE: [
            "Executable proof and explicit failure modes are required before implementation claims can pass.",
            "Operational and maintenance risks must remain visible instead of being averaged into a friendly verdict.",
        ],
        TribunalType.UI_UX: [
            "Viewport, interaction, accessibility, and repeated-use workflow evidence are required for a UI/UX pass.",
            "Code inspection alone cannot establish visual polish, cognitive load, or task completion quality.",
        ],
        TribunalType.COMPARISON: [
            "Comparison claims require a declared use case, real links, dated metadata, and differentiated scoring.",
            "A crown is valid only when category mismatches and material trade-offs remain explicit.",
        ],
    }

    def evaluate(self, request: JudgeRequest) -> BackendResult:
        findings = [
            self.MODE_FINDINGS[request.mode][0],
            f"{request.persona.name} lens: {request.persona.instructions}",
            self.MODE_FINDINGS[request.mode][1],
        ]
        evidence = [
            f"Target input was supplied to isolated judge R{request.round_index}J{request.judge_index}.",
            f"Persona `{request.persona.slug}` was selected with role `{request.persona.role}`.",
            f"Routed skills: {', '.join(request.routed_skills)}.",
            "The local-rules backend checked orchestration structure only; it performed no network or semantic target inspection.",
            "Structural score: 10 points each for a valid target, isolated judge coordinate, validated persona route, and mode-specific skill route.",
        ]
        gaps = [
            "Target semantics were not evaluated by the local-rules backend; use an evidence-capable live backend for substantive judgment."
        ]
        score = 40
        if request.notebooklm_url:
            evidence.append(f"NotebookLM reference recorded: {request.notebooklm_url}")
            gaps.append(
                "NotebookLM content was not queried by the local-rules backend; the URL is provenance, not verified evidence."
            )
            evidence.append(
                "A syntactically valid NotebookLM reference adds 10 structural provenance points; it does not prove source access."
            )
            score += 10
        else:
            gaps.append("No NotebookLM or equivalent source-corpus reference was supplied.")
        verdict = (
            f"{request.persona.name} completed a local structural readiness review at {score}/100. "
            "This score measures review setup, not the factual correctness or product quality of the target."
        )
        return BackendResult(
            verdict=verdict,
            score=score,
            findings=findings,
            evidence=evidence,
            evidence_gaps=gaps,
        )


def validate_backend_result(result: BackendResult, backend_name: str) -> BackendResult:
    if not isinstance(result, BackendResult):
        raise TypeError(f"backend {backend_name!r} must return BackendResult")
    if isinstance(result.score, bool) or not isinstance(result.score, int) or not 0 <= result.score <= 100:
        raise ValueError(f"backend {backend_name!r} score must be an integer from 0 through 100")
    if not isinstance(result.verdict, str) or not result.verdict.strip():
        raise ValueError(f"backend {backend_name!r} verdict must be a non-empty string")
    for field in ("findings", "evidence", "evidence_gaps"):
        value = getattr(result, field)
        if (
            not isinstance(value, list)
            or not value
            or any(not isinstance(item, str) or not item.strip() for item in value)
        ):
            raise ValueError(
                f"backend {backend_name!r} {field} must be a non-empty list of strings"
            )
    return result


class TribunalOrchestrator:
    def __init__(
        self,
        tribunal_type: TribunalType,
        rounds: int = 1,
        hardness: str | HardnessLevel = HardnessLevel.STANDARD,
        persona_dir: Path = DEFAULT_PERSONA_DIR,
        quota_file: str | None = None,
        quota_json: str | None = None,
        notebooklm_url: str | None = None,
        backend: JudgeBackend | None = None,
    ):
        if isinstance(rounds, bool) or not isinstance(rounds, int) or rounds < 1:
            raise ValueError("rounds must be >= 1")
        if rounds > MAX_ROUNDS:
            raise ValueError(f"rounds must be <= {MAX_ROUNDS}")
        if not isinstance(tribunal_type, TribunalType):
            raise ValueError("tribunal_type must be a TribunalType value")
        self.tribunal_type = tribunal_type
        self.requested_rounds = rounds
        self.hardness = self._normalize_hardness(hardness)
        self.rounds = max(rounds, HARDNESS_MIN_ROUNDS[self.hardness])
        self.notebooklm_url = validate_notebooklm_url(notebooklm_url) if notebooklm_url else None
        self.personas = PersonaLibrary(persona_dir)
        self.skills = SkillRouter()
        self.backend = backend or LocalRulesBackend()
        backend_name = getattr(self.backend, "name", None)
        if not isinstance(backend_name, str) or not backend_name.strip():
            raise ValueError("judge backend must expose a non-empty `name`")
        self.engine_manager = EngineManager(
            quota_file=quota_file,
            quota_json=quota_json,
            default_provider=backend_name,
        )

    @staticmethod
    def _normalize_hardness(hardness: str | HardnessLevel) -> HardnessLevel:
        if isinstance(hardness, HardnessLevel):
            return hardness
        try:
            return HardnessLevel(str(hardness).lower())
        except ValueError as error:
            allowed = ", ".join(item.value for item in HardnessLevel)
            raise ValueError(f"hardness must be one of: {allowed}") from error

    def judge(self, target: str, requested_personas: Iterable[str] | None = None) -> VerdictReport:
        if not isinstance(target, str) or not target.strip():
            raise ValueError("target must be a non-empty string")
        normalized_target = target.strip()
        if len(normalized_target) > MAX_TARGET_LENGTH:
            raise ValueError(f"target must be <= {MAX_TARGET_LENGTH} characters")
        requested_names = list(requested_personas) if requested_personas is not None else None
        panels: list[list[Persona]] = []
        for round_index in range(1, self.rounds + 1):
            panel = self.personas.select(
                self.tribunal_type,
                f"{normalized_target} round {round_index}",
                requested_names,
                offset=(round_index - 1) * 3,
            )
            if len({persona.slug for persona in panel}) != 3:
                raise RuntimeError(f"round {round_index} did not produce three unique personas")
            panels.append(panel)

        views: list[JudgeView] = []
        engine_plan = self.engine_manager.allocate(self.rounds * 3)
        allocation_index = 0
        for round_index, panel in enumerate(panels, start=1):
            round_views: list[JudgeView] = []
            for judge_index, persona in enumerate(panel, start=1):
                allocation = engine_plan[allocation_index]
                allocation_index += 1
                round_views.append(
                    self._evaluate(normalized_target, round_index, judge_index, persona, allocation)
                )
            views.extend(round_views)

        debate = self._debate(views)
        final_score = round(sum(view.score for view in views) / len(views))
        crown = (
            "👑"
            if self.tribunal_type == TribunalType.COMPARISON and final_score >= 80
            else ("✅" if final_score >= 80 else "⚠️")
        )
        verdict = (
            f"{crown} Tribunal score {final_score}/100 from backend `{self.backend.name}`. "
            f"{len(views)} judge views across {self.rounds} independent round(s). "
            "The score is bounded by the recorded evidence and all missing proof remains flagged."
        )
        return VerdictReport(
            target=normalized_target,
            mode=self.tribunal_type.value,
            rounds=self.rounds,
            requested_rounds=self.requested_rounds,
            hardness=self.hardness.value,
            notebooklm_url=self.notebooklm_url,
            engine_plan=engine_plan,
            judge_views=views,
            debate=debate,
            final_verdict=verdict,
            final_score=final_score,
            crown=crown,
        )

    def _evaluate(
        self,
        target: str,
        round_index: int,
        judge_index: int,
        persona: Persona,
        allocation: EngineAllocation,
    ) -> JudgeView:
        routed = self.skills.route(persona, self.tribunal_type, self.notebooklm_url)
        request = JudgeRequest(
            target=target,
            mode=self.tribunal_type,
            round_index=round_index,
            judge_index=judge_index,
            persona=persona,
            routed_skills=routed,
            notebooklm_url=self.notebooklm_url,
        )
        result = validate_backend_result(self.backend.evaluate(request), self.backend.name)
        evidence = [
            *result.evidence,
            f"Persona route reason: {self._persona_reason(persona)}",
            f"Engine `{allocation.provider}` came from `{allocation.source}`.",
            f"Hardness `{self.hardness.value}` produced {self.rounds} effective round(s) from {self.requested_rounds} requested.",
        ]
        return JudgeView(
            round_index=round_index,
            judge_index=judge_index,
            persona_slug=persona.slug,
            persona=persona.name,
            role=persona.role,
            backend=self.backend.name,
            engine=allocation.provider,
            engine_source=allocation.source,
            engine_capacity_before=allocation.capacity_before,
            routed_skills=routed,
            verdict=result.verdict,
            score=result.score,
            findings=result.findings,
            evidence=evidence,
            evidence_gaps=result.evidence_gaps,
        )

    def _persona_reason(self, persona: Persona) -> str:
        role = persona.role.lower()
        skills = " ".join(persona.skills).lower()
        if self.tribunal_type == TribunalType.UI_UX and (
            "ui" in role
            or "ux" in role
            or "workflow" in role
            or "ergonomics" in role
            or "design" in skills
            or "accessibility" in skills
        ):
            return "UI/UX mode needs interface, workflow, accessibility, or visual-design pressure."
        if self.tribunal_type == TribunalType.KNOWLEDGE and (
            "fact" in role or "research" in role or "knowledge" in skills or "web-search" in skills
        ):
            return "Knowledge mode needs fact-checking, primary-source review, and citation skepticism."
        if self.tribunal_type == TribunalType.CRITIQUE and (
            "architect" in role or "audit" in role or "karpathy" in skills
        ):
            return "Critique mode needs architectural teardown, evidence integrity, and hard technical skepticism."
        if self.tribunal_type == TribunalType.COMPARISON:
            return "Comparison mode needs tradeoff analysis, evidence checks, and one explicit winner."
        return "Selected as an independent adversarial judge to avoid a single-perspective verdict."

    @staticmethod
    def _debate(views: list[JudgeView]) -> DebateSummary:
        gap_counts: dict[str, int] = {}
        for view in views:
            for gap in view.evidence_gaps:
                gap_counts[gap] = gap_counts.get(gap, 0) + 1
        recurring = [gap for gap, count in gap_counts.items() if count > 1]
        scores = [view.score for view in views]
        disagreements = [
            f"Judge scores span {min(scores)}-{max(scores)} across persona-specific lenses."
        ]
        persona_lenses = [f"{view.persona_slug}: {view.findings[0]}" for view in views[:3]]
        disagreements.extend(persona_lenses)
        strongest: list[str] = []
        for view in sorted(views, key=lambda item: item.score, reverse=True):
            for finding in view.findings:
                if finding not in strongest:
                    strongest.append(finding)
                if len(strongest) == 3:
                    break
            if len(strongest) == 3:
                break
        return DebateSummary(
            kind="post-hoc-synthesis",
            recurring_failures=recurring or ["No evidence gap recurred across judge views."],
            disagreements=disagreements,
            strongest_points=strongest,
        )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a local Tribunal verdict.")
    parser.add_argument(
        "--mode",
        choices=[item.value for item in TribunalType],
        default=TribunalType.CRITIQUE.value,
        help="Tribunal type (default: critique).",
    )
    parser.add_argument(
        "--rounds",
        type=int,
        default=1,
        help=f"Requested Nx rounds, from 1 through {MAX_ROUNDS} (default: 1).",
    )
    parser.add_argument(
        "--hardness",
        choices=[item.value for item in HardnessLevel],
        default=HardnessLevel.STANDARD.value,
        help="Minimum pressure: light/standard=1, hard=2, brutal=4 rounds.",
    )
    parser.add_argument(
        "--target",
        required=True,
        help=f"Text or reference to review (maximum {MAX_TARGET_LENGTH} characters).",
    )
    parser.add_argument("--personas", default="", help="Comma-separated persona slugs.")
    parser.add_argument(
        "--quota-file",
        default=None,
        help="JSON file mapping engine names to per-run judge-slot capacities.",
    )
    parser.add_argument(
        "--notebooklm-url",
        default=None,
        help="Canonical https://notebooklm.google.com/notebook/<id> reference.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown.")
    return parser


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    return _build_parser().parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    requested = [item.strip() for item in args.personas.split(",") if item.strip()] or None
    try:
        orchestrator = TribunalOrchestrator(
            TribunalType(args.mode),
            rounds=args.rounds,
            hardness=args.hardness,
            quota_file=args.quota_file,
            notebooklm_url=args.notebooklm_url,
        )
        report = orchestrator.judge(args.target, requested_personas=requested)
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        print(f"tribunal: error: {error}", file=sys.stderr)
        return 2
    print(report.to_json() if args.json else report.to_markdown())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
