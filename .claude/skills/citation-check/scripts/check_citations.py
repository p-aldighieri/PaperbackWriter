#!/usr/bin/env python3
"""
check_citations.py -- verify every BibTeX entry against Crossref.

Design principle: AUTHORITATIVE field-checking requires a DOI. When an entry has a
DOI we pull that exact record and diff every field. When it does NOT, a title search
is too version-ambiguous to diff safely (it routinely matches an SSRN preprint or a
conference version of a journal paper), so we DO NOT assert field discrepancies --
instead we surface the canonical published record and the DOI to add, so a second
pass can verify authoritatively. Working papers / preprints are reported as such,
with a check for whether a published version now exists.

Pure standard library (urllib). No installs. Report-only -- never edits the .bib.

USAGE
  python check_citations.py path/to/refs.bib [--email you@example.com] [--json] [--quiet]

EXIT CODES
  0  no Critical/Important findings   (clean, or only add-a-DOI suggestions)
  2  at least one Critical or Important finding
  1  usage / read error

SEVERITY
  CRITICAL  WRONG-DOI (the DOI resolves to a different paper)
  IMPORTANT (DOI-anchored only) VENUE / VOLUME / ISSUE / PAGES / AUTHORS / YEAR; DOI-NOT-FOUND
  MINOR     (DOI-anchored only) title casing/punctuation; venue abbreviation; last-page-only
  UNVERIFIABLE  no-DOI (add one to verify); working paper / preprint; no confident match
"""
import argparse, difflib, json, re, sys, time, unicodedata, urllib.error, urllib.parse, urllib.request

UA = "PaperbackWriter-citation-check/1.0 (mailto:%s)"
DEFAULT_EMAIL = "pbragasoares@gmail.com"
WP_MARKERS = ("working paper", "arxiv", "mimeo", "manuscript", "unpublished",
              "discussion paper", "preprint", "in preparation", "ssrn",
              "nber working", "technical report", "tech. rep")
PUB_TYPES = ("journal-article", "proceedings-article", "book-chapter")


# ---------- BibTeX parsing (brace-aware, no deps) ----------
def _match_brace(text, i):
    depth = 0
    for k in range(i, len(text)):
        if text[k] == '{':
            depth += 1
        elif text[k] == '}':
            depth -= 1
            if depth == 0:
                return k
    return -1


def _clean(v):
    v = re.sub(r'\s+', ' ', v.replace('\n', ' ')).strip()
    return v.replace('{', '').replace('}', '').strip().rstrip(',').strip()


def _parse_fields(s):
    fields, i, n = {}, 0, len(s)
    while i < n:
        while i < n and s[i] in ' \t\r\n,':
            i += 1
        m = re.match(r'([A-Za-z][\w-]*)\s*=\s*', s[i:])
        if not m:
            break
        name = m.group(1).lower()
        i += m.end()
        if i >= n:
            break
        if s[i] == '{':
            close = _match_brace(s, i)
            if close < 0:
                break
            val, i = s[i + 1:close], close + 1
        elif s[i] == '"':
            depth, k = 0, i + 1
            while k < n:
                if s[k] == '{':
                    depth += 1
                elif s[k] == '}':
                    depth -= 1
                elif s[k] == '"' and depth == 0:
                    break
                k += 1
            val, i = s[i + 1:k], k + 1
        else:
            k = i
            while k < n and s[k] not in ',}':
                k += 1
            val, i = s[i:k].strip(), k
        fields[name] = _clean(val)
    return fields


def parse_bib(text):
    entries, i = [], 0
    while True:
        at = text.find('@', i)
        if at < 0:
            break
        m = re.match(r'@(\w+)\s*\{', text[at:])
        if not m:
            i = at + 1
            continue
        typ = m.group(1).lower()
        if typ in ('comment', 'preamble', 'string'):
            i = at + 1
            continue
        brace = at + m.end() - 1
        close = _match_brace(text, brace)
        if close < 0:
            break
        body = text[brace + 1:close]
        comma = body.find(',')
        key = (body[:comma] if comma >= 0 else body).strip()
        fields = _parse_fields(body[comma + 1:]) if comma >= 0 else {}
        entries.append({'type': typ, 'key': key, 'fields': fields})
        i = close + 1
    return entries


