"""Read-aloud lint for episode scripts. Usage: python scripts/lint_script.py episodes/NNN-slug.md

Two checks, both for how text sounds narrated once, no rewind:
1. Near repeats: a phrase of three or more content words recurring within 40
   words. On the page this reads as a rhetorical echo; in audio it sounds like
   the narrator stuttered. Rewrite the second occurrence.
2. Tics: stock narrator moves that sound like a language model.

Exit code 1 if anything is flagged, so the pre-flight can gate on it.
"""
import re
import sys

WINDOW = 40
STOP = set("the of a an and to in is that it was not on at his her he she with as for by "
           "or but this its be are were from which who what".split())

TICS = [
    r"\bis the point\b", r"\bthe point is\b", r"\bthat is the point\b",
    r"\bload-?bearing\b",
    r"\bthat is where\b.{0,30}\b(lies|is|sits|lives)\b",
    r"\breally lies\b",
    r"\bwhich is to say\b",
    r"\bhere's the thing\b", r"\bhere is the thing\b",
    r"\bthe thing to (learn|take|notice|see)\b",
    r"\bthat is the whole\b", r"\bis the whole of\b",
    r"\bit is not (a|the) \w+\. it is\b",
    r"\bnot because .{0,40} but because\b",
    r"\bthe (key|real|deeper|deepest) (insight|point|question|lesson)\b",
    r"\bthe payoff\b", r"\bmost important\b", r"\bsharpest\b", r"\bstriking\b", r"\bcrucial\b",
    r"\bNotice\b",
    r"\bin other words\b", r"\bput differently\b", r"\bto put it another way\b",
    r"\bsit with that\b", r"\bsit with how\b", r"\blet that (sink|land)\b",
    r"\band that is\b.{0,20}\b(lesson|point)\b",
    r"\bdo the work\b", r"\bdoes the work\b", r"\bearn(s|ed)? (its|the) (place|keep)\b",
    r"\bquietly\b", r"\bprecisely\b", r"\bexactly the\b",
    r"\bworth (noting|saying|having|pausing)\b",
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
    body = text.split("---", 2)[-1] if text.startswith("---") else text
    reps = near_repeats(body)
    tk = tics(body)
    for line, g in reps:
        print(f"{path}:{line}: repeat within {WINDOW} words: '{g}'")
    for line, g in tk:
        print(f"{path}:{line}: tic: '{g}'")
    print(f"{len(reps)} repeats, {len(tk)} tics")
    return 1 if (reps or tk) else 0


if __name__ == "__main__":
    sys.exit(max(main(p) for p in sys.argv[1:]))
