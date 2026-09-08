# PROJECT_LOG — The Annotated Shelf

Append-only, newest last. Entries 24 Aug – 8 Sep 2026 (Routine) are in
`archive/PROJECT_LOG_24aug26-08sep26.md` (rotated 8 Sep 26 at 96 KB).

## [2026-09-08] — Kevin's session: Routine fix, five series laid out, PubMed attached

**Decisions:** (1) Scott Alexander greenlit for three episodes after 036
Weber: Moloch, Cost Disease, the Beware-the-Man-of-One-Study / Control-Group
pair; picked for job-usefulness, not fame. (2) Five series scoped in
queue.md in this order: Collison shelf x8 (Stripe Press is the canon; the
patrickcollison.com/bookshelf page is NOT a source, 778 unranked titles and
by his own note ten years stale), nutrition science x9, science as an
institution x10 (Kuhn in three parts at Kevin's instruction), how evidence
was invented x8, doers x11 (eight subjects, three two-parters). Nutrition
and evidence approved "as a start", so re-ordering within them is allowed.
(3) Proximity rule: episodes touching Kevin's own work (nutrition 5 and 8,
doers 8 and 11) use the published record only; Kevin declined to steer them
for now. (4) Routine template step 1 now fixes a stale local main with
`git checkout main && git merge --ff-only origin/main` (fallback
`checkout -B`) and tells the Routine not to log it. (5) PubMed connector
attached to the Routine (8 Sep, before the nutrition series rather than
waiting for it). (6) Kevin authorised the push of the seven layout commits.

**Traps & dead ends:** The STATE open question about the Routine template's
2,800–3,600 word target was stale: the template had said 5,000–6,500 since
30 Aug. Three Routine sessions carried the note forward without checking
the template itself. Lesson: check the Routine with `RemoteTrigger get`
before repeating a claim about it. Also: two apparent missed runs (29 Aug,
5 Sep) were Saturdays, not failures.

**Open questions:** (HITL) Kevin has still not listened past 024; whether
the antidote season, the BLOOM aside density, and the unattended episodes
land is unjudged. (HITL) Whether the essays turn / Orwell series ever resume
after the five series (they are below the new series in queue order).
(AFK) First run with PubMed attached and the new branch-fix wording is
9 Sep; if 036 does not appear, read the run log before blaming either.

**Artifacts:** queue.md (Order of record block; Scott Alexander scoped;
five series sections; candidate list marked chosen); STATE.md (snapshot,
two stale AFK items resolved); Routine trig_017rhfD6LEfWxb4R7pgTuVTz
(step 1 text, mcp_connections = PubMed); memory
annotated-shelf-podcast.md (pointer refresh); this entry. Also: Kevin
asked for two paperbacks for his Saturday Sierra Leone trip; recommended
Goldberger's War (Kraut) and Skunk Works (Rich), alternate Wind, Sand and
Stars. Not a project decision.

**Context:** Kevin's brief for the new series: "we've done a lot on orgs
etc and I am interested in a new series", with Patrick Collison's
recommendations and nutrition-science history as his two ideas. The layout
covers roughly ten weeks of weekday runs. Local main was 21 commits behind
at session start; fast-forwarded with `git merge --ff-only`.
