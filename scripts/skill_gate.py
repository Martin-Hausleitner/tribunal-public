from __future__ import annotations

import sys
from pathlib import Path


def fail(message: str) -> int:
    print(f"skill-gate FAIL: {message}")
    return 1


def main() -> int:
    if len(sys.argv) != 2:
        return fail("usage: skill_gate.py <SKILL.md>")
    path = Path(sys.argv[1])
    if not path.is_file():
        return fail(f"missing file: {path}")
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return fail("missing YAML frontmatter boundary")
    frontmatter = text.split("---", 2)[1]
    if "name: tribunal" not in frontmatter or "description:" not in frontmatter:
        return fail("frontmatter must contain tribunal name and description")
    required = {
        "knowledge mode": "`knowledge`",
        "critique mode": "`critique`",
        "ui_ux mode": "`ui_ux`",
        "three judges": "three isolated judge requests",
        "backend isolation": "invoke the configured backend separately",
        "NotebookLM provenance": "canonical notebook identity",
        "post-hoc synthesis": "Synthesize only after all judges finish",
        "no interactive debate overclaim": "does not provide interactive inter-agent debate",
        "no cross-family overclaim": "do not prove cross-family independence",
        "evidence gaps": "evidence gaps",
        "one crown": "exactly one `👑`",
        "direct criticism boundary": "“Uncensored” means",
        "identity safety": "impersonate a real person",
    }
    missing = [label for label, needle in required.items() if needle not in text]
    if missing:
        return fail(f"missing contracts: {', '.join(missing)}")
    if "notebooklm.google.com/notebook/<" in text or "notebooklm.google.com/notebook/example" in text:
        return fail("placeholder NotebookLM URL found")
    print(f"skill-gate PASS: {path} contains all required Tribunal contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
