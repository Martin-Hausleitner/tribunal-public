## ADDED Requirements

### Requirement: Validated persona discovery
The persona library SHALL load sorted `personas/*.json` files, require non-empty name, role, stance, instructions, skills, and bare HTTPS GitHub repository references, preserve an optional non-empty disclaimer, and fail with the source path and field name when a document is invalid.

#### Scenario: Malformed persona file
- **WHEN** a persona JSON file omits its role
- **THEN** library initialization fails with an error naming both that file and the missing `role` field

### Requirement: Mode-specific persona routing
Persona selection SHALL prioritize source/correctness expertise for knowledge tribunals, architecture/security/implementation expertise for critique tribunals, and interaction/accessibility/visual expertise for UI/UX tribunals while preserving three unique assignments per round.

#### Scenario: UI and UX assignment
- **WHEN** a `ui_ux` tribunal selects its first-round panel from the bundled library
- **THEN** all three selected personas carry UI, UX, workflow, accessibility, or visual-design expertise

### Requirement: Karpathy-inspired technical critic
The bundled library SHALL include a persona clearly labeled as inspired by Andrej Karpathy's public implementation-first work, with public reference repositories, minimalism and understandability pressure, and an explicit non-endorsement statement.

#### Scenario: Inspect persona provenance
- **WHEN** an OSS user reads the Karpathy-inspired persona document and README
- **THEN** they can identify the public references and understand that the persona is neither authored nor endorsed by Andrej Karpathy

### Requirement: Installable Tribunal skill
The `skill/SKILL.md` artifact SHALL have valid frontmatter and SHALL instruct an agent how to select a tribunal type, choose Nx/hardness, isolate three judges, route type-specific capabilities, use real research for knowledge claims, synthesize disagreements, and apply anti-fake gates.

#### Scenario: Skill contract audit
- **WHEN** a maintainer runs the skill validation gate
- **THEN** the gate confirms all three primary types, judge independence, NotebookLM provenance, debate, evidence gaps, and exactly-one-crown guidance are present

### Requirement: Uncensored means critical, not unbounded
Documentation SHALL define “uncensored” as direct, non-sycophantic criticism that preserves factual, legal, privacy, and safety constraints and SHALL forbid invented evidence or personal impersonation.

#### Scenario: Read harsh-review guidance
- **WHEN** an agent follows the skill for a brutal critique
- **THEN** it is told to state failures plainly while retaining source, safety, and provenance requirements
