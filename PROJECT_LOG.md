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
