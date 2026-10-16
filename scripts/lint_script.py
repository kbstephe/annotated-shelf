"""Read-aloud lint for episode scripts. Usage: python scripts/lint_script.py episodes/NNN-slug.md

Two checks, both for how text sounds narrated once, no rewind:
1. Near repeats: a phrase of three or more content words recurring within 40
   words. On the page this reads as a rhetorical echo; in audio it sounds like
   the narrator stuttered. Rewrite the second occurrence.
2. Tics: stock narrator moves that sound like a language model. Seeded from
   the house list plus the online catalogues (Velitchkov's 22 Claude cliches,
   claudisms.ai, Will Francis's guide), 26 Aug 2026.

Exit code 1 if anything is flagged, so the pre-flight can gate on it.
"""
import re
import sys

WINDOW = 40
STOP = set("the of a an and to in is that it was not on at his her he she with as for by "
           "or but this its be are were from which who what".split())

TICS = [
    # narrator grading his own material
    r"\bis the point\b", r"\bthe point is\b", r"\bthat is the point\b",
    r"\bload-?bearing\b",
    r"\bthat is where\b.{0,30}\b(lies|is|sits|lives)\b", r"\breally lies\b",
    r"\bthe (key|real|deeper|deepest) (insight|point|question|lesson)\b",
    r"\bthe real (question|issue|problem|point|work|story) is\b",
    r"\bthe payoff\b", r"\bmost important\b", r"\bsharpest\b", r"\bstriking\b", r"\bcrucial\b",
    r"\bworth (noting|saying|having|pausing)\b", r"\bworth sitting with\b",
    r"\bsit with (this|it|that|how)\b", r"\blet that (sink|land)\b",
    r"\band that is\b.{0,20}\b(lesson|point)\b",
    r"\b(this|that|it) matters because\b", r"\bshapes? everything that follows\b",
    r"\bNotice\b",
    # restatement and signposting
    r"\bwhich is to say\b", r"\bin other words\b", r"\bput differently\b",
    r"\bto put it another way\b", r"\bbetter posed\b", r"\bthe (short|long) version\b",
    r"\bwhat (this|that) (means|tells you) is\b", r"\bhere's the thing\b",
    r"\bhere is the thing\b", r"\bthe thing to (learn|take|notice|see)\b",
    r"\bthat is the whole\b", r"\bis the whole of\b", r"\bhas a name\b",
    r"\bmore on that (later|below|in a moment)\b", r"\bwe'll get to\b", r"\bhold that thought\b",
    # contrastive frames
    r"\bit is not (a|the) \w+\. it is\b", r"\bnot because .{0,40} but because\b",
    r"\bnot (a|an) \w+ but (a|an) \w+\b", r"\bit would be wrong, though\b",
    # connectors and tail clauses
    r"\bfalls out of\b", r"\bfollows directly\b", r"\band no more\.",
    r"\bsupplies the other half\b", r"\bdo the work\b", r"\bdoes the work\b",
    r"\bearn(s|ed)? (its|the) (place|keep)\b", r"\bit turns out\b", r"\bturns out to be\b",
    r"\bwhich is (the|exactly|precisely)\b", r"\bnot least\b",
    # adverbs and catchphrases
    r"\bquietly\b", r"\bprecisely\b", r"\bexactly the\b", r"\bgenuinely\b",
    r"\bthe honest (answer|take|version)\b", r"\bhonest take\b", r"\bstated fairly\b",
    r"\bthat's the unlock\b", r"\bsmoking gun\b", r"\bbelt and suspenders\b",
    r"\bdelve\b", r"\bunderscore\b", r"\btapestry\b", r"\bnuanced\b", r"\bpivotal\b",
    # narrated bibliography (Kevin, 16 Oct 26: "no need for bibliography moving forward").
    # 060-066 closed on a source-list paragraph; these are its opening frames.
    r"\bfor the record\b", r"\bhow (this|the) (episode )?was grounded\b",
    r"\bhow much of this I (have )?(verified|checked|read)\b",
    # narrator staging his own drama (Kevin, 27 Aug 26: "this is where the pause carries weight")
    r"\bcarr(y|ies|ied) (the |its |real |a lot of )?weight\b", r"\bthe pause\b", r"\bpause (here|there|on)\b",
    r"\b(this|here) is where\b", r"\bheavy lifting\b", r"\bdoes a lot of\b",
    r"\bhard to overstate\b", r"\bcannot be overstated\b", r"\bthe tell\b", r"\bthe trick is\b",
    r"\bthe move (here|is)\b", r"\bwhat makes this\b", r"\bread that again\b", r"\bsay it again\b",
    r"\bthe quiet (part|truth|fact)\b", r"\bat bottom\b", r"\bin the end,\b", r"\bthe (deep|deeper) (story|truth)\b",
    r"\bworth\b.{0,12}\b(pausing|dwelling|lingering|noticing)\b", r"\bdwell on (this|that)\b",
    r"\bthe weight of (that|this|the)\b", r"\bland(s|ed)? (hard|differently)\b",
    r"\b(for|on|into|by) Monday\b", r"\bMonday\b",
    r"—",
    # narrator grading, second family (Kevin, 10 Sep 26: "we should dwell on it,
    # because of the weight of the argument"). "worth <verb>ing" had mutated
    # past the four forms above and closed nearly every episode 031-040.
    r"\bworth \w+ing\b", r"\bworth (a|an|the) (moment|look|second|closer|pause|detour|hearing)\b",
    r"\bdwell(s|ed|ing)? (on|in|inside|with|here|there|upon)\b", r"\bweight of\b", r"\bdeserves?\b", r"\brepays?\b",
    r"\bread(s)? (it |that |this )?twice\b", r"\bbears? (repeating|saying|restating|stating)\b",
    r"\bpay(s)? (slower|closer|more|particular) attention\b",
    r"\bmost (familiar|durable|useful|vivid|honest|important) \w+ (in|of|on) (his|her|the|this|that)\b",
    r"\bthe (whole |entire )?(essay|book|argument|lecture) turns on\b",
    r"\b(hinge|spine|centrepiece|heart) of the (essay|book|argument)\b",
    # persona (Kevin, 10 Sep 26): the narrator is Claude, never Kevin in the
    # first person. Judgments in "I" are fine; biography is not.
    r"\bI (run|work in|work at|help run|practise|practice|treat|trained)\b",
    r"\bmy (own )?(patients|career|field|trade|work|hospital|colleagues|trainees|programme|program|grants?|ward|clinic|lab)\b",
    r"\bfor a living\b",
    # --- review batch, 16 Oct 26 (reviews/2026-10-16-topics-and-improvements.md) ---
    # the closing question re-formed after the 27 Aug "Monday" ban
    # ("The question to carry into X" closed 7 of 8 episodes 058-065)
    r"\bgenerative (question|habit|test)\b",
    r"\bquestion (to|I would|I'd|you (can|could|might)) (carry|take|bring|hold) (into|back|with|to)\b",
    r"\bquestion for the (working |coming |next )?(week|month)\b",
    r"\bto carry into\b",
    # the charter's own checklist words, narrated ("flagged as constructed")
    r"\b(flagged|labell?ed|marked) as (constructed|invented|the narrator's|mine|my own)\b",
    r"\bmy own inference\b",
    r"\b(inference|rule|test|suggestion|arithmetic|case against) is (mine|the narrator's)\b",
    r"\bbelongs to the narrator\b",
    r"\bnarrator's (own|test|rule|suggestion|inference)\b",
    r"\bI (will )?(label|mark|flag) (it|this|that|them) as\b",
    # importance announced ahead of the payoff
    r"\bthis hour\b",
    r"\b(will|would) matter (later|more later|further on|in a (few )?(minutes?|moments?)|in the (final|last|next|closing) chapter|by the end)\b",
    r"\bmatters? (later|more later|further on)\b",
    r"\bremember (that|this) (\w+ )?(detail|number|name|date|sentence|figure|distinction|fact)\b",
    r"\bhold (on ?to|onto) (that|this) (\w+ )?(sentence|detail|number|name|date|fact|figure|choice|distinction|thought)\b",
    r"\bkeep (that|this|the) (\w+ )?(sentence|detail|number|name|date|fact|figure|distinction) in mind\b",
    r"\bbefore this (hour|episode|chapter) is (done|over|out)\b",
    # conversational residue: the listener is a stranger to the writing session
    r"\bthis session\b", r"\bas (you )?requested\b", r"\bas you suggested\b", r"\bthe user\b", r"\.md\b",
    # citation-first chapter openers: put the claim first, the citation second
    r"\bwith (a|the) title\b",
]


