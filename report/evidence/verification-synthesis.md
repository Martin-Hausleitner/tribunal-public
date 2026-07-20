# Verification-pass post-hoc synthesis

Synthesis began only after the three accepted role outputs were frozen. The judges did not inspect one another. Scores `95`, `57`, and `85` are not averaged because the roles examined different surfaces and all accepted outputs share the Gemini model family.

## Agreements

- The local core is an inspectable structural orchestration contract, not a semantic evaluator.
- NotebookLM URLs and citations provide provenance, not proof that a characterization is correct.
- Persona/request separation is useful blind initial isolation but does not establish provider-family or statistical independence.
- The synthetic Karpathy-inspired critic requires its unendorsed/non-impersonation disclaimer on every output surface.
- Persistent provider budgets, retries, traces, injection defenses, calibration, and visual accessibility evidence belong outside the bundled dependency-free core.
- Markdown is the flattened display surface and JSON is the lossless surface.

## Material disagreements and disposition

| Finding | Judge position | Direct disposition |
|---|---|---|
| Canonical NotebookLM URL strictness | Critique: validator accepts queries/fragments and should block | **Accepted, extended, and fixed.** The CLI reproduced an exit-0 structural score for query/fragment input; final E2E additionally reproduced acceptance of literal `<id>`. `validate_notebooklm_url` now rejects params/query/fragment, invalid identifier characters, and named example identifiers. Focused tests and both source/installed console probes exit 2 without traceback. |
| Generic top-level `personas` namespace | Critique: release blocker; UX/knowledge: acceptable current package | **Retained as future breaking-migration risk.** Standard wheel install is the declared surface. A namespace rename is not a small compatible fix and requires collision evidence plus a major-version plan. |
| Zipapp/PEX resources | Critique: block because filesystem globbing can fail | **Not a current blocker.** Zipapp/PEX is neither documented nor tested as supported. Standard sdist/wheel/filesystem installation remains the release contract. |
| `_markdown_code` XSS | Critique: raw HTML metadata is executable | **Not reproduced.** The helper wraps the value in an adaptive Markdown code span; conforming Markdown renderers treat tags inside code spans as literal. The claim remains a renderer-specific gap, not an established vulnerability, pending a concrete unsafe target renderer. |
| Whitespace collapse | Critique: destructive; UX: low-friction trade-off | **Published behavior.** Markdown deliberately normalizes backend prose and JSON preserves the original values. It remains usability debt, not data loss across both surfaces. |
| Custom backend self-declaration | Critique: fake-green path; knowledge/UX: explicit boundary | **Accepted trust boundary.** Shape validation cannot make external evidence true. Live hosts must validate provenance and gaps independently. |
| Persona repetition | Critique: independence loss; other judges: documented | **Published boundary.** Nine personas rotate for three rounds, then repeat; explicit panels repeat every round. No statistical-independence claim is made. |
| Final gates | UX said report/CSV/skill gates passed | **Deferred to root verification.** The matrix timestamp changed during the judge window, so every gate is rerun only after final report and E2E evidence are frozen. |

## Controlling verdict

The hostile `57/100 Block` verdict controls the need to reproduce findings, not the final recommendation automatically. One real contract defect was reproduced and fixed. The remaining proposed blockers either concern unsupported distribution targets, require a breaking migration without present failure evidence, are explicit trust/non-capability boundaries, or lack a concrete unsafe renderer reproduction.

The final exact-wheel build, clean installation, installed console, installed Python API, deterministic release gates, and immutable artifact-publication check passed after the scoped repair. The evidence supports **Ship with conditions** for the narrow offline orchestration, persona-library, and reusable-skill scope. It does not support production semantic verification, visual accessibility success, provider-family independence, or durable runtime claims.
