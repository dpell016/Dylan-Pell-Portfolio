#!/usr/bin/env python3
"""
Build the portfolio website and PDF from the markdown files in content/projects/.

Usage:
    python3 build.py            # build website into docs/
    python3 build.py --pdf      # build website and render the PDF
    python3 build.py --serve    # build, then serve at http://localhost:8000

Adding a project: copy content/projects/_TEMPLATE.md to NN-slug.md, fill it in,
drop images into assets/images/<slug>/, and rebuild. Nothing else to touch.
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).parent
CONTENT = ROOT / "content" / "projects"
TEMPLATES = ROOT / "templates"
ASSETS = ROOT / "assets"
SITE = ROOT / "docs"  # GitHub Pages only serves from root or docs/, so output here

MATH_BLOCK = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
MATH_INLINE = re.compile(r"(?<!\$)\$([^\$\n]+?)\$(?!\$)")


def parse_frontmatter(text):
    """Split a markdown file into (frontmatter dict, body string)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    meta = yaml.safe_load(text[3:end]) or {}
    body = text[end + 4:].lstrip("\n")
    return meta, body


def render_markdown(body):
    """Convert markdown to HTML, shielding math from the markdown parser."""
    stash = []

    def stash_math(match, display):
        stash.append((match.group(1), display))
        return f"@@MATH{len(stash) - 1}@@"

    body = MATH_BLOCK.sub(lambda m: stash_math(m, True), body)
    body = MATH_INLINE.sub(lambda m: stash_math(m, False), body)

    html = markdown.markdown(
        body, extensions=["extra", "sane_lists", "toc", "attr_list"]
    )

    for i, (expr, display) in enumerate(stash):
        expr = expr.strip()
        rendered = (
            f'<div class="math-display">$${expr}$$</div>'
            if display
            else f'<span class="math-inline">${expr}$</span>'
        )
        html = html.replace(f"@@MATH{i}@@", rendered)
    return html


def load_projects():
    projects = []
    for path in sorted(CONTENT.glob("*.md")):
        if path.name.startswith("_"):
            continue
        meta, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        if not meta.get("slug"):
            print(f"  ! skipping {path.name}: no slug in frontmatter")
            continue
        meta["body_html"] = render_markdown(body)
        meta["source"] = path.name
        # Only keep images that actually exist, so missing photos degrade gracefully.
        meta["images"] = [
            img for img in (meta.get("images") or [])
            if (ASSETS / "images" / img["file"]).exists()
        ]
        hero = meta.get("hero")
        meta["hero_exists"] = bool(hero and (ASSETS / "images" / hero).exists())
        projects.append(meta)
    projects.sort(key=lambda p: p.get("order", 999))
    return projects


def build(render_pdf=False):
    cfg = yaml.safe_load((ROOT / "portfolio.yaml").read_text(encoding="utf-8"))
    projects = load_projects()
    print(f"  found {len(projects)} projects")

    env = Environment(
        loader=FileSystemLoader(TEMPLATES),
        autoescape=select_autoescape(["html"]),
    )
    env.filters["md"] = render_markdown

    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)
    shutil.copytree(ASSETS, SITE / "assets")

    # Custom domain for GitHub Pages. Written on every build so it survives the rmtree
    # above; without this the CNAME is lost on rebuild and the domain detaches.
    domain = (cfg.get("domain") or "").strip()
    if domain:
        (SITE / "CNAME").write_text(domain + "\n", encoding="utf-8")
        print(f"  wrote CNAME ({domain})")

    # Make the PDF downloadable from the site. Copy an existing one in now; if we are
    # about to (re)generate it, make_pdf copies the fresh one too.
    pdf_name = (cfg.get("pdf") or {}).get("filename") or "portfolio.pdf"
    root_pdf = ROOT / pdf_name
    if root_pdf.exists():
        shutil.copy2(root_pdf, SITE / pdf_name)
    pdf_href = pdf_name if (render_pdf or root_pdf.exists()) else None

    # Timeline / index
    (SITE / "index.html").write_text(
        env.get_template("index.html").render(
            cfg=cfg, projects=projects, pdf_href=pdf_href
        ),
        encoding="utf-8",
    )

    # One page per project
    for i, proj in enumerate(projects):
        (SITE / f"{proj['slug']}.html").write_text(
            env.get_template("project.html").render(
                cfg=cfg,
                p=proj,
                prev=projects[i - 1] if i > 0 else None,
                next=projects[i + 1] if i < len(projects) - 1 else None,
            ),
            encoding="utf-8",
        )
        print(f"  built {proj['slug']}.html")

    # Print view: the PDF source
    include = (cfg.get("pdf") or {}).get("include") or []
    pdf_projects = (
        [p for slug in include for p in projects if p["slug"] == slug]
        if include
        else [p for p in projects if p.get("featured")]
    )
    (SITE / "print.html").write_text(
        env.get_template("print.html").render(cfg=cfg, projects=pdf_projects),
        encoding="utf-8",
    )
    print(f"  built print.html ({len(pdf_projects)} projects)")

    if render_pdf:
        make_pdf(cfg)

    print(f"\nSite ready: {SITE / 'index.html'}")


def make_pdf(cfg):
    out = ROOT / (cfg.get("pdf", {}).get("filename") or "portfolio.pdf")
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print(
            "\n  Playwright not installed, so the PDF was not generated automatically."
            "\n  Either run:  pip install playwright && playwright install chromium"
            "\n  Or open docs/print.html in your browser and use Print > Save as PDF."
        )
        return
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.goto((SITE / "print.html").as_uri(), wait_until="load")
        # KaTeX typesets synchronously while print.html parses, so it is done by load.
        # Wait on the font set rather than a fixed delay: a slow network used to lose
        # the race and silently produce a PDF in fallback fonts.
        page.evaluate("() => document.fonts.ready")
        # document.fonts.check() is no good here: it reports success for a family with
        # no @font-face at all, so a blocked stylesheet looks fine. Count loaded faces.
        missing = page.evaluate(
            """() => ['IBM Plex Sans', 'IBM Plex Serif', 'IBM Plex Mono'].filter(
                 f => ![...document.fonts].some(
                   ff => ff.family.replace(/["']/g, '') === f && ff.status === 'loaded'))"""
        )
        if missing:
            print(f"  ! {', '.join(missing)} did not load; PDF will use fallback fonts")
        page.pdf(
            path=str(out),
            format="Letter",
            print_background=True,
            margin={"top": "0.6in", "bottom": "0.6in", "left": "0.65in", "right": "0.65in"},
        )
        browser.close()
    # Mirror into docs/ so the website's download link serves the fresh PDF.
    shutil.copy2(out, SITE / out.name)
    print(f"  built {out.name}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", action="store_true", help="also render the PDF")
    ap.add_argument("--serve", action="store_true", help="serve the site locally")
    args = ap.parse_args()

    print("Building portfolio...")
    build(render_pdf=args.pdf)

    if args.serve:
        print("\nServing at http://localhost:8000  (Ctrl+C to stop)")
        subprocess.run([sys.executable, "-m", "http.server", "8000", "-d", str(SITE)])


if __name__ == "__main__":
    main()
