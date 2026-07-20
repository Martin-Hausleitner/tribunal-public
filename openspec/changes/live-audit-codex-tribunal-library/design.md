## Context

The repository already contains a completed implementation change, but the new brief demands live external evidence and observable execution rather than reuse of an old green state. The audit crosses local Python/skill artifacts, NotebookLM, independent model processes, GitHub metadata, Markdown report gates, Git publication, and a real CLI surface. External services can fail or rate-limit, so raw outputs and honest provenance are part of the design rather than incidental logs.

## Goals / Non-Goals

**Goals:**

- Produce a current, repeatable evidence chain from authoritative sources through three independent judgments to one scored recommendation.
- Validate the actual library and skill behavior through their public interface with a realistic tribunal input.
- Keep raw evidence separate from synthesis so report claims can be traced and independently challenged.
- Publish a report whose links, scoring arithmetic, crown count, Markdown structure, and E2E claims are mechanically checkable.

**Non-Goals:**

- Reimplement mature orchestration frameworks when an existing OSS component can be adapted.
- Claim that a persona is the real Andrej Karpathy or that an unavailable external engine ran successfully.
- Add speculative runtime abstractions unrelated to a failure discovered by the live audit.
- Treat local fixtures, mocked model output, or source-code inspection alone as an E2E pass.

## Decisions

1. **Use one canonical NotebookLM notebook as the IDR source of truth.** Reuse it only if its identity and URL can be verified; otherwise create a purpose-specific notebook. Ingest primary documentation and repository sources before secondary commentary, then run multiple cross-queries whose outputs are preserved. This avoids fragmented citations. A generic web-search-only dossier was rejected because the brief explicitly requires NotebookLM.

2. **Use isolated external processes for the three judges.** Invoke `grok --single -m grok-4.5 --effort high` separately for correctness, risk criticism, and UX feasibility. If that engine is genuinely unavailable, use the brief-approved isolated `agy` perspectives and label the fallback in every affected artifact. Reusing one synthesis call or fabricating outputs is prohibited because it defeats independence.

3. **Snapshot OSS evidence before scoring.** Capture canonical repository URLs, current star counts, licenses, release/activity signals, and feature evidence from GitHub or project documentation. Apply one predeclared 100-point rubric to all candidates and award exactly one crown. This is preferred to prose-only recommendation because the Operator mandate requires comparable OSS-first selection.

4. **Keep evidence in reviewable files under `report/evidence/`.** Preserve normalized NotebookLM answers, judge outputs, GitHub metadata, and E2E logs with timestamps and command provenance while excluding credentials and personal data. The final report links or quotes the decision-relevant parts. Ephemeral terminal-only claims were rejected because they cannot survive publication review.

5. **Test through the public CLI and validate output semantics.** Feed a realistic high-stakes technical prompt through the recommended Tribunal entry point, then assert three independent judge records, correct tribunal type, synthesis, engine provenance, evidence gaps, and hardness/Nx behavior. Directly importing private helpers is insufficient for the required E2E proof.

6. **Gate the report and publication mechanically.** Run the existing test/build/report validators, add only the smallest missing validation needed, inspect the generated Markdown, commit the exact evidence, push the configured branch, and retrieve the public blob URL. A local commit without a verified remote object does not satisfy delivery.

## Risks / Trade-offs

- **External service or quota failure** → Record the exact failure, retry only with a materially different supported path, and use only the brief-approved fallback with explicit provenance.
- **NotebookLM source answers overstate weak sources** → Prefer primary sources, ask contradiction/source-attribution queries, and distinguish sourced findings from tribunal inference.
- **GitHub stars change after capture** → Record an ISO date/time and call values snapshots rather than timeless facts.
- **Judge outputs are correlated despite separate calls** → Use role-specific rubrics, independent processes, no shared draft verdict, and synthesize only after all outputs are frozen.
- **A prior artifact appears complete but is stale** → Re-run live checks and replace claims only when backed by evidence from this audit.
- **Publication leaks secrets or user data** → Inspect staged diff and evidence files before commit; store no tokens, cookies, account identifiers, or private NotebookLM content.

## Migration Plan

1. Create the new live-audit evidence set without changing existing runtime behavior.
2. Run live IDR, OSS verification, and independent judgments; preserve raw outputs.
3. Run the public-interface E2E case and make surgical runtime/skill fixes only if needed.
4. Regenerate the final report and validation proof, then commit and push all required artifacts together.
5. Roll back by reverting this audit commit; the prior completed change and library remain intact.

## Open Questions

- Whether Grok 4.5 is reachable in the current authenticated environment; this is resolved by a real probe, not assumption.
- Whether the canonical NotebookLM notebook from the earlier run remains accessible and source-complete; this is resolved during notebook inventory.
- Whether the configured remote permits push and exposes a public blob; this is resolved before publication without altering unrelated remote configuration.
