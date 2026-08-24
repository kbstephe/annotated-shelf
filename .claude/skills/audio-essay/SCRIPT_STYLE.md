# Script style guide — "The Annotated Shelf"

Read this before writing every script. The house style was established by three
episodes on Rao's Gervais Principle and Dan Davies's body of work.

## Register
- Spoken essay, one narrator, addressed to a single smart listener ("you").
- Warm, wry, unhurried. Willing to be funny; never jokey for long.
- First person for judgments: "I'd argue", "my verdict", "here's where I think he's wrong."
- Numbers and acronyms written out for the ear: "nineteen eighty-eight", "H-I-W-T-Y-L spelled out once, then 'heads I win, tails you lose'."
- No formatting that can't be heard: no bullets, no bold, no parentheticals longer than a breath.

## Structure (7–10 chapters, each 250–400 words)
1. Cold open: why this work, and one sentence connecting it to the series so far.
2. Who/what it is: author, provenance, why it matters.
3–4. The two or three keenest insights, each slowed down with a **worked example** —
   a concrete scenario the listener can picture (a promotion, a meeting, a form,
   a grant, a ward round). Constructed examples must be flagged as constructed.
5. The intellectual substructure: what shelf the work stands on; name 2–4
   companion texts and say specifically what each adds.
6. The case against: the work's characteristic failure mode, stated fairly and hard.
7. Synthesis: how it connects to previous episodes in the series (Rao's pyramid,
   Jackall's blame hydraulics, Davies's sinks are the running reference points).
8. Verdict + prescription: who should read it, at what "dose", and one durable
   diagnostic question the listener can carry into work on Monday.
9. Sign off with "Thanks for listening."

## Intellectual standards
- Distinguish three things explicitly when they diverge: what the author claims,
  what the evidence supports, and what the narrator concludes.
- Every big idea gets one memorable test or question the listener can apply.
- Steelman before critique. Cynical frameworks get the "dosage" treatment:
  diagnostic doses good, identity doses toxic.
- Never invent quotes or scenes from real works. Paraphrase; flag reconstructions.

## The series canon (seed for queue.md)
Cynical core: Moral Mazes (Jackall) · Parkinson's Law · The Peter Principle
(Peter & Hull, the actual book) · Pournelle's Iron Law · The Utopia of Rules
and Bullshit Jobs (Graeber).
Systems turn: Seeing Like a State (Scott) · Normal Accidents (Perrow) ·
The Challenger Launch Decision (Vaughan) · The Unaccountability Machine and
Lying for Money (Davies — done).
Micro-mechanics: The Presentation of Self in Everyday Life (Goffman) ·
Games People Play (Berne) · Impro (Johnstone).
Antidotes: Exit, Voice, and Loyalty (Hirschman) · Governing the Commons
(Ostrom) · High Output Management (Grove, as the practitioner's rebuttal).
Coda: Rao's later work — Breaking Smart, "premium mediocre", Be Slightly Evil.

## Continuity rules (critical for unattended runs)
- Before writing, read the one or two most recent scripts in `episodes/` in full.
  The synthesis chapter must engage with what those episodes actually said, not
  with a guess at what they might have said.
- The Rao (Gervais Principle) and Davies episodes predate this feed: they exist
  as style ancestry only. Use their ideas freely as series touchstones (the
  pyramid, accountability sinks), but never call them "last episode" or cite an
  episode number for them — the listener's feed starts at Episode Zero.
- End the final chapter, just before "Thanks for listening," by naming the next
  work: "Next time, X." Pick the first unchecked item in queue.md. The overnight
  pipeline reads this sign-off to choose the next episode, so it is a promise —
  keep it.

## Pre-flight checklist (run before every commit)
1. Word count 2,800–3,600 (`wc -w`). If short, deepen chapters with worked
   examples and steelmanning — never pad with restatement.
2. `python scripts/build_site.py` must run clean (catches frontmatter and
   parse errors). Then discard the local site output — `git checkout site/`
   plus delete any untracked site/*.html — because CI rebuilds it; never
   commit site/ changes yourself.
3. Re-read the draft once against the Register and Structure sections above;
   fix anything that cannot be heard (bullets, digits, orphaned headings).
4. Frontmatter has both `title:` and `description:`; the description is one
   sentence, written for the feed listing.
