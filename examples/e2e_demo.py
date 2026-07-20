from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tribunal import TribunalOrchestrator, TribunalType


def main() -> int:
    tribunal = TribunalOrchestrator(
        TribunalType.COMPARISON,
        rounds=2,
    )
    report = tribunal.judge("Tribunal OSS library comparison and anti-fake gate")
    print(report.to_markdown())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
