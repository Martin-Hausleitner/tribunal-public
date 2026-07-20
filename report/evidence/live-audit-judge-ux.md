# Live-audit judge verdict: UX and implementation feasibility

**Engine:** `agy` / `Gemini 3.5 Flash (High)`  
**Execution:** fresh isolated read-only plan session  
**Input:** `report/evidence/live-audit-judge-packet.md` plus independently inspected repository surfaces  
**Normalization:** Local `file://` links from the model output are rendered below as repository paths; conclusions and scores are unchanged.

## 1. Scope and Perspective

- **Assigned Perspective:** Independent UX and Implementation Feasibility Judge.
- **Scope:** Evaluation of public CLI and Python API usability, packaging, installability, error recovery, output and provenance representation, repeated-use limits, skill routing, evidence workflow, and verification of claims that cannot be programmatically validated without a GUI.
- **Repository Snapshot Base:** `a8caf856425dc88be124a58e9be1aee2a8cf3df6`

## 2. Severity-Ordered Findings

### High Severity

1. **Line-Break and Formatting Stripping in Markdown Output**
   - **Reference:** `tribunal.py:23` and `tribunal.py:31` (`_markdown_text` and `_markdown_code`)
   - **Impact:** Both helpers normalize text via `" ".join(str(value).split())`. This replaces all newlines, tabs, and consecutive spaces with a single space. If a custom live backend returns a structured verdict, detailed findings, or bulleted evidence containing Markdown tables, lists, or line breaks, the format is flattened into a single line. This severely breaks output readability, forcing operators to consume raw JSON reports instead of reading the Markdown report.
2. **Top-Level Package Namespace Pollution**
   - **Reference:** `pyproject.toml:26` (`setuptools` configuration)
   - **Impact:** The metadata specifies `packages = ["personas"]`. This places the generic folder `personas` as a top-level package directly in `site-packages`. This introduces a high risk of name clashes and installation failures in user environments if other packages named `personas` exist or if the user creates a local `personas` module.

### Medium Severity

3. **Redundant Silent Evaluator Panels in Custom Runs**
   - **Reference:** `tribunal.py:607` (`judge()` panel offset)
   - **Impact:** When an operator requests exactly three unique personas via CLI `--personas` or Python `requested_personas`, the offset is calculated as `(round_index - 1) * 3`. Since the panel has three personas, the offset modulo three is always zero. Consequently, in brutal or multi-round runs, the exact same panel is evaluated in every round without raising a warning. When using a live, paid LLM backend, this silently consumes API quota and charges for redundant, identical calls without providing adversarial statistical diversity.
4. **Asymmetric CLI and API Capacity Options**
   - **Reference:** `tribunal.py:222` (`EngineManager` initialization) and `tribunal.py:787` (`_build_parser` parameters)
   - **Impact:** The Python API allows passing raw JSON capacity limits directly via `quota_json`. The CLI parser only exposes `--quota-file` and lacks a `--quota-json` option. CLI operators are forced to write a file to disk or export environment variables to control capacities, creating functional asymmetry.
5. **Silent Propagation of Typos in Persona Skills**
   - **Reference:** `tribunal.py:424` (`SkillRouter.route`)
   - **Impact:** Persona skills from JSON files are blindly appended and sorted. There is no dictionary check or validation that declared skills correspond to active capability files or are recognized by the system. Typos are silently routed and output in the report's evidence list, creating a false impression of capability coverage.

### Low Severity

6. **Bubbling of Live Backend Network Errors in CLI**
   - **Reference:** `tribunal.py:805` (`main` exception block)
   - **Impact:** The parser catches `OSError`, `RuntimeError`, `TypeError`, and `ValueError` to exit cleanly with code `2`. If a live backend raises other exception types, they bypass this handler, bubbling up as raw Python tracebacks and exiting with code `1`, which harms operational consistency.
7. **Unchecked Visual/Interaction Claims in Offline Mode**
   - **Reference:** `README.md:147` and `skill/SKILL.md:48`
   - **Impact:** While documented, the library does not validate the existence of screenshots or interface telemetry files before scoring. The compliance boundary remains an unchecked verbal instruction.

## 3. What Cannot Be Claimed Without a GUI

For a `ui_ux` mode tribunal, visual polish/alignment, render-time accessibility, micro-animations/interactions, and task success/cognitive load cannot be verified through the current CLI or static code inspection. These require actual viewport and interaction observations.

## 4. Rubric Component Scores

| Rubric Category | Weight | Score | Rationale |
|---|---:|---:|---|
| Type Fit | 25 | 23 | Clean mapping of four modes in CLI/API; deduction for post-hoc-only exchange. |
| Adversarial Depth | 20 | 18 | Strong unanimous-marker constraints; deduction for repeated explicit panels and absent family independence. |
| Evidence Provenance | 20 | 19 | Transparent allocation metadata; deduction for flattened Markdown evidence. |
| Persona/Skill Extensibility | 15 | 11 | Straightforward JSON; deduction for generic package namespace and unvalidated skill labels. |
| Observability/Repeatability | 10 | 9 | Friendly help and expected exit-2 paths; deduction for arbitrary backend exceptions. |
| Integration Cost | 10 | 9 | Dependency-free; deduction for CLI/API quota-input asymmetry. |
| **Total** | **100** | **89** | **Strong overall setup with packaging and output-format concerns.** |

## 5. Evidence Inspected

- `README.md`
- `tribunal.py`
- `pyproject.toml`
- `skill/SKILL.md`
- `report/evidence/notebooklm-live-audit.md`
- `report/evidence/live-audit-judge-packet.md`
- `personas/andrej-karpathy.json`, `personas/ux-operator-flow.json`, `personas/security-auditor.json`, `personas/systems-architect.json`
- `examples/e2e_demo.py`, `examples/phase1_core_modes.py`
- `tests/test_tribunal.py` (inspected and executed)
- Live-audit OpenSpec proposal, design, tasks, and capability spec

## 6. Gaps and Unsupported Claims

- **Model-family independence:** no programmatic enforcement exists; payload isolation is weaker.
- **Visual proof ingestion:** no image or binary upload surface exists to establish `ui_ux` visual assertions.

## 7. Recommendation and Prioritized Actions

**Recommendation:** **Ship with conditions**

1. Preserve multiline/list readability in Markdown output.
2. Move bundled personas under a namespaced package to reduce collision risk.
3. Add CLI `--quota-json` parity.
4. Warn when an explicit panel repeats across rounds.
5. Handle custom-backend operational errors consistently without raw tracebacks.

I did not inspect any other live-audit judge output.
