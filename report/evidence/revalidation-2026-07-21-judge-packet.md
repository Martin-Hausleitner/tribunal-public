# Frozen conclusion-free packet for 2026-07-21 judges

This packet is frozen from repository baseline HEAD `56df1b0c99e3c75546585ad5e4aea6f784081db5` after current NotebookLM and primary GitHub evidence was collected. It contains observations, public contracts, and open questions only. It deliberately omits earlier judge prose, current matrix rank/total/crown, synthesized verdicts, and the final recommendation.

All three judges receive this exact packet. A judge must not inspect `report/codex-trib-lib-tribunal.md`, `report/codex-trib-lib-matrix.csv`, Git history, or any file whose name includes `judge`, `external-attempt`, or `synthesis` other than this packet. No judge may inspect a sibling output.

## Assignment boundary

Independently audit the Codex Tribunal Python library and reusable skill from exactly one assigned perspective: knowledge/correctness, harsh criticism/risk, or CLI UX/implementability. Assess the bounded local contract and release evidence. Do not treat a NotebookLM citation, local structural score, project-authored rubric, or model opinion as semantic truth.

Permitted source surfaces are `tribunal.py`, `README.md`, `pyproject.toml`, `LICENSE`, `skill/SKILL.md`, `personas/*.json`, `personas/__init__.py`, `examples/*.py`, `tests/test_tribunal.py`, `scripts/*.py`, this pass's OpenSpec artifacts, and these evidence inputs:

- `report/evidence/revalidation-2026-07-21-baseline.md`
- `report/evidence/revalidation-2026-07-21-notebooklm.md`
- `report/evidence/revalidation-2026-07-21-oss.md`
- `report/evidence/github-snapshot.json`

Read-only direct commands against those surfaces are allowed. Do not edit files.

## Current bounded runtime contract to verify

- Public modes are `knowledge`, `critique`, `ui_ux`, and additional `comparison`.
- Each round selects three distinct persona slugs and sends three separate immutable `JudgeRequest` values through separate `JudgeBackend.evaluate` calls before post-hoc synthesis.
- Separate calls/personas establish request isolation only. They do not prove provider-memory isolation, family diversity, statistical independence, factual correctness, or interactive debate.
- The default `local-rules` backend is deterministic structural readiness only. It does not retrieve a NotebookLM URL, inspect target semantics, render pixels, or award a runtime crown.
- Local structural scores are 40/100 without a NotebookLM reference and 50/100 with a syntactically valid reference. That deliberately remains a warning, not a failed CI execution and not a semantic score.
- A positive runtime marker requires every view to score at least 80 and return no backend-declared evidence gap. A custom backend self-declares score/evidence/gaps; the core validates shape, not truth.
- Hardness minimums are one, one, two, and four effective rounds for light, standard, hard, and brutal. Nine bundled personas repeat after three complete rounds; an explicit three-person panel repeats each round.
- JSON and Markdown include mode/round/persona/skill/backend/engine/source provenance, findings, evidence, gaps, scores, post-hoc synthesis, and marker. Markdown normalizes and escapes backend-authored values; JSON preserves them.
- The Karpathy-inspired critic cites `llama2.c`, `minGPT`, and `micrograd`, is synthetic and unendorsed, and carries a runtime disclaimer. Generated conclusions must not be attributed to Andrej Karpathy.
- Routed skill names are host declarations. The core records labels but does not discover, install, validate, or execute external Codex skills.
- Capacity integers are per-run judge slots, not tokens, provider quota discovery, billing controls, or durable cross-run budgets.
- No live-provider adapter, cross-family policy, browser/TUI, persistent trace store, durable workflow runtime, visual accessibility runner, or prompt-injection defense is bundled or claimed.

## Direct controls observed in this pass

- Current HEAD matched `origin/master` at baseline; tracked files were clean before this pass's artifacts.
- `python -m py_compile tribunal.py tests/test_tribunal.py personas/__init__.py` exited `0`.
- `_normalize_hardness`, `_parse_capacities`, `_load`, `judge`, `VerdictReport.to_json`, and `VerdictReport.to_markdown` were callable.
- Nine personas loaded.
- `validate_backend_result` accepted a valid result with `evidence_gaps=[]`.
- `python tribunal.py --mode critique --rounds 0 --target invalid` printed one concise `tribunal: error:` line to stderr, no stdout or traceback, and exited `2`.
- Full unit/build/install/console/API gates remain pending and must be required before final release.

