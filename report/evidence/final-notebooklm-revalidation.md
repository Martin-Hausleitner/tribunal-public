# Final NotebookLM live revalidation

IDR: ja

- Recorded UTC: `2026-07-20T19:47:05Z`
- Canonical notebook: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515
- Notebook ID: `80cffd38-0185-4f4d-ae00-bbc67c4bc515`
- Title: `Tribunal IDR 2026-07-04`
- Authenticated CLI: `nlm 0.8.9`
- Public-link access: enabled; the returned public link exactly matched the canonical URL
- Conversation ID: `1ebabb83-484f-405b-8b24-a26cfa5b9afb`

The live authentication check succeeded and the notebook was resolved by exact ID, not inferred from a pasted URL. The authentication probe exposed account information in the private terminal; this public ledger deliberately omits it.

## Corpus inventory

After adding the four current revalidation OpenSpec artifacts and waiting for each to process, the first `nlm source list ... --json` inventory returned:

- total sources: `523`;
- processed (`status == 2`): `512`;
- failed (`status == 3`): `11`;
- newly added OpenSpec sources processed: `4/4`.

The four added sources are the current proposal, design, capability spec, and task list. Existing targeted primary sources for promptfoo, DeepEval, Microsoft Agent Framework, AutoGen, Ragas, OpenAI Evals, Langfuse, DSPy, Phoenix, and lm-evaluation-harness were all present and processed. Ten earlier Tribunal project artifacts were also processed. The eleven failures were duplicate or secondary web pages rather than any current project/OpenSpec or canonical matrix repository source. A later source-freshness control superseded this inventory; its final `535/524/11` state and fresh query set are recorded below.

Two initial knowledge-query invocations exited without a retained visible payload because of output filtering; they are not counted as evidence. The subsequent unfiltered invocation produced the retained Query 1 response below.

## Cross-query 1: knowledge and correctness

**Question:** Revalidate the current release from processed project artifacts and authoritative primary sources; distinguish executable structure from semantic correctness, visual quality, provider-family independence, and production observability; test the current corpus counts and new OpenSpec sources.

**Returned grounding:** `15` source IDs and `46` citation mappings.

**Supported result:** The standard-library core provides deterministic structural checks, bounded input validation, validated persona loading, explicit evidence gaps, post-hoc synthesis, stable JSON/Markdown serialization, and PEP 517 packaging. Its `40/100` or `50/100` local score is structural readiness, not semantic target quality. A NotebookLM URL is recorded provenance, not runtime retrieval proof. No GUI, provider-family enforcement, or durable production observability is bundled.

**Manual exclusions:** The answer reused stale historical judge scores despite the prompt; used `servas-ai/tribunal` instead of the actual repository; called separate backend calls concurrent; and imported a literature-specific error-correlation range as if locally measured. It also suggested unrelated mandatory controls. None of those claims is adopted.

## Cross-query 2: hostile risks and mitigations

**Question:** Rank reproducible current defects separately from future live-backend risks and test packaging, persona identity, skill routing, provenance, prompt injection, quota semantics, and publication gates without importing prior scores or study metrics.

**Returned grounding:** `24` source IDs and `34` citation mappings.

**Supported result:** A future live backend must independently address provider/model provenance, common-mode judge errors, prompt/style sensitivity, actual tool dispatch, hostile retrieval content, durable budget enforcement, state recovery, and trace persistence. Blind initial views and deterministic gates reduce specific failure modes without proving semantic truth.

**Manual exclusions:** The answer mislabeled intentionally stateless per-run capacity as a present defect, imported ML-DSA and cryptographic requirements from an unrelated source, mentioned Pydantic despite a standard-library-only runtime, and repeated a historical Markdown-escaping defect that is fixed and tested. Those are not current defects.

## Cross-query 3: CLI and UX feasibility

**Question:** Audit the observable CLI, Python API, reusable skill, persona library, packaging, and evidence workflow while separating terminal behavior from claims requiring a GUI, browser, viewport, accessibility audit, or human study.

**Returned grounding:** `12` source IDs and `39` citation mappings.

**Supported result:** The CLI has shared mode identifiers with the API, documented hardness expansion, concise invalid-input behavior, safe-normalized Markdown and lossless JSON, a clean-install entry point, validated personas, and an explicit Karpathy-inspired disclaimer. Nine personas repeat after three rounds; declared skills are orchestration labels, not executed-tool proof. CLI execution cannot prove visual UI/UX or human task success.

