# NotebookLM IDR revalidation (2026-07-21)

IDR: ja

- Recorded window: `2026-07-20T23:08Z` through `2026-07-21T00:11Z`
- Canonical public notebook: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515
- Notebook ID: `80cffd38-0185-4f4d-ae00-bbc67c4bc515`
- Title: `Tribunal IDR 2026-07-04`
- Authenticated CLI: `nlm 0.8.9`; authentication and public-sharing checks exited `0`
- Final directly reduced inventory: `875` total, `600` processed (`status=2`), `275` failed (`status=3`)

No credential, account identifier, cookie, token, collaborator identity, or private notebook title is retained.

## Capacity handling and failed sources

The canonical notebook was already at its exact 600-processed-source ceiling. Two concurrent, uniquely titled current-pass manifest additions returned source IDs but settled at status `3` with empty content:

- `ac80cbf6-cad3-491d-b8da-734ba78ec48b`
- `b2183fdb-123d-45b0-a810-f8f8872d1f2f`

Creating a fresh notebook also failed safely with API code `3` / `INVALID_ARGUMENT` while the authenticated inventory contained exactly `500` notebooks. No unrelated notebook or processed source was deleted, renamed, or repurposed. Both failed manifest sources are excluded from every query and cited nowhere as research.

The safe live path was therefore the existing canonical notebook with explicit processed source IDs, fresh conversation IDs, a pass-specific query ledger, and current GitHub/runtime controls outside NotebookLM.

## Selected processed source set

### Current code/project anchors available in the corpus

- `fe7a231f-4c3e-4039-81e4-7c71cf95ea61` — `tribunal.py source snapshot 2026-07-20`
- `c0534b8b-76ec-4ee3-a36b-121d9327a41a` — prior live-audit report, used only as historical context and never as controlling proof for this pass

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

### Criteria and bias sources

- `e390f1fb-bdae-43b5-86aa-55af5578aa80` — multi-agent-debate paper
- `92a44e33-1f12-4454-a4c2-e5e97feb8f98` — ACL position-bias study
- `4fd90dd9-426b-4d47-aaa3-c972c98f14fe` — Nielsen Norman Group usability heuristics
- `6bfa3b74-65f3-4361-b7de-e9ce3ae20f6c` — W3C WCAG 2.2 Quick Reference

## Broad role queries

Each broad query used a fresh conversation UUID and an explicit source-ID list:

| Role | Conversation | Returned grounding used for audit | Disposition |
|---|---|---|---|
| Knowledge/correctness | `5df53cc5-0fad-4e42-9caa-960fe7142b3e` | Initial answer returned 12 selected source IDs and 50 citation mappings | Retain structural/non-capability boundaries; reject historical stars and current-code claims until externally controlled |
| Harsh criticism/risk | `29840410-53f5-44a3-abda-d85b6306d29e` | Compact control returned the ACL study and historical report | Retain systematic bias risk; historical release defects are not assumed current |
| CLI UX/feasibility | `615ae36c-b7f2-4f11-8610-7c6fb6a976f3` | Compact control cited only the historical report | Insufficient for new facts; superseded by the no-report UX control below |
| OSS-first synthesis | `7073062b-864e-465e-87ce-43df8321f154` | Compact control cited only the historical report | Insufficient for new facts; superseded by the ten-repository control below |
| Contradiction/source attribution | `9ef326eb-dd3d-4456-801b-ca12dc037773` | ACL position-bias study plus historical report | Retain evidence hierarchy and bias warning; require direct code/execution for all runtime claims |

The broad knowledge answer correctly separated structural orchestration from semantic, visual, retrieval, family-independence, durable-quota, and observability claims. It also repeated stale stars, an old AutoGen score/order, and snapshot behavior as though current. Those mutable claims were excluded.

## Non-circular controls

Because several broad follow-ups over-relied on the earlier report, four new conversations excluded that report entirely:

### Knowledge/control

- Conversation: `987a101b-7589-4050-b6f9-4e81f26147a6`
- Returned grounding: 13 selected sources and 34 citation mappings: code snapshot, all ten OSS repositories, multi-agent-debate paper, and ACL position-bias study.
- Retained: strict score/result boundaries are visible in the snapshot; alternatives provide complementary red-team, metric, orchestration, benchmark, optimization, and observability surfaces; systematic judge bias prevents equating separate role prompts with statistical independence.
- Correction: the paper's multi-round-debate results are external research, not proof that Tribunal's post-hoc synthesis produces the same effect.

