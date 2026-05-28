---
name: related-literature
description: |
  Draft or revise the Related Literature section. Uses a verified citation universe
  (`refs.bib` + `brief.md` anchors + `references/pdfs/`). **Never invents citations.** Marks
  unresolved claims with `[CITATION NEEDED]`. Use when the user says "write the related lit",
  "do a lit review pass", or after the main results are stable.
---

# related-literature

## Why this skill is locked down

Pure-LLM related-work generation is the highest-risk failure mode in academic LLM pipelines — citation fabrication runs ~66% in unguarded pipelines. This skill is designed to fail closed.

## Invocation

User says: "write the related lit", "do a lit review pass", "draft section §X".

## Preconditions

1. `<target>/brief.md` lists ≥ 3 comparison anchors.
2. `<target>/tex/refs.bib` exists and contains at least those anchors.
3. `<target>/tex/sections/results.tex` is non-trivially populated.

## What this skill does

1. **Build the citation universe** — the only citations the agent may use:
   - Entries in `<target>/tex/refs.bib`.
   - Citation keys explicitly named in `brief.md`.
   - Papers physically present in `references/pdfs/`.

2. **Spawn the `related-lit-writer` agent.** Pass it: STRUCTURE.md, `brief.md`, the results section, and the citation universe.

3. **Verify every `\cite{}` key** in the agent's output exists in `refs.bib`. If not, replace with `[CITATION NEEDED: <what the agent thought it was citing>]`.

4. Write to `<target>/tex/sections/related.tex`.

5. Run the `gatekeeper` skill.

## What to do with `[CITATION NEEDED]` markers

Surface every one to the user with the agent's intended claim. The user resolves them — by adding to `refs.bib`, rewording, or deleting the claim.

## Codex / Opus pass

If the user wants to delegate a Codex or Opus pass on this section, prep a focused prompt in `<target>/notes/related-lit-prompt.md` containing the current draft + the citation universe + the hard rule "no citations outside the supplied universe."

## What this skill does NOT do

- Does not search the web for new papers.
- Does not rank or quantify cited papers.
- Does not write the contribution sentence — that's the intro's job.
