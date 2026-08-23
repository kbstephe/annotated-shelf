---
name: audio-essay
description: Produce a podcast episode analyzing a book, essay series, or thinker's body of work — write the script, render it to MP3 via TTS, and publish it to the user's private podcast RSS feed. Trigger when the user asks for an "episode", "audio essay", "audio review", or names a work from the reading queue (e.g. "do Moral Mazes next", "episode on Normal Accidents"). Also handles feed maintenance ("rebuild the feed", "list episodes").
---

# Audio Essay Pipeline

Turn a topic into a finished podcast episode in Kevin's private feed:
script → MP3 (OpenAI TTS) → episode file + updated RSS → git push → appears in his podcast app.

## Repo layout (this skill lives inside the podcast repo)

```
podcast/
├── config.json           # feed metadata + tts_engine ("edge" | "piper" | "say") + voice
├── episodes.json         # episode manifest (source of truth for the feed)
├── episodes/             # NNN-slug.mp3 + NNN-slug.md (script)
├── feed.xml              # generated — never edit by hand
├── queue.md              # the reading list / planned series
├── .github/workflows/render.yml  # cloud rendering — push a .md, get an episode
└── .claude/skills/audio-essay/   # this skill
```

If run outside the repo, ask for the repo path. If the repo doesn't exist yet, run first-time setup (below).

## Workflow for "make an episode on X"

### 1. Research (only if needed)
For works you know well, skip. For recent works, living authors' current output, or anything post-cutoff, do a quick web search to verify facts. Never fabricate quotes; constructed illustrative dialogue must be labeled as constructed inside the script.

### 2. Write the script
Read `SCRIPT_STYLE.md` in this skill folder **every time** before writing. Target 2,800–3,600 words (≈ 20–26 min spoken). Save as `episodes/NNN-slug.md` (NNN = next number from episodes.json, zero-padded). The script is plain prose with `## Chapter N: Title` headings — no markdown emphasis, no bullets, nothing that reads badly aloud.

Show the user the chapter outline and the first ~150 words, then continue without waiting unless they've asked to review scripts first (check config.json `review_before_render`).

### 3. Render audio — pick the mode by where you're running

**Cloud/CI mode (default when running in a remote/sandboxed session, or when
ffmpeg/edge-tts aren't available):** don't render locally. Ensure the script
.md has frontmatter (`title:`, `description:`), then commit and push just the
.md. The repo's GitHub Action (.github/workflows/render.yml) renders the audio
and updates the feed on GitHub's servers. Tell the user the episode will
appear in ~5–10 minutes and skip steps 3–4 below.

**Local mode (laptop with ffmpeg + edge-tts installed):**
```
python .claude/skills/audio-essay/scripts/render.py episodes/NNN-slug.md
```
render.py splits on paragraphs (<4000 chars/chunk), calls the configured free TTS engine (engine + voice from config.json, default edge-tts / en-US-AndrewMultilingualNeural), concatenates with ffmpeg, writes `episodes/NNN-slug.mp3`, and prints duration + size. Uses a free TTS engine (edge-tts by default — no API key); requires ffmpeg. On chunk failure it retries 3× then resumes — safe to re-run, it skips finished chunks.

Announce chapter transitions in the audio by writing the chapter title as its own short paragraph in the script (render.py inserts a beat of silence around single-line paragraphs).

### 4. Publish
```
python .claude/skills/audio-essay/scripts/publish.py episodes/NNN-slug.mp3 \
  --title "Episode title" --description "One-paragraph show-notes summary"
```
publish.py appends to episodes.json, regenerates feed.xml from config.json + episodes.json, then commits and pushes (`git add -A && git commit && git push`). After pushing, tell the user the episode will appear in their podcast app within a few minutes (podcast apps poll the feed) and state the duration.

### 5. Update the queue
Mark the work done in queue.md and note the next one up.

## First-time setup (only if repo/config missing)
1. `git init`, create config.json (ask for: feed title, author name, GitHub username → base_url `https://USER.github.io/REPO`), episodes.json (`[]`), `.gitignore` with `.env`, and queue.md seeded from the canon list in SCRIPT_STYLE.md.
2. Ask the user to: create a **public** GitHub repo, enable Pages (main branch, root), and install ffmpeg plus edge-tts (`brew install ffmpeg && pip install edge-tts`). No API key needed.
3. After first publish, give them the feed URL (`base_url/feed.xml`) and tell them: Overcast → Add URL, or Apple Podcasts → Follow a Show by URL. Note the repo must stay public for Pages unless they have Pro; the feed URL is obscure but not secret.

## Costs & guardrails
- TTS is free (edge-tts / piper / macOS say). If edge-tts breaks (unofficial service), fall back to piper (offline) by setting tts_engine in config.json.
- Never regenerate audio for an already-published episode unless asked (feed enclosures should be stable).
- If a work is under copyright, the script is analysis and criticism in Claude's own words — quotes under 15 words, at most one per source.
