# NotebookLM IDR evidence ledger

## Canonical notebook

- ID: `80cffd38-0185-4f4d-ae00-bbc67c4bc515`
- Title: `Tribunal IDR 2026-07-04`
- Public link: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515
- Verified public: `2026-07-20`
- Final source count after this run: `330`
- Shared NotebookLM conversation ID returned by the cross-queries: `1ebabb83-484f-405b-8b24-a26cfa5b9afb`

## Source work performed

The notebook began this run with 98 sources. This run then:

1. Added 12 targeted URLs and waited for processing: the GitHub repositories for promptfoo, DeepEval, DSPy, Langfuse, Phoenix, AutoGen, Ragas, OpenAI Evals, and lm-evaluation-harness; the multi-agent-debate paper; NN/g's usability heuristics; and W3C's WCAG 2.2 quick reference.
2. Uploaded `README.md`, `skill/SKILL.md`, the OpenSpec proposal/design, and all three OpenSpec capability specs.
3. Added `tribunal.py` as a pasted-text source after NotebookLM correctly rejected `.py` as an unsupported upload extension.
4. Preserved 75 cited sources from a previously completed but unimported deep-research task.
5. Ran a new deep web research task, ID `fb447053-85cc-4315-9c23-341cf6037844`, which found 137 sources and imported 133.
6. Re-read notebook details and sharing state after processing; NotebookLM reported 330 sources and public access.

### Targeted primary/project sources

- https://github.com/promptfoo/promptfoo
- https://github.com/confident-ai/deepeval
- https://github.com/stanfordnlp/dspy
- https://github.com/langfuse/langfuse
- https://github.com/Arize-ai/phoenix
- https://github.com/microsoft/autogen
- https://github.com/vibrantlabsai/ragas
- https://github.com/openai/evals
- https://github.com/EleutherAI/lm-evaluation-harness
- https://arxiv.org/abs/2305.14325
- https://www.nngroup.com/articles/ten-usability-heuristics/
- https://www.w3.org/WAI/WCAG22/quickref/
- Local `README.md`, `tribunal.py`, `skill/SKILL.md`, proposal, design, and capability specs

## Cross-query 1: architecture and correctness

**Question:** Using only the notebook sources, audit the proposed dependency-free Tribunal library architecture for knowledge/correctness, harsh critique/risk, and UI/UX judges. Identify which claims are supported, which are unsupported, and the minimum evidence/provenance contract needed to avoid fake independence or fake-green scoring. Cite source titles or citation numbers for every substantive conclusion.

**Grounded synthesis:**

- Supported: an offline deterministic layer is useful for structural gates, schema validation, and repeatable orchestration, provided it does not claim semantic truth.
- Supported: decomposing a broad review into correctness, risk, and UI/UX reduces single-judge cognitive overload.
- Unsupported: three role prompts or three samples from the same model family are automatically independent. Sources on verifier redundancy, judge replacement, and self-correction show correlated error and shared information boundaries.
- Required for substantive correctness: external primary/reference sources and, where possible, executable constraints such as tests, compilers, parsers, or observed tool results.
- Required for comparative live judges: provider/model identity, rubric version, prompt/contract identity, blind pre-debate outputs, error-dependence or bias probes, and explicit evidence gaps.
- Required for UI/UX: real viewport and interaction evidence; text-only inspection cannot establish visual fidelity or task completion quality.

NotebookLM cited, among others, `A Survey on Agent-as-a-Judge`, `Large Language Models Cannot Self-Correct Reasoning Yet`, `When the Judge Changes, So Does the Measurement`, `Turning Bias into Bugs`, the local OpenSpec design/spec, and the `tribunal.py` snapshot.

## Cross-query 2: hostile risk audit

**Question:** Using only notebook sources, act as a hostile architecture and security auditor. Identify the top failure modes and abuse cases for the proposed Tribunal OSS library and skill, distinguish defects in the current dependency-free local backend from risks of future live LLM backends, and give the smallest defensible mitigations.

**Grounded synthesis:**

- Same-family groupthink can make a multi-judge dashboard look independent while errors remain correlated.
- Style, position, verbosity, and self-preference bias can move LLM-as-judge scores independently of semantic quality; the BITE work demonstrates a concrete style-manipulation attack surface.
- A live retrieval/backend layer adds prompt-injection, fabricated-trace, stance-instability, runaway-loop, and cost-control risks that the offline library does not have.
- Minimal mitigations are deterministic gates before LLM aggregation, isolated pre-debate results, recorded provider/model/rubric provenance, pair-order swaps for pairwise comparisons, explicit budgets at a trustworthy boundary, and human or executable verification for high-risk claims.
- This release intentionally implements the honest offline boundary and evidence-gap reporting. It does not claim cross-family enforcement, durable runtime state, a billing proxy, or live prompt-injection defense.

## Cross-query 3: UX and implementability

