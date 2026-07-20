# Live brief revalidation baseline

Collection date: `2026-07-20`

## Repository

- Worktree: `/home/coder/tribunal-public`
- Starting branch: `master`
- Starting full commit: `9f1dc36899a530ad4477784b3d12e1fd5c302da1`
- Starting remote: `origin https://github.com/Martin-Hausleitner/tribunal-public.git`
- Starting tracked state: clean
- Public report, structured matrix, evidence ledgers, runtime, tests, nine persona JSON files, skill, examples, build metadata, and multiple completed OpenSpec changes were present.
- During the run, an unrelated untracked `openspec/changes/verify-complete-codex-tribunal-library-brief/` directory appeared. It was treated as another actor's work, not edited, and excluded from this pass's staging scope.

## Weekly guard

The required VCVM guard returned:

```text
session_used=9
session_left=91
session_reset=0s
weekly_used=65
weekly_left=35
weekly_reset=575724s
fast=not_seen
status=LIMIT_GUARD
```

Because weekly usage exceeded the 50 threshold, this pass started no Codex/OMX team burst. It used only the brief-mandated Grok attempts and authorized `agy` fallbacks. No fast mode was used.

## Sanitized tool state

- `nlm 0.8.9`
- `grok 0.2.102`
- `agy`: available with Gemini 3.1 Pro, Gemini 3.5 Flash, Claude 4.6, and GPT-OSS 120B entries
- `openspec 1.4.1`
- `Python 3.12.3`
- `build 1.5.0`
- `git 2.43.0`

Authentication checks recorded only validity and resource access; account identifiers, cookies, and tokens are omitted.

## OpenSpec-first gate

A distinct pass-specific change was created at [`../../openspec/changes/revalidate-trib-codex-trib-lib-brief/`](../../openspec/changes/revalidate-trib-codex-trib-lib-brief/) before NotebookLM queries or external judge calls. Proposal, Design, one capability Spec, and a 35-task checklist were apply-ready and `openspec validate ... --strict` exited `0`.

