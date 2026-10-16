#!/usr/bin/env python3
"""Merge new publications from DBLP into _bibliography/papers.bib.

papers.bib is the curated source of truth: entries already in it are never
rewritten. The script only
  * adds DBLP entries that are not on the site yet,
  * replaces an arXiv-only preprint with its published version once DBLP
    lists it (keeping site fields such as `selected` and `award`, and
    updating {% cite %} keys in pages and projects), and
  * adds an `arxiv` field to a published entry when DBLP lists its preprint.

DBLP keys listed in _bibliography/dblp-ignore.txt are never imported; add a
key there after deleting an entry you don't want on the site.

Usage:
  bin/update_pubs.py                # download from DBLP
  bin/update_pubs.py dblp.bib       # use a .bib file downloaded by hand
  bin/update_pubs.py --dry-run      # report changes without writing
"""

import argparse
import os
import re
import sys
import urllib.request

DBLP_PID = "02/133"
DBLP_URL = "https://dblp.org/pid/%s.bib" % DBLP_PID
DBLP_PAGE = "https://dblp.org/pid/%s.html?view=bibtex" % DBLP_PID

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIB_PATH = os.path.join(ROOT, "_bibliography", "papers.bib")
IGNORE_PATH = os.path.join(ROOT, "_bibliography", "dblp-ignore.txt")
CITE_DIRS = ["_pages", "_projects"]

# DBLP bookkeeping fields that add nothing on the site
DROP_FIELDS = {"timestamp", "biburl", "bibsource", "editor", "eprinttype", "eprint"}
# Site-specific fields carried over when a preprint is replaced by its published version
CARRY_FIELDS = [
    "selected", "award", "award_name", "preview", "pdf", "code", "website", "slides",
    "poster", "video", "blog", "html", "supp", "abstract", "google_scholar_id",
]
# DBLP venue key -> badge abbreviation (colors live in _data/venues.yml)
VENUES = {
    "aies": "AIES", "acl": "ACL", "chiplay": "CHI PLAY", "chiwork": "CHIWORK", "comsnets": "COMSNETS",
    "cscw": "CSCW", "cui": "CUI", "fat": "FAccT", "facct": "FAccT", "icccrea": "ICCC", "icml": "ICML",
    "ijcai": "IJCAI", "mobicom": "MobiCom", "uxtv": "UXTV", "ibmrd": "IBM JRD", "pacmhci": "CSCW",
    "tochi": "TOCHI", "igi": "Book", "um": "UMAP",
}


# ---------------------------------------------------------------------------
# BibTeX parsing and formatting
# ---------------------------------------------------------------------------

def parse_bib(text):
    """Return entries as dicts with type, key, ordered fields, and their [start, end) span in text."""
    entries = []
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", text):
        start, i, depth = m.start(), m.end(), 1
        while depth and i < len(text):
            depth += {"{": 1, "}": -1}.get(text[i], 0)
            i += 1
        body = text[m.end():i - 1]
        fields = {}
        j = 0
        while True:
            fm = re.compile(r"\s*,?\s*(\w+)\s*=\s*").match(body, j)
            if not fm or fm.end() >= len(body):
                break
            k, j = fm.group(1).lower(), fm.end()
            if body[j] == "{":
                d, s = 0, j
                while True:
                    d += {"{": 1, "}": -1}.get(body[j], 0)
                    j += 1
                    if d == 0:
                        break
                value = body[s + 1:j - 1]
            elif body[j] == '"':
                e = body.index('"', j + 1)
                value, j = body[j + 1:e], e + 1
            else:
                vm = re.compile(r"[^,\s]+").match(body, j)
                value, j = vm.group(0), vm.end()
            fields[k] = re.sub(r"\s*\n\s*", " ", value).strip()
        entries.append({"type": m.group(1).lower(), "key": m.group(2), "fields": fields,
                        "span": (start, i)})
    return entries


def format_entry(typ, key, fields):
    width = max(len(k) for k in fields)
    body = ",\n".join("  %s = {%s}" % (k.ljust(width), v) for k, v in fields.items())
    return "@%s{%s,\n%s\n}\n" % (typ, key, body)


def norm_title(title):
    return re.sub(r"[^a-z0-9]", "", title.lower().replace("{", "").replace("}", ""))


