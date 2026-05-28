---
name: gatekeeper
description: |
  Audit the current draft for craft and integrity violations. Runs `integrity-gatekeeper`
  and `exposition-gatekeeper` agents in parallel, synthesizes findings into Critical /
  Important / Minor. **Reports only — never auto-fixes.** **Does not check math.** Use
  after any substantive draft pass.
---

# gatekeeper

## Philosophy

Gatekeepers fail closed. They emit refusal classes, not suggestions. The user decides whether to act.

This pipeline **does not check math** — proofs come from a separate pipeline and are immutable input. The gatekeepers check prose integrity (citations, claim faithfulness against `brief.md`), structure, and craft.

## Invocation

User says: "run the gatekeeper", "audit the draft". Auto-invoked after `hydrate` skills and `motivation-pass`.

## What this skill does

1. Spawn **`integrity-gatekeeper`** and **`exposition-gatekeeper`** agents **in parallel** (one Agent call with two tool uses).

   - `integrity-gatekeeper` audits citation faithfulness, claim faithfulness (prose vs `brief.md`/`proofs/`), notation consistency, cross-ref integrity.
   - `exposition-gatekeeper` audits structure, prose, signposting, theory-paper conventions against `STRUCTURE.md`.

2. Synthesize findings into a single report with three bands:

   - **Critical** — anything in the integrity refusal classes:
     - `CLAIM-UNSUPPORTED`: a prose claim doesn't trace to `brief.md` or `proofs/`.
     - `FABRICATED-REFERENCE`: a `\cite{}` key not in `refs.bib`.
     - `DANGLING-REF`: a `\cref{...}` to a non-existent label.
     - `NOTATION-MISMATCH`: prose notation doesn't match `model.tex` / `proofs/`.

   - **Important** — craft / structural issues from the exposition-gatekeeper:
     - `BOILERPLATE-INTRO`, `INTRO-OVERCITED`, `NO-CONTRIBUTION-SENTENCE`, `ROADMAP-OVERLOADED`
     - `RELATED-CHRONOLOGICAL`, `NO-DIFFERENTIATION`
     - `ORPHANED-NOTATION`, `NO-INTUITION`
     - Section-balance deviations from STRUCTURE.md norms.

   - **Minor** — copy-edit issues:
     - `STYLE-WORD`, `STYLE-HEDGE`, `PARAGRAPH-LENGTH`
     - `ABSTRACT-BOILERPLATE`, `ABSTRACT-LENGTH`, `ABSTRACT-CITES`

3. **Do not edit any files.** Output is the report.

## Output format

```
## Gatekeeper report — <target> — <timestamp>

### Critical (N)
- [CLAIM-UNSUPPORTED] intro.tex:42 — "robust to any prior" not in brief.md or proofs/.
- [FABRICATED-REFERENCE] related.tex:13 — \cite{bergemann2024robust} not in refs.bib.

### Important (N)
- [BOILERPLATE-INTRO] intro.tex:3 — opens with "In this paper, we…"
- [RELATED-CHRONOLOGICAL] related.tex paragraph 2

### Minor (N)
- [STYLE-WORD] intro.tex:18 — "novel"
- ...

### What I did not check
- Mathematical correctness (out of scope for this repo).
- Whether cited results say what's attributed to them (only that citations exist).
```

## When to run it

- After every substantive writing-role pass.
- Before every `latex-compile` you think of as "final."
- Whenever the user asks.

## What it does NOT do

- Does not auto-fix.
- Does not check math.
- Does not evaluate whether the paper is "good" — that's the user's call.
