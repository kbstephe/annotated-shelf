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
