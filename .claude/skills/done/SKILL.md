---
name: done
description: End-of-session capture for The Annotated Shelf. Trigger when the user says "done" or "wrap up", and at the end of every unattended Routine run after the episode is verified live. Appends one entry to PROJECT_LOG.md and refreshes the STATE.md snapshot so the next session (human or Routine) resumes cleanly.
---

# Session capture (repo-local version)

The repo holds its own state in three files. Each fact lives in exactly one:

- `STATE.md`: where the project stands now. REWRITTEN, surgically.
- `PROJECT_LOG.md`: what happened, session by session. APPEND-ONLY, newest last.
- `queue.md`: the reading list and TODO. Check items off in place; never add a
  second "done" list.

## Steps

1. Read the tail of `PROJECT_LOG.md` and the Snapshot of `STATE.md` first, so
   you do not repeat or contradict them.

2. Append one entry to `PROJECT_LOG.md`, newest last, in this shape:

   ```
   ## [YYYY-MM-DD] — <topic>

   **Decisions:** <craft or pipeline decisions taken, each with its why>
   **Verification:** <which quotes, dates, numbers were checked and how; what
     was stated from training knowledge at hedged precision>
   **Traps & dead ends:** <what was tried and abandoned; omit if none>
   **Open questions:** <each tagged HITL (only Kevin can answer) or AFK (an
     agent could resolve alone)>
   **Artifacts:** <files created or modified, with word counts for episodes>
   **Context:** <2–4 sentences of reasoning a future session needs>
   ```

   Phrase status as state, not instructions ("012 is 3,891 words", never
   "trim 012"). Report length and density as numbers under Artifacts, never
   as an open question. The routine fast-forward of a stale local main is not
   recorded anywhere.

3. Update `STATE.md`:
   - Snapshot: replace it in place, 3–6 lines. Episode count, what the latest
     sign-off promises (that promise is binding on the next writer), the single
     most important next step. Never add a "Previous" or "Earlier snapshot"
     section: git history and PROJECT_LOG hold the old one.
   - Decisions of record: add any new durable rule with its one-line why.
   - Open questions: at most twelve bullets, each at most two lines, newest
     first. If the same question is already open, add the episode number to
     that bullet instead of writing a new one. Delete resolved ones (the
     answer lives in today's log entry).
   Do not regenerate the whole file. Before committing, run
   `grep -c "^## Snapshot" STATE.md` (must print 1), `grep -c "Previous snapshot" STATE.md`
   (must print 0) and `wc -l STATE.md` (must be under 150); if any fails, fix
   STATE.md in this run and do not record the fix as an open question.

4. `queue.md`: tick the work just published with its episode number and date
   only (the summary lives in the log entry); if a new work was promised in
   the sign-off and is not on the queue, add it at the top of the fitting
   section.

4b. `FRAMES.md`: if the episode planted a frame the shelf should keep, add a
   row (name, distinctive keys, one-line mechanism). Usage counts are
   computed by `scripts/frames.py`, so nothing else needs updating.

5. Commit the changed files together (`Log: <topic>`) and push to main. In an
   unattended run this push is the last step; do not end the turn before it.

## Guardrails

- Never write outside the repo. No global handoff files.
- Never edit prior log entries.
- Nothing personal or sensitive; the repo is public.
