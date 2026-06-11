# WISDOM.md — distilled advice from experienced authors on writing econ theory papers

Companion to `STRUCTURE.md`. Where STRUCTURE.md catalogs *what theory papers look like* (empirically, across the 20-paper corpus), this document catalogs *what experienced authors say works*. Sources are economists who have written, edited, refereed, or taught the craft: Thomson, Cochrane, Board & Meyer-ter-Vehn, Shapiro, Head, Bellemare, McCloskey, Mankiw, Varian.

Organized around the writer's decisions, not around sources. Short quotes (<15 words) are flagged; everything else is paraphrase. URLs are at the bottom.

---

## 1. How to start the introduction

**Do not "clear your throat."** Cochrane's term for the first-paragraph throat-clearing that wastes space: "Financial economists have long wondered…" or "A large literature has studied…" Cochrane's rule: start with your central contribution, not with philosophy, not with the field's history, not with policy importance (Cochrane, writing tips). Mankiw echoes: cut the qualifiers and obvious modifiers, especially "of course," "clearly," "obviously" (Mankiw, How to Write Well).

Theory-specific carve-out from Board & Meyer-ter-Vehn: the first 1–2 paragraphs *can* be "broad motivation" — but motivation either by an application ("Why does inequality rise after recessions?") or by the literature ("Coase's conjecture states that…"). Either is acceptable; what they share is that *the reader sees a concrete question by the end of paragraph 2*, not a survey of the field.

Bellemare and Head warn explicitly against the "bait and switch": promising one topic in the hook and delivering another (Head, Introduction Formula; Bellemare, How to Write Applied Papers). And against the "all my friends are doing it" opening — motivating a paper only by the fact that others have written on the topic (Head).

