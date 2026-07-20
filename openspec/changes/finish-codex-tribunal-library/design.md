## Context

The current repository is a zero-dependency Python draft with a CLI, JSON personas, a skill, and simple gates. Its public surface is useful, but several behaviors are only asserted: built-in quota values look like live provider state, every judge receives nearly identical findings, arbitrary strings are accepted as NotebookLM evidence, and no tests or source ledger prove the release claims. The required live IDR and Grok deliberation are publication inputs, while the reusable library must remain deterministic and honest when run without network credentials.

The stakeholders are OSS users running the Python API or CLI, Codex users installing the skill, and reviewers auditing the published report. The hard constraints are a dependency-free runtime, three primary tribunal types, a Karpathy-inspired persona, no mock research, one real NotebookLM notebook, three independent external verdicts, and a public GitHub blob URL.

## Goals / Non-Goals

**Goals:**

- Make the local verdict engine explicit about what it did and did not verify.
- Guarantee three distinct persona assignments per round, bounded hardness/Nx behavior, stable serialized results, and strict boundary errors.
- Permit real judge integrations through a small backend contract without making a network provider a runtime dependency.
- Make personas and the skill reusable, validated, and accurately documented.
- Preserve reproducible research provenance: notebook identity, source inventory, query answers, Grok verdicts, star snapshot, scoring rubric, and report gates.
- Publish a report that can be audited independently of this work session.

**Non-Goals:**

- Implement a hosted orchestration service, browser UI, provider authentication, or a universal agent framework.
- Claim that the dependency-free backend performs semantic LLM judgment or validates the contents of a NotebookLM URL.
- Impersonate Andrej Karpathy or attribute generated conclusions to him; the persona is explicitly described as inspired by public technical principles.
- Keep speculative provider quota defaults or promise live quota discovery.
- Crown the Tribunal library itself unless the scored evidence actually makes it the strongest option for the stated use case.

## Decisions

### 1. Keep a standard-library core and add an explicit judge-backend boundary

`TribunalOrchestrator` will retain its small Python/CLI surface. It will invoke a `JudgeBackend` contract once for each independently selected persona. The built-in backend will be named and documented as a deterministic rule/evidence evaluator; result provenance will never imply a live LLM. A caller can inject a real backend without coupling the library to an SDK.

Alternative considered: embed Grok or another provider directly. Rejected because it would add credentials, network behavior, provider churn, and a hard dependency to a library whose offline gate is valuable.

### 2. Treat independence as an enforceable orchestration property

Each round will select three unique persona slugs, construct one immutable request per judge, and collect views before synthesis. Requested persona names are validated instead of silently ignored. Judge output records the persona slug, backend, engine provenance, evidence, and gaps. Post-hoc clash synthesis happens only after all per-round calls return; the contract does not imply interactive inter-agent debate or cross-family independence.

Alternative considered: keep three labels over one shared template. Rejected because it presents duplicated boilerplate as independent judgment.

### 3. Replace fictional quota defaults with honest local provenance

The default engine is `local-rules` with source `builtin-local`; it carries no claim about third-party quota. External engine allocation is accepted only from explicit JSON or file configuration and validated as non-negative integer capacity. Allocation is deterministic per run and fails clearly if one run needs more capacity than configured. Planning is stateless across `judge()` calls because the library is not a durable quota or billing authority.

Alternative considered: retain planning values for named providers. Rejected because snapshot-free numbers can be mistaken for real free quota.

### 4. Validate evidence references at the boundary

A supplied NotebookLM link must use HTTPS, the `notebooklm.google.com` host, and a `/notebook/<id>` path. Invalid persona documents, unknown requested personas, invalid score/output shapes, and malformed quota data fail with actionable errors. A syntactically valid link is recorded only as a reference, not proof that its contents were queried.

Alternative considered: accept arbitrary strings and expose gaps later. Rejected because downstream reports would serialize misleading provenance.

### 5. Separate live publication evidence from deterministic runtime behavior

NotebookLM research and Grok judge attempts will be performed live during release preparation and saved as evidence files. If Grok is unavailable, the brief-allowed isolated `agy` fallback will provide the three verdicts while the failures stay visible. The final report will synthesize those artifacts and a GitHub API star snapshot. Runtime examples will use the real notebook link only after it is created and verified.

Alternative considered: make the report a generated local-rule verdict. Rejected because the brief explicitly requires real NotebookLM and independent Grok work.

### 6. Score alternatives with a declared use-case rubric

The comparison will score alternatives on tribunal-type fit, judge independence/adversarial depth, evidence/research provenance, persona/skill extensibility, observability/repeatability, and OSS integration cost. Weights sum to 100. GitHub stars are a dated adoption signal, not a quality score. Exactly one crown is awarded to the best fit for reusable hard-critical Tribunal workflows, with trade-offs stated.

Alternative considered: rank primarily by stars. Rejected because mature observability and agent-framework projects solve different jobs and adoption would swamp task fit.

## Risks / Trade-offs

- [The built-in evaluator cannot assess arbitrary target truth] → Name it `local-rules`, keep semantic claims as gaps, and demonstrate real external verdicts separately.
- [Live NotebookLM/Grok outputs may change or become unavailable] → Preserve timestamped source/query/verdict evidence and make the report self-contained enough to audit.
- [GitHub star counts drift] → Record UTC snapshot time and numeric counts; never present them as timeless values.
- [Persona naming could imply endorsement] → Use “Karpathy-inspired” in documentation and state that it is not authored or endorsed by Andrej Karpathy.
- [A broad competitor matrix can compare unlike tools] → Declare the target use case, score dimensions, and category mismatch in every recommendation.
- [Public push can expose transient files or credentials] → Review tracked files, ignore caches/evidence secrets, and scan the final diff before publication.

## Migration Plan

1. Add the backend/result validation contracts while preserving the existing main imports and CLI flags where accurate.
2. Replace provider planning defaults with `local-rules`; users relying on per-run capacity planning can pass the existing environment/file configuration explicitly and enforce durable budgets in a trusted live-backend boundary.
3. Update personas, skill, examples, and README to the honest contracts.
4. Add unit/CLI/report gates and run them before report publication.
5. Create and verify the live research artifacts, then update the final link and snapshots.
6. Commit all source and evidence artifacts, create/configure the public remote, push, and verify the exact blob response.

Rollback is a normal Git revert of the publication commit. The canonical NotebookLM notebook is retained as an external research artifact; no destructive cleanup is part of rollback.

## Open Questions

None blocking. The winner and final numeric scores remain intentionally undecided until the live IDR, GitHub snapshot, and three Grok verdicts are complete.
