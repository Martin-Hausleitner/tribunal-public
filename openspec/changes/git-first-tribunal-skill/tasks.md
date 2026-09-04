# Implementation and rollout

- [x] Add public root SKILL.md and Git-first CLI without replacing legacy API.
- [x] Implement source deduplication and commit/policy binding.
- [x] Implement ordinary-push claims, lease renewal and fencing.
- [x] Preserve conditional work through fixes and fresh review.
- [x] Implement evidence checks, hard veto and bounded rounds.
- [x] Add safe Hans/OpenSpec projections and receipts.
- [x] Run 27 deterministic/real-local-Git tests and fresh-process roundtrip.
- [x] Author 11-system, 67-node, 13-view Squinch architecture.
- [x] Add read-only CI definition for tests and official Squinch render.
- [ ] Observe remote CI tests and successful official Squinch compilation.
- [ ] Independently review this implementation before production use.
- [ ] Verify parent Gitlinks, source coverage and startup routing in integration PRs.
- [ ] Wire and test a real host heartbeat plus actual isolated reviewers.
- [ ] Enforce private state-ref access, approved reviewers and clock policy in the host.
- [ ] Test a complete live issue -> claim -> reviews -> conditional fix -> fresh review -> host-authorized integration cycle.

A checked source/test item is not evidence that the unchecked live rollout is complete.
