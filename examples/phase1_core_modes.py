from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tribunal import HardnessLevel, TribunalOrchestrator, TribunalType


TARGETS = {
    TribunalType.KNOWLEDGE: "Public claim audit: Zustand, Jotai, and Redux are OSS state libraries with different tradeoffs.",
    TribunalType.CRITIQUE: "Synthetic architecture review: a Python CLI tribunal library with deterministic local gates.",
    TribunalType.UI_UX: "Synthetic UI review: a dense operator dashboard for repeat Tribunal runs and evidence gaps.",
}


def main() -> int:
    for mode, target in TARGETS.items():
        tribunal = TribunalOrchestrator(mode, rounds=1, hardness=HardnessLevel.HARD)
        report = tribunal.judge(target)
        print(f"=== {mode.value} ===")
        print(report.to_markdown())
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
