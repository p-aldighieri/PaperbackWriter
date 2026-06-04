---
name: citation-check
description: |
  Verify EVERY entry in a paper's `refs.bib` against Crossref's canonical record. Catches
  wrong DOIs, years, volumes, issues, pages, venues, and author lists; flags missing DOIs
  with the record to add; and detects when a "working paper" now has a published version.
  **Report-only — never edits the .bib.** **Does not check math or prose.** Use before any
  "final" compile / submission, or whenever the user says "check the citations", "verify the
  bib", "crossref the references", "are the citations right".
---

# citation-check

## Why this exists

A citation that looks right can be wrong in a way no compiler catches — a transposed
volume, an off-by-one year, a page range from the working-paper version, a DOI that points
at a different paper. These slip past the `gatekeeper` (which only checks that `\cite{}`
keys *exist* in `refs.bib`) and past `latex-compile` (which only checks the cites *resolve*).
This skill checks that each `refs.bib` entry is **bibliographically correct** against the
publisher's deposited metadata.

It pairs with the gatekeeper: gatekeeper = "is this key real and used?"; citation-check =
"is this entry's metadata true?".

## Core principle: DOI-anchored verification

**Authoritative field-checking requires a DOI.** With a DOI the skill pulls that exact
Crossref record and diffs every field — these findings are reliable. *Without* a DOI a title
search is too version-ambiguous to diff safely (it routinely matches an SSRN preprint or the
conference version of a journal paper), so the skill does **not** assert field discrepancies
for DOI-less entries — it surfaces the canonical published record and the DOI to add, so a
second pass can verify authoritatively. This is the right discipline: add DOIs, then verify.

## Invocation

User says: "check the citations", "verify the bib / references", "crossref the refs",
"citation hygiene pass". Also run it **before every compile you think of as final** and
before handing a draft off for submission.

## What this skill does

1. Identify the target's bib: `<target>/tex/refs.bib`.
2. Run the checker (pure stdlib, needs network for the Crossref API):

   ```bash
   python "<skill-dir>/scripts/check_citations.py" "<target>/tex/refs.bib" --email <user-email>
   ```

   It prints a banded report and exits `2` if any Critical/Important finding exists, else `0`.
   Add `--json` for a machine-readable form.

3. Present the findings to the user, grouped by band, and **propose the exact corrected
   BibTeX line** for each (the script already emits a `suggest:` line per finding). Do **not**
   edit `refs.bib` yourself — this is report-only, like the gatekeeper. The user (or a
   follow-up explicit "apply the fixes" instruction) decides.

4. If there are `NO-DOI` entries, recommend the **two-pass workflow**: add the suggested DOIs
   (after eyeballing the surfaced canonical record), then re-run for an authoritative field
   check. A bib with DOIs on every published entry is the goal.

## Reading the bands

- **CRITICAL — `WRONG-DOI`**: the DOI resolves to a *different* paper. Always fix.
- **IMPORTANT** (DOI-anchored, reliable): `YEAR`, `VENUE`, `VOLUME`, `ISSUE`, `PAGES`
  (first page), `AUTHORS` (missing/extra), `DOI-NOT-FOUND`. Real discrepancies — fix them.
- **MINOR** (DOI-anchored): `TITLE` casing/punctuation, `VENUE-ABBREV` (abbreviation vs full
  form — often a *deliberate* style choice; judge per the paper's convention), `PAGES-END`.
- **UNVERIFIABLE**:
  - `NO-DOI` — add the suggested DOI and re-run. The surfaced "closest Crossref record" lets
    the user eyeball volume/issue/pages/year against their entry immediately.
  - `NO-DOI-ALT` — a second strong match in a different venue (e.g. journal vs conference
    version). Pick the version the paper actually cites.
  - `PUBLISHED-VERSION-FOUND` — entry is a working paper but a journal version now exists;
    consider citing it.
  - `WORKING-PAPER` / `NO-CONFIDENT-MATCH` — not in Crossref; verify by hand.

## Judgment notes (do not over-apply)

- `VENUE-ABBREV` and `TITLE` capitalization are frequently intentional house style. Surface
  them, but don't push a "fix" that fights the paper's citation style.
- Crossref occasionally lacks an end page (common for older JSTOR deposits) or lists a
  preprint year. The skill already suppresses end-page noise when Crossref carries no range;
  still, sanity-check `YEAR` flags against print-vs-online dates before treating as gospel.
- The skill is conservative by design: a clean run on a DOI-rich bib is strong evidence; a
  pile of `NO-DOI` lines means "add DOIs to enable verification", not "the cites are wrong".

## Output format

```
## Citation check — <target>/tex/refs.bib
N entries | K clean (DOI-verified) | c critical | i important | m minor | u unverifiable

### CRITICAL (c)
- [WRONG-DOI] Key: ...

### IMPORTANT (i)
- [YEAR] Key: bib year X vs Crossref [Y]
    suggest: year = {Y}
...

### UNVERIFIABLE (u)
- [NO-DOI] Key: ... Closest Crossref record: <venue vol(iss) pages (year)>, DOI <doi>
    suggest: doi = {<doi>}
...
```

## What this skill does NOT do

- Does not edit `refs.bib` or any file (report-only).
- Does not check whether a cited paper *says* what the prose attributes to it (that's reading,
  not metadata).
- Does not check math, prose, or whether the paper is "good".
- Does not invent citations or fetch PDFs (for fetching, that's a separate concern).
