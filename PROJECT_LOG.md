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

## [2026-09-14] — Routine: Episode 042, Vannevar Bush's "Pieces of the Action"

**Decisions:** Wrote 042 from Bush's 1970 memoir as an organizational-design
manual rather than a war history, per the queue's own scoping. Structured
as a chain of three worked cases proving one mechanism generalizes: the MIT
Radiation Laboratory (radar), Section T/the Applied Physics Laboratory (the
proximity fuze), and OSRD's Committee on Medical Research (penicillin's
deep-tank fermentation at Pfizer) — three unrelated fields, three different
committee chairmen, the identical contract-not-conscription arrangement,
each landing a working answer inside the same wartime clock. Cold open used
Bush's own WWI submarine-detector failure (built the tech, no liaison to
get the Navy to use it) as the seed of the whole argument rather than the
more obvious 1940 Oval Office scene, which instead opens chapter two. Kept
"Science, The Endless Frontier" to a single pointer paragraph, per the
queue's explicit instruction that it belongs to series 4 item 1, not here.
No BLOOM aside: the genuine landing point was study-section grant review
(Bush-vs-Kilgore replayed on every scored R01), already Kevin's own
register per `listener.md`, so a second applied frame would have been the
shoehorn the charter bans — same call 041 made the episode before.

**Verification:** Primary-source access to the book itself failed this
session (the Internet Archive scan has no readable text or lending copy
available via fetch); grounded instead on two independent secondary
sources that each quote and paraphrase the book directly and corroborate
each other on the same material — Ari Wagen's review (the "general's hat"
quote, the NDRC/pyramid-vs-loose-structure argument, both Pyke stories in
detail, the tyro/amateur distinction, "inventions are a dime a dozen") and
a Roots of Progress compilation of direct memoir quotes (the "resignation"
episode, "the hell with the credit," the patent-and-invention material).
Historical facts around the book (Tizard mission date, magnetron origin,
Rad Lab output figures, Section T's move from Carnegie DTM to Johns
Hopkins APL, the CMR/Richards/Florey October 1941 meeting, Pfizer's deep-
tank fermentation and Brooklyn plant dates, the June 1940 FDR one-page
memo) were cross-checked across multiple independent aggregator sources
(historical societies, university and lab histories, a WWII-technology
history site) rather than a single source each. Reception/case-against
grounded on three separate secondary treatments read directly this
session: Kealey's crowding-out argument (via summaries of "The Economic
Laws of Scientific Research"), Larry Owens's 1994 Business History Review
"Counterproductive Management of Science" (abstract read directly,
full text paywalled), and multiple sources on the Bush-Kilgore fight
(patent policy, the 50%/100% overhead split, the ~15-institution
concentration complaint). No full primary read of "Pieces of the Action"
itself happened this session; flagged below.

**Traps & dead ends:** The Internet Archive listing for the book (Boston
Public Library scan, 396pp) shows metadata only, no readable text or
lending option reachable this session, so no primary-text verification of
any quote was possible; every quote used was already independently
verified as a direct quotation by a secondary source (Wagen, Roots of
Progress), matching the standard the last several episodes used when a
primary text was unreachable. A first attempt to fetch a Cambridge Core
review page and the Stripe Press book page directly worked for the latter
but 403'd for the former (`online.ucpress.edu`); the Owens argument was
sourced from the openly available abstract instead.

**Open questions:** (AFK) "Pieces of the Action" itself was never read in
primary form this session; every specific Bush quote and story used rests
on independent secondary-source corroboration (Wagen's review and Roots of
Progress's compilation agreeing on the same material) rather than a
page-checked primary read, the same caveat already on record for several
earlier episodes when a primary text wasn't fetchable. Worth a primary
read via Internet Archive's lending system (not reachable by fetch tools
this session, may work through an actual borrow flow) if the shelf ever
needs a more precise quotation from the book. (HITL) Whether the executing-
vs-innovating organizational distinction, reused here as the closing
generative question, lands as freshly as it did structuring 041's Great
Thoughts Time material, or starts to feel like a repeated device across
the Collison shelf's first three episodes — worth a listen to judge.

**Artifacts:** episodes/042-vannevar-bush-pieces-of-the-action.md (5,138
words, lint clean); queue.md (Collison shelf item 3 checked with full
summary, order-of-record note updated, sign-off pointer moved to Braben's
Scientific Freedom).

**Context:** Unattended Routine run, 14 Sep 26. Pre-flight found local
`main` behind `origin/main` by 36 commits, fixed with `git checkout main
&& git merge --ff-only origin/main` per the standing template step (not
logged as a pipeline event, per that step's own instruction). One push for
the episode and queue update, verified live via `site/feed.xml` on
`origin/main` before this log entry.

## [2026-09-15] — Routine: Episode 043, Donald Braben's "Scientific Freedom"

**Decisions:** Corrected an author-name error inherited from 042's own
sign-off, which named "David Braben" (the Elite/Frontier video-game
designer, a different person); the book's actual author is the physicist
Donald W. Braben. Episode text uses the correct name throughout; 042's
already-published text is left as is per the shelf's own no-rewrite rule,
and the correction is recorded here and in queue.md instead. Structured
the episode as: the March 1990 BP phone call ending Venture Research as
cold open; Braben's Planck Club claim (roughly three hundred paradigm-
resetting scientists a century) grounded concretely in Barbara
McClintock's documented thirty-year gap between her 1950 jumping-gene
result and her unshared 1983 Nobel, rather than left as an assertion; the
face-to-face, no-proposal selection method and its two questions; the
funded portfolio's genuine range, from Clough and Horsewill's obscure
Nottingham methyl-tunneling physics (1989-92) and Poliakoff's supercritical
chemistry (two decades ahead of green chemistry having a name) through
Dijkstra (twelve years funded) and Nobel laureate Dudley Herschbach; the
1990 closure read as a structural fragility (one executive's political
cover, no institutional memory to fall back on) rather than Braben's own
framing of it as simply a company losing its nerve; his post-BP UCL
continuation (Nick Lane) read as a tacit concession that the model still
needs ordinary peer review downstream once work stops looking strange.
Case against, three lines held to the charter's steelman-before-critique
order: Steven Hill's (Director of Research, Research England) published
demographic count against Braben's own refusal to disclose it; José Luis
Ricón's (Nintil) evaluation-methodology critique (self-graded results, no
counterfactual); the scale arithmetic against NIH-size funding, plus the
ARPA/FRO counter-examples this item's own queue scoping asked for, against
Braben's own on-record dismissal of the UK's ARIA as mistaken for keeping
any milestone at all. Bush callback (042): both writers need a filter for
the genuine outlier versus the confident crank, but Bush trusted
institutional embedding where Braben trusted one man's face-to-face read
of a stranger, framed as a genuinely different mechanism rather than a
smaller version of Bush's, to avoid re-running 041/042's executing-vs-
innovating device a third time running. No BLOOM; landed instead on the
fellowship director's own judgment call (per listener.md) of how much
unstructured runway to give a trainee on a conversation alone, with Hill's
diversity critique folded into that ending as the same mechanism's own
blind spot at the smaller scale, not just Braben's.

**Verification:** No primary read of "Scientific Freedom" itself this
session (see Open questions). Every claim about the book's contents and
Venture Research's mechanics is corroborated across at least two
independent named sources: José Luis Ricón's Nintil review, a LessWrong
review, Steven Hill's own site, an AEI long-form Q&A with Braben carrying
direct quotes, a Stripe Press publisher description, and an interview
transcript (jameshk.com) whose OCR mangled "Dudley Herschbach" to "George
Lee Hirschbach" but independently confirms the same funded-laureate claim
Ricón's review makes under the correct name. McClintock's 1950/1983 dates
and Nobel details, the Clough/Horsewill methyl-tunneling publication
record (Nottingham, 1984-1992 span), and the DARPA/Moderna mRNA and
Focused Research Organization facts were all checked directly via
targeted web search this session rather than asserted from training
knowledge alone. The total Venture Research budget (roughly twenty million
pounds/dollars over ten years) and researcher count (thirty to forty) were
stated with the hedge the sources themselves warrant, since aggregator
summaries disagree on the exact researcher count.

