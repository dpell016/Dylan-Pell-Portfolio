---
# Copy this file to add a project. Filename controls order: NN-slug.md
slug: my-project              # used for the page URL: my-project.html
title: Project Name
subtitle: One line describing what it is
tag: XX-00                    # P&ID-style tag shown on the timeline node
role: Your role
org: Organization
period: 2026                  # displayed on the timeline
status: active                # active | complete
order: 99                     # sort order on the timeline (low = newest/top)
featured: true                # include in the generated PDF
summary: >
  Two-line summary shown on the timeline and at the top of the page.
skills:
  - Skill one
  - Skill two
hero: my-project/hero.jpg     # optional; drop file in assets/images/my-project/
results:                      # optional; renders as a results strip
  - label: Outcome
    value: What happened
images:                       # optional; captioned figures on the page
  - file: my-project/photo.jpg
    caption: What this shows.
---

## The problem

What needed to be solved, and why it was not trivial.

## Constraints

- Budget, schedule, manufacturing capability, safety, team.

## Design decisions

The reasoning. This is the section that matters most. State the decision, then why, and
show the governing relation where it applies. Inline math uses $E = mc^2$ and display
math uses double dollars:

$$ \Delta p = f \, \frac{L}{D} \, \frac{\rho v^{2}}{2} $$

## What I built

The deliverable, concretely.

## Validation

How you proved it worked. Test ladder, measurements, comparison against prediction.

## What I would do differently

Honest retrospective. This section signals engineering maturity; do not skip it.
