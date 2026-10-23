# STATE — The Annotated Shelf

## Snapshot (23 Oct 2026, Routine run)

Seventy-two episodes (000 test + 001-071). 071, ISIS-2 and the astrological subgroup (ISIS-2 Collaborative Group) (5,243 words), was verified by Build commit and feed GUID. The ISIS-2 paper is closed; it is written from the PubMed abstract, Sleight 2000 and Peto 2011 in full text, and Lee 1980's abstract, said so in the script.
**Ruling for 068 onward (Kevin, 16 Oct 26):** no closing bibliography; thin sourcing is said inline in one clause.
**Next step:** 071's sign-off promises item 6, the Women's Health Initiative reversal (queue.md; numbered 072). WHI 2002 is at escholarship.org (qt3mr6f93p); Hernán 2008 is closed, so say so inline.

## Decisions of record

- **SCRIPT_STYLE.md is the craft charter** (24 Aug 26): show salience, never announce it; built from a five-report research pass (references/).
- **Big books get multi-part episodes** (~25 min parts), never one 60-minute file: spacing beats duration for attention and memory.
- **Signal shape, not significance**: section-opening questions are a soft default, never shoehorned; importance-announcement is banned.
- **Grounding hard rules**: no episode without material to reconstruct the work; quotes verified while writing or paraphrased; constructed examples flagged in plain speech.
- **Spoken numbers come from held text** (16 Oct 26): never from a fetch or search summary, which has fabricated and misplaced quotes and gave 059 a wrong figure (corrected in 063).
- **No narrated bibliography** (Kevin, 16 Oct 26): no closing source-list paragraph from 067; thin sourcing is said inline in one clause, and the full list goes in the log's Verification field. 060-066 stand.
- **Reception pass** for well-covered works: named critics, attributed, feeding case-against and verdict.
- **No em dashes** in episode text (the lint flags them); en dashes are permitted, commas and full stops preferred.
- **Length serves the analysis** (Kevin, 25-26 Aug 26): working target 5,000-6,500 words (Matter reads about 270 wpm); longer when the work needs it, never padded.
- **Titles are plain** (Kevin, 28 Aug 26): Work (Author): one short hook. Cap 105 characters and 15 words from 16 Oct 26, enforced by the lint; the rest goes in the description.
- **Digits** (16 Oct 26): numbers written out for the ear, except four-digit years and decimal statistics; enforced by the lint from 067.
- **Lint is mandatory** before every commit, unattended runs included (26 Aug 26, reaffirmed 10 Sep 26): it must print 0 repeats, 0 tics. New families apply forward only; the back catalogue stands.
- **The narrator is Claude** (Kevin, 10 Sep 26): never the listener's first person; his work is named in the third person.
- **BLOOM default is none** (Kevin, 10 Sep 26): one aside only when the mapping is unforced; listener.md maps where a genuine application lands.
- **Proximity rule** (Kevin, 8 Sep 26): episodes touching the listener's own work (nutrition 5 and 8, Doers 8 and 11, any later item so marked) use the published record only unless he steers them.
- **The sign-off is binding** (8 Sep 26): "Next time" names the next work; queue.md's Order of record is the tie-break.
- **Essays are a different format from books** (25 Aug 26): single deep read, the duel, the constellation; the reception pass is where the work goes.
- **Running frames live in FRAMES.md** (16 Oct 26): callbacks carry the mechanism, only where they apply; scripts/frames.py computes where each appears.
- **Sign-offs may be re-pointed** when the queue order changes (007 precedent). URLs and GUIDs stay stable.
- **Old episodes stand**: no rewrite of published scripts unless Kevin asks.
- **Zamishka posts are not copied into this public repo** (his copyright); fetch at writing time via the WordPress API.

## Overnight pipeline

Routine "Annotated Shelf: weekday 1AM episode", trig_017rhfD6LEfWxb4R7pgTuVTz, cron `0 6 * * 1-5` UTC (01:00 St. Louis until 1 Nov 2026, 00:00 after), PubMed connector attached, notifications off, model the environment default. A healthy weekday leaves three commits on main: "Episode NNN: Title", "Build: site + feed [skip ci]", "Log: Episode NNN". Every weekday since 23 Sep has succeeded. Step 1 fast-forwards a stale local main and is not logged. Step 6 (edited 16 Oct 26) waits for a Build commit after the episode commit and for the new episode's GUID in site/feed.xml, not its title. If an episode is missing: a "Pipeline failure" commit adding a line to pipeline.log means the prompt's FAILURE step ran; no such commit means the session died earlier, so open that day's run from the Routine's session list. CI builds with full history, so pubDates come from first-commit dates; a local shallow preview reuses the committed feed's dates.

## Open questions

- (AFK) 071 relays ISIS-2 through Sleight 2000 and Peto 2011 and holds Lee 1980 as an abstract; the ISIS-2 and Lee papers in full text would confirm them.
- (AFK) 069 relays Fisher 1955-56 quotes through Gigerenzer; Fisher 1955 (JRSS B) in full text would confirm them.
- (AFK) 068's smoking chapter rests on Salsburg's account; Cornfield 1959 and Fisher's Nature "Cancer and Smoking" in full text would confirm it.
- (AFK) 067's account of how Snow and Semmelweis were received rests on the standard story from memory, hedged in the script; Nuland, Johnson or the 1855 inquiry report in full text would confirm it.
- (HITL) Has Kevin listened past 024? Every register judgment since August waits on that: the density of 058-066, the register pivots of 037 and 043-050, and whether restored callbacks read as teaching or repetition. One listen to 062 and 065 back to back would settle the density question.
- (HITL) Whether to pin the Routine's model; it writes on the environment default, a tier below Kevin's day sessions.
- (HITL) Global health as an institution, making doctors, and the interlude pool (Shaw's preface before 068, Arrowsmith before 070) are scoped in reviews/2026-10-16-topics-and-improvements.md but not scheduled.
- (HITL) Whether the classic-essays and Orwell items ever resume; they sit below the series of record.
- (HITL) 052 and 055 were written under the proximity fallback with sources in Kevin's own research geography; whether that line was drawn right.
- (AFK) Nutrition 048-055 rest largely on secondary sourcing (log entries 22 Sep to 1 Oct); one slip found, 053's "listed no industry funding". A one-off check of their figures against primaries now reachable is optional.
- (AFK) Collison shelf 042-046 never read their books in primary form (log 14-18 Sep); 036 Weber and 035 Merton likewise (log 8-9 Sep).
- (AFK) Science series open reads: Merton 1968; Pier SI appendix; Li and Agha in full; Swiss lottery outcomes; the HHMI paper; Atlantic essay; Cochrane's 1979 essay and Mather 1976 (log 12-16 Oct).
- (AFK) ISIS-2, Guyatt 1992, Hill 1965, Hill 1990 and Hernán 2008 are unreachable from the cloud; a text copy placed in the repo would let 070-073 anchor on them.

## Out of scope

- Audio rendering. The edge-tts/MP3 path was deleted 25 Aug 26 (in git history before commit "Repo cleanup"); Matter narrates.
- Rewriting published episodes beyond the 002 opener fix.

Older snapshots and the full open-questions list to 16 Oct 26 are in archive/STATE_previous_snapshots_08sep26-16oct26.md; earlier ones in archive/STATE_previous_snapshots_to_07sep26.md.
