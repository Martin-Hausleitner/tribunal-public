# Frozen conclusion-free packet for final live judges, 2026-07-21

This packet is frozen from repository starting HEAD `990a8df200716a446472faf4110a2e896c52ab40` after current NotebookLM and primary GitHub evidence was collected. It contains observations, public contracts, open risks, and pending checks only. It deliberately omits earlier judge prose, current matrix rank/total/crown, synthesized verdicts, and the final recommendation.

All three judges receive this exact packet. A judge must not inspect `report/codex-trib-lib-tribunal.md`, `report/codex-trib-lib-matrix.csv`, Git history, or any file whose name includes `judge`, `external-attempt`, or `synthesis` other than this packet. No judge may inspect a sibling output.

## Assignment boundary

Independently audit the Codex Tribunal Python library and reusable skill from exactly one assigned perspective: knowledge/correctness, harsh criticism/risk, or CLI UX/implementability. Assess the bounded local contract and release evidence. Do not treat a NotebookLM citation, local structural score, project-authored rubric, prior report, or model opinion as semantic truth.

Permitted read-only repository surfaces are `tribunal.py`, `README.md`, `pyproject.toml`, `LICENSE`, `skill/SKILL.md`, `personas/*.json`, `personas/__init__.py`, `examples/*.py`, `tests/test_tribunal.py`, `scripts/*.py`, this pass's OpenSpec artifacts, and these evidence inputs:

- `report/evidence/final-live-2026-07-21-baseline.md`
- `report/evidence/final-live-2026-07-21-notebooklm.md`
- `report/evidence/final-live-2026-07-21-oss.md`
- `report/evidence/github-snapshot.json`

Read-only direct commands against those surfaces are allowed. Do not edit files.

## Current bounded runtime contract to verify

- Public review modes are `knowledge`, `critique`, `ui_ux`, plus `comparison` for the OSS matrix use case.
- Each round selects three distinct personas and sends three immutable `JudgeRequest` values through separate `JudgeBackend.evaluate` calls before creating a post-hoc synthesis.
- Separate requests/personas establish request isolation only. They do not prove provider-memory isolation, provider-family diversity, statistical independence, factual correctness, or interactive debate.
- The default `local-rules` backend is deterministic structural readiness only. It does not retrieve NotebookLM content, inspect target semantics, render pixels, execute routed skills, or award a runtime crown.
- Local structural scores are `40/100` without a NotebookLM reference and `50/100` with a syntactically valid reference. Both retain explicit evidence gaps and a warning marker.
- A positive runtime marker requires every judge view to score at least `80` and return no backend-declared evidence gap. A custom backend self-declares scores, evidence, and gaps; the core validates shape, not truth.
- Hardness establishes minimum effective rounds; total requested rounds are bounded at `32` and target input at `10,000` characters.
- JSON and Markdown include mode/round/persona/skill/backend/engine/source provenance, findings, evidence, gaps, scores, post-hoc synthesis, and marker. Markdown escapes/collapses backend text; JSON preserves values.
- Nine bundled personas are schema validated. The Karpathy-inspired critic cites public `llama2.c`, `minGPT`, and `micrograd` repositories, is synthetic and unendorsed, and carries a runtime disclaimer. Generated conclusions must not be attributed to Andrej Karpathy.
- Routed skill names are host declarations. The core records labels but does not discover, install, validate, or execute external Codex skills.
- Capacity integers are per-run judge slots, not tokens, provider quota discovery, billing controls, rate-limit retries, or durable cross-run budgets.
- No live-provider adapter, cross-family policy, browser/TUI, persistent trace store, durable workflow runtime, visual accessibility runner, human usability study, or prompt-injection defense is bundled or claimed.

## Current direct observations

- Baseline local HEAD equaled the then-current `origin/master`; tracked files were clean before this pass's artifacts.
- `nlm login --check` authenticated; the canonical notebook and sharing endpoints returned the public link recorded below.
- The canonical source inventory began at `942` total, `600` processed, and `342` failed; all 15 explicitly selected sources were independently reduced to `status=2`. Two safe current-pass insertion attempts created only failed records, so the final inventory was `944/600/344`; neither failed record was queried or cited.
- A direct critique CLI run emitted three `local-rules` views at `40/100`, explicit gaps, `post-hoc-synthesis`, and `⚠️`.
- Current source permits `evidence_gaps=[]`; the processed NotebookLM snapshot's contrary characterization is stale.
- Current `main` catches expected `OSError`, `RuntimeError`, `TypeError`, and `ValueError` paths and returns concise exit code `2`; full final error-path and clean-install gates remain pending.
- The JSON snapshot parses and the CSV gate currently passes `11` rows, exact component arithmetic, numeric stars, score spread, and one structural crown count. Judges are not given its project-authored totals or winner.
- Full unit, build, wheel-content, clean-install console/API, final report, and publication gates remain pending and must be conditions of release.

