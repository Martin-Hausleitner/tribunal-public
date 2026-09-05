# Tribunal repository entry

Read the root [SKILL.md](SKILL.md) for the Git-first skill v2. The old `tribunal.py` and `skill/SKILL.md` remain the legacy API; preserve compatibility and its tests.

Public code only. No private tickets, notebook identifiers, deployment hosts, credentials or raw customer evidence. Changes to policy, reviewer authorization or state-ref permissions require independent review.

Run the deterministic tests and the Git roundtrip from SKILL.md. They do not constitute live independent model reviews. Never let the skill approve its own code merely because fixtures pass.

The architecture source is [docs/tribunal.squinch](docs/tribunal.squinch). Use the official compiler, not an invented rendering format. Current implementation gates and open rollout work are in `openspec/changes/git-first-tribunal-skill/tasks.md`.