**Manual exclusions:** The answer used stale `servas-ai` and `~/.claude` paths, promised parallel execution where only separate calls are guaranteed, described a panel below three even though it is rejected, and promoted cross-family routing, formatting stripping, and resume hashing to current core requirements. Those are external/future integration controls, not release defects.

## Cross-query 4: contradiction and source attribution

**Question:** Audit the three preceding answers against the live corpus and current project artifacts for the exact named discrepancies: source counts, repository identity, stale scores, imported correlation, capacity semantics, cryptography/Pydantic, Markdown escaping, concurrency, panel size, skill path, and future controls.

**Returned grounding:** `19` source IDs and `46` citation mappings.

**Supported result:** The control confirmed the real repository, historical nature of earlier scores, lack of a local correlation measurement, stateless capacity boundary, absence of ML-DSA/Pydantic, current Markdown escaping, separate sequential calls, rejection of fewer than three personas, tracked `skill/SKILL.md`, and future/integration status of the proposed production controls.

**Residual correction:** The control correctly repeated `523/512/11` at first, then contradicted itself by claiming `512` total sources. Direct CLI inventory taken after all additions is authoritative: `523` total, `512` processed, `11` failed. The control also cannot verify the returned grounding counts of earlier calls from source prose; those counts were read directly from each JSON response.

## IDR conclusion

The research supports shipping Codex Tribunal for the bounded offline orchestration and reusable-skill contract. It does not justify representing the bundled backend as a semantic verifier, visual UI/UX tester, cross-family consensus engine, live NotebookLM client, durable quota authority, or production observability platform. Generated answers repeatedly crossed those boundaries even under explicit prompts; primary artifacts, direct CLI inventory, executable tests, and the contradiction audit therefore outrank fluent synthesis.

Unresolved evidence remains explicit: the mandated Grok availability must be retested; any live backend needs real provider/model/tool/cost/trace provenance; GUI claims require a real visual surface; and the mixed corpus contains duplication and unrelated research that demands source-level controls.

## Closure source-freshness control

Recorded UTC: `2026-07-20T19:57:53Z`

The first retained answers still cited project sources whose titles looked current but whose content predated later README/report corrections. Those answers were therefore useful as a stale-source detector, not as closure evidence. Twelve uniquely titled snapshots from repository HEAD `0e728e6` were added: README, skill, report baseline, the four revalidation OpenSpec artifacts, final baseline, conclusion-free judge packet, runtime, packaging metadata, and tests. NotebookLM accepted Markdown directly; the `.py` and `.toml` files were copied to temporary `.txt` files for upload, processed, and the temporary directory was removed.

The authoritative final CLI inventory is:

- total sources: `535`;
- processed (`status == 2`): `524`;
- failed (`status == 3`): `11`;
- fresh HEAD snapshots processed: `12/12`.

The query selection pinned those twelve fresh snapshots, the ten canonical OSS repository roots, the multi-agent debate paper, an OpenReview judge-bias study, Nielsen Norman Group usability heuristics, and W3C WCAG 2.2. The role calls were repeated in separate CLI processes, followed by a contradiction/source-attribution control.

| Fresh query | Returned source IDs | Citation mappings | Retained boundary | Manual exclusions |
|---|---:|---:|---|---|
| Knowledge/correctness | 12 | 44 | Dependency-free structural contract, bounded CLI, separate requests, explicit gaps, structural score ceiling | Non-local correlation values, old external-attempt facts, and non-goals portrayed as current defects |
| Hostile critique/risk | 13 | 39 | Live deployments need real provider/model/tool provenance, trusted budgets, retrieval safety, and trace persistence | Target text is escaped by `_markdown_text(self.target)`; documented persona repetition is a limitation, not a defect; current docs already reject family-independence claims |
| CLI and UI/UX feasibility | 18 | 58 | Installable CLI/API, concise errors, safe Markdown/lossless JSON, disclosed personas, and OSS composition boundaries | Stale corpus counts and historical judge scores; no browser/TUI claim is supported |
| Contradiction/source control | 7 | 20 | Confirmed disclosed rotation, no sibling-output reuse, no statistical-independence claim, and explicit non-capabilities | It incorrectly preferred stale ledger counts over returned JSON and repeated the false target-escaping claim |

Direct CLI JSON and current source code outrank generated prose. The final grounding counts are `12/44`, `13/39`, `18/58`, and `7/20`; the final notebook state is `535/524/11`. The closure conclusion remains bounded: ship the thin offline library/skill contract, compose mature OSS for CI/runtime/observability, and require separate executable proof for semantic, visual, provider-diversity, tool-use, budget, or durability claims.
