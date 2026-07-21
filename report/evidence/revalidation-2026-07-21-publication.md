# Current-pass immutable publication closure

This ledger is intentionally completed only after the final local gates pass. It records the first public verification commit, remote equality, clean-tree check, SHA-pinned retrieval, HTTP result, and content-identity proof. A later closure commit may add this observed evidence and completed OpenSpec task state; the final handoff separately verifies and reports that later commit's SHA-pinned report URL.

## First public verification stage

- Observed UTC: `2026-07-20T23:50:35Z`
- Verification commit: `566147a39751e7449581123e40caf1f015d8147b`
- Local `HEAD`, local `origin/master`, live `refs/heads/master`, and the GitHub commit API all returned that full SHA.
- SHA-pinned raw report: HTTP `200`
- SHA-pinned GitHub blob page: HTTP `200`
- Local committed report SHA-256: `17f5dfe1d6e0a5acd9df4b058c0bd0b86c8af6fc30f66c945bb63c705fac691e`
- Public raw report SHA-256: `17f5dfe1d6e0a5acd9df4b058c0bd0b86c8af6fc30f66c945bb63c705fac691e`
- Immutable blob URL: https://github.com/Martin-Hausleitner/tribunal-public/blob/566147a39751e7449581123e40caf1f015d8147b/report/codex-trib-lib-tribunal.md

The tree was intentionally not claimed clean at this stage because the pass-specific OpenSpec closure and this observed publication evidence still had to be committed. A later closure stage records remote equality and a clean tree after those files are included.

## Closure-stage verification

- Observed UTC: `2026-07-20T23:52:28Z`
- Closure commit: `8c2d4019035ce18bdf2f3f323e540a316d43a37d`
- Local `HEAD`, local `origin/master`, and live `refs/heads/master` all returned that full SHA.
- `git status --porcelain=v1` returned no path before this observation was added to the ledger.
- SHA-pinned raw report: HTTP `200`
- SHA-pinned GitHub blob page: HTTP `200`
- Local committed report SHA-256: `17f5dfe1d6e0a5acd9df4b058c0bd0b86c8af6fc30f66c945bb63c705fac691e`
- Public raw report SHA-256: `17f5dfe1d6e0a5acd9df4b058c0bd0b86c8af6fc30f66c945bb63c705fac691e`
- Immutable closure-stage blob URL: https://github.com/Martin-Hausleitner/tribunal-public/blob/8c2d4019035ce18bdf2f3f323e540a316d43a37d/report/codex-trib-lib-tribunal.md

This observed clean/equal stage satisfies the final OpenSpec publication condition. The later evidence-only commit that stores this section and the completed checkbox is verified separately in the final handoff; it does not change the report payload.

## Judge-chain repair and closing-refresh publication stage

- Observed UTC: `2026-07-21T00:21:16Z`
- Judge-chain repair commit: `6cc710da52892f3cb596a9885e6ee5a65852f74e`
- Closing live-evidence refresh commit: `b2cb34bedb478e2d71130d9c52ccd604f987f709`
- Local `HEAD`, local `origin/master`, live `refs/heads/master`, and the GitHub commit API all returned the closing-refresh full SHA.
- `git status --porcelain=v1` returned no path before this observation was added to the ledger.
- SHA-pinned raw report: HTTP `200`
- SHA-pinned GitHub blob page: HTTP `200`
- Local committed report SHA-256: `8b52edb4026dcc17df293dfb341a2710ac8b8024d8566896f21cf2333eba0f52`
- Public raw report SHA-256: `8b52edb4026dcc17df293dfb341a2710ac8b8024d8566896f21cf2333eba0f52`
- Immutable repaired-report URL: https://github.com/Martin-Hausleitner/tribunal-public/blob/b2cb34bedb478e2d71130d9c52ccd604f987f709/report/codex-trib-lib-tribunal.md

The repair did not relabel the earlier unverifiable transient judge packet. It published three later isolated verdicts that actually used committed packet SHA-256 `a5cda94bf1b2bbff444e37f15767357565c981bf700d9247bab3e74b118dddbf`: Knowledge `80/100`, Critique `73/100`, and UX `94/100`. The closing refresh then synchronized the final authenticated NotebookLM control and the `2026-07-21T00:12:42Z` eleven-repository GitHub snapshot without changing the `85/100` score or single Codex Tribunal crown.

Adding this observed publication record initially dirtied only this ledger. A subsequently completed installed-wheel verification updated the report and E2E ledger before this publication record was committed. The final commit containing those three files therefore receives its own report hash and is verified separately in the handoff; that later immutable result supersedes `b2cb34b` as the final URL without invalidating the historical observation above.

## Final installed-wheel and report publication stage

- Observed UTC: `2026-07-21T00:25:34Z`
- Final report/E2E commit: `2f796a97b0aa8eb5891abf4d2a8d999be89a181f`
- Local `HEAD`, local `origin/master`, live `refs/heads/master`, and the GitHub commit API all returned that full SHA.
- `git status --porcelain=v1` returned no path before this observation was added to the ledger.
- SHA-pinned raw report: HTTP `200`
- SHA-pinned GitHub blob page: HTTP `200`
- Local committed report SHA-256: `5181736f906814f198299b36dd28df313114f9a604737d363d0f8009ef8a6e74`
- Public raw report SHA-256: `5181736f906814f198299b36dd28df313114f9a604737d363d0f8009ef8a6e74`
- Immutable final-report URL: https://github.com/Martin-Hausleitner/tribunal-public/blob/2f796a97b0aa8eb5891abf4d2a8d999be89a181f/report/codex-trib-lib-tribunal.md

This stage includes the fresh no-dependency installed-wheel Console/API proof and changes the report evidence hash relative to `b2cb34b` without changing the `85/100` matrix score or the single Codex Tribunal crown. Adding this observation dirties only the publication ledger; its following ledger-only commit does not change the report payload.
