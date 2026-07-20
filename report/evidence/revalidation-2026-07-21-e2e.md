# Current-pass executable E2E proof

## Environment

- Python: `3.12.3`
- Starting runtime/package source: pass beginning at `56df1b0c99e3c75546585ad5e4aea6f784081db5`, with concurrent evidence-only progress commit `9b8c602`
- Fresh temporary root: `/tmp/tribunal-revalidation-20260721.FTq39Y`
- Canonical NotebookLM reference: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515

The temporary path is evidence context only; no claim depends on it remaining after this run.

## Source tests and direct user surfaces

| Surface | Command summary | Observed result |
|---|---|---|
| Unit suite | `python -m unittest discover -s tests -v` | exit `0`; `18` tests in `0.183s`; `OK` |
| Compilation | `python -m py_compile` over runtime, personas init, gates, tests, and examples | exit `0` |
| Three-mode example | `python examples/phase1_core_modes.py` | exit `0`; knowledge, critique, and UI/UX reports emitted with explicit structural gaps |
| E2E demo | `python examples/e2e_demo.py` | exit `0` |
| Real source comparison | `python tribunal.py --mode comparison --rounds 2 --hardness hard ... --notebooklm-url <canonical> --json` | exit `0`; 2 requested/effective rounds, 6 views, all `local-rules`, score `50`, two gaps/view, `post-hoc-synthesis`, marker `⚠️` |

The comparison target asked whether to retain the bounded Tribunal contract while composing established OSS for adjacent capabilities. The `⚠️` is correct: the local backend checked structure and recorded provenance but did not inspect semantic truth.

## Build and archive inspection

Command: `python -m build --outdir /tmp/tribunal-revalidation-20260721.FTq39Y/dist`

- exit `0`
- isolated build environment created
- sdist built, then wheel built from the sdist
- wheel: `codex_tribunal-1.0.0-py3-none-any.whl`
- wheel SHA-256: `e6ba78e8ace92568a85c567d63bb511aaf8a19e4aebd8487fe9b442a5e36fa5b`
- sdist SHA-256: `3e89c3b9b4c78210b8969a2376ea4f6e8181cf765321dee13820c46fea4be62d`

Wheel inspection listed `tribunal.py`, license/metadata/entry point files, `personas/__init__.py`, and all nine persona JSON files including `andrej-karpathy.json`.

## Clean install and installed console

Commands:

```text
python -m venv /tmp/tribunal-revalidation-20260721.FTq39Y/venv
<venv>/bin/python -m pip install --no-deps <wheel>
<venv>/bin/tribunal --mode comparison --rounds 2 --hardness hard ... --json
```

Observed:

- install exit `0`; `codex-tribunal-1.0.0` installed with no runtime dependency
- console exit `0` from `/tmp`, outside the repository
- `mode=comparison`, requested/effective rounds `2/2`, 6 views
- scores `[50,50,50,50,50,50]`; gap counts `[2,2,2,2,2,2]`
- engine set `[local-rules]`; final `50`; marker `⚠️`; synthesis kind `post-hoc-synthesis`
- six persona routes included systems architecture, knowledge, Karpathy-inspired criticism, and three UX lenses
- installed `--help` exited `0` and documented every supported option and bounds

## Installed Python API with evidence backend

A minimal driver imported the installed module from:

`/tmp/tribunal-revalidation-20260721.FTq39Y/venv/lib/python3.12/site-packages/tribunal.py`

It injected a backend named `e2e-evidence` returning score `88`, concrete finding/evidence lists, and no gaps. Observed result:

```json
{"mode":"critique","views":3,"backend":"e2e-evidence","score":88,"marker":"✅","personas":9}
```

This proves the installed backend contract, result validation, three-view routing, bundled persona discovery, and unanimous gap-free positive-marker condition. It does not prove that the injected natural-language evidence is factually true.

## Expected error path

Installed command with literal documentation placeholder:

