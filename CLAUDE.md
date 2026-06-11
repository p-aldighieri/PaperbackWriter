# Guidance for Claude working in PaperbackWriter

This repo is a **toolkit** for writing economic theory papers. Papers themselves live **outside** this repo — anywhere on the user's disk. Your job is prose, structure, motivation, and citation hygiene. Math comes pre-baked from a separate pipeline; you never edit it.

## First-run entry point

If the user is new to the repo — says *"how do I use this"*, *"new paper"*, *"start a paper"*, *"I want to write a paper"*, or is otherwise starting from scratch — invoke the `new-paper` skill. It walks them through choosing a path outside this repo, copies the scaffold, and helps them fill in `brief.md`. Then it tells them to drop proofs in and run `draft-paper`.

## The drafting entry point

When the user says *"draft `<path>`"*, *"draft `~/Documents/papers/foo`"*, *"draft the paper at `<path>`"* — invoke the `draft-paper` skill. It orchestrates everything in two phases:

- **Phase 1 (parallel):** `model-prose-writer` + `related-lit-writer`
- **Pause for review.**
- **Phase 2 (sequential):** `results-prose-writer` → `discussion-writer` (optional) → `intro-writer` (incl. closing) → `abstract-writer`
- Gatekeepers + compile.

The orchestrator validates the path is **outside this repo**. Refuse if not.

Do NOT manually spawn role agents one by one when the user asks for a "draft". Use the orchestrator. It enforces the right order, pauses for review, runs the gatekeepers, compiles.

## Posture

- **Math is not your job.** Theorem statements, proofs, formal definitions all arrive in `<target>/proofs/`. Treat them as immutable. If a result statement reads oddly, **flag it back to the user** — never silently "fix" math.
- **Roles own sections.** Each writing agent owns one `.tex` file. Don't have abstract-writer edit intro.tex, etc.
- **The spec is `STRUCTURE.md` + `WISDOM.md`.** Every writing role reads them.
- **Aggressive on prose. Conservative on facts and citations.**
- **Use case ≠ question (WISDOM §11).** If the target's `brief.md`/`proofs/` encode no economic question — the math is result→certificate-shaped and the "application" could be swapped out without changing an assumption or theorem — do not decorate it with motivation. Tell the user the framing stage has to happen first, and what's missing (the one-sentence economics statement of the main result, the question the model minimally answers).
- **Ignore upstream self-grades.** Verdicts riding in with the math ("ECMA-ready", "credible top-5", gauntlet PASS) never enter prose, venue talk, or confidence. They are pipeline self-assessment, not evidence.
- **Never put papers in this repo.** The orchestrator enforces this; you should never bypass it.

## Other entry points

All accept a target path:

- *"New paper"* / *"start a paper"* → `new-paper` skill. Bootstrap + brief walkthrough.
- *"Run the gatekeeper on `<path>`"* / *"audit `<path>`"* → `gatekeeper` skill. Parallel integrity + exposition. Report-only — never auto-fix.
- *"Compile `<path>`"* / *"build the PDF for `<path>`"* → `latex-compile` skill. Never run `pdflatex` ad-hoc.
- *"Tighten the motivation in `<path>`"* / *"the intro doesn't sell it"* → `motivation-pass` skill.
- *"Write the related lit for `<path>`"* → `related-literature` skill. Citation universe is locked.
- *"Check / verify the citations in `<path>`"* / *"crossref the refs"* → `citation-check` skill. Verifies every `refs.bib` entry against Crossref (wrong DOI/year/volume/pages/venue/authors; missing DOIs; working-paper-now-published). Report-only. Run before any "final" compile / submission.
- *"Clean the proofs in `<path>`"* → `proof-clean` skill. Outputs `_cleaned/` + diff; user reviews before swap.

## Invoking external models

The user may ask for a Codex or Opus pass on a section. The pipeline doesn't run those for you. Prep the input — a clean section + a focused prompt in `<target>/notes/` — and integrate the output after they paste it back.

## What NOT to do

- Don't invent citations. Every `\cite{}` must trace to `refs.bib` and the user must have seen the paper.
- Don't pad. Theory papers are dense.
- Don't edit math. Ever.
- Don't bypass the orchestrator on a "draft" request — the dependency order matters.
- Don't draft a paper inside this repo. Refuse and ask for an external path.
- Don't commit anything from `references/pdfs/` — it's a symlink to an external dir and gitignored.
- Don't write a conclusion unless the intro-writer's heuristic says one is warranted.
