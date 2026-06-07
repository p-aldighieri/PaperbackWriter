# STRUCTURE.md — structural spec for econ theory papers

Structural conventions of canonical economic theory papers as observed across the 20-paper corpus in `references/pdfs/`. Runtime reference for writing-role agents (abstract-writer, intro-writer, motivation-writer, related-lit-writer, model-writer, etc.). Describes how the genre is shaped; does not adjudicate content, mathematics, or topic choice.

**Companion:** [WISDOM.md](WISDOM.md) catalogs *what experienced authors say works* (Thomson, Cochrane, Board & Meyer-ter-Vehn, Shapiro, Head, Bellemare, McCloskey, Mankiw). Where STRUCTURE.md is descriptive ("intros are 4–10 pages"), WISDOM.md is prescriptive ("get to your main result by page 15"). Roles read both.

Numbers ("intros are X pages") come from direct observation. When the corpus disagrees with itself, the disagreement is noted with a resolution heuristic.

---

## 1. Paper-level shape

### Length bands

The corpus partitions cleanly into two length regimes:

- **Short-form**, ~8–20 journal pages. Typical of AER P&P-style notes, Theoretical Economics short pieces, and JPE shorts. Examples in this corpus: Roesler–Szentes 2017 (9 pp.), Hart–Reny 2015 (~30 pp. but compact), Lipnowski–Ravid 2020 (~30 pp.).
- **Long-form**, ~35–60 journal pages. Typical of Econometrica flagship and AER feature articles. Examples: Pavan–Segal–Toikka 2014 (53 pp.), Doval–Skreta 2022 (38 pp.), Kamenica–Gentzkow 2011 (26 pp. body, plus heavy appendix), Bergemann–Brooks–Morris 2015 (~37 pp.).

The median paper in this corpus is ~30 journal pages including bibliography, with body (excluding appendix and references) typically 22–35 pp.

### Section ordering — the dominant template

The dominant ordering observed in 17 of 20 papers:

1. Abstract
2. Introduction (numbered Section 1 in Econometrica; unnumbered in some JPE/AER papers)
3. (Sometimes) Related Literature — as a subsection of the introduction or as Section 2
4. Model / Setup / Framework / Environment
5. Main results (one or more sections — definitions, theorems, characterizations)
6. Applications / Extensions / Discussion
7. (Optional) Concluding remarks
8. Appendix (proofs); often Appendix A for proofs of main results, Appendix B for extensions, with an online Supplementary Appendix for omitted material
9. References

### Required vs. optional

- **Required**: abstract, introduction, model section, at least one results section, proof appendix (when proofs are nontrivial and excluded from body), references.
- **Conventional but skippable**: explicit "Related Literature" header (4 of 20 fold lit review entirely into the intro; the remainder split it out as §1.x or §2).
- **Optional**: separate "Discussion", "Applications", "Extensions" sections; a formal "Conclusion".

### Short- vs long-form differences

- **Short-form** papers compress: the intro is 1–2 pages, the "related literature" is footnoted or folded into the intro's last paragraphs, applications are illustrative paragraphs rather than full sections, and the conclusion is either absent or a single paragraph. Roesler–Szentes 2017 has no separate related-lit section and no conclusion — the structure is intro → model → results, finishing on the last theorem.
- **Long-form** papers expand the intro to 4–10 pages, separate the related literature into its own subsection or section, and devote one or more sections to applications/extensions before any conclusion. Pavan–Segal–Toikka's introduction runs ~7 pages including a sub-section "Related Literature".
- The presence of a **roadmap paragraph** ("The rest of the paper is organized as follows...") is near-universal in long-form (observed in Pavan–Segal–Toikka, Doval–Skreta, Cerreia-Vioglio et al., Ely–Frankel–Kamenica) and dispensable in short-form.

---

## 2. Section-by-section spec

### 2.0 Title

