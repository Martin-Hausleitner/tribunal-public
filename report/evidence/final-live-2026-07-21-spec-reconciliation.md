# Final live specification reconciliation, 2026-07-21

Capability spec: `openspec/changes/final-live-tribunal-verification-2026-07-21/specs/final-live-brief-verification/spec.md`

This ledger maps every normative requirement and scenario to direct current-pass evidence. Publication rows intentionally remain open until the corresponding remote operations are observed; no inherited branch state closes them.

| Requirement / scenario | Evidence | Pre-publication verdict |
|---|---|---|
| OpenSpec-first / planning precedes implementation | Proposal, design, spec, 61-task checklist; strict validation in `final-live-2026-07-21-baseline.md` | Pass |
| Authenticated canonical NotebookLM / identity and sharing | `final-live-2026-07-21-notebooklm.md`: valid authentication, canonical ID/title/link, `is_public=true` | Pass |
| NotebookLM / capacity fails safely | Initial `942/600/342`; two current-source insertions settled failed; final `944/600/344`; no pre-existing content deleted or repurposed | Pass |
| Source-grounded cross-query / auditable role queries | Two non-circular batches, explicit source sets, returned used-source/citation counts, query dispositions, repeated conversation-ID limitation | Pass |
| Source-grounded cross-query / prior reports do not prove current claims | Historical Tribunal report sources excluded; empty/weak grounding excluded; source/runtime corrections retained | Pass |
| Three independent adversarial verdicts / preferred Grok path | Three role-specific `grok --single -m grok-4.5 --effort high` calls observed; all HTTP 402 before output | Applicable branch observed; no Grok verdict existed |
| Three independent adversarial verdicts / authorized fallback | `final-live-2026-07-21-external-attempts.md`; three accepted hash-bound `agy` verdicts and all excluded quota/scope attempts | Pass |
| OSS-first comparison / current candidate metadata | Eleven canonical REST identities, numeric stars, push/archive state, root license/maintenance controls in JSON and OSS ledger | Pass |
| OSS-first comparison / popularity does not determine fit | Six weighted dimensions sum to 100; stars add zero; 11 differentiated rows; arithmetic gate passed | Pass |
| One bounded winner and implementation plan / unambiguous crown | CSV/report contain exactly one `👑`, Codex Tribunal `85/100`, narrow-use-case disclaimer, composition plan, and Mermaid flow | Pass |
| Real E2E / installed package workflow | `final-live-2026-07-21-e2e.md`: fresh sdist/wheel, contents, isolated install, installed two-round CLI, live GitHub REST backend, gap-preserving marker | Pass |
| Real E2E / artifacts agree | Skill/CSV/report/OpenSpec gates pass; canonical URL, 11 repos, scores, snapshot, winner, gaps, and disclaimers cross-check | Pass |
| Evidence-class separation / generated contradiction resolved | NotebookLM, GitHub, judges, scoring, runtime, synthesis, and E2E use separate ledgers; direct code/runtime overruled stale generated claims | Pass |
| Fail-closed public handoff / publication verifiable | Requires a new commit, local/remote SHA equality, and SHA-pinned public report retrieval | Open until publication |
| Fail-closed public handoff / a gate fails | Grok/quota/grounding failures were retained and excluded; report gate caught and required removal of an unfinished-marker word; no false success substituted | Pass |

## Current executable gate summary

- Source examples and concrete two-round comparison: pass.
- Unit suite: `18/18` pass; compile: pass.
- PEP 517 sdist/wheel and contents: pass.
- Fresh wheel install, installed console/API, live GitHub REST evidence backend: pass.
- Five expected-error paths: exit `2`, concise error, no traceback.
- Skill, CSV, report, strict OpenSpec, score/link/snapshot consistency: pass.
- Frozen judge packet content identity: `912f24d6b2503c5e07605f198df0ca4875a840bc9daff7617c7df42669c1aa74`.

Final status is withheld until the publication row is replaced with exact remote SHA, HTTP, and content-identity evidence.
