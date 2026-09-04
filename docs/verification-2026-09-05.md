# Verification receipt — 5 September 2026

## Executed in the current engineering session

Environment: Python 3.13.5, Git, temporary local bare remotes; no external model, NotebookLM or deployed host was called.

`python -m unittest discover -s tests_skill -v`: **28 tests passed** (including the added Hans-layout test). Includes two competing Git writers, stale fences, resume in a fresh process, source/policy drift, missing and forged evidence, symlink/path escapes, human-file preservation, complete conditional resolution and bounded rounds.

`python examples/skill/git_roundtrip.py`: **passed**. It runs a real failing assertion, commits an actual fix, runs a passing assertion, uses separate CLI processes and a local Git remote, retains both CONDITIONAL_GO and GO receipts and projects queue/OpenSpec output. **Judge results are explicit fixtures.** The final receipt has `action_authorized=false`.

## Not claimed

The complete GitHub CI run 33926805973 on commit 56dc86be38d9aa82d7a44c44d91399282453718b passed the 18 legacy tests, 27 then-current skill tests, fresh-process roundtrip and official Squinch 0.2.0 HTML/SVG rendering. Its downloaded artifact SHA-256 is 9b653573c31f09e40653049352595baf14c278c737d2b558b1ca97c45c0ccfc8. The final host-layout extension adds one test; consult the latest PR run for its remote result.

The first CI roundtrip failed because an equal-length source edit within one timestamp tick reused cached Python bytecode. This was reproduced locally and fixed by disabling bytecode writes in the fresh fixture subprocesses. No failure was hidden or converted to a pass.

No live scheduler, real independent reviewer identity, deployed multi-device heartbeat, production merge gate or security boundary against arbitrary Git writers has been verified. These remain rollout tasks.

## Diagram

`docs/tribunal.squinch`: 11 systems, 67 leaf nodes, 75 edges and 13 views. Host-dependent actions are labelled. Interactive HTML/SVG are generated only by the real Squinch compiler in CI.
