import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tribunal import (
    BackendResult,
    EngineManager,
    HardnessLevel,
    JudgeRequest,
    MAX_ROUNDS,
    MAX_TARGET_LENGTH,
    TribunalOrchestrator,
    TribunalType,
)


class RecordingBackend:
    name = "recording-live-backend"

    def __init__(self, score: int = 81, evidence_gaps: list[str] | None = None):
        self.score = score
        self.evidence_gaps = list(evidence_gaps or [])
        self.requests: list[JudgeRequest] = []

    def evaluate(self, request: JudgeRequest) -> BackendResult:
        self.requests.append(request)
        return BackendResult(
            verdict=f"{request.persona.slug} verdict",
            score=self.score,
            findings=[f"finding from {request.persona.slug}"],
            evidence=[f"evidence for R{request.round_index}J{request.judge_index}"],
            evidence_gaps=list(self.evidence_gaps),
        )


class MixedScoreBackend:
    name = "mixed-score-live-backend"

    def evaluate(self, request: JudgeRequest) -> BackendResult:
        score = 70 if request.judge_index == 1 else 85
        return BackendResult(
            verdict=f"{request.persona.slug} verdict",
            score=score,
            findings=[f"finding from {request.persona.slug}"],
            evidence=[f"evidence for R{request.round_index}J{request.judge_index}"],
            evidence_gaps=[],
        )


class MarkupBackend:
    name = "markup-live-backend"

    def evaluate(self, request: JudgeRequest) -> BackendResult:
        return BackendResult(
            verdict="<script>verdict</script>\nsecond line",
            score=90,
            findings=["<b>finding</b>"],
            evidence=["<img src=x onerror=alert(1)>"],
            evidence_gaps=[],
        )


class InvalidBackend:
    name = "invalid-backend"

    def evaluate(self, request: JudgeRequest) -> BackendResult:
        return BackendResult("invalid", 101, ["finding"], ["evidence"], ["gap"])


