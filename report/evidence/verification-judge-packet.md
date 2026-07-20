# Frozen conclusion-free packet for verification judges

Frozen from tracked repository HEAD `56450e401a5c134629c3c3f1bd467418a9b4145d` after the NotebookLM and primary GitHub evidence was collected. This packet contains observations, contracts, and open questions only. It deliberately omits prior judge prose, role scores, synthesized verdicts, and the final recommendation.

The three fresh role sessions receive this same packet. They MUST NOT inspect `report/codex-trib-lib-tribunal.md`, any file with `judge`, `external-attempt`, or `synthesis` in its name other than this packet, Git history for prior verdicts, or another role's output.

## Assignment

Independently audit the Codex Tribunal Python library and reusable skill from exactly one assigned perspective: knowledge/correctness, harsh criticism/risk, or CLI UX/implementability. Assess the bounded local contract and the evidence needed to release it; do not treat a local structural pass, NotebookLM citation, matrix score, or model opinion as semantic truth.

## Permitted local surfaces

- `tribunal.py`, `README.md`, `skill/SKILL.md`, `personas/*.json`, and `personas/__init__.py`.
- `examples/*.py`, `tests/test_tribunal.py`, and `scripts/*.py`.
- The committed `pyproject.toml` at HEAD, obtainable read-only as `git show 56450e401a5c134629c3c3f1bd467418a9b4145d:pyproject.toml`. A separate unowned worktree edit to that file is outside this packet and MUST be ignored.
- `openspec/changes/verify-complete-codex-tribunal-library-brief/` except task marks after this freeze.
- `report/evidence/verification-baseline.md`, `verification-notebooklm.md`, `verification-direct-controls.md`, `verification-oss.md`, and `github-snapshot.json` as evidence claims to challenge.
- `report/codex-trib-lib-matrix.csv` as a scoring input. Do not inherit its rank, total, or crown as your conclusion.

No other report/evidence file is permitted.

## Runtime contract to verify

- Public modes are `knowledge`, `critique`, `ui_ux`, and additional `comparison`.
- Each round selects three distinct persona slugs and sends three separate immutable `JudgeRequest` values through three `JudgeBackend.evaluate` calls before post-hoc synthesis.
- Separate calls/personas establish request isolation only. They do not establish provider-memory isolation, family diversity, statistical independence, factual correctness, or interactive debate.
- The default `local-rules` backend is deterministic structural readiness only. It yields 40/100 without a notebook reference and 50/100 with a syntactically valid one; it does not retrieve the URL, inspect target semantics, render pixels, or award a runtime crown.
- A positive runtime marker requires every view to score at least 80 and return no backend-declared evidence gap. A custom backend self-declares its score and gap list; the core validates shape, not truth.
- Hardness minimums are one, one, two, and four effective rounds for light, standard, hard, and brutal. Nine bundled personas repeat after three complete rounds; an explicit three-person panel repeats every round.
- JSON and Markdown carry mode/round/persona/skill/backend/engine/source provenance, findings, evidence, gaps, scores, post-hoc synthesis, and marker. Markdown normalizes and escapes untrusted natural-language values; JSON preserves them.
- The Karpathy-inspired critic cites `llama2.c`, `minGPT`, and `micrograd`, is explicitly synthetic and unendorsed, and carries a serialized disclaimer. Generated conclusions must never be attributed to Andrej Karpathy.
- Routed skill names are host declarations. The core records labels but does not discover, install, validate, or execute external Codex skills.
- Capacity integers are per-run judge slots, not tokens, provider quota discovery, billing controls, or durable cross-run budgets.
- No live-provider adapter, cross-family policy, browser/TUI, persistent trace store, durable workflow runtime, visual accessibility runner, or prompt-injection defense is bundled or claimed.

## Direct pre-freeze controls

- `python -m py_compile tribunal.py tests/test_tribunal.py personas/__init__.py` exited `0`.
- Import observed a callable `LocalRulesBackend.evaluate`, all four allegedly missing private/public methods, and nine loadable personas.
- Exact source contained separate imports, valid string escapes, a literal-backtick regex, and a non-empty adaptive Markdown delimiter.
- Rendering a value with Markdown markers escaped those markers; rendering a value with three backticks used a four-backtick delimiter.

These controls reject NotebookLM normalization artifacts. They do not replace the required unit suite, fresh build, exact-wheel install, source/installed CLI/API exercise, invalid-input path, or final gates.

## Authenticated NotebookLM observations

- Canonical public notebook: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515, title `Tribunal IDR 2026-07-04`, authenticated with `nlm 0.8.9`.
- The shared global inventory changed from `640/598/42` total/processed/failed to `669/600/69` while concurrent unowned work ran. Queries used explicit processed source IDs so those unrelated changes could not silently enter grounding.
- Two current-pass OpenSpec sources were added and processed; two file additions were rejected and one text source failed after initial acceptance. Failed sources were excluded.
- The accepted role/control queries returned source/citation counts `17/72`, `6/22`, `11/40`, and `6/23`. A default-conversation attempt with `0/0` grounding was rejected.
- Knowledge, critique, and UX answers independently invented fatal syntax/import/regex/delimiter/missing-method failures from normalized code. The fourth query corrected them only after receiving the direct executable controls.
- Processed status and citation mappings establish provenance, not correctness. Primary source and executable behavior control conflicts.

## Primary OSS observations

The primary snapshot completed at `2026-07-20T22:17:14Z` for eleven canonical, active, non-archived repositories. Numeric stars are dated adoption context and contribute zero rubric points. Primary qualifications include AutoGen CC-BY-4.0 plus maintenance mode and Microsoft Agent Framework migration guidance, OpenAI Evals dataset exceptions, Langfuse enterprise-directory exceptions, and Phoenix ELv2 hosted-service restrictions.

## Common 100-point rubric

- Type Fit: 25
- Adversarial Depth: 20
- Evidence Provenance: 20
- Persona/Skill Extensibility: 15
- Observability/Repeatability: 10
- Integration Cost: 10

Each component MUST be an integer within its weight and the total MUST equal the six-component sum. Stars provide no points. A reproduced deterministic-gate failure, fabricated provenance, hidden category mismatch, or total below 70 vetoes an unconditional positive recommendation.

## Required independent output

Return self-contained Markdown containing:

1. assigned role and exact inspected scope;
2. severity-ordered findings with concrete permitted file/source references;
3. all six component scores and checked total out of 100;
4. evidence actually inspected and direct observations performed;
5. explicit evidence gaps and unsupported claims;
6. exactly one recommendation: `Ship`, `Block`, or `Ship with conditions`, followed by prioritized actions;
7. provider/model provenance as displayed by the `agy` session if observable;
8. the exact sentence `I did not inspect any other verification judge output.`

Do not edit files. Do not inspect forbidden artifacts. Do not expose hidden chain-of-thought; provide concise, auditable rationale only.
