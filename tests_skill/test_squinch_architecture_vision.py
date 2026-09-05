import importlib.util
from pathlib import Path
import tempfile
import unittest

GEN = Path(__file__).resolve().parents[1] / "skills" / "squinch-architecture-vision" / "scripts" / "generate_mega_squinch.py"
spec = importlib.util.spec_from_file_location("mega", GEN)
mega = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mega)


class SquinchArchitectureVisionTests(unittest.TestCase):
    def render_source(self):
        temp = tempfile.TemporaryDirectory()
        path = Path(temp.name) / "mega.squinch"
        mega.emit(path)
        return temp, path, path.read_text()

    def test_blueprint_scale(self):
        self.assertGreaterEqual(len(mega.SYSTEMS), 18)
        self.assertGreaterEqual(sum(len(s[4]) for s in mega.SYSTEMS), 72)
        self.assertGreaterEqual(sum(sum(len(c[2]) for c in s[4]) for s in mega.SYSTEMS), 216)

    def test_generated_source_is_large_and_has_required_views(self):
        temp, path, text = self.render_source()
        try:
            self.assertGreaterEqual(len(text.splitlines()), 1000)
            for view in ("landscape", "tribunal", "hans", "agent", "oam", "endtoend", "visualqa", "everything"):
                self.assertIn(f"view {view} {{", text)
        finally:
            temp.cleanup()

    def test_native_color_vocabulary_only(self):
        temp, path, text = self.render_source()
        try:
            self.assertNotIn("color: #", text)
            for color in ("blue", "green", "violet", "amber", "pink", "teal", "red", "gray", "accent"):
                self.assertIn(f"color: {color}", text)
        finally:
            temp.cleanup()

    def test_html_contract_is_named_in_skill(self):
        skill = GEN.parents[1] / "SKILL.md"
        text = skill.read_text()
        self.assertIn("tribunal-architektur.html", text)
        self.assertIn("Capture screenshots from the HTML itself", text)
        self.assertIn("Inspect the screenshots with vision", text)

    def test_visual_qa_reference_has_blocking_severity(self):
        ref = GEN.parents[1] / "references" / "visual-qa.md"
        text = ref.read_text()
        self.assertIn("P0/P1 block delivery", text)
        self.assertIn("landscape", text)
        self.assertIn("everything", text)


if __name__ == "__main__":
    unittest.main()
