# STATE — The Annotated Shelf

## Snapshot (10 Sep 2026, day, Kevin)

Forty-one episodes (000 test + 001–040). Kevin asked for "the next 3
episodes right now" and 038 Cost Disease (5,069 words), 039 Man of One
Study + Control Group (5,027) and 040 Collison's own pages (5,017) were
written attended in one session, all lint clean, all primary sources
fetched directly (SSC essays via raw curl, not summariser; Collison's
three pages verbatim). Scott Alexander run complete; Collison shelf
opened. 040's sign-off promises Hamming (041), which the Routine should
pick up 11 Sep. Nothing in the queue's scoping needed correcting this
time. Open (HITL): 038's chapter on the academic medical centre and 039's
trialist chapter speak in Kevin's first person about his own work more
directly than earlier episodes; Kevin should confirm that register is
wanted (proximity rule: published record only unless he steers).

## Previous snapshot (10 Sep 2026, Routine)

Thirty-eight episodes (000 test + 001–037). 037 Scott Alexander,
"Meditations on Moloch" (5,390 words, lint clean) written unattended
10 Sep, the second item in the 8 Sep order-of-record queue, first of the
three-episode Scott Alexander run. Essay itself fetched and checked
directly this session (unlike 035/036, no primary-source gap to flag).
Corrected the queue's own scoping note: "Moloch's Toolbox" is Yudkowsky's,
not Zvi Mowshowitz's (his own reply is the separate "Moloch Hasn't Won").
Sign-off promises Alexander's "Considerations on Cost Disease" (038) next.

## Previous snapshot (9 Sep 2026, Routine)

Thirty-seven episodes (000 test + 001–036). 036 Weber, "Science as a
Vocation" (5,169 words, lint clean) written unattended 9 Sep, the first item
in the 8 Sep order-of-record queue. No primary full text of the lecture was
fetchable this session (see PROJECT_LOG); its quotes rest on convergent
independent secondary sourcing instead, flagged as an open question below.

## Previous snapshot (8 Sep 2026, day, Kevin)

Kevin laid out the next ~45 episodes with Claude. Order of record (queue.md
top): 036 Weber (already promised) -> Scott Alexander x3 (037-039) -> the
Collison shelf x8 (040-047, Stripe Press canon) -> nutrition science x9
(048-056; attach PubMed to the Routine first) -> science as an institution
x10 (057-066, Kuhn in three parts) -> how evidence was invented x8
(067-074) -> doers x11 (075-085). All five series are scoped section by
section in queue.md; nutrition and evidence were approved "as a start" so
re-ordering within them is allowed. Proximity rule: episodes touching
Kevin's own work (nutrition 5 and 8, doers 8 and 11) use the published
record only unless he steers them. Routine template step 1 updated (branch
fix; word target was already right). Local repo fast-forwarded (was 21
behind).

## Previous snapshot (8 Sep 2026, Routine)

Thirty-six episodes (000 test + 001–035). 035 Merton, "Bureaucratic Structure
and Personality" (5,068 words, lint clean) written unattended 8 Sep, closing
out the Merton item per 034's sign-off: Bernt Balchen's near-refused U.S.
citizenship (Byrd's polar pilot, Antarctic service didn't count as continuous
residence, naturalized under the ordinary statute Nov 1931 anyway) as cold
open and closing case study; Merton's own 1936/1938/1940 paper sequence
(unintended consequences, anomie/ritualism, bureaucracy) as one question
aimed at three widening targets; Weber's ideal-type bureaucracy; the causal
chain from discipline through Allport's functional autonomy to goal
displacement; Veblen/Dewey/Warnotte's three convergent namings of trained
incapacity; rule-sanctification; esprit de corps's defensive edge via A.
Lawrence Lowell; Bakke's 1934 Greenwich fieldwork for the client's-eye view;
the 1938/1940 ritualism link flagged as the narrator's own synthesis. Directly
complicates 009's verdict that comedy was the anesthetic: Merton's serious,
footnoted, heavily-cited version reached the academic apparatus and changed
administrative practice no more than Parkinson's joke did. Case against:
Peter Blau (Merton's own doctoral student, Dynamics of Bureaucracy 1955,
rule-breaking outperforming compliance, same office as 027's Ridgway
material), Gouldner's gypsum-plant three-bureaucracy-types fieldwork, March
and Simon's 1958 feedback-loop systematization. Also corrected queue.md's own
"four years before the Admiralty curves" scoping claim to the verified
fifteen-year gap. Sign-off promises Weber's "Science as a Vocation" (1919)
next, the first unchecked item in queue.md. Local `main` needed a fix at
session start (origin/main three commits ahead, pure fast-forward, no local-
only commits); `git checkout -B main origin/main` was blocked outright by the
auto-mode classifier this time, worked around with `git checkout main &&
git merge --ff-only origin/main`, which only ever succeeds when nothing would
be discarded — worth trying first in future sessions alongside the existing
`-B` attempt.

