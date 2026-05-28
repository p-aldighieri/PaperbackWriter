# Style guide — econ theory paper prose

Prose-level conventions. Structural conventions (section ordering, length norms, section-by-section internal patterns) live in [`STRUCTURE.md`](../STRUCTURE.md) — this guide is its sentence-level companion. The `exposition-gatekeeper` enforces both.

## The four invariants

1. **Math is out of scope.** Proofs come pre-baked in `<target>/proofs/`. Never edit formal statements, theorems, lemmas, or proofs. If math reads oddly, flag it back to the user.
2. **Demonstrate, don't assert.** Cut "interesting", "important", "novel", "elegant", "deep". If the result is interesting, the reader will notice.
3. **Theme over chronology.** Related lit is organized by what's being argued, not who-published-when.
4. **Density beats length.** Cut, don't fluff.

## Forbidden phrases

- "In this paper, we…" — opener. (Allowed once, in the intro contribution paragraph.)
- "We contribute by / make the following contribution(s)."
- "It is interesting / important / striking / surprising that…"
- "Intuitively, …" used as throat-clearing.
- "We believe / we feel / arguably / in our opinion."
- "There is a vast / rich / growing literature on…"
- "Future work will…" / "We leave for future work…"
- "Note that…" — almost always cuttable.
- "It is well-known that" as a sentence opener.

## Citation conventions

- `\citet{}` for textual citations: "Kamenica and Gentzkow (2011) show that…"
- `\citep{}` for parenthetical: "…concavification (Kamenica and Gentzkow, 2011)."
- First mention of a paper in a strand: textual. Later mentions: parenthetical, unless syntax demands textual.
- Citation key format: `firstauthor + year + keyword`, all lowercase. `kamenica2011bayesian`.
- Every entry in `refs.bib` gets a `% one-sentence summary` line above it. The `related-lit-writer` agent reads these.

## Notation hygiene

- Every symbol introduced in section N is used by section N+1. If not, cut it.
- Reuse standard letters where possible: $\theta$ for type, $a$ for action, $\mu$ for belief/measure, $\pi$ for policy, $u$ for utility, $\Theta$ for type space.
- Bold for vectors only if a non-bold scalar of the same letter also appears.
- Avoid Greek/Latin same-letter collisions ($\nu / v$).
- Notation is introduced in `model.tex` or `proofs/`. Prose uses what's already there — don't invent new symbols.

## Cross-references

- Use `\cref{}` and `\Cref{}` for theorem/lemma/section/equation references — never hand-coded "Theorem~\ref{...}" / "Section~\ref{...}".
- Capitalize sentence-leading refs: "\Cref{thm:main} characterizes…"

## Footnotes

- 1–4 per page in body is typical (per STRUCTURE.md observations).
- Each footnote earns its existence by saying something that doesn't fit the main flow.
- Footnotes carry: technical caveats, priority acknowledgments, pointers to extensions, edge cases.
- Footnotes do NOT carry: main arguments, statements of results, citations that belong only in the bibliography.

## Tense and voice

- Present tense throughout.
- First-person plural ("we") — even in single-author papers, this is convention.
- Active voice for results and arguments. Passive only when the agent is irrelevant.

## When in doubt

If the style guide doesn't cover what you need, check [STRUCTURE.md](../STRUCTURE.md). If neither does, read the corresponding section in 3 papers from `references/README.md` and imitate the median.
