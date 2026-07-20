from __future__ import annotations

import csv
import re
import sys
from datetime import datetime
from pathlib import Path


EMOJIS = {"✅", "⚠️", "❌"}
CAPABILITY_COLUMNS = {
    "Knowledge",
    "Critique",
    "UI/UX",
    "Independent Judges",
    "Evidence Provenance",
    "Persona/Skill Extensibility",
    "Observability/Repeatability",
}
RUBRIC_COLUMNS = {
    "Type Fit (25)": 25,
    "Adversarial Depth (20)": 20,
    "Evidence (20)": 20,
    "Extensibility (15)": 15,
    "Repeatability (10)": 10,
    "Integration (10)": 10,
}
BARE_GITHUB_URL = re.compile(r"https://github\.com/[^/\s]+/[^/\s]+")


def fail(message: str) -> int:
    print(f"csv-gate FAIL: {message}")
    return 1


def main() -> int:
    if len(sys.argv) != 2:
        return fail("usage: csv_gate.py <matrix.csv>")
    path = Path(sys.argv[1])
    if not path.exists():
        return fail(f"missing file: {path}")

    rows = list(csv.DictReader(path.open(newline="", encoding="utf-8")))
    if len(rows) < 6:
        return fail("expected at least 6 rows")
    required = {
        "Rank",
        "Tool",
        "GitHub URL",
        "License",
        "Stars",
        "Snapshot UTC",
        "Score",
        "Crown",
        *CAPABILITY_COLUMNS,
        *RUBRIC_COLUMNS,
    }
    missing = required.difference(rows[0].keys())
    if missing:
        return fail(f"missing columns: {sorted(missing)}")

    crowns = 0
    scores: list[int] = []
    ranks: list[int] = []
    tools: set[str] = set()
    snapshots: set[str] = set()
    for index, row in enumerate(rows, start=2):
        if not BARE_GITHUB_URL.fullmatch(row["GitHub URL"]):
            return fail(f"row {index} has non-bare GitHub URL: {row['GitHub URL']}")
        if not row["Tool"].strip() or row["Tool"] in tools:
            return fail(f"row {index} has empty or duplicate tool: {row['Tool']}")
        tools.add(row["Tool"])
        if not row["License"].strip():
            return fail(f"row {index} has empty license")
        if not row["Stars"].isdigit():
            return fail(f"row {index} has non-numeric stars: {row['Stars']}")
        try:
            rank = int(row["Rank"])
            score = int(row["Score"])
        except ValueError:
            return fail(f"row {index} has non-numeric rank or score")
        if not 0 <= score <= 100:
            return fail(f"row {index} score is outside 0-100: {score}")
        component_total = 0
        for column, maximum in RUBRIC_COLUMNS.items():
            try:
                value = int(row[column])
            except ValueError:
                return fail(f"row {index} has non-numeric rubric value in {column}")
            if not 0 <= value <= maximum:
                return fail(f"row {index} value in {column} is outside 0-{maximum}")
            component_total += value
        if component_total != score:
            return fail(f"row {index} rubric sums to {component_total}, not score {score}")
        for column in CAPABILITY_COLUMNS:
            if row[column] not in EMOJIS:
                return fail(f"row {index} capability {column} must be one of {sorted(EMOJIS)}")
        snapshot = row["Snapshot UTC"]
        try:
            datetime.fromisoformat(snapshot.replace("Z", "+00:00"))
        except ValueError:
            return fail(f"row {index} has invalid Snapshot UTC: {snapshot}")
        snapshots.add(snapshot)
        ranks.append(rank)
        scores.append(score)
        if "👑" in row["Crown"]:
            crowns += 1

    if crowns != 1:
        return fail(f"expected exactly one crown, found {crowns}")
    if ranks != list(range(1, len(rows) + 1)):
        return fail(f"ranks must be unique and ordered 1-{len(rows)}")
    if len(set(scores)) != len(scores) or scores != sorted(scores, reverse=True):
        return fail("scores must be unique and ordered descending")
    if len(snapshots) != 1:
        return fail("all rows must share one Snapshot UTC value")

    winner = next(row for row in rows if "👑" in row["Crown"])
    if winner["Rank"] != "1" or int(winner["Score"]) != max(scores):
        return fail("the crown must belong to rank 1 with the highest score")
    print(
        "csv-gate PASS: "
        f"{len(rows)} rows, one crown={winner['Tool']}, "
        f"score spread={min(scores)}-{max(scores)}, snapshot={next(iter(snapshots))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
