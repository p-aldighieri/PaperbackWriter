# PaperbackWriter

A **toolkit** of writing skills, role-based agents, and structural specs for drafting **economic theory papers** with Claude. Papers live **outside** this repo. The orchestrator takes a path to your paper folder and writes there.

## Discipline

> The papers you write are **not** committed to this repo. This repo is the toolkit; your papers live wherever you keep your work (`~/Documents/papers/...`, your Dropbox, anywhere). The orchestrator refuses to draft into any path inside `PaperbackWriter/`.

## Quickstart for first-time users

Just say *"new paper"* and Claude walks you through the setup via the `new-paper` skill: picks a path outside this repo, copies the scaffold, and helps you fill in the brief. You then drop your proofs in and say `draft <path>`.

## What you do, what Claude does (manual version)

```
You:
  1. Make a folder somewhere outside this repo: ~/Documents/papers/your-paper
  2. Write a brief: ~/Documents/papers/your-paper/brief.md
       (one paragraph: claim, who cares, comparison anchors)
  3. Drop pre-baked proofs in: ~/Documents/papers/your-paper/proofs/
       (LaTeX or markdown from your separate proof-checking pipeline)
  4. (optional) "clean the proofs in ~/Documents/papers/your-paper"   → /proof-clean
  5. "draft ~/Documents/papers/your-paper"                            → /draft-paper

Claude (via the draft-paper skill):
  - Resolves the path; refuses if it's inside this repo
  - Copies missing scaffold pieces from scaffold/ (tex/, sections/, refs.bib)
  - Never overwrites your brief.md or proofs/
  Phase 1 (parallel) — writes <target>/tex/sections/{related,model}.tex
  ┌──────────────────────────────────────┐
  │   model-prose-writer  related-lit-writer
  └──────────────────────────────────────┘
                  │
              pause for your review
                  │
  Phase 2 (sequential) — writes <target>/tex/sections/{results,discussion?,intro,abstract}.tex
   ┌──────────────────────┐
   │ results-prose-writer │
   └─────────┬────────────┘
             ▼
   ┌──────────────────────┐
   │ discussion-writer    │  (only if the paper needs it — long-form + extensions + applications)
   └─────────┬────────────┘
             ▼
   ┌──────────────────────┐
   │ intro-writer         │  (also writes closing paragraph if the heuristic says yes)
   └─────────┬────────────┘
             ▼
   ┌──────────────────────┐
   │ abstract-writer      │  (last — distills the now-stable intro)
   └─────────┬────────────┘
             ▼
   gatekeepers (integrity + exposition, in parallel)
             │
             ▼
   latex-compile → main.pdf
```

LaTeX `\input{}` mechanically aggregates the section files in `main.tex`. There's no separate aggregator — the LaTeX file IS the aggregator.

## Section ownership

| Section | Agent | Inputs |
|-|-|-|
| `tex/sections/abstract.tex` | `abstract-writer` (runs last) | STRUCTURE.md + WISDOM.md + brief.md + finished intro |
| `tex/sections/intro.tex` (+ optional closing) | `intro-writer` | STRUCTURE.md + WISDOM.md + brief.md + proofs/ + assembled body |
| `tex/sections/related.tex` | `related-lit-writer` | STRUCTURE.md + WISDOM.md + brief.md + refs.bib + repo's references/pdfs/ |
| `tex/sections/model.tex` | `model-prose-writer` | STRUCTURE.md + WISDOM.md + brief.md + proofs/ |
| `tex/sections/results.tex` | `results-prose-writer` | STRUCTURE.md + WISDOM.md + brief.md + proofs/ + model.tex |
| `tex/sections/discussion.tex` (optional) | `discussion-writer` | STRUCTURE.md + WISDOM.md + assembled paper |
| (read-only) | `integrity-gatekeeper`, `exposition-gatekeeper` | full draft |
| (cleanup) | `proof-cleaner` (via `proof-clean` skill) | proofs/ |

## How the spec works