`tribunal --mode knowledge --target invalid --notebooklm-url https://notebooklm.google.com/notebook/<id> --json`

Observed:

- exit `2`
- one concise line: `tribunal: error: NotebookLM URL must match https://notebooklm.google.com/notebook/<id>`
- no traceback

## Gates observed before final publication

- `skill-gate`: PASS
- `csv-gate`: PASS; 11 rows, one crown, score spread `53-85`, snapshot `2026-07-20T23:15:54Z`
- strict current OpenSpec validation: PASS
- `report-gate`: PASS; canonical notebook, 11 GitHub repositories, 11 matrix rows, and one Codex Tribunal crown
- all six strict OpenSpec changes named in the report: PASS
- final diff and publication checks are recorded after reconciliation and commit

## Final reconciliation gate pass

After the report, matrix, fallback provenance, and current OpenSpec wording were reconciled, the complete local gate set was run again:

| Gate | Final result |
|---|---|
| Unit discovery | exit `0`; `18` tests in `0.330s`; `OK` |
| Python compilation | exit `0` over runtime, personas init, gates, tests, and both examples |
| Three-mode example | exit `0`; knowledge, criticism, and UI/UX modes retained explicit structural gaps |
| E2E demo | exit `0`; comparison returned six post-hoc `local-rules` views and `⚠️` |
| Skill gate | PASS |
| CSV gate | PASS; 11 rows, one crown, score spread `53-85`, current snapshot timestamp |
| Report gate | PASS; canonical notebook, 11 GitHub repositories, 11 matched matrix rows, one crown |
| Strict OpenSpec | PASS for the current change and every historical change named in the report reproduction block |
| Local Markdown links | PASS; every relative report target existed |
| Patch whitespace | PASS; `git diff --check` returned no finding |
| Cross-artifact audit | PASS; JSON/CSV snapshot and all 11 stars matched, exactly one crown existed, all three accepted verdicts had the full required schema, and all three Grok 402 attempts remained excluded |

The first invocation of the optional cross-artifact helper referenced a nonexistent `html_url` key and exited `1` before comparing values. The corrected read-only invocation used the snapshot's actual `github_url`, `stars`, and `snapshot_utc` fields and passed. This was an audit-wrapper schema mistake, not an artifact or runtime failure.

## OpenSpec requirement reconciliation before publication

| Requirement | Controlling current evidence | State before commit |
|---|---|---|
| Authenticated canonical IDR | NotebookLM ledger and canonical public link | Satisfied |
| Source-grounded cross-query research | Nine conversation UUIDs, explicit processed source IDs, four non-circular controls, citation/source metadata | Satisfied |
| Current OSS-first comparison | GitHub JSON snapshot, OSS ledger, synchronized CSV, report matrix | Satisfied |
| Three isolated adversarial judgments | Frozen packet, three Grok 402 exclusions, three accepted isolated `agy` verdicts, provenance ledger | Satisfied through brief-authorized fallback |
| Evidence-controlled synthesis | Synthesis ledger and explicit primary/executable evidence hierarchy | Satisfied |
| Explicit crown and implementation plan | One gated crown, three verdicts, trade-offs, phased plan, Mermaid flow | Satisfied |
| Executable end-to-end proof | Source, build, archive, clean install, installed console/API, invalid-input observations | Satisfied |
| Repeatable repository gates | Final reconciliation gate table above | Satisfied |
| Immutable public handoff | Publication ledger | Pending until commit, push, remote equality, clean tree, and SHA-pinned retrieval are observed |

This reconciliation closes the local requirements review without pre-claiming the external publication requirement.

## Manual QA verdict

The actual source CLI, built wheel, clean-installed console, installed Python API, and expected failure surface all behaved according to the bounded contract. No runtime defect was reproduced. The generic top-level `personas` package remains a possible future ecosystem collision, not a failure of this claimed standard wheel surface.
