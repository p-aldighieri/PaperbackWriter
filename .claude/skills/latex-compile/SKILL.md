---
name: latex-compile
description: |
  Compile a paper in `<target>/tex/` to PDF. Runs pdflatex → bibtex → pdflatex → pdflatex,
  parses the .log for errors, surfaces a focused error report. Use whenever the user says
  "compile", "build the PDF", or after any non-trivial edit to the .tex sources.
---

# latex-compile

## Invocation

User says one of: "compile", "compile the paper", "build the PDF", "rerun latex".

You should also invoke this skill automatically after every successful pass through the gatekeeper, to confirm the paper still builds.

## What this skill does

0. **Pre-compile sanitation (harvest-junk guard).** Before building, scan `main.tex` for two artifacts that creep in when a `.tex` was harvested from an LLM/browser response rather than authored in place:
   - **Trailing junk after the document ends:** any non-whitespace content *after* the first `\end{document}`. This is almost always assistant chatter that followed the code block (e.g. lines like `G. appendix.tex patch`, `Notes`, `No new citation keys were added…`). LaTeX silently ignores it, so the PDF still builds and the problem goes unnoticed — but it pollutes the submission source.
   - **Leading junk before the preamble:** any non-whitespace content *before* the first `\documentclass` (e.g. a ```` ```latex ```` fence or a "Here is the file:" preamble line).

   If either is present: save a one-time backup `main.tex.bak` (only if it doesn't already exist), strip the offending region, and **report it** — e.g. "Stripped 6 lines of harvest junk after `\end{document}` (backup at `main.tex.bak`)." Do **not** touch anything between `\documentclass` and `\end{document}` — that is the real document. This is the one sanctioned exception to "does not edit `.tex` sources": removing text outside the document body is not editing the paper.

   One-liner that does it (POSIX `sed`): `sed -n '/\\documentclass/,/\\end{document}/p' main.tex` extracts exactly the document; compare line counts to detect junk before acting.

1. Identify the target. If the user names a slug, use `<target>/tex/`. Otherwise look for the most-recently-edited paper directory.
2. From that `tex/` directory, run the four-pass build:

   ```bash
   pdflatex -interaction=nonstopmode -halt-on-error main.tex
   bibtex main
   pdflatex -interaction=nonstopmode main.tex
   pdflatex -interaction=nonstopmode main.tex
   ```

   If `latexmk` is available, prefer:

   ```bash
   latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
   ```

3. Parse `main.log`. Report:
   - **Errors** (lines starting `!`) — show 3 lines of source context + the error message.
   - **Undefined references** — list them.
   - **Undefined citations** — list them, cross-check against `refs.bib`. If a key is in `refs.bib` but bibtex didn't pick it up, suggest rerunning bibtex.
   - **Overfull / underfull boxes** — summarize counts only; do not fix.
   - Final PDF path on success.

## Reporting style

- On success: one line — "Built `<target>/tex/main.pdf` (N pages)." plus warning counts.
- On failure: lead with the first error, show source context, suggest the likely fix.
- Never claim success unless `main.pdf` exists and the log's final status confirms it.

## Failure modes to watch for

- **Missing `econometrica.bst`** — for Econometrica submission, swap the official `.bst` from econometricsociety.org. Default template uses natbib + plainnat-compatible fallback.
- **Stale aux files** — if errors look like ghosts of removed labels, run `rm *.aux *.bbl *.blg` and rebuild.
- **Proofs not found** — if `\input{../proofs/...}` fails because no file is there, the user hasn't dropped in their pre-baked proofs yet. Suggest they do so.

## What this skill does NOT do

- Does not edit `.tex` sources.
- Does not rebuild figures.
- Does not push to remote or deploy.
- Does not touch anything in `proofs/`.
