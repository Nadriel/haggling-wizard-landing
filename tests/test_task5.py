"""HTML tests for Task 5: privacy.html content and structure."""

import os
import re
import unittest

ROOT = os.path.join(os.path.dirname(__file__), "..")

with open(os.path.join(ROOT, "privacy.html"), encoding="utf-8") as _f:
    _HTML = _f.read()


class TestPrivacyPageStructure(unittest.TestCase):
    def test_has_doctype(self):
        self.assertTrue(_HTML.strip().lower().startswith("<!doctype html"),
                        "privacy.html must begin with <!DOCTYPE html>")

    def test_has_title(self):
        self.assertIn("<title>", _HTML, "privacy.html must have a <title> element")
        self.assertRegex(_HTML, r'<title>[^<]*[Pp]rivacy[^<]*</title>',
                         "title must mention Privacy")

    def test_has_lang_attribute(self):
        self.assertIn('lang="en"', _HTML, "html element must have lang=en")

    def test_links_back_to_home(self):
        self.assertRegex(_HTML, r'href="/"',
                         "privacy.html must link back to the home page")

    def test_has_footer(self):
        self.assertIn("<footer", _HTML, "privacy.html must include a footer")

    def test_footer_has_copyright(self):
        self.assertRegex(_HTML, r'&copy;\s*2026\s*Haggling Wizard',
                         "footer must include © 2026 Haggling Wizard")

    def test_footer_links_to_privacy(self):
        self.assertIn('href="/privacy.html"', _HTML,
                      "footer must contain a link to /privacy.html")


class TestPrivacyPageContent(unittest.TestCase):
    def test_covers_email_collection(self):
        self.assertRegex(_HTML, r'email',
                         "privacy policy must mention email collection")

    def test_covers_no_cookies(self):
        lower = _HTML.lower()
        self.assertIn("cookie", lower,
                      "privacy policy must address cookies")
        self.assertRegex(lower, r'(no cookies|does not use cookies|not use cookies)',
                         "privacy policy must state that no cookies are used")

    def test_covers_no_tracking(self):
        lower = _HTML.lower()
        # Allow whitespace/newlines between words since HTML is multi-line
        self.assertRegex(lower, r'(no tracking|do\s+not\s+monitor|does\s+not\s+monitor)',
                         "privacy policy must state there is no tracking")

    def test_covers_affiliate_links(self):
        lower = _HTML.lower()
        self.assertIn("affiliate", lower,
                      "privacy policy must disclose affiliate links")

    def test_mentions_marketplaces(self):
        self.assertIn("eBay", _HTML, "privacy policy must mention eBay")
        self.assertIn("AbeBooks", _HTML, "privacy policy must mention AbeBooks")
        self.assertIn("Biblio", _HTML, "privacy policy must mention Biblio")

    def test_mentions_unsubscribe(self):
        self.assertIn("unsubscribe", _HTML,
                      "privacy policy must mention how to opt out of emails")

    def test_no_lorem_ipsum(self):
        self.assertNotIn("lorem ipsum", _HTML.lower(),
                         "privacy.html must not contain placeholder text")


class TestIndexFooterLinksPrivacy(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as f:
            self._index = f.read()

    def test_index_footer_links_to_privacy(self):
        self.assertIn('href="/privacy.html"', self._index,
                      "index.html footer must link to /privacy.html")


if __name__ == "__main__":
    unittest.main()
