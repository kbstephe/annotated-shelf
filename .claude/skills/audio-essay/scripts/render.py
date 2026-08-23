#!/usr/bin/env python3
"""Render an episode script (.md) to MP3 using FREE text-to-speech.

Engines (set "tts_engine" in config.json):
  edge   (default) — Microsoft Edge neural voices via the edge-tts package.
                     Free, no API key, excellent quality. Needs internet.
                     Voices: en-US-AndrewMultilingualNeural (default),
                     en-US-BrianMultilingualNeural, en-GB-RyanNeural, ...
  piper            — fully offline neural TTS (pip install piper-tts).
                     Good quality, runs on CPU. Voice model auto-downloads.
  say              — macOS built-in. Zero install. Quality depends on which
                     Enhanced/Premium voice you download in System Settings →
                     Accessibility → Spoken Content (e.g. "Zoe (Premium)").

Usage: python render.py episodes/004-moral-mazes.md
Requires ffmpeg on PATH. Safe to re-run: finished chunks are cached.
"""
import json, re, shutil, subprocess, sys
from pathlib import Path

MAX_CHARS = 3500

def find_root(start: Path) -> Path:
    p = start.resolve()
    for cand in [p, *p.parents]:
        if (cand / "config.json").exists():
            return cand
    return start.resolve()

def clean(text: str) -> str:
    text = re.sub(r"^---.*?---\s*", "", text, flags=re.S)
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.M)
    text = re.sub(r"[*_`]", "", text)
    return text.strip()

def chunk(text: str):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    chunks, cur = [], ""
    for p in paras:
        if len(cur) + len(p) + 2 <= MAX_CHARS:
            cur = f"{cur}\n\n{p}" if cur else p
        else:
            if cur:
                chunks.append(cur)
            while len(p) > MAX_CHARS:
                cut = p.rfind(". ", 0, MAX_CHARS) + 1 or MAX_CHARS
                chunks.append(p[:cut].strip())
                p = p[cut:].strip()
            cur = p
    if cur:
        chunks.append(cur)
    return chunks

# ---------------- engines ----------------

def tts_edge(text: str, out: Path, cfg: dict):
    voice = cfg.get("voice", "en-US-AndrewMultilingualNeural")
    rate = cfg.get("edge_rate", "-4%")  # slightly slower reads better for essays
    subprocess.run([sys.executable, "-m", "edge_tts", "--voice", voice,
                    "--rate", rate, "--text", text,
                    "--write-media", str(out)], check=True, capture_output=True)

def tts_piper(text: str, out: Path, cfg: dict):
    model = cfg.get("piper_model", "en_US-ryan-high")
    wav = out.with_suffix(".wav")
    subprocess.run(["piper", "--model", model, "--output_file", str(wav)],
                   input=text.encode(), check=True, capture_output=True)
    subprocess.run(["ffmpeg", "-y", "-i", str(wav), "-b:a", "64k", "-ac", "1",
                    str(out)], check=True, capture_output=True)
    wav.unlink()

def tts_say(text: str, out: Path, cfg: dict):
    voice = cfg.get("voice", "Zoe (Premium)")
    aiff = out.with_suffix(".aiff")
    args = ["say", "-o", str(aiff)]
    try:  # verify the requested voice exists; fall back to default if not
        voices = subprocess.run(["say", "-v", "?"], capture_output=True, text=True).stdout
        if voice.split(" (")[0] in voices:
            args += ["-v", voice]
    except Exception:
        pass
    subprocess.run(args, input=text.encode(), check=True)
    subprocess.run(["ffmpeg", "-y", "-i", str(aiff), "-b:a", "64k", "-ac", "1",
                    str(out)], check=True, capture_output=True)
    aiff.unlink()

ENGINES = {"edge": tts_edge, "piper": tts_piper, "say": tts_say}

def check_deps(engine: str):
    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg not found — install it (brew install ffmpeg)")
    if engine == "edge":
        r = subprocess.run([sys.executable, "-m", "edge_tts", "--help"],
                           capture_output=True)
        if r.returncode != 0:
            sys.exit("edge-tts not installed — run: pip install edge-tts")
    if engine == "piper" and not shutil.which("piper"):
        sys.exit("piper not installed — run: pip install piper-tts")
    if engine == "say" and not shutil.which("say"):
        sys.exit("'say' is macOS-only — use engine 'edge' or 'piper'")

def main():
    if len(sys.argv) != 2:
        sys.exit("usage: render.py episodes/NNN-slug.md")
    script = Path(sys.argv[1])
    root = find_root(script.parent)
    cfg = json.loads((root / "config.json").read_text()) if (root / "config.json").exists() else {}
    engine = cfg.get("tts_engine", "edge")
    if engine not in ENGINES:
        sys.exit(f"unknown tts_engine '{engine}' (use edge | piper | say)")
    check_deps(engine)

    chunks = chunk(clean(script.read_text()))
    work = root / ".render" / script.stem
    work.mkdir(parents=True, exist_ok=True)

    parts = []
    for i, c in enumerate(chunks):
        part = work / f"{i:03d}.mp3"
        parts.append(part)
        if part.exists() and part.stat().st_size > 0:
            print(f"chunk {i+1}/{len(chunks)}: cached")
            continue
        print(f"chunk {i+1}/{len(chunks)}: {len(c)} chars → {engine}")
        for attempt in range(3):
            try:
                ENGINES[engine](c, part, cfg)
                break
            except subprocess.CalledProcessError as e:
                if attempt == 2:
                    raise
                print(f"  retry {attempt+1}: {(e.stderr or b'').decode()[:200]}")

    concat = work / "list.txt"
    concat.write_text("".join(f"file '{p.resolve()}'\n" for p in parts))
    out = script.with_suffix(".mp3")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat),
                    "-c:a", "libmp3lame", "-b:a", "64k", "-ac", "1", str(out)],
                   check=True, capture_output=True)
    dur = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(out)], capture_output=True, text=True)
    secs = float(dur.stdout.strip() or 0)
    print(f"\nDONE: {out}  {out.stat().st_size/1e6:.1f} MB  {int(secs//60)}m{int(secs%60):02d}s")

if __name__ == "__main__":
    main()