def words(text):
    return [(m.group(0).lower(), m.start()) for m in re.finditer(r"[A-Za-z']+", text)]


def near_repeats(text, n=3):
    w = words(text)
    lw = [x for x, _ in w]
    seen, out = set(), []
    for i in range(len(lw) - n):
        g = tuple(lw[i:i + n])
        if sum(x in STOP for x in g) >= 2:
            continue
        for j in range(i + n, min(i + WINDOW, len(lw) - n)):
            if tuple(lw[j:j + n]) == g and g not in seen:
                seen.add(g)
                line = text.count("\n", 0, w[i][1]) + 1
                out.append((line, " ".join(g)))
    return out


def tics(text):
    out = []
    for pat in TICS:
        for m in re.finditer(pat, text, flags=re.I):
            line = text.count("\n", 0, m.start()) + 1
            out.append((line, m.group(0)))
    return sorted(out)


# Title cap (review batch, 16 Oct 26): titles had grown from about 100 to 310
# characters; the cap is anchored on the 25 titles Kevin renamed on 28 Aug 26
# (58-103 characters). Form: Work (Author): one short hook.
TITLE_MAX_CHARS, TITLE_MAX_WORDS = 105, 15

# Digits (review batch, 16 Oct 26): numbers are written out for the ear, except
# four-digit years and decimal statistics. A digit run attached to a letter,
# hyphen or slash (R01, ISIS-2, F-75, 24/7) is part of a name and passes.
DIGIT = re.compile(r"(?<![\w.,\-/])\d[\d,]*(?:\.\d+)?(?![\w\-/]|[.,]\d)")
YEAR = re.compile(r"^(1[5-9]\d\d|20\d\d)$")


