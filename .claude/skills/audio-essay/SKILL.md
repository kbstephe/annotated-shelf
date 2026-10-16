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

If run outside the repo, ask for the repo path.

## Workflow for "make an episode on X"

### 1. Research
Two parts, both before writing:
- **Facts**: fetch the text to verify (curl plus pdftotext, Europe PMC fullTextXML, raw HTML, or the Read tool on a PDF or scan); search finds sources, it does not supply spoken numbers or quotes. For biomedical papers try the PubMed connector first (convert the DOI to a PMCID, then get_full_text_article; an empty full_text means a scan, so move on). `references/sourcing-routes.md` lists the routes that work from the cloud environment and the hosts that do not; try each host once, never retry, and record changes in the log's Traps line. Never fabricate quotes; constructed examples are flagged in plain speech inside the script. If the work can't be reconstructed from held text plus solid knowledge, don't write the episode.
- **Reception**: for well-covered works, search the major published reviews and best long-form blog treatments — what named critics valued and objected to. Used attributed, per the Grounding section of SCRIPT_STYLE.md; feeds the case-against and verdict chapters.

### 2. Write the script
Read `SCRIPT_STYLE.md` in this skill folder **every time** before writing. Target 5,000–6,500 words (Matter narrates at ≈270 wpm, so ≈19–24 min; 3,100 words came out at 11–12 min and Kevin found that short, 26 Aug 26); go longer when the analysis needs it, never pad to reach the floor. Save as `episodes/NNN-slug.md` (NNN = next number after the highest in `episodes/`, zero-padded), with `title:` and `description:` frontmatter.

The script is plain prose — no markdown emphasis, no bullets, nothing that reads badly aloud. **Matter's TTS reads the page text**, so write chapter headings as plain words that make sense spoken ("Chapter Two: The Ladder"), not as decorative markers. A `## ` heading is fine and becomes an `<h2>`; keep the wording self-contained since the listener hears it as a sentence.

Before drafting, read FRAMES.md; after drafting, run `python3 scripts/frames.py episodes/NNN-slug.md` (see SCRIPT_STYLE.md, Continuity rules).

Show the user the chapter outline and the first ~150 words, then continue without waiting unless they've asked to review scripts first. In an unattended session (the 1AM Routine, or any run where nobody can reply) skip this step entirely: ending the turn to show something is a failed run.

### 2b. Lint (mandatory, unattended runs included)
`python scripts/lint_script.py episodes/NNN-slug.md` must print `0 repeats, 0 tics`
before commit. Fix by rewriting, never by deleting the check.

### 2c. Cold read (one round, unattended runs included)
After lint is clean, make one subagent call (the Agent tool, named Task in some
environments; general-purpose type) with
everything inline and an instruction not to open any file: the rubric below,
the full script, the last three paragraphs of each of the previous two episodes
(065 and 066 put a source list between the closing application and the sign-off),
and the "What he wants from the show" section of listener.md. Rubric, each item
PASS or FLAG with at most two quoted lines and a one-sentence fix:
R1 grading: the narrator telling the listener what matters, self-awarded
superlatives, quote ushers, numbered insight runs. R2 numbers: paragraphs with
more than six quantities; say which two the argument needs. R3 exactness: a
unit- or decimal-level figure the script itself says came from an abstract,
summary or memory. R4 formula: any construction shared with the previous
closers, any refrain. R5 rewind: up to three places a one-pass listener loses
the thread (term before definition, distant pronoun, list longer than three).
R6 chain: the paragraph where the questions stop pulling.
Apply the R1, R3, R4, R5 and R6 fixes you agree with, re-run lint, and record
what you did not apply under Verification in the log entry as "Cold read: ...".
R2 is advisory. One round only; a failed or empty call never blocks the run,
note it in the log and continue.

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

The episode is live when `git show origin/main:site/feed.xml` contains
`<guid isPermaLink="true">base_url/site/NNN-slug.html</guid>` for the new
file's stem. Do not check by title: the previous episode's sign-off already
quotes it inside the feed, and apostrophes are stored as `&#x27;`.

Then tell the user the episode is live and give the article URL
(`base_url/site/NNN-slug.html`). Never hand-edit anything in `site/`.

### 4. Update the queue
Mark the work done in queue.md and note the next one up.

## Guardrails
- Publishing is free: GitHub Actions + Pages on a public repo, and Matter does the narration.
- Don't rewrite an already-published episode's .md unless asked — the article URL is the feed's stable GUID.
- If a work is under copyright, the script is analysis and criticism in Claude's own words — quotes under 15 words, at most one per source.
