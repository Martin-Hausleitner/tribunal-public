## ADDED Requirements

### Requirement: Authenticated canonical IDR
The revalidation SHALL use the authenticated NotebookLM CLI against the canonical notebook, SHALL expose `IDR: ja` and its notebook link in the report, and SHALL preserve dated source inventory and cross-query evidence rather than relying on an unverified URL.

#### Scenario: Canonical notebook is revalidated
- **WHEN** the live IDR begins
- **THEN** the ledger records the authenticated CLI version, notebook ID/title, sharing or retrievability state, source processing counts, and canonical link

#### Scenario: Cross-source research is completed
- **WHEN** relevant project and primary OSS sources are processed
- **THEN** at least three role-aligned cross-queries plus a contradiction/source-attribution control are recorded with grounding metadata and manual corrections

### Requirement: Independent adversarial tribunal
The revalidation MUST run separate, conclusion-free judge attempts for knowledge/correctness, harsh critique/risk, and UI/UX feasibility, MUST attempt the mandated Grok command for each role first, and MUST never present a failed or incomplete model run as a verdict.

#### Scenario: Grok returns a complete verdict
- **WHEN** a fresh role-specific Grok process exits successfully with the requested structured assessment
- **THEN** its raw output, model, effort, role, timestamp, and isolation conditions are retained as that role's candidate verdict

#### Scenario: Grok fails before a verdict
- **WHEN** a role-specific Grok process exits without a complete answer
- **THEN** the exit status and sanitized failure are retained and only a fresh approved `agy` perspective can replace the missing role

#### Scenario: Synthesis begins
- **WHEN** the accepted role outputs have been frozen
- **THEN** agreements, disagreements, missed findings, provenance limits, and the controlling verdict are synthesized without averaging incompatible role scores into false consensus

### Requirement: Evidence-bound OSS comparison
The revalidation SHALL compare viable existing OSS before recommending custom work, using bare GitHub repository URLs, a dated numeric star snapshot, license qualifications, capability cells, a documented 100-point rubric, differentiated scores, and exactly one eligible winner marker.

#### Scenario: Candidate metadata is refreshed
- **WHEN** the OSS comparison is revalidated
- **THEN** each candidate's canonical repository metadata, numeric stars, activity, and license signal are captured from live primary metadata at a common completion timestamp

#### Scenario: Winner is selected
- **WHEN** the matrix is scored
- **THEN** stars contribute zero points, every dimension stays within its declared weight, totals are reproducible, veto rules are enforced, and exactly one highest eligible entry receives `👑`

### Requirement: Honest report synthesis
The final report MUST contain the IDR declaration/link, method, source inventory, cross-query conclusions, all three accepted role verdicts, provenance and limitations, OSS matrix and scoring, one crowned recommendation, Mermaid architecture or decision flow, and an actionable implementation plan.

#### Scenario: Report is gated
- **WHEN** the report gate runs
- **THEN** it fails on missing required sections, stale or mismatched matrix facts, invalid winner relationships, missing evidence links, or a non-reproducible publication claim

### Requirement: Real end-to-end proof
The recommendation MUST be exercised without a mocked backend result through the repository CLI, all three primary modes, comparison mode, an expected invalid-input path, a clean PEP 517 installation, the installed console entry point outside the repository, and the installed Python API.

#### Scenario: Repository surfaces run
- **WHEN** the source-tree E2E commands execute
- **THEN** the three core modes and comparison complete, structured provenance and bounded gaps remain visible, and invalid NotebookLM input exits concisely with status 2 and no traceback

#### Scenario: Installed package runs
- **WHEN** a fresh temporary virtual environment installs the project through PEP 517
- **THEN** the console script and Python API execute from outside the repository with JSON/Markdown parity and the declared persona disclaimer preserved

### Requirement: Fail-closed publication
The revalidation SHALL be considered complete only after targeted and full tests, compile/build checks, skill/CSV/report gates, strict OpenSpec validation, intended-diff inspection, commit and push containment, and retrieval of the report at an immutable public GitHub blob URL.

#### Scenario: A gate fails
- **WHEN** any required validation or publication check fails
- **THEN** completion is withheld and the failure is fixed or explicitly documented as a truthful blocker without fabricating success

#### Scenario: Publication succeeds
- **WHEN** every required gate passes and the intended artifacts are committed and pushed
- **THEN** the remote commit contains the report and evidence, and an HTTP-successful SHA-pinned blob link is reported