## Authenticated NotebookLM observations

- Canonical public notebook: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515; authenticated with `nlm 0.8.9`.
- The account had 500 notebooks. Notebook creation failed safely with API code 3.
- The canonical notebook had 600 processed sources. A pass manifest source returned an ID, then settled empty in failed status 3 and was excluded.
- Accepted queries used fresh conversation IDs and explicit processed source IDs. The preflight and six role/control queries selected every requested source and returned 5, 36, 30, 49, 35, 55, and 17 citation mappings respectively.
- One oversized answer had `sources_used=[]` and was rejected. One attempt produced no capturable output and was rejected.
- Knowledge, criticism, and UX answers independently repeated false current blockers from a normalized historical code snapshot: missing methods, rejected empty gaps, and missing error trapping. A separate contradiction query corrected them after receiving external current-HEAD observations.
- NotebookLM citation mappings establish provenance, not correctness. Current source and execution control implementation conflicts.
- Position bias and common-family agreement are legitimate downstream LLM-judge research risks; the selected research does not by itself prove a defect in the deterministic local core.

## Current primary OSS metadata

The live authenticated GitHub snapshot completed at `2026-07-20T23:15:54Z`. All eleven repositories reported `archived=false` and `disabled=false`. Stars are mutable adoption context and provide zero points.

| Candidate | Canonical repository | Stars | API SPDX |
|---|---|---:|---|
| Codex Tribunal | https://github.com/Martin-Hausleitner/tribunal-public | 0 | MIT |
| promptfoo | https://github.com/promptfoo/promptfoo | 23,446 | MIT |
| Microsoft Agent Framework | https://github.com/microsoft/agent-framework | 12,253 | MIT |
| DeepEval | https://github.com/confident-ai/deepeval | 16,983 | Apache-2.0 |
| AutoGen | https://github.com/microsoft/autogen | 59,851 | CC-BY-4.0 |
| Ragas | https://github.com/vibrantlabsai/ragas | 14,918 | Apache-2.0 |
| OpenAI Evals | https://github.com/openai/evals | 18,956 | NOASSERTION |
| Langfuse | https://github.com/langfuse/langfuse | 31,515 | NOASSERTION |
| DSPy | https://github.com/stanfordnlp/dspy | 36,262 | MIT |
| Phoenix | https://github.com/Arize-ai/phoenix | 10,642 | NOASSERTION |
| lm-evaluation-harness | https://github.com/EleutherAI/lm-evaluation-harness | 13,342 | MIT |

Primary qualifications: AutoGen is in maintenance mode and recommends Microsoft Agent Framework for new work; OpenAI Evals has dataset-specific license exceptions; Langfuse excludes declared enterprise directories from MIT; Phoenix uses Elastic License 2.0 and is source-available rather than OSI open source. These are repository observations, not legal advice.

## Common 100-point rubric

- Type Fit: 25
- Adversarial Depth: 20
- Evidence Provenance: 20
- Persona/Skill Extensibility: 15
- Observability/Repeatability: 10
- Integration Cost: 10

Each component must be an integer within its weight and the total must equal the six-component sum. Stars provide no points. A reproduced deterministic-gate failure, fabricated provenance, hidden category mismatch, or total below 70 vetoes an unconditional positive recommendation.

## Required independent output

Return self-contained Markdown with:

1. assigned role and exact inspected scope;
2. severity-ordered findings with concrete permitted file/source references;
3. all six component scores and checked total out of 100;
4. evidence actually inspected and direct observations performed;
5. explicit evidence gaps and unsupported claims;
6. exactly one recommendation: `Ship`, `Block`, or `Ship with conditions`, followed by prioritized actions;
7. provider/model provenance from the invocation: Grok CLI `0.2.102`, requested model `grok-4.5`, effort `high`, single-turn, no subagents;
8. the exact sentence `I did not inspect any other revalidation judge output.`

Do not expose hidden chain-of-thought. Provide concise, auditable rationale only.
