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

Pending live commands; populated only after direct execution.
