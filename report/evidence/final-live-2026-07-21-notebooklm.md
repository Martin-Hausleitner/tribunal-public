# Final live NotebookLM IDR, 2026-07-21

IDR: ja

- Observation window: `2026-07-21T00:44Z` through `2026-07-21T00:59Z`
- Canonical public notebook: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515
- Notebook ID: `80cffd38-0185-4f4d-ae00-bbc67c4bc515`
- Title: `Tribunal IDR 2026-07-04`
- Authenticated CLI: `nlm 0.8.9`; `nlm login --check`, notebook read, source inventory, sharing read, and all query commands exited successfully
- Public sharing: `is_public=true`, `access_level=public`; the service returned the same public link shown above
- Initial inventory: `942` total sources, `600` processed (`status=2`), `342` failed (`status=3`)
- Final inventory after two safe current-pass insertions: `944` total, still `600` processed and now `344` failed

The account was at `500` notebooks and the canonical notebook remained at its `600` processed-source ceiling. To fulfill the brief's source-insertion requirement without deleting user content, the pass attempted a SHA-pinned public raw `tribunal.py` URL and a short truth-bounded manifest for starting commit `990a8df200716a446472faf4110a2e896c52ab40`. The URL command returned exit `1`, but direct inventory exposed failed record `bf8ad6e1-c2d8-4efa-8a98-7ecf5c860a7c`; the text command returned ID `d494d264-56eb-4980-9360-d5d80bcff86c`, which also settled at status `3`. Neither was queried or cited. No pre-existing notebook or source was deleted, renamed, refreshed, or repurposed. Failed sources establish no research fact. No credential, cookie, token, account identifier, collaborator identity, or private notebook title is retained here.

## Explicit processed source set

A fresh `source list --json` reduction found all `15` selected IDs and one unique state, `status=2`:

### Current project anchor

- `fe7a231f-4c3e-4039-81e4-7c71cf95ea61` — `tribunal.py source snapshot 2026-07-20`

This snapshot is a research anchor, not the controlling implementation. Checked-out source at starting commit `990a8df200716a446472faf4110a2e896c52ab40` and direct execution overrule every stale snapshot claim.

### Canonical OSS repository sources

- `c79ca1bc-c92e-4932-9bdf-b8ebb403e74b` — promptfoo
- `73fd8d4d-1865-4901-9b88-15fcf9eb9da0` — Microsoft Agent Framework
- `f0cb48fe-9660-4200-8422-317343fd382b` — DeepEval
- `a7a42d60-b8af-4070-8c34-64631606592b` — AutoGen
- `9e65e710-a488-4705-8822-10ac6d4aa220` — Ragas
- `a17d1fb1-6a62-437f-bb6b-e3d1e292e6d8` — OpenAI Evals
- `1a88fad5-66a9-4d49-b7d6-39c6869eaa6b` — Langfuse
- `2e4919cf-0aa2-4e80-b6b1-ae24289173ab` — DSPy
- `25abb192-77ce-4e55-8529-a3ab5e131930` — Phoenix
- `b4d2fe1b-8174-42c7-8983-dc1510d84d44` — lm-evaluation-harness

### Research and UX criteria

- `e390f1fb-bdae-43b5-86aa-55af5578aa80` — multi-agent-debate paper
- `92a44e33-1f12-4454-a4c2-e5e97feb8f98` — ACL position-bias study
- `4fd90dd9-426b-4d47-aaa3-c972c98f14fe` — Nielsen Norman Group usability heuristics
- `6bfa3b74-65f3-4361-b7de-e9ce3ae20f6c` — W3C WCAG 2.2 Quick Reference

No historical Tribunal report source was selected for the current control queries.

## Fresh query ledger

All calls omitted `--conversation-id`, supplied explicit `--source-ids`, requested JSON, and used a `180` second timeout. NotebookLM nevertheless returned the same historical conversation identifier, `1ebabb83-484f-405b-8b24-a26cfa5b9afb`, for every call. The commands therefore prove fresh authenticated requests and returned answers, but not fresh-conversation isolation.

| Query | Selected scope | Returned grounding | Decision-relevant result | Disposition |
|---|---:|---:|---|---|
| Initial broad knowledge | 13 sources | `sources_used=[]`, no citation mapping | Returned a structural/semantic comparison, but without returned grounding metadata. | Excluded from new factual support; retained as a service/provenance observation. |
| Compact knowledge/correctness control | 6 sources | 6 used sources, 30 citation mappings | Separates structural schema validation from semantic proof; identifies position/family correlation and active multi-round debate as external research boundaries. | Accepted as source-grounded research, manually corrected against current code. |
| Harsh risk/failure-mode control | 5 sources | 5 used sources, 27 citation mappings | Raises position/length bias, missing active debate, stateless quota, external telemetry, and parser-failure concerns. | Accepted as adversarial input; several stale code claims are explicitly rejected below. |
| UX/implementability control | 5 sources | `sources_used=[]`, no citation mapping | Distinguishes CLI help/error/serialization mechanics from progress, human-task, visual, terminal, screen-reader, and WCAG proof. | Retained only as hypotheses and test design; it establishes no new source fact. |
| OSS-first composition control | 10 repositories | all 10 used sources, 183 citation mappings | Maps orchestration, red-team CI, metrics, benchmarks, optimization, tracing, and datasets to mature projects; warns against redundant composition. | Accepted as research; current GitHub metadata and licenses remain separately controlled. |
| Contradiction/source-attribution control | 6 sources | `sources_used=[]`, no citation mapping | Enumerates unsupported claims about semantic truth, provider independence, NotebookLM retrieval, durable quotas, injection defense, visual accessibility, and production telemetry. | Retained only as a falsification checklist because returned grounding metadata is empty. |

### Subsequent non-circular controls

