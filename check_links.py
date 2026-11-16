#!/usr/bin/env python3
"""Checks the generated site (sites/web): every internal link and asset exists, every sitemap URL is a page, and
titles/descriptions stay within 60/160 characters. Links to another site built locally can be checked too:
    python3 check_links.py https://tripsweep.idealy.ch=../website/sites/web
Exits 1 on a broken link."""
import os, re, sys
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "sites", "web")
ORIGIN = "https://" + open(os.path.join(OUT, "CNAME")).read().strip()
SITES = {ORIGIN: OUT, **dict(a.split("=", 1) for a in sys.argv[1:])}

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.title, self.desc, self.noindex, self._in_title = [], "", None, False, False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for k in ("href", "src"):
            if a.get(k):
                self.links.append(a[k])
        if tag == "meta" and a.get("http-equiv", "").lower() == "refresh":
            self.links.append(a["content"].split("url=", 1)[1])
        if tag == "meta" and a.get("name") == "description":
            self.desc = a.get("content", "")
        if tag == "meta" and a.get("name") == "robots" and "noindex" in a.get("content", ""):
            self.noindex = True
        self._in_title = tag == "title"
    def handle_endtag(self, tag):
        self._in_title = False
    def handle_data(self, data):
        if self._in_title:
            self.title += data

def local_file(url):
    """File behind an absolute URL on a site we have locally, or None for an external URL."""
    for origin, d in SITES.items():
        if url.startswith(origin + "/") or url == origin:
            path = urlparse(url).path.lstrip("/")
            path = os.path.join(d, path)
            return os.path.join(path, "index.html") if path.endswith("/") or os.path.isdir(path) else path
    return None

broken, long_meta, pages = [], [], {}
for dirpath, _, files in os.walk(OUT):
    for f in files:
        if not f.endswith(".html"):
            continue
        full = os.path.join(dirpath, f)
        rel = os.path.relpath(full, OUT)
        p = Page()
        p.feed(open(full, encoding="utf-8").read())
        pages[rel] = p
        # 404.html is served at any missing path, so its links are root-absolute.
        base = ORIGIN + "/" + ("" if rel == "404.html" else rel)
        for link in p.links:
            if link.startswith(("mailto:", "#", "data:")):
                continue
            target = local_file(urljoin(base, link).split("#")[0].split("?")[0])
            if target and not os.path.exists(target):
                broken.append(f"{rel}: {link}")
        if not p.noindex and (len(p.title.strip()) > 60 or (p.desc and len(p.desc) > 160)):
            long_meta.append(f"{rel}: title {len(p.title.strip())}, description {len(p.desc or '')}")

sitemap = re.findall(r"<loc>([^<]+)</loc>", open(os.path.join(OUT, "sitemap.xml"), encoding="utf-8").read())
missing = [u for u in sitemap if not os.path.exists(local_file(u))]
noindexed = [u for u in sitemap if pages.get(os.path.relpath(local_file(u), OUT), Page()).noindex]

print(f"{len(pages)} HTML files, {sum(len(p.links) for p in pages.values())} links, {len(sitemap)} sitemap URLs, "
      f"{sum(p.noindex for p in pages.values())} noindex pages")
for title, items in [("Broken links", broken), ("Sitemap URLs without a page", missing),
                     ("Sitemap URLs marked noindex", noindexed), ("Title > 60 or description > 160", long_meta)]:
    print(f"{title}: {len(items)}")
    for i in items:
        print("  " + i)
sys.exit(1 if broken or missing or noindexed else 0)
