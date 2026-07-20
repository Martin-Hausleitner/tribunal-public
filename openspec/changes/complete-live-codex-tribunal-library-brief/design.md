## Context

Codex Tribunal already provides a dependency-free Python orchestrator, an installable CLI/API, a reusable skill, nine persona definitions including a disclosed Karpathy-inspired critic, deterministic gates, a public report, and several historical live-audit ledgers. This change is a new acceptance pass for the supplied brief. The central claims rely on external state that can change within hours: NotebookLM authentication and source processing, provider quota, GitHub metadata, package-build behavior, the Git remote, and public blob availability.

Evidence must therefore remain separated by class. NotebookLM answers support research synthesis, external judges provide adversarial opinions, GitHub supplies primary OSS metadata, and executable observations prove local behavior. No class is allowed to stand in for another, and failed external calls remain evidence of availability rather than inferred verdicts.

## Goals / Non-Goals

**Goals:**

- Reproduce the brief from an OpenSpec contract created before new live calls.
- Produce a dated, rerunnable authenticated NotebookLM ledger with role queries and a contradiction control.
- Obtain three isolated role judgments through the mandated Grok command or the explicitly authorized `agy` alternative, with exact provenance and truthful exclusions.
- Bind the narrative report to primary GitHub metadata, a machine-checkable 100-point matrix, exactly one eligible winner, executable E2E evidence, and a clear implementation plan.
- Demonstrate source-tree and clean-install behavior through the actual CLI and Python API without mocked results.
- Publish one commit and prove the SHA-pinned report blob is publicly retrievable.

**Non-Goals:**

- Claim that the bundled deterministic backend semantically fact-checks targets, queries NotebookLM, enforces model-family independence, or performs visual UI inspection.
- Add a production provider integration, browser UI, durable quota store, or observability platform solely to improve this acceptance pass.
- Turn provider failures or incomplete generations into synthetic judge verdicts.
- Attribute the synthetic Karpathy-inspired persona's output to Andrej Karpathy.

## Decisions

1. **Create a distinct OpenSpec change for this pass.** Completed historical changes remain immutable input. Reopening an old checklist was rejected because stale evidence could appear current.
2. **Reuse the canonical notebook and candidate set, but re-observe them live.** This preserves comparability while satisfying the brief's live-IDR requirement. Creating a second notebook was rejected because it would fragment the evidence corpus and canonical link.
3. **Capture raw command output before synthesis.** Each external interaction receives its own dated evidence section or artifact. Relying on prose-only summaries was rejected because availability failures and grounding details would be unverifiable.
4. **Freeze a common conclusion-free judge packet.** The three roles receive the same observed repository facts, limitations, and required output schema but no sibling verdict or proposed winner. Letting later judges see earlier views was rejected because it weakens independence.
5. **Attempt Grok first for every role and use only the authorized alternative when needed.** Exit status and sanitized error text are retained. Provider failure is reported, never repaired with invented content.
6. **Keep JSON/CSV authoritative for mutable OSS facts and scoring.** Stars are dated adoption context and add zero rubric points. A gate joins report URLs, totals, and crown state to the structured data.
7. **Use real consumer surfaces for E2E.** Run the repository CLI, all primary modes, expected invalid input, then build/install an exact wheel into a temporary environment and invoke the installed console script and API outside the repository.
8. **Publish fail-closed.** Tests, compile, build, skill, CSV, report, OpenSpec, clean diff, remote SHA equality, and immutable HTTP retrieval all gate completion.

## Risks / Trade-offs

- **Notebook or provider quota blocks a fresh result** → preserve exact failure provenance, use only the permitted fallback, and mark any unfilled role as a limitation rather than fabricating completion.
- **NotebookLM repeats stale or incorrect source claims** → run a contradiction/source-attribution query and privilege primary GitHub/API observations plus executable repository evidence.
- **GitHub stars drift during the run** → capture candidates in one dated batch and update matrix/report together; stars remain unscored.
- **A deterministic local run looks like semantic proof** → keep the backend name, evidence gaps, and non-positive marker visible in every E2E observation.
- **Live evidence contains secrets or PII** → retain only sanitized command/output facts and never commit tokens, cookies, or local credentials.
- **Push succeeds without the requested artifact** → compare local and remote full SHAs and fetch the exact SHA-pinned blob before declaring completion.

## Migration Plan

1. Record the current branch, commit, tools, artifact inventory, and strict planning validation.
2. Capture authenticated NotebookLM, primary GitHub, isolated judge, and executable E2E evidence.
3. Reconcile contradictions and update the structured matrix and public report only when observations require it.
4. Run every deterministic gate and inspect the intended diff for unrelated or sensitive content.
5. Mark tasks complete from captured evidence, commit, push, compare SHAs, and retrieve the immutable blob.

Rollback is a normal revert of this pass's publication commit. Temporary judge sessions, query processes, build directories, and virtual environments are not committed.

## Open Questions

- Whether Grok 4.5 and the permitted fallback have usable quota is deliberately resolved by the required live attempts.
- Whether GitHub stars, archive state, activity, or license metadata changed is resolved only by the fresh primary snapshot.
- Whether existing runtime code needs modification remains contingent on a reproducible current E2E defect.
