# Live-audit tribunal synthesis

The three accepted outputs were frozen before this synthesis. Scores are not averaged: `100`, `65`, and `89` answer different role-specific questions and reveal material disagreement.

## Accepted verdicts

| Perspective | Engine | Score | Recommendation |
|---|---|---:|---|
| Knowledge/correctness | `agy` / Gemini 3.1 Pro (High) | 100/100 | Ship |
| Hard criticism/risk | `agy` / Claude Sonnet 4.6 (Thinking) | 65/100 | Ship with conditions |
| UX/feasibility | `agy` / Gemini 3.5 Flash (High) | 89/100 | Ship with conditions |

All required Grok 4.5 high-effort paths failed before model execution with HTTP 402. The accepted fallback set has separate sessions but only two provider families; two judges are Gemini-family models. This is payload/session isolation, not statistical or cross-family independence. One GPT-OSS UX attempt and one summary-only Claude Opus critique attempt were discarded transparently because they did not satisfy the output contract.

## Agreements

- The dependency-free core is a coherent structural orchestration and backend-extension contract.
- `local-rules` is not semantic verification, visual UX inspection, NotebookLM retrieval, live quota discovery, or provider-family enforcement.
- Unique personas and separate calls are useful isolation but insufficient evidence of independent errors.
- JSON/provenance fields, explicit gaps, input bounds, packaging, and deterministic tests are strong.
- A live deployment needs external provider/model provenance, executable evidence, trusted budgets, and trace/visual surfaces appropriate to its claim.
- Current live-audit E2E, report, OpenSpec, and publication tasks had to complete after the judges' in-flight snapshots.

## Material disagreements

- The knowledge judge found no required fixes. It missed the standalone Markdown identity-disclaimer gap and report/CSV relational weakness, so its perfect score is preserved but does not control remediation.
- The risk judge treated the in-progress task ledger as a release blocker; that is correct at its snapshot but disappears only after every task and gate is actually closed.
- The risk judge called `https://github.com/dip/cmdk` broken. Live GitHub API checks showed `dip/cmdk` is reachable, unarchived, and the redirect target returned even when querying `pacocoursey/cmdk`; this finding is rejected.
- The UX judge treated whitespace flattening as a high-severity readability bug. The current behavior deliberately neutralizes untrusted backend-authored Markdown while JSON remains lossless. The usability cost is real, but blindly preserving Markdown structure would reopen rendering/injection risk; no change is warranted without a separately designed safe structured-rendering contract.
- Repeated explicit three-person panels are described as silent waste by UX. README already states exact repetition semantics. Warning behavior would be policy noise in a deterministic library and is not required for this release.
- Generic top-level `personas` packaging has collision risk, but renaming the public packaging layout is disproportionate to this evidence-only audit and no installation failure was observed.

## Confirmed actions

1. Surface an optional persona disclaimer in every serialized judge view and Markdown section so Karpathy-inspired output remains non-impersonating when detached from README/persona files.
2. Clarify that routed skill names are declared/advisory labels; the core neither checks installation nor invokes them.
3. Strengthen final report validation against the sibling CSV so candidate URLs, scores, snapshot, and crown cannot drift independently.
4. Keep the 11-row matrix update, including Microsoft Agent Framework and AutoGen's maintenance-mode status.
5. Rerun the public CLI/package E2E, current OpenSpec validation, all tests/gates, and remote publication checks.

## Rejected or bounded actions

- Do not claim three-family or statistical independence.
- Do not add a bundled provider, durable engine, trace platform, or browser surface to the dependency-free core.
- Do not treat a backend's empty evidence-gap list as independently verified truth; retain the existing explicit documentation and regression coverage.
- Do not replace `dip/cmdk`; the live canonical check disproved the critique claim.
- Do not preserve arbitrary backend Markdown wholesale; JSON remains the lossless surface.
- Do not add cross-run quota state to a component explicitly scoped as a per-run planner.

## Synthesis verdict

Ship the library and skill for their bounded offline orchestration scope after the confirmed identity/documentation/report-gate fixes and current live-audit gates pass. The crown remains use-case-specific: Codex Tribunal is the best fit for the narrow three-perspective review contract, while promptfoo is the stronger ready-made adversarial regression tool and Microsoft Agent Framework is the stronger production multi-agent runtime. The report must state that the external judge set used an authorized fallback with two provider families and must retain every unresolved production-live limitation.
