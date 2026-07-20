# Real E2E revalidation

Collection date: `2026-07-20`

Source starting commit: `9f1dc36899a530ad4477784b3d12e1fd5c302da1`

Temporary clean-install root: `/tmp/trib-revalidation-e2e.HcOlVJ` (not committed)

No model result or backend result was mocked. All Tribunal outputs below came from the bundled `local-rules` backend and therefore demonstrate the public orchestration/serialization contract, not semantic target quality.

## Source-tree comparison

The realistic comparison target asked whether Codex Tribunal should stay narrow while composing promptfoo, Microsoft Agent Framework, and Langfuse for mature external capabilities.

Observed:

- command exit: `0`
- mode: `comparison`
- requested/effective rounds: `2/2`
- hardness: `hard`
- isolated views: `6`
- engine plan: six `local-rules` / `builtin-local` entries with no third-party capacity claim
- score: `50/100`
- marker: `⚠️`, not a crown
- every view retained two gaps: no semantic target evaluation and no NotebookLM content query
- canonical NotebookLM URL was serialized as provenance
- the Karpathy-inspired view retained the explicit neither-authored-nor-endorsed disclaimer

## Three primary source modes

Knowledge, critique, and UI/UX each ran through `python tribunal.py ... --json`.

For every mode:

- exit: `0`
- JSON parsed successfully
- three isolated views
- backend: `local-rules`
- score: `40/100`
- marker: `⚠️`
- two explicit evidence gaps per view
- no traceback

This is the expected bounded structural result and is not presented as a semantic or visual pass.

## Invalid NotebookLM boundary

An initial input ending in `/not-a-real-id` was accepted because the published validator intentionally accepts any non-empty final path segment; that is syntactically valid under the documented contract and was not counted as the negative test.

The actual malformed-host case used `https://example.com/notebook/id`:

```text
exit: 2
tribunal: error: NotebookLM URL must match https://notebooklm.google.com/notebook/<id>
```

No traceback appeared.

## PEP 517 build and packaging correction

The first isolated build succeeded but reproduced current setuptools deprecation warnings for a TOML-table license and license classifier. The pass fixed `pyproject.toml` to require `setuptools>=77`, use SPDX `license = "MIT"`, declare `license-files = ["LICENSE"]`, and remove the deprecated classifier.

A fresh second build then:

- exited `0`
- installed build dependency `setuptools>=77`
- produced `codex_tribunal-1.0.0.tar.gz`
- produced `codex_tribunal-1.0.0-py3-none-any.whl`
- emitted no deprecation warning
- serialized `License-Expression: MIT` and `License-File: LICENSE`
- included `tribunal.py`, console metadata, the MIT license, `personas/__init__.py`, and all nine persona JSON files

SHA-256:

- wheel: `082b979c0806d338c15f44d6d4337e01849181e19b411fdb7947ebbb755deae4`
- sdist: `b01773ede8b01d94200941636c2b11cf59320ddd0fd841e660cdec63f63e0e82`

The generic top-level `personas` package remains a documented namespace-collision risk; renaming it would be a breaking packaging migration and is not silently performed by this acceptance pass.

## Installed console entry point

The exact fresh wheel was installed with `--no-deps` into an isolated Python 3.12 virtual environment. From an outside directory, the installed `tribunal` entry point ran the two-round hard comparison:

- exit: `0`
- parsed JSON
- six isolated views
- `local-rules` provenance
- `50/100`, `⚠️`
- two gaps per view
- persona disclaimer present

## Installed Python API

The first test-driver assertion incorrectly looked for `backend_name`; the stable serialized field is `backend`. That driver traceback was not a product failure and is retained here rather than hidden.

The corrected outside-tree installed API test exited `0` and observed:

```json
{
  "module": "/tmp/trib-revalidation-e2e.HcOlVJ/venv/lib/python3.12/site-packages/tribunal.py",
  "mode": "critique",
  "score": 40,
  "marker": "⚠️",
  "views": 3,
  "backend": "local-rules",
  "gaps": [2, 2, 2],
  "disclaimer": "This synthetic review persona is neither authored nor endorsed by Andrej Karpathy and must not impersonate him or attribute generated conclusions to him.",
  "markdown_has_disclaimer": true
}
```

This proves the import came from the isolated site-packages directory, JSON and Markdown serialization work, gaps remain explicit, and the identity disclaimer survives both surfaces.

## Final deterministic gates

- `python -m unittest discover -s tests -v`: 18 tests passed
- `python -m py_compile ...`: exit 0
- skill gate: pass
- CSV gate: pass, 11 rows, one crown
- report gate: pass, canonical notebook, 11 GitHub repositories, synchronized matrix
- JSON parse: exit 0
- strict current OpenSpec validation: pass
- `examples/phase1_core_modes.py`: exit 0
- `examples/e2e_demo.py`: exit 0

An additional `pytest tests/` probe returned exit 2 with `No tests collected`; the suite is implemented and named for `unittest.TestCase`, and the authoritative unittest runner executed all 18 tests successfully. No test was deleted or weakened to alter that result.
