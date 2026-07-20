# Shared evidence packet for independent Grok judges

Snapshot: `2026-07-20T15:19:02Z`

This packet contains common facts and review targets. It deliberately contains no synthesized winner score and no other judge's conclusion.

## Assignment context

The requested artifact is a public MIT-licensed Tribunal library and Codex skill with three primary types: knowledge/correctness, hard critique/risk, and UI/UX implementability. The release must include live NotebookLM research, three independent external verdicts, an OSS matrix with dated GitHub stars and a 100-point rubric, exactly one use-case-bounded winner when warranted, a Mermaid flow, tests/gates, a commit, a public push, and a verified blob link.

## Review surfaces

- `tribunal.py`
- `README.md`
- `personas/*.json`
- `skill/SKILL.md`
- `examples/*.py`
- `scripts/csv_gate.py`
- `scripts/skill_gate.py`
- `scripts/report_gate.py`
- `tests/test_tribunal.py`
- `openspec/changes/finish-codex-tribunal-library/proposal.md`
- `openspec/changes/finish-codex-tribunal-library/design.md`
- `openspec/changes/finish-codex-tribunal-library/specs/**/*.md`
- `report/evidence/notebooklm-idr.md`

## Implemented runtime facts

- Python standard-library-only runtime.
- Primary enum modes: `knowledge`, `critique`, `ui_ux`; optional `comparison` mode.
- Hardness minimums: light/standard one round, hard two, brutal four.
- Three unique persona slugs are selected per round and evaluated through three separate `JudgeBackend.evaluate(JudgeRequest)` calls before synthesis.
- The default `local-rules` backend states that it checks orchestration structure only and does not semantically inspect targets, URLs, or NotebookLM contents.
- Callers can inject a custom backend returning validated `BackendResult` data.
- Reports include persona slug, backend, engine/source/capacity provenance, findings, evidence, evidence gaps, debate, final score, and recommendation marker in dict/JSON/Markdown forms.
- NotebookLM URLs are syntax-validated to the official HTTPS notebook path, but content verification remains a backend/evidence responsibility.
- The default engine records `local-rules`/`builtin-local`; named capacities exist only when explicitly supplied and are judge-slot counts, not claimed provider tokens.
- Persona JSON is validated. Unknown/duplicate/undersized explicit panels fail closed.
- The Karpathy-inspired persona is synthetic, cites three public repositories, disclaims authorship/endorsement, and forbids impersonation.
- “Uncensored” is documented as direct/non-sycophantic criticism within factual, legal, privacy, identity, and safety boundaries.

## Explicit non-capabilities

- No bundled live LLM provider, browser, hosted service, tracing database, visual UI, durable execution runtime, cryptographic log chain, billing proxy, or prompt-injection defense.
- Unique personas and separate backend calls do not enforce different model families. A custom backend may route all calls to one model unless it implements stronger provenance/policy.
- The CLI does not visually verify UI/UX claims. It records the missing evidence.
- The current project had no Git remote or commit at this snapshot; publication is a remaining task.

## Verification facts at packet creation

- `python -m unittest discover -s tests -v`: 11 tests passed after fixing one custom-backend debate bug found by the first run.
- Python compilation passed for the library, gates, tests, and examples.
- `examples/phase1_core_modes.py` ran the three primary modes successfully.
- `scripts/skill_gate.py skill/SKILL.md` passed.
- CSV/report positive gates await their final artifacts; deliberate negative runs rejected `README.md` as invalid input.
- `ruff` was unavailable. `basedpyright` and Biome LSPs were unavailable because installation had previously been declined in the environment.

## Live NotebookLM facts

- Canonical public notebook: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515
- Verified title: `Tribunal IDR 2026-07-04`.
- Verified final source count: 330.
- This run added nine competitor repositories, a multi-agent debate paper, NN/g heuristics, W3C WCAG 2.2, local README/skill/code/OpenSpec sources, imported 75 cited prior-research sources, and imported 133 of 137 sources from a new deep-research task.
- Five cross-queries covered architecture/correctness, hostile risks, UX/implementability, competitors, and scoring.
- `report/evidence/notebooklm-idr.md` records questions, synthesis, source URLs, and a manual audit of NotebookLM overclaims.

## GitHub metadata snapshot

Stars are a dated adoption signal and must receive zero scoring points.

| Repository | Stars | License evidence |
|---|---:|---|
| https://github.com/microsoft/autogen | 59844 | GitHub API reported `CC-BY-4.0`; repository licensing requires component-level care |
| https://github.com/stanfordnlp/dspy | 36251 | MIT |
| https://github.com/langfuse/langfuse | 31494 | MIT outside listed enterprise directories; custom top-level file |
| https://github.com/promptfoo/promptfoo | 23438 | MIT |
| https://github.com/openai/evals | 18953 | MIT code; listed datasets have separate licenses |
| https://github.com/confident-ai/deepeval | 16967 | Apache-2.0 |
| https://github.com/vibrantlabsai/ragas | 14918 | Apache-2.0 |
| https://github.com/EleutherAI/lm-evaluation-harness | 13340 | MIT |
| https://github.com/Arize-ai/phoenix | 10641 | Elastic License 2.0, source-available rather than OSI open source |

All star counts came from the live GitHub API at the snapshot and all nine repositories reported `archived=false`.

## Declared rubric for later synthesis

- Type Fit: 25
- Adversarial Depth: 20
- Evidence Provenance: 20
- Persona/Skill Extensibility: 15
- Observability/Repeatability: 10
- Integration Cost: 10

Total: 100. A deterministic-gate failure, fabricated provenance, score below 70, or undisclosed category mismatch vetoes a crown. The judges may criticize this rubric, but must not invent a precomputed matrix score.

## Required independent judge output

Return a self-contained Markdown verdict containing:

1. Assigned perspective and scope.
2. Findings ordered by severity, with file references or external URLs where possible.
3. A score from 0 through 100 and the scoring rationale.
4. Evidence actually inspected.
5. Explicit evidence gaps and claims that cannot be made.
6. A ship/block/ship-with-conditions recommendation and prioritized actions.
7. The sentence: `I did not inspect any other Tribunal judge output.`

Do not edit files. Do not expose hidden chain-of-thought; provide concise, auditable rationale only.
