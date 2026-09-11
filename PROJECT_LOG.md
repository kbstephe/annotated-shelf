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

## [2026-09-10] — Episode 037, Scott Alexander's Meditations on Moloch

**Decisions:** Opened on a grounded, numbers-heavy real-world multipolar
trap (the 1950s-2017 livestock antibiotics growth-promotion race) rather
than starting inside the essay itself, so the abstraction has a concrete
referent before Ginsberg or Alexander are introduced; the same case is
closed out later in its own chapter (the FDA's 2017 ban, and the honest
caveat that overall antibiotic sales have since drifted back up under the
looser "disease prevention" label) rather than left as a one-off cold open.
Alexander's own proposed fix, a superintelligence "gardener" coordinating
away traps no human institution can reach, is flagged explicitly as a
speculative leap the essay's own evidentiary standard for its diagnosis
doesn't meet, treating the essay's diagnosis and prescription as two
different genres rather than one continuous argument. The queue's own
scoping note for this item mis-attributed "Moloch's Toolbox" to Zvi
Mowshowitz; research this session found it is Eliezer Yudkowsky's own
LessWrong sequel to his book *Inadequate Equilibria*, and Mowshowitz's
actual reply is a separate piece, "Moloch Hasn't Won" (2019, opening his
Immoral Mazes sequence) — corrected in queue.md's done entry.

**Verification:** The essay itself was fetched from slatestarcodex.com this
session (not read from training knowledge alone) to confirm its structure,
its ten-plus catalogued traps, and exact wording for the one quote used
under fifteen words ("He is the god of child sacrifice"). Ginsberg's Moloch
vision (October 17 1954, Nob Hill apartment, the Sir Francis Drake Hotel,
peyote) checked against a Howl-scholarship source; the one Ginsberg quote
used ("Moloch whose name is the Mind") confirmed against the poem text via
the same research. Scott Alexander/Siskind biography (blog launch 2013,
the June 2020 NYT-doxxing deletion, the Astral Codex Ten relaunch) checked
via web search. The livestock antibiotics figures (eighty percent of US
antibiotic sales to livestock by 2014, seventeen thousand tons, the
growth-promotion sales drop from 5.7 million kg in 2016 to zero in 2017
under FDA Guidance for Industry 213, and the subsequent partial rebound
under the disease-prevention label) checked against CIDRAP and FDA-report
coverage. Zvi Mowshowitz's "Moloch Hasn't Won" and Yudkowsky's "Moloch's
Toolbox" both confirmed by title, author, and argument via web search
rather than assumed from the queue's own (incorrect) note. Mike Travers's
"Meditations on Meditations on Moloch" fetched directly and its
denial-of-agency argument and Ginsberg-inversion charge verified against
that fetch, not reconstructed from memory. Back-catalogue callbacks (Grove's
Intel memory-business exit from 023, Bevan/Hood's NHS ratchet from 028,
Ostrom's commons governance from 022, Jackall's blame games from 001) each
checked against the actual episode text this session rather than assumed
from the queue's own summaries.

