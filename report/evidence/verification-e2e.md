# Verification-pass end-to-end proof

Observed on `2026-07-20` against the working tree derived from starting HEAD `9f1dc36899a530ad4477784b3d12e1fd5c302da1`. Every result below comes from the real source, PEP 517 build, exact installed wheel, or deterministic gate. No backend or model result is mocked. The bundled `local-rules` backend is real deterministic code but is intentionally structural rather than semantic.

## Source CLI and API surfaces

The three primary source CLI modes were executed with the canonical argument surface. Each exited `0`, returned exactly three judge views, used `local-rules` from `builtin-local`, attached routed skills and two explicit evidence gaps to every view, scored `40/100` without a NotebookLM reference, and emitted `⚠️` rather than a positive semantic marker:

```text
python tribunal.py --mode knowledge --rounds 1 --target "Verification knowledge case" --json
python tribunal.py --mode critique --rounds 1 --target "Verification critique case" --json
python tribunal.py --mode ui_ux --rounds 1 --target "Verification UI/UX case" --json
```

The source comparison ran with `--rounds 2 --hardness hard` and the canonical NotebookLM URL. It exited `0` with requested/effective rounds `2/2`, coordinates `R1J1` through `R2J3`, six persona routes, six separate backend calls, six `50/100` structural views, two gaps per view, final `50/100`, and `⚠️`. The valid URL added provenance points but no NotebookLM-access claim.

`examples/phase1_core_modes.py` and `examples/e2e_demo.py` both exited `0`. The realistic comparison example preserved backend-authored multiline/markup values losslessly in JSON while Markdown normalized line breaks and escaped or code-wrapped display content according to the documented renderer contract. Unit coverage independently asserted that `<script>`, `<b>`, and `<img>` tags did not survive as active Markdown HTML and that the original JSON values remained unchanged.

`python -m unittest discover -s tests -v` passed all `18` tests. A complete `py_compile` pass covered `tribunal.py`, `personas/__init__.py`, all three gate scripts, both examples, and `tests/test_tribunal.py` with exit `0`.

## Invalid provenance controls and repaired defect

The hostile judge first exposed that query strings and fragments were accepted despite the canonical URL contract. A later explicit OpenSpec placeholder probe exposed the same boundary for the literal documentation placeholder `<id>`. The smallest repair rejects URL params, query strings, fragments, invalid identifier characters, and the named placeholder identifiers while retaining the tested real UUID and `1234-abcd` forms.

After repair, source CLI probes for these inputs all exited `2`, emitted one concise `tribunal: error: NotebookLM URL ...` message on stderr, emitted no stdout, and contained no traceback:

```text
https://example.com/notebook/id
https://notebooklm.google.com/notebook/<id>
https://notebooklm.google.com/notebook/your-notebook-id
https://notebooklm.google.com/notebook/abc?unexpected=1
https://notebooklm.google.com/notebook/abc#fragment
```

The focused validation test and direct compilation passed after the repair. The installed final wheel also rejected `<id>` with exit `2` and no traceback.

## PEP 517 distribution proof

The final command `python -m build --outdir /tmp/tmp.53y7PYW6LX/final` created an isolated build environment, built the sdist, then built the wheel from that sdist. It exited `0` and produced:

| Artifact | SHA-256 |
|---|---|
| `codex_tribunal-1.0.0-py3-none-any.whl` | `d93a7bf3500bcd38507f90ad8059c8581c07d55971758c359fd964f4e2f2c8be` |
| `codex_tribunal-1.0.0.tar.gz` | `c509061b6bf5ded16dbb219408b80e44b5e966ff87d1e55c5458ce2474d5c88f` |

The final wheel contains exactly the runtime module, MIT license, console/dist metadata, `personas/__init__.py`, and all nine persona JSON documents:

```text
tribunal.py
personas/__init__.py
personas/andrej-karpathy.json
personas/knowledge-analyst.json
personas/security-auditor.json
personas/systems-architect.json
personas/ui-minimalist.json
personas/ui-specialist.json
personas/ux-operator-flow.json
personas/ux-researcher.json
personas/ux-specialist.json
codex_tribunal-1.0.0.dist-info/licenses/LICENSE
codex_tribunal-1.0.0.dist-info/{METADATA,WHEEL,entry_points.txt,top_level.txt,RECORD}
```

The sdist additionally contains `README.md`, `pyproject.toml`, package metadata, and `tests/test_tribunal.py`. Build hashes identify these exact tested timestamped archives; they are not a claim of reproducible byte-for-byte builds across later timestamps.

## Exact-wheel clean installation

The exact wheel above was installed with `--no-deps` into the fresh environment `/tmp/tmp.uznQyIiPEl/final`. `pip show`/installation output identified `codex-tribunal 1.0.0`; no runtime dependency was installed for the project.

From working directory `/tmp`, the installed console ran the two-round comparison with the canonical NotebookLM URL. The JSON observations were:

- mode `comparison`, requested/effective rounds `2/2`, hardness `hard`;
- six distinct persona views and coordinates `R1J1` through `R2J3`;
- backend set `{local-rules}` and engine-source set `{builtin-local}`;
- non-empty routed skills and two evidence gaps on every view;
- unique view score `50`, final score `50`, marker `⚠️`;
- the Karpathy-inspired view carried its full synthetic/unendorsed disclaimer.

The installed Python API was then imported outside the repository. `tribunal.__file__` resolved to `/tmp/tmp.uznQyIiPEl/final/lib/python3.12/site-packages/tribunal.py`. It loaded all nine personas, validated all three Karpathy reference URLs as bare GitHub repository URLs, preserved the full disclaimer in the persona and serialized judge view, and returned three `local-rules` critique views with gap counts `[2, 2, 2]`, final `40/100`, and `⚠️`.

## Decision-relevant conclusion

The real package works through source CLI, examples, PEP 517 archives, exact-wheel installation, installed console, and installed Python API. Error behavior is fail-closed and operator-readable. These observations validate the narrow orchestration/persona/serialization contract. They do not prove target semantics, visual UX/accessibility, NotebookLM retrieval by `local-rules`, provider-family independence, or persistent production quota/trace behavior.