class TribunalContractTests(unittest.TestCase):
    def test_all_primary_modes_emit_three_views(self) -> None:
        for mode in (TribunalType.KNOWLEDGE, TribunalType.CRITIQUE, TribunalType.UI_UX):
            with self.subTest(mode=mode):
                report = TribunalOrchestrator(mode).judge("contract target")
                self.assertEqual(report.mode, mode.value)
                self.assertEqual(len(report.judge_views), 3)
                self.assertEqual(len({view.persona_slug for view in report.judge_views}), 3)

    def test_hardness_expands_effective_rounds(self) -> None:
        hard = TribunalOrchestrator(TribunalType.CRITIQUE, rounds=1, hardness="hard").judge(
            "hard target"
        )
        brutal = TribunalOrchestrator(
            TribunalType.CRITIQUE,
            rounds=1,
            hardness=HardnessLevel.BRUTAL,
        ).judge("brutal target")
        self.assertEqual((hard.requested_rounds, hard.rounds, len(hard.judge_views)), (1, 2, 6))
        self.assertEqual(
            (brutal.requested_rounds, brutal.rounds, len(brutal.judge_views)),
            (1, 4, 12),
        )

    def test_backend_is_invoked_once_per_isolated_judge(self) -> None:
        backend = RecordingBackend()
        report = TribunalOrchestrator(
            TribunalType.COMPARISON,
            rounds=2,
            backend=backend,
        ).judge("comparison target")
        self.assertEqual(len(backend.requests), 6)
        self.assertEqual(
            [(request.round_index, request.judge_index) for request in backend.requests],
            [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3)],
        )
        self.assertTrue(all(view.backend == backend.name for view in report.judge_views))
        self.assertEqual(report.final_score, 81)
        self.assertEqual(report.crown, "👑")

    def test_positive_markers_require_unanimous_gap_free_views(self) -> None:
        gapped = TribunalOrchestrator(
            TribunalType.COMPARISON,
            backend=RecordingBackend(score=95, evidence_gaps=["unresolved proof"]),
        ).judge("gapped comparison")
        mixed = TribunalOrchestrator(
            TribunalType.COMPARISON,
            backend=MixedScoreBackend(),
        ).judge("mixed comparison")
        self.assertEqual((gapped.final_score, gapped.crown), (95, "⚠️"))
        self.assertEqual((mixed.final_score, mixed.crown), (80, "⚠️"))

        gapped_knowledge = TribunalOrchestrator(
            TribunalType.KNOWLEDGE,
            backend=RecordingBackend(score=95, evidence_gaps=["unresolved proof"]),
        ).judge("gapped knowledge review")
        mixed_critique = TribunalOrchestrator(
            TribunalType.CRITIQUE,
            backend=MixedScoreBackend(),
        ).judge("mixed critique review")
        gap_free_ux = TribunalOrchestrator(
            TribunalType.UI_UX,
            backend=RecordingBackend(score=81),
        ).judge("gap-free UX review")
        self.assertEqual((gapped_knowledge.final_score, gapped_knowledge.crown), (95, "⚠️"))
        self.assertEqual((mixed_critique.final_score, mixed_critique.crown), (80, "⚠️"))
        self.assertEqual((gap_free_ux.final_score, gap_free_ux.crown), (81, "✅"))

    def test_ui_first_panel_contains_only_ui_ux_personas(self) -> None:
        report = TribunalOrchestrator(TribunalType.UI_UX).judge("operator dashboard")
        expected = {
            "ux-operator-flow",
            "ux-specialist",
            "ux-researcher",
            "ui-specialist",
            "ui-minimalist",
        }
        self.assertTrue({view.persona_slug for view in report.judge_views}.issubset(expected))

    def test_local_backend_has_honest_provenance_and_gaps(self) -> None:
        report = TribunalOrchestrator(TribunalType.KNOWLEDGE).judge("plain claim")
        self.assertTrue(all(view.backend == "local-rules" for view in report.judge_views))
        self.assertTrue(all(view.engine == "local-rules" for view in report.judge_views))
        self.assertTrue(all(view.engine_source == "builtin-local" for view in report.judge_views))
        self.assertTrue(all(view.engine_capacity_before is None for view in report.judge_views))
        self.assertTrue(
            all("not evaluated" in view.evidence_gaps[0] for view in report.judge_views)
        )

    def test_notebooklm_url_is_strictly_validated(self) -> None:
        invalid = (
            "http://notebooklm.google.com/notebook/id",
            "https://example.com/notebook/id",
            "https://notebooklm.google.com/other/id",
            "https://notebooklm.google.com/notebook",
        )
        for url in invalid:
            with self.subTest(url=url), self.assertRaisesRegex(ValueError, "NotebookLM URL"):
                TribunalOrchestrator(TribunalType.KNOWLEDGE, notebooklm_url=url)
        valid = "https://notebooklm.google.com/notebook/1234-abcd"
        report = TribunalOrchestrator(
            TribunalType.KNOWLEDGE,
            notebooklm_url=valid,
        ).judge("source-backed setup")
        self.assertEqual(report.notebooklm_url, valid)
        self.assertTrue(
            all("content was not queried" in view.evidence_gaps[1] for view in report.judge_views)
        )

    def test_requested_personas_are_validated_and_reusable_across_rounds(self) -> None:
        requested = (slug for slug in ("knowledge-analyst", "security-auditor", "systems-architect"))
        report = TribunalOrchestrator(TribunalType.KNOWLEDGE, rounds=2).judge(
            "target",
            requested_personas=requested,
        )
        self.assertEqual(len(report.judge_views), 6)
        with self.assertRaisesRegex(ValueError, "unknown requested persona"):
            TribunalOrchestrator(TribunalType.KNOWLEDGE).judge(
                "target",
                requested_personas=["missing", "security-auditor", "systems-architect"],
            )

    def test_invalid_persona_document_names_path_and_field(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "broken.json"
            path.write_text(
                json.dumps(
                    {
                        "name": "Broken",
                        "stance": "strict",
                        "instructions": "inspect",
                        "skills": ["audit"],
                        "reference_repos": ["https://github.com/example/example"],
                    }
                )
            )
            with self.assertRaisesRegex(ValueError, r"broken\.json.*`role`"):
                TribunalOrchestrator(TribunalType.CRITIQUE, persona_dir=Path(directory))

    def test_explicit_engine_capacity_is_bounded_per_run_and_reusable(self) -> None:
        manager = EngineManager(quota_json='{"alpha": 2, "beta": 1}')
        first = manager.allocate(3)
        second = manager.allocate(3)
        self.assertEqual(first, second)
        self.assertEqual([item.capacity_before for item in first], [2, 1, 1])
        self.assertTrue(all(item.source == "env:TRIBUNAL_ENGINE_QUOTAS_JSON" for item in first))
        with self.assertRaisesRegex(RuntimeError, "capacity exhausted"):
            manager.allocate(4)

        backend = RecordingBackend()
        orchestrator = TribunalOrchestrator(
            TribunalType.KNOWLEDGE,
            backend=backend,
            quota_json='{"alpha": 3}',
        )
        first_report = orchestrator.judge("first target")
        second_report = orchestrator.judge("second target")
        self.assertEqual(
            [item.capacity_before for item in first_report.engine_plan],
            [3, 2, 1],
        )
        self.assertEqual(first_report.engine_plan, second_report.engine_plan)

    def test_invalid_capacity_and_backend_result_fail_closed(self) -> None:
        for raw in ('{}', '{"alpha": -1}', '{"alpha": true}', '{"alpha": "1"}'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                EngineManager(quota_json=raw)
        with self.assertRaisesRegex(ValueError, "score must be"):
            TribunalOrchestrator(
                TribunalType.CRITIQUE,
                backend=InvalidBackend(),
            ).judge("target")

    def test_json_and_markdown_preserve_provenance(self) -> None:
        report = TribunalOrchestrator(TribunalType.CRITIQUE).judge("serialize me")
        payload = json.loads(report.to_json())
        markdown = report.to_markdown()
        self.assertEqual(payload["final_score"], report.final_score)
        self.assertEqual(payload["judge_views"][0]["persona_slug"], report.judge_views[0].persona_slug)
        self.assertIn("- Backend: `local-rules`", markdown)
        self.assertIn(f"- Final score: `{report.final_score}/100`", markdown)
        self.assertEqual(payload["debate"]["kind"], "post-hoc-synthesis")
        self.assertIn("## Post-hoc Synthesis", markdown)
        self.assertIn("not an interactive agent debate", markdown)
        self.assertIn("isolated judge views", report.final_verdict)
        self.assertNotIn("independent round", report.final_verdict)

    def test_backend_markdown_is_escaped_without_mutating_json(self) -> None:
        report = TribunalOrchestrator(
            TribunalType.COMPARISON,
            backend=MarkupBackend(),
        ).judge("markup target")
        markdown = report.to_markdown()
        payload = report.to_dict()
        self.assertNotIn("<script>", markdown)
        self.assertNotIn("<b>", markdown)
        self.assertNotIn("<img", markdown)
        self.assertIn("&lt;script&gt;verdict&lt;/script&gt; second line", markdown)
        self.assertEqual(payload["judge_views"][0]["verdict"], "<script>verdict</script>\nsecond line")

    def test_brutal_synthesis_and_critique_provenance_cover_every_view(self) -> None:
        report = TribunalOrchestrator(
            TribunalType.CRITIQUE,
            hardness=HardnessLevel.BRUTAL,
        ).judge("hardening target")
        self.assertEqual(len(report.judge_views), 12)
        self.assertEqual(len(report.debate.disagreements), 13)
        security_view = next(
            view for view in report.judge_views if view.persona_slug == "security-auditor"
        )
        self.assertTrue(
            any(
                "Critique mode needs architectural teardown" in item
                for item in security_view.evidence
            )
        )

    def test_persona_disclaimer_and_repository_urls_survive_loading(self) -> None:
        orchestrator = TribunalOrchestrator(TribunalType.CRITIQUE)
        persona = orchestrator.personas.personas["andrej-karpathy"]
        self.assertIn("neither authored nor endorsed", persona.disclaimer or "")
        for loaded in orchestrator.personas.personas.values():
            self.assertTrue(
                all(url.startswith("https://github.com/") for url in loaded.reference_repos)
            )

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "invalid-reference.json"
            path.write_text(
                json.dumps(
                    {
                        "name": "Invalid Reference",
                        "role": "Reviewer",
                        "stance": "strict",
                        "instructions": "inspect",
                        "skills": ["audit"],
                        "reference_repos": ["owner/repository"],
                    }
                )
            )
            with self.assertRaisesRegex(ValueError, r"invalid-reference\.json.*reference_repos"):
                TribunalOrchestrator(TribunalType.CRITIQUE, persona_dir=Path(directory))

    def test_round_target_bounds_and_markdown_target_escaping(self) -> None:
        with self.assertRaisesRegex(ValueError, f"rounds must be <= {MAX_ROUNDS}"):
            TribunalOrchestrator(TribunalType.CRITIQUE, rounds=MAX_ROUNDS + 1)
        orchestrator = TribunalOrchestrator(TribunalType.CRITIQUE)
        with self.assertRaisesRegex(ValueError, f"target must be <= {MAX_TARGET_LENGTH}"):
            orchestrator.judge("x" * (MAX_TARGET_LENGTH + 1))

        target = "<script>alert('x')</script> & evidence"
        report = orchestrator.judge(target)
        self.assertEqual(report.to_dict()["target"], target)
        self.assertIn("&lt;script&gt;alert('x')&lt;/script&gt; &amp; evidence", report.to_markdown())
        self.assertNotIn("<script>", report.to_markdown())

    def test_local_score_is_a_documented_structural_ceiling(self) -> None:
        without_notebook = TribunalOrchestrator(TribunalType.KNOWLEDGE).judge("target")
        with_notebook = TribunalOrchestrator(
            TribunalType.KNOWLEDGE,
            notebooklm_url="https://notebooklm.google.com/notebook/1234-abcd",
        ).judge("target")
        self.assertEqual(without_notebook.final_score, 40)
        self.assertEqual(with_notebook.final_score, 50)
        self.assertTrue(
            all("Structural score" in " ".join(view.evidence) for view in without_notebook.judge_views)
        )

    def test_cli_help_and_input_errors_are_operator_friendly(self) -> None:
        root = Path(__file__).resolve().parents[1]
        help_result = subprocess.run(
            [sys.executable, str(root / "tribunal.py"), "--help"],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(help_result.returncode, 0)
        for flag in (
            "--mode",
            "--rounds",
            "--hardness",
            "--target",
            "--personas",
            "--quota-file",
            "--notebooklm-url",
            "--json",
        ):
            self.assertIn(flag, help_result.stdout)

        error_result = subprocess.run(
            [
                sys.executable,
                str(root / "tribunal.py"),
                "--target",
                "bad notebook reference",
                "--notebooklm-url",
                "https://example.com/notebook/id",
            ],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(error_result.returncode, 2)
        self.assertIn("tribunal: error: NotebookLM URL", error_result.stderr)
        self.assertNotIn("Traceback", error_result.stderr)


if __name__ == "__main__":
    unittest.main()
