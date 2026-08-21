---
slug: copv
title: Composite Overwrapped Pressure Vessel Study
subtitle: Carbon fiber overwrap testing for higher tank pressure
tag: ST-01
role: General Member
org: Highlander Space Program, UC Riverside
period: 2024 - 2025
status: complete
order: 7
featured: true
summary: >
  Designed two bulkheads and a drill jig in SolidWorks to cap a small test pressure
  vessel, then worked with two teammates to assemble it and overwrap it in carbon fiber,
  studying how much a COPV could raise allowable tank pressure for Project Poseidon.
skills:
  - SolidWorks
  - Pressure vessel design
  - Carbon fiber composites
  - Composite layup
  - Design for manufacture
hero: copv/hero.jpg
hero_caption: Assembling the COPV test vessel.
images:
  - file: copv/bulkheads.jpg
    caption: The two bulkheads I designed in SolidWorks to cap the test vessel.
  - file: copv/layup.jpg
    caption: Wrapping carbon fiber around the test vessel.
  - file: copv/assembly.jpg
    caption: The assembled overwrapped test article.
---

## The problem

Project Poseidon fed its engine from pressurized propellant tanks. Higher tank pressure
raises chamber pressure, and higher chamber pressure raises thrust. What limits tank
pressure is the tank wall itself: push a metal vessel too far and the wall stress reaches
the material's yield point. You can allow more pressure by making the wall thicker, but
that adds weight the vehicle then has to carry all the way up.

The question our small group set out to answer was whether a composite overwrapped
pressure vessel, a COPV, could hold higher pressure without that weight penalty. I joined
the effort as a general member.

## Constraints

- **General-member role.** I was not leading this. I owned the CAD, and I shared the
  build and test with two teammates.
- **Student fabrication.** The test vessels, bulkheads, and tooling all had to be things
  we could machine and assemble ourselves.
- **A process we were still learning.** None of us were experienced with carbon fiber
  layup, so getting the process right was part of what we were testing rather than
  something we could assume.
- **Pressurized test article.** Anything that holds pressure is a hazard, so the parts
  had to be built and handled with that in mind.

## Design decisions

### Why a composite overwrap instead of a thicker metal wall

A thin-walled pressure vessel carries a hoop stress that grows with pressure and radius
and falls with wall thickness,

$$ \sigma_h = \frac{p\,r}{t} $$

To allow more pressure in an all-metal vessel you raise $t$, and that adds mass around the
entire vessel. A COPV takes a different route. A thin metal liner holds the gas and
provides the seal, while a carbon fiber overwrap carries most of the pressure load in
tension. Carbon fiber has a very high strength for its weight, so the overwrap buys
pressure capacity for far less mass than the equivalent metal would. That trade is the
reason COPVs are used on flight vehicles in the first place.

### Capping the vessel with bulkheads and a drill jig

To turn a plain section of tube into a vessel we could actually pressurize, both ends had
to be closed. I designed two bulkheads in SolidWorks to cap the ends of a smaller test
vessel, and a drill jig to locate the fastener holes.

The jig was the part that mattered most. The holes in the bulkhead have to line up with
the holes in the vessel, and drilling them by hand without a guide would not hit the same
pattern twice. Locating them with tooling instead of by eye is the same reasoning I used
again later on the [Bulkhead Drill Jig](drill-jig.html) for Poseidon.

### Building the overwrap by hand

With the vessel assembled, we wrapped carbon fiber around one of the two test vessels and
left the other bare as a reference. The goal was to learn the process directly: how the
fiber is tensioned and oriented, how the layup goes down, and how the overwrapped vessel
behaves under pressure compared to the bare one.

## What I built

Two bulkheads and a drill jig, all designed in SolidWorks, that turned a small tube into a
sealed, testable pressure vessel. Working with two teammates, I helped assemble the
vessels and overwrap one of them in carbon fiber to make the COPV test article.

## Validation

We pressurized both articles and compared the bare vessel against the carbon fiber
overwrapped one, so we could see directly how much pressure capacity the overwrap added
rather than estimating it. That comparison, together with what it took to build and handle
a COPV as a student team, is what the program used to weigh whether a COPV belonged on
Poseidon.

## What I would do differently

I would instrument the pressure test more heavily. We compared the two articles, but with
more measurement across the wall we would have understood how the overwrap carried load,
not only the point it reached, and we would have had data to design the next article
against.

The more honest lesson is about what the project was really for. We did not end up putting
a COPV on Poseidon. What we kept was the carbon fiber capability: we used what we learned
about composite layup to build lightweight housings for the fluid components exposed
underneath the pressure vessel, on the line running to the combustion chamber. The COPV
was the goal we set, but the composites skill was the result we actually carried forward,
and it went on to fly on [Project Poseidon](poseidon.html).
