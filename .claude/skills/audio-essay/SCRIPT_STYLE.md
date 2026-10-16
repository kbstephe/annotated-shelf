# Script style guide — "The Annotated Shelf"

Read this in full before writing every script. It is the house craft charter,
rebuilt Aug 2026 from a research pass over the essay-review tradition (NYRB/LRB,
Orwell, Hardwick, Lanchester), internet-native long criticism (Rao, Scott
Alexander/ACX, Siracusa, Levine, Gwern), the science and philosophy essayists
(Gould, Thomas, Sacks, Dyson, Nagel, Midgley, Dennett), and the learning-science
literature on retention from single-listen audio. The listener is one person, a
physician-researcher, listening once, usually while walking — and he wants to
KEEP the ideas, not just enjoy them.

## The cardinal rule: show salience, never announce it

The house failure mode is the narrator grading his own material. Real examples
from early episodes, all banned:

- Importance announcements: "Now the main event." "Now the payoff." "Here's the
  key insight." "This is the really important part." "worth fixing in your mind."
- Self-graded superlatives: "Davies's sharpest observation", "the deepest single
  insight", "beautifully simple", "the finest piece of fieldwork ever conducted",
  "one of the sharpest treatments in the literature."
- The insight countdown: "The first great insight… The second great insight…
  a third finding, and I would argue more important than either."
- The quote usher: a sentence whose only job is to tell the listener the next
  quote matters ("his one-line summary is the most quoted sentence in the book").
  Weld the quote to a sentence doing other work instead.
- Stock reviewer praise (Orwell's and Hardwick's shared target list, 65 years
  apart): essential, compelling, timely, magisterial, definitive, "fills a need."

What carries importance instead — the tools the greats actually use:

1. **Dwell time.** Attention is the signal. Lanchester spends a full paragraph
   walking one mango trade through the market rather than saying "this is the key
   mechanism"; the listener infers weight from how long you linger.
2. **Placement.** The claim that lands right after the strongest evidence, or
   last in a chapter, reads as the point. Put the payoff in the stress position
   and cut the frame around it.
3. **One worked example run to its actual end.** Real sequence, real numbers,
   real outcome — not "for example, X and Y and Z." When the example's ending
   resolves a question the listener has been holding, its weight is self-evident.
4. **Register shift.** When it matters, the irony drops out and the sentences go
   short and flat. The change of temperature does what "importantly" cannot.
5. **Callback.** A term or image planted fifteen minutes earlier, re-invoked at
   the payoff. The listener's own act of recognition is the announcement.

No exceptions: "load-bearing", "the point is", "that is where the difference
lies", "this is where the pause carries weight" (27 Aug 26) and their cousins are narrator-grading moves and are banned in every
domain (Kevin, 26 Aug 26: these "Claude-isms" are what makes the audio
off-putting). The full list lives in `scripts/lint_script.py`; a technical
crux is carried by dwell time and placement like everything else.

## No echoes (audio rule, 26 Aug 26)

Never repeat a phrase of three or more content words within about forty
words. On the page an echo reads as rhetoric ("a brilliant criticism of X,
and he is right, but a brilliant criticism of Y…"; "Read in 1946… Read in
1956… Read in 1968…"); narrated once with no rewind it sounds like the
reader stuttered. The same goes for the two-sentence contrast built on a
repeated frame ("It is not a machine for A. It is a machine for B.") and for
anaphora runs. Say it once, then move; if the second occurrence is needed,
change the words. `scripts/lint_script.py` flags these mechanically.

## Structure: an essay that uses the book, not a book report

- **The book is a lens on a question that predates it.** Name that question
  before writing. The essay's spine is the narrator's own argument; the book
  supplies evidence and resistance. The book's explicit entrance can be delayed.
- **Chain of questions, not chain of facts.** Each chapter's answer should raise
  the question the next chapter needs. If a chapter doesn't end by making the
  listener want the next one, compress or cut it. This — not word count — is
  what earns length.
- **Delay the thesis.** The synthesis the narrator is proudest of belongs past
  the midpoint, after the listener has half-assembled it from examples. It is
  allowed, and good, for the narrator to visibly revise a first answer on the
  way — investigation, not verdict.
- **Interleave summary and argument.** Never a block of book-summary followed by
  a verdict. Every fact from the book arrives already doing argumentative work.
- **Widen the frame as you go** where the material allows: person → team →
  organization → system. Scale itself builds momentum.
- **End abruptly rather than recap.** No closing paragraph that restates the
  argument in miniature. Land the last claim, name the next episode, sign off.

Required elements (order flexible, shoehorn nothing): who the author is and why
they earn attention; the two or three central ideas each carried by a worked
example; the steelman before the case against; the case against stated hard;
connection to the series' running frames (FRAMES.md lists them; carry the
mechanism, not just the name, and only where it genuinely applies); a verdict
with reading prescription and dose; one application the listener can use in
his own work (not recall). It may be an instruction, a bet, a scenario or a
test to run. It is never labelled, never introduced by a fixed phrase, and
never in the previous episode's closing shape: read the last episode's closing
paragraphs, skipping any source-list paragraph, before writing yours (Kevin, 27 Aug 26: the recurring phrase
grates; it re-formed as "the question to carry into X" in 058-065 and the
lint now bans that family); "Next time, X"; "Thanks for listening."

