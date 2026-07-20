# Verification-pass immutable publication closure

Observed UTC: `2026-07-20T22:51:25Z`

## Published artifact commit

- Full SHA: `d34ea93d754782576d100b8eff9712f710df9279`
- Branch: `master`
- Push: `e500e49..d34ea93  master -> master`
- `git ls-remote origin refs/heads/master`: `d34ea93d754782576d100b8eff9712f710df9279`
- SHA-pinned blob: https://github.com/Martin-Hausleitner/tribunal-public/blob/d34ea93d754782576d100b8eff9712f710df9279/report/codex-trib-lib-tribunal.md
- Blob HTTP result: `200`
- SHA-pinned raw retrieval compared with the local report through `cmp`: exit `0`, no difference
- Local and retrieved report SHA-256: `3e46db3f8a057b83ad741a5e7dcd1c171ee4e6c39a9738f20835a7cdfb03dd60`

This post-publication observation is preserved in a later closure commit rather than rewriting the already verified artifact commit. The final handoff separately verifies that closure commit and its SHA-pinned report surface.