- **Purpose.** Name the object, result, or phenomenon in a compact noun phrase — not a sentence, not a method dump. The reader should be able to say it aloud and remember it.
- **Length (corpus-derived, enforced).** Across the 20-paper corpus: median **5–6 words**, mean 5.6, 75% are ≤6 words, 90% ≤8, and **none exceeds 11**. So: **target ≤8 words; hard cap 12.** Count the words (a colon-separated subtitle counts toward the total). Over 12 → cut. The main phrase before any colon should be ≤6–7 words. A 15-word title with two stacked noun phrases is a defect.
- **Subtitle discipline.** Only **3 of 20** titles use a colon subtitle, and each is short and earns it ("Dynamic Mechanism Design: A Myersonian Approach", "Credible Auctions: A Trilemma"). Default to **no subtitle**. Use one only when it adds a genuine qualifier (the method, the twist, the scope) and the total still fits the cap. Never use the colon to glue together two long noun-stacks (e.g. "The X Channel in A B C: Semiparametric (In)efficiency of D Estimation under E Transitions" — that is two titles, not one).
- **Style.** Prefer naming the phenomenon over describing the exercise: "Bayesian Persuasion", "Selling Information", "Suspense and Surprise", "The Limits of Price Discrimination". Avoid "On the …", "A Note on …", "Toward a …". At most one acronym, and only if it is the paper's own coined object; spell out method names ("Temporal-Difference", "Semiparametric") only if they survive the word budget. Drop hedges and qualifiers ("under …", "with …", "in the presence of …") unless load-bearing.
- **Corpus anchors.** Short (the norm): "Robustness and Linear Contracts" (4), "Maximal Revenue with Multiple Goods" (5), "Cheap Talk with Transparent Motives" (5). Longest acceptable: "Bayes Correlated Equilibrium and the Comparison of Information Structures in Games" (11). Nothing longer appears.

### 2.1 Abstract

- **Purpose.** Tell the reader the setting, the question, the main result, and (often) the method, in one paragraph.
- **Length.** **Target ~100 words; hard cap 150.** This is enforced, not advisory: count the words before emitting, and if the draft exceeds 150, cut until it fits (drop the enumerated instance/regime lists and secondary asides first — they belong in the intro/body, not the abstract). Floor ~60. A 200+ word abstract is a defect, not a long abstract.
- **Internal structure.** The recurring sequence is: (1) setting (one sentence — "we study X" / "we consider Y"), (2) substantive assumption or question (one sentence), (3) main result (one to two sentences), (4) secondary result or method note (one sentence, often), (5) optional one-line application or implication. The opener is almost always either "We study…", "We consider…", "We analyze…", "This paper…", or "Consider [a setting]…".
- **Sentence conventions.** Present tense throughout. No citations, no equations, no footnotes (with rare exceptions). No "in this paper" filler at sentence-level; if used, it appears once. JEL codes and keywords follow.
- **Forbidden / weak patterns.** Avoid: hype words ("novel", "groundbreaking", "first to"), motivational throat-clearing ("It is well known that…"), citation strings, parenthetical asides, multi-clause definitions, more than one acronym.
- **Illustrative shape** (paraphrased composite): *"We study [setting with one substantive primitive]. Our main result characterizes [object] in terms of [property]. We use this to [secondary result / application]. The characterization implies [comparative static or corollary]."*

### 2.2 Introduction

- **Purpose.** Motivate the question, state the contribution, sketch the method, position against the literature.
- **Length.** 1.5–3 pages in short-form, 4–10 pages in long-form. The median across the corpus is ~5 pages.
- **Internal sub-structure — the five-move template.** Most introductions execute, in order:
  1. **Hook** (1 paragraph). Real-world motivation, stylized question, or tension in the literature. Long-form opens on motivation more often; short-form opens on a sharp question.
  2. **Model in words** (1–2 paragraphs). Players, primitive, friction. No formal notation. Often a leading example (prosecutor–judge in Kamenica–Gentzkow; think-tank–lawmaker in Lipnowski–Ravid).
  3. **Main result, stated informally** (1–2 paragraphs). Introduced by "Our main result…", "We show that…", "The main theorem…". The explicit contribution sentence falls on average around paragraph 4 (range 3–7).
  4. **Method / intuition / proof sketch** (1–3 paragraphs). Machinery used; geometric or algebraic content of the proof; why the result is non-obvious.
  5. **Related literature + roadmap.** Dedicated subsection (long-form) or 2–3 paragraphs (short-form), followed in long-form by a one-paragraph roadmap.
