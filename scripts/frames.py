"""Where the shelf's running frames appear. Usage:

  python3 scripts/frames.py                     table: every frame, first and last episode, count
  python3 scripts/frames.py episodes/NNN-x.md   frames the draft touches, then the ten frames
                                                longest unused before it (candidates, not quotas)

Frames and their regex keys live in FRAMES.md, one row each:
  - **Name** | keys: <regex> | <one-line mechanism>
Keys are case-sensitive and should be distinctive (proper nouns, multi-word
terms); a bare surname or common word produces false matches. Counts are
computed from the scripts, so nothing in FRAMES.md needs hand-updating except
new rows for frames an episode plants.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROW = re.compile(r"^- \*\*(?P<name>.+?)\*\* \| keys: (?P<keys>.+?) \| (?P<mech>.+)$")


def load_frames():
    frames = []
    for line in (ROOT / "FRAMES.md").read_text(encoding="utf-8").splitlines():
        m = ROW.match(line.strip())
        if m:
            frames.append((m["name"], re.compile(m["keys"].strip().strip("`")), m["mech"]))
    return frames


def body(path):
    text = Path(path).read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2]
    return text


def episodes(before=None):
    out = []
    for p in sorted((ROOT / "episodes").glob("[0-9][0-9][0-9]-*.md")):
        n = int(p.name[:3])
        if before is not None and n >= before:
            continue
        out.append((n, body(p)))
    return out


def usage(frames, eps):
    table = []
    for name, rx, mech in frames:
        hits = [n for n, text in eps if rx.search(text)]
        table.append((name, hits, mech))
    return table


def main(argv):
    frames = load_frames()
    if not argv:
        for name, hits, _ in usage(frames, episodes()):
            span = f"{hits[0]:03d}-{hits[-1]:03d}" if hits else "unused"
            print(f"{span:9s} {len(hits):3d}  {name}")
        return 0
    draft = Path(argv[0])
    num = int(draft.name[:3]) if draft.name[:3].isdigit() else None
    text = body(draft)
    touched = [(name, mech) for name, rx, mech in frames if rx.search(text)]
    print(f"Frames this draft touches ({len(touched)}):")
    for name, mech in touched:
        print(f"  {name}: {mech}")
    table = usage(frames, episodes(before=num))
    stale = sorted((t for t in table if t[1]), key=lambda t: t[1][-1])[:10]
    print("\nLongest unused before this episode (use only where one genuinely applies):")
    for name, hits, mech in stale:
        print(f"  last {hits[-1]:03d}  {name}: {mech}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
