---
name: audio-essay
description: Produce an audio-essay episode analyzing a book, essay series, or thinker's body of work — write the script and publish it as a text article plus full-text RSS feed that Matter narrates. Trigger when the user asks for an "episode", "audio essay", "audio review", or names a work from the reading queue (e.g. "do Moral Mazes next", "episode on Normal Accidents"). Also handles feed maintenance ("rebuild the feed", "list episodes").
---

# Audio Essay Pipeline (Matter mode)

Turn a topic into a finished essay in Kevin's Matter queue:
script → git push → GitHub Action builds an HTML article + full-text RSS → Matter
fetches the feed and narrates it aloud with its own TTS.

No audio is rendered here. Matter reads the text, so the script's *words* are the
deliverable; there is no MP3, no episodes.json, and no TTS config.

## Repo layout (this skill lives inside the repo)

```
annotated-shelf/
├── config.json           # feed metadata + base_url
├── episodes/             # NNN-slug.md (the scripts — the only thing you write)
├── scripts/build_site.py # .md → site/*.html + site/index.html + site/feed.xml
├── site/                 # generated — never edit by hand
├── queue.md              # the reading list / planned series
├── .github/workflows/build.yml   # cloud build — push a .md, get an article + feed
└── .claude/skills/audio-essay/   # this skill
```

If run outside the repo, ask for the repo path. If the repo doesn't exist yet, run first-time setup (below).

## Workflow for "make an episode on X"

### 1. Research (only if needed)
For works you know well, skip. For recent works, living authors' current output, or anything post-cutoff, do a quick web search to verify facts. Never fabricate quotes; constructed illustrative dialogue must be labeled as constructed inside the script.

### 2. Write the script
Read `SCRIPT_STYLE.md` in this skill folder **every time** before writing. Target 2,800–3,600 words (≈ 20–26 min spoken). Save as `episodes/NNN-slug.md` (NNN = next number after the highest in `episodes/`, zero-padded), with `title:` and `description:` frontmatter.

The script is plain prose — no markdown emphasis, no bullets, nothing that reads badly aloud. **Matter's TTS reads the page text**, so write chapter headings as plain words that make sense spoken ("Chapter Two: The Ladder"), not as decorative markers. A `## ` heading is fine and becomes an `<h2>`; keep the wording self-contained since the listener hears it as a sentence.

Show the user the chapter outline and the first ~150 words, then continue without waiting unless they've asked to review scripts first (check config.json `review_before_render`).

### 3. Publish — commit the .md, the workflow does the rest

Commit and push just the script:

```
git add episodes/NNN-slug.md queue.md && git commit -m "Episode NNN: Title" && git push
```

The build workflow (`.github/workflows/build.yml`) runs `scripts/build_site.py` on
GitHub's servers, writing `site/NNN-slug.html`, `site/index.html`, and
`site/feed.xml`, and commits them back. Matter picks the episode up on its next
feed poll and narrates it.

To preview locally before pushing (optional, no dependencies):
```
python scripts/build_site.py
```

Then tell the user the episode is live and give the article URL
(`base_url/site/NNN-slug.html`). Never hand-edit anything in `site/`.

### 5. Update the queue
Mark the work done in queue.md and note the next one up.

## First-time setup (only if repo/config missing)
1. `git init`, create config.json (ask for: feed title, author name, GitHub username → base_url `https://USER.github.io/REPO`), `.gitignore` with `.env`, and queue.md seeded from the canon list in SCRIPT_STYLE.md.
2. Ask the user to create a **public** GitHub repo and enable Pages (main branch, root). No API key, no local tooling needed.
3. After the first build, give them the feed URL (`base_url/site/feed.xml`) to add in Matter. The repo must stay public for Pages unless they have Pro; the feed URL is obscure but not secret, so nothing sensitive goes in an episode.

## Guardrails
- Publishing is free: GitHub Actions + Pages on a public repo, and Matter does the narration.
- Don't rewrite an already-published episode's .md unless asked — the article URL is the feed's stable GUID.
- If a work is under copyright, the script is analysis and criticism in Claude's own words — quotes under 15 words, at most one per source.
