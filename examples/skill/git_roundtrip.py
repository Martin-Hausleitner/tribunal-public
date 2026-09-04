#!/usr/bin/env python3
"""Actual Git/CLI/failing-test/fix/re-review roundtrip; judge packets are fixtures."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

SCRIPT = Path(__file__).resolve().parents[2] / "scripts/tribunal_git.py"
ENV = __import__("os").environ.copy()
ENV.update(GIT_AUTHOR_NAME="Tribunal Fixture", GIT_AUTHOR_EMAIL="fixture@localhost",
           GIT_COMMITTER_NAME="Tribunal Fixture", GIT_COMMITTER_EMAIL="fixture@localhost")


def run(argv, cwd):
    return subprocess.run(argv, cwd=cwd, env=ENV, text=True, capture_output=True, check=True).stdout.strip()


def demo():
    with tempfile.TemporaryDirectory(prefix="tribunal-roundtrip-") as folder:
        root = Path(folder)
        target = root / "target"
        target.mkdir()
        remote = root / "ledger.git"
        run(["git", "init", "--bare", "-q", str(remote)], root)
        run(["git", "init", "-q"], target)
        def commit(value):
            (target / "app.py").write_text(f"def answer():\n    return {value}\n")
            run(["git", "add", "app.py"], target)
            run(["git", "commit", "-qm", f"fixture answer {value}"], target)
            return run(["git", "rev-parse", "HEAD"], target)
        def cli(command, *args):
            return json.loads(run([sys.executable, str(SCRIPT), command, "--remote", str(remote), *args], target))
        def write(name, value):
            path = root / name
            path.write_text(json.dumps(value))
            return str(path)
        def packet(sha, conditional):
            proof = target / ".proof" / "test.txt"
            proof.parent.mkdir(exist_ok=True)
            p = subprocess.run([sys.executable, "-c", "from app import answer; assert answer() == 42; print('PASS: answer == 42')"],
                               cwd=target, capture_output=True, text=True)
            proof.write_text(f"exit_code={p.returncode}\n{p.stdout}{p.stderr}")
            if conditional:
                assert p.returncode != 0
            else:
                assert p.returncode == 0
            reviews = []
            for who in ("a", "b", "c"):
                reviews.append({"reviewer": who, "session": f"fixture-{sha[:8]}-{who}",
                    "target_commit": sha, "verdict": "CONDITIONAL_GO" if conditional and who == "a" else "GO",
                    "isolated": True, "provenance": "host-asserted",
                    "criteria": {"answer": {"status": "conditional" if conditional and who == "a" else "pass", "evidence": ["test"]}},
                    "conditions": [{"id": "answer", "criterion": "answer", "fix": "Return 42 and rerun the assertion"}] if conditional and who == "a" else [],
                    "resolved_conditions": [] if conditional else ["a.answer"]})
            return {"mode": "fixture", "target_commit": sha, "reviews": reviews,
                    "resolutions": {} if conditional else {"a.answer": ["test"]},
                    "evidence": [{"id": "test", "path": ".proof/test.txt", "target_commit": sha,
                                  "sha256": hashlib.sha256(proof.read_bytes()).hexdigest()}]}
        first = commit(41)
        request = {"source": "ticket:roundtrip", "target_commit": first, "criteria": ["answer"],
                   "reviewers": ["a", "b", "c"], "mode": "fixture", "max_rounds": 3}
        key = cli("enqueue", "--input", write("request.json", request))["result"]["id"]
        fence = cli("claim", "--task", key, "--actor", "fixture-host")["result"]["fence"]
        owner = ["--task", key, "--actor", "fixture-host", "--fence", str(fence)]
        one = cli("review", *owner, "--root", str(target), "--input", write("first.json", packet(first, True)))["result"]
        assert one["decision"] == "CONDITIONAL_GO"
        second = commit(42)
        cli("revise", *owner, "--commit", second)
        two = cli("review", *owner, "--root", str(target), "--input", write("second.json", packet(second, False)))["result"]
        assert two["decision"] == "GO" and not two["action_authorized"]
        resumed = cli("status")["state"]["tasks"][key]
        assert len(resumed["history"]) == 2 and resumed["status"] == "done"
        projection = cli("project", "--root", str(target))
        assert projection["written"]
        print(json.dumps({"mode": "fixture", "git_transport": "real local bare remote", "fresh_cli_processes": True,
                          "initial_test_failed": True, "fix_test_passed": True,
                          "decisions": [one["decision"], two["decision"]], "history_count": len(resumed["history"]),
                          "action_authorized": two["action_authorized"], "live_model_review": False}, indent=2))


if __name__ == "__main__":
    demo()
