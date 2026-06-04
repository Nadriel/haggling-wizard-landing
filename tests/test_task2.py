"""Structural and content tests for Task 2: HTML sections."""

import os
import re
import unittest
from html.parser import HTMLParser

ROOT = os.path.join(os.path.dirname(__file__), "..")

with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as _f:
    _HTML = _f.read()


class SectionParser(HTMLParser):
    """Collect all element IDs and track which tags appear in the document."""

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


_PARSER = SectionParser()
_PARSER.feed(_HTML)


class TestRequiredSections(unittest.TestCase):
    def test_hero_section_exists(self):
        self.assertIn("hero", _PARSER.ids, "Element with id='hero' must exist")

    def test_how_it_works_section_exists(self):
        self.assertIn(
            "how-it-works", _PARSER.ids,
            "Element with id='how-it-works' must exist"
        )

    def test_marketplaces_section_exists(self):
        self.assertIn(
            "marketplaces", _PARSER.ids,
            "Element with id='marketplaces' must exist"
        )

    def test_affiliate_disclosure_section_exists(self):
        self.assertIn(
            "affiliate-disclosure", _PARSER.ids,
            "Element with id='affiliate-disclosure' must exist"
        )

    def test_about_section_exists(self):
        self.assertIn("about", _PARSER.ids, "Element with id='about' must exist")

    def test_footer_section_exists(self):
        self.assertIn("footer", _PARSER.ids, "Element with id='footer' must exist")


class TestHeroContent(unittest.TestCase):
    def test_product_name_in_h1(self):
        self.assertIn(
            "Haggling Wizard", _HTML,
            "Product name 'Haggling Wizard' must appear in the page"
        )
        self.assertIn("<h1>", _HTML.lower() + "<h1>", "<h1> tag must be present")

    def test_tagline_present(self):
        self.assertIn(
            "Price alerts for out-of-print RPG", _HTML,
            "Tagline must include 'Price alerts for out-of-print RPG'"
        )

    def test_email_input_present(self):
        inputs = _PARSER.tag_attrs.get("input", [])
        email_inputs = [i for i in inputs if i.get("type") == "email"]
        self.assertTrue(email_inputs, "An <input type='email'> must be present")

    def test_email_form_has_label(self):
        self.assertIn(
            "Get notified when we launch", _HTML,
            "Email form label 'Get notified when we launch' must appear"
        )

    def test_mailchimp_placeholder_notice(self):
        self.assertIn(
            "placeholder", _HTML.lower(),
            "A placeholder notice about the Mailchimp embed must be visible"
        )

    def test_no_lorem_ipsum(self):
        self.assertNotIn(
            "lorem ipsum", _HTML.lower(),
            "Page must not contain placeholder lorem ipsum text"
        )


class TestHowItWorksContent(unittest.TestCase):
    def test_ordered_list_present(self):
        self.assertIn("ol", _PARSER.tags, "How-it-works steps must use an <ol>")

    def test_step_add_books(self):
        self.assertIn(
            "Add books to your wishlist", _HTML,
            "Step 1 text must be present"
        )

    def test_step_scan_daily(self):
        self.assertIn(
            "We scan second-hand marketplaces daily", _HTML,
            "Step 2 text must be present"
        )

    def test_step_email_deal(self):
        self.assertIn(
            "You get an email when a deal appears", _HTML,
            "Step 3 text must be present"
        )


class TestMarketplacesContent(unittest.TestCase):
    def test_ebay_listed(self):
        self.assertIn("eBay", _HTML, "eBay must be listed as a supported marketplace")

    def test_abebooks_listed(self):
        self.assertIn(
            "AbeBooks", _HTML,
            "AbeBooks must be listed as a supported marketplace"
        )

    def test_biblio_listed(self):
        self.assertIn(
            "Biblio", _HTML,
            "Biblio must be listed as a supported marketplace"
        )


class TestAffiliateDisclosure(unittest.TestCase):
    def test_commission_mentioned(self):
        self.assertIn(
            "commission", _HTML.lower(),
            "Affiliate disclosure must mention 'commission'"
        )

    def test_disclosure_text_plain_language(self):
        self.assertIn(
            "affiliate", _HTML.lower(),
            "Affiliate disclosure must use the word 'affiliate'"
        )


class TestAboutContact(unittest.TestCase):
    def test_contact_email_link_present(self):
        links = _PARSER.tag_attrs.get("a", [])
        mailto_links = [l for l in links if "mailto:" in l.get("href", "")]
        self.assertTrue(mailto_links, "A mailto: contact link must be present")

    def test_contact_email_domain(self):
        self.assertIn(
            "hagglingwizard.com", _HTML,
            "Contact email must use hagglingwizard.com domain"
        )

    def test_about_describes_project(self):
        self.assertIn(
            "personal", _HTML.lower(),
            "About section must describe the project as a personal project"
        )


class TestFooter(unittest.TestCase):
    def test_privacy_policy_link(self):
        links = _PARSER.tag_attrs.get("a", [])
        privacy_links = [l for l in links if "privacy" in l.get("href", "").lower()]
        self.assertTrue(privacy_links, "Footer must link to a privacy policy page")

    def test_copyright_year(self):
        self.assertIn(
            "2026", _HTML,
            "Footer must include the copyright year"
        )

    def test_copyright_symbol_or_word(self):
        self.assertTrue(
            "&copy;" in _HTML or "©" in _HTML or "copyright" in _HTML.lower(),
            "Footer must include a copyright notice"
        )

    def test_footer_affiliate_disclosure(self):
        self.assertIn(
            "commission", _HTML.lower(),
            "Affiliate disclosure language must appear (footer or body)"
        )


class TestSemanticStructure(unittest.TestCase):
    def test_uses_header_element(self):
        self.assertIn("header", _PARSER.tags, "Page must use <header> element")

    def test_uses_main_element(self):
        self.assertIn("main", _PARSER.tags, "Page must use <main> element")

    def test_uses_footer_element(self):
        self.assertIn("footer", _PARSER.tags, "Page must use <footer> element")

    def test_uses_section_elements(self):
        self.assertIn("section", _PARSER.tags, "Page must use <section> elements")

    def test_has_multiple_headings(self):
        self.assertIn("h2", _PARSER.tags, "Page must have <h2> section headings")

    def test_logo_image_has_alt(self):
        imgs = _PARSER.tag_attrs.get("img", [])
        logo_imgs = [i for i in imgs if "logo" in i.get("src", "").lower()]
        self.assertTrue(logo_imgs, "Logo <img> must be present")
        self.assertTrue(
            all(i.get("alt") for i in logo_imgs),
            "Logo <img> must have a non-empty alt attribute"
        )


if __name__ == "__main__":
    unittest.main()
