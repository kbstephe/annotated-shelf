#!/usr/bin/env python3
"""Add an episode to the manifest, regenerate feed.xml, commit and push.

Usage:
  python publish.py episodes/004-moral-mazes.mp3 \
      --title "Moral Mazes: The World of Corporate Managers" \
      --description "Jackall's ethnography of managerial ethics..."
"""
import argparse, email.utils, json, subprocess, time
from pathlib import Path
from xml.sax.saxutils import escape

def find_root(start: Path) -> Path:
    p = start.resolve()
    for cand in [p, *p.parents]:
        if (cand / "config.json").exists():
            return cand
    raise SystemExit("config.json not found — run from inside the podcast repo")

def duration_secs(mp3: Path) -> int:
    out = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(mp3)], capture_output=True, text=True)
    return int(float(out.stdout.strip() or 0))

def build_feed(cfg: dict, episodes: list) -> str:
    base = cfg["base_url"].rstrip("/")
    items = []
    for ep in sorted(episodes, key=lambda e: e["pub_ts"], reverse=True):
        url = f"{base}/{ep['file']}"
        d = ep["duration_secs"]
        items.append(f"""    <item>
      <title>{escape(ep['title'])}</title>
      <description>{escape(ep['description'])}</description>
      <enclosure url="{escape(url)}" length="{ep['bytes']}" type="audio/mpeg"/>
      <guid isPermaLink="false">{escape(ep['file'])}</guid>
      <pubDate>{email.utils.formatdate(ep['pub_ts'])}</pubDate>
      <itunes:duration>{d//3600:02d}:{d%3600//60:02d}:{d%60:02d}</itunes:duration>
    </item>""")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <channel>
    <title>{escape(cfg['title'])}</title>
    <link>{escape(base)}</link>
    <description>{escape(cfg.get('description', ''))}</description>
    <language>en-us</language>
    <itunes:author>{escape(cfg.get('author', ''))}</itunes:author>
    <itunes:block>Yes</itunes:block>
{chr(10).join(items)}
  </channel>
</rss>
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mp3")
    ap.add_argument("--title", required=True)
    ap.add_argument("--description", required=True)
    ap.add_argument("--no-push", action="store_true")
    a = ap.parse_args()

    mp3 = Path(a.mp3)
    root = find_root(mp3.parent)
    cfg = json.loads((root / "config.json").read_text())
    manifest_path = root / "episodes.json"
    episodes = json.loads(manifest_path.read_text()) if manifest_path.exists() else []

    rel = str(mp3.resolve().relative_to(root))
    episodes = [e for e in episodes if e["file"] != rel]  # idempotent re-publish
    episodes.append({
        "file": rel,
        "title": a.title,
        "description": a.description,
        "bytes": mp3.stat().st_size,
        "duration_secs": duration_secs(mp3),
        "pub_ts": time.time(),
    })
    manifest_path.write_text(json.dumps(episodes, indent=2))
    (root / "feed.xml").write_text(build_feed(cfg, episodes))
    print(f"feed.xml regenerated with {len(episodes)} episode(s)")

    if not a.no_push:
        subprocess.run(["git", "-C", str(root), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(root), "commit", "-m", f"Episode: {a.title}"], check=True)
        subprocess.run(["git", "-C", str(root), "push"], check=True)
        print(f"pushed — feed: {cfg['base_url'].rstrip('/')}/feed.xml")

if __name__ == "__main__":
    main()
