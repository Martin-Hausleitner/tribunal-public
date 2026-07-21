# Current-pass Tribunal synthesis and finding disposition

## Inputs

- Frozen packet SHA-256: `a5cda94bf1b2bbff444e37f15767357565c981bf700d9247bab3e74b118dddbf`
- Knowledge: Gemini 3.5 Flash Low, `80/100`, `Ship`
- Harsh criticism: Gemini 3.5 Flash High, `73/100`, `Ship with conditions`
- UX/implementability: Gemini 3.5 Flash Medium, `94/100`, `Ship with conditions`

Three Grok 4.5 High calls failed with HTTP 402 before model output. The brief-authorized `agy` fallback supplied the accepted verdicts after quota-, timeout-, mount-, and provenance-invalid attempts were excluded. All accepted models are Gemini-family; no provider-family or statistical independence is claimed. Scores are not averaged because the roles and score rationales differ.

## Finding disposition

| Finding | Classification | Direct disposition |
|---|---|---|
| Current semantic/backend proof boundary | Documented non-capability | `local-rules` remains structural only. The installed API E2E proves the backend seam and marker mechanics, not truth of injected prose. |
| NotebookLM historical-source hallucinations | Generated-evidence failure | Preserved in the IDR ledger; current exact source, GitHub primary metadata, and execution control conflicts. |
| Descending-score `strongest_points` may emphasize lenient findings | Terminology/design enhancement | Reproduced behavior, but no claimed contract says `strongest_points` is a severity queue. `disagreements` retains the first finding from every view and `recurring_failures` retains repeated gaps. Do not silently change semantics in this evidence-only pass. |
| Exact-string recurrence misses paraphrased gaps | Deliberate deterministic limitation | The core claims exact structural aggregation, not NLP equivalence. Fuzzy matching would add unstable semantics; leave for a separately specified backend/policy. |
| Markdown collapses backend line breaks | Documented output trade-off | README explicitly distinguishes normalized Markdown from lossless JSON. No preservation claim is retained. |
| Capacity is stateless across calls | Documented non-capability | README requires durable budgets/billing at a trusted external boundary. |
| Skill labels are not executed | Documented non-capability | Host validation/execution remains explicit. |
| CLI lacks persona enumeration | UX enhancement | Mode choices and all options are discoverable in `--help`; persona slugs remain documented/package resources. Consider a future `--list-personas` change, not a release blocker. |
| Default structural `⚠️` can be misread | UX/documentation risk | README and report explain that warning means unresolved semantic evidence, not command failure. Lowering the pass threshold would create fake green. |
| Visual/accessibility proof absent | Explicit scope boundary | Require external viewport, keyboard, contrast, reflow, assistive-technology, and human-task evidence before a visual pass. |
| Generic top-level `personas` namespace may collide | Future breaking-change risk | Clean wheel install/import and all nine resources work. Universal coexistence is unproved; retain as a future major-version migration concern. |

## Agreements

- The thin standard-library core is coherent as structural orchestration plus an injected backend seam.
- `local-rules` is not semantic fact checking, live NotebookLM retrieval, visual testing, provider-family enforcement, persistent quota/billing, or trace storage.
- Persona identity disclosure, bounded inputs/errors, deterministic output schemas, and explicit gaps are valuable controls.
- Mature OSS should supply adjacent red-team, orchestration, evaluation, optimization, and observability capabilities.
- Final release truth comes from current source, clean install/API/CLI behavior, deterministic gates, and immutable publication, not judge confidence.

## Material disagreements

- Knowledge recommends unconditional shipment of the bounded core at `80`; criticism and UX require conditions at `73` and `94`.
- Criticism treats synthesis ordering and exact recurrence as material risks; synthesis retains them as explicit deterministic semantics/enhancement questions because no loss or false positive was reproduced on the claimed surface.
- UX seeks persona enumeration and clearer warning terminology. These are reasonable next increments, but current help, README, and structural-gap wording satisfy the published CLI contract.

## Synthesized verdict

Codex Tribunal remains the `85/100` crowned fit for the narrow declared use case only after deterministic gates and immutable publication pass. The crown is project-authored and does not override the runtime `⚠️` produced by `local-rules`. Ship the library as an auditable offline review contract and reusable skill; compose promptfoo for adversarial CI, Agent Framework for larger workflows, and Langfuse/Phoenix-class tooling for durable observability as required.

Do not market the core as semantic truth, interactive debate, visual accessibility proof, cross-family consensus, durable quota enforcement, or a production trace system.