- **Sentence conventions.** First-person plural ("we"). Present tense. Signposting verbs: *We show / We characterize / We establish / We identify / We provide*. Contribution statement is almost always one cleanly-parsed sentence: "Our main result is that [X]." or "We characterize [X] in terms of [Y]." Footnote density moderate — 3–10 per intro, carrying edge cases, early-citation acknowledgments, caveats, pointers forward.
- **Forbidden / weak patterns.**
  - Don't open with a textbook definition. Open with stakes or a sharp question.
  - Don't delay the contribution past page 2 (short-form) or page 4 (long-form). If the reader can't find the main result by then, the intro is broken.
  - Don't survey the entire literature in prose; reserve breadth for the related-lit subsection.
  - Avoid promissory throat-clearing. The roadmap does this once.
  - Don't load the intro with displays. Most intros carry zero or one. When a display appears, it is illustrative, not load-bearing. A single intro figure (Akbarpour–Li's trilemma triangle, Bergemann–Brooks–Morris's surplus triangle) is acceptable for a geometric paper.

### 2.3 Related literature

- **Purpose.** Locate the contribution precisely against the closest predecessors and adjacent strands.
- **Length.** 0.5–2 pages when broken out as a subsection. 1–3 paragraphs when folded into the intro.
- **Internal structure.** Group by strand, not by paper. Standard pattern: 3–5 paragraphs, each opening with the strand label ("The closest paper to ours is…", "A related literature studies…", "Our paper also contributes to…"). The single closest predecessor is treated separately — usually in the opening paragraph — with an explicit delta ("In contrast to X, we…" or "We build on X by…").
- **Sentence conventions.** `\citet` (textual) when the author/paper is the grammatical subject; `\citep` (parenthetical) when grouped at the end of a clause. The dominant construction is `\citet`-as-subject for the lead paper of each strand.
- **Forbidden / weak patterns.**
  - Don't list papers without a delta. Every cited paper should be there because the reader needs to know how this paper differs from it.
  - Don't editorialize on quality.
  - Don't duplicate lit-review content in footnotes elsewhere in the body.
  - Avoid alphabet-soup paragraphs (eight surname-year tuples in one sentence).

### 2.4 Model / Setup / Environment

- **Purpose.** Define the primitives, players, strategy spaces, solution concept, and notation that the rest of the paper uses.
- **Length.** 1.5–6 pages. Median ~3.
- **Section name.** "Model", "The Model", "Setup", "Environment", "Framework", "Preliminaries", or "A Model of [X]". Choose by subfield: axiomatic decision theory uses "Framework" or "Preliminaries"; mechanism design uses "Environment" or "Model"; information design uses "Model" or "Setup".
- **Internal sub-structure.** Near-universal pattern: (a) "Primitives" or "Setup" subsection naming objects (state space, type space, action space, payoffs); (b) "Timing" or "Strategies" subsection if extensive-form; (c) "Solution concept" or "Equilibrium" subsection. Long-form often adds a "Conventions" or "Notation" subsection up front (topological / measurability). Short-form compresses all of this into one block.
- **Sentence conventions.** Present tense, declarative. Definitions in italics on first mention. Heavy use of "let", "denote", "we write", "we assume", "we say". Each primitive appears with both verbal description and symbol. Footnotes carry technicalities (measurability, tie-breaking, compactness). Footnote density highest of any section — 5–15 per model section in long-form.
- **Forbidden / weak patterns.**
  - Don't introduce notation that is never used.
  - Don't motivate in the model section — motivation belongs in the intro.
  - Don't define the same object twice (verbally then "Formally,…").
  - Don't bury substantive assumptions.
  - No results in the model section. Even a "preliminary lemma" belongs in the results section.

### 2.5 Main results

- **Purpose.** State and prove (or sketch) the central theorems; develop corollaries and their interpretations.
- **Length.** Variable — the bulk of the paper. Typically 30–60% of body length.
- **Internal sub-structure.** Two broad architectures:
  - **Sequential** ("definition → lemma → theorem → corollary → interpretation") — axiomatic decision theory, mechanism design.
  - **Geometric / characterization** ("define feasible set → characterize extreme points → comparative statics") — information design, robust mechanism design.
