# Design

The executable contract is `scripts/tribunal_git.py`, documented in `docs/git-skill.md`. Requests bind an exact target commit and approved criterion/reviewer IDs. The skill uses the host's real isolated reviewers; local deterministic tests use explicit fixtures.

State is `ledger.json` on `refs/heads/tribunal/state-v1` in an explicitly approved private remote. A new commit with the observed parent and an ordinary push is the compare-and-swap. Losers cannot claim work. Expiring leases and monotone fences reject stale workers. This is cooperative coordination, not a distributed clock service or access-control boundary.

Conditions have stable reviewer-scoped IDs. A new target revision invalidates prior review applicability, not history. Resolution requires current evidence plus every configured reviewer's confirmation. Hard vetoes are never averaged away. GO completes only the review; `action_authorized` remains false. Host authorization governs merges, deployments and other effects.

Projection is generated output in Hans queue, OpenSpec condition supplement and receipts. Human-authored files cannot be overwritten. Existing control authorities stay authoritative; do not introduce a second independent claim source for the same task.

Raw evidence and model identity are host responsibilities. Hashes prove byte integrity, not truth, identity or semantic independence. The public repository contains no private raw sources. Provider calls, scheduler wiring and trusted reviewer identity remain explicit rollout gates.
