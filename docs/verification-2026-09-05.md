# Verification receipt — 5 September 2026

## Executed in the current engineering session

Environment: Python 3.13.5, Git, temporary local bare remotes; no external model, NotebookLM or deployed host was called.

`python -m unittest discover -s tests_skill -v`: **27 tests passed** (15.034 s in the final local run). Includes two competing Git writers, stale fences, resume in a fresh process, source/policy drift, missing and forged evidence, symlink/path escapes, human-file preservation, complete conditional resolution and bounded rounds.

`python examples/skill/git_roundtrip.py`: **passed**. It runs a real failing assertion, commits an actual fix, runs a passing assertion, uses separate CLI processes and a local Git remote, retains both CONDITIONAL_GO and GO receipts and projects queue/OpenSpec output. **Judge results are explicit fixtures.** The final receipt has `action_authorized=false`.

## Not claimed

Legacy suite was preserved, not executed in this isolated partial checkout. The CI definition runs it against the complete repository. The official Squinch compiler is not installed in the local execution environment; its source is authored, not locally rendered. Consult the PR's actual CI result rather than inferring success from workflow YAML.

No live scheduler, real independent reviewer identity, deployed multi-device heartbeat, production merge gate or security boundary against arbitrary Git writers has been verified. These remain rollout tasks.

## Diagram

`docs/tribunal.squinch`: 11 systems, 67 leaf nodes, 75 edges and 13 views. Host-dependent actions are labelled. Interactive HTML/SVG are generated only by the real Squinch compiler in CI.
