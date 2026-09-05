import copy
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import threading
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "tribunal_git.py"
spec = importlib.util.spec_from_file_location("tribunal_git", SCRIPT)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class GitSkillTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.remote = self.root / "ledger.git"
        self.target = self.root / "target"
        self.target.mkdir()
        m.git(self.root, "init", "-q", "--bare", str(self.remote))
        m.git(self.target, "init", "-q")
        (self.target / "code.txt").write_text("original\n")
        m.git(self.target, "add", "code.txt")
        m.git(self.target, "commit", "-qm", "initial")
        self.sha = m.git(self.target, "rev-parse", "HEAD").stdout.strip()
        (self.target / "proof.txt").write_text("actual local test observation\n")
        self.request = {"source": "ticket:example-1", "target_commit": self.sha,
                        "criteria": ["correctness"], "reviewers": ["a", "b", "c"],
                        "mode": "fixture", "max_rounds": 3}
        self.ledger = m.Ledger(str(self.remote))
        self.key = self.ledger.transact(lambda s: m.enqueue(s, self.request))["result"]["id"]

    def tearDown(self):
        self.temp.cleanup()

    def state(self):
        return self.ledger.transact()["state"]

    def local_task(self):
        return self.state()["tasks"][self.key]

    def packet(self, commit=None):
        sha = commit or self.sha
        return {"target_commit": sha, "mode": "fixture", "resolutions": {},
            "evidence": [{"id": "e1", "path": "proof.txt", "target_commit": sha,
                          "sha256": hashlib.sha256((self.target / "proof.txt").read_bytes()).hexdigest()}],
            "reviews": [{"reviewer": x, "session": f"isolated-{x}", "target_commit": sha,
                         "verdict": "GO", "isolated": True, "provenance": "host-asserted",
                         "criteria": {"correctness": {"status": "pass", "evidence": ["e1"]}},
                         "conditions": [], "resolved_conditions": []} for x in ("a", "b", "c")]}

    def test_idempotent_enqueue_no_extra_commit(self):
        head = self.ledger.transact()["head"]
        result = self.ledger.transact(lambda s: m.enqueue(s, self.request))
        self.assertFalse(result["result"]["created"])
        self.assertEqual(head, result["head"])

    def test_claim_competition_and_fencing(self):
        t = self.local_task()
        one = m.claim(t, "worker-a", 10, 30)
        with self.assertRaises(m.Blocked):
            m.claim(t, "worker-b", 11, 30)
        two = m.claim(t, "worker-b", 41, 30)
        self.assertGreater(two["fence"], one["fence"])
        with self.assertRaises(m.Blocked):
            m.owned(t, "worker-a", one["fence"], 42)
        m.owned(t, "worker-b", two["fence"], 42)

    def test_remote_compare_and_swap_real_git(self):
        barrier = threading.Barrier(2)
        def runner(name):
            def change(s):
                value = m.claim(s["tasks"][self.key], name, 100, 30)
                barrier.wait(timeout=10)
                return value
            try:
                self.ledger.transact(change)
                return "won"
            except m.Blocked:
                return "lost"
        with ThreadPoolExecutor(2) as pool:
            results = list(pool.map(runner, ["worker-a", "worker-b"]))
        self.assertCountEqual(results, ["won", "lost"])
        self.assertEqual(self.local_task()["fence"], 1)

    def test_git_history_survives_new_process(self):
        p = subprocess.run(["python3", str(SCRIPT), "status", "--remote", str(self.remote)],
                           capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout)
        self.assertIn(self.key, json.loads(p.stdout)["state"]["tasks"])

    def test_offline_is_blocked_not_empty(self):
        with self.assertRaises(m.Blocked):
            m.Ledger(str(self.root / "missing.git")).transact()

    def test_conditional_fix_revision_re_review(self):
        t, packet = self.local_task(), self.packet()
        packet["reviews"][0]["verdict"] = "CONDITIONAL_GO"
        packet["reviews"][0]["conditions"] = [{"id": "fix", "criterion": "correctness", "fix": "Add missing behavior"}]
        result = m.review(t, packet, self.target)
        self.assertEqual(result["decision"], "CONDITIONAL_GO")
        self.assertFalse(result["action_authorized"])
        (self.target / "code.txt").write_text("fixed\n")
        m.git(self.target, "add", "code.txt")
        m.git(self.target, "commit", "-qm", "fix")
        sha = m.git(self.target, "rev-parse", "HEAD").stdout.strip()
        m.revise(t, sha)
        with self.assertRaises(m.Blocked):
            m.review(t, packet, self.target)
        fixed = self.packet(sha)
        fixed["resolutions"] = {"a.fix": ["e1"]}
        for r in fixed["reviews"]:
            r["resolved_conditions"] = ["a.fix"]
        final = m.review(t, fixed, self.target)
        self.assertEqual(final["decision"], "GO")
        self.assertEqual(len(t["history"]), 2)
        self.assertFalse(final["action_authorized"])
        self.assertEqual(final["mode"], "fixture")

    def test_condition_cannot_be_silently_dropped(self):
        t, p = self.local_task(), self.packet()
        p["reviews"][0].update(verdict="CONDITIONAL_GO", conditions=[{"id": "fix", "criterion": "correctness", "fix": "Fix"}])
        m.review(t, p, self.target)
        self.assertEqual(m.review(t, self.packet(), self.target)["decision"], "CONDITIONAL_GO")

    def test_unanimous_resolution_required(self):
        t, p = self.local_task(), self.packet()
        p["reviews"][0].update(verdict="CONDITIONAL_GO", conditions=[{"id": "fix", "criterion": "correctness", "fix": "Fix"}])
        m.review(t, p, self.target)
        p = self.packet()
        p["resolutions"] = {"a.fix": ["e1"]}
        p["reviews"][0]["resolved_conditions"] = ["a.fix"]
        self.assertEqual(m.review(t, p, self.target)["decision"], "CONDITIONAL_GO")

    def test_hard_veto_not_averaged_away(self):
        p = self.packet()
        p["reviews"][0]["verdict"] = "NO_GO"
        self.assertEqual(m.review(self.local_task(), p, self.target)["decision"], "NO_GO")

    def test_missing_evidence_not_go(self):
        p = self.packet()
        p["evidence"] = []
        for r in p["reviews"]:
            r["criteria"]["correctness"]["evidence"] = []
        self.assertEqual(m.review(self.local_task(), p, self.target)["decision"], "NEEDS_EVIDENCE")

    def test_missing_criterion_not_go(self):
        p = self.packet()
        p["reviews"][0]["criteria"] = {}
        self.assertEqual(m.review(self.local_task(), p, self.target)["decision"], "NEEDS_EVIDENCE")

    def test_forged_hash_rejected(self):
        p = self.packet()
        p["evidence"][0]["sha256"] = "0" * 64
        with self.assertRaises(m.Blocked):
            m.review(self.local_task(), p, self.target)

    def test_symlink_outside_root_rejected(self):
        p = self.packet()
        (self.root / "outside.txt").write_text("outside")
        (self.target / "escape").symlink_to(self.root / "outside.txt")
        p["evidence"][0]["path"] = "escape"
        with self.assertRaises(m.Blocked):
            m.review(self.local_task(), p, self.target)

    def test_path_traversal_rejected(self):
        p = self.packet()
        p["evidence"][0]["path"] = "../outside.txt"
        with self.assertRaises(m.Blocked):
            m.review(self.local_task(), p, self.target)

    def test_shared_session_rejected(self):
        p = self.packet()
        p["reviews"][1]["session"] = p["reviews"][0]["session"]
        with self.assertRaises(m.Blocked):
            m.review(self.local_task(), p, self.target)

    def test_fixture_not_live(self):
        p = self.packet()
        p["mode"] = "live"
        with self.assertRaises(m.Blocked):
            m.review(self.local_task(), p, self.target)

    def test_round_budget(self):
        t = self.local_task()
        t["round"] = 3
        with self.assertRaises(m.Blocked):
            m.review(t, self.packet(), self.target)

    def test_dirty_target_rejected(self):
        (self.target / "code.txt").write_text("uncommitted")
        with self.assertRaises(m.Blocked):
            m.review(self.local_task(), self.packet(), self.target)

    def test_projection_and_heartbeat(self):
        snap = self.ledger.transact()
        m.project(snap, self.target)
        items = m.discover(self.target, [])
        self.assertEqual(len(items["local"]), 1)
        snap["state"]["tasks"][self.key]["status"] = "active"
        m.project(snap, self.target)
        self.assertEqual(len(m.discover(self.target, [])["local"]), 1)
        self.assertTrue((self.target / f"openspec/changes/tribunal-{self.key}/tribunal-tasks.md").exists())

    def test_human_projection_not_overwritten(self):
        path = self.target / f"🎫-queue/pending/tribunal-{self.key}.md"
        path.parent.mkdir(parents=True)
        path.write_text("human content")
        with self.assertRaises(m.Blocked):
            m.project(self.ledger.transact(), self.target)
        self.assertEqual(path.read_text(), "human content")

    def test_changed_source_target_not_old_go(self):
        request = {**self.request, "target_commit": "f" * 40}
        with self.assertRaises(m.Blocked):
            self.ledger.transact(lambda state: m.enqueue(state, request))

    def test_changed_policy_requires_new_request(self):
        request = {**self.request, "criteria": ["different"]}
        with self.assertRaises(m.Blocked):
            self.ledger.transact(lambda state: m.enqueue(state, request))

    def test_conditional_requires_actionable_conditions(self):
        p = self.packet()
        p["reviews"][0]["verdict"] = "CONDITIONAL_GO"
        with self.assertRaises(m.Blocked):
            m.review(self.local_task(), p, self.target)

    def test_malformed_condition_fails_closed(self):
        p = self.packet()
        p["reviews"][0]["conditions"] = ["not an object"]
        with self.assertRaises(m.Blocked):
            m.review(self.local_task(), p, self.target)

    def test_projection_ancestor_symlink_rejected(self):
        outside = self.root / "outside"
        outside.mkdir()
        (self.target / "🎫-queue").symlink_to(outside, target_is_directory=True)
        with self.assertRaises(m.Blocked):
            m.project(self.ledger.transact(), self.target)
        self.assertEqual(list(outside.iterdir()), [])

    def test_receipt_digest_matches_retained_reviews(self):
        receipt = m.review(self.local_task(), self.packet(), self.target)
        expected = receipt.pop("sha256")
        self.assertEqual(expected, m.digest(receipt))
        self.assertEqual(len(receipt["reviews"]), 3)

    def test_cli_invalid_input_blocked(self):
        p = subprocess.run(["python3", str(SCRIPT), "claim"], capture_output=True, text=True)
        self.assertEqual(p.returncode, 2)
        self.assertFalse(json.loads(p.stdout)["action_authorized"])


if __name__ == "__main__":
    unittest.main()
