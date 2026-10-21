#!/usr/bin/env python3
"""Add paper PDFs to the site, with preview thumbnails.

Drop paper PDFs into one folder, named however they were downloaded. Each PDF
is matched to its papers.bib entry by
  * file name = bib key (WeiszMHSTS24.pdf),
  * file name = DOI suffix, as the ACM DL names downloads (3613904.3642466.pdf),
  * file name = arXiv id (2502.18509v2.pdf), or
  * the paper title found in the PDF's first page.

For each match
  * the PDF is copied to assets/pdf/papers/<key>.pdf and `pdf` is added to the
    entry, which gives the paper a PDF button, and
  * the top of the first page (title, authors, and usually the teaser figure)
    is rendered to assets/img/publication_preview/<key>.png and `preview` is
    added to the entry.
Existing PDFs and previews are kept unless --force is given.

Per-paper tweaks go in _bibliography/preview-overrides.txt, one line per key:
  WeiszMHSTS24  page=2 crop=0.05,0.45   # page 2, from 5% to 45% of its height
  DibiaACW17    crop=full               # the whole page
  Weisz09       nopdf                   # paywalled: preview only, never host the PDF

Usage:
  bin/make_previews.py ~/Downloads/papers            # all PDFs in a folder
  bin/make_previews.py ~/Downloads/papers --force    # redo existing previews
  bin/make_previews.py ~/Downloads/papers --dry-run  # only report matches
"""

import argparse
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from update_pubs import BIB_PATH, ROOT, format_entry, norm_title, parse_bib  # noqa: E402

OUT_DIR = os.path.join(ROOT, "assets", "img", "publication_preview")
PDF_DIR = os.path.join(ROOT, "assets", "pdf", "papers")
OVERRIDES_PATH = os.path.join(ROOT, "_bibliography", "preview-overrides.txt")
WIDTH = 600  # px; the preview column is ~150px wide, so this is sharp on 2x+ screens
DEFAULT_CROP = (0.0, 0.42)  # top of the page, about 4:3 for a US Letter page
DPI = 200
SIDE_TRIM = 0.07  # fraction of the page width cut from each side


def load_overrides():
    overrides = {}
    if not os.path.exists(OVERRIDES_PATH):
        return overrides
    with open(OVERRIDES_PATH) as fh:
        for line in fh:
            parts = line.split("#")[0].split()
            if parts:
                overrides[parts[0]] = dict((p.split("=", 1) + [True])[:2] for p in parts[1:])
    return overrides


def pdf_text(pdf):
    out = subprocess.run(["pdftotext", "-q", "-f", "1", "-l", "1", pdf, "-"], capture_output=True, text=True)
    return out.stdout


def match_pdf(pdf, entries, by_title):
    stem = re.sub(r"\s*\(\d+\)$", "", os.path.splitext(os.path.basename(pdf))[0])
    for e in entries:
        f = e["fields"]
        if stem == e["key"] or stem.lower() == f.get("doi", "").split("/")[-1].lower():
            return e
        if f.get("arxiv") and re.sub(r"v\d+$", "", stem) == f["arxiv"]:
            return e
    # Fall back to finding a title in the first page's text
    text = norm_title(pdf_text(pdf))
    hits = [e for t, e in by_title.items() if len(t) > 15 and t in text]
    return max(hits, key=lambda e: len(norm_title(e["fields"]["title"])), default=None)


