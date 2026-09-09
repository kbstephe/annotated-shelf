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

## [2026-09-09] — Routine: Episode 036, Weber's "Science as a Vocation"

**Decisions:** Wrote 035's promised next episode, the first item in the
8 Sep order-of-record queue. Single-read essay format: Weber's 1917 Munich
lecture, biography threaded through as the spine (his 1898 breakdown and
fourteen-year withdrawal from teaching, the 1917 lecture delivered nineteen
years into that withdrawal, the 1919 return to a Munich chair concurrent
with drafting the Weimar constitution and a failed parliamentary run, death
by influenza-turned-pneumonia June 1920 after three semesters back in the
classroom). Content chapters: the Privatdozent/habilitation lottery (Weber's
own fast rise as counter-case); the American "state-capitalist enterprise"
mirror read against Whyte/Jackall; specialization and personality as
self-erasure; being superseded as science's goal; disenchantment defined
precisely (calculability in principle, not more actual knowledge); the
Tolstoy exchange and the Abraham/satisfied-death passage; the "many old
gods" polytheism passage; the sacrifice-of-the-intellect passage (honest
religious return ranked above dishonest private mysticism) as an added
steelman beat; what science can still do and the teacher/demagogue line; a
translation-as-craft-problem chapter (Beruf, Wissenschaft, Gerth/Mills 1946
vs. later editions) per the queue's own scoping note. Direct callback to
035's Weber-derived Merton bureaucracy as one continuous rationalization
mechanism.

**Verification:** All quoted fragments (the "mad hazard" line, "scarcely to
be borne," the millennia line, "state-capitalist enterprise" and
"quasi-proletarian existence," the Tolstoy question, the "many old gods"
passage, the sacrifice-of-the-intellect passage, the teacher/demagogue line)
were checked this session against multiple independent web sources quoting
the Gerth/Mills or Livingstone translations, since no single clean full-text
mirror was fetchable (American University's html mirror is dead, several
PDFs 403/503'd or returned unreadable binary). Biographical facts (1897
father quarrel and death, 1898 breakdown, 1903 return to writing only, 1918
Vienna trial semester, 1919 Munich chair succeeding Lujo Brentano, Weimar
constitution drafting and Article 48, Versailles delegation, failed DDP
candidacy, three semesters taught, June 1920 death at 56, the 1894 Freiburg
chair at 30) each checked against at least one independent source. The
lecture series name ("Geistige Arbeit als Beruf"), venue (Steinicke's
bookshop), organizer (Immanuel Birnbaum), and Nov 7 1917 date corroborated
across sources. Reception figures (Leo Strauss's relativism charge, Rust
and Smallpage's "performative self-contradiction" reading, Chad Wellmon's
Aeon essay on the lecture's contemporary relevance) each drawn from a
distinct secondary source this session, not from training-knowledge recall
alone.

**Traps & dead ends:** No primary full-text mirror of the lecture proved
fetchable this session (American University html mirror, Penn/Weizmann/UMN/
Harvard PDFs, panarchy.org, Pfeiffer.edu, and web.archive.org were all
unreachable, blocked, or returned unusable binary). Grounding rested instead
on convergent quotation across several independent secondary fetches per
passage, all consistent with each other and with standard editions; flagged
here rather than in STATE since the episode's own quotes are still each
independently sourced, unlike 034/035's flagged single-source items.

**Open questions:** (AFK) Because no primary full text was read end to end,
a handful of quoted fragments rest on secondary aggregation rather than a
page-checked primary read, the same caveat 035 carried for Merton's essay.
Worth a primary read of the Gerth/Mills or Owen/Strong/Livingstone edition
if the shelf ever needs to quote this lecture more extensively or precisely.

**Artifacts:** episodes/036-weber-science-as-a-vocation.md (5,169 words,
lint clean); queue.md (Weber item checked off with full episode summary;
order-of-record line 1 updated to done, line 2 now current).

**Context:** Unattended Routine run, 9 Sep 26. Pre-flight: local `main` was
one fast-forward behind `origin/main` at session start (the routine,
expected checkout artifact per the template's own step 1 note); fixed
cleanly with `git checkout main && git merge --ff-only origin/main`, no
issue to log per the template's instruction. Build verified live: the
Build site Action's commit appeared within about three minutes of the push,
and `site/feed.xml` on origin/main carries 036's title and full text.
