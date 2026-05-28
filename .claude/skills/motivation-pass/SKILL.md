---
name: motivation-pass
description: |
  Tighten the "why does this matter" thread running through abstract + intro P1-P2. Targets
  motivation density, not prose polish. Use after the first intro draft if motivation is weak.
---

# motivation-pass

## When to invoke

- User says "the intro doesn't sell it", "motivation is weak", "why-does-this-matter pass".
- After the first intro-writer draft if the gatekeeper flagged motivation issues.
- Before any external Codex/Opus pass on the intro — clean the motivation first.

## What this skill does

1. Spawn the `motivation-writer` agent with:
   - `STRUCTURE.md`
   - `<target>/brief.md` (especially the "who should care" + "what's open" pieces)
   - Current `abstract.tex` + `intro.tex`

2. The agent emits a diff. It rewrites **only** abstract framing sentences and intro P1-P2. It does **not** touch P3+ (the contribution / methodology / roadmap paragraphs) or any formal content.

3. Apply the diff. Then run the `gatekeeper` skill.

## What "motivation density" means

A motivation paragraph passes if:
- It names a phenomenon, question, or open problem **a non-specialist can recognize**.
- It does not list known results before stating why we should care.
- Every sentence either escalates the puzzle or closes it.
- It does not contain the words "interesting", "important", "novel".

## Hard rules

- Does **not** change formal statements (they live in `proofs/`).
- Does **not** introduce new citations.
- Does **not** add jokes, metaphors, or "imagine you are…" framings unless `brief.md` explicitly invites one.