- **Sentence conventions.**
  - Theorem statements self-contained — readable without re-reading the preceding paragraph; hypotheses explicit.
  - Each major theorem followed by 1–3 paragraphs of interpretation. Theorem-after-theorem runs with no intervening prose are characteristic of weak exposition.
  - Proof location: body for short/load-bearing arguments where the technique is the point; appendix for length or technicality. Long-form default: **sketch in body, full proof in appendix**.
  - Numbering: usually one sequence per paper or per section across Theorem/Proposition/Lemma/Corollary. Definitions sometimes a separate sequence.
- **Forbidden / weak patterns.**
  - Don't state a theorem the reader cannot decode without going back to look up symbols. If symbols are heavy, restate in words first.
  - Don't bury the main theorem inside an "Auxiliary Lemmas" subsection.
  - Don't omit interpretation. Every theorem needs a plain-English "what this says" within a paragraph of it.
  - No uninterpreted display equations mid-section. If a long calculation is needed, defer to a proof.

### 2.6 Discussion / Applications / Extensions

- **Purpose.** Show what the main result enables: a concrete example, benchmark comparison, comparative statics, or relaxed assumption.
- **Length.** 1–8 pages. Optional in short-form; expected in long-form.
- **Internal sub-structure.** Subsection per application. Each application re-states its primitives (which differ from the general model) and then applies the main result.
- **Sentence conventions.** Looser than model/results. Numerical illustrations and figures most common here.
- **Forbidden / weak patterns.**
  - No new application requiring its own model section unless explicitly framed as an extension with primitives flagged "different from the main model".
  - No application that doesn't actually use the main theorem.

### 2.7 Conclusion / Concluding Remarks

- **Contested.** About half the corpus has one; the rest end on the final result, final application, or a one-paragraph close.
- **When present.** ½–2 pages: contribution summary (1 paragraph), interpretation (1–2 paragraphs), open questions or limitations (1–2 paragraphs).
- **Heuristic.** Include if (a) long-form, (b) nontrivial limitations the reader should leave with, or (c) directions others will pursue. Skip in short-form when the final result is itself a satisfying close.
- **Forbidden.** Don't restate the abstract. Don't introduce new results. Don't editorialize about the field's future.

### 2.8 Appendix (proofs)

- **Purpose.** Proofs of theorems/propositions not proved in body; technical lemmas; extensions.
- **Length.** Often comparable to body length in long-form (Pavan–Segal–Toikka and Doval–Skreta appendices run ~20–30 pp.).
- **Internal sub-structure.** Conventional: Appendix A — proofs of main results in body order. Appendix B — extensions / auxiliary results. Online / Supplementary — omitted material, generalizations, alternative proofs.
- **Sentence conventions.** Proofs titled "Proof of Theorem N". End markers: `Q.E.D.`, `■`, `□` (journal-dependent). Internal lemmas numbered "Lemma A.1" etc.
- **Forbidden / weak patterns.**
  - No forward references from body to proof step without first anchoring what that step is about.
  - No new notation in the appendix unless defined at the head of the appendix.

---

## 3. Cross-cutting conventions

**Citations.** `\citet` (textual) when the author/paper is grammatical subject or object. `\citep` (parenthetical) for end-of-clause grouping or lists. Rarely more than 3 parenthetical citations per sentence; larger lists go in a footnote. First mention of a foundational paper in a strand uses `\citet`; later mentions in the same paragraph may shorten.

**Notation hygiene.** Each symbol introduced before first use, italicized on introduction. Greek letters dominate for primitives (states, types, beliefs, signals); calligraphic for sets; capital Roman for distributions or function spaces; lowercase Roman for elements. Avoid colliding letters across sections (a `p` that is price in §2 should not become probability in §4). Vector convention is journal-split: Econometrica papers tend to use subscripts; AER tends to use unbolded letters with the dimension named in prose.

**Theorem environments.** Standard: Theorem, Proposition, Lemma, Corollary, Claim, Definition, Assumption, Remark, Example. Reserve Theorem for central results; Proposition for substantial but not headline results; Lemma for technical building blocks. Calling everything "Theorem" weakens the signal. Numbering: one continuous sequence per paper is modal; some papers use per-section numbering (Theorem 2.1).

