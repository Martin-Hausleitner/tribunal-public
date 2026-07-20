# Live-audit end-to-end proof

## Realistic fixture and expected contract

The public CLI receives this release-decision target:

> Decide whether Codex Tribunal should remain the narrow review contract while promptfoo supplies adversarial CI and Microsoft Agent Framework supplies production multi-agent runtime; require dated OSS evidence, explicit category mismatches, and no crown when semantic proof is missing.

The fixture uses `comparison`, two requested rounds, `hard`, the verified canonical NotebookLM URL, and JSON output. It invokes the actual bundled `local-rules` backend through the public CLI; no test double or mocked model response is injected.

Expected machine-checkable behavior:

- exit code `0`;
- `mode=comparison`, `requested_rounds=2`, `rounds=2`, `hardness=hard`;
- six separately constructed judge views and six unique personas with explicit role/backend/engine provenance;
- `debate.kind=post-hoc-synthesis`;
- the canonical NotebookLM reference retained while every view keeps semantic/content proof gaps visible;
- structural score `50`, marker `⚠️`, and no fake comparison crown;
- the Karpathy-inspired view carries its non-impersonation disclaimer in JSON and Markdown;
- the same contract survives PEP 517 installation and the `tribunal` console entry point.

## Observed execution

Executed UTC: `2026-07-20T18:38:11Z`

### Repository public CLI

The exact fixture was executed from the repository root:

```bash
python tribunal.py \
  --mode comparison \
  --rounds 2 \
  --hardness hard \
  --target "Decide whether Codex Tribunal should remain the narrow review contract while promptfoo supplies adversarial CI and Microsoft Agent Framework supplies production multi-agent runtime; require dated OSS evidence, explicit category mismatches, and no crown when semantic proof is missing." \
  --notebooklm-url https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515 \
  --json
```

Observed exit status: `0`.

Machine-checked and manually inspected observations:

- top-level contract: `mode=comparison`, `requested_rounds=2`, `rounds=2`, `hardness=hard`;
- `engine_plan` contains six `local-rules` / `builtin-local` allocations;
- `judge_views` contains six records at coordinates R1J1 through R2J3, with six unique persona slugs and six explicit roles;
- every view records backend, engine, engine source, routed labels, verdict, score, findings, evidence, and two evidence gaps, for `12` explicit gaps total;
- the Karpathy-inspired record includes the exact non-impersonation `persona_disclaimer`;
- `debate.kind=post-hoc-synthesis` and the synthesis retains the two recurring proof gaps;
- `final_score=50`, `crown=⚠️`, and the final verdict contains no false positive marker or runtime comparison crown.

The same installed console-script run was repeated from outside the repository after a clean PEP 517 build:

```bash
python -m venv /tmp/tribunal-live-audit-XXXXXX/venv
/tmp/tribunal-live-audit-XXXXXX/venv/bin/python -m pip install .
cd /tmp/tribunal-live-audit-XXXXXX
/tmp/tribunal-live-audit-XXXXXX/venv/bin/tribunal \
  --mode comparison \
  --rounds 2 \
  --hardness hard \
  --target "Decide whether Codex Tribunal should remain the narrow review contract while promptfoo supplies adversarial CI and Microsoft Agent Framework supplies production multi-agent runtime; require dated OSS evidence, explicit category mismatches, and no crown when semantic proof is missing." \
  --notebooklm-url https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515 \
  --json
```

The wheel built and installed as `codex-tribunal-1.0.0`; the console script exited `0` and reproduced the same contract, six-person panel, explicit gaps, structural score, post-hoc synthesis, and warning marker. A separate installed Markdown run visibly printed the role plus `Persona disclaimer:` under the Karpathy-inspired view.

### Negative and mode-coverage checks

The invalid source-reference command

```bash
python tribunal.py \
  --target "bad notebook reference" \
  --notebooklm-url https://example.com/notebook/id
```

exited `2`, printed the concise `tribunal: error: NotebookLM URL must match ...` message, and printed no traceback. `python examples/phase1_core_modes.py` executed `knowledge`, `critique`, and `ui_ux` successfully; `python examples/e2e_demo.py` also exited `0` through the public comparison surface.

### User-level conclusion

The public interface behaves as documented and is installable without a hidden repository-path dependency. Its warning result is the correct outcome: the run proves the orchestration and serialization contract, not the target's semantic quality, source access, visual UX, or provider-family independence. No mocked model response was supplied, and the built-in structural backend leaves those missing proofs visible instead of manufacturing a green verdict.
