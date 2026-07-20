# Verification direct contradiction controls

Observed against starting HEAD `9f1dc36899a530ad4477784b3d12e1fd5c302da1` on `2026-07-20`. These executable observations outrank NotebookLM's normalized code excerpts.

## Compilation and imports

`python -m py_compile tribunal.py tests/test_tribunal.py personas/__init__.py` exited `0` with no output. Importing `tribunal` then produced:

```text
evaluate_callable True
parse_capacities True
persona_load True
normalize_hardness True
judge True
personas 9
```

This directly rejects the generated claims that either source file has invalid import/string syntax or that `LocalRulesBackend.evaluate`, `EngineManager._parse_capacities`, `PersonaLibrary._load`, `TribunalOrchestrator._normalize_hardness`, or `TribunalOrchestrator.judge` is missing.

## Exact source text

The repository contains separate valid imports and these exact helpers:

```python
def _markdown_text(value: object) -> str:
    normalized = " ".join(str(value).split())
    escaped = html.escape(normalized, quote=False)
    for marker in ("\\", "`", "*", "_", "[", "]"):
        escaped = escaped.replace(marker, f"\\{marker}")
    return escaped


def _markdown_code(value: object) -> str:
    normalized = " ".join(str(value).split())
    longest_run = max((len(match.group(0)) for match in re.finditer(r"`+", normalized)), default=0)
    delimiter = "`" * (longest_run + 1)
    padding = " " if normalized.startswith("`") or normalized.endswith("`") else ""
    return f"{delimiter}{padding}{normalized}{padding}{delimiter}"
```

Exact symbol search located `_parse_capacities` at line 241, `_load` at line 289, `_normalize_hardness` at line 598, and `judge` at line 607.

The test file begins with five separate valid import statements followed by `from pathlib import Path`; it does not contain the normalized single-line form invented by NotebookLM.

## Rendering observation

Calling `_markdown_text` on a string containing an asterisk, brackets, and backticks returned escaped Markdown:

```text
a \* b \[c\] \`d\`
```

Calling `_markdown_code` on a value containing a run of three backticks returned a four-backtick delimiter around the unchanged value:

```text
````x```y````
```

Markdown's deliberate whitespace collapse is documented behavior for the safe display surface; JSON remains lossless. It is not a compile failure.

## Source-normalization conclusion

NotebookLM removed line breaks, underscores, backticks, and escape context from source passages. Its three role answers then confidently reinterpreted those lossy excerpts as fatal source defects. No generated patch is accepted. Full gates and exact-wheel E2E remain required before the bounded ship claim can pass.

## Hostile-judge control and scoped repair

The hostile judge identified one different, reproducible issue: the documented canonical NotebookLM form did not reject query strings or fragments. Before repair, both the direct validator and source CLI accepted `https://notebooklm.google.com/notebook/abc?unexpected=1#fragment` and emitted a 50/100 structural result.

`validate_notebooklm_url` now rejects URL params, query strings, fragments, invalid identifier characters, and documented placeholder identifiers, matching the canonical URL contract and the existing strict GitHub URL boundary. The focused unit test adds `<id>`, `your-notebook-id`, query, and fragment cases. After the change:

- `python -m unittest tests.test_tribunal.TribunalContractTests.test_notebooklm_url_is_strictly_validated -v` passed;
- host, `<id>`, `your-notebook-id`, query, and fragment CLI probes each exited `2` with `tribunal: error: NotebookLM URL must match https://notebooklm.google.com/notebook/<id>` and no traceback;
- the exact rebuilt wheel preserved the same `<id>` failure behavior through the installed console.

Full regression/build/install validation is recorded in `verification-e2e.md`.
