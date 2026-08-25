#!/usr/bin/env python3
"""Build the Annotated Shelf text site: episodes/*.md -> site/*.html + index + RSS.

Matter mode: we publish readable HTML articles and a full-text RSS feed.
Matter (or any reader) fetches the feed and narrates the text itself, so no
audio is rendered here. Stdlib only, so CI needs no pip installs.
"""

import html
import json
import re
import subprocess
import sys
from email.utils import format_datetime
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EPISODES = ROOT / "episodes"
SITE = ROOT / "site"
CONFIG = ROOT / "config.json"

CSS = """
:root { color-scheme: light dark; }
body { margin: 0 auto; padding: 2.5rem 1.25rem 4rem; max-width: 34rem;
  font: 1.0625rem/1.65 Georgia, 'Iowan Old Style', 'Times New Roman', serif;
  color: #1a1a1a; background: #fdfdfc; }
h1 { font-size: 1.75rem; line-height: 1.25; margin: 0 0 .35rem; }
h2 { font-size: 1.1rem; margin: 2.25rem 0 .75rem; letter-spacing: .01em; }
p { margin: 0 0 1.15rem; }
a { color: #1a1a1a; }
.desc { color: #555; font-style: italic; margin: 0 0 2rem; }
.meta { color: #777; font-size: .85rem; margin: 0 0 2.5rem; }
ul.episodes { list-style: none; padding: 0; }
ul.episodes li { margin: 0 0 1.5rem; }
ul.episodes a { font-size: 1.15rem; text-decoration: none; border-bottom: 1px solid #ccc; }
ul.episodes .desc { font-style: normal; margin: .3rem 0 0; font-size: .95rem; }
footer { margin-top: 4rem; color: #777; font-size: .85rem; }
@media (prefers-color-scheme: dark) {
  body { color: #e8e6e3; background: #17171a; }
  a { color: #e8e6e3; }
  .desc, .meta, footer { color: #a3a3a3; }
}
"""


def load_config() -> dict:
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    if not cfg.get("base_url"):
        sys.exit("config.json is missing base_url")
    cfg["base_url"] = cfg["base_url"].rstrip("/")
    return cfg


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Minimal YAML-frontmatter reader: flat `key: value` pairs only."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    meta = {}
    for line in parts[1].strip().splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip().strip('"').strip("'")
    return meta, parts[2].lstrip("\n")


def first_commit_date(path: Path) -> datetime:
    """Publication date = when the script first landed in git; stable across rebuilds.

    Needs full history (fetch-depth: 0 in CI); falls back to file mtime.
    """
    try:
        out = subprocess.run(
            ["git", "log", "--diff-filter=A", "--follow", "--format=%aI", "--", str(path)],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.strip().splitlines()
        if out:
            return datetime.fromisoformat(out[-1]).astimezone(timezone.utc)
    except Exception:
        pass
    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)


def body_to_html(body: str) -> str:
    """Blocks separated by blank lines; `## Heading` becomes <h2>, else <p>."""
    blocks = [b.strip() for b in re.split(r"\n\s*\n", body) if b.strip()]
    out = []
    for block in blocks:
        if block.startswith("#"):
            heading = block.lstrip("#").strip()
            out.append(f"<h2>{html.escape(heading)}</h2>")
        else:
            text = html.escape(" ".join(line.strip() for line in block.splitlines()))
            out.append(f"<p>{text}</p>")
    return "\n".join(out)


def page(title: str, inner: str, cfg: dict, home: bool = False) -> str:
    back = "" if home else '<footer><a href="index.html">&larr; All episodes</a></footer>'
    return (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"<title>{html.escape(title)}</title>\n"
        f"<link rel=\"alternate\" type=\"application/rss+xml\" title=\"{html.escape(cfg['title'])}\" href=\"feed.xml\">\n"
        f"<style>{CSS}</style>\n</head>\n<body>\n{inner}\n{back}\n</body>\n</html>\n"
    )


def main() -> None:
    cfg = load_config()
    base = f"{cfg['base_url']}/site"
    SITE.mkdir(exist_ok=True)

    episodes = []
    for md in sorted(EPISODES.glob("*.md")):
        meta, body = parse_frontmatter(md.read_text(encoding="utf-8"))
        title = meta.get("title") or md.stem
        desc = meta.get("description", "")
        article = body_to_html(body)
        slug = md.stem
        pub = first_commit_date(md)

        inner = (
            "<article>\n"
            f"<h1>{html.escape(title)}</h1>\n"
            + (f'<p class="desc">{html.escape(desc)}</p>\n' if desc else "")
            + f'<p class="meta">{pub.strftime("%d %B %Y")}</p>\n'
            + article
            + "\n</article>"
        )
        (SITE / f"{slug}.html").write_text(page(title, inner, cfg), encoding="utf-8")
        episodes.append({"slug": slug, "title": title, "description": desc,
                         "html": article, "pub": pub,
                         "url": f"{base}/{slug}.html"})
        print(f"built site/{slug}.html  ({len(article)} chars)")

    # Multi-part series land in one commit, so break date ties by slug (newest number first).
    episodes.sort(key=lambda e: (e["pub"], e["slug"]), reverse=True)

    items = "\n".join(
        "<item>\n"
        f"<title>{html.escape(e['title'])}</title>\n"
        f"<link>{html.escape(e['url'])}</link>\n"
        f"<guid isPermaLink=\"true\">{html.escape(e['url'])}</guid>\n"
        f"<description>{html.escape(e['description'])}</description>\n"
        f"<pubDate>{format_datetime(e['pub'])}</pubDate>\n"
        f"<content:encoded><![CDATA[{e['html']}]]></content:encoded>\n"
        "</item>"
        for e in episodes
    )
    feed = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" '
        'xmlns:atom="http://www.w3.org/2005/Atom">\n<channel>\n'
        f"<title>{html.escape(cfg['title'])}</title>\n"
        f"<link>{html.escape(base)}/index.html</link>\n"
        f"<description>{html.escape(cfg.get('description', ''))}</description>\n"
        "<language>en-us</language>\n"
        f"<atom:link href=\"{html.escape(base)}/feed.xml\" rel=\"self\" type=\"application/rss+xml\"/>\n"
        f"{items}\n</channel>\n</rss>\n"
    )
    (SITE / "feed.xml").write_text(feed, encoding="utf-8")

    listing = "\n".join(
        f'<li><a href="{html.escape(e["slug"])}.html">{html.escape(e["title"])}</a>'
        + (f'<p class="desc">{html.escape(e["description"])}</p>' if e["description"] else "")
        + "</li>"
        for e in episodes
    )
    index_inner = (
        f"<h1>{html.escape(cfg['title'])}</h1>\n"
        f'<p class="desc">{html.escape(cfg.get("description", ""))}</p>\n'
        f'<ul class="episodes">\n{listing}\n</ul>\n'
        '<footer><a href="feed.xml">RSS feed</a></footer>'
    )
    (SITE / "index.html").write_text(page(cfg["title"], index_inner, cfg, home=True), encoding="utf-8")

    print(f"built site/index.html and site/feed.xml  ({len(episodes)} episode(s))")


if __name__ == "__main__":
    main()
