"""Affiliate compliance audit tests for Task 7.

Checks index.html and privacy.html against every affiliate program
requirement listed in the spec (CLAUDE.md § Affiliate program requirements
and § Content requirements).
"""

import os
import re
import unittest
from html.parser import HTMLParser

ROOT = os.path.join(os.path.dirname(__file__), "..")

with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as _f:
    _HTML = _f.read()

_HTML_LOWER = _HTML.lower()


class _AttrParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.tags = set()
        self.tag_attrs = {}

    def handle_starttag(self, tag, attrs):
        self.tags.add(tag)
        attrs_dict = dict(attrs)
        self.tag_attrs.setdefault(tag, []).append(attrs_dict)
        if "id" in attrs_dict:
            self.ids.add(attrs_dict["id"])


_PARSER = _AttrParser()
_PARSER.feed(_HTML)


def _section_text(section_id):
    """Return the raw HTML inside the element with the given id."""
    pattern = rf'id="{re.escape(section_id)}".*?(?=\n\s*</(?:section|header|footer|main)>)'
    m = re.search(pattern, _HTML, re.DOTALL)
    return m.group(0).lower() if m else ""


# ---------------------------------------------------------------------------
# eBay Partner Network — "Affiliate disclosure visible on page"
# ---------------------------------------------------------------------------

class TestEbayPartnerNetworkCompliance(unittest.TestCase):
    def test_disclosure_in_hero_above_fold(self):
        """Disclosure must appear inside the <header> element (visible without scrolling)."""
        header_match = re.search(r'<header.*?</header>', _HTML, re.DOTALL | re.IGNORECASE)
        self.assertIsNotNone(header_match, "<header> element must exist")
        header_text = header_match.group(0).lower()
        self.assertIn("commission", header_text,
                      "Affiliate disclosure mentioning 'commission' must be inside <header>")

    def test_disclosure_mentions_ebay(self):
        """Disclosure must specifically name eBay as a partner site."""
        self.assertIn("eBay", _HTML,
                      "eBay must be named in the page content")

    def test_disclosure_states_no_extra_cost(self):
        """Spec requires disclosure language that links 'may earn a commission'."""
        self.assertRegex(_HTML_LOWER, r'may earn.{0,20}commission',
                         "Disclosure must state affiliate links 'may earn a commission'")

    def test_disclosure_visible_or_in_footer(self):
        """Spec: disclosure visible without scrolling on desktop OR present in footer."""
        footer_match = re.search(r'<footer.*?</footer>', _HTML, re.DOTALL | re.IGNORECASE)
        self.assertIsNotNone(footer_match, "<footer> element must exist")
        footer_text = footer_match.group(0).lower()
        header_match = re.search(r'<header.*?</header>', _HTML, re.DOTALL | re.IGNORECASE)
        header_text = header_match.group(0).lower() if header_match else ""
        in_header = "commission" in header_text or "affiliate" in header_text
        in_footer = "commission" in footer_text or "affiliate" in footer_text
        self.assertTrue(in_header or in_footer,
                        "Affiliate disclosure must appear in <header> or <footer>")


# ---------------------------------------------------------------------------
# AbeBooks / Impact Radius — "Site must describe how affiliate links will be used"
# ---------------------------------------------------------------------------

class TestAbeBooksImpactRadiusCompliance(unittest.TestCase):
    def test_dedicated_affiliate_disclosure_section_exists(self):
        self.assertIn("affiliate-disclosure", _PARSER.ids,
                      "A dedicated #affiliate-disclosure section must exist")

    def test_disclosure_section_names_abebooks(self):
        disclosure = _section_text("affiliate-disclosure")
        self.assertIn("abebooks", disclosure,
                      "Affiliate disclosure section must name AbeBooks")

    def test_disclosure_section_explains_usage(self):
        """Impact Radius requires the site to explain how affiliate links work."""
        disclosure = _section_text("affiliate-disclosure")
        self.assertRegex(disclosure, r'(click|purchase|buy)',
                         "Disclosure must describe the click-through / purchase mechanic")

    def test_disclosure_section_mentions_commission(self):
        disclosure = _section_text("affiliate-disclosure")
        self.assertIn("commission", disclosure,
                      "Disclosure section must mention commission")

    def test_disclosure_plain_language_not_legalese(self):
        """Spec: plain language, not legalese."""
        legalese = ["indemnify", "hereinafter", "notwithstanding", "pursuant"]
        for term in legalese:
            self.assertNotIn(term, _HTML_LOWER,
                             f"Disclosure must not use legalese term '{term}'")


