# Final live judge synthesis and direct dispositions, 2026-07-21

Packet SHA-256: `912f24d6b2503c5e07605f198df0ca4875a840bc9daff7617c7df42669c1aa74`

Accepted role scores are retained independently: knowledge `85/100`, harsh criticism `73/100`, and UX/implementability `85/100`. They are not averaged because the roles weight different failure surfaces and all accepted calls share the Google Gemini family.

## Agreements

- The dependency-free core is coherent only as structural orchestration with an injectable backend seam.
- `local-rules` is not semantic fact checking, NotebookLM retrieval, skill execution, visual inspection, provider-family enforcement, durable quota/billing, or production tracing.
- Separate personas and requests provide request isolation, not independent model errors or interactive debate.
- The explicit evidence/gap/provenance schemas, concise expected errors, package surface, and non-impersonation disclaimer are strong bounded contracts.
- Full source/build/wheel/clean-install/API/error/report/publication gates are conditions of release.
- UI/UX mode has no visual, accessibility, assistive-technology, or human-task proof.
- Mature OSS should supply red-team CI, semantic metrics, production orchestration, benchmarks, optimization, and observability rather than expanding the thin core by default.

## Material disagreements and direct disposition

1. **Structural NotebookLM point as false assurance.** Criticism treated the optional `40→50` structural increase as high risk. Current output and README explicitly say the URL is syntactic/unqueried provenance, retain evidence gaps, cap at `50`, and cannot award a comparison crown. The misuse scenario is real if a consumer discards backend and gap fields, but no published contract is violated. Retain the warning; no runtime change.
2. **Raw JSON as unescaped injection.** `json.dumps` correctly JSON-escapes syntax while intentionally preserving the backend's exact natural-language values. The focused markup test passes. README already states that a backend is untrusted code, its prose is untrusted input, and rendering hardening is not prompt-injection defense. This is a downstream trust boundary, not malformed serialization.
3. **Invalid persona failure described as mid-run.** `PersonaLibrary.select` is called while all panels are built before engine allocation or any `backend.evaluate` call. A direct invalid-persona CLI control returned one concise `tribunal: error:` line and exit `2`. Validation occurs after CLI parsing but before any judge side effect; no partial run defect reproduced.
4. **`DebateSummary` naming.** The noun can create an expectation, but the serialized kind is exactly `post-hoc-synthesis`, and README/skill explicitly deny interactive debate. A breaking rename is not justified in this verification pass.
5. **Stateless quota and declared skill routes.** Both behaviors are real and explicitly documented as host-owned boundaries. They are not silent production controls and therefore are not defects in the published thin-core scope.
6. **Persona tie-breaking and Markdown line collapse.** Both are deterministic documented/observable behaviors. JSON remains lossless, complete findings remain serialized, and no unbiased random selection or preserved Markdown layout is claimed. They remain optional ergonomic enhancements.

## Reproduced controls

- Fresh `local-rules` critique: three `40/100` views, explicit gaps, `post-hoc-synthesis`, `⚠️`.
- Valid `BackendResult(..., evidence_gaps=[])`: accepted.
- Invalid persona list: concise exit `2`, no traceback, and selection occurs before backend evaluation.
- Backend markup test: Markdown escaping passes while JSON preserves values.
- Skill/README inspection: structural ceiling, host-owned skill labels, post-hoc boundary, stateless capacity, untrusted backend prose, and visual-proof requirement are all explicit.

No current runtime, persona, package, or skill defect requiring code repair was reproduced from the accepted judgments. Final release remains conditional on the complete executable and publication gates.

## Synthesized verdict

Ship Codex Tribunal for the bounded offline orchestration and reusable-skill scope, with conditions: preserve every explicit limitation, require a real evidence backend for semantic claims, compose mature OSS for adjacent capabilities, and publish only after the full clean-install/E2E/public-blob gate passes. Do not market the local backend as semantic truth, the three calls as provider-independent judges, post-hoc synthesis as active debate, or text-only UI/UX output as visual/accessibility proof.
