## ADDED Requirements

### Requirement: OpenSpec-first execution
The verification pass SHALL define its scope, technical decisions, testable requirements, and checkable implementation tasks in a repo-local OpenSpec change before mutating the report, matrix, or runtime.

#### Scenario: Planning contract precedes implementation
- **WHEN** the final live verification begins
- **THEN** proposal, design, specification, and task artifacts exist and strict OpenSpec validation passes before implementation evidence is published

### Requirement: Authenticated canonical NotebookLM research
The verification pass MUST authenticate to NotebookLM, identify the canonical notebook, verify its public link and source states, and use only successfully processed sources as grounding evidence.

#### Scenario: Canonical notebook is revalidated
- **WHEN** the pass inspects the research corpus
- **THEN** the evidence records authenticated identity, canonical notebook ID/link, sharing state, source totals, processed source IDs used, failed-source exclusions, and observation time

#### Scenario: Capacity or processing fails safely
- **WHEN** a source cannot be added or processed because of account, notebook, or service limits
- **THEN** the failure is recorded and no unrelated notebook or source is deleted, renamed, repurposed, or represented as processed

### Requirement: Source-grounded cross-query IDR
The verification pass SHALL execute multiple fresh role-specific NotebookLM queries covering correctness, hostile risks, UX feasibility, OSS composition, and contradiction/source attribution, with non-circular controls that exclude prior Tribunal reports.

#### Scenario: Cross-queries are auditable
- **WHEN** NotebookLM returns a research answer
- **THEN** the query role, conversation provenance, selected/used source metadata, decision-relevant synthesis, and manual correction of stale or unsupported claims are retained

#### Scenario: Prior reports do not prove current claims
- **WHEN** a broad answer relies on a historical Tribunal report
- **THEN** it is treated as provenance only and a control query grounded in primary or independent sources is used for the current conclusion

### Requirement: Three independent adversarial verdicts
The verification pass MUST obtain separate initial judgments for knowledge/correctness, harsh criticism/risks, and UX/implementability from isolated sessions against one frozen conclusion-free packet.

#### Scenario: Preferred Grok path succeeds
- **WHEN** `grok --single -m grok-4.5 --effort high` returns a usable verdict for a role
- **THEN** that verdict is retained with role, engine, session, packet hash, score, recommendation, findings, risks, required evidence, and limitations

#### Scenario: Authorized fallback is required
- **WHEN** a required Grok call produces no model verdict because of quota, service, authentication, or execution failure
- **THEN** the exact failure is retained and a fresh isolated `agy` perspective MAY supply that role's verdict with full provenance and explicit provider-diversity limitations

### Requirement: OSS-first primary-source comparison
The verification pass SHALL compare Codex Tribunal with relevant existing OSS before recommending custom work, using current primary GitHub metadata and root documentation.

#### Scenario: Candidate metadata is refreshed
- **WHEN** the feature matrix is evaluated
- **THEN** each candidate has a real GitHub URL, numeric dated star count, relevant maintenance/license caveats, and evidence derived from primary GitHub surfaces

#### Scenario: Popularity does not determine fit
- **WHEN** the 100-point scores are calculated
- **THEN** stars contribute zero points, the weighted rubric totals exactly 100, category mismatches remain explicit, and score arithmetic matches the machine-readable matrix

### Requirement: One bounded winner and implementation plan
The report MUST name exactly one crowned winner for the declared use case, explain the bounded recommendation, include a Mermaid decision flow, and provide a concrete implementation plan that prefers composition with mature OSS over reinvention.

#### Scenario: Crown is unambiguous and qualified
- **WHEN** the final report is validated
- **THEN** exactly one matrix row and one recommendation identify the crown while disclaimers prevent interpreting it as an independent benchmark or universal superiority claim

### Requirement: Real end-to-end recommendation proof
The verification pass MUST exercise a concrete comparison case through the actual Codex Tribunal source, built distribution, clean-installed CLI, installed API, expected-error behavior, reusable skill, matrix, and report surfaces.

#### Scenario: User-facing package workflow works
- **WHEN** a user installs the newly built wheel in an isolated environment and runs the documented comparison case
- **THEN** the CLI and API return schema-valid three-judge output with the declared backend/provenance, preserve all evidence gaps, and emit concise non-traceback errors for invalid input

#### Scenario: Recommendation artifacts agree
- **WHEN** the E2E gate reads the JSON output, matrix, report, and skill
- **THEN** their modes, limitations, winner count, URLs, scores, NotebookLM link, and required evidence labels are mutually consistent

### Requirement: Evidence-class separation and synthesis
The final synthesis SHALL separate current executable facts, primary metadata, NotebookLM synthesis, external judge opinion, project-authored scoring, historical findings, hypotheses, and pending proof.

#### Scenario: Generated contradiction is resolved
- **WHEN** NotebookLM or a judge conflicts with current source or reproduced execution
- **THEN** the report states the conflict, assigns authority to the direct evidence, and does not silently promote generated prose into fact

### Requirement: Fail-closed public handoff
Completion MUST be gated by clean diagnostics, tests, compile, build, distribution contents, clean installation, live CLI/API/error checks, skill/report/matrix/OpenSpec validators, reviewed diff, push, and immutable public retrieval at the final commit SHA.

#### Scenario: Publication is verifiable
- **WHEN** all local checks pass and the change is committed
- **THEN** the exact commit is pushed and the report is retrievable through a public SHA-pinned GitHub blob or raw URL whose content matches the committed artifact

#### Scenario: A gate fails
- **WHEN** any required local, external, or publication check does not establish its claimed behavior
- **THEN** the pass records the failure and withholds the corresponding completion claim rather than substituting inherited evidence