# ---------- Crossref ----------
def _get(url, email):
    req = urllib.request.Request(url, headers={"User-Agent": UA % email})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def crossref_by_doi(doi, email):
    try:
        return _get("https://api.crossref.org/works/" + urllib.parse.quote(doi), email).get("message")
    except urllib.error.HTTPError as e:
        return "NOT_FOUND" if e.code == 404 else None
    except Exception:
        return None


def crossref_candidates(title, author, email, rows=10):
    try:
        q = {"query.bibliographic": title, "rows": str(rows)}
        if author:
            q["query.author"] = author
        items = _get("https://api.crossref.org/works?" + urllib.parse.urlencode(q), email)\
            .get("message", {}).get("items", [])
        scored = [(it, _ratio(title, (it.get("title") or [""])[0])) for it in items]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored
    except Exception:
        return []


# ---------- normalization / compare ----------
def _fold(s):
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()


def _norm_title(s):
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9 ]', ' ', _fold(s))).strip()


def _ratio(a, b):
    return difflib.SequenceMatcher(None, _norm_title(a), _norm_title(b)).ratio()


def _first_page(p):
    return re.split(r'[-–—]', (p or '').replace('--', '-').strip())[0].strip()


def _families(authors):
    out = []
    for a in authors or []:
        fam = a.get("family") or a.get("name") or ""
        if fam:
            out.append(_fold(fam).strip())
    return out


def _bib_families(s):
    out = []
    for a in re.split(r'\s+and\s+', s or ''):
        a = a.strip()
        if not a:
            continue
        fam = a.split(',')[0].strip() if ',' in a else a.split()[-1]
        out.append(_fold(fam).strip())
    return out


def _is_wp(entry):
    f = entry['fields']
    if entry['type'] in ('unpublished', 'misc', 'techreport') and not f.get('doi'):
        return True
    blob = " ".join([f.get('journal', ''), f.get('booktitle', ''), f.get('note', ''),
                     f.get('howpublished', ''), f.get('publisher', '')]).lower()
    return any(mk in blob for mk in WP_MARKERS)


def _is_preprint(m):
    ct = (m.get("container-title") or [""])[0].lower()
    return m.get("type") in ("posted-content", "preprint") or "ssrn" in ct or "arxiv" in ct


def _cr_years(m):
    ys = []
    for fld in ('issued', 'published-print', 'published', 'published-online'):
        dp = (m.get(fld) or {}).get('date-parts') or [[None]]
        if dp and dp[0] and dp[0][0]:
            ys.append(int(dp[0][0]))
    return ys


def _cite_str(m):
    ct = (m.get("container-title") or [""])[0]
    vol, iss, pg = m.get("volume", ""), m.get("issue", ""), m.get("page", "")
    yr = (_cr_years(m) or [""])[0]
    vi = f"{vol}({iss})" if (vol or iss) else (vol or "")
    s = f"{ct} {vi} {pg} ({yr}) [{m.get('type', '')}], DOI {m.get('DOI', '')}"
    return re.sub(r'\s+', ' ', s).strip()


