# STATE — The Annotated Shelf

## Snapshot (25 Aug 2026)

Thirteen episodes. 012 opens a **classic-essays turn**: shorter objects than the
books, scoped and analysed in queue.md's new "Classic essays" section (eight
picks plus a second tier). 012 is Jo Freeman's The Tyranny of Structurelessness
— Michels from inside a movement that had abolished elections. 011's sign-off
was re-pointed to hand off to it; 012 promises **The Peter Principle**, so the
weekday 1AM Routine picks that up next.

Written on branch `claude/classic-essays-workflow-0rl9li`, not by the pipeline —
the same merge-before-06:00-UTC caveat as the 006–007 run applies.

## Previous snapshot (24 Aug 2026, evening)

Twelve episodes written: 000 test, 001 Moral Mazes, 002 Davies survey, 003–005
The Unaccountability Machine deep series, 006–008 The Organization Man deep
series (Whyte + Burnham's Managerial Revolution + the wives/pipeline/exit part),
009 Parkinson's Law, 010–011 The Machiavellians two-parter (moved up from the
Coda at Kevin's request; Kevin also directed episodes be produced on demand
rather than waiting for the 1AM Routine). Feed builds via GitHub Actions;
Matter narrates. Episode 011's sign-off promises **The Peter Principle** next —
the weekday 1AM Routine will pick it up unless Kevin asks for it sooner.

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
- **Length serves the analysis** (Kevin, 25 Aug 26): 2,800–3,600 words is the
  target, not a ceiling; a longer episode is fine when the work needs it.
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
missing, read `pipeline.log` on main (one line per failed run). Live test
passed 25 Aug 13:38 UTC (episode 013). History of the two false diagnoses is
in PROJECT_LOG 25 Aug entries.

## Open questions

- (HITL) Which classic essays get greenlit, and whether the shelf runs a whole
  essays turn or takes them as interludes between books — the slate is scoped
  in queue.md, selection is Kevin's.
- (HITL) Scott Alexander best-of series: canon selection is Kevin's call
  before any episode is written (parked in queue.md).

## Out of scope

- Audio rendering. The edge-tts/MP3 path was deleted 25 Aug 26 (in git history
  before commit "Repo cleanup" if ever wanted); Matter narrates.
- Rewriting published episodes beyond the 002 opener fix.
