# Frozen conclusion-free packet for brief live judges

Frozen UTC: `2026-07-20T20:52:00Z`  
Repository starting snapshot: `2c27f51bfa33e75c4bbc73f82bd535d6638d4f56`

This packet contains observed inputs and declared boundaries only. It deliberately omits all historical judge prose, every role score, rank/crown conclusions, synthesis, and final recommendation. Judges MUST NOT inspect `report/codex-trib-lib-tribunal.md` or any file with `judge`, `external-attempt`, or `synthesis` in its name. The three role sessions receive this same packet before any new role output is written.

## Assignment

Independently audit the public Codex Tribunal Python library and reusable skill for exactly one assigned perspective: knowledge/correctness, hard criticism/risk, or CLI/UI-UX implementation feasibility. The declared surface includes three primary review modes, an additional comparison mode, a disclosed synthetic Karpathy-inspired critic, structured evidence gaps and provenance, NotebookLM research provenance, an OSS-first comparison contract, and installable CLI/API paths.

## Permitted local surfaces

- `tribunal.py`, `README.md`, `skill/SKILL.md`, `personas/*.json`, `personas/__init__.py`, and `pyproject.toml`.
- `examples/*.py`, `tests/test_tribunal.py`, and `scripts/*.py`.
- `openspec/changes/complete-live-codex-tribunal-library-brief/` except task marks after this freeze.
- `report/evidence/brief-live-baseline.md`, `brief-live-notebooklm.md`, `brief-live-oss.md`, and `github-snapshot.json` as evidence claims to challenge.
- `report/codex-trib-lib-matrix.csv` as a structured scoring input; do not inherit its rank or crown as your conclusion.

No other report/evidence file is permitted. Do not inspect Git history for prior verdicts.

## Current runtime contract to verify

- Public modes are `knowledge`, `critique`, `ui_ux`, and additional `comparison`.
- Each round selects three distinct persona slugs and creates three separate `JudgeBackend.evaluate(JudgeRequest)` calls before `post-hoc-synthesis`.
- Separate calls and personas establish request isolation only, not provider-memory isolation, model-family diversity, statistical independence, factual correctness, or interactive debate.
- The bundled `local-rules` backend is deterministic structural readiness only. It is capped at `40/100` without a syntactically valid NotebookLM URL and `50/100` with one; it does not fetch the URL, inspect target semantics, or render pixels.
- A positive runtime marker requires every view to score at least 80 and return no backend-declared evidence gap. Empty declared gaps are not independently verified truth.
- Hardness minimums are one, one, two, and four effective rounds for light, standard, hard, and brutal. Nine bundled personas repeat after three complete rounds; an explicit three-person panel repeats every round.
- JSON and Markdown carry persona/backend/engine/source provenance, findings, evidence, gaps, scores, post-hoc synthesis, and marker. Markdown normalizes untrusted text; JSON is lossless.
- The Karpathy-inspired critic cites `llama2.c`, `minGPT`, and `micrograd`, is explicitly synthetic and unendorsed, and carries a serialized disclaimer. Never attribute generated output to Andrej Karpathy.
- Routed skill names are host declarations. The Python core records but does not discover, validate installation of, or invoke external Codex skills.
- Capacity integers are per-run judge slots, not tokens, live quota discovery, billing controls, or durable cross-run budgets.
- No live provider, cross-family policy, browser/TUI, persistent traces, durable workflow store, visual accessibility runner, or prompt-injection defense is bundled or claimed.

## Direct controls completed before freeze

- `python -m py_compile tribunal.py personas/__init__.py` exited `0`.
- Import observed a callable `LocalRulesBackend.evaluate` and `9` loadable personas.
- Exact source shows target/backend Markdown neutralization and active GitHub reference validation.
- The existing wheel contains `personas/__init__.py` and all nine JSON personas.

These narrow controls disprove source-normalization artifacts; they do not replace the later full tests, fresh build, clean install, CLI modes, invalid-input check, or installed API proof.

## Authenticated NotebookLM facts

- Canonical notebook: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515
- Authenticated `nlm 0.8.9`; exact title `Tribunal IDR 2026-07-04`; public link enabled.
- Final direct inventory after thirteen selected additions: `560` total, `549` processed, `11` failed inherited secondary/duplicate pages.
- Four fresh role/control queries returned source-ID/citation-mapping counts `12/49`, `10/28`, `10/37`, and `8/31`.
- Generated prose falsely inferred a Python syntax error, missing persona package data, missing backend method, dead URL validator, and Pydantic dependency from normalized excerpts. Direct compile/import/symbol/wheel controls contradicted those claims.
- Generated prose also reused historical provider facts, mutable stars, and literature metrics despite explicit freshness constraints. Current direct/executable and primary metadata outrank generated characterization.

## Primary OSS facts

The primary snapshot completed at `2026-07-20T20:51:06Z` for eleven canonical, active, non-archived repositories: Codex Tribunal, promptfoo, Microsoft Agent Framework, DeepEval, AutoGen, Ragas, OpenAI Evals, Langfuse, DSPy, Phoenix, and lm-evaluation-harness. Numeric stars are dated adoption context and contribute zero points. Primary license qualifications include AutoGen CC-BY-4.0 plus maintenance status, OpenAI Evals dataset exceptions, Langfuse enterprise-directory exceptions, and Phoenix ELv2 hosted-service restrictions.

## Common 100-point rubric

- Type Fit: 25
- Adversarial Depth: 20
- Evidence Provenance: 20
- Persona/Skill Extensibility: 15
- Observability/Repeatability: 10
- Integration Cost: 10

Every component MUST be an integer within its weight and the checked total MUST equal their sum. Stars provide no points. A deterministic-gate failure, fabricated provenance, hidden category mismatch, or total below 70 vetoes an unconditional positive recommendation.

## Required independent output

Return self-contained Markdown containing:

1. assigned perspective and exact inspected scope;
2. severity-ordered findings with concrete local file/source references;
3. all six component scores and a checked total out of 100;
4. evidence actually inspected;
5. explicit evidence gaps and unsupported claims;
6. exactly one recommendation: `Ship`, `Block`, or `Ship with conditions`, followed by prioritized actions;
7. the exact sentence `I did not inspect any other brief-live judge output.`

Do not edit files. Do not inspect forbidden conclusion artifacts. Do not expose hidden chain-of-thought; provide concise auditable rationale only.