def digits(text):
    out = []
    for m in DIGIT.finditer(text):
        tok = m.group(0)
        if YEAR.match(tok) or "." in tok:
            continue
        line = text.count("\n", 0, m.start()) + 1
        out.append((line, f"digit {tok} (write it out)"))
    return out


def structure(text, meta):
    out = []
    last_line = text.rstrip().count("\n") + 1
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    tail = " ".join(paras[-2:])
    if "Next time" not in tail:
        out.append((last_line, "sign-off: no 'Next time' in the last two paragraphs"))
    if not text.rstrip().endswith("Thanks for listening."):
        out.append((last_line, "sign-off: script must end 'Thanks for listening.'"))
    title = meta.get("title", "")
    if not title:
        out.append((1, "frontmatter: no title"))
    elif len(title) > TITLE_MAX_CHARS or len(title.split()) > TITLE_MAX_WORDS:
        out.append((1, f"title {len(title)} chars / {len(title.split())} words "
                       f"(cap {TITLE_MAX_CHARS} / {TITLE_MAX_WORDS}): Work (Author): one short hook"))
    if not meta.get("description"):
        out.append((1, "frontmatter: no description"))
    return out


def frontmatter(text):
    meta = {}
    if text.startswith("---"):
        head = text[3:].split("---", 1)[0]
        for line in head.splitlines():
            if ":" in line:
                k, _, v = line.partition(":")
                meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta


def main(path):
    text = open(path, encoding="utf-8").read()
    meta = frontmatter(text)
    # blank the frontmatter rather than cut it, so reported line numbers are absolute
    if text.startswith("---"):
        head, rest = text[3:].split("---", 1)
        text = "\n" * (head.count("\n") + 1) + rest
    reps = near_repeats(text)
    tk = sorted(tics(text) + digits(text) + structure(text, meta))
    for line, g in reps:
        print(f"{path}:{line}: repeat within {WINDOW} words: '{g}'")
    for line, g in tk:
        print(f"{path}:{line}: tic: '{g}'")
    print(f"{len(reps)} repeats, {len(tk)} tics")
    return 1 if (reps or tk) else 0


if __name__ == "__main__":
    sys.exit(max(main(p) for p in sys.argv[1:]))