def render(pdf, out_path, page=1, crop=DEFAULT_CROP):
    with tempfile.TemporaryDirectory() as tmp:
        base = os.path.join(tmp, "page")
        subprocess.run(["pdftoppm", "-q", "-f", str(page), "-l", str(page), "-r", str(DPI), "-png", "-singlefile",
                        pdf, base], check=True)
        size = subprocess.run(["magick", "identify", "-format", "%w %h", base + ".png"], capture_output=True, text=True)
        w, h = map(int, size.stdout.split())
        top, bottom = (0.0, 1.0) if crop == "full" else crop
        # Trim the side margins, which hold arXiv stamps and publisher page tabs
        x = int(w * SIDE_TRIM)
        geometry = "%dx%d+%d+%d" % (w - 2 * x, int(h * (bottom - top)), x, int(h * top))
        cmd = ["magick", base + ".png", "-crop", geometry, "+repage"]
        cmd += ["-resize", "%dx" % WIDTH, "-strip", "-colors", "64", out_path]
        subprocess.run(cmd, check=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("folder", help="folder of paper PDFs")
    ap.add_argument("--force", action="store_true", help="regenerate previews that already exist")
    ap.add_argument("--dry-run", action="store_true", help="report matches without writing")
    args = ap.parse_args()

    for tool in ("pdftoppm", "pdftotext", "magick"):
        if subprocess.run(["which", tool], capture_output=True).returncode:
            sys.exit("%s not found (brew install poppler imagemagick)" % tool)

    pdfs = sorted(glob.glob(os.path.join(os.path.expanduser(args.folder), "*.pdf")))
    if not pdfs:
        sys.exit("No PDFs found in %s" % args.folder)

    with open(BIB_PATH) as fh:
        text = fh.read()
    entries = parse_bib(text)
    by_title = {norm_title(e["fields"].get("title", "")): e for e in entries}
    overrides = load_overrides()
    os.makedirs(OUT_DIR, exist_ok=True)
    os.makedirs(PDF_DIR, exist_ok=True)

    edits, seen, unmatched = [], set(), []
    for pdf in pdfs:
        e = match_pdf(pdf, entries, by_title)
        name = os.path.basename(pdf)
        if not e:
            unmatched.append(name)
            continue
        key = e["key"]
        if key in seen:
            print("= dup      %-28s %s (already used another PDF)" % (key, name))
            continue
        seen.add(key)
        opts = overrides.get(key, {})
        fields = dict(e["fields"])

        pdf_name = "papers/%s.pdf" % key
        pdf_path = os.path.join(PDF_DIR, key + ".pdf")
        if opts.get("nopdf"):
            if os.path.exists(pdf_path):
                print("! nopdf    %-28s assets/pdf/%s is on the site; delete it" % (key, pdf_name))
        elif os.path.exists(pdf_path) and not args.force:
            print("  skip     %-28s %s (PDF exists; --force to replace)" % (key, name))
        else:
            print("+ pdf      %-28s %s" % (key, name))
            if not args.dry_run:
                shutil.copyfile(pdf, pdf_path)
        if not opts.get("nopdf") and not fields.get("pdf"):
            fields["pdf"] = pdf_name

        filename = key + ".png"
        out_path = os.path.join(OUT_DIR, filename)
        if os.path.exists(out_path) and not args.force and not ("page" in opts or "crop" in opts):
            print("  skip     %-28s %s (preview exists; --force to redo)" % (key, name))
        else:
            crop = opts.get("crop", "")
            crop = "full" if crop == "full" else tuple(map(float, crop.split(","))) if crop else DEFAULT_CROP
            print("+ preview  %-28s %s" % (key, name))
            if not args.dry_run:
                render(pdf, out_path, int(opts.get("page", 1)), crop)
        fields["preview"] = filename
        if fields != e["fields"]:
            edits.append((e["span"], format_entry(e["type"], key, fields).rstrip("\n")))

    for name in unmatched:
        print("! no match %s (rename it to its bib key, e.g. WeiszMHSTS24.pdf)" % name)
    missing = [e["key"] for e in entries if e["key"] not in seen and "preview" not in e["fields"]]
    if missing:
        print("\n%d entries still have no preview: %s" % (len(missing), " ".join(missing)))

    if args.dry_run or not edits:
        return
    for (s, t), repl in sorted(edits, key=lambda x: x[0][0], reverse=True):
        text = text[:s] + repl + text[t:]
    with open(BIB_PATH, "w") as fh:
        fh.write(text)
    print("\nAdded `pdf`/`preview` to %d entries in _bibliography/papers.bib." % len(edits))


if __name__ == "__main__":
    main()
