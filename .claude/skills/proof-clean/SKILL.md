---
name: proof-clean
description: |
  Purge pipeline-internal references from the user's pre-baked proofs in `<target>/proofs/`.
  Outputs a `_cleaned/` directory + a diff report. **Never touches the math itself** — only
  removes meta-prose referring to the proof-checking pipeline (e.g., "in iteration 3 of the
  verification", "as shown in the previous step of the pipeline"). The user reviews the diff
  and decides whether to swap in the cleaned files.
---

# proof-clean

## Why this exists

The user's proofs are produced by a separate proof-checking pipeline. That pipeline often leaves traces in the prose around the math — references to iterations, verification steps, internal labels — that don't belong in a published paper. This skill removes them.

The math is **never** touched. Only the meta-prose wrappers are.

## Invocation

User says: "clean the proofs in `<target>`", "purge pipeline refs", "proof-clean `<slug>`".

Also suggested automatically by `draft-paper` if `_cleaned/` is missing or stale.

## What this skill does

1. Read every `.tex` and `.md` file in `<target>/proofs/` (excluding any existing `_cleaned/` subdirectory).
2. Spawn the `proof-cleaner` agent. It produces a cleaned version of each file.
3. Write the cleaned versions to `<target>/proofs/_cleaned/<filename>`.
4. Produce a diff report at `<target>/proofs/_cleaned/CHANGES.md` showing every deletion and its rationale.
5. Surface the diff summary to the user.

The user reviews `CHANGES.md`. If they like the cleanup, they swap the cleaned files over manually (or ask Claude to do it). Until they swap, the original `proofs/*.tex` files are untouched.

## What gets purged

Examples of pipeline-internal references the cleaner removes:

- "In iteration 3 of the verification, we established that…"
- "As shown in step 4.2 of the proof pipeline…"
- "The previous formal-methods run confirmed…"
- "Following the strategy outlined in our internal note…"
- "We have verified this in the type system at `lemma_4.lean`…"
- Comments like `% [auto-generated from run 2025-03-14]`

The cleaner keeps the math statement that follows such phrases. It just removes the meta-wrapper.

## What does NOT get touched

- Theorem, lemma, proposition, corollary, definition statements.
- Proof steps and the math within them.
- References to *other parts of this paper* (e.g., "by \cref{thm:main}" or "from Lemma 2.1"). These are legitimate cross-references; only pipeline-external references are purged.
- Citations to other papers (`\cite{...}`).
- Author intent comments (e.g., `% TODO: tighten this bound`).

If the cleaner is uncertain whether something is a pipeline artifact or a real intra-paper reference, it leaves it alone and notes the ambiguity in `CHANGES.md`.

## Output

```
<target>/proofs/_cleaned/
├── <file1>.tex          ← cleaned versions
├── <file2>.tex
├── ...
└── CHANGES.md            ← diff report with rationale per change
```

A summary to the user:

```
## proof-clean report — <target>

### Files processed: N

### Total deletions: M
- pipeline-iteration references: K
- pipeline-step references: K
- auto-generated comments: K
- other: K

### Ambiguous (not removed, flagged): K
- See _cleaned/CHANGES.md for details.

### Math untouched: YES
```

## Hard rules

- **Never modify math.** Theorem statements, equations, formulas — untouched.
- **Never remove intra-paper cross-references** (`\cref{thm:main}`, "by Lemma 2.1", etc.).
- **Never remove citations** to other papers.
- Output to `_cleaned/`, never overwrite the originals.
- When in doubt, leave it alone and flag it.
