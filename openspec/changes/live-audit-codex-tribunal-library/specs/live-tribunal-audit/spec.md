## ADDED Requirements

### Requirement: Canonical live NotebookLM research
The audit SHALL use one identifiable NotebookLM notebook, add authoritative primary and relevant OSS sources, run multiple cross-source queries, and record the live notebook URL plus decision-relevant sourced findings.

#### Scenario: Canonical IDR evidence is produced
- **WHEN** the live research phase completes
- **THEN** the evidence identifies one notebook URL, its source corpus, at least three cross-queries, source-attributed findings, contradictions or limitations, and an explicit `IDR: ja` report header

### Requirement: Three independent adversarial judgments
The audit SHALL obtain three separately executed verdicts for knowledge/correctness, hard criticism/risks, and UX/feasibility using Grok 4.5 high effort or the brief-approved isolated fallback, with truthful engine provenance.

#### Scenario: Judge independence and scope are auditable
- **WHEN** all tribunal perspectives have completed
- **THEN** three distinct raw outputs identify their role, execution command or engine, independent recommendation, failure modes, evidence gaps, and confidence before synthesis begins

### Requirement: OSS-first comparison and crown
The audit SHALL compare viable existing OSS solutions using verified canonical GitHub links, snapshot star counts, licensing and activity evidence, a predeclared differentiated rubric totaling 100 points, and exactly one crowned recommendation.

#### Scenario: Recommendation is reproducible
- **WHEN** a reviewer recalculates each candidate from the report matrix
- **THEN** every total equals the sum of its category scores, no category exceeds its weight, the ranking is unambiguous, and exactly one candidate carries the crown

### Requirement: Persona and tribunal-type coverage
The audited solution SHALL support knowledge/correctness, hard criticism/risk, and UX/feasibility tribunal types plus a clearly disclosed Karpathy-inspired implementation critic without impersonating a real person.

#### Scenario: Library and skill expose the required modes
- **WHEN** a user inspects the public API, CLI help, persona data, and reusable skill instructions
- **THEN** all three tribunal types are routable, persona provenance is explicit, and expected structured verdict fields are documented

### Requirement: Real end-to-end proof
The audit MUST exercise the recommended solution through its public user-facing surface with a realistic input and MUST preserve a non-mocked proof/log that demonstrates the claimed output contract.

#### Scenario: CLI tribunal case succeeds
- **WHEN** the realistic test case is submitted through the documented CLI entry point
- **THEN** the process exits successfully and yields three independent judge records, the selected tribunal type, synthesis, provenance, evidence gaps, and pressure configuration in machine-checkable output

### Requirement: Publication-ready tribunal report
The audit SHALL deliver `report/codex-trib-lib-tribunal.md` containing the IDR dossier, three verdicts, synthesis, 100-point feature matrix, one crown, Mermaid flow, implementation plan, E2E proof, limitations, and traceable evidence links.

#### Scenario: Report passes delivery gates
- **WHEN** the final report and evidence are validated, committed, and pushed
- **THEN** automated checks pass, the remote branch contains the exact commit, and a verified GitHub blob URL resolves to the delivered report
