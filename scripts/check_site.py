#!/usr/bin/env python3
"""Dependency-free static validation for SD Advisory Group pages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = ["index.html", "business.html", "about.html", "industries.html",
         "case-studies.html", "insights.html", "consultation.html"]

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.images = []
        self.title = False
        self.viewport = False
        self.main = False
        self.nav = False
        self.headings = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "img" and a.get("src"):
            self.images.append(a["src"])
        if tag == "meta" and a.get("name") == "viewport":
            self.viewport = True
        if tag == "title": self.title = True
        if tag == "main": self.main = True
        if tag == "nav": self.nav = True
        if tag == "h1": self.headings += 1

errors = []
for name in PAGES:
    file = ROOT / name
    if not file.is_file():
        errors.append(f"{name}: missing")
        continue
    source = file.read_text(encoding="utf-8")
    parser = Links()
    parser.feed(source)
    for field in ("title", "viewport", "main", "nav"):
        if not getattr(parser, field):
            errors.append(f"{name}: missing {field}")
    if parser.headings != 1:
        errors.append(f"{name}: expected exactly one h1; found {parser.headings}")
    for url in parser.links + parser.images:
        parts = urlsplit(url)
        if parts.scheme or url.startswith("//") or url.startswith(("mailto:", "tel:")):
            continue
        path = parts.path
        if not path:
            continue
        target = (ROOT / path.lstrip("/")).resolve()
        if not target.is_relative_to(ROOT.resolve()) or not target.is_file():
            errors.append(f"{name}: broken local reference: {url}")
    print(f"CHECKED {name}: {len(parser.links)} links, {len(parser.images)} images")
if errors:
    print("\nFAIL\n" + "\n".join(errors))
    sys.exit(1)
print("\nPASS: all static checks")