**Footnotes.** 1–4 per page in the body is typical; model section higher, appendix lower. Footnotes carry technical caveats, priority acknowledgments, pointers to extensions, alternative interpretations, edge cases. They do *not* carry main arguments, statements of results, or citations that belong only in the bibliography.

**Displays vs. inline math.** Display math for: equations referenced later, equations that are the visual object of an argument, equations longer than ~½ a text line. Inline math for short expressions, defined terms, references to existing displays. Number displays only when referenced.

**Where proofs go.** Body if the proof is short (<~½ page) and the technique is part of the contribution. Appendix if long, technical, or routine. Sketch-in-body + full-proof-in-appendix is the long-form default for the central theorem.

---

## 4. Subfield deltas

Conventions above are corpus-wide. Where subfields meaningfully diverge:

**Information design / Bayesian persuasion.** Model sections often skip an explicit "timing" subsection (sender-receiver order is universal). Geometric characterizations make figures more common in the body. Related-literature sections are short — the field is concentrated, standard predecessors are well known.

**Mechanism design (static and dynamic).** Heavy model section: separate "Environment", "Mechanisms", "Solution concept" subsections standard. Notation density highest of any subfield. Revelation-principle-style results often serve as Theorem 1, re-defining the object of design before any optimality result. Dynamic papers (Pavan–Segal–Toikka, Halac–Yared, Doval–Skreta) carry additional "Histories", "Strategies", "Belief system" subsections.

**Decision theory / axiomatic.** Model called "Framework" or "Preliminaries". Axioms numbered (Axiom 1, Axiom 2, …) and stated as standalone propositions in italics. Headline result is a representation theorem of the form "preferences satisfy axioms A1–An if and only if there exists a [functional form] representing them" — anchors the paper. Discussion section is heavier (comparative statics on representation parameters, comparison to existing models, experimental evidence). Footnote density higher.

**Game theory / cheap talk / equilibrium characterization.** Solution concept (PBE, sequential, sender-preferred) is explicit and prominent. Main result is often an equilibrium characterization or an equivalence between solution concepts, rather than an optimal-design statement. Examples are heavier — the leading example often runs through the paper.

**Robust / worst-case theory.** Model spells out the principal's information explicitly (different from standard Bayesian). Often a "Principal's knowledge" subsection. Contribution sentence often takes the form "the optimal contract/mechanism is [linear / cutoff / separable]" — a structural rather than parametric result.

---

## 5. What this spec is NOT for

- Not a guide to mathematical correctness — describes how proofs are presented, not whether they are right.
- Not a topic-ideation tool.
- Not a substitute for reading the source papers. When stuck on a section, open the relevant exemplars in `references/pdfs/` and read the analogous section.
- Not a prose style guide (sentence rhythm, idiom, authorial voice).
- Not a journal-formatting reference (margins, bibliography style, LaTeX class).
- Not a citation-policy adjudicator — whether a literature should be cited is a content judgment.

---

## 6. What I didn't get to

- **Bibliography style.** Journal-specific reference formats (Econometrica, AER, TE, JPE) not encoded.
- **Figure / table conventions.** Observed where figures appear (intro, applications) but did not document caption norms, axis labeling, or visual-design choices. The corpus is figure-light (most papers carry 0–3 figures).
- **Online vs. in-paper appendix split.** Boundary varies by paper and journal; not all corpus papers were checked for supplementary materials.
- **Acknowledgment footnote** (the unnumbered title-page footnote). Universally present, but content conventions — coauthor disclaimers, funding, seminar lists — not catalogued.
- **Proof-prose conventions.** Sentence-level signposting within proofs ("we show" vs. "note that" vs. "observe that") would need a dedicated pass for a proof-writing role.
- **Reputation / repeated games and pure cheap-talk.** Flagged as gaps in the corpus itself; the "game theory" subfield delta is correspondingly thin.
- **Quantitative contribution-paragraph position.** The "paragraph 3–7" range in §2.2 is approximate. A precise pass would count paragraphs per intro across all 20 papers and report a distribution.
- **Conclusion conventions.** The "about half" claim in §2.7 rests on a subset of papers (Carroll 2015, Lipnowski–Ravid 2020, Cerreia-Vioglio et al. 2015). A full closing-page pass would tighten it.