**Question:** Using only notebook sources, give a concise UX and implementability audit of a CLI plus Codex `SKILL.md` Tribunal workflow for repeated operator use. Cover discoverability, cognitive load, status/provenance visibility, accessibility, evidence inspection, failure recovery, and what cannot be claimed without viewport or interaction testing.

**NotebookLM result:** `80/100` UX readiness, with prioritized recommendations for cross-family routing, formatting-bias tests, durable runtime separation, visual/browser verification, and out-of-band quota controls.

**Manual correction:** The score overstates the implemented surface. The CLI is keyboard-operable, has explicit modes, structured Markdown/JSON output, and visible provenance/gaps, but it has no interactive TUI or web UI. The notebook answer incorrectly imported future recommendations from other sources as current implementation, including a SHA-256 responsibility chain, assertion-driven backtracking, and durable checkpoints. Those features are not in this release. Therefore the report treats `80/100` as NotebookLM's recommendation-oriented assessment, not verified product behavior.

W3C WCAG 2.2 and NN/g sources support the general accessibility/usability criteria. They do not prove this CLI's user experience. The executed CLI smoke tests are the only direct UX evidence in this release.

## Cross-query 4: competitor differentiation

**Question:** Using only notebook sources, compare promptfoo, DeepEval, DSPy, Langfuse, Phoenix, AutoGen, Ragas, OpenAI Evals, lm-evaluation-harness, and the proposed Tribunal layer for the narrow use case of three-perspective hard-critical reviews with persona routing and explicit evidence gaps.

**Grounded synthesis:**

- promptfoo: strong declarative CLI, assertions, CI gates, and adversarial red teaming; not a persona-panel orchestrator.
- DeepEval: strong Python/pytest evaluation metrics; not a durable multi-agent debate runtime.
- DSPy: strong declarative programs and optimization; category mismatch for tribunal execution.
- Langfuse: strong traces, datasets, and evaluation observability; passive platform rather than the orchestration layer.
- Phoenix: strong OpenInference observability/evaluators; source-available ELv2 in the current repository, and not a tribunal router.
- AutoGen: strongest listed general multi-agent conversation/orchestration primitive; higher complexity and no native evidence-gap/crown contract.
- Ragas: strong RAG/agent evaluation metrics; no three-persona orchestration.
- OpenAI Evals and lm-evaluation-harness: strong reproducible static eval/benchmark runners; category mismatch for interactive tribunal workflow.
- Tribunal: exact narrow workflow fit, dependency-free local gate, explicit persona/evidence-gap contracts; immature, no telemetry store, no live backend, and no cross-family enforcement.

NotebookLM recommended Tribunal as the narrow use-case winner composed with Langfuse for telemetry and promptfoo for adversarial regression. Manual review accepts the composition direction but rejects NotebookLM's statement that Tribunal already enforces cross-family epistemic isolation; it currently enforces unique persona assignments and separate backend calls only.

## Cross-query 5: 100-point rubric

**Question:** Using only notebook sources, define scoring anchors, anti-gaming rules, and no-crown conditions for exactly: Type Fit 25, Adversarial Depth 20, Evidence Provenance 20, Persona/Skill Extensibility 15, Observability/Repeatability 10, Integration Cost 10.

**Adopted anchors:**

- Type Fit rewards native support for the three review types and an isolated pre-debate panel; generic evaluation or observability receives partial credit.
- Adversarial Depth rewards role specialization, blind initial verdicts, bias controls, and genuinely heterogeneous evidence/model boundaries; labels alone are not independence.
- Evidence Provenance rewards primary sources, executable observations, citations, evidence gaps, and rerunnable gates.
- Persona/Skill Extensibility rewards validated, discoverable, task-routed personas and reusable agent instructions.
- Observability/Repeatability rewards stable schemas, pinned provenance, machine-readable results, traces, and deterministic reruns.
- Integration Cost rewards a small dependency/security surface and clear embedding contract, while recognizing that absent integrations are not automatically a benefit.

No crown is awarded if deterministic gates fail, provenance is materially fabricated, all candidates score below 70, or the winner depends on an undisclosed category mismatch. Stars remain a dated adoption signal and contribute zero rubric points.

## Manual source-quality and answer audit

NotebookLM is a research surface, not an oracle. This run found several reasons to retain human audit:

- The 330-source corpus contains duplicate imports and mixes primary papers/docs with secondary blog material.
- Some answers generalized recommendations into nonexistent current features.
- The competitor and rubric answers returned prose source titles but empty `sources_used`/`citations` arrays; they are treated as qualitative synthesis, not direct citation proof.
- The architecture answer referred to an unverified `servas-ai/tribunal` identity; the local project had no remote at query time.
- A recommendation to preserve private chain-of-thought is not adopted. Public audit artifacts record concise rationales, inputs, results, and citations without requiring hidden reasoning disclosure.
- Numeric claims from secondary sources are not repeated as release facts unless independently corroborated. The report uses the robust qualitative conclusions: correlated judges are not independent, style/position bias exists, external evidence matters, and visual claims require visual proof.