- **[STRUCTURE.md](STRUCTURE.md)** — descriptive. Section-by-section conventions distilled from a 20-paper corpus.
- **[WISDOM.md](WISDOM.md)** — prescriptive. Decision-oriented advice from named theorists (Thomson, Cochrane, Board & Meyer-ter-Vehn, Shapiro, Head, Bellemare, McCloskey, Mankiw). Body-vs-appendix calls, proof verbosity, intro craft, reviewer failure modes.
- **[prompts/style-guide.md](prompts/style-guide.md)** — sentence-level prose conventions.
- **[pipeline/README.md](pipeline/README.md)** — dependencies if you skip the orchestrator and invoke individual roles.

## Iterating after the first draft

The orchestrator does one pass. After review, fire individual roles for revisions:

- *"Tighten the motivation in `<path>`"* → `motivation-pass` skill → `motivation-writer` agent.
- *"Rewrite the related lit in `<path>`"* → `related-literature` skill.
- *"Check the citations in `<path>`"* → `citation-check` skill (verify every `refs.bib` entry against Crossref; report-only). Run before any "final" compile / submission.
- *"Audit `<path>`"* → `gatekeeper` skill (parallel integrity + exposition).
- *"Compile `<path>`"* → `latex-compile`.

## Proofs

The math is **out of scope** for this repo. Proofs come pre-baked from your separate proof-checking pipeline. Drop LaTeX or markdown into `<target>/proofs/`; the prose roles wrap them. No role here edits math.

If your proof pipeline leaves pipeline-internal references (e.g., "in iteration 3 we verified…"), run the `proof-clean` skill before `draft-paper`. It produces a cleaned copy + diff for your review at `<target>/proofs/_cleaned/`.

## Layout (of this repo, the toolkit)

```
STRUCTURE.md                  ← descriptive spec from the 20-paper corpus
WISDOM.md                     ← prescriptive spec from public writing guides

references/
  README.md                   ← index of the 20 canonical papers
  pdfs/                       ← symlink to external sample dir (gitignored)

scaffold/                     ← copied into <target> by the orchestrator if missing
  brief.md                    ← (you supply this in <target>, not copied)
  proofs/README.md
  tex/main.tex
  tex/preamble.tex
  tex/refs.bib
  tex/sections/

.claude/
  skills/
    new-paper/                ← first-run: bootstrap + brief walkthrough
    draft-paper/              ← main entry point once brief + proofs are ready
    proof-clean/              ← purge pipeline-internal references from proofs/
    gatekeeper/               ← integrity + exposition audit
    motivation-pass/          ← tighten intro P1-P2
    related-literature/       ← lit review only
    citation-check/           ← verify every refs.bib entry vs Crossref (report-only)
    latex-compile/            ← build the PDF
  agents/
    abstract-writer.md
    intro-writer.md
    motivation-writer.md
    related-lit-writer.md
    model-prose-writer.md
    results-prose-writer.md
    discussion-writer.md
    integrity-gatekeeper.md
    exposition-gatekeeper.md
    proof-cleaner.md

pipeline/README.md            ← role dependencies (if you bypass the orchestrator)
prompts/style-guide.md        ← sentence-level prose conventions
CLAUDE.md                     ← guidance for Claude in this repo
```

## Layout (of a paper, in `<target>` outside the repo)

```
<target>/
├── brief.md                  ← you write
├── proofs/                   ← you drop in (LaTeX or markdown)
│   ├── theorems.tex
│   ├── proofs.tex
│   ├── ...
│   └── _cleaned/             ← optional, produced by proof-clean
├── tex/                      ← scaffold copied; roles write into sections/
│   ├── main.tex
│   ├── preamble.tex
│   ├── refs.bib
│   └── sections/
│       ├── abstract.tex
│       ├── intro.tex
│       ├── related.tex
│       ├── model.tex
│       ├── results.tex
│       ├── discussion.tex
│       └── appendix.tex
└── notes/                    ← optional, for Codex/Opus prompts
```
