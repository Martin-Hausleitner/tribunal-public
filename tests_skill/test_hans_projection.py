import tempfile
from pathlib import Path
import unittest
import test_git_skill as core


class HansProjectionTests(unittest.TestCase):
    def test_hans_projection_keeps_canonical_roots(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            core.m.git(root, "init", "-q")
            state = {"version": 1, "tasks": {}}
            key = core.m.enqueue(state, {
                "source": "ticket:hans-fixture", "target_commit": "0" * 40,
                "criteria": ["correctness"], "reviewers": ["a", "b", "c"],
                "mode": "fixture", "max_rounds": 3})["id"]
            snapshot = {"head": "0" * 40, "state": state}
            core.m.project(snapshot, root, "docs/tribunal/changes")
            self.assertTrue((root / f"docs/tribunal/changes/tribunal-{key}/tribunal-tasks.md").exists())
            self.assertFalse((root / "openspec").exists())
            with self.assertRaises(core.m.Blocked):
                core.m.project(snapshot, root, "../outside")


if __name__ == "__main__":
    unittest.main()
