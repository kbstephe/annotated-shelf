# Craft research pass, 24 Aug 2026

Five research reports that fed the SCRIPT_STYLE.md rebuild. The charter is the
operational distillation; this file preserves the detail and sources. Consult it
when a charter rule needs its rationale, or when writing in a new domain.

---

## Report 1: The essay-review tradition (NYRB/LRB, Orwell, Hardwick, Lanchester)

### Signaling importance without stating it

The technique the greats share is displacement of judgment onto structure and
detail, never onto adjectives.

- **Dwell time as emphasis.** The reviewer's attention is the signal. Lanchester
  spends a full paragraph walking through a single worked transaction (his
  mango-trading parable in the LRB piece "For Every Winner a Loser") rather than
  asserting "this is the key mechanism." The judgment ("finance has become
  socially useless") is delivered as an observation about a mechanism, not a
  verdict.
- **Placement.** What's said last, or immediately after the strongest evidence,
  reads as the point.
- **The pivot sentence.** A short, plain declarative dropped after a long
  expository run; the register drop itself signals weight.
- **Juxtaposition.** The book's claim next to a fact, an anecdote, or a rival
  book's claim, letting the contradiction do the arguing.
- **The specific worked example carries generalizations.** Walk one trade or one
  career all the way through and let the generalization be the reader's own
  conclusion.

### Structure — the review as essay

- NYRB's founding idea, per Robert Silvers: get good writers and use books as an
  excuse to let them take off and talk about a subject. The book is occasion,
  not container.
- **Delayed entrance of the book.** In Lanchester's "For Every Winner a Loser"
  the two central books don't appear until roughly a third of the way in. The
  reviewer's own argument is the spine; the books arrive once the frame is built.
- Thesis openings suit abstraction-heavy subjects (finance/systems); scene
  openings suit character/institution-driven subjects (Didion, Malcolm).
- Silvers pushed writers for MORE summary, not less — readers need to know
  what's in the book to trust the argument about it. The failure mode is
  undifferentiated summary (block recap + verdict paragraph), not summary
  itself. The fix: interleave — every fact introduced already doing
  argumentative work.

### Voice

- Earned authority is demonstrated through command of specifics, not claimed.
- First person as a lens ("what struck me"), not confession.
- Clive James's standard: "highly intelligent without making mysteries,
  wide-ranging without lapses into eclecticism... hardbitten yet receptive,
  colloquial yet compressed." And: "Any critic who complains about the monotony
  of what he is being paid to look at is really complaining about the condition
  of his own soul."
- Didion: "My mind veers inflexibly toward the particular." Dispassion as
  technique — moral weight accumulates from arrangement, not adjectives.

### Anti-patterns named by the greats

- Orwell, "Confessions of a Book Reviewer" (1946, verified from source):
  reviewing is "in essence humbug" when reviewers manufacture reactions;
  praising King Lear and a thriller with the same word empties the vocabulary;
  his fix — ignore most books and give very long reviews to the few that
  matter. Stock phrases reviewers reach for "like iron filings obeying the
  magnet": "a book that no one should miss," "something memorable on every
  page," "of special value are the chapters dealing with."
- Hardwick, "The Decline of Book Reviewing" (Harper's, Oct 1959; wording via
  Harper's retrospective, not the full original): reviewing as a "hidden
  dissuader" — praise so undifferentiated it amounts to a campaign against
  caring about books. "A genius may indeed go to his grave unread, but he will
  hardly have gone to it unpraised." Silvers credited this essay as the direct
  inspiration for founding the NYRB.

---

## Report 2: Internet-native criticism (Rao, ACX, Siracusa, Levine, Gwern)

Twelve operational rules:

1. **Take the conceit dead seriously.** Rao opens the Gervais Principle by
   claiming The Office "is a fully realized theory of management" that
   "falsifies 83.8% of the business section" — fake-precise statistic as
   weapon. Never signal "I know this is silly"; the sincerity/triviality gap IS
   the humor.
2. **Mint reusable vocabulary.** Capitalized terms (Sociopath/Clueless/Loser)
   with edges the listener can apply to their own workplace a week later.
3. **Diagrams-in-prose.** Build an explicit taxonomy/2x2/life-cycle in words a
   listener could sketch from audio alone; reuse it as a checkpoint.
4. **Write to sound like live discovery.** Rao on his own method: language as
   "a passive recording medium in a feedback loop" (close paraphrase); the
   essay as performance, not transmission.
5. **Delay the thesis; change your mind on the page.** Scott Alexander lays out
   ~fourteen examples in "Meditations on Moloch" before stating the principle;
   often the real thesis arrives two-thirds through; sections sometimes end
   without stating their point, trusting triangulation; pieces end abruptly
   without summary.
6. **The book is a lens on a pre-existing question.** ACX contest guidance:
   the strongest entries use the book as an excuse to write an essay about a
   related topic.
7. **Length is earned through nested questions only.** Each answer spawns a
   harder question; padding is restating a landed point.
8. **Worked examples at full length.** Siracusa's ~26,000-word OS X reviews:
   one specific mechanism walked all the way through, chunked with deliberate
   break points. Levine: one derivative structure explained until fully
   legible, wit continuous rather than as punctuation.
9. **Importance via callback, register shift, or example payoff — never
   announcement.** Levine's deadpan: flatness reads as weight because it
   breaks the register.
10. **Humor as continuous texture**, not demarcated comic relief.
11. **Detours must return carrying something the spine needed** — or compress
    to the single dramatizing detail (Tanner Greer's evolution from wholesale
    quotation to the one sharp fact).
12. **Widen the frame section over section** (person → team → org → system);
    scale creates momentum.

Sources: ribbonfarm.com (Gervais Principle; Rediscovering Literacy),
hardlyworking1.substack.com (analysis of Scott Alexander), astralcodexten.com
contest rules, marco.org/2012/07/25 (Siracusa review-review), gwern.net,
Harvard Magazine on Matt Levine.

---

## Report 3: AI-written podcast/essay pipelines — precedents

- **NotebookLM Audio Overviews**: the dominant comparison point. Rob Allandale's
  teardown names the two-host "dramaturgy" skeleton and tells ("let's dive in",
  "the document says"). What works: tight source-grounding, the TTS itself
  contributing prosody. No fix found for the formulaic dialogue skeleton.
- **Washington Post "Your Personal Podcast"** (2025): even with real journalism
  as source, staffers flagged invented/misattributed quotes in production — the
  app now tells listeners to verify. Grounding rules are not optional.
- **Michael Simmons** (aimaker.substack.com): Claude Code skill → TTS → personal
  RSS, closest build to ours. His lesson is upstream: generic AI voice often
  traces to thin source material, not generation-time prompting.
- **Detection literature**: Wikipedia "Signs of AI Writing"; Simon Willison's
  cliché highlighter (Jul 2026); Will Francis's "How to Stop Claude Writing
  Like an AI" (ban list, kill false-contrast constructions which "mimic insight
  without providing any", read-aloud as final check). Corpus linguistics
  (refsmmat.com): LLM prose is more informationally dense, less involved, low
  interactional metadiscourse, rigid phrase-bundles.
- **Caution on ban-lists** (secondary-sourced, unverified): suppressing a phrase
  can weaken the whole adjacent concept-cluster — negative constraints can
  flatten good writing too. Prefer positive craft rules over ever-longer bans.
- **Exemplar-based style imitation** (arXiv 2509.14543, verified): few-shot
  style copying works in structured genres (news) and WORST in personal-essay/
  blog voice; 5→10 exemplars gives limited gains; topically-similar exemplars
  REDUCE style capture vs varied ones. Implication: a written rules-charter
  plus our own best episodes as exemplars beats "write like Rao."
- **Length ceiling**: no published account of a successful 45–60 min fully
  AI-written audio essay. Going long is unmapped; track our own completion
  signal as original data.

---

## Report 4: Learning science for single-listen audio

- **Listening ≈ reading for comprehension** (Willingham) — but difficult texts
  favor print (re-reading, backtracking), and audio's real threat is divided
  attention. A 2025 randomized crossover driving-simulator trial (PLOS ONE):
  no significant retention difference between undistracted, low-load, and
  high-load driving at one month — walking/driving is fine; a second cognitive
  task is not.
- **Mind-wandering** runs ~24–28% in audio studies, compounds with duration and
  difficulty — the case against single long files.
- **Narrative is "psychologically privileged" in memory** (Willingham): the
  four Cs — causality, conflict, complications, character.
- **Pretesting**: a question posed before content improves retention of the
  answer AND surrounding material (Educational Psychology Review meta-review).
  Best-evidenced cheap win; adopted as a soft default.
- **Signaling and segmenting** (Mayer): explicit structural cueing measurably
  helps learning (segmenting supported in 10/10 tests, median ES 0.79;
  pre-training 13/16, ES 0.75). This is the honest tension with essayist
  aesthetics; resolved in the charter as "signal shape, not significance."
- **Seductive-details effect** (Harp & Mayer): entertaining-but-irrelevant
  material actively harms recall of core content while raising enjoyment
  ratings. Digressions must do argumentative work.
- **Retrieval/generation**: self-generated answers beat passive re-exposure
  (generation effect, Slamecka & Graf 1978); end-of-episode application
  questions are the right pattern. Spacing is among the most robust effects in
  memory research — cross-episode callbacks and interleaved threads are
  spaced repetition in disguise.
- **Audio-only cognitive load**: no visual channel to offload onto; the only
  levers are pacing, chunking, pruning. Fewer ideas, worked deeper.

---

## Report 5: Science and philosophy essay craft

- **Gould**: specimen → theory in one arc; open on one concrete oddity, widen
  once anchored, return to the same image at the landing ("mosaic" not "plate
  glass" writing). His baseball essay ("The Streak of Streaks," NYRB 1988) and
  his evolution work are the same statistical argument twice — which is why his
  range reads as authority, not dilettantism.
- **Lewis Thomas**: brevity as compression, not simplification; wonder
  delivered by restraint, never "isn't that amazing." Cut explanation earlier
  than instinct suggests.
- **Sacks**: the case as person, not exhibit — the disorder is the entry point,
  the subject is what it reveals about ordinary selfhood; keep the person's
  unresolved edges.
- **Dyson/Weinberg**: the review as vehicle for the reviewer's own stated
  position; disagreement from a visible home stance reads as argument, not
  summary-plus-adjectives.
- **Explainer debt**: deferred, distributed exposition — define a term at the
  moment it's needed, in apposition, never a front-loaded primer. Ed Yong:
  most writing problems are structuring problems; most structuring problems are
  reporting (i.e., understanding) problems.
- **Philosophy reviewing**: charity as a four-step procedure (strongest
  reconstruction → agreements → what was learned → only then critique). The
  two failure modes: journal-referee dryness (propositions graded, no stakes)
  and pop-philosophy mush (takeaway with no traceable premises). Midgley
  threads it: plain diction for the moving parts, visibly human stakes.
- **Dennett's intuition pump**: the philosophy-side equivalent of Gould's
  specimen — a small story engineered to produce "of course." Honest use names
  the trick.
- **Arguments for the ear**: narrative embedding beats premise-numbering (a
  listener can't glance back at "first"); recap by restatement-with-variation;
  hold the what's-at-stake sentence in reserve until just after the last
  premise; signposting the SHAPE of an argument up front is legitimate in
  audio in a way it isn't in print.
- **Science exception**: technical claims sometimes have a correct/incorrect
  structure tone can't convey — one or two direct "this is the load-bearing
  claim" moments per science episode are licensed; philosophy and literary
  segments carry importance by placement, example, and dwell time alone.
- **Range test**: before entering a new domain, ask whether the analytical tool
  carried over (statistical intuition, demand for operational definitions,
  suspicion of unfalsifiable claims) is the same one used at home. If judgment
  resets to generic enthusiasm per domain, that's dilettantism.
