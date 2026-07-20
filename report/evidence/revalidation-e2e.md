# End-to-end revalidation proof

Completed UTC: `2026-07-20T19:25:03Z`

## Repository CLI

The realistic release-decision target was submitted through the actual public CLI with the bundled deterministic backend. No test double, mocked backend response, or generated model result was injected.

```text
python tribunal.py --mode comparison --rounds 2 --hardness hard \
  --target "Decide whether Codex Tribunal should remain the narrow review contract while promptfoo supplies adversarial CI and Microsoft Agent Framework supplies production multi-agent runtime; require dated OSS evidence, explicit category mismatches, and no crown when semantic proof is missing." \
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
  "engine_sources": ["builtin-local"],
  "gap_count": 12,
  "debate_kind": "post-hoc-synthesis",
  "final_score": 50,
  "crown": "⚠️"
}
```

The Karpathy-inspired record contained its non-authorship/non-endorsement disclaimer. Manual inspection confirmed that the warning marker is correct: this execution proves orchestration and serialization while keeping missing semantic evidence visible.

## Mode coverage and expected failure

- `python examples/phase1_core_modes.py`: exit `0`; knowledge, critique, and UI/UX modes rendered successfully.
- `python examples/e2e_demo.py`: exit `0`; the comparison mode rendered six views and post-hoc synthesis.
- Invalid NotebookLM host: exit `2`; exact concise stderr `tribunal: error: NotebookLM URL must match https://notebooklm.google.com/notebook/<id>`; no traceback.

## Clean PEP 517 installation

A new directory was created under `/tmp`, followed by a new venv and an install from the repository root. Pip built and installed `codex-tribunal-1.0.0` successfully.

```text
Created wheel: codex_tribunal-1.0.0-py3-none-any.whl
Wheel SHA-256: 114eeb4bca36fa0f596f9239a6a2efdb03d1714c237f83f102b17a49066e2262
Successfully installed codex-tribunal-1.0.0
```

The installed `tribunal` console script was then executed from the temporary directory rather than the repository. It exited `0` and reproduced `comparison`, requested/effective rounds `2/2`, six views, six personas, twelve gaps, `post-hoc-synthesis`, score `50`, warning marker `⚠️`, and at least one serialized persona disclaimer.

## Installed Python API

The installed package was imported directly outside the repository and exercised through `TribunalOrchestrator(TribunalType.KNOWLEDGE).judge(...)`. Assertions verified three views, the requested mode, post-hoc synthesis, the warning marker, JSON parseability, equal final scores in dict/JSON, and the Markdown judge-view section.

```text
{'mode': 'knowledge', 'views': 3, 'score': 40, 'marker': '⚠️', 'json_markdown_parity': 'PASS'}
```

## E2E verdict

PASS for the declared offline library and reusable-skill scope. The package works through the repository CLI, installed console script, and installed Python API. The proof does not claim semantic target correctness, NotebookLM content retrieval by the runtime, visual UI quality, or provider-family independence.
