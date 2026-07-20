## ADDED Requirements

### Requirement: Fresh OpenSpec-bound baseline
The delivery SHALL create and strictly validate a distinct OpenSpec change before new live research or judge synthesis, and SHALL retain the starting repository, tool, and weekly-guard state.

#### Scenario: Revalidation begins from a completed repository
- **WHEN** a new run starts after an earlier brief completion
- **THEN** proposal, design, capability spec, tasks, and baseline distinguish this run from historical evidence

### Requirement: Authenticated canonical NotebookLM IDR
The delivery MUST use the authenticated `nlm` CLI with the canonical notebook, verify identity and source processing state, run knowledge/correctness, criticism/risk, and UI/UX cross-source queries plus a contradiction/source-attribution control, and publish `IDR: ja` with the canonical link and truthful limitations.

#### Scenario: Canonical IDR succeeds
- **WHEN** the notebook and selected sources are available
- **THEN** the retained ledger identifies the notebook, current source counts, query prompts, grounding metadata, decision-relevant answers, contradictions, and manual corrections without credentials

#### Scenario: IDR operation fails
- **WHEN** authentication, inventory, processing, or a required query fails
- **THEN** the failure is retained and that operation is not represented as successful

### Requirement: Primary OSS-first comparison
The delivery SHALL compare viable existing OSS before custom work, SHALL refresh canonical GitHub URLs and numeric stars, and MUST apply the published 100-point rubric with differentiated totals and exactly one evidence-eligible crowned winner.

#### Scenario: Mutable metadata is refreshed
- **WHEN** the candidate batch is queried
- **THEN** timestamped primary metadata, license/activity qualifications, component scores, totals, and crown state agree across structured evidence, CSV, and report while stars contribute zero points

### Requirement: Three isolated adversarial perspectives
The delivery MUST independently obtain or truthfully attempt knowledge/correctness, harsh criticism/risk, and UI/UX feasibility judgments, attempting `grok --single -m grok-4.5 --effort high` first for every role and using only the brief-authorized `agy` fallback when Grok returns no complete answer.

#### Scenario: A role returns a complete verdict
- **WHEN** an allowed provider completes the role contract
- **THEN** the retained verdict identifies role, engine provenance, score, recommendation, evidence, gaps, and independence limits

#### Scenario: Grok fails before a verdict
- **WHEN** the mandated Grok call exits without a complete answer
- **THEN** its failure is retained, excluded from verdict synthesis, and the authorized fallback may be attempted

### Requirement: Evidence-bound public synthesis
The delivery SHALL keep `report/codex-trib-lib-tribunal.md` aligned with current evidence and include `IDR: ja`, the canonical NotebookLM link, three role verdicts, agreements and disagreements, a 100-point feature matrix, exactly one crown, final recommendation, limitations, Mermaid flow, actionable implementation plan, and an index to this pass's evidence.

#### Scenario: Current evidence is synthesized
- **WHEN** NotebookLM, GitHub, judge, and executable observations are frozen
- **THEN** each claim is traceable to its correct evidence class and no semantic, provider-independence, visual-UX, or persona-authorship claim is overstated

### Requirement: Real source and installed-package E2E
The delivery MUST run a realistic comparison through the source CLI, all three primary modes, an expected invalid-NotebookLM-input path, a clean PEP 517 build and isolated install, the installed console entry point outside the source tree, and the installed Python API without mocked backend or model results.

#### Scenario: Bounded recommendation works through public surfaces
- **WHEN** the actual source and installed package are invoked
- **THEN** output is structurally valid, backend provenance and evidence gaps remain visible, serialization preserves the synthetic persona disclaimer, and structural readiness is not mislabeled as semantic proof

#### Scenario: Invalid NotebookLM input is rejected
- **WHEN** a malformed or placeholder NotebookLM URL is supplied
- **THEN** the CLI exits with status 2, concise stderr, and no traceback

### Requirement: Fail-closed publication and immutable handoff
The delivery MUST pass unit, compile, build, skill, CSV, report, strict OpenSpec, evidence, diff, and secret checks; stage intended artifacts with force-add where required; commit and push the current branch; compare the remote and local full SHAs; and retrieve the SHA-pinned public report blob.

#### Scenario: All release gates pass
- **WHEN** every deterministic and manual observation agrees with the report
- **THEN** the pushed commit and retrievable immutable blob are reported as the completed handoff

#### Scenario: A release gate fails
- **WHEN** a required check exits nonzero or evidence contradicts a public claim
- **THEN** publication is blocked until the scoped defect is fixed or truthfully reported as unresolved
