# Frozen evidence packet for independent revalidation judges

Frozen UTC: `2026-07-20T19:15:00Z`  
Repository snapshot base: `8816e035d7320955eea745e84832bafcca381ed8`

This packet contains verified inputs and disclosed boundaries only. It deliberately omits every prior judge output, score, rank, crown, final recommendation, and synthesis. Judges must not read the final report or any file whose name contains `judge-knowledge`, `judge-critique`, or `judge-ux`.

## Assignment

Independently audit a public MIT-licensed Codex Tribunal Python library and reusable skill for exactly one assigned perspective: knowledge/correctness, hard criticism/risk, or CLI UX/implementation feasibility. The required product scope includes three tribunal modes, a disclosed Karpathy-inspired synthetic persona, evidence-aware structured verdicts, NotebookLM research provenance, an OSS-first comparison contract, and a public-interface E2E path.

## Inspectable project surfaces

- `tribunal.py`: dependency-free Python API and CLI.
- `README.md`: documented public behavior and limitations.
- `personas/*.json`: nine persona documents.
- `skill/SKILL.md`: reusable routing and anti-fake workflow.
- `pyproject.toml`, `examples/*.py`, `tests/test_tribunal.py`, and `scripts/*.py`.
- `openspec/changes/live-audit-codex-tribunal-library/`: proposal, design, capability spec, and completed task contract.
- `report/evidence/notebooklm-live-audit.md`: prior normalized live IDR ledger with manual contradiction controls.
- `report/evidence/e2e-proof.md`: previously retained public-interface execution ledger; treat it as a claim to challenge until reproduced.
- `report/evidence/github-snapshot.json` and `report/codex-trib-lib-matrix.csv`: prior metadata/scoring artifacts; the fresh metadata below supersedes their mutable star counts.

Do not inspect `report/codex-trib-lib-tribunal.md`, prior Grok/agy evidence, live-audit judge outputs, or sibling revalidation outputs. Those files contain conclusions that would contaminate a blind initial verdict.

## Verified runtime boundaries

- Public modes are `knowledge`, `critique`, `ui_ux`, and optional `comparison`.
- Every round selects three distinct persona slugs and issues three separate `JudgeBackend.evaluate` calls before post-hoc synthesis.
- Separate calls and unique personas prove payload/process separation only. They do not prove provider memory isolation, distinct model families, statistical independence, or factual correctness.
- The bundled `local-rules` backend checks structural readiness, records evidence gaps, and has a 40/100 ceiling without a NotebookLM URL and 50/100 with one. It does not query that URL or inspect semantics or pixels.
- Hardness minimums are 1, 1, 2, and 4 effective rounds for light, standard, hard, and brutal. Nine bundled personas repeat after three rounds; an explicit three-person panel repeats each round.
- JSON and Markdown reports include judge persona, backend/engine/source provenance, findings, evidence, gaps, score, synthesis, and marker. Positive markers require every view to score at least 80 and declare no evidence gap; an empty gap list remains a backend assertion.
- The Karpathy-inspired critic is synthetic, cites public repositories, carries a runtime disclaimer, and disclaims authorship and endorsement by Andrej Karpathy.
- No bundled live provider, cross-family router, browser/TUI, persistent trace store, live quota discovery, durable workflow runtime, cryptographic log chain, or prompt-injection defense is claimed.

## Fresh NotebookLM facts

- Canonical public notebook: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515
- Authenticated CLI inventory at this revalidation found 336 total sources: 331 processed and five failed. All five failures are duplicated or secondary Medium articles; current project artifacts and targeted primary OSS sources are processed.
- Three new role-aligned cross-queries were followed by one contradiction/source-attribution query in the same notebook conversation.
- Knowledge query metadata returned 15 source IDs and 46 citation mappings; critique returned 15 and 33; the UX answer returned empty source/citation arrays and therefore cannot count as grounded research evidence.
- The contradiction query returned eight source IDs and 24 citation mappings. It confirmed that 330 is stale, the unrelated 70-row model registry is not project evidence, capacity inputs are not durable quotas, separate calls are not memory/family independence, and study-specific correlation/churn values are not local measurements.
- Generated NotebookLM prose is research input, not executable proof. Current code and direct execution outrank it when they conflict.

## Fresh live OSS metadata

Authenticated GitHub REST calls completed before this packet was frozen. All eleven candidate repositories resolved to their canonical URLs and were unarchived. Mutable star values at capture were:

- Codex Tribunal 0
- promptfoo 23,441
- Microsoft Agent Framework 12,247
- DeepEval 16,979
- AutoGen 59,848
- Ragas 14,918
- OpenAI Evals 18,955
- Langfuse 31,505
- DSPy 36,256
- Phoenix 10,642
- lm-evaluation-harness 13,341

GitHub API SPDX signals were MIT for Tribunal, promptfoo, Microsoft Agent Framework, DSPy, and lm-evaluation-harness; Apache-2.0 for DeepEval and Ragas; CC-BY-4.0 for AutoGen; and NOASSERTION for OpenAI Evals, Langfuse, and Phoenix. Repository-level qualifications still require direct license-file review. Stars are dated adoption context and contribute zero rubric points.

## Common 100-point rubric

- Type Fit: 25
- Adversarial Depth: 20
- Evidence Provenance: 20
- Persona/Skill Extensibility: 15
- Observability/Repeatability: 10
- Integration Cost: 10

A component may not exceed its weight. A deterministic-gate failure, fabricated provenance, hidden category mismatch, or total below 70 vetoes a positive recommendation.

## Required independent output

Return self-contained Markdown containing:

1. assigned perspective and inspected scope;
2. severity-ordered findings with concrete file/source references;
3. all six component scores and a checked total out of 100;
4. evidence actually inspected;
5. explicit evidence gaps and unsupported claims;
6. `Ship`, `Block`, or `Ship with conditions`, followed by prioritized actions;
7. the exact sentence `I did not inspect any other revalidation judge output.`

Do not edit files. Do not expose hidden chain-of-thought; provide concise, auditable rationale only.
