# Tribunal Independent Verdict: UX and Implementability (Judge 3)

**Engine:** `agy` / `Gemini 3.5 Flash (High)`  
**Perspective:** Judge 3 (UX and Implementability)  
**Scope:** Evaluation of the Tribunal library, CLI tools, Python API architecture, personas, skill, example runs, test suites, documentation, and OpenSpec design artifacts based on operator workflow, discoverability, error handling, provenance, accessibility, onboarding, and integration cost.

## Severity-Ordered Findings

### 1. CRITICAL: Stateful Quota Depletion Across Repeated Orchestrator Runs

- **File Reference**: `tribunal.py:221`, `tribunal.py:506`, `tribunal.py:539`
- **Impact**: The `EngineManager` is initialized once inside `TribunalOrchestrator.__init__` and statefully decrements capacities when `allocate` is called in `judge()`. If a developer reuses the same orchestrator instance to judge multiple targets, subsequent calls can exhaust the configured capacity and fail. No reset API exists.

### 2. MAJOR: Stateless JudgeRequest Contract Prevents True Agentic Debate

- **File Reference**: `tribunal.py:59`, `tribunal.py:541`, `tribunal.py:646`
- **Impact**: `JudgeRequest` contains no sibling or earlier verdict context. Custom live backends cannot implement interactive debate through the current call. The report's Debate section is post-hoc synthesis rather than runtime inter-agent exchange.

### 3. MAJOR: CLI Crashes with Raw Exception Tracebacks on User Input Failures

- **File Reference**: `tribunal.py:687`
- **Impact**: `main()` does not trap orchestrator errors. A malformed NotebookLM URL, unknown persona slug, or bad quota file produces a raw Python traceback rather than a concise operator error.

### 4. MODERATE: Poor Parameter Discoverability in CLI Help Output

- **File Reference**: `tribunal.py:675`
- **Impact**: Only `--personas` and `--json` have descriptive help. The other flags lack explanations.

### 5. MODERATE: Fragile Target-Word-Matching for Persona Selection

- **File Reference**: `tribunal.py:347`
- **Impact**: Minor wording changes can change target keyword matches and selected personas, reducing baseline stability.

### 6. MINOR: Missing Standard Python Packaging Files

- **File Reference**: workspace root
- **Impact**: No `pyproject.toml`, `setup.py`, or `requirements.txt` exists. Standard installation requires manual path handling.

## Score and Rationale: 74/100

- **Type Fit (22/25)**: Required modes and rounds/hardness mappings are clean.
- **Adversarial Depth (15/20)**: Unique persona selection and backend isolation are enforced; runtime interactive debate is absent.
- **Evidence Provenance (18/20)**: Strong metadata, source, and gap recording; live retrieval remains caller work.
- **Persona/Skill Extensibility (12/15)**: Personas are discoverable validated JSON.
- **Observability/Repeatability (4/10)**: Structured output is offset by stateful capacity and target-sensitive ranking concerns.
- **Integration Cost (3/10)**: Dependency-free core is small, but absent packaging and live integration increase work.

## Evidence Inspected

1. `tribunal.py`
2. `tests/test_tribunal.py`, `examples/phase1_core_modes.py`, `examples/e2e_demo.py`
3. `scripts/skill_gate.py`, `scripts/csv_gate.py`, `scripts/report_gate.py`
4. `README.md`, `skill/SKILL.md`, `personas/andrej-karpathy.json`, `personas/ux-operator-flow.json`
5. OpenSpec proposal and design
6. `report/evidence/notebooklm-idr.md`, `report/evidence/grok-evidence-packet.md`

## Evidence Gaps and Unsupported Claims

- No visual or viewport testing: there is no TUI, GUI, or browser automation.
- No live provider/LLM orchestration: credentials, rate limits, prompt tokens, and active endpoints are outside the core.
- The Debate output is a post-hoc summary of independent non-communicating runs, not interactive agent debate.

## Recommendation: Ship-with-Conditions

1. Fix capacity depletion so an orchestrator instance is reusable.
2. Convert expected input failures to concise CLI errors.
3. Document every CLI argument.
4. Consider a future, separate interactive-debate contract rather than implying it exists now.
5. Add standard Python packaging.

I did not inspect any other Tribunal judge output.
