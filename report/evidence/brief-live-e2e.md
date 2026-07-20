# Brief-live source, build, wheel, console, and API E2E

- Recorded UTC: `2026-07-20T21:18:30Z`
- Python: `3.12.3`
- Package: `codex-tribunal 1.0.0`
- Canonical NotebookLM provenance: https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515

No model result or backend result was mocked. Every run used the repository's real `LocalRulesBackend`, which intentionally proves the bounded structural contract and retains semantic/source gaps.

## Source-tree comparison case

The source CLI evaluated the real OSS-first recommendation with `--mode comparison --rounds 2 --hardness hard --json`.

Observed exit `0` and:

- requested/effective rounds `2/2`, hardness `hard`;
- six views, coordinates `R1J1` through `R2J3`;
- six personas: `systems-architect`, `knowledge-analyst`, `andrej-karpathy`, `ux-specialist`, `ux-researcher`, `ux-operator-flow`;
- backend `local-rules`, engine source `builtin-local`;
- two explicit gaps in every view;
- final score `50/100`, marker `⚠️`, therefore no runtime crown;
- the synthetic Karpathy-inspired non-authorship/non-endorsement disclaimer in serialized output.

## Three primary source modes

Separate source CLI processes ran `knowledge`, `critique`, and `ui_ux` with the canonical NotebookLM reference. Each exited `0`, returned three coordinates, backend `local-rules`, final `50/100`, marker `⚠️`, and two evidence gaps per judge. The role-specific panels were:

| Mode | Personas |
|---|---|
| `knowledge` | `knowledge-analyst`, `systems-architect`, `security-auditor` |
| `critique` | `systems-architect`, `security-auditor`, `andrej-karpathy` |
| `ui_ux` | `ux-specialist`, `ux-researcher`, `ux-operator-flow` |

The Markdown critique path was also inspected directly. It contained the target heading, mode, final verdict, target-semantics gap, NotebookLM-not-queried gap, and exact synthetic-persona disclaimer.

## Expected invalid input

Supplying `--notebooklm-url not-a-notebook-url` returned exit `2` with one concise stderr line and no traceback:

```text
tribunal: error: NotebookLM URL must match https://notebooklm.google.com/notebook/<id>
```

## Clean PEP 517 artifacts

`python -m build` produced a clean sdist and wheel in `/tmp/tribunal-brief-e2e.E6msm3/dist`:

| Artifact | SHA-256 |
|---|---|
| `codex_tribunal-1.0.0.tar.gz` | `c40d3f707073deb10faa21c2e3e2fbe6a15470adbb171303b6cad134fc434cc6` |
| `codex_tribunal-1.0.0-py3-none-any.whl` | `7b3f4b8b337691ec37168e5ba48a545116a1107cdcf389426286c501bfd436d4` |

The exact wheel was installed with `--no-deps` into a new virtual environment. The wheel contained `personas/__init__.py` and all nine persona JSON files. Installation reported `Successfully installed codex-tribunal-1.0.0`.

The first orchestration helper found the built files but rejected `rtk find`'s normalized `./wheel` display because it expected an absolute path. The artifacts were already valid and were reused; no second build was hidden. Likewise, the first API driver passed literal `\n` sequences to `python -c` and was excluded after a driver `SyntaxError`. The materially different single-line driver below succeeded.

## Installed console outside the repository

From `/tmp/tribunal-brief-e2e.E6msm3`, the installed `venv/bin/tribunal` comparison command exited `0` and reproduced the source observation exactly: six views, the same six personas, `local-rules`, `builtin-local`, two gaps per view, `50/100`, `⚠️`, and the serialized Karpathy-inspired disclaimer.

## Installed Python API outside the repository

The installed API loaded from:

```text
/tmp/tribunal-brief-e2e.E6msm3/venv/lib/python3.12/site-packages/tribunal.py
```

An explicit three-person critique panel returned three views, `50/100`, `⚠️`, two gaps per view, and `debate.kind=post-hoc-synthesis`. Programmatic assertions observed the synthetic disclaimer in both `to_dict()`/JSON and `to_markdown()`.

## E2E conclusion

The recommendation works through the current source CLI, all primary modes, comparison path, failure boundary, clean PEP 517 artifacts, exact installed console entry point, and installed Python API. The observation supports the thin local orchestration contract only; it does not promote structural `50/100` output into semantic, visual, NotebookLM-retrieval, or provider-independence proof.