**Traps & dead ends:** Considered opening on Harry Kroto's buckminsterfullerene
discovery, which several aggregator summaries loosely credit to Venture
Research; checked directly and found the actual 1985 Nobel-winning
experiment was a Rice University collaboration with no confirmed Venture
Research funding line, only earlier, separately-funded Kroto astrochemistry
work at Sussex that motivated it. Dropped the claim entirely rather than
use a popular but unverifiable attribution. Two source fetches 403'd
(RAND's own report page, ucl.ac.uk) and one 503'd (Idea Machines podcast
transcript); worked around with corroborating sources instead of leaving
the claims unverified.

**Open questions:** (AFK) "Scientific Freedom" itself was never read in
primary form this session; every claim about its contents rests on
independent secondary corroboration (reviews, an author interview and
Q&A, the publisher's own description) rather than a page-checked read,
the same caveat now on record for several earlier episodes. (HITL) 043
drops the study-section/grant-committee register 041 and 042 both landed
on, in favor of an individual fellowship-mentorship judgment call, partly
to answer the open question on record about that device recurring a third
time; worth a listen to judge whether the new register lands as a genuine
widening or as a strained pivot away from a frame that still fit. (AFK)
The exact total researcher count for Venture Research is reported
inconsistently across sources (some say roughly thirty, others roughly
forty); the episode uses "three or four dozen" to stay honest to that
spread rather than pick one figure.

**Artifacts:** episodes/043-donald-braben-scientific-freedom.md (5,071
words, lint clean); queue.md (Collison shelf item 4 checked with full
summary and the author-name correction noted, order-of-record note
updated, sign-off pointer moved to Waldrop's The Dream Machine, part one).

**Context:** Unattended Routine run, 15 Sep 26. Pre-flight found local
`main` already current with `origin/main` (no fast-forward needed this
time). One push for the episode and queue update, verified live via
`site/feed.xml` on `origin/main` before this log entry.

## [2026-09-16] — Routine: Episode 044, J.C.R. Licklider, The Dream Machine, Part One

**Decisions:** Wrote 044 from Waldrop's book as an essay-format single read
of Licklider's own ARPA IPTO tenure (1962-64), reserving Xerox PARC and the
Alto for part two per the queue's own scoping. Cold open: the April 1963
"Members and Affiliates of the Intergalactic Computer Network" memo, four
isolated machines that could not exchange a character, with its own buried
line ("to bring into being the technology that the military needs") kept as
the tension the episode returns to rather than resolved early. Central
chain: SAGE's light-pen consoles as the origin of Licklider's man-machine
conviction; "Man-Computer Symbiosis" (1960) built from his own 85-percent
time-study and the fig-tree/wasp symbiosis-vs-automation distinction; hired
to run ARPA's "Command and Control Research" office, October 1962, and
renaming it the Information Processing Techniques Office on arrival, a
bureaucratic act that redirected Cold War money toward the most basic
research he could find; the funded portfolio (Corbató/CTSS/Project MAC,
McCarthy's Stanford AI lab via the 1956 Dartmouth workshop, Berkeley's
Project Genie, Engelbart's Augmentation Research Center) as computer
science funded into existence before the field had a name. Succession as
the spine and the episode's actual widening move: Licklider names Ivan
Sutherland as his own successor before leaving for IBM in 1964, Sutherland
hands to Robert Taylor, whose three-mismatched-terminals irritation becomes
the actual ARPANET in 1969; Wes Clark's resistance (keeping Washington
University in St Louis, Licklider's own undergraduate school, off the
network for years) as the case that participation had to be a funding
condition, not a favor. Landed on a program officer's harder bet, chosen
deliberately to avoid a fourth straight recurrence of 041-043's fellowship-
director-runway frame: not how much rope to give one promising trainee, but
who gets trusted to keep making the same unglamorous call once the current
director's own term ends, with DARPA's present fixed-term program-manager
model as the mechanism's institutionalized descendant. Direct callback to
040's own Kaufman/Collison replacement-rate question, answered more fully
here than anywhere earlier on the shelf.

**Verification:** "Man-Computer Symbiosis" (1960) itself was not read
end to end this session; its content (the fig-tree opening, the 85-percent
time study, the battle-planning example, the mechanically-extended-man
versus automation distinction) was reconstructed from a targeted fetch of a
page quoting substantial passages plus independent secondary confirmation
of the automation/symbiosis distinction, and the two direct quotes used
("getting into a position to think"; the fig-tree/wasp opening described in
paraphrase) are both under the fifteen-word limit. The April 1963
"Intergalactic Computer Network" memo was fetched in two forms this
session, a PDF that would not extract cleanly and a hosted transcript
(thekurzweillibrary.com) that did; the quote used ("to bring into being the
technology that the military needs") is verified against that transcript
directly. Licklider's own "It really wasn't a command and control research
program. It was an interactive computing program" is a direct quote from
his own oral history, confirmed via independent secondary citation this
session. Larry Roberts's "The vision was really Lick's originally" and
Robert Taylor's description of Licklider as "the most unlikely great man"
were each checked against independent sources this session rather than
recalled from training knowledge alone. Biographical facts (1915 St Louis
birth, Baptist minister father, Washington University in St Louis and
Rochester PhD, 1950 MIT Acoustics Lab, 1957 move to BBN, SAGE human-factors
role) and institutional facts (ARPA's 1958 founding after Sputnik, the
Command and Control Research charter, the October 1962 hire, Project MAC's
July 1963 two-million-dollar contract, Corbató/CTSS/Multics, McCarthy's
1956 Dartmouth workshop and 1962 Stanford move, Engelbart's October 1962
report and his own 1950 origin story, Sutherland's 1964 succession at
twenty-six, Taylor's three-terminal frustration and 1966 budget, the 29
October 1969 first message crashing after "LO," the 1971 growth to fifteen
nodes, Licklider's 1964-67 IBM period and 1968-70 Project MAC directorship,
his 1974 return to IPTO, and his 1990 death) were each checked against at
least one independent source this session (Britannica, IEEE Computer
Society, Computer History Museum, historyofcomputercommunications.info,
and others), not asserted from training knowledge alone. Paul Edwards's
"The Closed World" reading of "Man-Computer Symbiosis" as Cold War
closed-world/cyborg discourse tracing to the Macy Conferences, Janet
Abbate's social-construction critique of great-man ARPANET histories, and
the Wes Clark/Washington University resistance anecdote from Hafner and
Lyon's "Where Wizards Stay Up Late" were each verified via targeted search
this session rather than assumed. DARPA's current fixed-term (three-to-
five-year) program-manager model was checked directly rather than assumed
to still hold.

**Traps & dead ends:** The Licklider memo PDF (worrydream.com) would not
extract as text (FlateDecode-compressed, binary only); the hosted
transcript at thekurzweillibrary.com supplied the verified quote instead.
No other major dead ends this session; research converged quickly on
well-documented computing-history sources.

**Open questions:** (AFK) "Man-Computer Symbiosis" and "Libraries of the
Future" were both read this session only via targeted fetches and
secondary quotation aggregation, not as full primary texts end to end;
worth a full primary read of the 1960 paper if the shelf ever needs to
quote it more precisely. (HITL) This is the fourth of five Collison-shelf
episodes running (041-044) to land at or near a research-funding/mentorship
register; 044 deliberately varied the frame to succession rather than
per-trainee runway to answer that recurrence directly, but whether the
shift reads as a genuine widening or as the same well being revisited a
fourth time is worth a listen to judge, especially set against 043's
identical worry about a third recurrence.

**Artifacts:** episodes/044-licklider-dream-machine-part-one.md (5,152
words, lint clean); queue.md (Collison shelf item 5 checked off with full
summary, order-of-record note updated, sign-off pointer moved to The Dream
Machine, part two).

**Context:** Unattended Routine run, 16 Sep 26. Pre-flight found local
`main` three commits behind `origin/main`, fixed cleanly with `git checkout
main && git merge --ff-only origin/main` per the standing template step
(not logged as a pipeline event, per that step's own instruction). One
push for the episode and queue update, verified live via `site/feed.xml`
on `origin/main` before this log entry.


## [2026-09-17] — Episode 045, Robert Taylor, The Dream Machine, Part Two

**Decisions:** Landed the episode on a measurement register (which ledger an
organization reads when judging whether strange research paid off) rather
than a fifth funding/mentorship frame, the deliberate widening 044's own
open question asked for after four straight Collison-shelf episodes in a
row on grant-review and fellowship registers. No BLOOM aside; the one
generic monitoring-data image in the close (a reviewer reading the dramatic
number instead of the one paying for the operation) was kept unnamed rather
than tied to the programme, since naming it would have been the shoehorn
the charter bans and the general form did the same work.
**Verification:** Every date, dollar figure, and named person in the episode
was checked against at least one independent source this session (the
Mansfield Amendment's 1969 passage and its effect on ARPA-funded computer
science; Robert Taylor's 1965-69 IPTO tenure and 1970 move to Xerox; the
Berkeley Computer Company's 1970 collapse and its staff's move to PARC en
masse; George Pake's refusal to give Taylor a formal manager title; Gary
Starkweather's 1971 transfer and the SLOT prototype; Bill English's 1971
move from Engelbart's ARC to PARC and the rebuilt mouse; Alan Kay's 1972
Dynabook proposal and the "invent the future" line's contested but
Kay-confirmed origin; the Alto's 1973 build, ~$12,000-per-unit parts cost
per Thacker, and ~2,000 units with none sold; Ethernet's May/November 1973
dates and the 1976 patent's four named co-inventors; the Xerox 9700's 1977
release; Grapevine as an early networked email system; the two 1979 Apple
visits to PARC (Jef Raskin's first, Jobs's second) and the $1M pre-IPO
stock trade; Adele Goldberg's "kitchen sink" objection; the Star's 1981
price and ~25,000-unit sales figure through 1985; Tesler/Simonyi/Metcalfe/
Warnock/Geschke's respective departures; Taylor's 1983 "I quit" exit and
the CSL walkout to DEC's new Systems Research Center). Taylor's own quote
crediting Licklider as "the father of it all" is a direct quote from a
Charles Babbage Institute oral history, confirmed this session rather than
recalled from training knowledge. Malcolm Gladwell's "Creation Myth"
reassessment and the digitaltonto.com counter-read of the standard "Xerox
fumbled the future" parable were both checked directly rather than assumed.
Michael Hiltzik's "Dealers of Lightning," named in queue.md as the episode's
companion source, was not read end to end this session; its parts-bin
argument about Engelbart's own borrowed inventions was confirmed via
independent secondary sourcing on Engelbart's and English's own moves, not
a page-checked primary read of the book itself.
**Traps & dead ends:** A search for a Maze War / multiplayer-game detail at
PARC turned up a murkier attribution (the game originated at NASA Ames on
an Imlac, ported to the Alto only in 1977 by researchers other than the
ones this episode already names) than the confident single-lab-invention
version the detail would have needed to earn its place; dropped rather than
stretched to fit. No other major dead ends; research converged quickly on
well-documented computing-history sources, several already partly covered
by 044's own research pass.
**Open questions:** (AFK) "Dealers of Lightning" itself was never read in
primary form this session, only via independent secondary sourcing of its
specific claims; worth a primary read if the shelf ever needs a more
precise Hiltzik quotation. (HITL) This is the first Collison-shelf episode
since 040 to land outside a funding/mentorship register; worth a listen to
judge whether the measurement-ledger frame reads as a genuine widening of
the shelf's running concerns or as a plausible-sounding but disconnected
one-off, especially set against 044's own explicit worry about a fourth
straight recurrence.
**Artifacts:** episodes/045-dream-machine-part-two-xerox-parc.md (5,024
words, lint clean); queue.md (Collison shelf item 6 checked off with full
summary, order-of-record note updated, sign-off pointer moved to Gurri's
The Revolt of the Public, 046).
**Context:** Unattended Routine run, 17 Sep 26. Pre-flight found local
`main` six commits behind `origin/main`, fixed cleanly with `git checkout
main && git merge --ff-only origin/main` per the standing template step
(not logged as a pipeline event, per that step's own instruction). One push
for the episode and queue update, verified live via `site/feed.xml` on
`origin/main` before this log entry.

## [2026-09-18] — Episode 046, Martin Gurri, The Revolt of the Public

**Decisions:** Left the Collison shelf's computing-history run entirely for
a media/information-theory book, the shelf's own item 7 scoping. Cold open
on Wael Ghonim's anonymous "We Are All Khaled Said" Facebook page and
Mubarak's 11 February 2011 resignation rather than on Gurri himself, so the
book's explanatory power shows before its author does. Widened past the
book's own two editions (2014, 2018) into a case neither could have used,
the WHO's 2020 "infodemic" coinage and the CDC/WHO mask-guidance reversal,
as the generative widening the queue's own public-health scoping note
called for; kept the closing application fully generic (a district health
office, no programme named) per the no-shoehorn default, since the queue
note authorized a public-health read but not a BLOOM-specific one. Used
one callback to episode 002's accountability sinks (Davies) where the
mechanism genuinely inverts it: sinks hide accountability inside an
institution, the fifth wave routes a public around the institution's own
account entirely. Landed the verdict on Gurri's own 2024 "ten years on"
essay (DOGE, Milei, Le Pen/AfD exclusion, Romania's nullified election)
against this shelf's running funding-side question, left open rather than
resolved, of whether lost institutional trust can be rebuilt by
demonstration the way Bush's peer-review structure was.
**Verification:** Checked directly this session: Gurri's biography (born
Havana 1949, arrived Miami October 1960, twenty-nine years at the CIA's
Open Source Center, director of research, 2014 self-publish, 2018 Stripe
reissue); Ghonim's page and arrest timeline (page created June 2010,
arrested two days into the protests his own event page called for on 25
January 2011, released 7 February after eleven days, Mubarak resigned 11
February); the Bay of Pigs/Kennedy 83-percent approval figure; Abu Ghraib
(2004) and WikiLeaks's 2010 releases (Collateral Murder in April, Manning's
arrest in May, Cablegate in November, Manning's 35-year sentence); Santelli's
19 February 2009 CNBC rant and the ten-day gap to the first Tea Party
rallies; the Five Star Movement's October 2009 founding; Bouazizi's 17
December 2010 self-immolation and 4 January 2011 death; the Indignados'
15 May 2011 Puerta del Sol occupation and Podemos's January 2014 founding
out of it; Brexit (June 2016) and Trump's election; the WHO's Tedros
"infodemic" quote (15 February 2020, Munich) and the term's 2003 coinage;
the CDC's February-to-April 2020 mask-guidance reversal. Scott Alexander's
and Noah Smith's reviews were read directly this session, not recalled,
and their objections (tribal re-consolidation of trust; 1789-1848 and
1960s-70s precedent; undercounted elite accomplishments) are drawn from
the reviews themselves rather than paraphrased from memory. The third
case-against line (calling a correct diagnosis "nihilism" flatters elites)
is the narrator's own argument, not attributed to a named critic, and is
flagged as such in the episode.
**Traps & dead ends:** An early draft placed Ghonim's arrest twelve days
before his own event page's protest date; the actual sequence is the
reverse, arrested two days after the protests he had called for began,
caught and corrected before publication. A Daphni Leef tent-protest
attendance/approval figure sourced only from a secondary review summary
was dropped rather than stated as a precise number the session could not
independently verify.
**Open questions:** (HITL) 046 drops the funding/mentorship register
entirely for an information-and-legitimacy one, the widest departure yet
from the shelf's first six Collison-shelf episodes; worth a listen to judge
whether the shelf-level pivot reads as a deliberate widening (queue.md's
own item 7 scoping) or as a break in the shelf's throughline. (AFK) Gurri's
book itself was read this session only through targeted research on its
specific claims, named terms, and case studies, not as a full primary
text end to end; worth a full primary read if the shelf ever needs a more
precise quotation. (AFK) The Daphni Leef tent-protest figures were dropped
for exactly this reason; worth checking primary Israeli press coverage if
that protest ever needs harder numbers.
**Artifacts:** episodes/046-gurri-revolt-of-the-public.md (5,086 words,
lint clean); queue.md (Collison shelf item 7 checked off with full
summary, sign-off pointer already pointing to Munger, item 8, unchanged).
**Context:** Unattended Routine run, 18 September 2026. Pre-flight found
local `main` detached and nine commits behind `origin/main` (a HEAD-detached
variant of the usual stale-ref artifact); fixed with `git checkout main &&
git merge --ff-only origin/main`, per the standing template step, not
logged as a pipeline event. One push for the episode and queue update,
verified live via `site/feed.xml` on `origin/main` before this log entry.

## [2026-09-21] — Episode 047, Charlie Munger's The Psychology of Human Misjudgment, closing the Collison shelf

**Decisions:** Wrote 047 from the fully revised 2005 text of Munger's talk
(the version Stripe Press published as an appendix to Poor Charlie's
Almanack, licensed and hosted verbatim by fs.blog with Peter Kaufman's and
Munger's own permission), not the shorter 1995 Harvard version, per this
item's own queue scoping. Cold open and mid-episode payoff both built
around one case Munger tells about himself: an unnamed aircraft maker's
FAA-style evacuation certification test, run twice in one dark hangar on
the same elderly volunteers, roughly forty serious injuries and one
permanent paralysis across both runs, used as Munger's own demonstration of
"lollapalooza tendency," several mild shortcuts compounding into one
severe outcome. Selected five tendencies for full worked treatment rather
than enumerating all twenty-five, per the charter's ban on list-reading
aloud: reward-and-punishment superresponse, doubt-avoidance paired with
inconsistency-avoidance, social proof paired with authority-misinfluence,
reciprocation, and reason-respecting tendency, each carrying at least one
of Munger's own named cases rather than a restated definition. Flagged the
Kitty Genovese bystander-count as the popular, since-corrected version
Munger's own retelling repeats, rather than silently reusing the debunked
thirty-eight-witness figure as fact. Case against, the three lines this
item's own queue scoping named: hindsight, built as the narrator's own
argument from Munger's own Q&A concession that the twenty-five tendencies
overlap and could be organized differently ("The answers are yes, yes, and
yes"); Gerd Gigerenzer's fast-and-frugal-heuristics critique, that calling
a shortcut a bias assumes an idealized rational alternative that actually
performs worse in real, uncertain environments; and Munger's own record,
the Wheeler, Munger & Co. partnership's 1973-74 peak-to-trough drawdown of
over fifty percent from a leveraged, concentrated bet, plus the
self-admitted 2021-22 Alibaba mistake at Daily Journal Corporation ("I
regard Alibaba as one of the biggest mistakes I ever made"). Verdict closed
out the eight-episode Collison shelf by naming what each of the other seven
answered institutionally (Bush's peer review, Braben's one-man patronage,
Licklider's named successors, Taylor's collapse without one, Gurri's broken
information monopoly) against what Munger's checklist answers instead: not
which institution to trust, but what a single mind can do alone, portable
precisely because it needs no institution and therefore catches nothing
when its user's attention lapses, the same gap Munger's own worst mistakes
fell through. No BLOOM aside; the checklist's own individual-cognition
register never pointed toward the programme without a stretch, so none was
forced.

**Verification:** The talk itself was read directly this session, start to
finish, from raw HTML fetched and stripped by hand (not a WebFetch summary,
after two earlier summarizer calls on the same page returned incomplete or
inconsistently ordered accounts of tendencies 13-25, a repeat of the house
lesson from 040's Collison-page fetches: raw curl-and-strip is the reliable
path for a text this long and quote-bearing). Every tendency, example, and
short quote used in the episode (the Federal Express night shift, the Xerox
commission story, the gall-bladder surgeon, the Westinghouse accounting
collapse, Darwin's disconfirmation habit, Planck and Einstein, Franklin's
small-favor trick and its Korean War application, the Milgram twenty-six-
of-forty figure, Cialdini's zoo experiment and its Watergate application,
Sam Walton's no-favors rule, Carl Braun's who/what/where/when/why rule, the
photocopier-line experiment, the Munger family dog, the Belridge Oil
mistake, the Carly Fiorina hiring critique, and the Q&A's tautology
admission) traces to that same direct read of the primary text. Munger's
biography (Omaha 1924, Army Air Corps meteorology at Caltech, Harvard Law
1948, the 1959 Omaha dinner with Buffett, Berkshire vice chairman from
1978, death 28 November 2023 at 99, the tenure fact checked to confirm it
ran his full working life though the death date is not used in the episode
itself) was checked against independent sources this session (CNBC's
obituary coverage, Caltech's own alumni page). The Milgram twenty-six-of-
forty figure and its context (24 experimental conditions, an average
obedience rate near forty-three percent across all of them, not the
headline sixty-five percent alone) and the Kitty Genovese bystander-count
correction (the New York Times's own 2016 acknowledgment that the original
thirty-eight-witness account was overstated) were both checked directly
this session rather than taken from Munger's own retelling. The Wheeler,
Munger & Co. 1973-74 drawdown figures (down 31.9 percent in 1973, a further
31.5 percent in 1974, a 53.3 percent peak-to-trough loss driven by a
leveraged stake in New America Fund and Blue Chip Stamps) and the Alibaba
mistake (Daily Journal's 2021 buildup, the 2022 halving of the position,
Munger's own quoted admission at that firm's annual meeting) were each
checked against independent financial-press coverage this session, not
recalled from training knowledge alone. Gerd Gigerenzer's fast-and-frugal-
heuristics program and its specific objection to labeling a shortcut a
bias against an idealized rational baseline were checked directly against
his own published framing, not assumed from a general sense of the
behavioral-economics debate.

**Traps & dead ends:** Two early WebFetch-summarized passes over the same
fs.blog transcript (once trying to extract tendencies 13-25 directly, once
trying a different mirror) each returned incomplete and mutually
inconsistent orderings and mislabeled several tendencies (Reciprocation
Tendency mislabeled "13," a jump from item 17 straight to item 22 in one
pass); neither was used. The raw curl-and-strip fetch of the same page
supplied the complete, correctly ordered, and internally consistent primary
text used for the whole episode. A first draft using only five tendency
chapters came in at 4,339 words under the 5,000 floor; brought over the
floor by adding two more full worked chapters (Reciprocation Tendency with
the Cialdini zoo experiment and Watergate case; Reason-Respecting Tendency
with Carl Braun and the photocopier-line experiment) rather than by
restating material already used, per the charter's ban on padding by
restatement.

**Open questions:** (HITL) 047 closes the eight-episode Collison shelf on a
register none of the other seven used, individual cognitive habit rather
than institutional design; worth a listen to judge whether that closing
move reads as answering the shelf's own running question from a genuinely
different angle, or as a step outside the shelf's own throughline right at
its close. (AFK) The episode's three-line case against draws its "Munger's
own record" material from two well-documented but separate events three
decades apart (the 1973-74 partnership drawdown, the 2021-22 Alibaba
position); worth checking whether a closer, single example exists if the
shelf ever revisits Munger.

**Artifacts:** episodes/047-munger-psychology-of-human-misjudgment.md
(5,096 words, lint clean); queue.md (Collison shelf item 8 checked off
with full summary, closing the shelf; order-of-record block updated to
show all eight items done and point to nutrition science item 1).

**Context:** Unattended Routine run, 21 September 2026. Pre-flight found
local `main` twelve commits behind `origin/main`, fixed cleanly with `git
checkout main && git merge --ff-only origin/main` per the standing
template step, not logged as a pipeline event. One push for the episode
and queue update, verified live via `site/feed.xml` on `origin/main`
before this log entry.

## [2026-09-22] — Episode 048, Scurvy: the cure found, lost, and found again, opening the nutrition science series

**Decisions:** Wrote 048 as the pilot of the nutrition science series, per
queue.md's item 1 scoping (Lind's 1747 trial, the gap before Admiralty
lemon juice, the lime-juice regression, the Scott expedition; anchors
Carpenter's *The History of Scurvy and Vitamin C* and Bown's *Scurvy*).
Restructured the item's own theme, "a proven intervention and the
institutional reasons it does not get adopted," into a sharper spine once
research turned up a repeating pattern the queue note had not fully named:
not one delayed adoption but four separate loss-and-recovery cycles across
two hundred fifty years, each with a different mechanism. Cold-opened on
the 1875 Nares Arctic expedition (men taking their official lime-juice
ration exactly as ordered and getting scurvy anyway) as the hour's driving
mystery, answered only once the story reaches the 1860 lemon-to-lime
substitution. Callback structure: John Woodall's 1617 East India Company
manual opens the historical account and closes the verdict chapter; James
Lind's own twenty-five-year tenure as chief physician of Haslar Hospital
(1758-1783), retiring twelve years before his own finding became fleet
policy, is planted in Chapter Three and re-invoked when Haslar's own
admission numbers (1,457 cases in 1780 versus two in 1806-1810) appear in
Chapter Six. Case-against layer, per the higher grounding bar this series
carries (Kevin's own field): Carpenter's and Bown's own competing
revisionist framings against the tidy popular Lind-then-Blane myth; Thomas
Trotter's complicating role as a Channel Fleet physician who pushed hard
on naval health reform but never endorsed citrus as prevention, only as
cure; and the genuinely unsettled historical question of whether scurvy
contributed to the deaths of Scott's own polar party, stated as contested
rather than resolved either way. Verdict lands on the series' own running
concern for a trialist audience: a proven intervention with no known
mechanism cannot protect itself from a good-faith substitution, and the
closing generative question extends that past scurvy to any modern
feeding protocol, supplement source, or therapeutic food whose exact
composition can drift from what its own original trial tested. No BLOOM
aside; nothing in the material pointed toward the programme without a
stretch, so the default (none) held.

**Verification:** Facts and figures were checked across multiple
independent web sources this session, not from training knowledge alone:
Woodall's 1617 *The Surgeon's Mate* and its East India Company context;
Lind's 1747 Salisbury trial (twelve sailors, six pairs, the six-day
citrus result) and his own 1753 treatise, cross-checked against the James
Lind Library's own historical scholarship; Lind's Haslar appointment
(1758) and retirement (1783), and the 1,457-to-two Haslar admission
figures; Anson's 1740-44 circumnavigation losses (close to nineteen
hundred men, roughly fourteen hundred dead by 1742, overwhelmingly
scurvy), corroborated across two independent sources though historians'
exact figures vary; Macbride's and Pringle's fixed-air/wort theory and the
abandoned 1762 Portsmouth/Plymouth naval trial; Cook's 1768-71 voyage and
the confounded wort/sauerkraut/fresh-produce/cleanliness bundle behind its
reported success; Blane's 1779-82 service with Rodney's fleet, the one
man in seven annual disease-death tally from his own 1781 memorial, and
Rodney's scurvy-free six-month West Indies voyage (winter 1781-82) — a
direct quotation attributed to Rodney about this voyage turned up in only
one aggregated source this session and was not independently verified
verbatim, so it was paraphrased rather than quoted, per the grounding
rule against unverified quotations; the 1795 Suffolk voyage and Blane's
Commissioner appointment; the 1860 lemon-to-lime substitution and its
1918 potency test; the 1875 Nares expedition (the sixty-cases/four-deaths
figure rests on a single secondary source found this session and is
flagged below as unverified against a second source); Scott's 1901-04
Discovery expedition, Reginald Koettlitz's watercress crop, and the
Terra Nova polar ration's calorie composition; Holst and Frølich's 1907
guinea-pig model and the animal-model-validity point (most standard lab
animals synthesize their own vitamin C and cannot develop scurvy);
Szent-Györgyi's 1927-32 hexuronic-acid-to-ascorbic-acid work and his 1937
Nobel Prize. No primary text (Lind's own treatise, Carpenter's or Bown's
book) was read in full this session; all of the above rests on targeted,
cross-checked web research rather than a page-checked primary read.

**Traps & dead ends:** An initial draft ran 4,227 words, under the 5,000
floor; brought over the floor by deepening existing worked examples
(Lind's Haslar career, Macbride's fixed-air theory, Blane's Rodney-fleet
record) rather than by restating material already used, per the charter's
ban on padding by restatement. A first-pass sentence attributed a direct
quotation to Rodney ("not one was buried in six months") sourced from a
single aggregated search result; on review this could not be confirmed
verbatim against a second source, so it was rewritten as paraphrase before
publication rather than published as an unverified quotation.

**Open questions:** (AFK) The 1875 Nares expedition's specific casualty
count, sixty cases and four deaths, rests on one secondary source found
this session (a history-focused newsletter) rather than a primary
Admiralty inquiry record or a second independent corroborating source;
worth checking against the official 1877 Arctic Committee report if the
shelf ever needs a harder number. (AFK) None of this episode's four
anchor primary materials, Lind's 1753 treatise, Carpenter's and Bown's
histories, or a primary Admiralty or Discovery-expedition record, was read
in full this session; the episode rests on targeted, cross-checked
secondary research throughout, the same caveat now on record for many
earlier episodes. (HITL) 048 restructures its own queue-note theme
("institutional reasons a proven intervention does not get adopted") into
a four-cycle repeating-loss structure the queue note did not fully
anticipate; worth a listen to confirm that widening reads as delivering
the queue's own scoped theme rather than substituting a different one.

**Artifacts:** episodes/048-scurvy-cure-found-lost-found-again.md (5,031
words, lint clean); queue.md (nutrition science item 1 checked off with
full summary; order-of-record block updated to point to item 2, beriberi).

**Context:** Unattended Routine run, 22 September 2026. Pre-flight found
local `main` fifteen commits behind `origin/main`, fixed cleanly with `git
checkout main && git merge --ff-only origin/main` per the standing
template step, not logged as a pipeline event. One push for the episode
and queue update, verified live via `site/feed.xml` on `origin/main`
before this log entry.

## [2026-09-23] — Routine: Episode 049, Beriberi, Takaki, Eijkman, Grijns, and Funk

**Decisions:** Structured the item's own scoping (Takaki, Eijkman, Grijns,
Funk) around a mechanism genuinely different from 048's: not a cure lost
and refound inside one institution, but a cure proven cleanly and then
refused for two decades by a second institution in the same country, at a
countable cost. Cold open on the Russo-Japanese War's Army-wide beriberi
toll (roughly 250,000 cases, 27,000 dead against 47,000 killed by the
enemy; 25,000 of the 80,000-strong Third Army evacuated at Port Arthur),
set against the fact that the Imperial Japanese Navy had already
eliminated the same disease from its own ranks two decades earlier.
Takaki's Ryujo/Tsukuba paired-ship trial (1882-84) built as this series'
own echo of Lind's Salisbury trial, with the fourteen Tsukuba sailors who
refused the new ration read as an accidental control group inside the
experiment itself; the 1885 barley compromise's success despite Takaki's
own wrong nitrogen-ratio theory read against 048's Blane material (a
mandate that works without a mechanism). Army resistance built through
named actors: Ishiguro Tadanori's anti-barley faction and 1895 quote,
Ogata Masanori's unreproducible "beriberi bacillus," the demotion of army
surgeons Toki Yoritoku and Horiuchi Toshikuni for reporting the navy's own
result during the First Sino-Japanese War, Terauchi's too-late February
1905 field order. Java strand run as a second, structurally different
kind of loss: Eijkman's accidental chicken discovery, his own inability to
fully abandon a toxin theory even after his data broke it; Grijns's 1901
correct deficiency hypothesis and Nobel snub (1929, shared with Hopkins,
uncredited in Eijkman's own lecture) as a credit-versus-correctness case
parallel to Suzuki's 1910 oryzanine losing priority to Funk's 1911-12
"vitamine" over a dropped clause in a German translation. Steelmanned the
Army's resistance explicitly (germ theory's own recent, real successes
made a laboratory-mechanism standard a reasonable one to hold in the
abstract) before the case against. No BLOOM aside; the closing generative
question (what moves one part of an institution trained to trust one kind
of evidence to accept a result from a part trained to trust another) was
left general rather than pointed at the listener's own programme.

**Verification:** Takaki's biography, epidemiological survey (18 ships,
4,683 personnel), and the Ryujo (376 crew, 169 cases/44.9%, 25 deaths) and
Tsukuba (14 cases) trial numbers checked against three independent
sources this session (the James Lind Library's dedicated Takaki article,
Wikipedia's sourced biography, and a peer-reviewed 2024 Annals of Surgery
Open history article via PubMed/PMC, "ADOPTERs of Innovation in a
Crisis"), which disagreed on the Tsukuba's total crew size (287 versus
333) and is flagged as an open question below rather than silently picked
one way. The Russo-Japanese War beriberi figures (250,000 cases, 27,000
dead, 47,000 combat dead, the Port Arthur 25,000-of-80,000 evacuation)
were cross-checked across the same PMC article, a Wikipedia summary
citing independent sources, and a web search of secondary coverage, all
converging on the same figures. Ishiguro Tadanori's 1895 quote, Shigemichi
Suzuki's 1901 and 1906 quotes, and Shimazono's 1927 concession are all
drawn from the PMC article's own translated citations of primary Japanese
sources, not reconstructed from training knowledge. Eijkman's biography
and the chicken-feed accident were checked against a peer-reviewed 2019
neurology-journal retrospective (PMC6803585) fetched this session; Grijns's
1901 hypothesis, his exclusion from the 1929 Nobel Prize, and the 1935
translation date came from a dedicated World Neurology Online article on
Grijns, single-sourced and flagged as such below. The Suzuki/Funk priority
dispute (the German translation dropping Suzuki's novelty claim) and the
Jansen/Donath 1926 crystallization plus Robert Williams's 1936 structure
and synthesis of thiamine were each checked via independent web sources
this session. Carpenter's book was read only via a single review
(dannyreviews.com) rather than the text itself; Alexander Bay's
institutional argument and the "power and medicine" quote came from a
Medical History journal book review of Bay's own monograph, read directly
this session.

**Traps & dead ends:** An initial fetch of the Military Medicine journal
PDF on the Imperial Japanese Army's beriberi history (Hawk, 2006) hit a
paywall and returned only its abstract; the PMC "ADOPTERs" article,
fetched successfully via the PubMed tool, supplied the same ground with
far more citation detail and became the episode's central source for the
Army-resistance chapters instead.

**Open questions:** (AFK) The Tsukuba's total crew size is reported
inconsistently across sources (287 in the PMC "ADOPTERs" article, 333 in
the James Lind Library's account); the episode uses "around three
hundred" to stay honest to that spread rather than pick one figure, the
same hedge 043 used for Venture Research's researcher count. (AFK)
Grijns's Nobel-nomination and translation-date claims rest on a single
source (World Neurology Online) not independently corroborated this
session; worth a second check if the shelf ever leans harder on the
credit-dispute framing. (AFK) Kenneth Carpenter's book itself, this
item's named anchor, was not read in primary form this session, only via
one review; worth a fuller read if the shelf ever needs to quote Carpenter
more precisely than the even-handed "luck and translation" framing used
here. (HITL) The episode leans on a body-count argument (an institution
changed course only once the cost in lives became too large to ignore)
as its own closing generative question; worth a listen to judge whether
that reads as an honest reading of the record or as an overly grim note
to end a nutrition-science episode on, three episodes running now (037,
048, 049) that have closed on a comparably dark note.

**Artifacts:** episodes/049-beriberi-navy-proved-army-refused.md (5,014
words, lint clean); queue.md (nutrition science item 2 checked off with
full summary; order-of-record block updated to point to item 3,
pellagra).

**Context:** Unattended Routine run, 23 September 2026. Pre-flight clean,
local `main` already current with `origin/main`. One push for the episode
and queue update; the Build site Action's commit appeared within about
two minutes, and `site/feed.xml` on `origin/main` carries 049's title
before this log entry.

## [2026-09-24] — Routine: Episode 050, Pellagra and Joseph Goldberger

**Decisions:** Structured this item's own scoping (Goldberger against the
germ-theory consensus, the orphanage/asylum trials, Rankin, the filth
parties, twenty years to a fix) around two throughlines run in parallel
rather than one: the science question (poverty-diet cause vs. the
Thompson-McFadden Commission's contagion theory) and, held apart as a
second and separate audit in the closing chapter, a research-ethics
question about the consent those same proofs rested on. Cold open on the
epidemic's own scale (roughly three million cases, a hundred thousand
deaths, 1906-1940) against two wrong answers already on record by 1914:
Lombroso's decades-long spoiled-corn toxin theory and the Thompson-
McFadden Commission's 1912-14 verdict for person-to-person, likely
fly-borne contagion. Chain: the clean 1914 orphanage and Georgia State
Sanitarium diet trials; the Rankin State Prison Farm experiment (twelve
convict volunteers, one discharged for an unrelated condition, six of the
remaining eleven produced confirmed pellagra on a corn-heavy ration);
the 1916 filth parties as the negative control ruling out contagion on
Goldberger's own body; Sydenstricker's 1918-20 cotton-mill-village income
study as the economic proof. Steelmanned the Thompson-McFadden
Commission's germ-theory standard explicitly, then argued the comparison
to 049's Army resistance only holds part way: unlike the Army, the South's
resistance blended an honest evidentiary dispute with a regional economy's
material stake in the wrong answer, since accepting the diagnosis meant
indicting cotton monoculture itself, a distinction the episode names as
the narrator's own revision of the parallel it opens by suggesting. Landed
the twenty-year gap to an actual fix on two forces converging without the
South ever conceding the diagnosis: wartime bread fortification (1938-42)
following Elvehjem's 1937 niacin identification, and the Depression-era
cotton collapse that forced crop diversification for economic reasons that
had nothing to do with Goldberger being believed. No BLOOM aside; the
closing chapter's research-ethics question (a coerced or institutionalized
population's consent, an IRB's own modern audit) lands directly on the
listener's actual professional terrain per `listener.md` (trial consent,
vulnerable populations, ethics committees in two countries) without
needing a bridge to any specific programme.

**Verification:** Checked directly this session via web search (no primary
read of Kraut's "Goldberger's War" itself, flagged below): Goldberger's
biography (1874 birth near Girált, Austro-Hungarian Empire; 1883
immigration; Bellevue MD 1895; 1899 Marine Hospital Service; yellow fever,
dengue, and typhus each contracted in the field; 1906 marriage to Mary
Farrar across both families' religious objections; his own "never faced
anything with greater reluctance" quote to his wife on the 1914
assignment). The Thompson-McFadden Pellagra Commission's 1912-14
Spartanburg investigation, its Army Medical Corps leadership, its fly
vector suspicion, and Senator Ben Tillman's documented interest in its
Spartanburg site selection were each checked via independent sources. The
1914 Jackson, Mississippi orphanage trials and the Georgia State
Sanitarium trial (72 patients, 36 Black women from October and 36 white
women from December, no recurrences through October 1915) were checked
against a James Lind Library account of the trials. The Rankin State
Prison Farm timeline (twelve volunteers, one discharged in July for
prostatitis, baseline period 4 Feb-19 Apr, dermatitis first observed 12
Sept, study closed 31 Oct 1915, six of eleven confirmed) was checked
against a dedicated Mississippi Encyclopedia account and cross-checked
against Jon Harkness's 1996 "Prisoners and Pellagra," the paper this
episode's ethics case-against draws on for the coercion argument and the
volunteer who reportedly could not withdraw once sick; the contemporary
press quote used ("no effort to minimize the grave physical risk," under
fifteen words) is drawn from Harkness's own quotation of that press
account, not the primary press item itself, and is flagged as such here.
The 1916 filth parties (eight sessions, seventeen participants, the April
26 mutual blood injections) were checked against the Science History
Institute's account. Sydenstricker's cotton-mill-village figures (roughly
3.5 cases per thousand at the top wage tier, roughly twelve times higher
at the bottom, ten times higher again among non-earning women) and Seale
Harris's editorial line ("does the South a gross injustice," under fifteen
words) were each checked via independent web sources. The 1927 Mississippi
flood relief figures (sixteen million acres, twelve thousand pounds of
yeast, four-thousand-plus cured) and Goldberger's January 1929 death from
kidney cancer were checked directly. Elvehjem's 1937 niacin identification
using Goldberger and Wheeler's own black-tongue dog model, and the
fortification timeline (1938 voluntary enrichment, 1941 FDA standards,
February 1942 Army enriched-flour-only purchasing, three-quarters of
white bread fortified by year's end) were each checked against independent
sources. The Depression-era crop-diversification figures (roughly 8%
higher corn acreage, 3% peanut, 1.2% sweet potato per capita in
high-cotton-loss counties) came from an NBER working paper whose own PDF
would not extract as readable text this session; the acreage percentages
are instead as reported in a web-search synthesis of that paper's stated
findings, not independently verified against the paper's own tables, and
are flagged below at that hedge.

**Traps & dead ends:** Two PDF fetches (the NBER working paper on
pellagra's rise and fall, and Harkness's own CDC-hosted "Prisoners and
Pellagra") returned unreadable binary/compressed-stream content rather
than extractable text in this session's environment, the same PDF-
extraction gap earlier sessions hit with the Hamming and Bush books;
worked around both times with targeted web-search synthesis of each
paper's stated findings rather than a page-checked primary read.

**Open questions:** (AFK) Neither Kraut's "Goldberger's War," this item's
own named anchor, nor Harkness's "Prisoners and Pellagra," nor the NBER
working paper on pellagra's economic history, was read in primary form
this session; the episode's ethics case-against and the Depression-era
crop-diversification figures both rest on search-synthesized secondary
accounts of those sources rather than a page-checked read, worth
revisiting if the shelf ever needs more precise figures or quotations.
(HITL) The episode closes on a research-ethics verdict (informed consent
under coercion, an IRB's modern standard) rather than folding an
application into a BLOOM aside; worth a listen to judge whether landing
directly on trial methods and ethics, without naming any programme, reads
as a genuine and undiluted connection to the listener's own actual work or
as a missed chance to make it concrete. (HITL) The episode explicitly
revises its own opening comparison to 049's Army resistance partway
through (Chapter Eight), arguing the South's resistance combined
evidentiary caution with material self-interest in a way beriberi's story
did not; worth judging whether that self-correction reads as the delayed-
thesis device the charter calls for or as hedging.

**Artifacts:** episodes/050-pellagra-goldberger-south-twenty-years.md
(5,087 words, lint clean); queue.md (nutrition science item 3 checked off
with full summary; order-of-record block updated to point to item 4, the
Minnesota Starvation Experiment).

**Context:** Unattended Routine run, 24 September 2026. Pre-flight found
local `main` one commit behind `origin/main` (a non-fast-forward push
rejection on the first dry-run check, the same routine checkout artifact
prior sessions have hit), fixed cleanly with `git checkout main && git
merge --ff-only origin/main` per the standing template step, not logged as
a pipeline event. One push for the episode and queue update; the Build
site Action's commit appeared within about two minutes, and
`site/feed.xml` on `origin/main` carries 050's title before this log
entry.

## 2026-09-25 — Episode 051: The Minnesota Starvation Experiment

**Decisions:** Landed the study's modern application on Kevin's own SAM/RUTF
research territory (the WHO F-75/F-100 staged refeeding protocol, and a
grounded note on the Uganda F-75-to-RUTF transition literature) rather than
on BLOOM, per `listener.md`'s instruction to land an application on the
right part of the listener's work rather than defaulting to the same
programme every time; `listener.md` names severe/moderate acute
malnutrition treatment as Kevin's actual primary study area, a closer and
less-stretched fit than a maternal mental-health counselling programme for
a study about staged refeeding physiology. Framed the episode's spine as
the explicit contrast 050's own sign-off promised (genuine volunteer
consent versus Rankin's coerced pardon), then complicated rather than
simply confirmed that contrast with the "Compelled to Volunteer" thesis on
CPS social pressure and the desire to disprove the "coward" charge, judged
the more honest version of the story than a clean opposite. Used the
Bhatt/Lederman/Voo 2021 bioethics critique (Minnesota's data cited to
justify Guantanamo force-feeding) as the case-against/reception chapter,
since it engages the same consent theme from a genuinely different angle
(voluntary data weaponized against an involuntary population) rather than
re-litigating 050's own argument. One direct callback to 042 (OSRD's
Committee on Medical Research, the same wartime funding body behind both
the penicillin scale-up and this study).

**Verification:** Core facts (dates, phase calorie levels, the four
refeeding groups and their caloric increments, physical effects, MMPI use,
attrition numbers) were checked against multiple independent sources
(Wikipedia, MNopedia/Minnesota Historical Society, the Brethren Historical
Library's archive page) and found consistent. The Samuel Legg finger-
amputation incident and his euphoric aftermath (seventeen soda fountains)
were corroborated across several independent secondary accounts and an
AFSC oral-history page naming him alongside fellow volunteer Marshall
Sutton, though none of these is Tucker's book itself, which was not
fetched or read in primary form this session. The Neil Hartman and Harold
Blickenstaff material, the "Will You Starve That They Be Better Fed?"
brochure title, and the Carlyle Frederick cookbook detail all came from
independent secondary sources converging on the same wording. The
Schnitker et al. 1951 Japanese POW refeeding-death figures and the 1981
Weinsier/Krumdieck refeeding-syndrome naming were checked against a
dedicated PMC history-of-refeeding-syndrome article. The Bhatt, Lederman
and Voo 2021 Journal of Bioethical Inquiry critique was verified via its
own abstract and independent summaries, not the full text (paywalled). Two
arithmetic errors caught and fixed before publication: a "sixty-nine years
later" line for the 2021 citation (corrected to seventy-seven, from 1944)
and a line conflating the 2018 publication date of the "57-year follow-up"
study with the 57-year mark itself (the interviews were conducted in 2002,
fifty-seven years after 1945; publication was delayed to 2018, a fact now
stated directly rather than elided).

**Traps & dead ends:** None; all primary web fetches this session
succeeded (Wikipedia, MNopedia, the AFSC oral-history page, the PMC
refeeding-syndrome history), unlike several recent sessions' PDF-extraction
failures.

**Open questions:** (AFK) Todd Tucker's "The Great Starvation Experiment"
(2006) and Keys et al.'s "The Biology of Human Starvation" (1950), this
item's two named anchors, were not read in primary form this session; the
episode's account rests on convergent secondary sourcing (Wikipedia,
MNopedia, APA Monitor-adjacent coverage, academic retrospectives) rather
than a page-checked primary read, the same caveat now on record for most
of this shelf's nutrition-science episodes. The Bhatt/Lederman/Voo 2021
paper was read only via its abstract and secondary summaries, not the full
text. (HITL) The episode complicates 050's "opposite direction from
Goldberger's Rankin trial" framing with the "Compelled to Volunteer"
thesis rather than leaving the contrast clean; worth a listen to judge
whether that complication reads as honest nuance or as undercutting the
sign-off's own promised setup right at the episode's start.

**Artifacts:** episodes/051-minnesota-starvation-experiment-refeeding.md
(5,082 words, lint clean); queue.md (nutrition science item 4 checked off
with full summary; order-of-record block updated to point to item 5, the
great protein fiasco).

**Context:** Unattended Routine run, 25 September 2026. Pre-flight found
local `main` behind `origin/main` by six commits (the same routine
checkout artifact prior sessions have hit), fixed cleanly with `git
checkout main && git merge --ff-only origin/main` per the standing
template step, not logged as a pipeline event. One push for the episode
and queue update; the Build site Action's commit appeared within about
thirty seconds, and `site/feed.xml` on `origin/main` carries 051's title
before this log entry.

## [2026-09-28] — Routine: Episode 052, The Great Protein Fiasco

**Decisions:** Wrote item 5 unattended under the item's own 8 Sep 26
proximity fallback (queue.md: "if he has not [steered it] by the time
they come up, write them from the published record only and make no
reference to his studies"); no steering had occurred, so the episode
proceeds on that pre-authorized basis. No BLOOM aside; unlike 051, this
episode makes no reference to RUTF, SAM treatment protocols, or any
research territory adjacent to the listener's own work, per the proximity
rule's explicit instruction, even though several of the historical
sources used (the 2013 Malawi twin-microbiome study, a Malawi antioxidant
trial) sit in that same geography. Cold open built around Donald
McLaren's own career pivot (kwashiorkor-dominant Tanzania 1957-62 to
marasmus-dominant Beirut 1962) as the worked case seeding his doubt,
rather than opening on the UN bureaucracy directly. Explicit mirror-image
framing against 049 and 050: those two episodes were institutions
refusing a *correct* diagnosis; this one is institutions eagerly
embracing an *incorrect* one, for the opposite reason (it cost them
nothing and opened funding). Closed not on a tidy correction but on the
still-unresolved question the protein theory had been a wrong answer to
in the first place (why kwashiorkor's oedema versus marasmus's wasting on
similar diets), and on the further irony that kwashiorkor research
itself collapsed into what a 2014 reviewer called an "orphan disease"
once the tidy story fell, even as the disease kept killing children by
the hundreds of thousands a year.

**Verification:** Donald McLaren's actual 1974 Lancet article ("The Great
Protein Fiasco") was fetched as a PDF and read in full primary form this
session via the Read tool's native PDF support, a break from this
series' usual pattern of AFK-flagged secondary-only sourcing for its
named anchor. Every figure and quote drawn from it (Cicely Williams's
"for the last 20 years I've been trying to debunk kwashiorkor," Marcel
Autret's 1969 restatement, the ten-million-ton/hundred-billion-dollar
closed "gap," the McLaren/Scrimshaw exchange, the Incaparina and Vitasoy
economics, the 1966 Hamburg suppression account) is quoted or paraphrased
directly from that primary text, not reconstructed from secondary
summaries. A second primary source, André Briend's 2014 CMAM Forum
technical brief "Kwashiorkor: still an enigma," was also fetched as a PDF
and read in full; it supplied the free-radical hypothesis (Golden and
Ramdath 1985/87), the Malawi antioxidant-trial null/adverse result, the
aflatoxin hypothesis and its reverse-causality rebuttal, the
dysadaptation/insulin-cortisol hypothesis, the 2013 Malawi twin-microbiome
study (Smith et al., Science), the requirement-table wobble through 2007,
and the publication-count "orphan disease" finding, all cited directly
from Briend's own text and reference list rather than search summaries.
Waterlow and Payne's 1975 Nature paper and Sukhatme's 1970 Nutrition
Reviews paper were not reachable in primary form this session (Nature
redirected to an authentication wall); their content rests on convergent
secondary sourcing (search-engine summaries, the Karger "Rise and Fall of
Protein Malnutrition" review, a JHU preprint history of the protein gap)
corroborating each other and consistent with how McLaren's own paper
cites them. Cicely Williams's biography (Oxford, Colonial Medical
Service, 1929 Gold Coast posting, wartime Japanese POW years, 1933/1935
papers) and the institutional history (PAG founding 1955, World Food
Conference November 1974, PAG wind-down by 1977, FAO/WHO/UNU 1985
revision) were each checked against at least one independent source this
session, not asserted from training knowledge alone.

**Traps & dead ends:** Direct WebFetch of both the Lancet and Nature
articles' own hosting pages failed (403 and an authentication redirect
respectively); a raw curl-and-download of a PDF mirror of McLaren's paper
succeeded where the WebFetch tool did not, and the Read tool's native PDF
rendering extracted the full four-page article cleanly, including its
reference list, a path worth trying first on future episodes before
accepting a secondary-only read. The Waterlow/Payne Nature paper had no
equivalent open mirror found this session.

**Open questions:** (AFK) Waterlow and Payne's 1975 Nature paper itself
was not read in primary form this session; its content rests on
convergent secondary corroboration, the same caveat on record for most of
this series' non-McLaren sources. Sukhatme's 1970 Nutrition Reviews paper
was likewise not read in primary form. (HITL) Whether opening on
McLaren's own biographical pivot, rather than on the UN apparatus
directly, delays the institutional thesis too long before the listener
has a name for what is wrong with it; worth a listen to judge against the
charter's own delayed-thesis preference. (HITL) Item 5's proximity rule
required omitting any BLOOM aside or reference to the listener's own
research territory even though several of the strongest available
sources (the Malawi twin study, the Malawi antioxidant trial) come from
exactly that geography; worth Kevin's judgment on whether the episode
drew that line correctly or overcorrected into avoidance.

**Artifacts:** episodes/052-great-protein-fiasco-kwashiorkor.md (5,017
words, lint clean); queue.md (nutrition science item 5 checked off with
full summary; order-of-record block updated to point to item 6,
diet-heart, Keys vs. Yudkin, already promised by 051's own sign-off).

**Context:** Unattended Routine run, 28 September 2026. Pre-flight found
local `main` behind `origin/main` by nine commits, fixed cleanly with
`git checkout main && git merge --ff-only origin/main` per the standing
template step, not logged as a pipeline event. One push for the episode
and queue update; the Build site Action's commit appeared within about
ninety seconds, and `site/feed.xml` on `origin/main` carries 052's title
and full text, verified before this log entry.

## [2026-09-29] — Routine: Episode 053, Diet-Heart: Keys versus Yudkin

**Decisions:** Spine question: what could have decided a duel between two men reading the same table of country numbers, and did anyone run that test. Kept the case against running both ways (Keys overconfident about a food, right about a mechanism; Yudkin right to ask, wrong to be as sure as his title; Taubes's suppression narrative not equal to truth). Read Kearns 2016 as a process failure rather than proof the fat conclusion was false, because the paper itself does not establish that. Steelmanned the trials' critics with reverse causality (callback to 052's aflatoxin), so the recovered-data headline is not left unqualified. Ran under the proximity fallback again: published record only, no BLOOM aside, no reference to the listener's own studies. Callbacks to 051 (Keys's starvation study), 050 (Goldberger's intervention breaking a confounded correlation) and 052 (mirror-image hardening).
**Verification:** Checked against search results this session: Minnesota Coronary Experiment design and numbers (9,423 randomised; 2,355 on diet at least a year; cholesterol down 13.8% vs 1.0%; 22% higher death risk per 30 mg/dL fall; pooled ratios 1.13 and 1.07; Frantz sons, third basement trip; STAT and BMJ editorial), Sydney Diet Heart Study (458 men; 17.6% vs 11.8% and 17.2% vs 11.0%), Kearns 2016 (Project 226, about $6,500, Hickson's approval of the draft on 2 Nov 1966, NEJM 1967, more than 340 documents), Yerushalmy and Hilleboe 1957 (22 countries vs Keys's six), Seven Countries (16 cohorts, 12,763 men; Kromhout 2018 sucrose and saturated fat both correlating 0.68 to 0.92 with 50-year CHD mortality), Cochrane 2020 (15 trials, 56,675 adults), Yudkin's dates and Keys's 1971 sentence, Guyenet's and Hall's reviews of Taubes. Stated from training knowledge at hedged precision: Keys's 1965 prediction equations, the metabolic-ward feeding studies, drug trials on LDL, the North Karelia project, Lustig's 2009 lecture views. Keys's "mountain of nonsense" reported at one remove and labelled as such in the script. The partial-hydrogenation trans-fat point is flagged in the script as the narrator's inference.
**Traps & dead ends:** PMC pages for the Ramsden and Kearns papers returned only a CAPTCHA to WebFetch, and Europe PMC returned the linked BMJ editorial in place of the Ramsden paper, so both papers rest on secondary sourcing (STAT, UCSF coverage, abstracts through search). The UCSF news page returned 403.
**Open questions:** (AFK) Neither the Ramsden 2016 nor the Kearns 2016 paper was read in primary form; a future session could try a direct PDF fetch. (AFK) The Keys 1971 Atherosclerosis paper and Yudkin's 1957 Lancet paper were not read directly; the Keys sentence rests on a secondary biography. (HITL) Whether the compressed Yudkin biography and the Finnish North Karelia aside pay their way, or read as seductive detail.
**Artifacts:** episodes/053-keys-yudkin-diet-heart-duel.md (5,876 words, lint clean); queue.md (item 6 checked off with summary, order-of-record block points to item 7).
**Context:** Unattended Routine run, 29 September 2026. Pre-flight found local main behind origin/main, fixed by fast-forward per the standing step. One episode push, then the Build site commit appeared within about a minute and site/feed.xml on origin/main carries the 053 title. Sign-off promises item 7, Barker and fetal origins.

## [2026-09-30] — Routine: Episode 054, Barker and the Fetal Origins of Adult Disease

**Decisions:** Spine question: when a disease arrives late in life, where does its beginning lie, and what else could have produced the same ledger entries. Told the field as a sequence of supports removed one at a time (birth-weight blood-pressure gradient shrank with sample size; part of the rest is shared fetal genetics; the Dutch famine result did not run through birth weight), so the verdict is a split: the strong womb-as-cause form lost, the weak form is too general to be wrong, and the clearest consequences of early undernutrition are height, schooling and earnings (Victora 2008). Explained the adjust-for-current-weight trap in plain words because it is the technical core of the Huxley critique. Callbacks to 053 (archive boxes, ecological tables) and 051 (Minnesota versus the Hunger Winter). Proximity fallback again: published record only, no BLOOM aside, COGENT read-across from the queue left out.
**Verification:** Checked against search results this session: Hertfordshire 1989 (about 5,654 men, threefold risk at 18 lb or less versus 27 lb or more at one year, about 37,000 in the cohort, Burnside credited for the records), Sheffield 1993 (1,586 men, SMRs 119 and 74, placental ratio 137), Huxley 2002 Lancet (55 studies, minus 1.9, 1.5 and 0.6 mm Hg per kg by study size, twins about 0.6, publication bias), Roseboom 2000 (8.8% versus 3.2%, groups of 120, 108 and 68, independent of birth weight; six cases is the narrator's arithmetic and is labelled so), Ravelli 1976 (about 300,000 men, opposite signs by timing), Hattersley and Tooke 1999 (533 g in 58 offspring), Vaag review (2 of 45 loci), Horikoshi 2016 (153,781 people, 60 loci, about 15%, rg minus 0.22, 0.27, 0.30), Moore 1997 Nature, Victora 2008, Eriksson 2001 (4,630 men) and the Cole, Fewtrell and Lucas critique, Barker's dates. Stated from training knowledge at hedged precision: Neel 1962, the Hunger Winter ration levels and rail strike, Lucas, Fewtrell and Cole BMJ 1999 as a general point on adjustment, the Dutch later glucose findings, pregnancy supplementation trials in Guatemala, the Gambia and Bangladesh. No quotes used.
**Traps & dead ends:** The first Huxley fetch returned an unrelated paper (Blake 2002); the meta-analysis numbers rest on search summaries. PubMed pages returned only a cookie notice. Primary papers were not read in full.
**Open questions:** (AFK) Read Huxley 2002 and the 1989 Lancet paper in primary form to confirm the study-size gradient and the SMR figures. (AFK) The Gambia paper's cause-of-death breakdown was not verified; the script attributes the excess only to early adult mortality tied to immune development. (HITL) Whether the two-chapter genetics argument is too dense for a walking listen.
**Artifacts:** episodes/054-barker-fetal-origins-hertfordshire-ledgers.md (5,463 words, lint clean); queue.md (item 7 checked off with summary, order-of-record block points to item 8).
**Context:** Unattended Routine run, 30 September 2026. Pre-flight found local main behind origin/main (dry-run push rejected), fixed by fast-forward per the standing step. One episode push; the Build site commit appeared within about thirty seconds and site/feed.xml on origin/main carries the 054 title. Sign-off promises item 8, growth standards.

## [2026-10-01] — Routine: Episode 055, Growth Standards: who is the reference child

**Decisions:** Spine question: who is the reference child, and who chose. Ordered the story as successive repairs to Gomez's percent-of-median grade (Waterlow's two axes, then z-scores, then the reference itself), so the NCHS/Fels problem arrives after the listener holds the arithmetic. Used the reference-versus-standard distinction as the thesis and gave the verdict as a split: trust the standard for the clinic and for a country against itself, hold cross-country league tables loosely, because the 3 percent between-site share was produced partly by the selection filter. Percent-of-median problem shown with a labelled constructed example. Callbacks to 052 (diagnosis hardening) and 054 (Victora 2008 needs a common ruler). Proximity fallback again: published record only, no BLOOM aside.
**Verification:** Checked against search results this session: Gomez bands (76-90, 61-75, 60 or below percent of Harvard 50th percentile), Waterlow 1972 stunting and wasting bands and 1977 Bulletin paper, NCHS 1977 construction (Fels, Yellow Springs, 1929-75, formula-fed, three-month visit intervals, length/stature discontinuity at 24-36 months), Habicht 1974 title and conclusion as summarised, MGRS (1997-2003, six sites, 8,440 children, longitudinal 0-24 months plus cross-sectional 18-71 months, 3 percent between-site versus 70 percent between-individual variance in length), release date 27 April 2006, direction of 2006 shifts versus NCHS, 2009 joint statement (WHZ below -3 or MUAC below 115 mm, raised from 110), Sachdev's and Natale-Rajagopalan's figures as reported in a 2024 BMJ Paediatrics Open debate page, INTERGROWTH-21st scope and critique. Stated from training knowledge at hedged precision: WHO's late-1970s endorsement of NCHS, Dibley 1987 content, the 2007 five-to-nineteen reference method, Borghi's affiliation (named only by surname, as the source gave it). Constructed example flagged in script. No quotes used.
**Traps & dead ends:** Gomez 1956 paper pages returned 403 or lacked numbers, so mortality figures by degree are described qualitatively. PubMed returned a cookie notice. Sachdev's first name and the debate's venue come from one fetched page.
**Open questions:** (AFK) Read Gomez 1956, Habicht 1974, Waterlow 1972 and 1977 in primary form and add exact numbers. (AFK) Confirm the Natale and Rajagopalan figures against the BMJ Open paper itself. (HITL) Whether the six-site critique chapters are too dense for a walking listen.
**Artifacts:** episodes/055-growth-standards-reference-child-gomez-to-who.md (5,612 words, lint clean); queue.md (item 8 checked off with summary, order-of-record block points to item 9).
**Context:** Unattended Routine run, 1 October 2026. Pre-flight clean (local main level with origin). One episode push; the Build site commit appeared within about a minute and site/feed.xml on origin/main carries the 055 title. Sign-off promises item 9, the closer duel on nutritional epidemiology.

## [2026-10-02] — Routine: Episode 056, Can Nutritional Epidemiology Be Trusted? (series closer)

**Decisions:** Spine question: when effects are small and the exposure is everything a person eats, what evidence could ever decide which food does what. Opened on Ioannidis's hazelnut arithmetic and ended the series on the lime-to-hazelnut distance. Scored the duel as a split: Ioannidis right about food-by-food, single-study, lifespan-scale claims; wrong to let that class stand for the whole field; Harvard right that trans fat and folate were real, but their measurement-error defence answers attenuation, not differential confounding. Added a narrator test (convert an association into years per dose) and labelled it as the narrator's own. Told trans fat as a case with several legs and beta carotene as a case with one. Callbacks to 048 (Lind), 050 (Goldberger), 052 (aflatoxin), 054 (Huxley adjustment). Proximity fallback again: published record only, no BLOOM aside.
**Verification:** Read Ioannidis's JAMA Viewpoint (online August 2018) in full from a typeset PDF copy this session: hazelnut, coffee, mandarin, egg and bacon figures, attenuation argument, 250,000 foods, genome-linkage analogy, beta carotene RR 0.69 (0.59-0.80), PREDIMED passage, reforms. Read Satija, Yu, Willett and Hu (Adv Nutr 2015) on the open archive: FFQ correlations 0.4 to 0.7, WHI adherence, 30 to 40 percent dropout, trans fat 29 percent (11 to 49), NYC 72 percent, 518 to 1,037 deaths, folate 19 percent, PREDIMED 7,447 and 4.8 years. Via search summaries: Schoenfeld and Ioannidis 2013 (50 ingredients, 40 with studies, 20 with 10 or more, 264 assessments, 191 or 72 percent, 75 percent weak or null, 36 meta-analyses median RR 0.96), Willett's Medscape reply of 14 September 2018 and Hu's reported remark (both paraphrased, no quotes), Hall 2019 (20 adults, 508 kcal per day more), WHI DM trial (48,835 women, 8.1 years, fat gap 10.7 to 8.1 points), PREDIMED retraction and republication with similar results. Stated from training at hedged precision and flagged in the script: ATBC and CARET lung cancer increases, Nurses' Health Study trans fat findings, feeding-trial lipid effects, WHI breast cancer HR near 0.91 and null heart disease, the nature of PREDIMED's randomisation errors.
**Traps & dead ends:** Springer (Eur J Epidemiol 2019 paper) and the HSPH news page redirected to login or the home page and were not read. No JAMA letter exchange was found; the script says the direct reply came through the press plus the 2015 paper, which predates the essay.
**Open questions:** (AFK) Find the Willett and Hu 2018-19 replies in primary form (Medscape piece, any published rejoinder) and replace the paraphrases. (AFK) Verify the beta carotene trial figures and WHI hazard ratios against the papers. (HITL) Whether the PREDIMED chapter and the WHI numbers are too dense for a walking listen.
**Artifacts:** episodes/056-ioannidis-willett-hu-nutritional-epidemiology-duel.md (5,980 words, lint clean); queue.md (item 9 checked off, order-of-record block points to Bush, science as an institution item 1).
**Context:** Unattended Routine run, 2 October 2026. Pre-flight found local main behind origin/main, fixed by fast-forward per the standing step. One episode push; the Build site commit appeared within about a minute and site/feed.xml on origin/main carries the 056 title. The nutrition series is complete (048 to 056). Sign-off promises Bush, Science, the Endless Frontier.

## [2026-10-05] — Routine: Episode 057, Science, the Endless Frontier (Vannevar Bush)

**Decisions:** Spine question: when a society pays for knowledge nobody can promise will be useful, who decides what is funded and what is it owed. Read the report as a document first (ledger, then spending table, then design) and the reputation second, so the pipeline attribution is tested against the text. Used the report's own penicillin example as the worked case because it holds both halves of Bush's position. Split verdict by claim: market-failure argument stands, sequence claim is more careful than its reputation but defined basic research by motive, governance by an eminent board was removed by the veto. Narrator's own test (market, pipeline or mission claim, and which one the review form measures) labelled as the narrator's. Callbacks to 042 (the contract method), 036 (Weber's guild gamble), 053 (country-level tables), 048-050 (the deficiency diseases in the ledger). Proximity fallback again: published record only, no BLOOM aside.
**Verification:** Read in full from the NSF 75th-anniversary PDF reprint this session: Roosevelt's letter and four questions, Bush's transmittal (social sciences and humanities excluded), the Summary, Chapters 1 to 3 and 5 to 6 (death rate 14.1 to 0.6 per thousand, life expectancy 49 to 65, 1930 to 1940 spending table, basic research and pacemaker passages, penicillin and the development-phase sentence, crowding-out passage, Five Fundamentals, the nine-member Foundation, divisions, patent, bids and vouchering clauses, medical 5 to 20 million, program 10 to 50 million), and the committee rosters (Maclaurin as secretary of the Bowman committee). Via fetched pages or search summaries: Truman's memorandum of 6 August 1947 (objections paraphrased from a summary), 1950 act and National Science Board, early NSF appropriations and first grants, Bush versus Kilgore dispute, Nelson's review of Kealey, Godin 2006 abstract, Edgerton's title and thesis, Pielke's Nature 2010 piece, Stokes's quadrants, Comroe and Dripps percentages, Kevles 1977 title and issues. Stated from training knowledge at hedged precision and flagged in the script: the penicillin timeline, ONR, NIH and AEC postwar funding, Kealey's later career. No direct quotes used beyond short phrases from the report text.
**Traps & dead ends:** nsf.gov history pages carried no report text, archive.org hOCR reset the connection, the Nature article and a CSPO page were gated, and the Truman Library page returned base64 so the veto memo came via the UCSB page summary. One search summary claimed the Senate overrode the veto; that contradicts the other sources and was not used. The PDF extraction dropped the budget table in Chapter 6, so only the Chapter 3 budget figures are cited.
**Open questions:** (AFK) Read Godin 2006, Edgerton 2004 and Pielke 2010 in full and confirm the attributions. (AFK) Read the Truman memorandum in full text and Kevles 1977. (AFK) Recover the Chapter 6 budget table from the report. (HITL) Whether the design and veto chapters are too dense for a walking listen.
**Artifacts:** episodes/057-bush-science-the-endless-frontier.md (6,140 words, lint clean); queue.md (item 1 checked off with summary, order-of-record block points to item 2).
**Context:** Unattended Routine run, 5 October 2026. One episode push; the Build site commit appeared within about a minute and site/feed.xml on origin/main carries the 057 title. Sign-off promises item 2, Kuhn part one.

## [2026-10-06] — Routine: Episode 058, The Structure of Scientific Revolutions, Part One (Thomas Kuhn)

**Decisions:** Spine question: if most research is mop-up inside a framework nobody questions, what makes it productive, what does it cost, and what does a funding system that mostly rewards it select. Ordered the episode as the electricians (pre-paradigm to Franklin), the three classes of mop-up with Coulomb's pan balances run to the end, the puzzle definition, rules versus exemplars (Galileo, Huygens, Bernoulli from the Postscript), the textbook chapter, then Popper and Kuhn, then the study section. Steelmanned normal science as productive restriction before the cost. Verdict is a split: Kuhn's reply on frameworks and teaching close to decisive; his community-not-subject-matter repair partly a retreat; funding claim stated as untested. Narrator's own test (what would the field learn if the result came out the other way) is labelled as the narrator's. The reading of Bush and Godin as a textbook phenomenon is labelled as inference. Callbacks to 057 (Bush, Godin) and 056 (Ioannidis). Proximity fallback: no BLOOM aside. Ran long at 7,235 words because the Popper exchange and the study-section chapter each carried new material.
**Verification:** Read in full from a text copy of the second edition: Preface, chapters I to V, chapter XI to the element example, Postscript sections 1 to 3 (disciplinary matrix, exemplars, community size of about one hundred and under twenty-five for a revolution, Masterman and the twenty-two count). Read Popper's essay and Kuhn's reply in the 1970 Lakatos and Musgrave volume from an archive text. Via search summaries: Conant's 1947 course and the Aristotle episode, the Essential Tension's 1959 Utah occasion and convergent/divergent argument, NIH simplified framework effective 25 January 2025 (three factors), Nicholson and Ioannidis 2012 (700 papers, 0.8 percent of panel members) and Salzberg's re-analysis (125 sampled, 63 reviews, 17 off-field, 34 of 45 supported). Stated from training knowledge and flagged in the script: Clairaut and the 1750 lunar solution, Kuhn's biography beyond the preface. No quotes beyond short phrases.
**Traps & dead ends:** Project MUSE and the INFORMS page (Boudreau et al.) returned a challenge page or 403, so that paper was dropped. The Essential Tension was not found in primary form.
**Open questions:** (AFK) Read the Essential Tension paper and Nicholson and Ioannidis in primary form. (AFK) Confirm the Salzberg figures against his own post. (HITL) Whether 7,235 words is acceptable for a two-voice exchange chapter, and whether the Popper and study-section chapters are too dense for a walking listen.
**Artifacts:** episodes/058-kuhn-structure-of-scientific-revolutions-part-one-normal-science.md (7,235 words including frontmatter, lint clean); queue.md (item 2 checked off, order-of-record block points to item 3).
**Context:** Unattended Routine run, 6 October 2026. Pre-flight clean. One episode push; the Build site commit appeared within about a minute and site/feed.xml on origin/main carries the 058 title. Sign-off promises item 3, Kuhn part two.

## [2026-10-07] — Routine: Episode 059, The Structure of Scientific Revolutions, Part Two (Thomas Kuhn)

**Decisions:** Spine question: how does a field come to see what was in front of it, and once seen, what could count as evidence when the standards themselves are disputed. Ran Kuhn's chapters VI to X and XII as a chain (discovery as process, anomaly against expectation, crisis, anomaly versus counterinstance, incommensurability, persuasion and the Planck remark) and used the Helicobacter pylori story as the worked medical case, as the queue item allowed. Scored it by claim: it fits Kuhn on discovery and on the newcomer, poorly on crisis as precondition, and against Kuhn on incommensurability, because the argument was won in the incumbents' own currency (a blinded relapse trial against cimetidine). Marked the case as chosen for fit, so an illustration and not a test. Added a narrator's addition, labelled as such: find the instrument the other side accepts as decisive. Callback to 049 and 050 (institutional resistance with interests, against Kuhn's resistance made of assurance). Listener aside confined to one third-person program-director paragraph; no BLOOM. Cut a first draft of 6,988 words to the ceiling.
**Verification:** Read in full from a text copy of the second edition: chapters VI, VII, VIII, IX, X (to the Dalton example), XII, and the opening of XIII (only its first pages were read; XIII is not used beyond that). Helicobacter material is from Marshall's 2005 Nobel lecture (the full text PDF at nobelprize.org): Warren's pilot, the Easter 1982 culture and the 48-hour discard, Table 2 (58 of 100 infected; 13 of 13 duodenal ulcer, p 0.00044; 18 of 22 gastric ulcer; 27 of 31 ulcers), the Fremantle donor serology (43 percent), the Martin and Hollanders relapse figures (about 90 and 60 percent at two years), the bismuth disc test, the piglets, the self-experiment timeline and the fact that tinidazole came after the day-fourteen endoscopy, the four-arm trial, the NHMRC funding terms, the 104 and 14 figures (his own words), Rauws, Graham and Hentschel, the 1994 NIH conference. The risk ratio (27 of 58 against 4 of 42) is the narrator's arithmetic from his table. Via search summaries only: Azoulay, Fons-Rosen and Graff Zivin 2019 (collaborators decline, non-collaborators rise, about 7 percent growth), Hull, Tessner and Diamond 1978 (78 scientists, age did not predict acceptance), and the February 1994 date of the NIH conference. Both are flagged in the script as unchecked. Not verified against the Lancet papers. No direct quotes beyond a few words.
**Traps & dead ends:** The BMJ and NCBI pages on the Helicobacter story carried only the Nobel announcement; the Nobel lecture PDF was the usable primary text. The Mayo Clinic Proceedings page returned 403. The lecture does not mention the rejected conference abstract found in popular accounts, so it was left out. Thagard's analysis of the ulcer case (cogsci.uwaterloo.ca) returned 503 and was not used.
**Open questions:** (AFK) Read Hull et al. 1978 and Azoulay et al. 2019 in primary form and confirm the figures. (AFK) Check the Marshall and Warren Lancet 1984 paper against the lecture's table. (AFK) Confirm the NIH 1994 consensus statement wording and date. (AFK) Read Kuhn XIII in full if progress is ever needed. (HITL) Whether the Helicobacter case, which takes about a third of the episode, is more than a Kuhn episode should carry.
**Artifacts:** episodes/059-kuhn-structure-of-scientific-revolutions-part-two-anomaly-crisis-revolution.md (6,514 words including frontmatter, lint clean); queue.md (item 3 checked off with summary, order-of-record block points to item 4).
**Context:** Unattended Routine run, 7 October 2026. Pre-flight needed a routine fast-forward of local main. One episode push; the Build site commit appeared within about two minutes and site/feed.xml on origin/main carries the 059 title. Sign-off promises item 4, Kuhn part three (Lakatos, Feyerabend, Kuhn's retreat from the relativist reading, what survives).

## [2026-10-08] — Routine: Episode 060, The Structure of Scientific Revolutions, Part Three (Thomas Kuhn)

**Decisions:** Spine question: what could a funder or panel know in the present tense that sorts a Neptune from a Vulcan, and what did the 1965 London debaters say. Opened on Lakatos's own imaginary-planet story (telescope grant, dust cloud, satellite), flagged as his invention, then ran the real pair (Le Verrier's Neptune and Vulcan, ended by Einstein's 43 arcseconds). Ordered the debate as Lakatos's mob-psychology charge and research-programme test (Prout run to its end, Bohr briefly), Kuhn's 1970 reply (values not rules; variability of judgment as risk spreading), Feyerabend (tenacity, proliferation, telescope and physiological optics out of phase), then Kuhn's later disowning of the strong programme and local incommensurability. Verdict by claim: the three answer different questions (record, variance, rivals); none gives a rule for the present tense, and Kuhn's portfolio argument justifies variance in a field, not any one grant. Narrator's test for panels (what did the rescue hypotheses predict that was then checked; what first result would embarrass the rival) labelled as the narrator's. Constructed three-application panel case flagged as constructed. Callbacks to 058 (NIH framework, Popper), 059 (the shared instrument). No BLOOM aside.
**Verification:** Read in full text this session from archive.org copies: Criticism and the Growth of Knowledge (1970) including the preface (Bedford College, 11 to 17 July 1965; symposium of 13 July; Watkins stepping in), Lakatos's essay (imaginary planet story, hard core, positive heuristic, Prout and Bohr, the end of instant rationality, p. 178 mob psychology line used as one short quote, footnote on Feyerabend), Feyerabend's Consolations (Berkeley 1960-61, Cafe Old Europe footnote, tenacity, proliferation, Bohm, Copernicus and the telescope), Kuhn's Reflections on my Critics (values, risk distribution, mob, Lakatos as social-psychological). The Road Since Structure: Harvard Rothschild lecture of 19 November 1992 (damagingly mistaken, strong programme absurd, easy dismissal ignores a real challenge), the incommensurability passages, the editors' note on post-Darwinian Kantianism. Kuhn's five values and the Copernicus, Ptolemy and oxygen examples from the posted 1977 essay text. Via fetched summaries: Vulcan and Mercury chronology (1859 residual 43 arcseconds, Lescarbault, 2 January 1860, 1878 Watson and Swift, Campbell and Perrine 1908), Feyerabend's later book and the planned joint book (Stanford Encyclopedia). Stated from training at hedged precision: Galle finding Neptune within the first night, Lescarbault as country doctor. The NIH 2025 framework factor names come from memory and 058.
**Traps & dead ends:** The attributed line "I am not a Kuhnian" was searched for in the Road Since Structure text and not found, so it is reported as unfound and not quoted. Direct PDF fetch of Feyerabend returned binary; archive.org text for the lending-restricted copies returned 401, but another copy of the volume downloaded. The Kuhn 1977 essay page was truncated after the simplicity section, so the risk-spreading claim rests on the 1970 reply.
**Open questions:** (AFK) Read Against Method and the Kuhn 1977 essay in full. (AFK) Confirm Galle's date and Lescarbault's biography against a primary source. (AFK) Read the Road Since Structure chapter on local incommensurability in full. (HITL) Whether the constructed three-application panel chapter is too schematic for a walking listen.
**Artifacts:** episodes/060-kuhn-structure-of-scientific-revolutions-part-three-lakatos-feyerabend-reception.md (about 5,850 words including frontmatter, lint clean); queue.md (item 4 checked off, order-of-record points to item 5).
**Context:** Unattended Routine run, 8 October 2026. Pre-flight needed a routine fast-forward of local main. One episode push; the Build site commit appeared within about two minutes and site/feed.xml on origin/main carries the 060 title. Sign-off promises item 5, Polanyi, The Republic of Science (1962).

## [2026-10-09] — Routine: Episode 061, The Republic of Science (Michael Polanyi)

**Decisions:** Spine question: what does the jigsaw picture of mutual adjustment license a funder or panel to do, and what does it assume about the table. Opened on the puzzle and the pea-shellers, placed Polanyi in the Bernal debate, then ran his one long case (the Royal Society's 1945 survey of neglected subjects, the Manchester chairs) to its end. Steelmanned with three claims (information, unpredictable use, self-renewing authority) and gave Bernal's side its best form; separated Lysenko (dictating conclusions) from Bernal's proposal (directing topics). Case against: the policing assumption (Begley and Ellis, Open Science Collaboration), the plausibility filter as both defence and suppressor (callback to 059 Marshall), and follow-the-winners as a rule that depends on prior allocation (bridge to 062 Merton). Verdict by claim: coordination in discovery holds, governance varies by how fast a field corrects itself, allocation is weakest but unreplaced. Narrator's test for panels (which neighbourhood vouches for the merit) labelled as the narrator's. Constructed twenty-member panel case flagged as constructed. No BLOOM aside.
**Verification:** Read the essay in full from a posted copy of the Minerva text (jigsaw, pea-shellers, three merit standards, overlapping neighbourhoods, Rayleigh 1947, Darwin memorandum and Egerton circular, Manchester chairs, Vice-Chancellors' memorandum of July 1946, Brains Trust January 1945, Planck eleven years, authority and tradition, Burke and Paine). One quote used: the 'kill or mutilate' line (13 words), plus the short 'impossible and indeed nonsensical' fragment. Read Fehér's essay for the Bernal debate (Bernal on pure science as snobbery, Association of Scientific Workers manifesto, Polanyi's 1935 Soviet visit, 1942 Lysenko address). Via search summaries only: Society for Freedom in Science founders and 1940 date, The Planning of Science pamphlet of 1946, Begley and Ellis 2012 (six of fifty-three), Open Science Collaboration 2015 (ninety-seven percent versus thirty-six percent, about half the effect size), Mirowski's critique (catalogue descriptions). All flagged in the script. Polanyi's move from the laboratory in the late 1940s is hedged.
**Traps & dead ends:** Springer and kfki pages for McGucken and a second Fehér copy were not fetchable (redirect, 503); a polyanyiana.org PDF of Fehér downloaded. No source found placing Hayek in the Society, so Hayek is not used. The Guston Minerva piece could not be found and is not cited.
**Open questions:** (AFK) Read McGucken's Minerva history of the Society and Bernal's book directly. (AFK) Read Begley and Ellis and the Open Science Collaboration paper in primary form. (AFK) Confirm the founding membership of the Society. (HITL) Whether the episode leans too heavily on the replication literature given item 7 and later items cover related ground.
**Artifacts:** episodes/061-polanyi-republic-of-science.md (about 5,680 words including frontmatter, lint clean); queue.md (item 5 checked off, order-of-record points to item 6).
**Context:** Unattended Routine run, 9 October 2026. Pre-flight needed a routine fast-forward of local main. One episode push; the Build site commit appeared within a few minutes and site/feed.xml on origin/main carries the 061 title. Sign-off promises item 6, Merton on priority (1957) and the Matthew effect (1968).

## [2026-10-12] — Routine: Episode 062, Priorities in Scientific Discovery and The Matthew Effect in Science (Robert K. Merton)

**Decisions:** Spine question: when credit goes to the credited, is that a distortion or a rational prior, and what do the natural experiments say a funder should do about it. Opened on Darwin's June 1858 letters (from Merton's own quotations), then the 1957 argument (recognition as the only property; bystander indignation; Cavendish), then the 1968 effect and the forty-first chair, then Strevens's defence as the steelman, then three tests (Cole summaries, Azoulay-Stuart-Wang HHMI design, Bol/de Vaan/van de Rijt threshold). Verdict by claim: 1957 well supported; 1968 effect on credit real but small, short and largest where quality is hard to read; funding-threshold compounding is the one to worry about but measured in one programme. Distinguished credit-for-a-paper from funding-after-a-threshold as different phenomena. Narrator's panel rule (treat within-noise ties as ties) labelled as the narrator's. Constructed applicant pair flagged as constructed. Callbacks to 061 (Polanyi's jigsaw, Schuster question). No BLOOM aside. Ran 6,563 words including frontmatter, slightly over the ceiling.
**Verification:** Read from a JSTOR scan: Merton 1957 opening survey, norms, reward system and eponymy, the Darwin and Wallace section, Euler/Lagrange, Cavendish/Water Controversy, Galileo. Not read: its multiples section and closing pages. Read in full: Strevens, The Role of the Matthew Effect in Science (quotes Merton 1968 with page refs; source of laureate remarks, Merton's attention explanation). Read: Azoulay, Stuart and Wang NBER working paper 18625 (design, 443 investigators 1984 to 2003, 2,375 controls, 24 on 68 citations, 72nd to 81st percentile, forty-first chair and definition quotes). Bol et al. via the PNAS abstract only (via Europe PMC). Cole 1970 and Cole and Cole 1973 via search summaries and a Nature review. Merton 1968 itself never obtained. Zuckerman acknowledgement via a biographical summary. Stated from training and flagged: Darwin's child dying that week, Merton's self-fulfilling prophecy of 1948. Strevens's publication year given as mid-2000s in the script text only as 2006.
**Traps & dead ends:** Berkeley-hosted Merton PDF was a CalNet login page; science.org 403; PMC page for Bol was a reCAPTCHA; Scribd failed to load. The Washington copy of Merton 1957 was HTML but the joelvelasco.net PDF was the real scan.
**Open questions:** (AFK) Obtain Merton 1968 and confirm the quotations and the laureate remarks. (AFK) Read Bol et al. tables and Cole 1970 in primary form. (AFK) Confirm the Azoulay figures against the Management Science version. (AFK) Confirm the date of Charles Waring Darwin's death against the letters. (HITL) Whether the episode, 6,563 words, is acceptable at the top of the range.
**Artifacts:** episodes/062-merton-priorities-and-the-matthew-effect.md (6,563 words including frontmatter, lint clean); queue.md (item 6 checked off, order-of-record points to item 7).
**Context:** Unattended Routine run, 12 October 2026. Pre-flight needed a routine fast-forward of local main. One episode push; the Build site commit appeared within a few minutes and site/feed.xml on origin/main carries the 062 title. Sign-off promises item 7, Azoulay, Fons-Rosen and Graff Zivin on star deaths.

## [2026-10-13] — Routine: Episode 063, Does Science Advance One Funeral at a Time? (Azoulay, Fons-Rosen and Graff Zivin)

**Decisions:** Spine question: what does a famous person do to a field by being in it, and what changes when they are gone. Opened on Planck's sentence and Samuelson's 1975 compression, separating the generational-replacement mechanism (tested by Hull et al. and mostly not supported) from the gatekeeping reading the 2019 paper tests. Walked the design on the paper's own Herskowitz yeast example, then results (collaborators about minus 21 percent, non-collaborators plus 8.6 percent, NIH awards plus 11.6 and minus 23), the citation-quantile gradient, the three checks that outsiders enter on central questions with newer references, the disruption result (small revolutions, not Kuhnian), Goliath's shadow (only three of 452 on study sections) and the invisible-college splits. Steelman: gatekeeping may help young fields; the authors decline policy conclusions. Case against labelled as the narrator's: life sciences only, effect concentrated in the younger deaths so it tests premature loss and not Planck's old man, anticipated deaths and estate planning, outsider label limited to US med-school and NIH rosters, author-chosen keywords in the field definition. Constructed heart-failure pathway case flagged as constructed; narrator's panel rule (ask for a record with the method, not in the field) and bridge-fund suggestion labelled as the narrator's. Corrected 059's "about seven percent" in the script. Callbacks to 040 (Collison replacement rate), 058-060 (Kuhn), 061 (Polanyi neighbourhoods), 062 (Merton, forty-first chair). No BLOOM aside.
**Verification:** Read in full the AER January 2019 published text (main text, Tables 1 to 7); coefficients converted to percentages as the paper does. Not obtained: the online appendices, so statements on death-by-cause and age cutoffs are the main text's descriptions. Planck wording, the 1946 Naturwissenschaften article, and Samuelson's Newsweek date from a Quote Investigator page, not the book. Hull, Tessner and Diamond 1978 and the plate-tectonics result via search summaries and a forum post quoting a review, flagged as unchecked in the script. Quote used: a seven-word Planck fragment only. No published critique or replication of the paper found.
**Traps & dead ends:** The first NBER URL guess (w24625) was a different paper; the right one was w21788. A first Build poll matched falsely because 062's sign-off already contains the new title in the feed; verification waited for the Build commit above the episode commit.
**Open questions:** (AFK) Read the AER online appendices (Tables E3 to E10, F, G1). (AFK) Read Hull et al. 1978 and the plate-tectonics study in primary form. (AFK) Confirm Planck's wording in the book. (HITL) Whether the constructed pathway chapter and the three panel levers are too schematic for a walking listen.
**Artifacts:** episodes/063-azoulay-fons-rosen-graff-zivin-does-science-advance-one-funeral-at-a-time.md (6,014 words including frontmatter, lint clean); queue.md (item 7 checked off, order-of-record points to item 8).
**Context:** Unattended Routine run, 13 October 2026. Pre-flight needed a routine fast-forward of local main. One episode push; the Build site commit appeared within a few minutes and site/feed.xml on origin/main carries the 063 entry. Sign-off promises item 8, Bloom, Jones, Van Reenen and Webb versus Collison and Nielsen and Park et al.

## [2026-10-14] — Routine: Episode 064, Are Ideas Getting Harder to Find? (Bloom, Jones, Van Reenen and Webb) against Collison and Nielsen and Park, Leahey and Funk

**Decisions:** Spine question: when progress costs more, is the cause in the thing, in us, or in the ruler. Opened on Moore's law as a treadmill (18x researchers, 6.8 percent a year), ran the paper's cases (aggregate 41x, crops, NMEs, cancer years of life saved, Compustat, Census) and the beta puzzle (0.2 for chips, over 3 aggregate), then objections (Tadepalli; Alston and Pardey and Guzey and Rischel by description only), then the Atlantic survey and the CD index with a constructed worked example, then the two corrections (Macher et al., Holst et al.). Synthesis after the midpoint: three rulers measure three different things; the economists' arithmetic survives, the survey and the disruption curve are the weak legs. Callbacks to 057 (Endless Frontier, which Park's last line quotes), 062 (Matthew effect as narrowing citation), 063 (outsiders), 040 (Collison). No BLOOM aside.
**Verification:** Read in full: Bloom et al. AER 2020 (Stanford copy; Table 7, Moore's law, crops, medicine, firm-level, conclusion). Park et al.: Nature page abstract, references and extended-data legends; main text from arXiv v5 preprint (patent count 3.5M in preprint, 3.9M in Nature). Holst et al. 2024 arXiv preprint read in full. Macher, Rutzer and Weder via WebFetch summary of arXiv v1 (88 percent, 0.39 vs 0.09, 38 percent vs under 2 percent); Research Policy 2024 publication from search listings. Atlantic essay NOT reached (403): survey details from a Cummings blog excerpt and search summaries (93 physicists, 37 to 47, near-constant rate phrase). Tadepalli (Asterisk, Oct 2025) via fetch summary. Alston and Pardey, Guzey and Rischel by search description only. CD index formula stated from training knowledge; worked example flagged as constructed.
**Traps & dead ends:** Atlantic, Forbes, New Things Under the Sun, ageconsearch returned 403; web.archive.org reset. A first Build poll matched falsely because 063's sign-off already contains the title; waited for the Build commit above the episode commit.
**Open questions:** (AFK) Read the Atlantic essay directly and check its Nobel-lag and baseline handling. (AFK) Read the Nature main text and Macher et al. in full; look for a Park, Leahey and Funk reply to Holst. (AFK) Read Alston and Pardey and Guzey and Rischel. (HITL) Whether 058 to 064 are dense for a walking listen.
**Artifacts:** episodes/064-bloom-jones-van-reenen-webb-are-ideas-getting-harder-to-find.md (6,028 words including frontmatter, lint clean); queue.md (item 8 checked off, order-of-record points to item 9).
**Context:** Unattended Routine run, 14 October 2026. Pre-flight clean. One episode push; Build commit f7455da carries the 064 entry in site/feed.xml. Sign-off promises item 9, the study section (Pier et al., Fang and Casadevall, Bhattacharya and Packalen, programme-manager model).

## [2026-10-15] — Routine: Episode 065, The Study Section (Pier and colleagues; Fang and Casadevall; Bhattacharya and Packalen)

**Decisions:** Spine question: if a study section cannot rank the good from the excellent, what should replace it, and which failure does each replacement fix. Opened on the Pier mock panels run to their end (43 reviewers, 25 R01s, ICC 0, alpha 0.024, within-reviewer 0.17 versus between-reviewer 0.03), then Li and Agha against the Fang, Bowen and Casadevall restricted reanalysis (same data, different range), then the mBio lottery, New Zealand and Swiss practice, Gross and Bergstrom's contest model, four objections (training fix, lost critiques, screen noise, ruler), Bhattacharya and Packalen's second ruler, the ARPA programme-manager model. Synthesis after the midpoint: noise, ruler and judge are three separate failures with three fixes, none tested against the others. Narrator inferences labelled: manager as one internally consistent reviewer; effort advice for applicants; constructed 100-applications payline example flagged as constructed. Callbacks to 061, 062, 063, 064. No BLOOM aside. Lint caught echoes and tics; the first draft ran 7,900 words and was cut to 6,408.
**Verification:** Read: Pier et al. main text (Gwern-hosted PNAS copy; SI not read); Fang and Casadevall mBio via Europe PMC with Barnett letter and reply; Fang, Bowen and Casadevall eLife (results and start of discussion); Bhattacharya and Packalen NBER w26752 text; Gross and Bergstrom intro and discussion; Sattler et al. abstract and intro; Azoulay, Fuchs, Goldstein, Kearney NBER w24674 (history, selection, challenges). Via fetch or search summary only: Li and Agha (abstract numbers), Liu et al. NZ survey (counts and percentages), SNSF lottery history, HHMI paper (abstract). Heyard et al. read to the start of the method; no Swiss outcomes. The 97 percent breakthrough figure is Bhattacharya and Packalen's footnote; the link to the HHMI paper is flagged in the script as unconfirmed. Quotes: one fragment from Fang and Casadevall, none otherwise beyond paraphrase.
**Traps & dead ends:** pnas.org, journals.asm.org and PMC pages returned 403 or reCAPTCHA; curl needed the proxy CA bundle; Europe PMC full-text XML worked and the Gwern copy gave the PNAS PDF. NBER PDF via WebFetch returned binary; pdftotext on a curl download worked. No search found Swiss lottery results.
**Open questions:** (AFK) Read the Pier SI appendix and search for published replies. (AFK) Read Li and Agha in full and the Azoulay, Graff Zivin and Manso HHMI paper to confirm the 97 percent figure. (AFK) Find Swiss lottery outcome data and the BMJ Open Postdoc.Mobility study. (HITL) Whether 058 to 065 are dense for a walking listen.
**Artifacts:** episodes/065-pier-fang-casadevall-bhattacharya-packalen-the-study-section.md (6,408 words including frontmatter, lint clean); queue.md (item 9 checked off, order-of-record points to item 10).
**Context:** Unattended Routine run, 15 October 2026. One episode push (commit 865d7df); Build commit 4b72d21 appeared within a few minutes and site/feed.xml on origin/main carries the 065 title. Sign-off promises item 10, Cochrane, Effectiveness and Efficiency, which closes the science series.

## [2026-10-16] — Kevin's session (overnight): new-topic scouting and project audit, part one

**Decisions:** Kevin asked for new valuable topics and an investigation of
ways to improve the project, with learning as the yardstick ("goal is for me
to learn"), and approved the plan: scout, judge, synthesise, write a report,
add the proposed series to queue.md as unscheduled candidates, log the
session. Nothing in the pipeline, the charter, the Routine or the episodes
was changed this session; every improvement is a proposal in the report
(part two) for Kevin to pick from. The one binding addition is a sourcing
pointer for the 16 Oct Cochrane run, in STATE.md's Next step.

**Verification:** Method: eight topic scouts, one lens each (trial-methods
classics; global-health institutions; frontline implementation; medicine's
history and sociology; science essayists in the home lens; fiction read as
peer literature; judgment, noise and forecasting; economics of science),
each checking anchors by web search; 80 unique candidates; a four-judge
panel (listener advocate, grounding skeptic, curriculum editor, learning
scientist). Six project audits (pipeline and build; craft drift; state and
docs hygiene; grounding and sourcing; quality loop and feedback; listener
experience and series design) produced 47 findings, each handed to an
independent refuter with repo access: 42 survived, 5 were refuted, and most
severities were downgraded. Facts the refuters confirmed by re-measuring:
CI is healthy (66 of 69 builds green, the 3 failures on 26 Aug before the
Routine era; one Episode commit on every weekday 24 Sep to 15 Oct, none
doubled, Build commit 11 to 19 s after each). The Routine runs on the
environment's default model, not the one Kevin's day sessions use. Seven of
the nine nutrition episodes never read their named anchor in primary form,
though 13 of 14 spot-checked figures in 053 match the primaries. Titles have
grown from about 100 to 222-310 characters. A narrated sourcing paragraph
("For the record, here is how this episode was grounded") has closed every
episode since 060, growing from 129 to 227 words, and the charter does not
mention it. The closing question has re-formed into "The question to carry
into X is" in 7 of the last 8 episodes. STATE.md is 93 percent history.
GitHub Pages renders episodes/*.md through Jekyll as unstyled duplicates
(no .nojekyll). The Routine's step-6 grep of feed.xml for the new title can
be satisfied by the previous episode's sign-off text. From the cloud egress,
Europe PMC REST, OpenAlex, arXiv, Gutenberg, NBER and gwern PDFs work;
bmj.com, jamanetwork, pnas.org, science.org, scholar.archive.org,
web.archive.org and PMC behind reCAPTCHA do not. Cochrane 1972 exists online
only as a 94-page image-only Nuffield Trust scan (pdftotext returns nothing;
the Read tool renders it page by page).

**Traps & dead ends:** One workflow was capped at two concurrent agents by
the 4-CPU container; splitting the same work into four workflows ran eight.
Agent outputs over about 30 KB cannot be passed on as workflow arguments;
details went to a scratch JSON file and only an index was passed.

**Open questions:** (HITL) The report's questions for Kevin (a title cap,
the narrated bibliography, a cold second-reader step before publish, a
one-minute feedback channel) arrive in part two. (AFK) The 16 Oct run reads
the Cochrane scan via the Read tool's pages parameter, per STATE.md.

**Artifacts:** PROJECT_LOG.md (this entry); STATE.md (snapshot rewritten in
place, Next step carries the Cochrane route). Part two adds
reviews/2026-10-16-topics-and-improvements.md and a candidate section in
queue.md.

**Context:** Session of 16 Oct 2026, 00:00 UTC onward, attended at the
start. About 8 million subagent tokens across 65 agents so far (scouting
1.2 M, audits and verification 6.4 M; panel and synthesis still running when
this entry was written). Kevin's brief, in his words: "new valuable topics
and investigation of ways to improve this project"; "high quality insightful
summaries ... goal is for me to learn"; "I approve".

## [2026-10-16] — Kevin's session (overnight): new-topic scouting and project audit, part two

**Decisions:** None taken; everything below is a proposal for Kevin. The
report is reviews/2026-10-16-topics-and-improvements.md: five proposed
series (the analysis plan; the judge and the formula; the view from
headquarters; global health as an institution; making doctors), a pool of
ten interludes, 25 ranked improvements in three groups (do now with no
decision; needs Kevin; later), five dismissed findings with the refuter's
reasons, and five questions only Kevin can answer. The top three series are
scoped at the end of queue.md under "Proposed next series", with hyphen
bullets and no checkboxes so the fall-through rule cannot pick them up.
Recommended order after the Doers: the analysis plan first, as the layer
under the evidence series and the sequel to 065.

**Verification:** Panel of four judges over 80 candidates (listener
advocate, grounding skeptic with web spot-checks, curriculum editor,
learning scientist); 76 survived, 4 vetoed by two or more judges
(task-shifting constellation, his own literature; Lewis Thomas, lending-only
texts; Yes Minister, no checkable script; Bosk alone, no open text). Top
single candidates by weighted score: the Indian monitoring constellation
(9.3), can anyone predict the trial (9.2), Ware's ECMO trial (8.4), the
adjustment constellation (8.4). Improvements: 42 findings confirmed by an
independent refuter with repository access, 5 refuted (a daily density
question at the done skill; synthesis episodes closing each series; a
charter density rule; a question frontmatter key; short interlude formats).
The refuters re-measured every number used in the report.

**Open questions:** (HITL) The five in STATE.md: the narrated closing
source paragraph (keep, page-only, or log-only); a title cap; digits
written out or years and decimals exempt; a one-line "listened" issue from
the phone; a silent-failure watchdog issue. Also whether to pin the
Routine's model. (AFK) The do-now group in the report's Part B is written
to be applied by a day session in about a working day: lint families, three
charter sentences, the held-text sourcing rule and a dated routes file, a
cold second-reader step, FRAMES.md, the STATE rewrite and done-skill
wording, the document reconciliation, .nojekyll.

**Artifacts:** reviews/2026-10-16-topics-and-improvements.md (13,675
words); queue.md (pointer under Candidate next series; the proposed section
at the end, 1,947 words); STATE.md (snapshot names the report; Open (HITL)
block rewritten as six numbered questions); this entry.

**Context:** Session of 16 Oct 2026, 00:00 to about 02:15 UTC. Totals from
the session record at 02:06 UTC: 2.7 million output tokens, 4.5 million
input tokens, 78 million cache-read tokens, across 66 agents plus the main
session. The user asked mid-session why his usage meter showed nothing;
the answer lives in the chat, not here.

## [2026-10-16] — Episode 066, Cochrane, Effectiveness and Efficiency (Routine)

**Decisions:** Treated the book as an inventory of untested practice plus a weaker diagnosis (inflation) and prescription, and made the case against rest on that split, since the inventory is well supported and the other two claims are by his own account short of proof. Gave the cervical smear its own chapter with Peto 2004 set against his 1972 doubt, stating that the evidence that vindicated screening was cohort-level, not a trial. Tied the Scottish length-of-stay scatter to 065's study section and the U/non-U complaint to the Bush (057) and Polanyi (061) episodes as the series closer. Left the script longer than the 6,500 ceiling (7,702 words with frontmatter) after cutting a 9,800-word first draft by about a fifth; each remaining chapter carries a worked example. No quotation from the book beyond a few words (copyright). No BLOOM aside.
**Verification:** The Nuffield scan was read page by page in five Read calls (1-94); every figure and anecdote from the book was checked against those pages, including a reread of the Guy's Hospital Bedford trial, where tolbutamide showed slightly fewer cardiovascular deaths (caught and corrected in review of the draft). Later history came from search summaries only: Mather 1971 (343 randomized) and 1976 (450; twenty-eight day mortality 12 versus 14 percent, 330 days 20 versus 27) from BMJ abstracts; Peto 2004 abstract; UGDP controversy summaries; the 1979 essay and wooden spoon via editorials and Cochrane Collaboration history pages, with the exact 1979 wording not seen; Chalmers bibliography about 3,500 reports, 1985; Collaboration founded 1993; Greenhalgh, Howick and Maskrey 2014 summary. The script states these limits in its closing source paragraph. No contemporary review of the 1972 book was found.
**Traps & dead ends:** A first draft ran 9,822 words and carried several misreadings and overreaches (Hofvendahl's country, "placebo" in the Elwood trial, the tolbutamide direction, the claim that the Mather result "just happened" to be overtaken by technology); all were fixed in the rewrite. The lint's reported line numbers run one line behind the file.
**Open questions:** (AFK) the 1979 essay in primary form; One Man's Medicine; the full Mather 1976 and Peto 2004 papers. (HITL) the six numbered questions in STATE.md stand, including whether 058 to 066 are dense for a walking listen and whether 7,700 words is too long.
**Artifacts:** episodes/066-cochrane-effectiveness-and-efficiency.md (7,702 words with frontmatter, lint 0 repeats 0 tics); queue.md (item 10 ticked); STATE.md snapshot; this entry. Build commit "Build: site + feed [skip ci]" appeared on origin/main within about a minute and the feed contains the new title.
**Context:** Routine run of 16 Oct 2026 after the same night's scouting and audit session; nothing in the pipeline, charter or lint was changed. The series "science as an institution" is now complete; the next episode opens "How evidence was invented".

## [2026-10-16] — Kevin's session: no narrated bibliography from 067

**Decisions:** Kevin answered the review's first question: "no need for
bibliography moving forward." From 067 on, episodes do not close with a
paragraph on what was and was not read; thin sourcing is said inline in one
clause, and the full account stays in this log's Verification field, where
it already lives. 060-066 stand as published (no-rewrite rule). The ruling
is in SCRIPT_STYLE.md (Grounding, and pre-flight item 4), STATE.md (decision
of record, and a line above Next step so the Monday run sees it before
reading 065 and 066, which both end on one), and the lint.
**Verification:** Three lint patterns added ("for the record"; "how this
(episode) was grounded"; "how much of this I have verified"), written by a
Python script run by path, not a heredoc. They fire on every bibliography
opener in 060-066 and on nothing in 012-059 (all still 0 repeats, 0 tics).
066 (written this morning by the Routine) used the Cochrane scan pointer and
read the book in full; it also closed on a bibliography copied from 065 and
ran 7,700 words with frontmatter.
**Open questions:** (HITL) Questions 2 to 5 of the review and the Routine
model stand in STATE.md. Whether the five proposed series join the order of
record is Kevin's call; until he says so they stay unscheduled at the end of
queue.md and the Routine follows the evidence series (067-074), then Doers
(075-085).
**Artifacts:** .claude/skills/audio-essay/SCRIPT_STYLE.md;
scripts/lint_script.py; STATE.md; this entry.

## [2026-10-16] — Kevin's session: the review's next batch applied

**Decisions:** Kevin: "no worries on those things, just unlock next batch",
so the open choices were taken at the defaults the review recommended: title
cap 105 characters and 15 words (the 28 Aug set); digits written out except
four-digit years and decimals; no listen-issue channel and no watchdog (both
need Kevin's participation or break the no-notifications rule); the three
scoped series scheduled after Doers (analysis plan 086-095, the judge and the
formula 096-105, the view from headquarters 106-115). Applied: lint families
(closing formula, narrated checklist words, delayed importance, session
residue, citation-first openers), a structure check (sign-off shape, title
cap) and a digit check, all counted as tics so the gate string is unchanged;
FRAMES.md and scripts/frames.py; held-text sourcing rule and
references/sourcing-routes.md; cold-read step SKILL.md 2c; proximity rule
copied into the charter; next-work rule fixed to the Order of record;
done-skill limits (one snapshot, at most twelve open questions, STATE under
150 lines, length reported as numbers, never as a question); STATE.md cut from
57,754 to 7,145 bytes with the old file archived verbatim; queue.md curriculum
lines for the evidence and Doers series; .nojekyll and a root redirect;
site/** added to the build trigger; shallow-clone builds reuse committed
pubDates; config.json description; Routine step 6 verifies by GUID and step 4
names the title cap (update_trigger; schedule, connector and model unchanged).
**Verification:** New lint families fire only on genuine drift across
012-066 (42 "this hour", 14 closing-formula, 5 session residue, the rest
single digits); no episode fails the sign-off check; 37 of 55 titles since
012 exceed the new cap and stand. A shallow-clone build reproduces all 67
committed pubDates (it would have re-dated 50 before). frames.py: two keys
tightened after false matches (Christensen's "disruptive" in 024, a generic
"research programme" in 025). An independent three-lens review of the diff
was still running at commit time; its fixes, if any, follow in a separate
commit before Monday's 067 run.
**Open questions:** In STATE.md, now nine bullets.
**Artifacts:** CLAUDE.md, STATE.md, queue.md, config.json, FRAMES.md,
index.html, .nojekyll, .github/workflows/build.yml, scripts/lint_script.py,
scripts/frames.py, scripts/build_site.py, .claude/skills/audio-essay/SKILL.md,
SCRIPT_STYLE.md, references/sourcing-routes.md, .claude/skills/done/SKILL.md,
archive/STATE_previous_snapshots_08sep26-16oct26.md; this entry.

## [2026-10-16] — Kevin's session: review fixes to the batch

**Decisions:** An independent three-lens review of the batch (Monday-run
simulation, code, content) found no blocker and several should-fixes, all
applied: the digit check now ends tokens on a digit, so a year before a comma
("In 1847,") passes; the lint catches 066's closing variant ("carry the six
boxes into the routine"); reported line numbers are exact and a malformed
header no longer crashes the lint; the closing-shape check reads the last three
paragraphs (065 and 066 put a source list between the closer and the sign-off);
seven FRAMES keys tightened (Parkinson's disease, study section as everyday
context, Licklider's "tight coupling", Kuhn in a Hamming key, generic
"paradigm", Grove's name, Waterlow and Ioannidis outside their frames); the
man-of-one-study frame now carries both essays' mechanisms; the STATE
bibliography decision stands on its own; Nuland and Johnson marked lending-only
for 067; archive.org IDs for Snow and Semmelweis; range and episode-number
corrections. Routine prompt (update_trigger): step 3's fallback now follows the
Order of record, and step 5 runs the SKILL.md 2c cold read and re-lints.
**Verification:** Synthetic scripts: years before commas pass, 43 and 1,987
flag, 8.6 and R01 and ISIS-2 pass; an unterminated header reports tics instead
of a traceback; lint line numbers match grep -n. frames.py table re-run after
the key changes. Build and Pages runs for 997274d were queued at the time.
**Artifacts:** scripts/lint_script.py, FRAMES.md, STATE.md, queue.md,
.claude/skills/audio-essay/SKILL.md, SCRIPT_STYLE.md,
references/sourcing-routes.md; Routine trig_017rhfD6LEfWxb4R7pgTuVTz prompt.

## [2026-10-19] — Episode 067, Snow and Semmelweis (unattended)

**Decisions:** Title in the 105-character form: "Cholera and Childbed Fever (Snow and Semmelweis): ..." with the two authors joined by "and". The queue's framing (why one was believed and the other was not) was revised in the script itself: from the reception as I understand it, neither was believed in their lifetime, so Chapter Five reverses the premise and puts the difference in the afterlife and in Semmelweis's polemical book. No BLOOM aside and no proximity issue; the closer is a question about routine-data gaps with a third comparison group, reworded after the cold read to avoid the "next ten" construction of 065 and 066. No closing bibliography (16 Oct ruling); thin sourcing said inline.
**Verification:** Read in full from archive.org text: Snow 1855 (b28985266; Broad Street inquiry, Tables VII to X, the pump-handle caveat, the Thames Ditton move in 1852, the silver nitrate test) and Semmelweis 1861 (b33953740, German OCR; the 1846 to 1848 tables, Kolletschka, the October and November 1847 relapses, the Michaelis letter and his end, Skoda, Hebra, Scanzoni passage). Every spoken figure is from those texts; Semmelweis passages are the writer's own paraphrase, no quotes. From training knowledge, hedged in the sentence: official reception of Snow's pump theory, Snow's death in 1858, Koch in the 1880s; Nuland and Johnson not held. Semmelweis's 1846 second-clinic rate computed as 105 of 3,754 (2.8 percent); OCR percent signs were garbled so rates were recomputed from the counts. Cold read: first call failed (placeholders unfilled in my brief), resumed once with file paths. Applied R1 (cut three signposts), R4 (closer reworded), R5 (pump-count list, Braun, third-row callback), R6 (case-against paragraphs merged). Not applied: R2 density cuts (advisory), Chapter One birth counts kept.
**Traps & dead ends:** Snow OCR doubles spaces; normalise with tr before grepping. Semmelweis OCR garbles decimals ("2.,,"), so recompute from counts. Lint's digit check fired on comma numbers; written out.
**Open questions:** (AFK) Snow's and Semmelweis's reception rests on memory of the standard account; a held text of Nuland or Johnson, or the Cholera Inquiry Committee report, would confirm Chapter Five. (HITL) Whether the reversal of the queue's premise suits the series.
**Artifacts:** episodes/067-snow-semmelweis-cholera-and-childbed-fever.md (5,818 words); queue.md ticked; Build commit bd100ea verified by GUID in site/feed.xml.
**Context:** First episode under the title cap, digit rule and cold-read step; lint clean on the first full pass after rewrites. 067's sign-off promises Fisher (item 2): randomisation and the lady tasting tea, The Design of Experiments (1935), with the tobacco denial as case against.

## [2026-10-20] — Episode 068, Fisher, The Design of Experiments (unattended)

**Decisions:** Built around the tea experiment's logic (count before pouring, sugar as the failure case, randomisation guarantees validity not equality), then Darwin's maize as the worked case run to its end (t 2.148 against 2.145; Galton's rearrangement 5.171; the randomisation count 5.267 percent), Fisher's factorial argument, and the tobacco dispute as case against. Argued that Cornfield wins on Fisher's own "reliable method of procedure" sentence, and that Fisher moved the plausibility line for the as-if-randomised supposition to suit his conclusion. Application: the unit randomised must be the unit the standard error counts (made-up school-feeding example, flagged in speech). No BLOOM aside. Sign-off re-uses the series format; closer is a test, not a question.
**Verification:** Read from archive.org text: Fisher, Design of Experiments (ninth edition, 1971; carries the 1960 section 12.1), including chapters I to V and the factorial sections; every spoken figure (seventy, 924, thirty-five of seventy, t 2.148, 9.746, 863, 5.267, 5.171, the 16-mixture 96-test design) is from it. Salsburg, The Lady Tasting Tea, held as text for the tea story (via Hugh Fairfield Smith), Rothamsted and the Broadbalk weeds story, and the smoking dispute (Cornfield 1959, Berkson, Neyman, inhalers, twins), all attributed to Salsburg. Nature 1958 letter: only the opening sentence reachable. Cornfield 1959 itself not held. From memory, hedged in the sentence: other tellings placing the tea at Rothamsted, Fisher's tobacco consulting. Darwin pair signs (two negatives, 67 and 48) inferred from the OCR table and checked against the sum 314. Cold read: ran with file paths (subagent). Applied R1 (two cuts), R3 (softened counts to "about thirty", "very many millions"), R4 (dropped "this show is written for"), R5 (t named before use; "those two sentences"). Not applied: R2 (advisory), R6 reading-advice paragraph kept as the verdict, R4 sign-off kept because the lint requires it.
**Traps & dead ends:** nature.com article page loads but is paywalled after the first sentence; Adelaide digital library PDF 404; Europe PMC has no full text for the Cornfield reprint commentary.
**Open questions:** (AFK) Cornfield 1959 and Fisher's Nature "Cancer and Smoking" in full text would firm Chapter Six; Hill 1965 next but one. (HITL) Whether the reading-assignment paragraph suits the show.
**Artifacts:** episodes/068-fisher-the-design-of-experiments.md (6,126 words); queue.md ticked; Build commit 3b0e242 verified by GUID in site/feed.xml.
**Context:** 068 sets up 069 (Fisher against Neyman) through section 12.1 and the five percent convention. It plants the "reliable method" sentence for Hill's 070 and the unit-of-randomisation test for the SAP half of 069.

## [2026-10-21] — Episode 069, Fisher versus Neyman and Pearson (unattended)

**Decisions:** Built as a duel in order: Fisher's tea (seventy ways, the null defined, "usual and convenient", second-kind error declared meaningless for simple tests), Neyman and Pearson's rules of behaviour, then the late Fisher's attack and the 1960 section 12.1 against them, then Gigerenzer's hybrid, a case-against chapter on Gigerenzer's own paper (psychology-only evidence, remedy fits badly, Loftus), the ASA 2016 principles, and the SAP application (a constructed trial with 290 per arm; label each 0.05 as an error rate or a reading). Gigerenzer's plate example kept, with his false-alarm slip mentioned in one clause. Planted frame: the null ritual, same words. No BLOOM, no proximity issue. Closer is a March/October contrast, not a test or question.
**Verification:** Read as text: Gigerenzer 2004 (library.mpib-berlin.mpg.de PDF), Neyman and Pearson 1933 (errorstatistics.com searchable scan), Fisher 1935 ninth edition (archive.org), ASA 2016 press release only (amstat.org; the statement itself not held, said in the script). Fisher 1955 and 1956 quotes ("absurdly academic", "childish") are via Gigerenzer and attributed so in the sentence. Lehmann's convergence view from memory, hedged. Constructed trial: 290 per arm from the normal approximation (70 vs 80 percent, alpha 0.05, power 0.8); 77 vs 70 gives p about 0.06, interval about minus 0.3 to 14 points, computed by hand. Cold read (subagent, file paths): applied R1 (three grading lines cut), R4 (dropped "Last episode's test" paragraph, reworded closer), R5 (plate slip shortened, readings named), R2 partial (Waller and Loftus figures cut). Not applied: R3 blanket attribution, R5 recipe paragraph split, R6 cut of Cohen paragraph, Chapter Eight trim.
**Traps & dead ends:** Fisher 1956 (archive.org statisticalmetho0000rona_k0w6 and statisticalmetho00fish) lending-only, 401/403. Design of Experiments djvu text file is named 2015.199572.The-Design-Of-Experiments_djvu.txt, not the identifier. Neyman and Pearson 1933 is reachable at errorstatistics.com though Royal Society is walled.
**Open questions:** (AFK) Fisher 1955 in full text (JRSS B) would confirm the relayed quotes. (HITL) Whether Chapter Eight's protocol detail exceeds the one-aside preference; the episode runs 6,440 words.
**Artifacts:** episodes/069-fisher-neyman-pearson-significance-versus-hypothesis-testing.md (6,443 words); queue.md ticked; Build commit 061f647 verified by GUID in site/feed.xml.
**Context:** 069 sets up 070, the 1948 streptomycin trial (Hill, sealed envelopes, scarcity), promised in its sign-off. The 0.05 is framed as an error rate or a reading, never both unlabelled.

## [2026-10-22] — Episode 070, the streptomycin trial (unattended)

**Decisions:** Built on the paper's own problem order: eligibility as denominator, the envelope (randomness versus concealment, with the same-issue BMJ editorial's alternation argument), the scarcity defence of the lottery and where it fails (no consent recorded; scarcity justifies a lottery, not a comparison), the blinded film panel, then resistance as the finding the headline omits, with the point that only the S versus C contrast is protected by the draw and the resistance grading is observational (callback to 068). Case against: size and scope, the mid-trial change from six to four months of treatment, collapse therapy as co-intervention, the two excluded early deaths, the garbled one-year addendum. No BLOOM, no proximity issue. Cold read applied: R1 superlatives cut, R2 figures trimmed, R5 groups named, R6 villages example cut so the application ends on the concealment test and the border between protected and unprotected comparisons. Not applied: R4 (the closer shape is lint-required).
**Verification:** Read in full from archive.org text (sim_british-medical-journal_1948-10-30_2_4582): the MRC report (design, Table I, treatment, results, resistance, toxicity, discussion, addendum) and the same-issue editorial "The Controlled Therapeutic Trial". Every spoken figure is from it. The one-year table's streptomycin row is garbled in the OCR; only the control figure (24 of 52) is spoken and the gap is said in the script. The "forty of fifty-five" and "thirty-three" general-condition counts are from the text with one OCR repair (33 from "3 (60%)", checked against 60 percent of 55). "Twenty-eight" others in the severity comparison is 41 minus 13, the OCR showing "2g". From memory, hedged in the sentence: later historians finding earlier alternation or random trials; combination therapy trials that followed. Hill 1965 and 1990 not held.
**Traps & dead ends:** The BMJ djvu needs curl -L (a first non-redirected request returned empty). OCR tables are scrambled; counts were cross-checked against the prose.
**Open questions:** (AFK) The excluded early deaths' arm and the one-year streptomycin mortality could be confirmed from the Lancet 1948 or MRC follow-up papers. (HITL) Whether the ethics chapter's reading (no recorded consent, scarcity argument) suits the show.
**Artifacts:** episodes/070-hill-mrc-streptomycin-trial-sealed-envelopes-and-a-scarce-drug.md (5,847 words); queue.md ticked; Build commit 3a6ef5d verified by GUID in site/feed.xml.
**Context:** 070 promises item 5, ISIS-2 and the astrological subgroup (Lancet 1988 is closed from the cloud; write from open restatements and say so inline). The sealed-envelope concealment test and the protected-versus-unprotected comparison distinction are planted for the analysis-plan series.

## [2026-10-23] — Episode 071, ISIS-2 and the astrological subgroup (unattended)

**Decisions:** Built on two demonstrations of what happens to a fair comparison afterwards: ISIS-2's factorial design and additive effects (additivity checked from the abstract's own percentages, 2.8 plus 2.4 equals 5.2), then the zodiac subgroup (Gemini and Libra 150 vs 147; the other ten signs 654 vs 869), then Sleight's three real harms from believed subgroups (anterior vs inferior infarction, HOPE, the North American GUSTO result), the false-negative framing, Peto's three remedies, Lee 1980 as the second mechanism (imbalance inside a slice), a case against the demonstration (loud overall effect, assumed homogeneity of proportional effect, the joke displacing the good question), and a short SAP application. No BLOOM, no proximity issue. Title uses "Collaborative Group" as the author form. Cold read applied: R1 rankings cut, R2 counts paragraphs simplified (rounded the ISIS-2 percentages for the ear, dropped the combination series from the time-window paragraph), R5 odds reduction glossed and false negative named, R6 Chapter Ten trimmed (one paragraph cut), and the factual fixes (pooled comparisons not "alone" groups, dropped Sleight's 9 percent figure, overall P aligned, Libra and Gemini deaths about three hundred, schools not clusters). Not applied: R4 (closer shape is lint-required), R3 for the Lee numbers (abstract is said to be the only text held).
**Verification:** The ISIS-2 paper itself is closed (archive.org Lancet issue sim_the-lancet_1988-08-13_2_8607 is lending-only, 401). Held as text: the PubMed abstract of ISIS-2 (via the connector; every headline count, the time-window odds reductions, the bleeding and stroke figures), Sleight 2000 (Europe PMC XML PMC59592: randomisation by telephone, the CAPP envelope example, anterior infarction errors, HOPE, GUSTO, the sixteen countries and the unreported country results, the 12 signs, forty-subgroups arithmetic) and Peto 2011 (PMC3068511: the Table 1 counts 150 vs 147, 654 vs 869, 804 vs 1016, the selection of the least promising signs, the three remedies, Capricorn). Lee 1980 from its PubMed abstract only. Pieces I computed and said so: the expected 131 to 166 split and the two-spread departure, the 46 percent family chance for twelve looks, the 52 fewer deaths per thousand. From memory, hedged: streptokinase still contested in the 1980s, the label "large simple trial". Not used: the abstract's bleeding and stroke figures (held, not spoken). Reception: only the two insiders' accounts; no dissent found, and the script says so.
**Traps & dead ends:** archive.org djvu, searchtext and docling files for the Lancet issue all return 401. Europe PMC has no full text for Bland and Altman's Bonferroni note or for the 1991 Deykin lessons paper (500). The PubMed connector's get_article_metadata returns full abstracts for pre-2000 items.
**Open questions:** (AFK) The ISIS-2 paper in full would confirm the Sleight and Peto relays and show what the trial itself said about subgroups. (AFK) Lee 1980 in full text. (HITL) Whether Chapter Ten's application suits the show at this length; the cold read called it advice.
**Artifacts:** episodes/071-isis-2-collaborative-group-aspirin-streptokinase-and-the-star-signs.md (5,243 words); queue.md ticked; Build commit 93bc795 verified by GUID in site/feed.xml.
**Context:** 071 sets up 072, the Women's Health Initiative reversal (Nurses' Health Study against the 2002 trial), promised in its sign-off. The false negative, the idea that a subgroup read as an answer removed treatment from people who would have benefited, and the point that randomisation balances on average and not inside a slice are planted for the analysis-plan series.

## [2026-10-26] — Episode 072, the Women's Health Initiative reversal (unattended)

**Decisions:** Built as a reversal in five moves: the cohort case at its strongest (Stampfer and Colditz 1991, Nurses' 1996, HERS 1998 as the first crack), Matthews 1996 run to its end as the healthy-user experiment, the trial (hazard ratios and absolute risks, the 2003 final analysis whose monitoring-adjusted interval reaches 0.97), then the prevalent-user mechanism (Prentice 2005, WHI observational arm) and Hernán 2008's step-by-step walk from 1.42 to 0.67. The timing hypothesis is treated as a subgroup claim with the zodiac of 071 as the test, and the case against attacks both the "cohorts cannot be trusted" retelling and the trial's own limits, with an inside-job caveat (Manson and Grodstein on both sides). Application: a time-zero test for cohort estimates, and prespecifying effect modifiers. No BLOOM, no proximity issue. Cold read applied: R1 signposts cut, R2 and R5 hazard-ratio and covariate lists trimmed, net-nineteen explained as the global index, the supplement example and one imagined-numbers paragraph cut (R6), closer reworded off 071's opener (R4), p-values named by analysis. Not applied: R3 rounding of abstract-sourced decimals (each is said to come from the abstract).
**Verification:** WHI 2002 principal-results paper not held: escholarship.org returns a CloudFront WAF 202 with an empty body (qt3mr6f93p), jamanetwork walled, so every 2002 figure is from the PubMed abstract. Read in full text via the PubMed connector: Hernán 2008 (PMC3731075; every Nurses' re-analysis figure, the 1.42, 0.98, 0.77, 0.67 and 0.68 chain, strata, p values), Manson 2013 JAMA overview (PMC3963523) and Rossouw 2013 commentary (PMC3547645; the 40 percent use figure, one third of prescriptions over sixty, 15 percent of WHI observational current users under two years, KEEPS and ELITE status, the thirty-thousand-woman estimate, the strata counts). Abstracts only: Grodstein 1996, Stampfer and Colditz 1991, HERS 1998, Matthews 1996, Rossouw 2007, Manson 2003, Prentice 2005. Vandenbroucke 2009 and Michels and Manson 2003 not held (title only, said so in the script). From my own arithmetic: one woman in five hundred a year (19 per 10,000), "more than two in five" (157 of 355). First names Meir Stampfer, Graham Colditz, Karen Matthews, Francine Grodstein from memory.
**Traps & dead ends:** Europe PMC fullTextXML returns 500 for PMC3731075 although the PubMed connector returns its full text; the connector is the route for NIH-manuscript papers. escholarship.org PDF is behind a WAF challenge from this egress (updates the "Evidence series anchors" note in sourcing-routes.md only by this entry).
**Open questions:** (AFK) The 2002 principal-results paper in full text would confirm the abstract-sourced figures and show how it treated subgroups. (AFK) Vandenbroucke 2009 in full text. (HITL) Whether Chapter Eight's inside-job caveat suits the show.
**Artifacts:** episodes/072-women-s-health-initiative-rossouw-hormone-therapy-trial-versus-cohorts.md (5,589 words); queue.md ticked; FRAMES.md row added (healthy-user effect and the clock); Build commit d90b0d2 verified by GUID in site/feed.xml.
**Context:** Hernán 2008, which the queue listed as closed, is reachable through the PubMed connector. 072 sets up 073, evidence-based medicine as a movement (Guyatt 1992, Sackett, the hierarchy, Greenhalgh 2014, industry capture), promised in its sign-off. The healthy-user effect and the prevalent-user clock are planted for the analysis-plan series.

## [2026-10-27] — Episode 073, evidence-based medicine as a movement (unattended)

**Decisions:** Opened on the two parachute papers (Smith and Pell 2003, the PARACHUTE trial 2018) because each is a joke aimed at a different misreading of the movement, then separated the 1992 claim into three parts (appraisal skill, ranking by susceptibility to bias, decision rule with judgement and patient wishes). Ranking read as a list of named mistakes, with the WHI re-analysis (072) as the case where the rung was not the cause. Greenhalgh's five problems worked one by one, then sorted with Straus and McAlister's three bins; the episode's own argument is that the movement moved epistemic authority from persons to documents and so moved the trust to whoever writes the document. Goodhart planted on the guideline-compliance measures; Kuhn's crisis used once. Case against the critics: remedy at an unfalsifiable level, appeal to expertise, marginal-gains overreach, and the paper never counts harms. No BLOOM, no proximity issue. Cold read applied: R1 (best exhibit, announcement lines cut), R2 (dates and the eighteen and forty-four dropped), R4 (reading lead-in and closer changed), R5 (five problems named before they are described, bins named), R6 (analysis-plan paragraph cut, so the close carries the uncounted-harms question). Not applied: R3 hedges on two-page and four colleagues (PubMed metadata gives pages 71-2 and five authors).
**Verification:** Read in full text: Greenhalgh, Howick and Maskrey 2014 (Europe PMC PMC4056639; every figure on asthma, VTE, washout 3 to 48 per 100,000, the 3679 pages and 122 hours, 37 of 38 and 14 of 36, the Box 2 asks) and the PARACHUTE trial (PubMed connector PMC6298200; 92 screened, 69 not randomised, 23 randomised, 0.6 m, 800 and over nine thousand metres, the Sri Lanka registry). Abstract or metadata only: Smith and Pell 2003, Tonelli 1998, Straus and McAlister 2000, and the titles, pages and indexing of Guyatt 1992 and Sackett 1996. From memory, hedged in the sentence: Guyatt leading the working group at McMaster, the Users' Guides series beginning in JAMA, Sackett's definition and "not cookbook" content, the shape of the hierarchy. Computed: sixteen-fold (48 over 3), about three working weeks (122 hours). Hernán 2008 described from 072 without numbers.
**Traps & dead ends:** Sackett 1996 (PMC2349778) and Straus 2000 (PMC80509) return empty full text through the connector; Europe PMC fullTextXML gives 500 for PMC80509 and PMC300808; archive.org BMJ 1996 issue returns 403. PMC6298199 is only the PARACHUTE correction notice; the trial itself is PMC6298200. The PARACHUTE text and table disagree on the arm sizes (12 and 11), so the script gives only the total.
**Open questions:** (AFK) Guyatt 1992 and Sackett 1996 in full text would firm Chapter Two. (AFK) Straus and McAlister 2000 in full text. (HITL) Whether the satirical opening suits the show; the episode runs 4987 words, near the floor.
**Artifacts:** episodes/073-guyatt-sackett-evidence-based-medicine-and-its-critics.md (4987 words); queue.md ticked; Build commit 7a3a6d4 verified by GUID in site/feed.xml.
**Context:** 073 sets up 074, the replication-crisis closer (Ioannidis 2005, Prasad and Cifu, registration and prespecified SAPs), promised in its sign-off. The uncounted-harms question and the sponsor-learns-the-checklist point are planted for it; the trust-moves-from-persons-to-documents argument is the new frame, not yet in FRAMES.md.
