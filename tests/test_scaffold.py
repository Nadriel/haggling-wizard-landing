"""Structural tests for Task 1: project scaffold."""

import os
import unittest
from html.parser import HTMLParser
import xml.etree.ElementTree as ET

ROOT = os.path.join(os.path.dirname(__file__), "..")


class HTMLStructureChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.has_doctype = False

    def handle_decl(self, decl):
        if decl.lower().startswith("doctype html"):
            self.has_doctype = True

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        self._attrs = dict(attrs)

    def get_attr(self, tag, attr):
        for t, a in self._all_attrs:
            if t == tag:
                return a.get(attr)
        return None


class DetailedHTMLChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = set()
        self.attrs_by_tag = {}
        self.has_doctype = False

    def handle_decl(self, decl):
        if decl.lower().startswith("doctype html"):
            self.has_doctype = True

    def handle_starttag(self, tag, attrs):
        self.tags.add(tag)
        self.attrs_by_tag.setdefault(tag, []).append(dict(attrs))


class TestScaffoldExists(unittest.TestCase):
    def test_index_html_exists(self):
        self.assertTrue(
            os.path.isfile(os.path.join(ROOT, "index.html")),
            "index.html must exist",
        )

    def test_style_css_exists(self):
        self.assertTrue(
            os.path.isfile(os.path.join(ROOT, "style.css")),
            "style.css must exist",
        )

    def test_logo_svg_exists(self):
        self.assertTrue(
            os.path.isfile(os.path.join(ROOT, "assets", "logo.svg")),
            "assets/logo.svg must exist",
        )

    def test_changelog_exists(self):
        self.assertTrue(
            os.path.isfile(os.path.join(ROOT, "CHANGELOG.md")),
            "CHANGELOG.md must exist",
        )

    def test_assets_directory_exists(self):
        self.assertTrue(
            os.path.isdir(os.path.join(ROOT, "assets")),
            "assets/ directory must exist",
        )


class TestIndexHTML(unittest.TestCase):
    def setUp(self):
        path = os.path.join(ROOT, "index.html")
        with open(path, encoding="utf-8") as f:
            self.content = f.read()
        self.parser = DetailedHTMLChecker()
        self.parser.feed(self.content)

    def test_has_doctype(self):
        self.assertTrue(self.parser.has_doctype, "index.html must have <!DOCTYPE html>")

    def test_has_html_tag_with_lang(self):
        self.assertIn("html", self.parser.tags, "index.html must have <html> tag")
        langs = [a.get("lang") for a in self.parser.attrs_by_tag.get("html", [])]
        self.assertTrue(any(langs), "<html> must have a lang attribute")

    def test_has_head_and_body(self):
        self.assertIn("head", self.parser.tags, "index.html must have <head>")
        self.assertIn("body", self.parser.tags, "index.html must have <body>")

    def test_has_charset_meta(self):
        metas = self.parser.attrs_by_tag.get("meta", [])
        charsets = [m.get("charset") for m in metas if m.get("charset")]
        self.assertTrue(charsets, "<head> must include a charset meta tag")

    def test_has_viewport_meta(self):
        metas = self.parser.attrs_by_tag.get("meta", [])
        viewports = [m for m in metas if m.get("name") == "viewport"]
        self.assertTrue(viewports, "<head> must include a viewport meta tag")

    def test_has_title(self):
        self.assertIn("title", self.parser.tags, "index.html must have a <title>")

    def test_links_stylesheet(self):
        links = self.parser.attrs_by_tag.get("link", [])
        stylesheets = [l for l in links if l.get("rel") == "stylesheet"]
        self.assertTrue(stylesheets, "index.html must link style.css via <link rel='stylesheet'>")
        hrefs = [l.get("href") for l in stylesheets]
        self.assertIn("style.css", hrefs, "stylesheet href must be 'style.css'")


class TestLogoSVG(unittest.TestCase):
    def setUp(self):
        path = os.path.join(ROOT, "assets", "logo.svg")
        with open(path, encoding="utf-8") as f:
            self.content = f.read()

    def test_is_valid_xml(self):
        try:
            ET.fromstring(self.content)
        except ET.ParseError as e:
            self.fail(f"assets/logo.svg is not valid XML: {e}")

    def test_is_svg_element(self):
        root = ET.fromstring(self.content)
        self.assertIn("svg", root.tag, "Root element must be <svg>")

    def test_has_xmlns(self):
        root = ET.fromstring(self.content)
        self.assertIn("http://www.w3.org/2000/svg", root.tag + str(root.attrib),
                      "SVG must declare the SVG namespace")


class TestStyleCSS(unittest.TestCase):
    def test_is_readable_file(self):
        path = os.path.join(ROOT, "style.css")
        with open(path, encoding="utf-8") as f:
            content = f.read()
        # Just confirm it's readable; content will grow in later tasks
        self.assertIsInstance(content, str)

    def test_no_external_imports(self):
        path = os.path.join(ROOT, "style.css")
        with open(path, encoding="utf-8") as f:
            content = f.read()
        # Per spec: no external fonts, no frameworks
        self.assertNotIn("fonts.googleapis.com", content,
                         "style.css must not import Google Fonts")
        self.assertNotIn("bootstrap", content.lower(),
                         "style.css must not reference Bootstrap")
        self.assertNotIn("tailwind", content.lower(),
                         "style.css must not reference Tailwind")


if __name__ == "__main__":
    unittest.main()
