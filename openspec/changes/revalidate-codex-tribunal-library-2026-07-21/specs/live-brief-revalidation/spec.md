## ADDED Requirements

### Requirement: Authenticated canonical IDR
The verification SHALL use the authenticated canonical NotebookLM notebook, expose its real notebook link in the report, and retain a pass-specific source/query ledger.

#### Scenario: Canonical notebook is live
- **WHEN** the operator checks authentication, notebook identity, and the source inventory
- **THEN** the ledger records a successful authenticated check, the canonical notebook ID/link, and concrete current source IDs without cookies or private account data

### Requirement: Source-grounded cross-query research
The verification SHALL query multiple relevant OSS sources from the canonical notebook for knowledge, risk, and UX perspectives and SHALL execute a separate contradiction/source-attribution control.

#### Scenario: Cross-query evidence is complete
- **WHEN** NotebookLM returns the role-aligned answers and control answer
- **THEN** the ledger records each question, answer, cited source IDs, unresolved uncertainty, and any conflict resolved against primary or executable evidence

### Requirement: Current OSS-first comparison
The verification SHALL compare established OSS candidates before recommending custom work, SHALL record bare canonical GitHub URLs and numeric star counts, and SHALL score candidates with one stable 100-point rubric.

#### Scenario: Feature matrix has one recommendation
- **WHEN** the current primary metadata snapshot and feature assessment are complete
- **THEN** the matrix contains differentiated capability cells, totals at or below 100, exactly one crown, and an explanation that stars are context rather than score points

### Requirement: Three isolated adversarial judgments
The verification SHALL attempt three independent Grok single-turn judgments covering knowledge/correctness, harsh criticism/risks, and UX/implementability without exposing sibling verdicts to any judge. If a Grok attempt returns no model output, the verification SHALL retain that failure and MAY use the brief-authorized `agy` perspective fallback for the affected role.

#### Scenario: Judge outputs are admissible
- **WHEN** the three isolated role paths finish through Grok or a documented `agy` fallback
- **THEN** each accepted output identifies its role, engine/model provenance, and evidence scope; provides a 0-100 score and recommendation; lists concrete findings and unresolved gaps; states limitations; and preserves every no-output attempt as excluded provenance

### Requirement: Evidence-controlled synthesis
The report SHALL distinguish factual primary evidence, NotebookLM synthesis, external judge opinion, project-authored scores, and local structural runtime output, and SHALL not upgrade an unsupported model claim into fact.

#### Scenario: Conflicting claims are synthesized
- **WHEN** a model output conflicts with checked-out code, GitHub metadata, or executable behavior
- **THEN** the report names the conflict, uses primary or executable evidence as controlling proof, and preserves the model error as a limitation

### Requirement: Explicit crown and implementation plan
The report SHALL provide three tribunal verdicts, agreements and disagreements, exactly one crowned recommendation, a Mermaid architecture/adoption flow, and an actionable phased implementation plan.

#### Scenario: Decision artifact is consumable
- **WHEN** an operator reads the report without the raw ledgers
- **THEN** the operator can identify the selected OSS approach, its trade-offs, the rejected alternatives, the next implementation steps, and the evidence limitations

### Requirement: Executable end-to-end proof
The recommendation SHALL be exercised through source execution, package build, clean installation, console entry point, installed Python API, and an expected-error path using a real comparison case.

#### Scenario: Packaged recommendation works
- **WHEN** the operator builds and installs the artifact into a fresh environment and runs the comparison case
- **THEN** the CLI and API return structurally valid tribunal results, the expected limitation markers remain truthful, and invalid input fails cleanly without a traceback

### Requirement: Repeatable repository gates
The verification SHALL run the unit, compile, example, skill, CSV, report, OpenSpec, and evidence-consistency gates after all relevant edits.

#### Scenario: Local handoff is green
- **WHEN** the final gate set runs against the completed worktree
- **THEN** every required check exits successfully or a pre-existing unrelated failure is explicitly named without being weakened or deleted

### Requirement: Immutable public handoff
The completed report and supporting changes SHALL be committed and pushed, and the handoff SHALL use a SHA-pinned public GitHub blob URL proven to match the local commit.

#### Scenario: Public artifact matches local result
- **WHEN** local validation is complete and the commit is pushed
- **THEN** local HEAD equals the remote branch SHA, the clean tree is confirmed, and the SHA-pinned report content is retrievable
