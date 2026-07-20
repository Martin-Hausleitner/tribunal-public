# End-to-end release proof

Verified UTC: `2026-07-20T17:30:11Z`  
Runtime: `Python 3.12.3`  
Pre-verification base commit: `e1172bea919ffd28d1f245599f17c9abcda12fd0`

This ledger records direct execution of the public library, CLI, package, gates, and failure paths. It is not a semantic verdict from the deterministic `local-rules` backend. Live NotebookLM research and external-model verdict provenance remain in their dedicated evidence ledgers.

## Automated contracts and deterministic gates

Executed from the repository root:

```bash
python -m unittest discover -s tests -v
python -m py_compile tribunal.py personas/__init__.py scripts/csv_gate.py scripts/report_gate.py scripts/skill_gate.py tests/test_tribunal.py examples/e2e_demo.py examples/phase1_core_modes.py
python scripts/skill_gate.py skill/SKILL.md
python scripts/csv_gate.py report/codex-trib-lib-matrix.csv
python scripts/report_gate.py report/codex-trib-lib-tribunal.md
openspec validate finish-codex-tribunal-library --strict
```

Observed:

- `18` unit tests passed in `0.219s`.
- Compilation exited `0` for the runtime, persona package, gates, tests, and examples.
- Skill gate passed with all Tribunal contracts.
- CSV gate passed with `10` rows, one crown for Codex Tribunal, score spread `53-85`, and snapshot `2026-07-20T15:53:55Z`.
- Report gate passed with the canonical NotebookLM URL, `10` GitHub repositories, and exactly one crown.
- Strict OpenSpec validation passed.

The negative gates were also exercised against `README.md`: the CSV gate exited `1` for missing matrix columns, and the report gate exited `1` for missing mandatory report sections.

## Real CLI modes

Each primary CLI mode was run as JSON with `--hardness hard`; the comparison mode was run with two requested rounds.

| Mode | Requested/effective rounds | Views | Final score | Marker | Declared evidence gaps |
|---|---:|---:|---:|:---:|---:|
| `knowledge` with canonical NotebookLM reference | 1/2 | 6 | 50 | `⚠️` | 12 |
| `critique` | 1/2 | 6 | 40 | `⚠️` | 12 |
| `ui_ux` | 1/2 | 6 | 40 | `⚠️` | 12 |
| `comparison` | 2/2 | 6 | 40 | `⚠️` | 12 |

The comparison output contained six persona slugs across two panels, `post-hoc-synthesis`, seven disagreement/persona-lens entries, and no false crown. All views recorded `local-rules` as backend and engine.

## Public Python API anti-fake boundary

A minimal custom `JudgeBackend` driver returned three `95/100` views twice. With one declared gap per view, the real orchestrator returned `⚠️`; with empty gap lists, it returned `✅`. Both verdicts said `isolated judge views across 1 evaluation round`, avoiding a claim that repeated rounds or providers are statistically independent.

## Installed-package E2E

A new temporary virtual environment built and installed the project through PEP 517, producing and installing `codex_tribunal-1.0.0-py3-none-any.whl`. The installed `tribunal` console script then ran this real comparison path:

```bash
tribunal --mode comparison --rounds 2 --hardness hard \
  --target "Final installed package E2E" --json
```

Observed installed-package result:

```json
{
  "mode": "comparison",
  "requested_rounds": 2,
  "rounds": 2,
  "views": 6,
  "unique_personas": 6,
  "backend": ["local-rules"],
  "score": 40,
  "crown": "⚠️",
  "declared_evidence_gaps": 12
}
```

Loading six unique bundled personas through the installed console script proves that the wheel retained the JSON package data. The final verdict explicitly reported six isolated judge views and preserved every evidence gap.

## Expected failure path

The invalid reference command:

```bash
python tribunal.py --target "bad reference" \
  --notebooklm-url https://example.com/notebook/id
```

exited `2`, printed exactly the concise `tribunal: error: NotebookLM URL must match https://notebooklm.google.com/notebook/<id>` boundary message, and emitted no traceback.

## Live external checks used by the release

- NotebookLM returned the canonical ID/title, `330` sources, public sharing, and a new source-grounded control query under conversation `1ebabb83-484f-405b-8b24-a26cfa5b9afb`.
- GitHub returned all ten matrix repositories as reachable and unarchived. Star drift from the dated release snapshot was only `0` through `+7`; stars remain adoption metadata and contribute zero rubric points.
- The pinned public report blob is checked again after the final release commit and push; the successful final URL is reported in the handoff.
