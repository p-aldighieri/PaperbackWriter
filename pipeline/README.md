# Pipeline

The **role-based** pipeline. Each role owns a section. The `draft-paper` skill orchestrates them; this doc explains the dependencies so you know what's happening (or so you can invoke individual roles outside the orchestrator).

## The roles

| Role | Owns | Reads | Writes |
|-|-|-|-|
| `model-prose-writer` | model | STRUCTURE.md, brief.md, proofs/ | sections/model.tex |
| `related-lit-writer` | related lit | STRUCTURE.md, brief.md, refs.bib, references/pdfs/ | sections/related.tex |
| `results-prose-writer` | results | STRUCTURE.md, brief.md, proofs/, model.tex | sections/results.tex |
| `discussion-writer` | discussion | STRUCTURE.md, brief.md, full paper | sections/discussion.tex |
| `intro-writer` | intro (+ optional closing) | STRUCTURE.md, brief.md, proofs/, assembled body | sections/intro.tex |
| `motivation-writer` | intro P1-P2 only | STRUCTURE.md, brief.md, current intro | diff against intro.tex |
| `abstract-writer` | abstract | STRUCTURE.md, brief.md, finished intro, proofs/ | sections/abstract.tex |
| `integrity-gatekeeper` | (read-only) | citations, claim-trace, notation, cross-refs | report |
| `exposition-gatekeeper` | (read-only) | structure, prose, craft against STRUCTURE.md | report |
| `proof-cleaner` | proofs/ meta-prose only | proofs/ | _cleaned/ + CHANGES.md |

## Dependency graph

```
   brief.md  +  proofs/  (you provide)
        │
        │   (optional: proof-clean → _cleaned/)
        ▼
   ┌──────────────────────────────────────────────────┐
   │  Phase 1 — parallel, independent inputs           │
   │                                                    │
   │  model-prose-writer       related-lit-writer       │
   │  reads brief + proofs     reads brief + refs.bib   │
   │                                                    │
   └──────────────────────────────────────────────────┘
        │
        │   YOU REVIEW
        ▼
   results-prose-writer
   (depends on model.tex for notation; proofs/ for theorems)
        │
        ▼
   discussion-writer        (optional; long-form + extensions)
        │
        ▼
   intro-writer
   (writes intro now that the body exists; optional closing paragraph)
        │
        ▼
   abstract-writer
   (last — distills the now-stable intro)
        │
        ▼
   gatekeepers              (parallel: integrity + exposition)
        │
        ▼
   latex-compile
```

The `draft-paper` skill executes this graph automatically with a pause between phases.

## Why this order

- **Phase 1 in parallel.** `model-prose-writer` and `related-lit-writer` have no shared dependencies — model reads `proofs/`, related-lit reads `refs.bib` + brief anchors. Both can fire at once.
- **Results before discussion.** Discussion talks about what the results imply; it needs results to exist.
- **Intro after the body.** A good intro accurately previews what the paper says. Writing the intro before the body produces speculative motivation.
- **Abstract last.** The abstract distills the intro. Writing it first means rewriting it after every subsequent section drifts.

## Invoking individual roles

Useful when iterating after the first draft:

- *"Tighten the motivation in `<target>`"* → `motivation-pass` skill → `motivation-writer`.
- *"Rewrite the related lit"* → `related-literature` skill → `related-lit-writer`.
- *"Redraft the abstract"* → directly spawn `abstract-writer` (no skill needed for a single role).
- *"Audit the draft"* → `gatekeeper` skill.

## When proofs change

If you swap in a new version of `proofs/`, the section files written against the old version may be stale. The gatekeeper will catch notation mismatches and unsupported claims. Re-fire the affected role:

- `proofs/theorems.tex` changed → re-fire `results-prose-writer`, then `intro-writer` (contribution sentence) and `abstract-writer`.
- `proofs/definitions.tex` changed → re-fire `model-prose-writer`, then check downstream.

In practice, large proof changes are best handled by re-running the whole `draft-paper` skill.

## Calling Codex / Opus

The pipeline does not call external models. When you want a Codex or Opus pass on a section:

1. The relevant skill (or you manually) writes a focused prompt to `<target>/notes/<section>-prompt.md`.
2. You run that prompt externally.
3. You paste the result back into `sections/<section>.tex`.
4. Run the `gatekeeper` skill.

External passes are **explicit and traceable** by design. No silent model swaps.

## What's NOT in this pipeline (by design)

- **Proof checking.** Separate pipeline. This one trusts `proofs/`.
- **Result ideation.** Roles write papers, they don't prove theorems.
- **Web search for new citations.** Citation universe is `refs.bib` + `brief.md` anchors + `references/pdfs/`.
- **End-to-end autonomy.** You review at least once mid-pipeline (after Phase 1).