### Harsh-critique/control

- Conversation: `707b3956-8b3c-4041-a83d-8e8d1e96bf28`
- Returned `sources_used`: only the ACL position-bias study, despite prose naming other selected sources.
- Retained: judge/task dependence and answer-quality-gap sensitivity are credible deployment risks.
- Rejected: an asserted multi-round collusive conversation cannot apply directly because current `JudgeRequest` does not conduct interactive sibling debate; strict validation and fail-closed capacity are documented behavior, not reproduced defects.

### UX/control

- Conversation: `6b77552b-389d-4b68-a52c-a649d79c28c9`
- Returned grounding: code snapshot, promptfoo, Microsoft Agent Framework, Nielsen heuristics, and WCAG Quick Reference.
- Retained: CLI execution can establish discoverability, parsing, bounds, error mechanics, serialization, and installability. It cannot establish viewport layout, contrast, focus order, screen-reader behavior, or human task completion. Nielsen/WCAG are criteria only.
- Rejected: an Azure CLI authentication aside was irrelevant to this dependency-free local package.

### OSS/control

- Conversation: `c947474f-934f-4f90-b8e1-9dcfc4026322`
- Returned grounding: all ten canonical OSS repository source IDs.
- Retained composition: promptfoo for adversarial CI/red-team checks; Agent Framework for production multi-agent workflows; DeepEval/Ragas for metrics; Langfuse/Phoenix for live traces and datasets; OpenAI Evals/lm-evaluation-harness for benchmark runners; DSPy for program optimization. AutoGen is maintenance-mode prior art whose README directs new users to Agent Framework.
- Correction: composing all ten simultaneously would be needless complexity; select only the adjacent capability a deployment actually needs.

## Final live read-only cross-query

At `2026-07-21T00:11Z`, authenticated identity, public sharing, the `875/600/275` source inventory, and the selected processed-source presence were rechecked without modifying the notebook. A final four-lens cross-query covered knowledge/correctness, harsh risk, CLI UX/implementability, and OSS-first composition using the current code snapshot, ten OSS sources, the debate/bias sources, Nielsen heuristics, and WCAG criteria.

- Conversation returned by the CLI: `1ebabb83-484f-405b-8b24-a26cfa5b9afb`. This identifier was reused by NotebookLM despite omitting `--conversation-id`, so this call proves a fresh live query, not fresh-conversation isolation.
- Returned grounding: `10` actually used source IDs and `37` citation mappings.
- Retained: the structural-versus-semantic boundary, judge-family correlation risk, absence of visual/accessibility proof, and composition with promptfoo, evaluation frameworks, and observability tooling.
- Rejected against current source/execution: `LocalRulesBackend` is not a mock; valid empty `evidence_gaps` are supported; expected CLI validation/backend errors are caught and returned as concise exit `2` messages without traceback; static skill labels do not execute NotebookLM.
- Qualified: proposals for position swapping, cross-family routing, progress UI, durable budgets, and external tracing remain optional future integrations, not current capabilities or release blockers.

## Direct controls that outrank generated prose

The NotebookLM code snapshot predates current code commit `d34ea93d754782576d100b8eff9712f710df9279`. Exact current-source inspection established:

- `validate_notebooklm_url` now rejects query strings, fragments, documentation placeholders, and invalid ID characters; the older snapshot omitted some of those controls.
- `validate_backend_result` requires non-empty `findings` and `evidence` but correctly permits an empty `evidence_gaps` list; NotebookLM repeated the older non-empty-gap rule.
- `EngineManager.allocate` copies configured capacities per call and fails closed when one run cannot be planned; it is not a durable quota or billing authority.
- `local-rules` scores structure only: `40/100` without a NotebookLM reference and `50/100` with one, always with explicit gaps.
- The Karpathy-inspired persona retains a non-endorsement/non-impersonation disclaimer and three public repository references.

Current GitHub REST/license reads and the final executable E2E control every mutable repository, license, packaging, and runtime claim.

## IDR conclusion

Live selected-source research supports retaining Codex Tribunal as a small, inspectable offline review contract and reusable skill. It supports OSS composition instead of rebuilding evaluation, orchestration, or observability platforms. It does not support marketing the local backend as semantic truth, NotebookLM retrieval, visual accessibility proof, statistically independent judging, persistent quotas, or live trace storage.

Processed status and citation mappings prove provenance, not correctness. Exact source, primary metadata, and execution remain the controlling evidence hierarchy.