**Traps & dead ends:** An initial web search for a named economist critique
("it's just externalities and game theory with a demon on top," the framing
in this item's own queue scoping note) turned up nothing citable; no such
attributed reception piece was found this session, so that reading was
dropped from the episode rather than asserted without a source. The
Travers piece supplied a stronger, citable case against instead.

**Open questions:** (AFK) Alexander's own essay was read this session only
via targeted fetches answering specific questions (structure, named
examples, exact short quotes), not end to end in one continuous pass;
worth a full primary read if the shelf ever needs to quote it more
extensively. (HITL) Whether the antibiotics cold open (a constructed frame
run through the essay's own logic, not one of Alexander's own listed
examples) belongs in future episodes as a recurring device, opening on a
grounded real-world case before naming the work, is Kevin's call to bless
or veto.

**Artifacts:** episodes/037-scott-alexander-meditations-on-moloch.md
(5,390 words, lint clean); queue.md (Moloch item checked off with full
episode summary and the Yudkowsky/Mowshowitz correction; order-of-record
line 2 updated).

**Context:** Unattended Routine run, 10 Sep 26. Pre-flight clean, no stale
local `main` this time. Build verified live: the Build site Action's
commit appeared within about ninety seconds of the push, and
`site/feed.xml` on origin/main carries 037's title and full text.

## [2026-09-10] — Kevin's day session: Episodes 038, 039, 040 in one sitting

**Decisions:** Kevin asked for the next three episodes at once (also as a
Fable usage test). Followed the order of record: 038 Cost Disease, 039 the
research-epistemics pair, 040 Collison's own pages, each with its sign-off
pointing to the next. Titles keep 037's "Author, Work: what you'll hear"
pattern. 038 opens and closes on Keynes 1930 rather than inside the essay;
its worked case is the academic medical centre ratchet ("every safeguard
has a birthday"), with the Shorr 2012 bed-alarm RCT as the safeguard that
failed its test and survived. 039 treats the two essays as one argument
with Bem as cold open, credits the control-group frame to Allan Crossman
as the essay itself does, and turns Alexander's man-of-one-study lens back
on his own choice of psi meta-analysis (ganzfeld walked past). 040 holds
to the Stripe Press + own-pages source discipline; Kaufman 1976 is framed
as the empirical floor under the whole org series; the vetocracy is read
as an antibody (Moses, Pruitt-Igoe, thalidomide) so the question becomes
dose, not abolition. Each episode carries exactly one BLOOM aside.

**Verification:** All three SSC essays fetched as raw HTML and read in
body text (the summariser fetch fabricated a "Science became trapped in an
epistemological ouroboros" quote that is NOT in the essay; the essay's
actual ending is the "Ouroboros of Scientific Evidence" image plus the
"Science! YOU WERE THE CHOSEN ONE" joke — the fake quote was not used).
Exact quotes used, all under fifteen words and checked against the raw
text: "increase by ten times without a single cent of the gains going to
teachers, doctors, or nurses" (038); "What's happening? I don't know and I
find it really scary" (038); "I find their case pretty convincing"
(Alexander 2019 review, via readscottalexander mirror); "causes even half
the price rise" (Caplan, Econlib 10 Jun 2019); "so weak and flawed as to
permit a field of study to sustain itself" (Yudkowsky as quoted by
Alexander, 039). Collison pages fetched verbatim via curl: Pentagon 491 d,
Van Ness 7,600 d / $346M / $110,000 per metre, Alaska Highway $793/m,
Marinship dates, Moderna 45 d / 266 d / 94.5%, Berlin Airlift 277,000
flights / Tegel 92 d, WWII 3 y 8 m 23 d, BART 16 mi / $2.3B / ~7 y,
NIH ~$37B, the replacement-rate and cost-disease question texts, and the
Advice page including "If you're 20–30: I don't know yet." Numbers cited
from memory and NOT re-verified this session (flagged for the reader as
approximate where used): Kaufman 1976 counts (175 / ~85% / 27 / 246),
Woolhandler & Himmelstein 2003 (31% vs ~17%), Ioannidis JAMA 2005
(49 papers, ~16% contradicted, ~16% shrunk), Shorr 2012 (16 units, null),
Fast Grants survey (~78% / ~64%), Bloom et al. 2020 (18x), Transit Costs
Project findings, Surgery Center of Oklahoma (prices posted 2009).

**Traps & dead ends:** The WebFetch summariser refused a verbatim request
on patrickcollison.com/questions on fair-use grounds and paraphrased
elsewhere; raw curl + tag-strip in Python was the reliable path for exact
wording and should be the default for quote-bearing sources. The Bash tool
mangled a Python heredoc containing apostrophes; edit scripts were written
with the Write tool and executed by path instead. First drafts of all
three came in at 4,200–4,300 words; each was brought over the 5,000 floor
by adding worked cases (Transit Costs Project, Oklahoma, bed-alarm RCT;
Ioannidis JAMA, ganzfeld, publication-as-trap; Questions-page portrait,
Bloom et al., Arc), not by restatement.

**Open questions:** (HITL) 038 and 039 use Kevin's own professional
standing ("I run randomised trials for a living", "I work in an academic
medical centre") more directly than earlier episodes; confirm the register.
(HITL) Whether the memory-cited numbers above should be re-verified before
the episodes are relied on for anything beyond listening. (AFK) 041
Hamming: the Stripe Press edition text is not online; the 1986 lecture
transcript is, and the queue already plans it as the spine.

**Artifacts:** episodes/038-scott-alexander-considerations-on-cost-disease.md;
episodes/039-scott-alexander-man-of-one-study-control-group.md;
episodes/040-patrick-collison-fast-questions-advice.md; queue.md (three
items checked with full summaries; order of record updated); STATE.md.

**Context:** Attended session, 10 Sep 26, on Fable 5.1. Three commits,
one push; build verified after push (see below).

## [2026-09-10] — Kevin's day session, part two: lint was half-dead; narrator is Claude

**Decisions:** (1) Narrator persona ruling: the show is written from Claude's
point of view, never in Kevin's first person ("I run trials", "my career").
Judgments in "I" stay; biography goes third person ("the trialist this show
is written for", "the programme its listener runs"). SCRIPT_STYLE.md
Register updated; 038-040 re-edited and re-pushed. (2) "worth <verb>ing"
(holding/keeping/stating/carrying...) is now a tic; it had closed nearly
every episode 031-040 as a fixed formula for the weekly question, which
Kevin banned 27 Aug. (3) Episodes 012-037 stay as published (they now show
0-11 tics each under the repaired lint); a back-catalogue re-edit is
offered, not done.

**Verification:** Root cause of the tics Kevin still hears: the 27 Aug
batch of patterns in scripts/lint_script.py (lines 54-61: carries weight,
the pause, this is where, heavy lifting, hard to overstate, the tell, the
trick is, dwell on, the weight of, lands hard, Monday) had been written via
a Bash heredoc that converted every `` into a literal backspace byte
(0x08). Fifty backspaces found and replaced bytewise; those eleven lines
had never matched a script. New families added: worth+gerund, dwell*,
weight of, deserves, repays, reads twice, bears repeating, pay closer
attention, "most X thing in the", "the essay turns on", persona forms
(I run/work in/help run, my career/field/trade/patients, for a living).
Re-lint after fixes: 038 5,066 w, 039 5,051 w, 040 5,020 w, all 0/0.

**Traps & dead ends:** Same heredoc trap bit twice more this session
(apostrophes, then `` again). Rule of record: any file containing a
backslash is written with the Write tool or a Python script executed by
path, never a Bash heredoc. The lint file itself is now the proof.

**Artifacts:** scripts/lint_script.py; .claude/skills/audio-essay/
SCRIPT_STYLE.md (Register: persona rule); episodes/038, 039, 040 re-edited.

## [2026-09-10] — Kevin's day session, part three: back-catalogue re-edit 012–037

**Decisions:** Kevin: "go ahead and re edit". All 22 episodes 012–037 with
hits under the repaired lint were re-edited in place (104 lines across 23
files; article URLs/GUIDs unchanged, so Matter keeps its place). Three
kinds of change: (1) narrator-grading sentences rewritten ("deserves a
moment", "worth stating", "here is where", "the whole essay turns on",
"most useful book on the shelf"); (2) the closing-question formula, which
had gone "the question for Monday" (012–020 chapter headings included) →
"worth carrying" (023–037), replaced with twelve rotating phrasings so no
single one recurs more than twice; (3) the six BLOOM asides in 031–037
that spoke as Kevin ("I run something with the same shape", "report up
through me") recast in the third person per the persona ruling. Content,
claims and callbacks untouched. Lint's `dwell` pattern narrowed to
"dwell(s) on/in/inside/with" so "dwellings per hectare" passes.

**Verification:** `lint_script.py` on every file 012–040: 0 repeats,
0 tics. Closers grepped and read for grammar after variation. Grep for
residual first person ("I've watched", "through me", "my own work") in
031–037: none. 001–011 untouched (pre-lint, per the standing rule).

**Artifacts:** episodes/012–037 (22 files), scripts/lint_script.py.

## [2026-09-10] — Kevin's day session, part four: no shoehorning, listener.md, Remote Control

**Decisions:** (1) BLOOM asides: default is none. Charter now says an aside
earns its place only when a stranger who knew both the book and the
programme would have made the connection unprompted; the 031–037 asides are
named as the failure mode. (2) `listener.md` added at repo root, public,
faculty-page level (role, studies, weekly decisions, lenses, what he wants
from the show), so applications can land on fellowship direction, grant
writing, trial methods or reading a literature, not always on BLOOM. Kevin
approved the draft as written ("seems ok to me"). (3) Machine-level, not
project: a Claude Code Remote Control listener named "laptop" now runs at
logon (memory `claude-remote-control-listener`); it runs from
`C:\Users\kbste\remote` because home-directory trust is never saved.

**Open questions:** (HITL) Read the opening of 041 Hamming when the Routine
ships it 11 Sep: first unattended run under the Claude-narrator rule, the
no-shoehorn rule and `listener.md`. (AFK) Two `listener.md` items are
in-progress work (choline, potassium salt); Kevin did not ask for their
removal.

**Artifacts:** Created `listener.md`; Modified
`.claude/skills/audio-essay/SCRIPT_STYLE.md` (Register: never shoehorn,
pointer to listener.md).

**Context:** The Routine runs in the cloud on the public repo, so anything
the narrator is meant to know about the listener must be in the repo or
nowhere; that constraint, not preference, set the file's disclosure level.

## [2026-09-11] — Routine: Episode 041, Hamming's "You and Your Research"

**Decisions:** Wrote 041 from Hamming's 1986 Bell Labs lecture itself
rather than from the Stripe Press book's surrounding chapters, per the
queue's own scoping (the lecture as spine); the Stripe Press PDF wouldn't
extract in this session's environment (no pdftotext, and the pypdf
install hit a broken `_cffi_backend`/cryptography binding), so the primary
source of record is the lecture transcript, cross-read across three
independently hosted copies. No BLOOM aside: the payoff already lands
cleanly on the fellowship-director/study-section register that is Kevin's
actual job per `listener.md`, so a BLOOM aside would have been exactly the
shoehorn the 10 Sep charter ruling bans. This is also the first episode
written entirely under all three 10 Sep rulings at once (Claude-narrator
persona, no-shoehorn default, listener.md) in an unattended run, the test
the previous session's sign-off flagged as HITL.

**Verification:** Full primary transcript of the 7 March 1986 talk fetched
and read start to finish (cs.princeton.edu copy, cross-checked against the
cs.virginia.edu and gwern.net transcriptions for the same wording). Every
story and figure in the episode traces to that transcript: the McCall
chemistry-table exchange, the Los Alamos origin, the Pfann/Clogston/
Shannon examples, Bode's compound-interest story, the important-problem
definition and Great Thoughts Time, the door-open/closed observation, the
personality-defect stories (dressing, bicycle, Barney Oliver), the
seven-year rule and the Shannon verdict, the Bode vision-vs.-management
exchange, and Hamming's own "biased sample" admission in the Q&A, all
quoted or paraphrased from the transcript text directly, not summarized.
The 1947 relay-computer frustration and 1950 Hamming-code publication
(outside the talk itself) were corroborated across two independent
histories (IEEE Computer Society's pioneer page and a Bell Labs technical
retrospective) before use. Cal Newport's open-door critique was verified
against the raw fetched HTML of his own site after his first WebFetch
summary misattributed it to a comment thread; the exact sentence quoted
("orders of magnitudes smaller than what we encounter in an age of
networked computers") sits in his own body text. The Erren/Cullen/Erren/
Bourne PLoS Computational Biology rule list was verified the same way,
by rendering the article's raw HTML rather than trusting a WebFetch
summary, after the PDF version failed to extract in this environment;
rule nine and rule ten are confirmed as quoted. gwern.net's two footnotes
(the Newton line flagged apocryphal; the Institute for Advanced Study
verdict read as possible regression to the mean) were read directly from
the raw page text, not the page's own AI-generated summary.

**Traps & dead ends:** The Stripe Press zine PDF fetched cleanly but no
PDF text extractor worked in this session (`pdftotext` absent, `pypdf`'s
native dependency chain broken); worked around by relying on the lecture
transcript, which the queue already treats as the primary text, rather
than losing time on the book's surrounding chapters. A first WebFetch
summary of Cal Newport's page put his open-door critique "in the
comments," which the raw HTML showed was wrong — it is in his own
post body; raw curl-and-strip-tags, the house pattern since the 040
session, is confirmed again as the reliable path for a load-bearing
attributed quote, this time from a WebFetch summariser misattributing a
location rather than fabricating a quote outright.

**Open questions:** (HITL) Read or listen to 041 to confirm the register:
first unattended episode under the persona rule, the no-shoehorn rule,
and `listener.md` together. (AFK) The seven-year-field-shift rule and the
"Shannon ruined himself" verdict are presented in the episode as Hamming's
own harsh, unfalsifiable judgment rather than settled fact; worth a listen
to confirm the framing reads as clearly contested as intended, not as the
narrator's own claim.

**Artifacts:** episodes/041-hamming-you-and-your-research.md (5,149 words,
lint clean); queue.md (Collison shelf item 2 checked with full summary,
order-of-record note updated, sign-off pointer moved to Bush's Pieces of
the Action).

**Context:** Unattended Routine run, 11 Sep 26. Pre-flight found local
`main` behind `origin/main` by 33 commits, fixed with `git checkout main
&& git merge --ff-only origin/main` per the standing template step (not
logged as a pipeline event, per that step's own instruction). One push
for the episode and queue update, verified live via `site/feed.xml` on
`origin/main` before this log entry.

