# Engineering Portfolio — Dylan Encarnacion Pell

Liquid propulsion and fluid systems work, organized as a timeline with the design
reasoning behind each decision.

One markdown source generates both the website and the PDF.

## Setup

```bash
pip install -r requirements.txt
playwright install chromium      # only needed for automatic PDF export
```

## Build

```bash
python3 build.py            # website into docs/
python3 build.py --pdf      # website + Dylan_Pell_Portfolio.pdf
python3 build.py --serve    # build, then http://localhost:8000
```

No Playwright? `build.py` still writes `docs/print.html`. Open it and use
Print > Save as PDF.

## Adding a project

1. Copy `content/projects/_TEMPLATE.md` to `content/projects/07-name.md`
2. Fill in the frontmatter and write the six standard sections
3. Drop photos into `assets/images/<slug>/`
4. Rebuild

## Adding photos

Each project declares its images in frontmatter. Until a file exists at that path the
site shows a dashed placeholder naming the exact path, and the PDF skips the figure.
So you can add photos whenever, in any order, without touching code.

```
assets/images/clementine/hero.jpg
assets/images/clementine/pid.jpg
assets/images/poseidon/pressure-vessel.jpg
...
```

Use JPG or PNG. Roughly 1600px wide is plenty. Landscape works best.

## Publishing

GitHub Pages: push the repo, then Settings > Pages, deploy from branch, folder `/docs`.
The `docs/` folder is committed for this (GitHub Pages only serves from root or docs/).
Then put the URL in `portfolio.yaml` as `site_url` so it appears on the PDF cover.
