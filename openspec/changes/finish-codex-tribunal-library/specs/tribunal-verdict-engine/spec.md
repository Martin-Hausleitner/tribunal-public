## ADDED Requirements

### Requirement: Supported tribunal types
The library SHALL expose `knowledge`, `critique`, and `ui_ux` as primary tribunal types and MAY expose `comparison` as an additional reporting type. The Python API and CLI SHALL use the same identifiers.

#### Scenario: Run every primary type
- **WHEN** an operator runs one verdict for each primary tribunal type
- **THEN** each run completes with the requested mode recorded in its serialized report

### Requirement: Three independent judges per round
The orchestrator SHALL assign exactly three unique personas per round, invoke the configured backend separately for each assignment, and delay debate synthesis until all judge views have been collected.

#### Scenario: Two-round hard tribunal
- **WHEN** an operator requests two rounds at hard severity
- **THEN** the report contains six judge views, three unique persona slugs in each round, and one synthesis created after those views

### Requirement: Hardness and Nx semantics
The engine SHALL reject round counts below one and SHALL enforce minimum effective rounds of one for `light` and `standard`, two for `hard`, and four for `brutal`, while preserving both requested and effective round counts.

#### Scenario: Brutal mode expands work
- **WHEN** a caller requests one round with `brutal` hardness
- **THEN** the report records one requested round and four effective rounds with twelve judge views

### Requirement: Honest backend and engine provenance
Every judge view SHALL identify the backend and engine used. The default runtime SHALL identify itself as a local deterministic rules backend and SHALL NOT report assumed third-party quotas. External quota plans MUST come from explicit caller, environment, or file input.

#### Scenario: Offline default run
- **WHEN** a caller runs the orchestrator without quota configuration or a custom backend
- **THEN** all views identify local rule evaluation and no third-party provider or free-quota claim appears

#### Scenario: Explicit engine capacity
- **WHEN** a caller supplies valid JSON capacities for external engines
- **THEN** the per-run allocator records that explicit source and assigns only configured engines with remaining capacity without permanently depleting later `judge()` calls

### Requirement: Evidence-aware judge output
Each judge view SHALL contain a bounded integer score from 0 through 100, persona-specific findings, explicit evidence, and explicit unresolved evidence gaps. A syntactically valid NotebookLM reference MAY be recorded, but the engine MUST NOT state that its content was verified unless a backend provides such evidence.

#### Scenario: No external evidence
- **WHEN** the local rules backend judges a text target without a NotebookLM reference
- **THEN** the view records the missing external research as an evidence gap rather than a verified claim

### Requirement: Strict public-input validation
The library SHALL reject malformed hardness values, quota payloads, requested persona slugs, backend results, and NotebookLM references with actionable exceptions.

#### Scenario: Invalid NotebookLM host
- **WHEN** a caller supplies an HTTPS URL whose host is not `notebooklm.google.com`
- **THEN** construction fails before judging and identifies the invalid NotebookLM reference

#### Scenario: Unknown requested persona
- **WHEN** a caller requests any persona slug absent from the library
- **THEN** judging fails and lists the unknown slug instead of silently substituting a different persona

### Requirement: Stable report serialization
Verdict reports SHALL serialize to UTF-8-safe JSON-compatible dictionaries, JSON, and Markdown while preserving target, mode, requested/effective rounds, hardness, provenance, views, debate, evidence gaps, numeric score, and recommendation marker.

#### Scenario: Round-trip structural inspection
- **WHEN** a caller parses `to_json()` and reads `to_markdown()` for the same report
- **THEN** both representations expose the same mode, round counts, judge identities, provenance, and final score

### Requirement: Bounded reusable public surface
The orchestrator SHALL bound requested rounds and target length, remain reusable across repeated `judge()` calls, HTML-escape the target in Markdown only, and render expected CLI input/configuration failures without a Python traceback.

#### Scenario: Reuse explicit capacity
- **WHEN** a caller invokes `judge()` twice on one orchestrator whose explicit capacity fits each individual run
- **THEN** both runs receive the same valid per-run allocation plan