A practical opening test from Thomson: by leafing through your article, can a reader spot the main results and crucial definitions? If not, the front matter is doing too little work (Thomson, Young Person's Guide).

## 2. The contribution statement

The most consistent advice across all sources: **make the contribution explicit, early, and concrete.**

- Cochrane: figure out the *one* central contribution and write it in a single paragraph. The paragraph must contain the actual fact, not a placeholder. Not "we find pecking-order theory is rejected" but the specific coefficient, mechanism, or theorem (Cochrane).
- Board & Meyer-ter-Vehn: literally write the line "The contribution of this paper is…" to force yourself to be explicit. Their canonical intro reserves paragraphs 3–4 (after motivation) for this; expand to two paragraphs only if the model *and* the result are both novel (Board & Meyer-ter-Vehn).
- For theory, they enumerate six possible *forms* of contribution, and a strong intro tells the reader which one(s) apply: (1) the paper asks a new question; (2) posits a new model; (3) speaks to an important application; (4) identifies a new economic force; (5) generates new empirical predictions; (6) makes a technical contribution. Different readers weight these differently — abstract theorists value (2) and (6); applied readers value (3) and (5) — so the intro must signal which boxes you're claiming (Board & Meyer-ter-Vehn).
- Shapiro reframes this as a contract: by the end of the intro, you have promised the reader something specific, and the body must deliver on that promise. He recommends drafting an "aspirational introduction" *before* the paper exists, then asking "if I write this paper, will I be happy with it?" (Shapiro, Four Steps).

**Where in the intro.** Head's formula places the question in paragraph 2–3, then antecedents, then ~3 specific value-added points. Board & Meyer-ter-Vehn place the contribution in paragraphs 3–4 (after a 1–2 paragraph motivation), then the model sketch (1–2 paragraphs), then results (1–2 pages), then related work (1–2 pages). For theory, the *model sketch* and the *contribution* are intertwined enough that they often share these paragraphs.

**Form.** The contribution paragraph should be self-contained — it cannot assume the reader knows your model yet (Board & Meyer-ter-Vehn). And: never criticize others' work explicitly; instead of "Arrow–Debreu ignored market power," write "we develop Arrow–Debreu's canonical model to include market power" (Board & Meyer-ter-Vehn). Cochrane: "you do not have to say that everyone else did it all wrong."

## 3. Length budgeting

Numbers from the advice literature (the corpus observations are in STRUCTURE.md):

- **Introduction.** Cochrane: three pages is a good upper limit. Board & Meyer-ter-Vehn: 1–2 paras motivation, 1–2 paras contribution, 1–2 paras model, 1–2 *pages* results, 1–2 *pages* related work — so an upper bound of ~5 pages of intro, with results description occupying the bulk. Shapiro's 15-paragraph template is ~4 pages.
- **Body.** Board & Meyer-ter-Vehn: "get to your main result by page 15." Readers drop off with every page (Board & Meyer-ter-Vehn).
- **Whole paper.** Cochrane: no more than 40 pages final. Thomson: refuses to give a number — "as long as it needs to be, no longer, and no shorter" — but adds that *length itself is not a problem if structure is clear* (Thomson). Implication: a 50-page theory paper can succeed if the layered structure (intro → key result by p.15 → extensions → appendix) lets the reader stop reading when they have what they need.
- **Footnotes.** Board & Meyer-ter-Vehn: fewer footnotes than pages. Cochrane: footnotes are only for things the typical reader can skip but a few might want. If it's important, put it in the text; if it's not, delete it (Cochrane).

## 4. Proof exposition — body vs. appendix

This is the highest-stakes judgement in a theory paper, and the named sources disagree productively. Distill the disagreement before applying it.

**The two camps.**

- **Thomson is body-first.** He "does not generally favor relegating proofs to appendices" and finds it "annoying to have to go back and forth between the body of the paper and the appendix" when reading. If a proof is short and informative, keep it where the reader meets the result (Thomson, Young Person's Guide).
- **Board & Meyer-ter-Vehn are pragmatic.** Their rule: if the proof is *interesting or short*, include it in the main text; if it is *standard and boring*, put it in the appendix; if the proof is *key for the paper* but long, put a heuristic version in the body before the theorem and the full proof in the appendix (Board & Meyer-ter-Vehn).

**Synthesis for the decision.** A proof belongs in the body when it satisfies *any* of:
1. It is short (a few lines to half a page).
2. It contains the paper's central economic argument — the proof *is* the contribution, not a technical confirmation of it.
3. The technique is novel or load-bearing for understanding later results.
4. The intuition is most cleanly delivered by the proof itself (e.g., a one-paragraph revealed-preference argument).

A proof belongs in the appendix when:
1. It is long and technical without delivering economic insight.
2. It is a standard exercise (compactness, continuity, fixed-point invocations) where the reader can verify by inspection that the standard machinery applies.
3. It is repetitive — a near-copy of an earlier proof modulo notation. Board & Meyer-ter-Vehn flag "heavy notation" and "repetitive" cases as appendix material.

**The hybrid move.** When the proof is both load-bearing and long: state a *heuristic version* in the body before the theorem (or right after), and put the rigorous proof in the appendix. Board & Meyer-ter-Vehn: by putting something in the main text, "you nudge readers to read it" — most readers skip appendix-only proofs. Thomson endorses placing informal explanation *before* the formal statement so it prepares the reader, never *inside* the formal proof.

**Appendix discipline.** Board & Meyer-ter-Vehn: the appendix should still fit the paper's narrative — "not a dumping ground." Cochrane is more lenient: the appendix is a great way to satisfy referees who want robustness checks without consuming body space. For theory, follow Board & Meyer-ter-Vehn's stricter line.

## 5. Proof verbosity — the "obvious" / "clearly" trap

Thomson's warning: after completing the paper, search for "clearlys" and "obviouslys" and check that what you called clear is, "if not clear and obvious, at least true" (Thomson, footnote 21). Errors hide in the steps the author is overconfident about, not the steps that look hard. Cochrane: "'It is easy to show that' means that it isn't." Mankiw lists "of course," "clearly," and "obviously" for deletion.

Concrete rules for proof density:

- **Math/English ratio.** Thomson's tongue-in-cheek "interval (52%, 63.5%)" points at a real consensus: a proof of pure math is unreadable, a proof of pure English imprecise. Aim for proofs where each algebraic step is preceded or followed by a one-sentence English claim about what just happened.
- **Don't leave too many steps to the reader.** Even "standard" steps deserve a sentence naming the theorem invoked (Thomson).
- **Be specific about which assumption is doing the work.** Not "the above assumptions imply…" but "Assumption 3 and part (ii) of Assumption 4 imply…" (Thomson). The discipline catches bugs.
- **Divide long proofs into named units.** Step 1, Claim 1a, Subcase 1b, each with a one-line title (Thomson). In the body, this is what makes the proof survivable; in the appendix, what makes referee verification possible.
- **Parallel format for parallel theorems.** If Theorem 2 differs from Theorem 1 only in C → C′, state it in the same template so the difference is visible at a glance (Thomson).

**Notation hygiene that affects proof readability.** Best notation is "notation that can be guessed" (Thomson) — X for sets, p for prices, t for time. Don't introduce a symbol used only once or twice. Mnemonic abbreviations for assumptions ("Mon", "Cont", "Diff"), never "A1, B3" (Thomson). Eliminate all but essential notation (Board & Meyer-ter-Vehn). Theorems should be English sentences that happen to be mathematically true; their compact template: "Define p. Define q. Theorem: Every p is q."

## 6. Related literature — what to include, what to leave out

The advice here is unusually unanimous.

- **Not at the front of the intro.** Cochrane: do not start the intro with a page and a half of others' work; readers can't evaluate your difference from a literature they haven't seen until they understand your paper first. After your contribution is clear, then a brief literature review — separate section or set off so readers can skip it.
- **5–10 closest studies, not more.** Bellemare: relate to the five-to-ten closest studies, "the closer to five, the better." Cochrane: set your paper off against "the 2 or 3 closest current papers" and give priority credit where due.
- **Tell a story, don't list.** Thomson: give priority to the development of ideas, not to "who did what." Bellemare: nobody wants a bland enumeration ("Johnson found this. Wang found that."). The intellectual history of the topic should be tellable.
- **Be generous in citation but not strategic.** Cochrane: be generous, but the final version should not be padded with citations to potential referees.
- **Master's-thesis-style separate "Literature Review" sections are unnecessary for journal papers.** Bellemare: almost always unwarranted. The mini-review inside the intro plus citations in context suffices. (STRUCTURE.md confirms: 4 of 20 papers in the corpus fold lit review entirely into the intro.)
- **Background sections are different.** If the paper requires institutional detail (a specific market, legislation, mechanism in the wild), a separate background section is appropriate. This is the exception that proves the rule (Bellemare).

For theory specifically: Board & Meyer-ter-Vehn want the literature paragraph to *elaborate on your contribution*, not to survey. The point of citing X is to say "X did A, we add B, here's why B matters." If a citation doesn't fit that template, ask whether it belongs in the bibliography but not the body.

## 7. What reviewers and editors complain about

Aggregated from Board & Meyer-ter-Vehn (who referee theory papers), Bellemare (editor), Thomson, and Cochrane.

Concrete failure modes that get papers desk-rejected or trigger reject decisions:

1. **The contribution is unclear.** The reader finishes the intro and can't say what's new. Most consequential failure (Board & Meyer-ter-Vehn; Cochrane; Bellemare).
2. **Bait and switch.** The intro promises X; the body delivers Y. Bellemare: this alone is enough to recommend rejection.
3. **Typos and loose statements.** Board & Meyer-ter-Vehn: when an author is junior, readers update fast on ability; typos and ill-formed conjectures cause readers to question everything. Conjectures must be flagged as conjectures.
4. **The model "changes" mid-paper.** A new variable, a new assumption, slipped in just before a theorem. Board & Meyer-ter-Vehn: "one paper, one model." Either parameterize the variations or use a clean extension section. Don't shift the object of analysis silently.
5. **Theorems whose statement is impossible to parse without scrolling.** Thomson: theorems should be self-contained, no fresh notation introduced inside the statement.
6. **Long-winded assumption defenses in the intro.** Board & Meyer-ter-Vehn: be defensive about a non-standard assumption in one sentence, not five paragraphs.
7. **Discussion of extensions before the model is clear.** Same source: the reader barely understands the baseline; details of extensions are wasted.
8. **Repeating the same point in the abstract, intro paragraph 3, and lit review.** Board & Meyer-ter-Vehn list this explicitly. Cochrane: "if you've said it once, you don't have to say it again."
9. **Stranded hypotheses.** Thomson: after QED, check if any hypothesis was not used. Either it's a hidden bug, or your result is stronger than you stated.
10. **Passive voice avoidance theater.** Cochrane and Mankiw converge: passive voice signals the author dodging responsibility for the claim.
11. **Footnotes that contain content the reader needs.** Thomson and Cochrane agree: never define important notation in a footnote you then reference in the body — readers skip footnotes.
12. **Roadmap paragraphs that say nothing.** Head: avoid "Section 2 is the middle of the paper." Tailor or omit. (Cochrane omits routinely; the corpus is mixed.)

Two meta-failures named directly by editors:

- **No clear answer to "Why should I care?"** (Board & Meyer-ter-Vehn open with this question).
- **Sentence-by-sentence imprecision.** Cochrane: "read each sentence carefully. Does each sentence say something, and does it mean what it says?"

## 8. Lessons unique to theory papers

Pulled from Thomson and Board & Meyer-ter-Vehn — the sources most concentrated on theory craft.

**The model is the contribution as much as the theorem is.** Board & Meyer-ter-Vehn: "the heart of a theory paper are its model and its theorems." The model section is not setup — it is *how you want the reader to think about the problem*. If it takes four pages to state, you have not simplified anything.

**One paper, one model.** Changing the model over the course of the paper is the most common source of confusion. Parameterize variations or treat them as comparative statics. Avoid the pattern of "an overly general model in which one can prove little of interest, and then introduce crucial assumptions just before the theorem" (Board & Meyer-ter-Vehn).

**Build down from the canonical four questions.** For game-theoretic / mechanism-design models: who are the players, what can they do, what do they know, what are their preferences. State these succinctly and in this order; do not intersperse with interpretation (Board & Meyer-ter-Vehn).

**Define concepts in their full generality, then specialize.** A Walrasian equilibrium is a Walrasian equilibrium without convexity; convexity enters when you discuss existence. Mixing the concept's definition with the assumptions needed for your result is a category error (Thomson).

**Reproduce the discovery process.** Thomson: get to the main theorem in small steps — first work it out for two agents, two goods, then generalize. The reader needs to see the simple case to grasp the central ideas; the details of the general proof are not what makes the paper useful to her own work.

**Separate the formal model from its interpretation.** Thomson: write the formal definition (e.g., a coalitional-game solution) cleanly, then explain "Fi(v) can be interpreted as the value to player i…" The separation lets readers in different applied subfields each find their own use for your result.

**Be careful with informal vs. formal exposition.** Board & Meyer-ter-Vehn: be consistent — if you explain a result using intuition, use intuition throughout, don't switch every other result. Thomson: informal explanation should come *before* the formal statement, never inside it. And: never write "We have therefore proved the following theorem" after a stretch of mixed prose-and-algebra; this "mugs" the reader.

**Best results say what *must* happen, not what *may* happen.** Board & Meyer-ter-Vehn: existence-of-bad-equilibrium results are weaker than impossibility results; possibility theorems are weaker than uniqueness. Only "may happen" results that are *very* surprising get a pass.

**Define independently of utility representation when you can.** Thomson: if your theory is about preferences, write "S(R) R_i S(R_{-i}, R'_i)" rather than dressing everything in utility functions you don't need. This isn't aesthetic — utility notation in normative/welfare contexts misleads readers into thinking the theory permits interpersonal comparisons.

**Laundry-list theorems are weak.** Board & Meyer-ter-Vehn: do not state every implication that falls out of the setting. Pick two or three; ask which the reader should *remember* if they had to. Thomson: if you have ten theorems, force-rank the top three.

**Numerical examples are not always useful.** Thomson: numerical examples often obscure the structure (you lose units, you confuse 9 with x₁+x₂, you can't tell pre- from post-shock income). Algebraic examples with two agents and two goods usually beat numerical ones. Use numerics only when the operations are simple and the numbers stay distinct after the operations.

**Pictures and Venn diagrams pay outsized returns.** Thomson: a labeled diagram in a proof can halve the time to understanding. Venn diagrams of assumption relations let the reader see at a glance whether your weakening is "much weaker" or "barely weaker" than prior work.

## 9. Subfield notes

Material on subfield-specific writing conventions is thinner online than general advice. What surfaced:

- **Mechanism / information design.** Board & Meyer-ter-Vehn's canonical "asks a new question" example is Kamenica–Gentzkow (2011) — the shift from "does signal X help the sender?" to "what is the best signal?" For an information-design paper, position the contribution at the level of the design problem, not the answer.
- **Axiomatic theory / social choice.** Thomson writes from inside this tradition. Subfield-specific advice: name axioms mnemonically ("Mon", "Cont"), not "A1, A2"; order assumptions by decreasing plausibility; challenge dominant terminology when inadequate (he prefers "contraction independence" to Nash's "independence of irrelevant alternatives").
- **Contract theory / dynamic models.** Board & Meyer-ter-Vehn cite Sannikov (2008) as the canonical "new model" contribution — the value was tractability of a different framework. If your contribution is methodological, the intro should foreground what the new framework lets you do that the old one couldn't.
- **Game theory.** Board & Meyer-ter-Vehn cite Sugaya (2014) for "technical contribution": long-standing problem, new proof technique. The intro then carries unusual weight on the *prior literature's struggle* — without it, the technique doesn't read as a contribution.

For decision theory, behavioral, matching, auctions, and macro theory, the named-source advice base is thin. Subfield norms are mostly transmitted through reading recent published papers (which is what STRUCTURE.md operationalizes).

## 10. The meta-rules

Five rules that recur across every source:

1. **Write to be skimmed.** Newspaper / triangular style — main point first, then context, then qualifications (Cochrane). Theorem display, mnemonic notation, named subsections (Thomson). Most readers will read the abstract, the intro, glance at theorem statements, and stop.
2. **Revise heavily.** Thomson: "good writing requires revising, revising, and revising again." Bellemare: he revisits the intro a few hundred times per paper. Shapiro's four-step process is iteration-by-design.
3. **Brevity.** McCloskey's first rule is to omit needless words; Cochrane echoes; Mankiw lists "very," "in order to," "it should be noted that" for deletion. Theorems should be the shortest English sentences that are still mathematically true.
4. **Take responsibility for your claims.** Cochrane's diagnosis: passive voice, "it should be noted," and front-loaded literature reviews are all evasions. Active voice, "I" or "we," and direct claims are not stylistic preferences — they are the visible sign that the author is willing to be wrong on the record.
5. **Imagine a specific reader.** McCloskey: pick someone with high standards and write to them. Shapiro: write for a robot — linear, plain, formal, unimpressed by fancy talk. Bellemare: an audience of PhD economists outside your subfield. The constraint forces precision.

## 11. Scanning as economic theory — field notes from expert reads of generated drafts

Provenance differs from the rest of this document: not the advice literature, but the post-mortem of an expert theorist's read of two pipeline-generated drafts (June 2026), which "did not scan as economic theory papers." These are the failure modes specific to papers whose math arrives pre-baked from a proving pipeline, and they are detectable within one page — before any proof is checked.

**The contract.** An economic theory paper runs *question → minimal model → insight*: an economic question stated first, a model presented as the minimal vehicle for that question, theorems that answer it in economic terms. A math or CS paper runs *result → certificate → robustness*. Drafts whose math was produced first default to the second shape, and a theorist pattern-matches the shape instantly. Rewording cannot fix this; the paper's spine must be rebuilt around the question — or, if no economic question exists, that fact must be escalated to the author, not papered over.

**The scan test (run before anything ships).** Hand the abstract, intro P1–P3, and the headline theorem statement to an imagined theorist for 90 seconds. They must be able to answer: (i) what economic question does the paper ask; (ii) what is the answer, in one English sentence with no symbols; (iii) which contribution type from §2's six-item list is being claimed. Any unavailable answer means the draft does not scan as economics.

**The main result must exist as an economics sentence.** Somewhere before its formal statement, the headline result must appear as one sentence a PhD economist outside the subfield could repeat at lunch — e.g., "receiver control reshapes the value of persuasion but never the form of the optimal experiment." If no such sentence can be written, the result has not yet been understood as economics. That is a framing debt owed by the author, not a prose gap a writer can fill.

**Use case ≠ question.** Bolting an application (credit ratings, loan rollovers) onto a math-shaped result is the generated-paper version of Bellemare's bait-and-switch (§1, §7), and it is detected as fast. The swap test: could a different application replace this one with zero changes to the assumptions, the theorems, or the abstract's claims? If yes, the application is a costume — either cut it or rebuild the model so the application disciplines at least one assumption, one comparative static, or one interpretation the abstract actually uses.

**Assumptions are standard or defended — once, in place.** Every non-standard assumption gets one sentence of defense where it is introduced (§7, item 6) — not five paragraphs, not zero, and never a trailing "honest scope" / "knife-edge cases" inventory. A collected caveats dump tells the referee the model was built backwards from the theorem. If an assumption exists only to make the proof go through and has no economic defense, that is information for the *author* about the model; prose cannot absorb it.

**Benchmark honesty.** When a headline comparison is partially true by construction — e.g., the favored institution in the model gets free access to information the rival must pay to acquire — the paper must say so itself and relocate the claimed contribution to the non-trivial side (the converse bound, the characterization, the conceptual identification). A referee who discovers a rigged benchmark on their own rejects the paper; a paper that points it out first keeps the referee's trust.

**Title and abstract carry zero machinery.** No internal mechanism nouns (decoders, certificates, labels, wedges, kernels-as-objects), no math symbols, no numerical constants. A numerical threshold in an abstract ("γ̄ ≈ 0.8582") is an instant tell that no economist framed the result. The abstract states the question and the answer in words; the machinery is named for the first time in the model section.

**Upstream pipeline verdicts are not evidence.** Self-grades attached to the incoming math ("ECMA-ready", "credible top-5", "gauntlet PASS 9/9") are produced by the same class of system that produced the proofs. They must never shape venue claims, adjectives, or confidence in the prose. Treat the math as given and every assessment of its importance as unestablished until the human author says otherwise.

---

## Sources

- John H. Cochrane, "Writing Tips for Ph.D. Students" (2005). General craft, structural advice, sentence-level rules. Empirical-leaning but the structural and sentence-level rules transfer cleanly to theory. <https://economics.rice.edu/sites/g/files/bxs4046/files/inline-files/Cochrane%202005%20Writing%20Tips.pdf>
- Simon Board and Moritz Meyer-ter-Vehn, "Writing Economic Theory Papers" (2018, UCLA). The single most important source for this document — written by theorists, for theorists, with explicit body-vs-appendix rules, a canonical intro template, and an enumeration of contribution types. <http://www.econ.ucla.edu/sboard/teaching/WritingEconomicTheory.pdf>
- William Thomson, "The Young Person's Guide to Writing Economic Theory" (JEL, 1999). The comprehensive theory-craft reference: notation, definitions, proof structure, assumption ordering, figures, theorem statement. <https://econ.duke.edu/sites/econ.duke.edu/files/documents/Thomson,%20William%20-%20Guide%20to%20Writing%20Economic%20Theory_0.pdf>
- Keith Head, "The Introduction Formula" (UBC). The five-component intro template (Hook, Question, Antecedents, Value-Added, Roadmap) that has become standard advice across applied economics; useful for theory papers too, with the caveat that the "Question" often is a modeling question rather than an empirical one. <https://keithjakee.com/wp-content/uploads/2015/06/The-Introduction-Formula.pdf>
- Jesse Shapiro, "Four Steps to an Applied Micro Paper" (2022). The aspirational-introduction-as-compass technique, and the "write for a robot" body-drafting discipline. <https://shapiro.scholars.harvard.edu/file_url/103> (also <https://www.gabornyeki.com/files/shapiro_four_steps.pdf>)
- Marc Bellemare, "How to Write Applied Papers in Economics" (2020). Editor's-eye view; the bait-and-switch failure mode; the 5-to-10 closest-studies rule; the case against separate literature-review sections in journal papers. <https://marcfbellemare.com/wordpress/wp-content/uploads/2020/09/BellemareHowToPaperSeptember2020.pdf>
- Marc Bellemare, "The Conclusion Formula" (blog post). Four-part conclusion template (summary, limitations, policy implications, future research). <https://marcfbellemare.com/wordpress/12060>
- Tim Taylor, "Writing the Intro to Your Economics Research Paper" (Conversable Economist, 2020). Useful synthesis of Head, Sahm, and applied-econ intro conventions. <https://conversableeconomist.com/2020/02/17/writing-the-intro-to-your-economics-research-paper/>
- Greg Mankiw, "How to Write Well" (2006, blog). The numbered cuts: passive voice, jargon, custom acronyms, "very," etc. <https://gregmankiw.blogspot.com/2006/10/how-to-write-well.html>
- Deirdre McCloskey, *Economical Writing*. Reachable secondary summaries: <https://press.uchicago.edu/ucp/books/book/chicago/E/bo25674588.html>. Brevity, specificity, active voice, the imagined reader.
- Hal Varian, "How to Build an Economic Model in Your Spare Time" (cited by Board & Meyer-ter-Vehn as the personal-approach counterpoint to their "how-to" guide). Not directly fetched here.
- Karl Whelan, "Writing Tips for PhD Theses" (UCD). Mentioned in searches; not directly cited above. <https://www.karlwhelan.com/Teaching/PhD/phd-writing-talk.pdf>
- *Theoretical Economics*, "Guidelines for Referees" (Econometric Society). Surfaced but not directly accessible during research; provides the journal's own framing of what referees evaluate. <https://www.econometricsociety.org/publications/theoretical-economics/policies/guidelines-for-referees>

## What I couldn't find

Honest gaps:

- **Direct editor commentary from Econometrica, AER, JPE, or TE editors** specifically on theory-paper craft. Berk–Harvey–Hirshleifer (JEP 2017) aggregates editor wisdom on referee mistakes for theoretical papers — the searches surfaced a list (inappropriate topic descriptions; improper use of theoretical constructs; loose logical arguments; incorrectly stated conclusions; inaccurately described contributions) but the PDF wouldn't render, so the list couldn't be expanded with direct quotation.
- **Subfield-specific written craft guides** for information design, decision theory, contract theory, behavioral theory, matching/market design. These traditions transmit conventions orally and by example.
- **Twitter/X threads from prominent theorists.** Useful in principle but unstable to access systematically.
- **Don Davis and Plamen Nikolov.** Both exist (Nikolov on SSRN/IZA); their advice is largely co-extensive with Cochrane and Bellemare on the empirical side, nothing distinctively theory-flavored beyond what's already covered.
- **Hamermesh on economic writing.** Has written about economics as a discipline (publication patterns, age distributions) but no dedicated writing-craft guide surfaced.
- **Tirole, Fudenberg, Levin, Athey, Bresnahan on theory writing.** Names surface; public writing advice is sparse or concentrated on graduate-school logistics.

The triangulation across Cochrane, Board & Meyer-ter-Vehn, Thomson, Shapiro, Head, Bellemare, and McCloskey is dense enough that further sources would mostly restate. The genuine gap is subfield-specific craft — exactly what STRUCTURE.md's corpus-grounded observations are designed to backfill.