## Authenticated NotebookLM observations

- Canonical public notebook: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515; authenticated with `nlm 0.8.9`.
- The account had exactly `500` notebooks. No pre-existing external content was deleted, renamed, refreshed, or repurposed.
- The canonical notebook began with `600` processed sources and `342` failed sources. A SHA-pinned URL insertion and a truth-bounded manifest insertion settled as two new failed records, yielding a final `600/344`; neither is evidence. Only 15 explicitly selected `status=2` source IDs were queried, and historical Tribunal report sources were excluded from the current controls.
- A compact knowledge answer returned 6 used sources and 30 citation mappings; harsh risk returned 5 and 27; OSS composition returned all 10 selected repositories and 183 mappings.
- The initial broad knowledge, compact UX, and contradiction controls returned substantive answers but empty `sources_used`/citation metadata. They establish no new factual support and are retained only as query provenance, hypotheses, or falsification checklists.
- Subsequent controls returned knowledge `7/21`, UX `5/35`, OSS `10/31`, and contradiction `13/36` used-source/citation counts. A harsh-risk call returned only `1/1`, while its compact capture returned `0/0`; ungrounded risk prose was excluded.
- Every fresh request returned the same historical conversation identifier even though no continuation identifier was supplied. Fresh service requests are observed; fresh-conversation isolation is not claimed.
- NotebookLM repeated stale claims that `local-rules` is a semantic mock pass, empty gap lists crash, and expected errors escape. Current source and direct execution overrule them.
- NotebookLM citation mappings establish provenance, not correctness. The current code checkout, primary GitHub reads, and final executable proof control conflicts.

## Current primary OSS metadata

The authenticated GitHub snapshot completed at `2026-07-21T00:53:15Z`. All eleven repositories returned `archived=false` and `disabled=false`. Stars are mutable adoption context and provide zero rubric points.

| Candidate | Canonical repository | Stars | API SPDX |
|---|---|---:|---|
| Codex Tribunal | https://github.com/Martin-Hausleitner/tribunal-public | 0 | MIT |
| promptfoo | https://github.com/promptfoo/promptfoo | 23,446 | MIT |
| Microsoft Agent Framework | https://github.com/microsoft/agent-framework | 12,254 | MIT |
| DeepEval | https://github.com/confident-ai/deepeval | 16,984 | Apache-2.0 |
| AutoGen | https://github.com/microsoft/autogen | 59,851 | CC-BY-4.0 |
| Ragas | https://github.com/vibrantlabsai/ragas | 14,919 | Apache-2.0 |
| OpenAI Evals | https://github.com/openai/evals | 18,957 | NOASSERTION |
| Langfuse | https://github.com/langfuse/langfuse | 31,516 | NOASSERTION |
| DSPy | https://github.com/stanfordnlp/dspy | 36,262 | MIT |
| Phoenix | https://github.com/Arize-ai/phoenix | 10,642 | NOASSERTION |
| lm-evaluation-harness | https://github.com/EleutherAI/lm-evaluation-harness | 13,342 | MIT |

Primary qualifications: AutoGen is in maintenance mode and recommends Microsoft Agent Framework for new projects; OpenAI Evals has dataset-specific license exceptions and currently declines custom-code submissions; Langfuse excludes named enterprise directories from MIT; Phoenix uses Elastic License 2.0 and restricts hosted-service use. These are repository observations, not legal advice.

## Common 100-point rubric

- Type Fit: 25
- Adversarial Depth: 20
- Evidence Provenance: 20
- Persona/Skill Extensibility: 15
- Observability/Repeatability: 10
- Integration Cost: 10

Each component must be an integer within its weight and the total must equal the six-component sum. Stars provide no points. A reproduced deterministic-gate failure, fabricated provenance, hidden category mismatch, or total below `70` vetoes an unconditional positive recommendation.

## Required independent output

Return self-contained Markdown with:

1. assigned role and exact inspected scope;
2. packet SHA-256 supplied in the invocation;
3. severity-ordered findings with concrete permitted file/source references;
4. all six component scores and checked total out of `100`;
5. evidence actually inspected and direct observations performed;
6. explicit risks, evidence gaps, unsupported claims, and limitations;
7. exactly one recommendation: `Ship`, `Block`, or `Ship with conditions`, followed by prioritized actions;
8. actual engine/model provenance from the invocation;
9. the exact sentence `I did not inspect any sibling judge output.`

Do not expose hidden chain-of-thought. Provide concise, auditable rationale only.