A second set of fresh authenticated calls used the same 15 processed sources and continued to exclude every historical Tribunal report. These calls independently reproduced the service's conversation-ID reuse and supplied an additional grounding audit:

| Control | Returned grounding | Disposition |
|---|---:|---|
| Knowledge/correctness | 7 used source IDs, 21 citation mappings | Retain structural/semantic boundaries, position/family bias, and selective OSS composition; correct stale code claims directly. |
| Harsh risk | Initial call: 1 used source and 1 citation; compact capture: 0 and 0 | Retain only the cited position-bias claim; exclude the attractive five-risk compact prose as ungrounded. |
| UX/implementability | all 5 selected sources, 35 citation mappings | Retain terminal-test boundaries; Nielsen/WCAG remain criteria rather than passed visual or assistive-technology evidence. |
| OSS-first composition | all 10 selected repositories, 31 citation mappings | Retain capability/category mapping and the warning against composing all ten simultaneously. |
| Contradiction/source attribution | 13 used source IDs, 36 citation mappings | Retain the direct-control hierarchy; reject stale claims about gap validation, semantic mocks, and expected-error tracebacks. |

All subsequent calls again returned conversation ID `1ebabb83-484f-405b-8b24-a26cfa5b9afb` despite omitting continuation input. This is fresh-query proof, not conversation-isolation proof.

## Accepted synthesis

### Knowledge and correctness

- The corpus supports a distinction between validated output structure and verified target semantics. A schema-valid `BackendResult` can still contain false prose.
- Separate persona calls are process isolation only. The position-bias study supports concern about order effects and correlated same-family preferences; it does not prove that any particular Tribunal result is wrong.
- The multi-agent-debate paper studies active multi-round exchange. It is not evidence that this library's explicitly post-hoc `DebateSummary` has the same factuality effect.
- promptfoo, DeepEval, and Agent Framework expose adjacent executable evaluation or orchestration surfaces. Their existence supports composition, not automatic correctness of this project.

### Harsh criticism and risk

- Position/order, style/verbosity, correlated-model, prompt-contamination, and linguistic-evidence risks remain real integration concerns for any live LLM backend.
- The bundled engine manager is deliberately a per-call capacity planner, not a retry layer, durable quota ledger, rate-limit shield, or billing authority.
- The core has no built-in production trace store or OpenTelemetry exporter. Hosts that need those surfaces should compose an observability project rather than expand the dependency-free core without need.
- The post-hoc synthesis is not interactive cross-examination. The report and README must continue saying so.

### CLI UX and implementability

- Current source and execution can establish help discoverability, bounds, exit codes, JSON/Markdown serialization, installation, and no-traceback handling for expected errors.
- Neither source inspection nor a terminal-only run establishes progress comprehension, human task success, screen-reader quality, viewport behavior, contrast, or WCAG conformance. Nielsen and WCAG are criteria, not passed tests.
- The generated concerns about progress during long live-backend calls and operator interruption are plausible future human-test questions, not current release failures in the bounded offline package contract.

### OSS-first composition

- promptfoo is the leading adjacent choice for adversarial CI and red-team assertions.
- Microsoft Agent Framework is the current Microsoft production-orchestration direction; AutoGen remains useful prior art but its own repository notice controls maintenance/successor claims.
- DeepEval and Ragas cover application/RAG metrics; OpenAI Evals and lm-evaluation-harness cover benchmark execution; DSPy covers program optimization; Langfuse and Phoenix cover tracing/dataset workflows.
- A minimum deployment should add only the missing adjacent surface. The NotebookLM proposal to compose four projects at once is not automatically minimal and is not adopted as a blanket requirement.

## Manual corrections against current source and execution

The generated answers repeated stale or overstated claims from the `2026-07-20` source snapshot:

1. **`local-rules` is not a semantic mock pass.** A fresh critique run emitted three separate `local-rules` views at `40/100`, two explicit evidence gaps per view, `post-hoc-synthesis`, and `⚠️`. Its output states that it performed no network or semantic target inspection. It cannot emit a positive marker under that evidence state.
2. **Empty evidence gaps are supported.** Current `validate_backend_result` requires `findings` and `evidence` to be non-empty, but validates `evidence_gaps` as a list whose present items must be non-empty strings. `[]` is valid. The proposed empty-gap crash test targets stale code.
3. **Expected backend/input failures are caught.** Current `main` catches `OSError`, `RuntimeError`, `TypeError`, and `ValueError`, emits `tribunal: error: ...`, and returns exit code `2`. Fail-closed abortion of a malformed judge result is deliberate; it is not an uncaught raw crash.
4. **The synthesis makes no active-debate claim.** Current JSON names `debate.kind` as `post-hoc-synthesis`. The external debate paper cannot be transferred to this implementation.
5. **Skill labels do not execute external systems.** Routed labels such as `notebooklm` or `andrej-karpathy` are host-owned orchestration metadata. The local backend does not query NotebookLM and the synthetic persona is not an endorsement.

The current source still confirms meaningful limitations: no native semantic fact checker, provider-family enforcement, prompt-injection defense, persistent quota/billing authority, retry/backoff policy, live trace platform, or visual/human UX proof.

## IDR conclusion

The live processed-source corpus supports shipping Codex Tribunal only as a small, inspectable structural orchestration contract and reusable skill with an injectable evidence backend. It supports OSS-first composition for semantic evaluation, orchestration, adversarial CI, benchmarks, and observability instead of rebuilding those systems. It does not support presenting the bundled backend as semantic truth, live NotebookLM retrieval, statistically independent judging, active debate, durable quotas, production tracing, or accessibility proof.

Processed status, answer text, and citation mappings prove provenance only. Current primary metadata, exact source, and end-to-end execution remain controlling evidence.