def _diff_fields(f, m):
    """Authoritative field diff against a DOI-resolved record."""
    out = []
    cr_title = (m.get('title') or [''])[0]
    cr_cont = (m.get('container-title') or [''])[0]
    cr_vol = str(m.get('volume', '') or '')
    cr_iss = str(m.get('issue', '') or '')
    cr_page = str(m.get('page', '') or '')
    cr_years = _cr_years(m)

    if f.get('title') and _ratio(f['title'], cr_title) < 0.85:
        out.append(('MINOR', 'TITLE', f"bib '{f['title']}' vs Crossref '{cr_title}'",
                    f"title = {{{cr_title}}}"))
    by = f.get('year', '')
    if by and cr_years and not any(str(y) == re.sub(r'\D', '', by) for y in cr_years):
        out.append(('IMPORTANT', 'YEAR', f"bib year {by} vs Crossref {cr_years}",
                    f"year = {{{cr_years[0]}}}"))
    bj = f.get('journal', '') or f.get('booktitle', '')
    if bj and cr_cont:
        vr = _ratio(bj, cr_cont)
        if vr < 0.6:
            out.append(('IMPORTANT', 'VENUE', f"bib '{bj}' vs Crossref '{cr_cont}'",
                        f"journal = {{{cr_cont}}}"))
        elif vr < 0.92:
            out.append(('MINOR', 'VENUE-ABBREV', f"bib '{bj}' vs Crossref '{cr_cont}'", ''))
    bv = f.get('volume', '')
    if bv and cr_vol and re.sub(r'\D', '', bv) != re.sub(r'\D', '', cr_vol):
        out.append(('IMPORTANT', 'VOLUME', f"bib volume {bv} vs Crossref {cr_vol}",
                    f"volume = {{{cr_vol}}}"))
    bn = f.get('number', '') or f.get('issue', '')
    if bn and cr_iss and bn.strip() != cr_iss.strip():
        out.append(('IMPORTANT', 'ISSUE', f"bib number {bn} vs Crossref issue {cr_iss}",
                    f"number = {{{cr_iss}}}"))
    bp = f.get('pages', '')
    if bp and cr_page:
        if _first_page(bp) != _first_page(cr_page):
            out.append(('IMPORTANT', 'PAGES', f"bib pages {bp} vs Crossref {cr_page}",
                        f"pages = {{{cr_page.replace('-', '--')}}}"))
        elif re.search(r'[-–—]', cr_page) and \
                _fold(bp).replace('--', '-') != _fold(cr_page).replace('--', '-'):
            # only when Crossref actually carries an end page (JSTOR deposits often don't)
            out.append(('MINOR', 'PAGES-END', f"bib pages {bp} vs Crossref {cr_page}",
                        f"pages = {{{cr_page.replace('-', '--')}}}"))
    bf, cf = _bib_families(f.get('author', '')), _families(m.get('author'))
    if bf and cf:
        missing = [a for a in cf if a not in bf]
        extra = [a for a in bf if a not in cf]
        if missing or extra:
            msg = []
            if missing:
                msg.append("Crossref authors not in bib: " + ", ".join(missing))
            if extra:
                msg.append("bib authors not in Crossref: " + ", ".join(extra))
            out.append(('IMPORTANT', 'AUTHORS', "; ".join(msg), ''))
    return out


# ---------- per-entry check ----------
def check_entry(entry, email):
    f = entry['fields']
    key = entry['key']
    title = f.get('title', '')
    doi = f.get('doi', '')

    # 1) DOI present -> authoritative
    if doi:
        m = crossref_by_doi(doi, email)
        if m == "NOT_FOUND":
            return key, 'doi-missing', [('IMPORTANT', 'DOI-NOT-FOUND',
                                         f"DOI {doi} not found in Crossref", '')]
        if m is None:
            return key, 'error', [('UNVERIFIABLE', 'LOOKUP-FAILED',
                                   f"Crossref lookup failed for DOI {doi}", '')]
        if title and _ratio(title, (m.get('title') or [''])[0]) < 0.5:
            return key, 'doi', [('CRITICAL', 'WRONG-DOI',
                                 f"DOI {doi} resolves to a DIFFERENT paper: "
                                 f"\"{(m.get('title') or [''])[0]}\"", 'fix the DOI or the entry')]
        return key, 'doi', _diff_fields(f, m)

    # 2) working paper / preprint (no DOI)
    if _is_wp(entry):
        if title:
            cands = crossref_candidates(title, f.get('author', ''), email)
            pub = next((c for c, r in cands if r >= 0.9 and not _is_preprint(c)
                        and c.get('type') in PUB_TYPES), None)
            if pub:
                return key, 'wp-pub', [('UNVERIFIABLE', 'PUBLISHED-VERSION-FOUND',
                                        f"listed as working paper; a published version exists: "
                                        f"{_cite_str(pub)}",
                                        f"consider citing it (doi = {{{pub.get('DOI', '')}}})")]
        return key, 'wp', [('UNVERIFIABLE', 'WORKING-PAPER',
                            'working paper / preprint -- not a published record; verify by hand', '')]

    # 3) no DOI, not a working paper -> actionable, no field assertions
    if not title:
        return key, 'no-title', [('UNVERIFIABLE', 'NO-TITLE', 'no title field to search on', '')]
    cands = crossref_candidates(title, f.get('author', ''), email)
    good = [(c, r) for c, r in cands if r >= 0.80]
    if not good:
        best = cands[0][1] if cands else 0.0
        return key, 'no-match', [('UNVERIFIABLE', 'NO-CONFIDENT-MATCH',
                                  f"no confident Crossref match (best title similarity {best:.2f}); "
                                  f"verify by hand", '')]
    pub = next((c for c, r in good if not _is_preprint(c) and c.get('type') in PUB_TYPES), None)
    chosen = pub or good[0][0]
    if _is_preprint(chosen):
        out = [('UNVERIFIABLE', 'NO-DOI',
                f"not DOI-anchored, and only a PREPRINT record was found (the published DOI may "
                f"differ -- confirm it by hand). Closest: {_cite_str(chosen)}", '')]
    else:
        out = [('UNVERIFIABLE', 'NO-DOI',
                f"not DOI-anchored -- add a DOI to verify fields authoritatively. "
                f"Closest Crossref record: {_cite_str(chosen)}",
                f"doi = {{{chosen.get('DOI', '')}}}   (then re-run for a full field check)")]
    alt = next((c for c, r in good
                if c.get('DOI', '') != chosen.get('DOI', '') and r >= 0.9
                and (c.get('container-title') or [''])[0].lower()
                != (chosen.get('container-title') or [''])[0].lower()), None)
    if alt:
        out.append(('UNVERIFIABLE', 'NO-DOI-ALT',
                    f"alternative record (pick the right version): {_cite_str(alt)}", ''))
    return key, 'title', out


