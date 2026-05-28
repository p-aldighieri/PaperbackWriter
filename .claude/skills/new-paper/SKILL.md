---
name: new-paper
description: |
  Bootstrap a new paper. Asks for an external target path, creates the directory, copies the
  scaffold, and walks the user through filling in the brief. Use when the user says "new
  paper", "start a paper", "I want to write a paper", "set up a new paper", or when they're
  new to the repo and need onboarding. This is the **first-run entry point**.
---

# new-paper

The first-run entry point. Bootstraps an external paper directory and walks the user through the inputs they need to provide before `draft-paper` can run.

## Invocation

User says: "new paper", "start a paper", "I want to write a new paper", "set up a paper", "how do I begin", or anything else that suggests they're starting from scratch.

If the user just cloned this repo and is asking "what do I do" / "how do I use this", invoke this skill.

## Step 1 — Where will the paper live?

Ask the user once:

> "Where should the paper live? Give me an absolute path — e.g., `~/Documents/papers/persuasion-2026` — anywhere outside this repo. The repo is a toolkit; your papers belong on your own filesystem."

Resolve the path. Validate:
- It must be an absolute path (after expanding `~`).
- It must NOT be inside this `PaperbackWriter` repo. If it is, refuse and ask again.
- If the directory already exists and contains `brief.md` + `proofs/`, this isn't a "new" paper — point them at `draft-paper` instead.

Call the resolved path `$TARGET`.

## Step 2 — Create and scaffold

If `$TARGET` doesn't exist, create it (and any missing parents).

Copy the entire `scaffold/` contents from this repo into `$TARGET`, with these adjustments:

- `scaffold/brief.md` → `$TARGET/brief.md` *(template skeleton; the user fills it in next)*
- `scaffold/proofs/README.md` → `$TARGET/proofs/README.md`
- `scaffold/tex/` → `$TARGET/tex/` (entire tree, including empty section stubs)

Do **not** create proof files. Those come from the user's separate proof pipeline.

## Step 3 — Walk through the brief

The brief is the most important input. The orchestrator can't draft without it.

Show the user the `$TARGET/brief.md` template. Then ask, one at a time:

1. **"What does the paper claim, in one sentence?"** — a colleague-readable one-liner. Capture verbatim.
2. **"Who should care, and why?"** — the open question or tension the paper addresses. Capture verbatim.
3. **"What's NOT in this paper?"** — the contribution boundary (so the motivation-writer doesn't overstate). Capture.
4. **"Which 3–6 papers is this most directly in conversation with?"** — comparison anchors. Citation keys preferred (e.g., `kamenica2011bayesian`); plain author-year is fine. The related-lit-writer uses these as the seed set.

Assemble the answers into the structured `brief.md` format. Write to `$TARGET/brief.md`.

If the user says "I'll write the brief myself" — fine. Skip the walkthrough and tell them to fill in `$TARGET/brief.md` directly.

## Step 4 — Remind about proofs

Tell the user:

> "Now drop your pre-baked proofs into `$TARGET/proofs/`. Two formats accepted: LaTeX (`*.tex`, preferred) or markdown with LaTeX math (`*.md`). The proofs come from your separate proof-checking pipeline — this repo's roles don't write or edit math.
>
> If your proof pipeline leaves internal references (e.g., 'in iteration 3 we verified…'), run `/proof-clean <target>` afterward to purge them. It outputs a cleaned copy + diff for review.
>
> When the proofs are in, say `draft <target>` and the orchestrator will write the paper around them."

## Step 5 — Sanity check, then hand off

Confirm:
- `$TARGET/brief.md` is non-skeletal.
- `$TARGET/proofs/` exists.
- `$TARGET/tex/sections/` exists with the empty stubs.
- `$TARGET/tex/main.tex`, `preamble.tex`, `refs.bib` all present.

Print a final summary:

```
✓ Paper scaffold created at $TARGET
✓ brief.md populated
☐ proofs/ — drop your LaTeX/markdown here
  Then run: draft $TARGET
```

If the user wants to proceed immediately *and* has proofs ready, you can hand off to `draft-paper`. Otherwise stop and let them populate proofs.

## Hard rules

- **Target must be outside this repo.** Refuse any path under `PaperbackWriter/`.
- **Never invent the brief.** If the user can't articulate the claim, push back — the paper isn't ready to draft.
- **Don't generate proofs.** Math is the user's job; this skill doesn't write a single equation.
- **Don't fire `draft-paper` without proofs in place.** If proofs are missing, stop after Step 5.

## What this skill does NOT do

- Doesn't write proofs.
- Doesn't write the abstract, intro, or any section. That's `draft-paper`'s job once the inputs are in.
- Doesn't initialize git in the target directory. The user manages source control of their papers.
