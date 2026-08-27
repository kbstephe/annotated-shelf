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
    # narrator staging his own drama (Kevin, 27 Aug 26: "this is where the pause carries weight")
    r"carr(y|ies|ied) (the |its |real |a lot of )?weight", r"the pause", r"pause (here|there|on)",
    r"(this|here) is where", r"heavy lifting", r"does a lot of",
    r"hard to overstate", r"cannot be overstated", r"the tell", r"the trick is",
    r"the move (here|is)", r"what makes this", r"read that again", r"say it again",
    r"the quiet (part|truth|fact)", r"at bottom", r"in the end,", r"the (deep|deeper) (story|truth)",
    r"worth.{0,12}(pausing|dwelling|lingering|noticing)", r"dwell on (this|that)",
    r"the weight of (that|this|the)", r"land(s|ed)? (hard|differently)",
    r"(for|on|into|by) Monday", r"Monday",
    r"—",
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


def main(path):
    text = open(path, encoding="utf-8").read()
    # blank the frontmatter rather than cut it, so reported line numbers are absolute
    if text.startswith("---"):
        head, rest = text[3:].split("---", 1)
        text = "\n" * (head.count("\n") + 1) + rest
    reps = near_repeats(text)
    tk = tics(text)
    for line, g in reps:
        print(f"{path}:{line}: repeat within {WINDOW} words: '{g}'")
    for line, g in tk:
        print(f"{path}:{line}: tic: '{g}'")
    print(f"{len(reps)} repeats, {len(tk)} tics")
    return 1 if (reps or tk) else 0


if __name__ == "__main__":
    sys.exit(max(main(p) for p in sys.argv[1:]))
