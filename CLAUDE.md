# Portfolio project — working notes

Engineering portfolio for Dylan Encarnacion Pell. Mechanical engineering student at UC
Riverside (B.S. expected March 2027), focused on liquid rocket propulsion and fluid
systems. Applying to aerospace and defense roles: Mach Industries, Anduril, Inversion,
Vast, Howmet.

## What this repo is

One content source generates two outputs:

- **Website** — `docs/`, a static site. Timeline on the index, one page per project.
- **PDF** — `Dylan_Pell_Portfolio.pdf`, generated from the same markdown.

Content lives in `content/projects/*.md`. Nothing about a project is duplicated anywhere
else. Add a file, rebuild, and both outputs update.

## Build

```bash
pip install -r requirements.txt      # first time
python3 build.py                     # website only
python3 build.py --pdf               # website + PDF
python3 build.py --serve             # build, then http://localhost:8000
```

If Playwright is unavailable, `build.py` still writes `docs/print.html`. Open it in a
browser and use Print > Save as PDF. Same result.

## Layout

```
content/projects/NN-slug.md   project content + frontmatter (the source of truth)
content/projects/_TEMPLATE.md copy this to start a new project
portfolio.yaml                name, contact, thesis, PDF options
templates/                    Jinja2: base, index (timeline), project, print
assets/css/style.css          design system
assets/css/print.css          PDF-only overrides
assets/images/<slug>/         photos for that project
assets/vendor/katex/          vendored KaTeX (offline math, do not edit)
build.py                      the whole build
docs/                         generated output (safe to delete, regenerated)
```

## Adding a project

1. `cp content/projects/_TEMPLATE.md content/projects/07-thing.md`
2. Fill in the frontmatter. `slug` sets the URL, `order` sets timeline position (low =
   top), `featured: true` includes it in the PDF, `tag` is the P&ID-style bubble label.
3. Write the body using the standard section order below.
4. Put photos in `assets/images/<slug>/` and list them under `images:` in frontmatter.
5. `python3 build.py --pdf`

## Section order for every project

Keep this consistent. It is the reason the portfolio reads as engineering rather than
as a gallery.

1. **The problem** — what needed solving and why it was not trivial
2. **Constraints** — budget, schedule, manufacturing capability, safety, team
3. **Design decisions** — the reasoning, with governing equations where they apply
4. **What I built** — the concrete deliverable
5. **Validation** — how it was proven, measurements against prediction
6. **What I would do differently** — honest retrospective; never omit this

## Writing conventions

- **No em dashes.** Dylan's preference across all his application materials. Use commas,
  periods, or colons.
- First person, plain and direct. Short sentences. No marketing voice.
- State the decision, then the reason, then the equation. Never an equation without the
  reason it mattered.
- Claim only what actually happened. Distinguish projected from realized results. The
  rocket and team won the competition; Dylan built the pressure vessel and feed system.
- Math: `$inline$` and `$$display$$`, rendered by KaTeX at page load.
- Cross-link projects with relative links, e.g. `[Project Poseidon](poseidon.html)`.

## Two hard rules

**Export control.** This is liquid rocket propulsion work. Before publishing new
propulsion design detail publicly, Dylan checks with Highlander Space Program leadership
or the faculty advisor. When in doubt, describe the engineering reasoning and omit
specific dimensions, pressures, and performance figures. Defense employers care that a
candidate understands this boundary.

**Proprietary information.** The SKDLA internship content must stay genericized. Never
add the supplier's identity, real cost figures, or internal process specifics. Describe
the methodology only.

## Design system

Visual language is borrowed from P&IDs and instrument drawings, which is Dylan's actual
domain. Do not replace this with a generic portfolio template.

- `--navy #193E5F` matches his resume and cover letters, so the PDF sits alongside them
- `--cryo #2E7FA6` oxidizer and cryogenic, `--ember #B8431F` hot fire and active work
- IBM Plex Sans (headings), Serif (body), Mono (tags, data, captions)
- Signature element: the schematic spine on the index, with ISA-style instrument bubbles
  carrying each project's tag number. Sequence is real information here, so the timeline
  structure is earned rather than decorative.

## Current state

Six projects written: Clementine, Poseidon, sizing tool, drill jig, FSAE upright,
L'SPACE. Five are in the PDF; L'SPACE is `featured: false`.

**Photos are not in yet.** Every project has image slots declared in frontmatter. Missing
files degrade gracefully: the site shows a dashed placeholder naming the exact path to
drop the file at, and the PDF omits the figure entirely. Adding photos is just copying
files to the right paths.

## Likely next steps

- Add photos to `assets/images/*/`
- Write up the SKDLA internship, genericized (`07-skdla.md`)
- Fill `site_url` in `portfolio.yaml` once hosted, then add the URL to his resume
- Publish with GitHub Pages: push, then Settings > Pages > deploy from `docs/`
