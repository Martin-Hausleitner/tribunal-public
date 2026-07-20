## ADDED Requirements

### Requirement: Canonical live NotebookLM research
The release SHALL use one real canonical NotebookLM notebook, add relevant primary and OSS sources, wait for source processing, and perform multiple cross-source queries covering architecture patterns, failure modes, UX, evidence provenance, and differentiation. The report SHALL begin its IDR section with `IDR: ja` and the real notebook link.

#### Scenario: Audit notebook provenance
- **WHEN** a reviewer follows the notebook link and reads the saved source/query ledger
- **THEN** the notebook identity, processed sources, query questions, and source-grounded answers correspond to the published IDR

### Requirement: Three independent external verdicts
The release SHALL attempt Grok 4.5 high-effort for three isolated verdicts scoped respectively to knowledge/correctness, harsh criticism/risk, and UX/implementability. If Grok is unavailable, the brief-allowed `agy` path MAY supply the verdicts and the failed Grok attempts MUST remain visible. Each completed verdict SHALL receive the same evidence packet but MUST complete without seeing the other verdicts.

#### Scenario: Inspect tribunal evidence
- **WHEN** a reviewer opens the three saved verdict artifacts
- **THEN** each names its assigned perspective, findings, score, recommendation, evidence, and unresolved gaps without depending on another judge's conclusion

### Requirement: Sourced OSS feature matrix
The report SHALL compare at least six relevant OSS alternatives using bare GitHub repository URLs, licenses, numeric star counts captured with a UTC timestamp, capability markers using `✅`, `⚠️`, or `❌`, and differentiated scores on a declared 100-point rubric.

#### Scenario: Run matrix gate
- **WHEN** the comparison CSV is passed to `scripts/csv_gate.py`
- **THEN** the gate verifies row count, link shape, numeric stars, capability markers, differentiated scores, and exactly one crown

### Requirement: One use-case-specific winner
The synthesis SHALL award exactly one `👑`, explain why that choice wins for the declared Tribunal use case, and state material category mismatches and trade-offs so the crown cannot be read as universal superiority.

#### Scenario: Read final recommendation
- **WHEN** a reviewer reads the matrix and synthesis
- **THEN** exactly one project is crowned and its recommendation is bounded to the scored use case

### Requirement: Complete publication report
`report/codex-trib-lib-tribunal.md` SHALL contain the IDR header/link, method, source inventory, query synthesis, three tribunal verdicts, debate/synthesis, scoring rubric, feature matrix, one crown, recommendation, Mermaid architecture or implementation flow, concrete implementation plan, limitations, and reproduction commands.

#### Scenario: Run report gate
- **WHEN** the final Markdown file is passed to the report validation script
- **THEN** all mandatory sections and invariants are confirmed before publication

### Requirement: Verifiable public delivery
All source, spec, evidence, gate, and report artifacts SHALL be committed and pushed to a public GitHub repository. The handoff SHALL include an HTTP-successful blob URL pinned to the delivered commit or branch.

#### Scenario: Fetch delivered blob
- **WHEN** a reviewer requests the reported GitHub blob URL without local workspace access
- **THEN** GitHub returns the published `report/codex-trib-lib-tribunal.md` content successfully