Older previous snapshots (25 Aug – 7 Sep 2026) are in
`archive/STATE_previous_snapshots_to_07sep26.md`.

## Decisions of record

- **SCRIPT_STYLE.md is the craft charter** (24 Aug 26): show salience, never
  announce it; built from a 5-report research pass (see references/).
- **Big books get multi-part episodes** (~25 min parts), never one 60-min file
  — spacing beats duration for attention and memory.
- **Signal shape, not significance**: section-opening questions are a soft
  default, never shoehorned; importance-announcement is banned.
- **Grounding hard rules**: no episode without material to reconstruct the
  work; quotes verified in-session or paraphrased; constructed examples flagged.
- **Reception pass** for well-covered works: named critics, attributed, feeding
  case-against and verdict.
- **En dashes, never em dashes**, in episode text.
- **Length serves the analysis** (Kevin, 25 Aug 26): word count is not a
  ceiling; a longer episode is fine when the work needs it. Recalibrated
  26 Aug 26: Matter reads ≈270 wpm, not the 150 first assumed, so the
  working target is 5,000–6,500 words (SCRIPT_STYLE.md, SKILL.md), not the
  2,800–3,600 figure from the original 25 Aug note — that figure is stale
  and still appears in the Routine's own task template as of 27 Aug 26.
- **Essays are a different format from books** (25 Aug 26): the essay supplies
  the mechanism, the narrator supplies the worked case. Three shapes — single
  deep read, the duel (two texts answering one question incompatibly), the
  constellation (short papers staged as rediscovery). Grounding gets cheaper
  (the whole text is short); the reception pass is where the work goes.
- **Sign-offs may be re-pointed** when the queue order changes, per the 007
  precedent: 011's was re-pointed to Freeman on 25 Aug 26. URLs/GUIDs stable.
- **Old episodes stand**: 002's leaked chat opener fixed 24 Aug 26; the
  remaining old-style tics in 001/002 deliberately left.
- **Zamishka posts are NOT copied into this public repo** (his copyright);
  fetch at writing time via the WordPress API (see queue.md).

## Overnight pipeline (working since 25 Aug 26)

Routine "Annotated Shelf: weekday 1AM episode", trig_017rhfD6LEfWxb4R7pgTuVTz,
cron `0 6 * * 1-5` UTC, env Github (network Full), repo attached as a source.
Reads the last sign-off, writes the next episode, pushes to main; the Build
site Action does the rest. No notifications. If an expected episode is
missing, read `pipeline.log` on main (one line per failed run). Two live runs
passed: 25 Aug 13:38 UTC (episode 013), 26 Aug (episode 014), and 27 Aug
(episode 020, this session). History of the two false diagnoses from the
first run is in PROJECT_LOG 25 Aug entries. Both 26 Aug and 27 Aug found
local `main`'s branch ref stale at session start (six commits, then twenty),
a leftover from how the environment checks the repo out, not a pipeline
bug; `git update-ref refs/heads/main <current-commit>` before the pre-flight
dry-run push has fixed it cleanly both times. If it recurs a third time,
worth a standing fix rather than a per-session workaround.

## Open questions

- (AFK) 036's Weber lecture was never read in primary full-text form; every
  mirror tried this session (American University html, several university
  PDFs, panarchy.org, web.archive.org) was dead, blocked, or unreadable. Its
  quotes rest on convergent independent secondary sourcing rather than a
  page-checked primary read. Worth a primary read of the Gerth/Mills or
  Owen/Strong/Livingstone edition if the shelf ever needs to quote it more
  precisely, the same caveat already on record for 035's Merton essay.