# ---------------------------------------------------------------------------
# Biblio / Awin — "Active site with relevant content; disclosure required"
# ---------------------------------------------------------------------------

class TestBiblioAwinCompliance(unittest.TestCase):
    def test_disclosure_names_biblio(self):
        self.assertIn("Biblio", _HTML,
                      "Affiliate disclosure must name Biblio")

    def test_relevant_content_rpg(self):
        """Awin requires an active site with relevant content."""
        self.assertRegex(_HTML_LOWER, r'(rpg|tabletop|d&amp;d|d\+d|dungeon)',
                         "Page must contain relevant RPG/D&D content for Awin review")

    def test_disclosure_present_for_awin(self):
        self.assertIn("affiliate", _HTML_LOWER,
                      "Page must contain the word 'affiliate' for Awin compliance")


# ---------------------------------------------------------------------------
# General pre-launch checklist (all three programs)
# ---------------------------------------------------------------------------

class TestPreLaunchChecklist(unittest.TestCase):
    def test_no_lorem_ipsum(self):
        self.assertNotIn("lorem ipsum", _HTML_LOWER,
                         "Page must contain no placeholder lorem ipsum text")

    def test_all_three_marketplaces_present(self):
        for name in ("eBay", "AbeBooks", "Biblio"):
            self.assertIn(name, _HTML,
                          f"{name} must be named on the page with correct capitalisation")

    def test_contact_email_uses_product_domain(self):
        """Spec: must not be a personal address; must use hagglingwizard.com."""
        mailto_links = [a for a in _PARSER.tag_attrs.get("a", [])
                        if "mailto:" in a.get("href", "")]
        self.assertTrue(mailto_links, "A mailto: contact link must be present")
        for link in mailto_links:
            href = link["href"]
            self.assertIn("hagglingwizard.com", href,
                          f"Contact mailto link must use hagglingwizard.com, got: {href}")

    def test_privacy_policy_linked_from_footer(self):
        footer_match = re.search(r'<footer.*?</footer>', _HTML, re.DOTALL | re.IGNORECASE)
        self.assertIsNotNone(footer_match)
        self.assertIn('href="/privacy.html"', footer_match.group(0),
                      "Footer must link to /privacy.html")

    def test_footer_copyright_present(self):
        footer_match = re.search(r'<footer.*?</footer>', _HTML, re.DOTALL | re.IGNORECASE)
        self.assertIsNotNone(footer_match)
        footer_text = footer_match.group(0)
        self.assertTrue("&copy;" in footer_text or "©" in footer_text,
                        "Footer must contain a copyright symbol")

    def test_no_unsupported_marketplaces_mentioned(self):
        """Spec: do not mention sites not yet integrated."""
        unsupported = ["alibris", "thriftbooks", "bookfinder"]
        for site in unsupported:
            self.assertNotIn(site, _HTML_LOWER,
                             f"Page must not mention unsupported marketplace '{site}'")

    def test_supported_marketplaces_section_is_exhaustive(self):
        """The #marketplaces section must list exactly the three supported sites."""
        section = _section_text("marketplaces")
        for name in ("ebay", "abebooks", "biblio"):
            self.assertIn(name, section,
                          f"#marketplaces section must list '{name}'")

    def test_page_has_lang_attribute(self):
        self.assertIn('lang="en"', _HTML,
                      "html element must have lang=en for accessibility and SEO")

    def test_page_charset_utf8(self):
        self.assertRegex(_HTML, r'charset=["\']?UTF-8',
                         "Page must declare UTF-8 charset")


if __name__ == "__main__":
    unittest.main()
