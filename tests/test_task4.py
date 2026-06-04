"""CSS tests for Task 4: hero emphasis, step cards, marketplace list, CTA polish."""

import os
import re
import unittest

ROOT = os.path.join(os.path.dirname(__file__), "..")

with open(os.path.join(ROOT, "style.css"), encoding="utf-8") as _f:
    _CSS = _f.read()


class TestHeroHeadline(unittest.TestCase):
    def test_h1_font_weight_bold(self):
        # Extract font-weight from the #hero h1 rule
        match = re.search(r'#hero h1\s*\{([^}]+)\}', _CSS, re.DOTALL)
        self.assertIsNotNone(match, "#hero h1 rule must exist")
        block = match.group(1)
        weights = re.findall(r'font-weight\s*:\s*(\d+)', block)
        self.assertTrue(weights, "#hero h1 must set font-weight to a numeric value")
        self.assertGreaterEqual(int(weights[0]), 700,
                                "#hero h1 font-weight must be >= 700 (bold)")

    def test_h1_has_color(self):
        match = re.search(r'#hero h1\s*\{([^}]+)\}', _CSS, re.DOTALL)
        self.assertIsNotNone(match, "#hero h1 rule must exist")
        self.assertIn("color", match.group(1),
                      "#hero h1 must set an explicit color for prominence")


class TestCTAButton(unittest.TestCase):
    def test_button_has_box_shadow(self):
        self.assertIn("box-shadow", _CSS, "CTA button must have box-shadow for visual prominence")

    def test_button_has_transition(self):
        self.assertIn("transition", _CSS, "CTA button must have transition for smooth hover")


class TestStepCards(unittest.TestCase):
    def test_counter_reset_present(self):
        self.assertIn("counter-reset", _CSS,
                      "#how-it-works ol must use counter-reset for numbered steps")

    def test_counter_increment_present(self):
        self.assertIn("counter-increment", _CSS,
                      "#how-it-works li must use counter-increment")

    def test_step_number_pseudo_element(self):
        self.assertIn("counter(step)", _CSS,
                      "#how-it-works li::before must render the step number via counter(step)")

    def test_li_has_background(self):
        match = re.search(r'#how-it-works li\s*\{([^}]+)\}', _CSS, re.DOTALL)
        self.assertIsNotNone(match, "#how-it-works li rule must exist")
        self.assertIn("background", match.group(1),
                      "#how-it-works li must have a background to appear as a card")

    def test_li_has_border_radius(self):
        match = re.search(r'#how-it-works li\s*\{([^}]+)\}', _CSS, re.DOTALL)
        self.assertIsNotNone(match, "#how-it-works li rule must exist")
        self.assertIn("border-radius", match.group(1),
                      "#how-it-works li must have border-radius for card appearance")


class TestMarketplaceList(unittest.TestCase):
    def test_li_has_border(self):
        match = re.search(r'#marketplaces li\s*\{([^}]+)\}', _CSS, re.DOTALL)
        self.assertIsNotNone(match, "#marketplaces li rule must exist")
        self.assertIn("border", match.group(1),
                      "#marketplaces li must have a border for clean visual separation")


if __name__ == "__main__":
    unittest.main()