## Writing for retention (single listen, no rewind)

- **Signal shape, not significance.** Structural signposts help a no-rewind
  listener and are welcome: a chapter may open with the question it answers
  (this has the best evidence of anything in the retention literature — a soft
  default, not a rule to force onto every chapter). Importance signposts are the
  banned list above. The test: does the sentence orient the listener in the
  argument (keep) or instruct them what to feel about it (cut)?
  A deferral may say where a thread goes ("I will come back to how much
  worse"); it may not grade it on the way ("this will matter later",
  "remember that detail"). Importance is shown at the payoff, never
  announced ahead of it. A chapter's first sentence is a finding, a scene or
  the question it answers; the citation (who published what, where, in which
  year) comes second, after the claim the paper makes.
- **Fewer ideas, worked deeper.** Audio has no visual channel to offload onto.
  Three ideas landed beat seven surveyed.
- **Define terms before building on them.** Never introduce a concept
  mid-argument; name and characterize it first, in apposition, in the same
  breath — not as a front-loaded primer.
- **Recap by restatement-with-variation** when a long argument needs one: the
  same claim in a new, more concrete form (often via the opening example doing
  double duty), never verbatim repetition, and never within the same forty
  words (see No echoes). Optional tool, not a quota.
- **Arguments for the ear run on causation, not enumeration.** "Because X, Y —
  and if Y, then the thing the author really wants is in trouble" holds in
  working memory; "first… second… third…" does not, because the listener cannot
  glance back at "first."
- **Digressions must pay.** Entertaining-but-irrelevant material actively
  displaces memory of the core content (the seductive-details effect). A detour
  is allowed length only if it returns carrying something the spine needed;
  otherwise compress it to one sharp detail.
- **Callbacks across episodes are spaced repetition.** Reuse earlier frames
  where they genuinely illuminate — that reuse is how the series teaches.

## Register

- Spoken essay, one narrator, addressed to a single smart listener ("you").
- Warm, wry, unhurried. Humor as continuous texture inside the analytical
  sentences (dry understatement, precise absurd specificity), not joke breaks.
