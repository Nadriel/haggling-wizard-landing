"""CSS tests for Task 3: mobile-first responsive layout."""

import os
import re
import unittest

ROOT = os.path.join(os.path.dirname(__file__), "..")

with open(os.path.join(ROOT, "style.css"), encoding="utf-8") as _f:
    _CSS = _f.read()


class TestMobileFirst(unittest.TestCase):
    def test_has_media_query(self):
        self.assertIn("@media", _CSS, "CSS must contain at least one @media rule")

    def test_has_min_width_breakpoint(self):
        self.assertIn("min-width", _CSS,
                      "Mobile-first CSS must use min-width media queries")

    def test_min_width_query_present(self):
        queries = re.findall(r'@media[^{]+', _CSS)
        self.assertTrue(
            any("min-width" in q for q in queries),
            "Must have at least one @media (min-width: ...) block"
        )


class TestFontStack(unittest.TestCase):
    def test_uses_system_font(self):
        system_keywords = [
            "system-ui", "-apple-system", "BlinkMacSystemFont",
            "Segoe UI", "Roboto", "sans-serif", "serif",
        ]
        self.assertTrue(
            any(kw in _CSS for kw in system_keywords),
            "CSS must define a system font stack"
        )

    def test_no_google_fonts(self):
        self.assertNotIn("fonts.googleapis.com", _CSS,
                         "CSS must not import Google Fonts")

    def test_no_bootstrap(self):
        self.assertNotIn("bootstrap", _CSS.lower(),
                         "CSS must not reference Bootstrap")

    def test_no_tailwind(self):
        self.assertNotIn("tailwind", _CSS.lower(),
                         "CSS must not reference Tailwind")


class TestLayoutRules(unittest.TestCase):
    def test_box_sizing_reset(self):
        self.assertIn("box-sizing", _CSS,
                      "CSS must include box-sizing reset")

    def test_line_height_set(self):
        self.assertIn("line-height", _CSS,
                      "CSS must set line-height for readability")

    def test_max_width_present(self):
        self.assertIn("max-width", _CSS,
                      "CSS must use max-width to constrain readable line lengths")

    def test_section_padding(self):
        self.assertIn("padding", _CSS,
                      "CSS must set padding for section spacing")

    def test_hero_styled(self):
        self.assertIn("#hero", _CSS, "CSS must include rules for #hero")

    def test_footer_styled(self):
        self.assertIn("#footer", _CSS, "CSS must include rules for #footer")

    def test_how_it_works_styled(self):
        self.assertIn("#how-it-works", _CSS,
                      "CSS must include rules for #how-it-works")


class TestNoExternalResources(unittest.TestCase):
    def test_no_external_import(self):
        external = re.findall(r'@import\s+["\']?(https?://[^"\';\s]+)', _CSS)
        self.assertFalse(external,
                         f"CSS must not @import external URLs: {external}")

    def test_no_external_url(self):
        urls = re.findall(r'url\(["\']?(https?://[^"\')\s]+)', _CSS)
        self.assertFalse(urls,
                         f"CSS must not load external URLs: {urls}")


if __name__ == "__main__":
    unittest.main()
