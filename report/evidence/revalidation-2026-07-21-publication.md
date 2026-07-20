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
