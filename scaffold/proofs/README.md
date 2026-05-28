# Proofs

Drop your pre-baked proofs here. Two formats accepted:

- **LaTeX** (`*.tex`) — preferred. The roles' `model-prose-writer` and `results-prose-writer` `\input` from these files when assembling `sections/model.tex`, `sections/results.tex`, and `sections/appendix.tex`.
- **Markdown with LaTeX math** (`*.md`) — accepted. A minimal one-time conversion to `.tex` happens before the prose pipeline runs.

## What goes here

- Theorem and proposition statements (formal).
- Definitions of objects (formal).
- Assumptions.
- Proofs.
- Auxiliary lemmas.

## What does NOT go here

- Motivation prose. That's the intro's job.
- Discussion of modeling choices. That goes in `sections/discussion.tex`.
- Comparison to other papers' results. That's the related-lit's job.

## Conventions

Whatever you bring in. The prose pipeline adapts to your notation; the `exposition-gatekeeper` will flag notation that's introduced but never used in prose. The pipeline does **not** edit your math.

## Suggested layout

```
proofs/
├── theorems.tex      ← headline results
├── definitions.tex   ← objects + assumptions
├── lemmas.tex        ← auxiliary results
└── proofs.tex        ← the proofs themselves
```

But any layout works. The roles read everything in this directory.
