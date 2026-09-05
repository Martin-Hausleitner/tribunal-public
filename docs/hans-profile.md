# Hans host profile

The parent pins this public repository at `core/skills/repos/tribunal` and owns its entry hook. Parent instructions and data boundaries take precedence; no private source is copied back here.

Hans keeps its existing root layout. When projecting a private ledger, use:

```sh
python3 -I core/skills/repos/tribunal/scripts/tribunal_git.py project \
  --remote <approved-private-ledger> --root . \
  --spec-dir docs/tribunal/changes
```

This emits the existing emoji queue/receipt paths and generated condition supplements under `docs/tribunal/changes`. It does not add a new Hans root or pretend the supplements are standalone OpenSpec changes. The actual proposal/design/spec/tasks remain in the target project's canonical OpenSpec change; queue tickets link that work.

The generic CLI default remains `openspec/changes` for hosts that use that layout. The relative `--spec-dir` must stay inside the projection root. A parent entry wrapper verifies the Gitlink and clean tracked module before invoking discovery. Missing module or GitHub access is blocked; no background scheduler is implied.