# ---------------------------------------------------------------------------
# DBLP entries -> site entries
# ---------------------------------------------------------------------------

def dblp_venue(key):
    parts = key.split(":", 1)[-1].split("/")
    return parts[1] if len(parts) > 2 else ""


def is_corr(key):
    return key.startswith("DBLP:journals/corr/")


def site_key(dblp_key):
    return dblp_key.split("/")[-1]


def abbr_for(entry):
    venue, f = dblp_venue(entry["key"]), entry["fields"]
    bt, series = f.get("booktitle", ""), f.get("series", "")
    if venue == "corr":
        return "arXiv"
    if venue == "chi":
        return "CHI EA" if "Extended Abstracts" in bt else "CHI"
    if venue == "iui":
        if "CEUR" in series or "Workshops" in bt:
            return "IUI WS"
        return "IUI Comp." if "Companion" in bt else "IUI"
    if venue in ("kdd", "aaai", "cikm") and ("Workshop" in bt or "CEUR" in series):
        return venue.upper() + " WS"
    if venue in VENUES:
        return VENUES[venue]
    return None


def to_site_entry(entry):
    """Clean a DBLP entry into papers.bib form: badge, bibtex button, no DBLP noise."""
    f = dict(entry["fields"])
    # DBLP sometimes glues page ranges onto CEUR titles ("... Persona 121-129")
    f["title"] = re.sub(r"\s+\d+-\d+$", "", f.get("title", ""))
    abbr = abbr_for(entry)
    out = {"abbr": abbr or dblp_venue(entry["key"]).upper(), "bibtex_show": "true"}
    if is_corr(entry["key"]) and "eprint" in f:
        out["arxiv"] = f["eprint"]
        f.pop("doi", None)
    for k, v in f.items():
        if k not in DROP_FIELDS and k not in out:
            out[k] = v
    return out, abbr is None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def fetch_dblp():
    req = urllib.request.Request(DBLP_URL, headers={"User-Agent": "jweisz.org publication sync (web@jweisz.org)"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            text = resp.read().decode("utf-8")
    except Exception as exc:  # network errors, HTTP 429, etc.
        text, err = "", str(exc)
    else:
        err = "DBLP returned a web page instead of BibTeX (probably its bot check)"
    if text.lstrip().startswith("@"):
        return text
    sys.exit(
        "Could not download %s: %s.\n"
        "Download it in a browser instead: open %s and save the BibTeX,\n"
        "then pass the file to this script, e.g.:\n"
        "  mise run pubs ~/Downloads/dblp.bib" % (DBLP_URL, err, DBLP_PAGE)
    )


def load_ignore():
    if not os.path.exists(IGNORE_PATH):
        return set()
    with open(IGNORE_PATH) as fh:
        return {line.split("#")[0].strip() for line in fh} - {""}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("bibfile", nargs="?", help="DBLP .bib file to use instead of downloading")
    ap.add_argument("--dry-run", action="store_true", help="report changes without writing")
    args = ap.parse_args()

    if args.bibfile:
        with open(os.path.expanduser(args.bibfile)) as fh:
            dblp_text = fh.read()
    else:
        dblp_text = fetch_dblp()
    dblp = parse_bib(dblp_text)
    if not dblp or not any(e["key"].startswith("DBLP:") for e in dblp):
        sys.exit("No DBLP entries found in the input.")

    with open(BIB_PATH) as fh:
        text = fh.read()
    site = parse_bib(text)
    ignore = load_ignore()

    site_keys = {e["key"] for e in site} | {re.sub(r"b$", "", e["key"]) for e in site}
    site_arxiv = {e["fields"]["arxiv"] for e in site if "arxiv" in e["fields"]}
    by_title = {}
    for e in site:
        by_title.setdefault(norm_title(e["fields"].get("title", "")), e)

    added, upgraded, linked, unknown = [], [], [], []
    edits = []  # (span, replacement text) applied to papers.bib, back to front
    renames = {}

    # Published versions first, so a preprint and its published version in the
    # same run resolve to one entry.
    for d in sorted(dblp, key=lambda e: is_corr(e["key"])):
        key = site_key(d["key"])
        if d["key"] in ignore or key in ignore or key in site_keys:
            continue
        title = d["fields"].get("title", "")
        match = by_title.get(norm_title(title))

        if is_corr(d["key"]):
            eprint = d["fields"].get("eprint")
            if eprint in site_arxiv:
                continue
            if match and match["fields"].get("abbr") != "arXiv":
                if "arxiv" not in match["fields"] and eprint:
                    match["fields"]["arxiv"] = eprint
                    if match["span"]:  # existing entry; entries added in this run are written later
                        edits.append((match["span"], format_entry(match["type"], match["key"], match["fields"]).rstrip("\n")))
                    site_arxiv.add(eprint)
                    linked.append((match["key"], eprint))
                continue
            if match:
                continue

        fields, unknown_venue = to_site_entry(d)
        if match and match["fields"].get("abbr") == "arXiv" and not is_corr(d["key"]):
            # A preprint on the site has been published: replace it in place
            old = match["fields"]
            for k in CARRY_FIELDS:
                if k in old and k not in fields:
                    fields[k] = old[k]
            if "arxiv" in old:
                fields.setdefault("arxiv", old["arxiv"])
            edits.append((match["span"], format_entry(d["type"], key, fields).rstrip("\n")))
            renames[match["key"]] = key
            upgraded.append((match["key"], key, fields["abbr"], old.get("additional_info")))
        elif match:
            continue  # already on the site under a different key (e.g. added by hand)
        else:
            added.append((d["type"], key, fields))
        if unknown_venue:
            unknown.append((key, dblp_venue(d["key"]), fields["abbr"]))
        site_keys.add(key)
        if "arxiv" in fields:
            site_arxiv.add(fields["arxiv"])
        by_title[norm_title(title)] = {"key": key, "fields": fields, "type": d["type"], "span": None}

    # Report
    for typ, key, f in added:
        print("+ add      %-28s [%s] %s (%s)" % (key, f["abbr"], f.get("title"), f.get("year")))
    for old, new, abbr, info in upgraded:
        print("~ publish  %-28s -> %s [%s]" % (old, new, abbr))
        if info:
            print("           dropped note: %s" % info)
    for key, eprint in linked:
        print("~ arxiv    %-28s + arXiv:%s" % (key, eprint))
    for key, venue, abbr in unknown:
        print("! venue    %-28s DBLP venue '%s' has no badge mapping; using '%s'."
              " Add it to VENUES in bin/update_pubs.py and a color in _data/venues.yml." % (key, venue, abbr))
    if not (added or upgraded or linked):
        print("papers.bib is up to date with DBLP (%d DBLP entries checked)." % len(dblp))
        return
    if args.dry_run:
        print("\nDry run: papers.bib not changed.")
        return

    for (s, e), repl in sorted(edits, key=lambda x: x[0][0], reverse=True):
        text = text[:s] + repl + text[e:]
    if added:
        new_text = "".join(format_entry(t, k, f) + "\n" for t, k, f in added)
        fm = re.match(r"---\s*\n---\s*\n\s*", text)
        pos = fm.end() if fm else 0
        text = text[:pos] + new_text + text[pos:]
    with open(BIB_PATH, "w") as fh:
        fh.write(text)

    # Keep {% cite %} references pointing at upgraded entries
    for d in CITE_DIRS:
        for dirpath, _, files in os.walk(os.path.join(ROOT, d)):
            for name in files:
                if not name.endswith((".md", ".html", ".liquid")):
                    continue
                path = os.path.join(dirpath, name)
                with open(path) as fh:
                    src = fh.read()
                out = src
                for old, new in renames.items():
                    out = re.sub(r"(\{%\s*cite\s+(?:[\w:-]+\s+)*)" + re.escape(old) + r"\b", r"\g<1>" + new, out)
                if out != src:
                    with open(path, "w") as fh:
                        fh.write(out)
                    print("  updated cite keys in %s" % os.path.relpath(path, ROOT))

    print("\nUpdated _bibliography/papers.bib: %d added, %d preprints published, %d arXiv links."
          % (len(added), len(upgraded), len(linked)))
    print("New entries get a venue badge but not `selected` or awards; edit papers.bib to add those.")


if __name__ == "__main__":
    main()
