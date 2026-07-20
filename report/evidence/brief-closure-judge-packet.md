# Frozen conclusion-free packet for brief-closure judges

- Frozen UTC: `2026-07-20T20:51:09Z`
- Repository base: `2c27f51bfa33e75c4bbc73f82bd535d6638d4f56`
- Public repository: https://github.com/Martin-Hausleitner/tribunal-public
- Canonical NotebookLM: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515

This packet contains scope, reproducible observations, and disclosed limits only. It deliberately omits prior and sibling judge prose, role scores, rank/crown decisions, final recommendations, and synthesis. Do not inspect `report/codex-trib-lib-tribunal.md`, any file whose name contains `judge-knowledge`, `judge-critique`, `judge-ux`, `external-attempts`, or `synthesis`, or another active judge process.

## Assignment

Independently audit this public MIT-licensed Codex Tribunal Python library and reusable skill for exactly one assigned perspective: knowledge/correctness, harsh criticism/risk, or CLI/UI/UX implementation feasibility. The declared release surface is a dependency-free local orchestration contract with three primary review modes, an additional comparison mode, isolated initial persona calls, explicit evidence gaps, a disclosed Karpathy-inspired synthetic persona, stable Markdown/JSON, a CLI/API/wheel path, and an OSS-first composition recommendation.

## Permitted project surfaces

- `tribunal.py`, `README.md`, `pyproject.toml`, `LICENSE`, `skill/SKILL.md`, and `personas/*.json`.
- `examples/*.py`, `tests/test_tribunal.py`, and `scripts/*.py`.
- `openspec/changes/complete-live-codex-tribunal-library-brief/` except task completion marks written after this freeze.
- `report/evidence/brief-live-notebooklm.md`, `report/evidence/brief-closure-baseline.md`, and structured `report/evidence/github-snapshot.json` / `report/codex-trib-lib-matrix.csv` as inputs to challenge, never conclusions to inherit.

## Directly observed runtime boundaries

- Public modes are `knowledge`, `critique`, `ui_ux`, and additional `comparison`.
- Each round selects three distinct persona slugs and calls `JudgeBackend.evaluate` separately for each view before a post-hoc synthesis. This proves separate calls and initial payload separation only, not distinct processes, provider memory isolation, model-family diversity, statistical independence, factual correctness, or interactive debate.
- `LocalRulesBackend.evaluate` exists. The standard-library local backend inspects orchestration structure rather than target semantics. Its ceiling is `40/100` without a NotebookLM reference and `50/100` with one, with evidence gaps remaining visible.
- Positive markers require every judge score to be at least 80 and every backend-declared evidence-gap list to be empty. An empty list remains a backend assertion, not independently verified truth.
- `_markdown_text` escapes the target before Markdown output; `python -m py_compile` passed at freeze. No current syntax or missing-backend-method defect is established.
- Nine JSON personas and `personas/__init__.py` are packaged. The Karpathy-inspired persona references three public repositories and serializes an explicit non-authorship/non-endorsement disclaimer.
- Routed skills are host-facing labels. The local core does not discover or execute installed Codex skills.
- Engine capacities are explicit per-run judge slots, not tokens, billing promises, provider discovery, or durable cross-run quotas.
- The repository claims no live provider, live NotebookLM client, browser/TUI, visual accessibility proof, checkpoint store, durable trace database, cross-family router, or prompt-injection defense.

## Live NotebookLM boundary

- Authenticated `nlm 0.8.9` resolved the canonical notebook and public link.
- The directly observed final inventory at packet freeze was `560` sources: `549` processed and `11` inherited failed duplicate/secondary sources.
- Current role queries and contradiction controls repeatedly hallucinated fatal syntax, missing backend, missing package data, Pydantic, and checkpoint behavior. Direct compilation, source search, import, and package layout contradicted those claims.
- NotebookLM supports the thin structural contract and OSS composition direction, but its prose is research synthesis rather than executable proof.

## Common 100-point rubric

- Type Fit: 25
- Adversarial Depth: 20
- Evidence Provenance: 20
- Persona/Skill Extensibility: 15
- Observability/Repeatability: 10
- Integration Cost: 10

A component cannot exceed its weight. Stars are dated adoption context and contribute zero points. A deterministic-gate failure, fabricated provenance, hidden category mismatch, or total below 70 vetoes an unconditional positive recommendation.

## Required independent output

Return self-contained Markdown containing:

1. assigned perspective and inspected scope;
2. severity-ordered findings with concrete file/source references;
3. all six component scores and a checked total out of 100;
4. evidence actually inspected;
5. explicit evidence gaps and unsupported claims;
6. `Ship`, `Block`, or `Ship with conditions`, followed by prioritized actions;
7. the exact sentence `I did not inspect any other brief-closure judge output.`

Do not edit files. Do not expose hidden chain-of-thought; provide concise, auditable rationale only.
