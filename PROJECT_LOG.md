# PROJECT_LOG — The Annotated Shelf

Append-only, newest last.

## [2026-08-24] — Craft charter rebuild + Davies three-part deep series

**Decisions:** SCRIPT_STYLE.md rewritten as the craft charter (show-don't-tell
salience, chain-of-questions structure, retention design, grounding rules,
reception pass, multi-part policy, en dashes). Multi-part chosen over single
long episodes for big books. 002's leaked chat-reply opener fixed; other old
tics left. Section-opening questions adopted as soft default only (Kevin: "not
an abs rule that you shoehorn everything into"). Davies deep redo chosen over
continuing the queue when "next series" was clarified.

**Traps & dead ends:** zamishka.com DNS is dead; the WordPress mirror
(zamishkadotcom.wordpress.com) 403s WebFetch/direct fetch, but BOTH the
site via Chrome AND the public WordPress API work
(`public-api.wordpress.com/rest/v1.1/sites/zamishkadotcom.wordpress.com/posts/`
— 22 posts, 2016–2020). web.archive.org is unfetchable from this environment.
A Scott Alexander series was started on a misread request and parked; its
research survives here: Moloch verified (30 Jul 2014, ~14 examples before the
principle, Elua ending), Outgroup verified (30 Sep 2014, proximity-plus-small-
differences, Red/Blue/Grey, self-implicating ending), reception search found
David Gerard and Elizabeth Sandifer as named critics.

**Open questions:** see STATE.md (overnight-pipeline existence AFK; Scott
Alexander canon HITL).

**Artifacts:** Modified `SCRIPT_STYLE.md` (charter), `SKILL.md` (research step
with reception pass), `episodes/002` (opener), `queue.md` (Organization Man,
Zamishka unblocked, SA series parked, 003–005 done). Created
`references/craft-research-aug2026.md` (five research reports),
`episodes/003–005` (Unaccountability Machine parts 1–3; 2,823 / 2,802 / 2,795
words, pre-flight clean), and the four project docs.

**Context:** The charter came from five parallel research reports (NYRB/LRB
craft, Rao/ACX internet criticism, AI-podcast precedents, learning science,
science/philosophy essayists) — full detail preserved in references/, so the
rationale for any rule is recoverable. The one deliberate tension resolution:
retention evidence favors explicit signposting, essayist craft bans it; the
charter splits it as "signal shape, not significance." Part 005's sign-off
promises The Organization Man next — under the continuity rules that promise
is binding on whoever writes episode 006.

## [2026-08-24 evening] — Organization Man two-parter (006–007)

**Decisions:** Kevin confirmed the queue's recommended pairing: The Organization
Man (Whyte) + The Managerial Revolution (Burnham) as one two-part series. 006 is
Whyte (Social Ethic, Park Forest, personality tests, cheat appendix); 007 is
Burnham steelmanned, Orwell's "Second Thoughts" as the case against, then the
synthesis: Burnham tracked command migrating out of the owners' hands but
misread the destination — it dissolved into procedure (Davies's machine), the
managers became components, Rao's Sociopaths are squatters on an empty throne.
007's sign-off promises Parkinson's Law.

**Traps & dead ends:** WebFetch egress is blocked for nearly all domains
(ribbonfarm.com, wikipedia, orwellfoundation, orwell.ru, terebess.hu);
WebSearch snippets still work and were enough to verify all load-bearing
quotes: Whyte's opening line + Social Ethic three propositions, Mills's NYT
review "Crawling to the Top" (9 Dec 1956, "organizational crawl", "Boy Scout"),
Orwell's "predicting a continuation of the thing that is happening" and "power
worship blurs political judgement", groupthink coined by Whyte in Fortune
March 1952, Rao's Ribbonfarm Whyte series (Nov 2008, planned ~8 parts, stalled
after 3 posts: Introduction / Ideology / Training). Berle–Means "200 largest ≈
half of corporate wealth" and the WPB mobilization material are from training
knowledge, stated at rounded precision.

**Resolved:** the AFK open question — the overnight pipeline EXISTS: Routine
"Annotated Shelf: weekday 1AM episode" (cron 0 6 * * 1-5 UTC), fires into a
fresh session, reads the last sign-off, pushes to main. Noted in STATE.md.

**Artifacts:** episodes/006-organization-man-part-one.md (2,919 w),
episodes/007-organization-man-part-two.md (2,829 w), queue.md (006–007 done,
Parkinson's Law next), STATE.md (snapshot + AFK resolution).

**Context:** Written in an interactive session on branch
claude/episode-status-plan-om1bg7, not by the 1AM pipeline — if this branch is
not merged to main before the next weekday 06:00 UTC firing, the pipeline will
re-write The Organization Man itself (it reads origin/main), so merge or pause
the trigger first.

## [2026-08-24 night] — Part Three added; "old episodes stand" softened

**Decisions:** Kevin asked for the remaining valuable Whyte/Burnham material to
be published and explicitly OK'd editing published episodes (the "old episodes
stand" decision is therefore softened — edits allowed, URLs/GUIDs stay stable).
Shipped 008 (Part Three: the corporation wife via Whyte's Oct–Nov 1951 Fortune
series, the training pipeline of Part II of the book, Friedan as the closing of
Whyte's case file, and the Street Life Project exit as the verdict on the
appendix). Edited 006/007 descriptions to "of three" and rewrote 007's sign-off
to hand off to Part Three (008 now carries the Parkinson's Law promise).
Burnham's The Machiavellians added to queue (Coda) rather than crammed in.

**Verification:** wife-screening (~half of companies in Fortune's study) and
the Oct/Nov 1951 Fortune wives series confirmed via search; Part II chapter
titles confirmed; Whyte plaza quote "what attracts people most, it would
appear, is other people" verified, plus 1969 Street Life Project start, plaza
zoning and Bryant Park lineage. Friedan connection drawn analytically, no
cross-citation claimed.

**Artifacts:** episodes/008-organization-man-part-three.md (2,839 w), edits to
006/007, queue.md, STATE.md.

## [2026-08-24 late] — 009 Parkinson + 010–011 Machiavellians, on demand

**Decisions:** Kevin: don't wait for the 1AM Routine — produce and push now;
The Machiavellians promoted from Coda to next series. Shipped 009 (Parkinson's
Law, single episode: Admiralty/Colonial Office curves, the two engines,
injelititis, bikeshed + cabinet life-cycle read through Ashby, reception-as-
case-study verdict) and 010–011 (The Machiavellians: formal vs real meaning,
Machiavelli/Mosca/Pareto/Sorel in part one; Michels's iron law, freedom as
contested power, Orwell + the school's fascist-adjacent biographies as the
case against, in part two). 011 promises The Peter Principle.

**Verification:** Admiralty 78%-up/ships 67%-down and Colonial Office 372→1661
(~5–6%/yr) verified; "work expands..." opening and triviality-law sentence
verified; bikeshed figures (£10M/2.5min, £350/45min, £21/75min) verified;
Michels 1911 SPD case verified; Pareto "graveyard of aristocracies" verified.
Coefficient-of-inefficiency (~20) and injelititis from training knowledge,
stated with hedged precision; "who says organization says oligarchy" used as
paraphrase, not quoted.

**Artifacts:** episodes/009 (2,898 w), 010 (2,813 w), 011 (2,778 w); queue.md
(009–011 done, Machiavellians entry moved out of Coda); STATE.md snapshot.

## [2026-08-25] — 012 Freeman, and a classic-essays slate

**Decisions:** Kevin asked for classic essays that could be ported into the
Matter workflow, with analysis. Scoped eight candidates plus a second tier into
a new queue.md section, with the format analysis behind them: an essay is too
short to carry an episode the way a book does, so the essay supplies the
mechanism and the narrator supplies the worked case — three usable shapes
(single deep read, the duel, the constellation). Shipped the top pick as 012:
Jo Freeman's The Tyranny of Structurelessness, read as the field report the iron
law never had. Chapters: the decision nobody made; the organizer who had seen a
real organization (SCLC, then the Westside Group in her own apartment); there is
no such thing as a structureless group; the denominator problem (the clinician's
chapter — an informal elite is unaccountable because it is unmeasurable); the
star system and Trashing; the case against; verdict. Delayed thesis: structure
does not stop power concentrating, it gives the concentration an address, and an
address is the difference between an elite you can fight and one you cannot name.
Re-pointed 011's sign-off to hand off to Freeman (007 precedent); 012 promises
The Peter Principle, keeping the 1AM Routine on the queue's first unchecked item.

**Verification:** publication history verified (Beulah, Mississippi talk May
1970; declined by Notes from the Third Year 1971; The Second Wave 1972; Berkeley
Journal of Sociology vol 17 1972-73 pp 151-165; Ms. July 1973; Joreen on the
movement printings). Biography verified (Berkeley BA 1965, SCLC in the South,
free school course June 1967, Westside Group in her apartment, Chicago PhD 1972
on the movement itself). Core arguments verified: structurelessness impossible,
"smokescreen for the strong or the lucky", elite as friendship network and not
conspiracy, the star system, and all seven principles of democratic structuring.
Trashing verified (Ms. April 1976, the Ramparts letter incident, drew more mail
than any prior Ms. article; the "psychologically mangled" phrase used once,
under fifteen words). Case against verified: Cathy Levine, The Tyranny of
Tyranny, Black Rose no. 1, Autumn 1974; Jason McQuinn's "organizationalist
repudiation of anarchism" review. The Occupy read is marked as the narrator's
conclusion rather than borrowed from a named critic, since only summaries were
reachable.

**Blocker found:** the remote session's egress proxy returned 403 for
jofreeman.com, marxists.org, crassh.cam.ac.uk, en.wikipedia.org and
public-api.wordpress.com. The essay could not be fetched; grounding fell back to
training knowledge verified through web search, which was adequate here and
would not be for an obscure work. The queued Zamishka episode depends on the
WordPress API and cannot be written at all under this policy — noted in queue.md
and STATE.md, since the 1AM Routine will hit it.

**Artifacts:** episodes/012-tyranny-of-structurelessness.md (3,710 w), edit to
011's sign-off, queue.md (Classic essays section, Zamishka caveat), STATE.md.

**Context:** Written in an interactive session on branch
claude/classic-essays-workflow-0rl9li. Pages serves main, so nothing reaches
Matter until this is merged.

## [2026-08-25 later] — 012 verified against the primary text; one fix

**Context:** Kevin set the environment's network access to Full, so the
primary sources became fetchable. Pulled jofreeman.com's texts of The Tyranny
of Structurelessness and Trashing and re-verified 012 against them.

**Confirmed:** "no such thing as a structureless group"; "smokescreen for the
strong or the lucky"; elites as friendship networks, "not conspiracies";
the star system (press-appointed, movement "cannot remove them"); all seven
principles of democratic structuring; publication history exactly as the
site's headnote gives it; Trashing's April 1976 date, record letter response,
end-of-1969 dropout, "numb despair", "psychologically mangled" phrasing.

**Fixed:** chapter five had attributed the Ramparts-letter incident to the
Ms. article — it is not in it (the word never appears); it comes from
Freeman's later accounts of the Westside Group. Re-attributed, cut an
unverifiable invented detail ("roughly two hundred words long"), and rebuilt
the passage on what Trashing actually documents: the thousand-cuts ostracism
(quoted, under fifteen words), the mailing list, the changed meeting dates,
the dissolved fund-raising plan, the denial-of-pattern — tied back to chapter
four's no-address structure. 3,851 words after the edit. GUID/URL unchanged.

**Also this session:** live test of the rebuilt 1AM Routine fired at ~10:43
UTC (session cse_01Nn4e1uPQpUopAMxf2kWTRw), expected to publish 013 Peter
Principle; monitor running. Routine now has no notifications — failures append
a line to pipeline.log on main instead.

## [2026-08-25 midday] — Pipeline stall diagnosed; fixes half-landed, two approvals pending

**Finding:** the overnight Routine's failure mode is a STALL, not a crash. Live
test fired 10:43 UTC (session cse_01Nn4e1uPQpUopAMxf2kWTRw): it went idle at
10:44:49 — 80 seconds in, ~4k output tokens, ~$0.38 — in "needs input" state,
with nothing pushed. Because the session never *thinks* it failed, the FAILURE
step (pipeline.log) never runs; the run just waits forever for a reply that
cannot come. Same signature as the 25 Aug 06:30 UTC silent failure. A 40-min
git monitor confirmed: no episode, no pipeline.log, ever.

**Two suspected causes, one confirmed class:** (1) turn-ending to "show the
user" — SKILL.md's "show the chapter outline and first ~150 words" invites a
headless session to end its turn, which is fatal; (2) auto-mode permission
gates — confirmed real this session when the classifier blocked this very
session twice (writing .claude/settings.json; re-firing the trigger). A
headless session hitting such a gate stalls identically.

**Fixed already:** the Routine's prompt (trig_017rhfD6LEfWxb4R7pgTuVTz) now
opens with an UNATTENDED SESSION block: nobody will ever reply; never end the
turn until the episode is published-and-verified or the FAILURE step has
pushed pipeline.log; skip the outline-showing step. Routine design otherwise:
no notifications (Kevin's call), pre-flight git fetch + push --dry-run aborts
before any writing, failures append one line to pipeline.log on main.

**Pending, needs Kevin:** (1) approve committing .claude/settings.json with a
permissions.allow list (git add/commit/push/fetch/pull/checkout/log/show/
status/diff, python3 scripts/build_site.py, WebSearch, WebFetch) so headless
runs never hit a prompt — classifier rightly refused to let the session
self-grant; (2) re-run the test (say "fire it" or use Run now on the Routine
at claude.ai). If a re-test still stalls at the push step, the allowlist is
the missing half. The stalled test session is inspectable in Kevin's session
list ("⚡ Annotated Shelf: weekday 1AM episode") — opening it would show
exactly what it was waiting on.

**Also useful for future sessions:** network access is now Full — jofreeman.com
etc. fetchable (that's how 012's Trashing fix happened). SKILL.md's
show-the-outline step deserves an "unless unattended" carve-out if stalls
recur. Next scheduled firing: 26 Aug 06:05 UTC, expected to attempt 013 The
Peter Principle.

## [2026-08-25 afternoon] — Pipeline root cause: no repo source on the Routine

**Finding:** the run log of the 10:43 UTC test (get_run_log on
cse_01Nn4e1uPQpUopAMxf2kWTRw) shows "No sources configured", a manual clone,
then `git push --dry-run` rejected 403 by the git proxy because the repo was
not in the session's authorized set. The midday "stall" diagnosis was wrong:
the session ended its turn correctly because it could not push anything,
including pipeline.log. Permission gates were never hit.

**Fixed:** Routine trig_017rhfD6LEfWxb4R7pgTuVTz now has
`sources: [github.com/kbstephe/annotated-shelf]`; prompt says the repo is
pre-cloned and forbids push notifications. build.yml now triggers only on
main (side-branch builds were producing bot commits that needed merge
commits). SKILL.md step 2 has an unattended-session carve-out.

**Pending:** delete the three stale remote `claude/*` branches (classifier
blocked the delete here; content is all on main, leftovers are bot builds).
Live test = the 26 Aug 06:05 UTC firing.

**Live test PASSED** (25 Aug 13:33 UTC fire, session cse_01G1jgLYyP1xwE4cncELbf2s):
Episode 013 The Peter Principle pushed 13:38 UTC (3,049 w), site built, feed
updated, no pipeline.log. Stale claude/* branches deleted. Quality of the
unattended draft not yet reviewed by Kevin.

## [2026-08-25 afternoon, 2] — Repo cleanup

**Removed:** the dead MP3 pipeline (render.yml, render.py, auto_publish.py,
publish.py, root feed.xml + episodes.json, the 000 test MP3). All recoverable
from git history. `.gitignore` trimmed to `__pycache__/`.

**Fixed in build_site.py:** episodes committed together (multi-part series)
sorted arbitrarily in the index and feed (009 above 010/011, 006 above 007);
ties now break by slug, newest first. pubDates normalised to UTC (local
commits produced -0500, bot commits +0000).

**Docs:** STATE.md pipeline section condensed; SKILL.md first-time-setup
section dropped, step numbering fixed (4 was missing); queue.md duplicate
Done entry for 006–008 removed.

**Flagged, not changed:** 012 is 3,891 words (band is 2,800–3,600); 002 keeps
13 em dashes under the "old episodes stand" decision; episode 000 (pipeline
smoke test) is still first in the public feed and index, pending Kevin.

## [2026-08-25 afternoon, 3] — Session close: pipeline fixed, repo cleaned, /done added

**Decisions:** Length band 2,800–3,600 is a target, not a ceiling (Kevin).
Routine now runs a 7th step: session capture via the repo-local
`.claude/skills/done/SKILL.md` (log entry + STATE snapshot + push), so
unattended runs leave the same record a human session does. MP3 path deleted
rather than kept as a fallback. build.yml triggers on main only.

**Traps & dead ends:** two false diagnoses of the overnight failure preceded
the real one (see the two earlier 25 Aug entries): "stall / needs permission
allowlist" was wrong; the Routine simply had no repo source attached.
`get_run_log` on the run session is the tool that settles it. The auto-mode
classifier blocks `git push --delete` and some Edit calls from Claude Code
sessions; Kevin ran those by explicit permission.

**Open questions:**
- (HITL) Episode 000, the 126-word smoke test, still opens the public feed
  and index. Delete or keep.
- (HITL) Has Kevin listened to 013, the first unattended episode? Quality of
  unattended Sonnet output is unreviewed.
- (HITL, carried) Classic-essays selection; Scott Alexander canon.

**Artifacts:** Created `.claude/skills/done/SKILL.md`; modified `CLAUDE.md`
(pointer), Routine prompt (step 7, length rule, read STATE first). Earlier
today: build.yml, build_site.py, SKILL.md, STATE.md, queue.md, .gitignore;
deleted render.yml, scripts/{render,auto_publish,publish}.py, root feed.xml,
episodes.json, 000 MP3.

**Context:** The Routine is now the primary writer; interactive sessions are
for on-demand episodes and craft changes. Every fact about pipeline health is
in STATE.md's "Overnight pipeline" section and pipeline.log on main.

## [2026-08-26] — 014 The Utopia of Rules, unattended Routine run

**Decisions:** Wrote The Utopia of Rules (Graeber, 2015) as a single episode
rather than a multi-part series — queue.md had not flagged it for parts, and
the four essays compress into one question chain without padding. Spine:
constituted power (rules backed by force) versus constituent power (the
capacity to make new rules), with the Batman appendix's argument as the
delayed thesis rather than a detour. Chapters: the mother's-paperwork cold
open plus author bio (LSE anthropologist, Debt: The First 5,000 Years, Occupy
organizer); the iron law of liberalism against this season's audit-society
and Organization Man material; structural violence, structural stupidity,
and interpretive labor from "Dead Zones of the Imagination," read against
013's creative incompetence to show why this asymmetry has no individual
escape hatch; "Of Flying Cars and the Declining Rate of Profit" read as what
Burnham's managers (007) actually did with the power they inherited; the
title essay's play-versus-games distinction and bureaucracy as relief, not
just cage; the Batman/"Super Position" appendix on constituent power, tied
back to Graeber's own Occupy involvement. 014's sign-off promises Bullshit
Jobs, the next unchecked queue item.

**Verification:** Book's four-part structure confirmed (intro "The Iron Law
of Liberalism and the Era of Total Bureaucratization"; essays "Dead Zones of
the Imagination," "Of Flying Cars and the Declining Rate of Profit," "The
Utopia of Rules, or Why We Really Love Bureaucracy After All"; appendix "On
Batman and the Problem of Constituent Power," originally "Super Position,"
The New Inquiry, 8 Oct 2012). Mother's-stroke anecdote and its close ("running
around feeling like an idiot all day?") verified via the book text; the iron
law of liberalism's wording verified across multiple sources; "impersonal
rules... backed up by the threat of force" and the structural-stupidity
definition verified; poetic-vs-bureaucratic-technologies and the 1970s pivot
verified; play-vs-games/Calvinball distinction and "fear of play" verified;
the Batman appendix's constituent/constituted-power argument and its closing
line ("shriveled into incoherence," 14 words, quoted) verified against the
original New Inquiry essay text. Graeber's "99 percent" credit stated with
his own qualification (collaborative, not sole authorship) per his own
account. Reception: Bart Zantvoort (Marx and Philosophy Review of Books) and
Tomas Hachard (NPR) both verified by fetch, used as the case against.

**Traps & dead ends:** The Batman appendix's full text wasn't fetchable from
theanarchistlibrary.org (too long for the fetch tool) or revoltlib.com (503);
verified instead via the original shorter New Inquiry piece and secondary
summaries, which was sufficient since the appendix is the book chapter
reprinted from it.

**Open questions:** carried from STATE.md — episode 000's fate, Kevin's
listen-through of the unattended episodes, classic-essays/Scott-Alexander
selection.

**Artifacts:** episodes/014-utopia-of-rules.md (3,170 words), queue.md (014
done, Bullshit Jobs promised), STATE.md snapshot.

**Context:** Written by the unattended weekday Routine. Pre-flight found
local `main` on a detached HEAD with the `main` branch ref six commits stale
(from a prior session's checkout); fixed by fast-forwarding the ref rather
than deleting anything, since it was a clean ancestor of origin/main. Build
Action commit landed and the feed carried the new title within about a
minute of the push.

## [2026-08-26] — 015 Second Thoughts on James Burnham (on-demand interlude)

**Decisions:** Kevin asked for the Orwell essay the shelf had cited three
times (007, 010, 011) as its own episode. Single deep read, essay format.
Spine: the track-record audit (score the forecaster's lean before arguing the
model), a clinician's instrument. Chapters: the ledger of Burnham's 1940/42/44
forecasts; power worship read off the Lenin's Heir banquet passage; Orwell's
own concessions as the steelman; the turn — Orwell's closing "democratise or
perish" forecast scored by his own method, open and losing for 45 years, saved
only by having a mechanism where Burnham had momentum; case against (reading
motive off prose is psychology on a text; the Francis/Lyons managerial
revival) answered with Milanovic's 80-years-on verdict. Sign-off re-promises
Bullshit Jobs so the Routine's next target is unchanged; 014's sign-off left
as is.

**Verification:** Essay text fetched (Orwell Foundation + orwell.ru):
"whoever is winning at the moment will always seem to be invincible" (the one
quote used, 11 words); "fascinated admiration", "major mental disease...
cowardice", "never stops to ask why people want power", "democratize itself,
or it will perish", the 1940/1942/1944 forecast sequence, and the concession
that the drift toward oligarchy was real all verified; banquet passage
paraphrased. Shelden's "brilliant criticism" via Wikipedia summary,
attributed. Milanovic (Global Policy / Substack, Mar 2024) and Lyons (China
Convergence, 2023, with its "front of one's nose" epigraph) fetched and
attributed. Orwell's 1944 Tribune review and 1947 New Leader essay mentioned
from search results only, no quotes. Kelly's Cornell biography chapter did
not load (ECONNREFUSED); not cited.

**Artifacts:** episodes/015-second-thoughts-on-burnham.md, queue.md,
STATE.md, this entry.

## [2026-08-26] — Audio echoes and Claude-isms (Kevin feedback)

**Decisions:** Kevin hears phrases repeated back-to-back in the narration and
narrator tics ("the point is", "load-bearing", "that is where the difference
really lies"). Cause is the writing, not the build: the charter allowed
restatement-with-variation and rhetorical echoes, and licensed "load-bearing"
for technical cruxes. Charter now bans echoes within ~40 words and all such
tics; new `scripts/lint_script.py` flags both and is a mandatory pre-flight
step (SKILL.md 2b). 015 re-edited surgically (14 + 9 replacements, 3,138
words, lint clean) — the one exception to "old episodes stand", because it
was minutes old. Earlier episodes left as published; lint shows 001–014 all
carry echoes (004, 012, 013 worst), fixable on request.

## [2026-08-26] — Lint extended from online Claude-ism catalogues; 012–014 cleaned

**Decisions:** Kevin: "it is worth sitting with this" is a classic; find the
documented Claude-isms online. Lint list now also carries Velitchkov's 22
Claude cliches (Link & Think), claudisms.ai / Will Francis patterns:
"genuinely", "the honest version", "has a name", "not a X but a Y", "which is
exactly", "turns out to be", "it matters because", "falls out of", etc.
Episodes 001–011 stay as published (Kevin has listened through
Machiavellians); 012, 013, 014 re-edited surgically (18 + 22 + 16
replacements) and 015 once more; all four lint clean. Heredoc backslash
mangling bit twice while building the lint file; it was rewritten whole via
the Write tool.

**Artifacts:** scripts/lint_script.py (rewritten), episodes/012–015.

## [2026-08-26] — 016 Bullshit Jobs, 017 Seeing Like a State Part One; length recalibrated; Orwell series queued

**Decisions:** Kevin: episodes are coming out 11–12 min, "kinda short". At
~3,100 words that means Matter reads ≈270 wpm, not the 150 the charter
assumed. Target now 5,000–6,500 words (charter + SKILL updated). 016 written
at 5,300 words: the denominator as the spine; five types mapped onto
Parkinson/Peter/Whyte/Davies; managerial feudalism steelmanned then answered
with the empty-throne finding from 007; Soffia et al. (EWCS: 4.8%, falling,
refuse workers highest, graduates half the rate) vs Walo (AWCS: 19%, sales
OR 2.61, finance 2.20, managers 1.85) resolved as a frame problem (feeling of
useful work vs the job's social usefulness); case against from Robbins,
Anthony, Heller, Duncan. 017 written at ~5,200 words as part one of two:
forestry (second rotation, Waldsterben), legibility (surnames incl.
Philippines 1849, metric, cadastre), a new grid chapter (Bruges/Chicago,
Manhattan 1811, Dutch registers), high modernism and the four conditions,
Haussmann, Plan Voisin, Jacobs, Brasília via Holston; ends on the question
part two answers. Queue: Orwell's great essays series added with nine
candidates; selection Kevin's.

**Verification:** Graeber quotes: "a scar across our collective soul" (Strike!
2013, via libcom mirror); definition paraphrased. Soffia et al. and Walo
numbers from the journal pages. Robbins (Nation) fetched. Duncan/Anthony/
Heller via the Wikipedia reception section, attributed. The German-military
computer testimony is from memory of the book (Kurt), told without a quote
and flagged as one of the testimonies. Scott: forestry, legibility,
four conditions, Brasília/Holston/brasilite from solid knowledge plus the
SSC review and Cato Unbound page; the Dutch-registers case is in the book
but told from memory; the 1811 plan figures (12 avenues, 155 streets) from
general knowledge. Strike! site itself 403'd.

**Artifacts:** episodes/016, 017; SCRIPT_STYLE.md, SKILL.md (length);
queue.md (016 done, 017 part one, Orwell series); STATE.md; this entry.

## [2026-08-26] — 018 Seeing Like a State Part Two, 019 Politics and the English Language

**Decisions:** 018: collectivisation opened via Campbell's Montana farm and
Lenin's Taylorism (from knowledge of the book), legibility-for-appropriation
as the driver, private plots as the illegible remainder; ujamaa via Scott's
own figure (at least five million moved, 1973–76, verified by search) with
the colonial precedent; mētis (harbour pilot, oak leaf/squirrel's ear); the
four rules read as prescribing rules and as the reverse of the four
conditions; case against from Tauger (H-Net 1999, harvests omitted), Scott
Alexander (dice stacked; Green Revolution; mētis vs resistance), DeLong vs
Farrell on Hayek (Crooked Timber fetched), Laitin; a closing "lean" chapter
applying 015's Orwell audit to Scott himself. 019: rules conceded in full
(Pullum's 26% vs ~17% passives, Zwicky/Strunk provenance, Elimination of
the Fittest; Poole "most wildly overrated"; Ed Smith's misleading
simplicity), mechanism defended: the sentence that cannot be checked; the
euphemism list removes the image, not the information; the blank-discs hack
as the organization man at sentence level. Two worked cases: a constructed
clinical note and a constructed grant paragraph, both flagged as
constructed. Chapter on the shelf's own lint as an Orwellian instrument.
Sign-off → Shooting an Elephant.

**Verification:** Orwell quotes verified against the Foundation text (soft
snow; lies truthful/murder respectable; the self-admission; the
pacification list; Ecclesiastes parody). Pullum count from Language Log
(p=2922: "more than 20 percent"; the 26%/17% figures from the search
summary of his passive_loathing paper). Poole and Smith quotes via search
summaries, attributed. Wikipedia's ujamaa figure (11 million) conflicts
with Scott's "at least five million"; the episode uses Scott's, attributed
to him. Tauger's review page 403'd; his argument taken from the H-Net search
summary and his title. Campbell/Gigant details from memory of the book.

**Artifacts:** episodes/018, 019; queue.md; STATE.md; this entry.

## [2026-08-26] — Session close (five episodes, lint, length recalibration)

**Decisions:** Recorded in the five entries above (015–019, echo/tic lint,
270-wpm length target, build.yml rebase-before-push, Orwell series queued).
**Traps & dead ends:** Bash-tool heredocs strip backslashes; every regex
edit attempted inline broke the lint file until it was rewritten whole via
the Write tool. WebFetch 403s on strike.coop, H-Net, LessWrong; DeLong's
typepad is dead (use Crooked Timber / Cato Unbound). Two push races with the
site-build bot; fixed in build.yml. Lint flags legitimate noun/verb uses of
"notice" and the six rules quoted verbatim; reworded rather than exempted.
**Open questions:** in STATE.md (Orwell order HITL; Matter listen-through
HITL; word floor and sentence-shape tics AFK).
**Artifacts:** episodes/015–019, scripts/lint_script.py, SCRIPT_STYLE.md,
SKILL.md, build.yml, queue.md, STATE.md.
**Context:** Episodes 001–011 deliberately left with their echoes and tics
(Kevin has listened through Machiavellians); 012–019 are lint clean.

## [2026-08-27] — 020 Shooting an Elephant (unattended weekday Routine)

**Decisions:** Local `main` branch ref was found stale by twenty commits at
session start (HEAD was detached and current, but the `main` branch pointer
itself lagged) — the same class of issue as 26 Aug's six-commit lag, now
twenty; fixed with `git update-ref` before the pre-flight dry-run push, same
fix as last time. 020 written at 5,059 words (the STATE/SCRIPT_STYLE
5,000–6,500 target, not the leaner 2,800–3,600 figure that ships in the
Routine's own task template — the repo's dated recalibration from Kevin's
actual listening feedback took precedence over the template's stale number).
Structure: cold open a constructed defensive-medicine vignette (flagged),
then Blair's five Burma years, the elephant essay's plot beat by beat (the
"must" state, the two-thousand-strong crowd, the mask/hollow-dummy lines),
paired with the earlier A Hanging as the same trap with the audience swapped
for a schedule (the puddle-step, the dog, the "Ram!" cry silenced by the
lever rather than by anyone's decision). Steelman via Hitchens's "sadist or
automaton" worry and obedience-that-survives-disbelief, set against Whyte's
believing organization man; Jackall's look-up-and-look-around and Burnham's
power worship read in reverse geometry (officer reading the crowd, not the
crowd reading the officer). Case against in two parts: the did-it-happen
dispute (Crick's missing record, Davison's George Stuart/Katha-transfer
interview and the Rangoon Gazette's Major E. C. Kenny item) and Pavan Kumar
Malreddy's postcolonial reading (imperialist shame vs. indigenous guilt; the
crowd as undifferentiated "yellow faces"; Orwell's own "invariably the case
in the East" line as evidence against himself). Sign-off promises Notes on
Nationalism, the next unchecked Orwell candidate in queue.md.

**Verification:** All quotes from Shooting an Elephant and A Hanging fetched
and checked against orwell.ru and orwellfoundation.com full texts this
session (the mask/hollow-dummy/absurd-puppet lines, the death sequence, the
"glad the coolie had been killed" and "solely to avoid looking a fool"
closers; the puddle-step, the dog, the "Ram! Ram!" cry, the final "hundred
yards away"). Crick's skepticism, Davison's Stuart interview and Rangoon
Gazette find, and Shelden's Moulmein dates confirmed via Wikipedia's sourced
account. Hitchens's "sadist or automaton" reading and the "hated it more
bitterly" line confirmed via search summaries of Why Orwell Matters, both
attributed rather than block-quoted at length. Malreddy's authorship of
"Imperialist shame and indigenous guilt" (European Journal of English
Studies, 2019) confirmed via Semantic Scholar after the publisher page
403'd. Emma Larkin's "unintended trilogy" framing and the Burmese Days
libel/name-change detail are from solid general knowledge, not
re-verified by search this session, and are flagged here as such.

**Traps & dead ends:** Local `main` was on a stale branch ref again (see
Decisions); STATE.md's "overnight pipeline" note from 26 Aug already
diagnoses this as an artifact of how the environment checks the repo out,
not a pipeline bug, and the same `git update-ref` fix applied cleanly.
tandfonline.com 403'd on the Malreddy paper; Semantic Scholar had the
author name instead.

**Open questions:** (HITL) Orwell series order beyond Notes on Nationalism
is still a proposal in queue.md, Kevin's to confirm or reorder. (AFK) The
Routine's own outer task template still states a 2,800–3,600 word target
that contradicts STATE.md's dated 5,000–6,500 recalibration; worth updating
the template so future runs do not have to resolve the conflict themselves.

**Artifacts:** episodes/020-shooting-an-elephant.md (5,059 words, lint
clean); queue.md (020 ticked with case-against detail); this entry;
STATE.md snapshot.

## [2026-08-27] — Antidote season: 021 Hirschman, 022 Ostrom, 023 Grove

**Decisions:** Kevin: feed too cynical/dark → four antidote episodes on good
management (Hirschman, Ostrom, Grove, then Christensen at his suggestion).
Notes on Nationalism deferred (021 says so in-episode; 020 not edited).
"Question for Monday" formula dropped from the charter and linted. New lint
tics for narrator staging ("carries weight", "the pause", "this is where",
"heavy lifting", "the tell", etc.). 023's sign-off points to Christensen;
024 should point to the measurement constellation, not Orwell.
**Traps & dead ends:** Drafted as 020–022 before noticing the Routine had
already pushed 020 that morning; push rejected, rebase conflicted, reset to
origin/main and renumbered. Check `git fetch` + `ls episodes` BEFORE
numbering on any day the Routine runs. Inline heredoc Python with quotes
broke again; edit scripts go through the Write tool to the scratchpad.
Chapter headings count toward the 40-word echo window.
**Open questions:** Christensen 024 not yet written (AFK, Routine). Episodes
still 4,500–4,700 words vs the 5,000 floor (AFK). Kevin listen-through of
021–023 (HITL).
**Artifacts:** Created episodes/021–023; Modified scripts/lint_script.py,
SCRIPT_STYLE.md, queue.md, STATE.md.
**Context:** Reception verified by web search: Barry 1974 / Dowding 2000;
Agrawal 2001, Cox–Arnold–Villamayor-Tomás 2010, Araral 2014; Grove's
Hersey–Blanchard debt. Le Grand / Cooper NHS material, Ostrom lab and Lam
1998, and the Grove memory-exit / Pentium stories are from training knowledge.

## [2026-08-28] — 024 How Will You Measure Your Life (unattended weekday Routine)

**Decisions:** Local `main`'s branch ref was stale again at session start (HEAD
detached and current at origin/main, but the `main` branch pointer itself
twenty-five commits behind) — the third occurrence of this exact pattern
(26 Aug six commits, 27 Aug twenty, 28 Aug twenty-five); fixed this time with
`git checkout -B main origin/main` rather than `git update-ref`, since the
working tree was clean and the local branch was a strict ancestor of origin.
STATE.md's own open question flagged this as worth a standing fix after a
third occurrence — noting it here rather than attempting a pipeline change
unattended. 024 written at 5,191 words (the SCRIPT_STYLE/STATE 5,000–6,500
target, not the 2,800–3,600 figure in the Routine's own outer task template
this run) as the fourth and last of the antidote season, closing it out per
023's sign-off and queue.md's brief. Structure: the Grove/Celeron cold open
run to its actual end from the original 2010 HBR article's own text, then
Christensen's health as an unstated frame (heart attack 2007, lymphoma late
2009, the stroke in spring 2010 that produced the article itself, kidney
cancer, the leukaemia that killed him in 2020) rather than a plot point the
book itself foregrounds; the three-question class structure with the
Patrick Chun sidebar quote for period texture; Herzberg's noble-profession
vision; the Oxford purpose-hour bridging into resource allocation as a
life's emergent (not deliberate) strategy, with a constructed junior-doctor
example; the tools-of-cooperation/culture model and the
resources-processes-priorities outsourcing warning for children; the Sunday
basketball story run to its end for the ninety-eight-percent rule, read
against Jackall's managers from episode 001 (marginal-cost ethics as the
same "just this once" trade from the inside); jobs-to-be-done (the milkshake
study) applied to marriage. Case against in two parts: Lepore's 2014 New
Yorker critique of the parent disruption theory's evidentiary basis plus
Christensen's own defensive reaction to it (a Businessweek quote), and
named reader reviews (Russell Fox, Dorthe) on the book's unexamined
privilege and traditionalism, read through the clinician's "ask for the
denominator" lens against the book's n-of-one evidentiary problem. Sign-off
promises the measurement constellation (Ridgway/Goodhart/Campbell), not
Notes on Nationalism, per queue.md's instruction to keep the tone up.

**Verification:** The full text of Christensen's original July–August 2010
Harvard Business Review article was fetched as a PDF and read directly this
session, confirming the Grove/Celeron dialogue, the Herzberg
manager-driving-home vision, the resource-allocation and 1979-classmates
passages, the Sunday basketball story and the ninety-eight-percent line, the
humility-class material (not used in the episode), and the closing
cancer/yardstick paragraph verbatim. Christensen's health timeline (2007
heart attack, late-2009 lymphoma, 2010 stroke with expressive aphasia,
later kidney cancer, death from treatment-related leukaemia in January 2020
at 67) confirmed via Deseret News and Wikipedia. Jill Lepore's 2014 New
Yorker essay and its "profound anxiety about financial collapse... and
shaky evidence" line confirmed via search summaries of the piece and
secondary coverage (Salon, Slate, H-Net); Christensen's own "criminal act of
dishonesty ... at Harvard of all places" response confirmed via a
Digital Clarity Group piece quoting his Businessweek interview (the direct
Bloomberg source 403'd). The milkshake/jobs-to-be-done marriage quote and
the resources-processes-priorities parenting framework are corroborated by
multiple independent summaries (Shortform, Medium, and others) rather than
one primary source read in full this session, and are flagged here as such.
Russell Fox's and Dorthe's reviews were read via a Goodreads fetch this
session, quoted directly and attributed by name.

**Traps & dead ends:** First lint pass came back with 8 repeats and 14 tics
— mostly parallel "How can I be sure..." question structure copied too
close to the source article's own repetition, a repeated "two thousand and"
date sequence in the health paragraph, and several banned tics ("most
important" used three times, "load-bearing," "sharpest," "notice" as a
verb, "which is exactly," em-dash-adjacent contrastive framing). Fixed by
rewording each instance rather than deleting the check; used the extra
editing pass to also deepen four chapters (Oxford purpose-hour, the
resources-processes-priorities framework, Christensen's own reaction to
Lepore) and bring the draft from 4,644 words up to the 5,000-word floor
without padding by restatement.

**Open questions:** (HITL) Whether the antidote season landed for Kevin
(021–024) is still unjudged; a listen-through would settle it. (AFK) The
stale-local-`main` issue has now recurred three sessions running (26, 27,
28 Aug); STATE.md already flagged a standing fix as worth doing after a
third occurrence, and this is that occurrence — worth investigating why the
environment's checkout leaves the branch pointer behind HEAD, rather than
re-applying the same session-local fix a fourth time. (AFK) The Routine's
outer task template still states a 2,800–3,600 word target against
STATE/SCRIPT_STYLE's 5,000–6,500; this is now the third run to resolve the
conflict in the same direction rather than the template being corrected.

**Artifacts:** episodes/024-how-will-you-measure-your-life.md (5,191 words,
lint clean); queue.md (024 ticked, antidote season closed); this entry;
STATE.md snapshot.

## 28 Aug 2026 (day) — titles, BLOOM frame, Grove ×2, constellation ×2

**Done:** Renamed all 25 episode titles to "Book (Author): what you'll
hear" (Kevin: the creative titles didn't tell him what he'd hear; the
title's job is to let him identify and choose). Added the BLOOM
applied-frame rule to SCRIPT_STYLE (Kevin: BLOOM, not the hospital, is his
hardest management situation; but "not lots of BLOOM every episode",
advice goes there where relevant). Wrote 025 Only the Paranoid Survive, 026
Grove on medicine, 027 + 028 the measurement constellation as a two-parter.
Re-pointed 024's sign-off to 025. Pushed.

**Verification:** Grove facts checked this session against the Fortune
1996 cover story (PSA 5 → 6.0/6.1, 15+ physicians, HDR implant + 28
external doses in Seattle, the fact-checker's arithmetic catch), JAMA 2005
abstract page (Moore's-law vs war-on-cancer framing, 15–20% EHR figure,
≈10% NIH / $2.8B biomarker ask, translational hospitals, Medicare data
standard), Forbes Jan 2008 (Parkinson's numbers, At Home Box, Bankiewicz,
Amgen GDNF), VentureBeat Nov 2007 (Hamilton/Vioxx), Science.org index of
Lowe's "Rich, Famous, Smart and Wrong" and "A Note to Andy Grove" (bodies
403'd; content from secondary summaries), Kirkus on Swimming Across,
Commoncog on Paranoid, Fortune Oct 2025 Intel-culture reporting, CNN/
TechTarget on Otellini–iPhone and Gelsinger. Constellation: Bevan & Hood
2006 PDF read directly (8-minute spike, 23%→5.3%, 139/158 vs 69%, NAO 2001
nine trusts/6,000 records, Nove 1958 "105 not 125", four motivations,
random-audit remedy); Goodhart 1975 wording and Strathern 1997 attribution
via Wikipedia/Chrystal-Mizen summaries; Campbell law statement and 1976/
1979 venues via Wikipedia + ERIC; Ridgway's single/multiple/composite
structure via the Policy & Society review. **Not verified this session,
from training knowledge:** Ridgway's exact case list beyond Blau and
Berliner; Seidman & Couzens as the DC source; CAST dates; QOF exception-
reporting audit findings; Propper et al. results; HITECH ≈$25B and >90%
adoption. All stated at the level of confidence they deserve.

**Traps:** Lint first passes: 025 16 repeats/10 tics, 026 13/6, 027 8/2,
028 15/5 — all reworded, none deleted. 027 came in at 3,510 words; added a
"law in a white coat" chapter (CAST, QOF, citation metrics) rather than
pad. Bash heredoc rule respected: every multi-replacement edit went through
a Write-tool script.

**Open:** (HITL) Kevin has not yet listened to 025–028; whether the BLOOM
aside density is right is his call. (AFK) The Routine template's word
target still conflicts with the charter (fourth run). Next for the Routine:
Normal Accidents.
