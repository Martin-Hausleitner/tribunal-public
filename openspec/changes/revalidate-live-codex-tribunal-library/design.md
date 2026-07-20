## Context

Codex Tribunal already has a dependency-free Python core, reusable skill, persona library, deterministic gates, prior NotebookLM/GitHub research ledgers, three accepted external verdicts, and a public report. The current task is a live release revalidation, not a redesign: mutable metadata, authenticated research state, provider quotas, package installation, and the public Git object must be observed again. Existing uncommitted report and E2E evidence must be preserved while new artifacts remain attributable to this pass.

The chief constraint is evidence separation. NotebookLM synthesis can inform design-space claims, external judges can critique a frozen repository snapshot, and executable tests can prove package behavior; none of those evidence classes can replace another. Provider or quota failures are valid operational findings but never synthetic verdicts.

## Goals / Non-Goals

**Goals:**

- Produce a dated, rerunnable live-IDR ledger from the canonical authenticated notebook and source-backed cross-queries.
- Obtain three isolated role verdicts through the mandated Grok path or the explicitly approved `agy` fallback, preserving complete provenance and exclusions.
- Bind the human report to machine-checkable GitHub metadata, matrix scoring, winner rules, E2E evidence, and strict gates.
- Reproduce the public package contract from both the repository and a clean installation outside the working tree.
- Publish one commit whose pushed tree contains all required artifacts and whose SHA-pinned blob is retrievable.

**Non-Goals:**

- Claim that the bundled `local-rules` backend performs semantic fact-checking, NotebookLM retrieval, visual UI inspection, or model-family enforcement.
- Add a production LLM provider, browser UI, durable trace store, or cross-run quota authority during an evidence-only revalidation.
- Convert failed or incomplete external model runs into inferred verdicts.
- Change the runtime solely to improve a report score unless a reproducible contract defect is observed.

## Decisions

1. **Use a new OpenSpec change for this pass.** Earlier changes remain immutable historical context; a new checklist makes fresh observations distinguishable. Reusing a completed task list was rejected because it could make stale evidence appear current.
2. **Freeze a conclusion-free judge packet before external calls.** Every role receives the same repository facts, behavioral proofs, known boundaries, and scoring format without sibling verdicts or a proposed winner. Letting judges read a draft synthesis was rejected because it would defeat independent initial judgment.
3. **Attempt Grok exactly as mandated, then fail over only as authorized.** Each role starts in a fresh `grok --single -m grok-4.5 --effort high` process. If it fails before answer generation, the failure is logged and a fresh isolated `agy` session can supply that role. Fabricated completion or reuse of partial prose is prohibited.
4. **Treat the CSV and JSON snapshot as authoritative structured evidence.** Report tables duplicate those facts for readers, while gates enforce URL, star, score, crown, and snapshot agreement. Stars provide dated adoption context but contribute no score.
5. **Keep evidence classes explicit.** NotebookLM supports research synthesis, judges supply adversarial opinions, and CLI/API/install observations establish executable behavior. The final verdict is bounded to the intersection of those proofs.
6. **Prefer real consumer surfaces for E2E.** The CLI is run from the repository, then the wheel is built/installed into a new temporary virtual environment and invoked from outside the repository; the installed Python API is also called. Unit-only proof was rejected because packaging and entry-point failures would remain invisible.
7. **Publish fail-closed.** Required gates, a clean intended diff, commit containment, push containment, and HTTP retrieval of the exact SHA-pinned report blob must all pass. A mutable branch URL alone is insufficient.

## Risks / Trade-offs

- **Provider quotas can block fresh verdicts** → retain exit status and sanitized error output, try only the approved fallback, and distinguish previously accepted verdicts from fresh supplemental views.
- **NotebookLM can mischaracterize its own sources** → record citation/grounding metadata and run a contradiction/source-attribution control; manually prefer primary artifacts and executable behavior.
- **Mutable GitHub stars can create report drift** → capture all repositories in one timestamped snapshot and regenerate/verify the matrix and narrative against it.
- **A deterministic local backend can look greener than it is** → preserve explicit evidence gaps and prevent a crown or positive marker when semantic proof is absent.
- **Existing worktree edits may belong to another process** → inspect and preserve them, make additive changes, and stage only the intended final artifact set.
- **A public push can succeed while the desired file is absent** → compare local/remote commit IDs and fetch the immutable blob URL after push.

## Migration Plan

1. Add the revalidation planning artifacts without changing public runtime behavior.
2. Capture live NotebookLM, GitHub, judge, and E2E evidence in separate dated ledgers.
3. Update the report and any structured snapshot only after contradictions are resolved.
4. Run strict gates and package/manual QA; fix only reproducible scoped defects.
5. Mark tasks complete, commit the exact intended artifacts, push, and verify the SHA-pinned blob.

Rollback consists of reverting the single revalidation commit; earlier completed release artifacts remain intact. Temporary virtual environments and provider sessions are not part of the repository.

## Open Questions

- Whether Grok has regained paid quota is intentionally resolved only by the three mandated live attempts.
- Whether fallback model quotas permit all three fresh verdicts is likewise an observed condition, not an assumption.
- Any changed GitHub metadata or license signal is accepted only after the live snapshot and primary repository metadata agree.
