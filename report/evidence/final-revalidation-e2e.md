# Final end-to-end revalidation proof

Completed UTC: `2026-07-20T19:56:36Z`

## Real repository CLI comparison

The actual public CLI and bundled deterministic backend received a realistic release-decision target; no backend result, model response, or verdict object was mocked:

```text
python tribunal.py --mode comparison --rounds 2 --hardness hard \
  --target "Decide whether Codex Tribunal should remain the narrow offline review contract while promptfoo supplies adversarial CI and Microsoft Agent Framework supplies production multi-agent runtime; require dated OSS evidence, explicit category mismatches, and no crown when semantic proof is missing." \
  --notebooklm-url https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515 \
  --json
```

Observed exit: `0`.

```json
{
  "mode": "comparison",
  "requested_rounds": 2,
  "rounds": 2,
  "hardness": "hard",
  "view_count": 6,
  "persona_count": 6,
  "coordinates": ["R1J1", "R1J2", "R1J3", "R2J1", "R2J2", "R2J3"],
  "backends": ["local-rules"],
  "engines": ["local-rules"],
  "engine_sources": ["builtin-local"],
  "gap_count": 12,
  "debate_kind": "post-hoc-synthesis",
  "final_score": 50,
  "crown": "⚠️"
}
```

The serialized views included the full Karpathy-inspired non-authorship/non-endorsement disclaimer. The warning marker is correct: the run proves orchestration, provenance, persona rotation, and serialization while refusing to convert a syntactically linked notebook into semantic proof.

## Core modes and negative path

- `python examples/phase1_core_modes.py` exited `0`; `knowledge`, `critique`, and `ui_ux` each rendered two hard rounds/six views with visible semantic and corpus gaps.
- `python examples/e2e_demo.py` exited `0`; comparison rendered two rounds/six views and `post-hoc-synthesis`.
- `python tribunal.py --target "bad notebook reference" --notebooklm-url https://example.com/notebook/id` exited `2` with exact concise stderr `tribunal: error: NotebookLM URL must match https://notebooklm.google.com/notebook/<id>` and no traceback.

## PEP 517 build and clean installation

A fresh directory `/tmp/tribunal-final-e2e.K4upj4` was created. The project was built through an isolated PEP 517 environment:

```text
python -m build --outdir /tmp/tribunal-final-e2e.K4upj4/dist .
```

Both `codex_tribunal-1.0.0.tar.gz` and `codex_tribunal-1.0.0-py3-none-any.whl` built successfully. Wheel SHA-256:

```text
f6312696838cf001c7b729f1043a05ed1f4c7c1ce10f343d2fb798e3395287b8
```

The build emitted forward-looking setuptools deprecation warnings for the table-form `project.license` and license classifier, with a stated 2027-02-18 deadline; they did not affect build or install success and are not disguised as a clean-warning claim.

A new virtual environment installed that exact wheel successfully as `codex-tribunal-1.0.0`.

## Installed console script outside the repository

From `/tmp/tribunal-final-e2e.K4upj4/run`, the installed `tribunal` entry point executed the same two-round hard comparison. It exited `0` and reproduced:

- `comparison`, requested/effective rounds `2/2`, and `hard`;
- six unique personas and coordinates `R1J1` through `R2J3`;
- backend `local-rules` from `builtin-local`;
- twelve evidence gaps, `post-hoc-synthesis`, score `50`, and `⚠️`;
- the serialized Karpathy-inspired disclaimer.

Running outside the repository prevents an accidental import of the source-tree module from masquerading as installed-package proof.

## Installed Python API outside the repository

The wheel-installed API was imported directly from the same external directory and called through `TribunalOrchestrator(TribunalType.KNOWLEDGE).judge(...)`. Assertions checked mode, three views, JSON parseability, dict/report score equality, warning marker, and the Markdown judge/synthesis sections:

```text
{'mode': 'knowledge', 'views': 3, 'score': 40, 'marker': '⚠️', 'json_markdown_parity': 'PASS'}
```

## E2E verdict

PASS for the declared offline Python library and reusable-skill scope. The source CLI, all primary modes, comparison example, expected failure, PEP 517 artifacts, installed console entry point, and installed Python API were observed working this turn. This proof does not claim semantic target correctness, runtime NotebookLM retrieval, GUI quality, provider-family independence, or durable production controls.
