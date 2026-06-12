---
name: draft-paper
description: |
  End-to-end first-draft orchestrator. Takes an **external target folder path** (the paper
  lives outside this repo). Sets up missing scaffold pieces, then runs the role agents in
  two phases: Phase 1 (parallel) writes related-lit and model-prose. Phase 2 (sequential)
  writes results-prose, then optional discussion, then intro (incl. closing if warranted),
  then abstract last. Pauses for review between phases. Use when the user says "draft
  <path>", "draft `~/Documents/papers/foo`", or similar.
---

# draft-paper

The single entry point. The user passes a **target folder path** — the paper does not live in this repo. This skill writes inside that external folder.

## Invocation

User says: "draft `<path>`", "draft `~/Documents/papers/foo`", "write `<path>`", "first draft of `<path>`".

If the user passes just a name with no path (e.g., "draft foo"), refuse and ask where the paper lives. **Do not default to creating a paper inside this repo.** Papers must live outside.

## Resolve the path

1. Expand `~` and resolve to an absolute path. Call this `$TARGET`.
2. Reject `$TARGET` if it's inside this repo (the `PaperbackWriter` directory). Print: "This repo is a toolkit. Papers must live outside it." Suggest a path under `~/Documents/` or wherever the user keeps their work.
3. If `$TARGET` does not exist, ask the user once whether to create it.

## Preconditions

The user is expected to bring two things to `$TARGET`:
- `$TARGET/brief.md` — what the paper claims, who should care, comparison anchors (one paragraph, ~150 words).
- `$TARGET/proofs/` — pre-baked LaTeX or markdown from their separate proof-checking pipeline.

Check both. If `brief.md` is missing or is still the scaffold skeleton, refuse. If `proofs/` is empty, refuse. Tell the user what to provide and stop. **Do not draft against missing inputs.**

## Set up missing scaffold

For files the user is *not* expected to bring, copy from this repo's `scaffold/` directory if they're missing in `$TARGET`:

| Path in `$TARGET` | Copy from `scaffold/` if missing |
|-|-|
| `tex/main.tex` | yes |
| `tex/preamble.tex` | yes |
| `tex/refs.bib` | yes (initial; will be populated) |
| `tex/sections/*.tex` | yes (empty stubs with TODO comments) |
| `proofs/README.md` | yes (only if `proofs/README.md` itself is missing) |
| `brief.md` | **no — user provides** |
| `proofs/*.tex`, `proofs/*.md` | **no — user provides** |

Never overwrite existing files in `$TARGET`. Only create the ones that are missing.

## Pre-flight: clean the proofs

If `$TARGET/proofs/_cleaned/` does not exist or is older than the newest file in `$TARGET/proofs/`:

> Suggest the user run the `proof-clean` skill first: *"clean the proofs in `$TARGET`"*. Don't run it automatically — the user reviews the cleanup diff.

If the user wants to proceed without cleaning, that's their call. Note it in the report.

## Phase 0 — framing (autonomous; no pause)

Run the WISDOM §11 scan test on `$TARGET/brief.md` against the headline result in `$TARGET/proofs/`:

- Does the brief state an **economic question**?
- Does it contain the **main result as one symbol-free English sentence**?
- Does any named application pass the **swap test** (it could not be replaced without changing an assumption, theorem, or claim)?

If all three pass, note "Phase 0: brief passed scan test" in the report and move on.

If any fails, spawn the `framing-writer` agent with `$TARGET`. It works backwards from the headline theorem to the question it answers, backs up `brief.md` → `brief.original.md`, rewrites `brief.md`, and records the derivation in `$TARGET/notes/derived-framing.md`. **Do not pause for the user** — this phase is autonomous by design. Note in the report: "Phase 0: framing derived (brief.md rewritten; original preserved; see notes/derived-framing.md)".

## Phase 1 — parallel

Spawn the following roles **in parallel** (one tool turn, two Agent tool calls). Pass each agent the absolute `$TARGET` path so it knows where to read/write:

- `model-prose-writer` — writes `$TARGET/tex/sections/model.tex` around `$TARGET/proofs/` definitions.
- `related-lit-writer` — writes `$TARGET/tex/sections/related.tex` against the locked citation universe (`$TARGET/tex/refs.bib` + `$TARGET/brief.md` anchors + repo's `references/pdfs/`).

When both return:

1. Show the user a brief summary: lines written, any `[MATERIAL GAP]` / `[CITATION NEEDED]` markers.
2. **Pause.** Ask the user to review `$TARGET/tex/sections/model.tex` and `related.tex` and confirm before Phase 2.

If the user wants edits before continuing, apply them by re-firing the relevant role with their notes appended, then re-prompt for review. Do not proceed to Phase 2 until the user says go.

## Phase 2 — sequential

Once the user OKs Phase 1:

### Step 2a — `results-prose-writer`

Reads `$TARGET/proofs/` and `$TARGET/tex/sections/model.tex` (for notation consistency). Writes `$TARGET/tex/sections/results.tex`.

### Step 2b — `discussion-writer` *(conditional)*

Skip by default. Run if:
- The paper is long-form (likely > 25 pages once assembled), OR
- `$TARGET/brief.md` explicitly mentions extensions, robustness, or applications that haven't been written elsewhere, OR
- The user asks for it.

Heuristic: if you're unsure, ask the user once before running.

### Step 2c — `intro-writer`

Now that the body is on the page, the intro can be precise. Writes `$TARGET/tex/sections/intro.tex`. Per the agent's spec, it also writes a one-paragraph closing if the heuristic says yes; otherwise no conclusion section is added.

### Step 2d — `abstract-writer`

Last. Reads the intro and `$TARGET/proofs/` to distill the 70–150-word abstract.

After all four steps:

1. Show the user the assembled draft summary.
2. Spawn the `gatekeeper` skill (parallel `integrity-gatekeeper` + `exposition-gatekeeper`), pointed at `$TARGET`.
3. Run `latex-compile` with cwd = `$TARGET/tex/`.
4. Report.

## Output

A structured report at the end:

```
## draft-paper report — $TARGET — <timestamp>

### Phase 0
- scan test: passed / framing derived (see notes/derived-framing.md)

### Phase 1
- $TARGET/tex/sections/model.tex: N lines, M markers
- $TARGET/tex/sections/related.tex: N lines, M markers

### Phase 2
- results.tex: N lines, M markers
- discussion.tex: skipped / written (N lines)
- intro.tex: N lines, M markers; conclusion paragraph: yes/no
- abstract.tex: N words

### Gatekeeper
- Critical: N
- Important: N
- Minor: N

### Compile
- PDF: $TARGET/tex/main.pdf (N pages)
- Warnings: N
```

## Hard rules

- **Papers live outside this repo.** Refuse to draft into any path under the `PaperbackWriter` directory.
- **Do not edit anything in `$TARGET/proofs/`.** The math is the user's.
- **Do not skip the Phase 1 review pause** unless the user explicitly says "go through without stopping."
- **Do not generate citations outside the locked universe.**
- **Do not invent results, lemmas, or proof steps.** If a role emits `[MATERIAL GAP]`, surface it and stop that role's section.
- **Do not overwrite files in `$TARGET` that already exist** (other than the section .tex files, which are the roles' job; exception: Phase 0's `framing-writer` may rewrite `brief.md` after backing it up to `brief.original.md`).

## What this skill does NOT do

- Does not write proofs.
- Does not call Codex or Opus externally.
- Does not commit `$TARGET` to git.
- Does not push or deploy.
- Does not iterate beyond one draft pass — for revisions, the user re-fires individual roles or the `motivation-pass` skill.
