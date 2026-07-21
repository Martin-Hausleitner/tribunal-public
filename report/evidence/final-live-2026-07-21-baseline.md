# Final live verification baseline, 2026-07-21

Observation window began after the repo-local OpenSpec proposal was present and before any current-pass NotebookLM query, external judge call, report edit, matrix edit, or runtime edit.

## Repository

- Branch: `master`
- Starting local SHA: `990a8df200716a446472faf4110a2e896c52ab40`
- Starting `origin/master`: `990a8df200716a446472faf4110a2e896c52ab40`
- Remote: `https://github.com/Martin-Hausleitner/tribunal-public.git`
- Worktree: no tracked modification and no unrelated untracked file; the only entry was the expected new `openspec/changes/final-live-tribunal-verification-2026-07-21/` planning directory.
- GitHub API identity: `Martin-Hausleitner/tribunal-public`, visibility `public`, default branch `master`, public repository URL `https://github.com/Martin-Hausleitner/tribunal-public`.
- GitHub CLI authentication was valid. No token, cookie, credential body, or collaborator address is retained in this ledger.

## Weekly guard

The required VCVM guard returned at `2026-07-21T00:39:57Z`:

- `session_used=9`, `session_left=91`, `session_reset=0s`
- `weekly_used=88`, `weekly_left=12`, `weekly_reset=565402s`
- `fast=not_seen`
- `status=LIMIT_GUARD`, `mode=check`

Because weekly use exceeded 50, this pass is Priority-only and starts no expensive Codex/OMX team burst. The brief-required external Grok/`agy` judge paths remain in scope. Fast mode was not visible and was not enabled.

## Tool surface

- Python `3.12.3`
- build `1.5.0`
- NotebookLM CLI `nlm 0.8.9`
- Grok CLI `0.2.102 (ab5ebf69ac)`
- `agy 1.1.4`
- OpenSpec `1.4.1`
- GitHub CLI `2.88.0`

All required executables resolved from the current environment. `nlm login --check` subsequently returned valid authentication and exactly `500` notebooks; the account identity is intentionally redacted here.

## OpenSpec-first gate

The repo-local change `final-live-tribunal-verification-2026-07-21` contains a proposal, design, one capability specification, and a 61-item checklist. Before current-pass live research or judge calls:

```text
openspec validate final-live-tribunal-verification-2026-07-21 --strict
Change 'final-live-tribunal-verification-2026-07-21' is valid
```

`openspec instructions apply ... --json` reported schema `spec-driven`, state `ready`, progress `0/61`, repo-local edit scope, and no workspace-planning restriction.
