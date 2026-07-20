# NotebookLM live-audit evidence

## Canonical notebook verification

- Verified UTC: `2026-07-20T17:56:31Z`
- Notebook ID: `80cffd38-0185-4f4d-ae00-bbc67c4bc515`
- Title: `Tribunal IDR 2026-07-04`
- Public link: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515
- Sharing state: public link enabled
- Source count before this audit: `330`
- Source count after live-audit additions: `336`

Notebook identity, source count, sharing state, and URL were read from the authenticated NotebookLM CLI. Private collaborator/account details are deliberately omitted.

## Corpus audit and additions

All twelve required targeted sources were present before the new additions: promptfoo, DeepEval, DSPy, Langfuse, Phoenix, AutoGen, Ragas, OpenAI Evals, lm-evaluation-harness, the multi-agent-debate paper, NN/g usability heuristics, and W3C WCAG 2.2. The corpus also retained processed local README, skill, runtime, proposal, design, and capability-spec sources from the earlier release run.

This audit added and waited for successful processing of six current local artifacts:

1. `report/codex-trib-lib-tribunal.md`
2. live-audit OpenSpec `proposal.md`
3. live-audit OpenSpec `design.md`
4. live-audit capability `spec.md`
5. live-audit OpenSpec `tasks.md`
6. `report/evidence/live-audit-baseline.md`

After processing, `331` sources had status `2` (processed) and five had status `3` (failed). Every newly added source and every required targeted source was processed. The five failures were duplicated or secondary Medium articles, including two duplicate AutoGen-commentary entries; they are excluded from decision evidence and do not create a primary-source gap.

## Live cross-queries

The following sections are populated only from new NotebookLM calls made after the six current sources were processed. Returned source/citation metadata and any overclaims are audited explicitly.

All four calls returned conversation ID `1ebabb83-484f-405b-8b24-a26cfa5b9afb`. Each call was made without supplying a prior-answer payload; the ID is NotebookLM's notebook conversation identifier, not proof that the answers are statistically independent.

### Query 1: knowledge, correctness, and independence

**Question:** Using only the processed sources, audit the current release report and live-audit OpenSpec; distinguish structural orchestration from semantic truth, test the independence boundary, and report supported/unsupported claims plus the minimum evidence contract.

**Returned metadata:** `22` source IDs and `62` citation mappings.

**Grounded result:** The deterministic core can validate input and orchestration structure but cannot establish semantic correctness, source retrieval, or visual UX quality. Three unique persona assignments and separate backend requests give payload/session isolation, not model-family or statistical independence. A defensible live record needs provider/model and rubric identity, blind pre-synthesis outputs, source or executable evidence, explicit gaps, and external bias/error-dependence controls. Production-only controls such as durable traces, trusted budgets, and cross-family policy remain recommendations.

**Manual correction:** The answer incorrectly described current documentation as claiming interactive debate and autonomous self-correction; the README, skill, JSON report kind, and final report explicitly label synthesis as post-hoc and do not promise autonomous repair. Its HTTP-402 Grok statement came from the previous release report, not from a new Grok attempt. Its `330`-source wording was stale after the live additions raised the corpus to `336`. Numerical correlation and benchmark figures are study-specific and are not adopted as runtime guarantees.

### Query 2: hostile risks and smallest mitigations

**Question:** Separate defects in the local backend from risks introduced by a future live LLM backend; give severity-ordered findings, source attribution, smallest mitigations, blockers, and confidence.

**Returned metadata:** `15` source IDs and `27` citation mappings.

**Grounded result:** The high-impact future-live risks are correlated same-family judgments, generated claims of tool execution without actual state change, style/format sensitivity, prompt-injection and stale-trace risks, cost leakage, and non-durable failure recovery. The local core's semantic blindness and static capacity inputs are real limitations but are explicitly bounded behavior rather than hidden live-provider defects. Useful controls include deterministic pre-gates, provider/model provenance, external execution proof, and bias calibration.

**Manual correction:** The answer said the release presents cryptographic chains, post-quantum certificates, durable state, and cross-family routing as implemented; the release says the opposite in its synthesis, limitations, and next-increments sections. It also called post-hoc synthesis an undocumented overclaim even though the current docs label it. Formatting stripping and pair-order swaps are candidate mitigations, not universal mandates: one cited study reports that position swapping can hurt on some adversarial datasets, so a live backend must calibrate rather than blindly apply them.

### Query 3: CLI UX and operational feasibility

**Question:** Audit the Python CLI, JSON/Markdown surfaces, reusable skill, personas, installation, and evidence workflow; separate executable proof from claims requiring a visual surface.

**Returned metadata:** `18` source IDs and `38` citation mappings.

**Grounded result:** PEP 517 packaging, a dependency-free runtime, explicit modes, strict boundary validation, bounded hardness, concise Markdown/JSON output, persona discovery, and evidence-gap visibility support low-friction CLI use. The core has no bundled live provider, TUI/browser UI, dynamic quota discovery, durable checkpointing, or visual accessibility proof. Executable CLI runs can prove parsing, schema loading, serialization, process exit behavior, panel construction, and declared gaps; they cannot prove viewport layout, color contrast, responsive behavior, or end-user task success.

**Manual correction:** The answer repeated a superseded claim that expected input failures emit raw tracebacks; current `main()` catches expected failures and the behavior is unit-tested, but it must be re-executed in this audit. It also called brutal mode's 12 views distinct and described non-overlapping persona rotation; the nine bundled personas repeat after three rounds, and an explicit three-person panel repeats every round. The current documentation already calls debate post-hoc.

### Query 4: contradiction and source-attribution control

**Question:** Audit the first three answers for primary/executable support, secondary-only claims, contradictions, numerical claims needing independent verification, and conservative final wording.

**Returned metadata:** `12` source IDs and `33` citation mappings.

**Grounded result:** The answer correctly recovered five critical boundaries from project sources: expected CLI failures are concise exit-2 errors; synthesis is post-hoc; unique personas are not model-family independence; brutal mode repeats personas after the nine-person library is exhausted; and cryptographic traces/durable state are not implemented. It advised conservative wording that describes the release as an offline structural orchestration contract rather than a semantic verifier, visual tester, cross-family consensus engine, or production trace platform.

**Manual correction:** Even this contradiction query claimed that the release documentation presents advanced controls as implemented, while the citation excerpt immediately states they are absent. This is a concrete NotebookLM self-contradiction and confirms why the final report must privilege current executable project evidence over generated characterization. Workload-specific percentages, correlations, and attack effect sizes remain external study results and are not repeated as properties of Tribunal.

## IDR conclusion

The fresh NotebookLM run strengthens the bounded recommendation and does not justify a broader green claim. The reusable core is defensible when described as deterministic orchestration, provenance, explicit gaps, and backend extension points. Any live deployment must independently prove model/provider routing, actual source/tool access, budgets, traces, and visual interaction. NotebookLM itself demonstrated why a generated research synthesis needs manual contradiction checks: it retrieved the current report yet still repeated superseded findings and misread explicit non-capabilities as claims.
