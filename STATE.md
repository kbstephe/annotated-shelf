# STATE — The Annotated Shelf

## Snapshot (27 Aug 2026)

Twenty-one episodes (000 test + 001–020). 020 Shooting an Elephant
(5,059 words, lint clean) written unattended by the weekday Routine 27 Aug,
paired with A Hanging as the same trap with the audience swapped for a
schedule; case against covers the did-it-happen dispute (Crick, Davison)
and Malreddy's postcolonial reading. 020's sign-off promises **Notes on
Nationalism** (Orwell series, item 3) – next for the Routine. Local `main`'s
branch ref was stale at session start for the second time running (see
Decisions below); worth a permanent fix if it recurs a third time.

## Previous snapshot (26 Aug 2026, late)

Twenty episodes (000 test + 001–019). 018 Seeing Like a State Part Two
(~4,400 words) and 019 Politics and the English Language (~4,700 words)
written on-demand 26 Aug; both lint clean. 019's sign-off promises
**Shooting an Elephant** (Orwell series, item 1) – next for the Routine.
Still slightly under the 5,000-word floor; the Routine should aim higher.

## Previous snapshot (26 Aug 2026, night)

Eighteen episodes (000 test + 001–017). 016 Bullshit Jobs (5,300 words) and
017 Seeing Like a State Part One (~5,200 words) written on-demand 26 Aug.
**Length target recalibrated**: Matter reads ≈270 wpm, so 3,100-word
episodes ran 11–12 min and Kevin found that short; charter now says
5,000–6,500 words. `scripts/lint_script.py` (echoes within 40 words + the
Claude-ism list) is a mandatory pre-flight step. 017's sign-off promises
**Seeing Like a State Part Two** (collectivisation, ujamaa, mētis, the case
against: DeLong/Hayek, Scott Alexander, Laitin, Boudreaux) – next for the
Routine. Queue gained an **Orwell's great essays** series (Kevin, 26 Aug).

## Previous snapshot (26 Aug 2026, evening)

Sixteen episodes (000 test + 001–015). 015 Second Thoughts on James Burnham
(Orwell, 3,186 words) written on-demand 26 Aug as an essays-turn interlude;
its sign-off re-promises **Bullshit Jobs (Graeber)**, still next up for the
Routine. Otherwise unchanged from the morning snapshot below.

## Previous snapshot (26 Aug 2026, morning)

Fifteen episodes (000 test + 001–014). 014 The Utopia of Rules (Graeber),
3,170 words, is the second episode written unattended by the weekday 1AM
Routine — pipeline still works end to end, feed updated within about a
minute of the push. 014's sign-off promises **Bullshit Jobs (Graeber)**;
that's next up, on-demand or at the next weekday firing. Repo cleaned 25 Aug
(MP3 path gone, feed ordering fixed). Next human step: listen to 013 and 014
and judge unattended quality; decide whether episode 000 stays.

## Previous snapshot (25 Aug 2026, evening)

Fourteen episodes (000 test + 001–013). 013 The Peter Principle was the first
episode written unattended by the weekday 1AM Routine. 013's sign-off promised
The Utopia of Rules (Graeber); the Routine attempted it 26 Aug 06:05 UTC and
that became 014. Repo cleaned 25 Aug (MP3 path gone, feed ordering fixed).

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

- (HITL) Which classic essays get greenlit, and whether the shelf runs a whole
  essays turn or takes them as interludes between books — the slate is scoped
  in queue.md, selection is Kevin's.
- (HITL) Scott Alexander best-of series: canon selection is Kevin's call
  before any episode is written (parked in queue.md).
- (HITL) Orwell series order: 020's sign-off commits to Notes on Nationalism;
  the rest of the candidate order in queue.md is a proposal.
- (HITL) Judge 016–020 in Matter: do the longer episodes (16–20 min) land
  right, or push toward the 6,500 ceiling?
- (AFK) Lint is regex-only; sentence-shape tics ("It is not A. It is B.",
  anaphora runs) still need the manual pass.
- (AFK) The Routine's own outer task template still states a 2,800–3,600
  word target that contradicts this file's 26 Aug recalibration; worth
  updating the template directly so future runs do not have to resolve the
  conflict themselves each time.

## Out of scope

- Audio rendering. The edge-tts/MP3 path was deleted 25 Aug 26 (in git history
  before commit "Repo cleanup" if ever wanted); Matter narrates.
- Rewriting published episodes beyond the 002 opener fix.