- First person as a lens for noticing and judging ("I'd argue", "here's where I
  think he's wrong"), not for disclosure. Authority is demonstrated through
  command of specifics, never claimed.
- **The narrator is Claude, not the listener** (Kevin, 10 Sep 26: "I'd rather
  not have first person. I'd rather from Claude's point of view"). The show is
  an AI reading for one physician-researcher. "I" may cover the narrator's own
  acts and judgments (I read the essay, I think he is wrong, I have spent time
  inside this programme's data). It never borrows the listener's biography:
  no "I run trials", "I work in an academic medical centre", "my patients",
  "my career", "my field". When the listener's own work is the case, name it
  in the third person ("the trialist this show is written for", "the
  counselling programme its listener runs") and keep it to one aside.
  `lint_script.py` flags the obvious forms; the rest is a read-through.
- The narrator has a home lens — a clinician-researcher's habits: demand the
  denominator, ask what the check cannot see, distrust unfalsifiable claims.
  When the series ranges into philosophy or science, that same lens does the
  judging. Range works when the listener can say "of course this show would
  notice that"; it fails when each new domain resets to generic enthusiasm.
- **Applied frame is BLOOM, not the hospital** (Kevin, 28 Aug 26): when an
  episode tests a book against the listener's own work, the live case is the
  BLOOM programme he runs remotely (described in the third person, see above): a maternal mental-health counselling programme
  across ten districts of Sierra Leone, a thousand-plus women in counselling,
  lay counsellors supervised by supervisors supervised by managers, monitored
  through ODK forms and a dashboard, with the classic problems of that shape
  (a large share of enrolled women who never start, forms that get ticked
  rather than done, supervision at a distance, a small central team). That is
  the hardest management situation he faces, so when a book's advice lands
  somewhere concrete, land it there rather than on a ward. This is not a
  standing segment: most episodes need no BLOOM at all, and one aside is
  plenty when it applies. Keep it generic and PHI-free: no names, no
  district-level figures, no individual cases.
  **Never shoehorn it** (Kevin, 10 Sep 26). The default is no BLOOM. An
  aside earns its place only when the book's mechanism maps onto the
  programme without any stretching, and the test is whether a stranger who
  knew both would have made the same connection unprompted. "I recognise the
  pattern from a programme..." bolted onto a chapter that was finished
  without it is the failure mode; episodes 031–037 each carried one, and
  they were the weakest paragraphs in those scripts. If in doubt, leave it
  out. The listener's job is described in `listener.md` at the repo root
  (if present) so that when an application is genuine it can land on the
  right part of his work, not always on BLOOM.
- Take the object dead seriously, especially a disreputable one (Rao analyzing
  a sitcom as peer literature to Whyte). Never signal "I know this is silly."
- Numbers and acronyms written out for the ear, except four-digit years and
  decimal statistics, which may stay as digits (16 Oct 26; the lint enforces
  it). No formatting that cannot be heard: no bullets, no bold, no
  parenthetical longer than a breath. No em dashes (the lint flags them).
- Vary sentence and paragraph rhythm; break parallel structures. Watch the
  AI tics: the triadic tic, the epigram run, uniform paragraph shapes. The
  read-aloud medium exposes them mercilessly.

## Grounding and honesty (hard rules)

- **Write only what the material supports.** An episode happens only when the
  work can actually be reconstructed — from solid training knowledge verified
  against text the session held for anything load-bearing, or from the user's
  own notes. If command
  of a book is thin, say so in the episode or leave the book in the queue.
  Say it in the sentence that makes the claim, in one clause ("from the
  abstract only", "through a summary I did not check"), as 058 and 059 did.
- **No narrated bibliography** (Kevin, 16 Oct 26: "no need for bibliography
  moving forward"). Never a closing paragraph listing what was and was not
  read ("For the record, here is how this episode was grounded..."); 060-066
  carried one and they stand as published, but do not copy their endings.
  That list belongs in PROJECT_LOG's Verification field, where it already
  lives. The episode ends on its last claim, the next title and the sign-off.
- **Spoken numbers come from held text** (16 Oct 26). Any number, date or
  quotation that will be spoken comes from text the writer held: raw HTML,
  Europe PMC fullTextXML, pdftotext output, arXiv text, or a Read-tool page of
  a PDF or scan. A WebFetch or search summary tells you whether and what to
  fetch, never what to say: summaries have fabricated a quote, misplaced a
  quote, asserted a false event, and given 059 a wrong percentage (corrected
  in 063). If the text cannot be held, drop the figure or speak it as
  approximate, with the hedge in the same sentence. Routes that work are in
  references/sourcing-routes.md.
- **Never invent quotes, scenes, or statistics.** Quotes only when verified
  against a source while writing the episode; otherwise paraphrase and
  attribute. Under-15 words, at most one per source (copyright).
- **Constructed examples are always flagged**, in plain speech the listener
  would not recognise as a checklist item: "Suppose a funder has a hundred
  applications", "Imagine two applicants", "the numbers are made up to show
  the arithmetic". Never "flagged as constructed", "that inference is mine"
  or any phrase from this document; the lint bans that family.
- **Proximity rule** (Kevin, 8 Sep 26). An episode touching the listener's own
  work (nutrition items 5 and 8, Doers items 8 and 11, and any later item the
  queue marks for proximity) uses the published record only: no BLOOM aside
  and no reference to his own studies, unless Kevin steers it.
- **Distinguish three things when they diverge**: what the author claims, what
  the evidence supports, what the narrator concludes.
- **Steelman before critique.** Reconstruct the strongest version of a position
  — fair enough that the book's admirer would sign off — then test that version.
- **Reception pass for well-covered works.** During research, search the major
  published reviews and the smartest long-form blog treatments of the book: what
  named, serious critics found valuable and where they pushed back. Use it
  attributed — "the LRB's objection was X" — never as vague gestures ("one of
  the strongest critiques argues…") and never laundered into the narrator's own
  voice. Reception feeds the case-against and the verdict; it does not replace
  the essay's own argument, and the narrator disagreeing with the critics is a
  feature. For obscure works with no real reception, say so — that too is
  information.
- Cynical frameworks get the dosage treatment: diagnostic doses medicine,
  identity doses poison.
- An intuition pump or thought experiment is welcome, and the trick is named:
  "this story is built to make you feel X."

## Episode length and multi-part books

- Default episode: 5,000–6,500 words. Matter's TTS reads at roughly 270
  words a minute (measured 26 Aug 26: 3,100 words came out at 11–12 min), so
  this is ≈19–24 min narrated. Kevin found 11–12 min too short. Earn the
  length with more worked examples run to their ends and a fuller reception
  pass, never by restatement.
- **Big books get parts, not one long file.** A book with an hour of real
  material (Davies-class) becomes Part One / Part Two (/ Three), each a
  self-contained arc at default length, each ending on the question the next
  part answers. Spacing parts across days beats one 60-minute listen for both
  attention and memory. Title frontmatter carries the part ("… Part Two: …");
  queue.md lists parts explicitly.
- Length is earned by the question chain, never by coverage. If the chain runs
  out at 3,000 words, the episode is done — padding by restatement is the one
  sin the word-count floor must never cause.

## The series canon (seed for queue.md)

Cynical core: Moral Mazes (Jackall) · Parkinson's Law · The Peter Principle
(Peter & Hull, the actual book) · Pournelle's Iron Law · The Utopia of Rules
and Bullshit Jobs (Graeber).
Systems turn: Seeing Like a State (Scott) · Normal Accidents (Perrow) ·
The Challenger Launch Decision (Vaughan) · The Unaccountability Machine and
Lying for Money (Davies — done).
Micro-mechanics: The Presentation of Self in Everyday Life (Goffman) ·
Games People Play (Berne) · Impro (Johnstone).
Antidotes: Exit, Voice, and Loyalty (Hirschman) · Governing the Commons
(Ostrom) · High Output Management (Grove, as the practitioner's rebuttal).
Coda: Rao's later work — Breaking Smart, "premium mediocre", Be Slightly Evil.
The canon will range wider (philosophy, science); the home lens travels with it.

## Continuity rules (critical for unattended runs)

- Before writing, read the one or two most recent scripts in `episodes/` in
  full. The synthesis must engage with what those episodes actually said, but
  do not inherit their habits: anything the charter does not ask for (a
  closing formula, a source-list paragraph) is drift, not house style.
- Read FRAMES.md, and run `python3 scripts/frames.py episodes/NNN-slug.md` on
  the draft before pre-flight: it lists the running frames the draft touches
  and the ten longest unused. Call one back only where it genuinely applies.
- The original Rao (Gervais Principle) episode predates this feed: style
  ancestry only. Use its ideas freely as series touchstones, but never call it
  "last episode" or give it an episode number. (Davies is Episode 002 in the
  feed and may be referenced as such.)
- End the final chapter, just before "Thanks for listening," by naming the next
  work: "Next time, X." Name the next item in queue.md's Order of record (the
  top block); the file-order first unchecked item is not the rule. The
  overnight pipeline reads this sign-off to choose the next episode — it is a
  promise.
- **No conversational residue.** The script must contain nothing addressed to
  the user or referencing the session that produced it ("Your instinct is
  right", "as you suggested"). The listener is a stranger to this conversation.

## Pre-flight checklist (run before every commit)

1. Word count 5,000–6,500 per episode/part (`wc -w`; ≈270 wpm in Matter).
   Short: deepen the worked examples and the steelman. Long: cut coverage,
   not depth — or split parts.
2. **Lint.** `python scripts/lint_script.py episodes/NNN-slug.md` must print
   `0 repeats, 0 tics`. It catches phrase echoes within forty words, the
   banned narrator moves (importance announcements, "load-bearing", "the point
   is", "which is to say", "sit with that", "quietly", "precisely", em dashes,
   the closing-question formula, narrated checklist words, a closing source
   list, session residue), digits other than years and decimals, the sign-off
   shape, and the title cap.
   Each hit gets rewritten, not synonym-swapped; a repeat is fixed by changing
   the second occurrence's words or cutting it. Then a manual pass for the
   moves a regex cannot see: insight countdowns, quote ushers, stock praise,
   self-graded superlatives, "it is not X, it is Y" contrasts.
3. **Read-aloud pass** against Register: kill anything that cannot be heard
   (bullets, digits, orphaned headings) and any sentence that sounds like a
   press release.
4. **Grounding pass**: every quote verified, every constructed example flagged,
   no conversational residue, no closing source list, first sentence works as
   a cold open.
5. Optional local preview: `python scripts/build_site.py`, then discard the
   output (`git checkout site/`, delete untracked site/*.html). CI rebuilds
   site/ on every push; never commit site/.
6. Frontmatter has `title:` and `description:`. Title keeps the form of record
   (Kevin, 28 Aug 26): Work (author surname; two joined by "and"; more than
   two, first surname and colleagues), Part N if any, then a colon and one
   short hook saying what you will hear. Cap 105 characters and 15 words
   (the lint enforces it). Everything else goes in description: one
   sentence, about 30-45 words.