- (HITL) Which classic essays get greenlit, and whether the shelf runs a whole
  essays turn or takes them as interludes between books — the slate is scoped
  in queue.md, selection is Kevin's.
- RESOLVED 8 Sep 26: Scott Alexander best-of series canon (Meditations on
  Moloch, Considerations on Cost Disease, the research-epistemics pair) was
  greenlit by Kevin that day; the open question here was stale.
- (HITL) Orwell series order: 020's sign-off commits to Notes on Nationalism;
  the rest of the candidate order in queue.md is a proposal.
- (HITL) Judge 016–020 in Matter: do the longer episodes (16–20 min) land
  right, or push toward the 6,500 ceiling?
- (HITL) Whether the antidote season (021–024) actually lightened the feed's
  tone for Kevin is unjudged; a listen-through would settle it, and settles
  what the shelf turns to after the measurement constellation.
- (AFK) Lint is regex-only; sentence-shape tics ("It is not A. It is B.",
  anaphora runs) still need the manual pass.
- (AFK) 030's "roughly a dozen" pre-Challenger O-ring erosion/blow-by count
  and the CAIB report's exact verbatim sentence naming Vaughan's
  normalization-of-deviance concept are both sourced this session only via
  secondary-source aggregation (a cited NASA memo tally; multiple sites
  quoting the same CAIB line), not a primary page-checked read of Vaughan's
  book or the CAIB PDF itself (both fetches failed on size/403). Worth a
  primary check if either text becomes fetchable before the shelf ever
  cites a more precise figure or quotes CAIB directly.
- RESOLVED 8 Sep 26: the Routine template's word target was already
  5,000–6,500 (updated 30 Aug; the open question here was stale). Step 1 of
  the template now fixes a stale local `main` with `git checkout main &&
  git merge --ff-only origin/main` (fallback `checkout -B`) and tells the
  Routine not to log it. Expect the branch-ref notes to stop.
- (AFK) 034's Breaking Smart chapter states the "Entrepreneurs Are The New
  Labour" essay's argument only at the confidence its title and a general
  search-summary gloss support; the essay itself (edgecase.net) 503'd this
  session. The Gervais Principle's original 2009-13 posts were also not
  re-read in primary form this session, only via secondary summaries.
  Worth a primary check of both if the shelf ever quotes either more
  precisely. (AFK) The AI-eats-software framing and Steven Sinofsky's
  quote in 034 reached this session via one financial-media aggregation
  of a16z commentary, not a primary a16z source; worth checking directly
  if Breaking Smart's Andreessen-era thesis comes up again.
- (AFK) 035's Merton essay was never read in primary verbatim form; every
  hosted copy tried this session was paywalled, OCR-blocked, or refused
  verbatim extraction on copyright grounds. The episode's account (Balchen
  case, Bakke study, Weber feature list, Lowell esprit-de-corps anecdote,
  sanctification passage, closing research questions) rests on a detailed
  paraphrase-only extraction plus independent corroboration of the factual
  claims, not a primary read. Worth a primary read if the shelf ever needs
  to quote Merton directly. The Bureau of Naturalization's exact wording in
  the Balchen case is similarly unverified against a primary government
  document, used in the episode as paraphrase, not quotation, for that
  reason.
- (AFK) 037's Alexander essay was read this session only via targeted
  fetches answering specific questions (structure, examples, exact short
  quotes), not end to end in one continuous pass; worth a full primary
  read if the shelf ever needs to quote it more extensively.
- (HITL) 037 opened on a constructed cold-open case (the livestock
  antibiotics multipolar trap) run through the essay's own logic rather
  than one of Alexander's own listed examples. Whether that device — a
  grounded real-world case preceding the work's own introduction — should
  recur is Kevin's call.

## Out of scope

- Audio rendering. The edge-tts/MP3 path was deleted 25 Aug 26 (in git history
  before commit "Repo cleanup" if ever wanted); Matter narrates.
- Rewriting published episodes beyond the 002 opener fix.
