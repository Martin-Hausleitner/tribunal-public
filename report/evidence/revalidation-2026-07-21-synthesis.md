# Current-pass Tribunal synthesis and finding disposition

## Inputs

- Frozen packet SHA-256: `59de53373a1386b2d14ed7d8d82ad6f9493d1d2247eefebd93df1069bb8b1521`
- Knowledge: Gemini 3.1 Pro High, `80/100`, `CONDITIONAL`
- Harsh criticism: Gemini 3.5 Flash High, `40/100`, `BLOCK`
- UX/implementability: Gemini 3.5 Flash Medium, `92/100`, `CONDITIONAL`

Three Grok 4.5 High calls failed with HTTP 402 before model output. The brief-authorized `agy` fallback supplied all accepted verdicts. All accepted models are Gemini-family; no provider-family/statistical independence is claimed. Scores are not averaged because roles and score rationales differ.

## Finding disposition

| Finding | Classification | Direct disposition |
|---|---|---|
| Current-pass proof was pending at judge time | Conditional proof requirement | Unit, compile, three-mode example, comparison CLI, build, wheel inspection, clean install, installed console/API, help, invalid-input, skill, CSV, report, and all named strict OpenSpec paths later exited as expected; publication remains fail-closed until remote equality and immutable retrieval complete. |
| CSV metadata was stale against the fresh GitHub snapshot | Reproduced current defect | Reproduced exactly: timestamp plus seven stars differed. Fixed by synchronizing the CSV to `2026-07-20T23:15:54Z`; `csv-gate` then passed 11 rows, one crown, score spread 53–85. |
| NotebookLM reused old conclusions/current-code assumptions | Generated-evidence failure | Preserved in the IDR ledger. Non-circular controls excluded the prior report; current exact source and executable behavior control conflicts. |
| Model/provider independence not enforced | Documented non-capability | README, packet, report, runtime provenance, and final limitations already say separate requests are not cross-family/statistical independence. No runtime change. |
| Synthesis is not interactive debate | Documented non-capability | Runtime serializes `kind=post-hoc-synthesis`; README/report state judges do not respond to siblings. No interactive debate claim is retained. |
| Markdown escaping is not prompt-injection defense | Documented non-capability | Markdown is display hardening; JSON is lossless; downstream agents must treat model prose as untrusted. No semantic-defense claim is retained. |
| Generic top-level `personas` namespace may collide | Future breaking-change risk | Current wheel contains all nine JSON resources and imports successfully from a clean environment. Universal coexistence is not proved. Keep as a planned major-version migration question, not a silent rename in this task. |
| Karpathy identity risk | Controlled current behavior | JSON and installed runtime preserve the synthetic, non-authored, non-endorsed, non-impersonation disclaimer plus three public repository references. |
| Critique score derived from local 40/50 ceiling | Judge-method error | Preserve the independent `40/BLOCK` output, but reject comparability: `local-rules` structural setup scoring and external product-review scoring are different instruments. |

## Agreements

- The thin standard-library core is coherent as structural orchestration plus an injected backend seam.
- `local-rules` is not semantic fact checking, live NotebookLM retrieval, visual testing, family diversity enforcement, persistent quota/billing, or trace storage.
- The final handoff must be gated by execution and immutable publication rather than model confidence.
- Mature OSS should supply adjacent red-team, orchestration, metric, benchmark, and observability capabilities.

## Material disagreements

- Knowledge and UX viewed the bounded contract as conditionally releasable; criticism blocked at the judge-time snapshot because matrix and proof were incomplete.
- The stale matrix was a real defect and was fixed. The provider/debate/injection items are real limitations but were already disclosed.
- UX treats the generic namespace as high severity; synthesis retains it as a future breaking-distribution concern because the claimed standard wheel surface works and no collision was reproduced.

## Synthesized verdict

Codex Tribunal remains the `85/100` crowned fit for the narrow declared use case only after deterministic gates and publication closure pass. The crown is project-authored and does not override the runtime `⚠️` produced by `local-rules`. Ship the library as an auditable offline review contract and reusable skill; compose promptfoo for adversarial CI, Agent Framework for larger agent workflows, and Langfuse/Phoenix-class tooling for durable live observability as required.

Do not market the core as semantic truth, interactive debate, visual accessibility proof, cross-family consensus, durable quota enforcement, or a production trace system.
