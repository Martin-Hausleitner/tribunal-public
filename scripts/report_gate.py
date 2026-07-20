from __future__ import annotations

import re
import sys
from pathlib import Path


NOTEBOOK_URL = re.compile(r"https://notebooklm\.google\.com/notebook/[A-Za-z0-9-]+")
GITHUB_URL = re.compile(r"https://github\.com/[^/\s|)]+/[^/\s|)]+")


def fail(message: str) -> int:
    print(f"report-gate FAIL: {message}")
    return 1


def main() -> int:
    if len(sys.argv) != 2:
        return fail("usage: report_gate.py <report.md>")
    path = Path(sys.argv[1])
    if not path.is_file():
        return fail(f"missing file: {path}")
    text = path.read_text(encoding="utf-8")
    required_headers = [
        "## IDR",
        "## Method",
        "## Source inventory",
        "## NotebookLM cross-query synthesis",
        "## Tribunal verdict 1: Knowledge and correctness",
        "## Tribunal verdict 2: Harsh critique and risks",
        "## Tribunal verdict 3: UX and implementability",
        "## Debate and synthesis",
        "## 100-point rubric",
        "## OSS feature matrix",
        "## Verdict and recommendation",
        "## Implementation plan",
        "## Limitations",
        "## Reproduction",
    ]
    missing = [header for header in required_headers if header not in text]
    if missing:
        return fail(f"missing sections: {', '.join(missing)}")
    idr_lines = text.split("## IDR", 1)[1].split("## ", 1)[0].strip().splitlines()
    if not idr_lines or idr_lines[0].strip() != "IDR: ja":
        return fail("IDR section must begin with `IDR: ja`")
    urls = NOTEBOOK_URL.findall("\n".join(idr_lines))
    if len(set(urls)) != 1:
        return fail("IDR section must contain exactly one canonical NotebookLM URL")
    if len(set(GITHUB_URL.findall(text))) < 6:
        return fail("report must contain at least six distinct GitHub repository URLs")
    if text.count("👑") != 1:
        return fail(f"expected exactly one literal crown, found {text.count('👑')}")
    if "```mermaid" not in text:
        return fail("missing Mermaid diagram")
    if text.count("/100") < 4:
        return fail("missing tribunal and matrix score evidence")
    if re.search(r"\b(?:TODO|TBD|PLACEHOLDER)\b", text, re.IGNORECASE):
        return fail("unfinished placeholder marker found")
    print(
        f"report-gate PASS: canonical notebook={urls[0]}, "
        f"GitHub repos={len(set(GITHUB_URL.findall(text)))}, one crown"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
