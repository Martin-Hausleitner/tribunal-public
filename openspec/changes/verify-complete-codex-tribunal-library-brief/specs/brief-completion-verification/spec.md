## ADDED Requirements

### Requirement: OpenSpec-first verification baseline
The delivery SHALL complete and strictly validate a distinct OpenSpec change before synthesizing new external evidence, and SHALL retain the starting repository, tool, authentication, and resource-guard state.

#### Scenario: Verification begins from a completed repository
- **WHEN** mutable live evidence must be revalidated for the current brief
- **THEN** a proposal, design, capability spec, and checkable task list define the exact observations required for completion

### Requirement: Authenticated canonical NotebookLM IDR
The delivery MUST use the authenticated `nlm` CLI against the canonical notebook, add at least one uniquely identifiable current-pass source, verify source processing, run three role-aligned selected-source queries plus a contradiction/source-attribution control, and publish `IDR: ja` with the canonical link and truthful limitations.

#### Scenario: Canonical live research succeeds
- **WHEN** the notebook, current source, and selected primary corpus are available
- **THEN** the ledger records notebook identity, public link state, source counts, added-source state, exact questions, returned grounding metadata, answers, contradictions, and manual corrections without credentials

#### Scenario: NotebookLM operation fails
- **WHEN** authentication, source ingestion, processing, or a query fails
- **THEN** the failure is retained and the report does not claim that operation succeeded

### Requirement: OSS-first primary comparison
The delivery SHALL recheck viable existing OSS through canonical GitHub metadata before retaining or changing the custom library recommendation, and MUST publish numeric stars, license/activity qualifications, a documented 100-point rubric, differentiated totals, and exactly one evidence-eligible crown.

#### Scenario: Mutable OSS metadata is refreshed
- **WHEN** candidate repositories are queried for this pass
- **THEN** the timestamped snapshot, CSV, and report agree on canonical URLs, stars, relevant repository facts, score components, totals, and crown state while stars contribute zero score points

### Requirement: Three isolated adversarial judgments
The delivery MUST run separate fresh `agy` sessions for knowledge/correctness, harsh criticism/risks, and CLI UX/implementability, with no sibling verdict or draft synthesis in any judge prompt.

#### Scenario: A role response is accepted
- **WHEN** an isolated judge returns a complete response grounded in the frozen packet and permitted repository scope
- **THEN** its retained verdict identifies role, provider/model provenance, inspected evidence, score, recommendation, findings, gaps, independence limitations, and any required conditions

#### Scenario: A role response is unusable
- **WHEN** a judge fails, is incomplete, exceeds scope, or asserts unsupported evidence
- **THEN** the attempt is retained but excluded from synthesis and any retry uses a fresh session with a materially corrected prompt

### Requirement: Evidence-bound public report
The delivery SHALL update `report/codex-trib-lib-tribunal.md` with `IDR: ja`, the canonical link, three accepted role verdicts, post-hoc agreements and disagreements, the 100-point feature matrix, exactly one crown, a recommendation, Mermaid evidence flow, explicit limitations, an actionable implementation plan, and links to this pass's ledgers.

#### Scenario: Report synthesis completes
- **WHEN** IDR, OSS snapshot, judge verdicts, and E2E observations are frozen
- **THEN** every material claim maps to the correct evidence class and the report does not overstate semantic correctness, visual UX proof, durable quotas, or provider independence

### Requirement: Real end-to-end recommendation proof
The delivery MUST execute the actual source CLI, all three primary modes, comparison mode, expected invalid-input behavior, a PEP 517 build, an isolated installation of the exact built wheel, the installed console entry point outside the source tree, and the installed Python API without mocked model or backend results.

#### Scenario: Source and installed surfaces work
- **WHEN** a realistic Tribunal comparison and package-use case run
- **THEN** outputs have valid schemas, separate judge calls, explicit local-backend provenance and evidence gaps, bounded structural scores, safe Markdown, lossless JSON, and the synthetic-persona disclosure

#### Scenario: Invalid provenance is rejected
- **WHEN** a malformed or placeholder NotebookLM reference reaches the CLI
- **THEN** it exits with status 2, concise stderr, and no traceback

### Requirement: Fail-closed verification gates
The delivery MUST pass unit, compile, build, skill, CSV, report, strict OpenSpec, evidence-link, and manual surface checks before publication.

#### Scenario: Any required check fails
- **WHEN** a deterministic gate or observed user surface contradicts the report
- **THEN** publication remains blocked until a scoped repair passes or the unresolved blocker is truthfully reported

### Requirement: Immutable public handoff
The delivery MUST stage only intended artifacts, commit them, push the current branch, verify the remote branch equals the exact local full SHA, and retrieve the SHA-pinned public report blob.

#### Scenario: Verification is publicly complete
- **WHEN** all evidence and gates pass
- **THEN** the final handoff includes the full commit SHA and a working immutable GitHub blob URL containing the requested report
