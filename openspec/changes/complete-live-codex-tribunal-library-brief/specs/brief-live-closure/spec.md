## ADDED Requirements

### Requirement: OpenSpec-first live baseline
The delivery SHALL create and strictly validate a distinct OpenSpec change before new live research or judge synthesis, and SHALL record the starting repository and tool state.

#### Scenario: Fresh pass begins
- **WHEN** a new live brief run starts from a previously completed repository state
- **THEN** a new proposal, design, capability spec, task list, and baseline identify what evidence must be observed again

### Requirement: Authenticated canonical IDR
The delivery MUST use the authenticated `nlm` CLI with the canonical NotebookLM notebook, verify notebook identity and relevant source state, run three role-aligned cross-source queries plus a contradiction/source-attribution control, and publish `IDR: ja` with the canonical link and truthful grounding limitations.

#### Scenario: Live NotebookLM research completes
- **WHEN** the canonical notebook and required current sources are available
- **THEN** the evidence records notebook identity, source counts, query prompts, returned grounding metadata, answers, contradictions, and manual corrections without exposing credentials

#### Scenario: NotebookLM cannot complete a required operation
- **WHEN** authentication, source processing, or a query fails
- **THEN** the delivery preserves the failure and does not claim that operation succeeded

### Requirement: OSS-first primary comparison
The delivery SHALL compare viable existing OSS before recommending custom work, SHALL use canonical GitHub links and current numeric stars, and MUST apply a documented 100-point rubric with differentiated totals and exactly one evidence-eligible crowned winner.

#### Scenario: Candidate metadata is mutable
- **WHEN** the comparison is refreshed
- **THEN** primary GitHub metadata, license qualification, archive/activity signals, score dimensions, totals, URLs, and crown state agree across the snapshot, CSV, and report while stars contribute zero score points

### Requirement: Three isolated adversarial perspectives
The delivery MUST independently obtain or truthfully attempt knowledge/correctness, harsh criticism/risk, and UI/UX feasibility judgments, attempting `grok --single -m grok-4.5 --effort high` first for every role and using only an explicitly authorized fallback when Grok produces no complete answer.

#### Scenario: Role verdict succeeds
- **WHEN** an approved provider returns a complete role judgment
- **THEN** the retained verdict identifies its role, provenance, score, recommendation, evidence, risks or gaps, and independence conditions

#### Scenario: Provider fails before a verdict
- **WHEN** Grok or an authorized fallback exits without a complete role judgment
- **THEN** the failure is retained and excluded from accepted verdict synthesis rather than being presented as model output

### Requirement: Evidence-bound synthesis and public report
The delivery SHALL publish `report/codex-trib-lib-tribunal.md` with the IDR declaration and link, three role verdicts, agreements and disagreements, the 100-point feature matrix, exactly one crown, recommendation, limitations, Mermaid evidence flow, and an actionable implementation plan.

#### Scenario: Report is finalized
- **WHEN** IDR, OSS metadata, judge attempts, and E2E observations have been frozen
- **THEN** every public claim is traceable to the correct evidence class and the report does not overstate semantic, provider-independence, or visual-UX proof

### Requirement: Real end-to-end package proof
The delivery MUST run a realistic Tribunal case through the source CLI, all three primary modes, a comparison path, an expected invalid-input path, a clean PEP 517 build and installation, the installed console entry point outside the source tree, and the installed Python API, without mocked model or backend results.

#### Scenario: Bounded local recommendation works
- **WHEN** a user runs the actual source and installed package surfaces
- **THEN** output is structurally valid, provenance and evidence gaps remain visible, the synthetic persona disclaimer survives serialization, and deterministic readiness is not mislabeled as semantic proof

#### Scenario: Invalid NotebookLM input is rejected
- **WHEN** a placeholder or malformed NotebookLM reference is supplied
- **THEN** the CLI exits with status 2, concise stderr, and no traceback

### Requirement: Fail-closed gates
The delivery MUST pass relevant unit tests, compile checks, package build, skill, CSV, report, strict OpenSpec, and evidence-link checks before publication.

#### Scenario: A required gate fails
- **WHEN** a deterministic release check exits nonzero or the observed artifact contradicts the report
- **THEN** completion and publication are blocked until the scoped defect is fixed or truthfully reported as an unresolved blocker

### Requirement: Commit, push, and immutable handoff
The delivery MUST stage the intended artifacts, commit them, push the current branch, verify the remote branch resolves to the exact local full SHA, and retrieve the SHA-pinned public report blob.

#### Scenario: Public closure succeeds
- **WHEN** all gates and manual observations pass
- **THEN** the final handoff reports the commit SHA and a working immutable GitHub blob URL containing the requested report
