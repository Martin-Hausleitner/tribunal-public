# Git-first Tribunal v2

## What is implemented

A dependency-free Python CLI provides paginated GitHub/local-ticket discovery, explicit intake, durable Git transactions, single-winner claims, expiry/renewal/fencing, commit-bound packet/evidence validation, a bounded conditional-fix/re-review state machine and regenerable Hans/OpenSpec projections. The legacy Python library remains intact.

State is `ledger.json` on the dedicated `refs/heads/tribunal/state-v1` in an approved private repository. Each successful transition creates a child commit of the previously fetched head and uses a normal push. Competing commits share a parent: only one can advance the ref; the other fails closed. A network error is not success. No force push, shell interpolation, remote auto-selection or execution of issue bodies exists.

Git write permission is the trust boundary. Claims are cooperative, clocks must be synchronized and administrative ref rewrites must be prevented by the host/forge policy. This is not a Byzantine consensus system, cryptographic reviewer identity or protection from an authorized writer deliberately bypassing the tool. For large installations move coordination behind the existing control authority rather than creating competing claim authorities.

## Review packet

```json
{
  "mode": "live",
  "target_commit": "<40-character Git SHA>",
  "evidence": [{"id": "tests", "path": ".proof/tests.txt", "sha256": "<64 hex>", "target_commit": "<same SHA>"}],
  "resolutions": {},
  "reviews": [{
    "reviewer": "correctness", "session": "fresh-session-1",
    "target_commit": "<same SHA>", "isolated": true,
    "provenance": "host-asserted", "verdict": "CONDITIONAL_GO",
    "criteria": {"ac-1": {"status": "conditional", "evidence": ["tests"]}},
    "conditions": [{"id": "fix-1", "criterion": "ac-1", "fix": "Concrete correction and acceptance test"}],
    "resolved_conditions": []
  }]
}
```

The abbreviated example shows one reviewer; real submissions must contain every configured reviewer (3–12 unique IDs/sessions). `GO`, `CONDITIONAL_GO`, `NO_GO`, `NEEDS_EVIDENCE` and `NEEDS_HUMAN` are supported. Each criterion status is `pass`, `conditional`, `block` or `missing`. After correction, submit fresh packets, set `resolutions` to e.g. `{"correctness.fix-1": ["tests"]}`, and have every reviewer name that condition in `resolved_conditions`.

The gate checks the exact checkout HEAD, tracked cleanliness, confined nonempty evidence files and their hashes. It does not execute tests or infer their meaning from bytes: collecting real test/browser/log evidence and reviewing its meaning is the host's responsibility. Record true model/provider identity in private host logs; session IDs in a packet are assertions, not independent authentication. No live-model call is implemented or fabricated by this CLI.

An unchanged source is idempotent. To review a new target after completed GO, enqueue the source scoped with the new target SHA. Within a conditional run use `revise`; the total round budget remains bounded and previous evidence is invalidated. Reusing a source with another target or policy is rejected, never silently accepted.

## Host integration

A host reads the root skill through a pinned Git submodule. Its `AGENTS.md` and `HEARTBEAT.md` invoke discovery on entry and each real host wake-up. The host reads actual tickets and drives authorized research/review/fix actions. A Markdown file cannot install a background daemon.

The `project` command writes only generated `tribunal-<id>` files, refusing to overwrite human files or traverse outside the root. Queue views follow the existing Hans directories; OpenSpec gets a generated `tribunal-tasks.md` supplement rather than overwriting manual specs. Receipts record review packets, conditions, hashes and target revisions. Views can be stale and must be refreshed from the ledger before action; partial local projection failure is recoverable by regeneration and never changes canonical state.

Private raw evidence, health data, mail contents and notebook identifiers must never enter the public skill or public CI. Do not recursively clone Hans from this repository. Public tests use synthetic fixtures and local temporary bare repositories only.

## Limits and rollout gates

The new Git backend is an opt-in standalone profile. Where a production `af.control` claim/approval authority already owns an action, integrate through that authority rather than claiming the same action twice. Orca remains execution/worktrees, the existing UI remains presentation, and Matrix/browser shells remain projections. This package does not deploy those integrations.

Before live rollout: independent code review; approved private ledger remote; Git push rights and ref protections; synchronized clocks; actual isolated reviewer capability; host heartbeat invocation; retention/redaction policy; and end-to-end verification in that host. Tests here prove the declared offline/fixture scope only. Legacy reports do not turn these live gates green.
