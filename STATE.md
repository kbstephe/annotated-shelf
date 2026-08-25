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

## Open questions

- (HITL, 25 Aug 26) **Overnight pipeline stalls, half-fixed.** Diagnosis: fired
  sessions go idle within ~90s in "needs input" — they end their turn (or hit
  an auto-mode permission gate) and wait forever; pipeline.log never gets
  written because the session doesn't know it failed. Prompt fix is live on
  trig_017rhfD6LEfWxb4R7pgTuVTz (UNATTENDED SESSION block). Awaiting Kevin:
  (a) approval to commit .claude/settings.json permission allowlist for the
  pipeline's git/build/search commands; (b) a re-test (fire the Routine).
  Details in PROJECT_LOG 2026-08-25 midday entry.

- ~~(AFK) Is any overnight pipeline scheduled?~~ RESOLVED 24 Aug 26, REBUILT
  25 Aug 26: the Routine "Annotated Shelf: weekday 1AM episode" is now
  trig_017rhfD6LEfWxb4R7pgTuVTz (cron 0 6 * * 1-5 UTC, enabled, same
  environment). The original fired 25 Aug 06:30 UTC and failed silently,
  publishing nothing. Current design, per Kevin (keep it simple, no
  notifications, don't burn tokens): pre-flight (git fetch + push dry-run)
  aborts BEFORE any research or writing; a run that fails at any stage appends
  one line to pipeline.log at the repo root ("<UTC ts> FAILED (<stage>):
  <reason>") and pushes it to main — that file is the failure record, check it
  if an expected episode is missing. No notifications of any kind.
- ~~(BLOCKER, 25 Aug 26) egress policy blocked research hosts~~ RESOLVED
  25 Aug 26: Kevin set the environment's network access to Full. Zamishka's
  WordPress API and primary-text sites are reachable from new sessions.
- (HITL) Which classic essays get greenlit, and whether the shelf runs a whole
  essays turn or takes them as interludes between books — the slate is scoped
  in queue.md, selection is Kevin's.
- (HITL) Scott Alexander best-of series: canon selection is Kevin's call
  before any episode is written (parked in queue.md).

## Out of scope

- Local audio rendering (edge-tts path is manual-dispatch only; Matter narrates).
- Rewriting published episodes beyond the 002 opener fix.