# ---------- main ----------
def main():
    ap = argparse.ArgumentParser(description="Verify every BibTeX entry against Crossref.")
    ap.add_argument("bib")
    ap.add_argument("--email", default=DEFAULT_EMAIL)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true", help="suppress per-entry progress on stderr")
    a = ap.parse_args()

    try:
        with open(a.bib, encoding="utf-8") as fh:
            text = fh.read()
    except Exception as e:
        print(f"cannot read {a.bib}: {e}", file=sys.stderr)
        return 1

    entries = parse_bib(text)
    if not entries:
        print(f"no BibTeX entries found in {a.bib}", file=sys.stderr)
        return 1

    bands = {'CRITICAL': [], 'IMPORTANT': [], 'MINOR': [], 'UNVERIFIABLE': []}
    ok, records = [], []
    for idx, e in enumerate(entries, 1):
        if not a.quiet:
            print(f"  [{idx}/{len(entries)}] {e['key']}", file=sys.stderr)
        key, how, findings = check_entry(e, a.email)
        records.append({'key': key, 'matched_by': how,
                        'findings': [{'severity': s, 'code': c, 'message': msg, 'suggest': sg}
                                     for (s, c, msg, sg) in findings]})
        if not findings:
            ok.append(key)
        for (sev, code, msg, sg) in findings:
            bands[sev].append((key, code, msg, sg))
        time.sleep(0.15)

    if a.json:
        print(json.dumps({'records': records,
                          'summary': {k: len(v) for k, v in bands.items()},
                          'clean': ok}, indent=2))
        return 2 if (bands['CRITICAL'] or bands['IMPORTANT']) else 0

    print(f"\n## Citation check -- {a.bib}")
    print(f"{len(entries)} entries | {len(ok)} clean (DOI-verified) | "
          f"{len(bands['CRITICAL'])} critical | {len(bands['IMPORTANT'])} important | "
          f"{len(bands['MINOR'])} minor | {len(bands['UNVERIFIABLE'])} unverifiable\n")
    for sev in ('CRITICAL', 'IMPORTANT', 'MINOR', 'UNVERIFIABLE'):
        rows = bands[sev]
        if not rows:
            continue
        print(f"### {sev} ({len(rows)})")
        for (key, code, msg, sg) in rows:
            print(f"- [{code}] {key}: {msg}")
            if sg:
                print(f"    suggest: {sg}")
        print()
    if ok:
        print(f"### CLEAN -- DOI-verified, no discrepancies ({len(ok)})")
        print("  " + ", ".join(ok) + "\n")
    print("Report-only: no files were edited. CRITICAL/IMPORTANT are DOI-anchored and "
          "reliable; add the suggested DOIs and re-run to authoritatively verify the rest.")
    return 2 if (bands['CRITICAL'] or bands['IMPORTANT']) else 0


if __name__ == "__main__":
    sys.exit(main())
