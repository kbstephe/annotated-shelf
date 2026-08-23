#!/usr/bin/env python3
"""CI entrypoint: render every episodes/*.md that lacks an .mp3, then rebuild
episodes.json + feed.xml. Title/description come from the script's YAML
frontmatter:

    ---
    title: "Moral Mazes: The World of Corporate Managers"
    description: "Jackall's ethnography of managerial ethics, and why ..."
    ---

Run by .github/workflows/render.yml on every push. No git operations here —
the workflow commits the results.
"""
import json, re, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3] if (Path(__file__).resolve().parents[3] / "config.json").exists() else Path.cwd()
RENDER = Path(__file__).with_name("render.py")

def frontmatter(md: Path):
    text = md.read_text()
    m = re.match(r"^---\s*\n(.*?)\n---", text, flags=re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"').strip("'")
    title = meta.get("title") or md.stem.split("-", 1)[-1].replace("-", " ").title()
    desc = meta.get("description") or f"An audio essay: {title}."
    return title, desc

def main():
    episodes_dir = ROOT / "episodes"
    if not episodes_dir.exists():
        print("no episodes/ directory; nothing to do")
        return
    manifest_path = ROOT / "episodes.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else []
    known = {e["file"] for e in manifest}
    rendered_any = False

    for md in sorted(episodes_dir.glob("*.md")):
        mp3 = md.with_suffix(".mp3")
        rel = str(mp3.relative_to(ROOT))
        if not mp3.exists():
            print(f"rendering {md.name} ...")
            subprocess.run([sys.executable, str(RENDER), str(md)], check=True)
            rendered_any = True
        if rel not in known:
            title, desc = frontmatter(md)
            dur = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries",
                                  "format=duration", "-of", "csv=p=0", str(mp3)],
                                 capture_output=True, text=True)
            manifest.append({
                "file": rel,
                "title": title,
                "description": desc,
                "bytes": mp3.stat().st_size,
                "duration_secs": int(float(dur.stdout.strip() or 0)),
                "pub_ts": time.time(),
            })
            rendered_any = True
            print(f"  added to manifest: {title}")

    if not rendered_any:
        print("everything already rendered and in the feed")
        return

    manifest_path.write_text(json.dumps(manifest, indent=2))
    sys.path.insert(0, str(RENDER.parent))
    from publish import build_feed  # reuse feed generator
    cfg = json.loads((ROOT / "config.json").read_text())
    (ROOT / "feed.xml").write_text(build_feed(cfg, manifest))
    print(f"feed.xml rebuilt with {len(manifest)} episode(s)")

if __name__ == "__main__":
    main()
