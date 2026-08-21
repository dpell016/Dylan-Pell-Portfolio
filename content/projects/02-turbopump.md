---
slug: turbopump
title: Project Turbopump
subtitle: Electric-driven propellant pumps to replace pressure-fed feed
tag: TM-01
role: Sole designer
org: Personal project
period: 2026 - Present
status: active
order: 2
featured: true
summary: >
  A personal project branching off Clementine: two electric-motor-driven propellant pumps,
  one per propellant, that add feed pressure actively instead of carrying it as heavy
  pressurant gas. I derived the pump requirements from the engine, chose and defended the
  architecture, designed the LOX pump end to end in parametric CAD, and wrote a
  water-similarity test program to prove it.
skills:
  - Turbomachinery design
  - Requirements derivation
  - Cavitation and NPSH analysis
  - Rotordynamics
  - Parametric CAD (Python / CadQuery)
  - Test planning and safety engineering
---

## The problem

[Project Clementine](clementine.html) is pressure-fed: high-pressure GN2 pushes on the LOX
and ethanol to drive them through the system. It works, but the gas and the vessels that
hold it are dead weight, and tank pressure caps how hard I can run the engine. I wanted to
know if I could pump instead. Two small electric-motor-driven pumps, one for LOX and one
for ethanol, that add the pressure actively rather than carrying it as stored gas. That is
the electric turbopump idea, and in the last few years it has gone from exotic to
flight-proven. So I started a project of my own, branched it off Clementine, and worked
backward from the engine: an 8.8 kN ethanol/LOX engine running 600 psig chamber pressure.

## Constraints

- **First principles, alone.** No team, no inherited design. If I could not derive a number
  and point to a source, I did not use it.
- **Cryogenic oxygen service.** LOX is not water. Material compatibility, cavitation, and
  cleanliness all come with it, held to oxygen-service standards.
- **Buildable and testable by one person** on a student budget. I wanted hardware I could
  actually machine and validate, not a report that ends at a render.
- **A documented trail, not a clean story.** Every decision, correction, and dead end goes
  in a logbook as it happens.

## Deriving the requirements

Everything starts at the engine. From thrust and specific impulse I worked back to mass
flow,

$$ \dot{m} = \frac{F}{I_{sp}\,g_0} $$

and from there to what each pump has to deliver: 441 m of head on the LOX side and 806 m on
the ethanol, at 1.86 and 1.68 L/s, for 30 to 44 kW of shaft power total. The first useful
result was not a calculation, it was a catch. My first-principles mass flow disagreed with
the data sheet I had been handed, and the reason was a units-label error in the sheet. That
set the rule for the whole project: derive it myself, then trust it.

## The architecture, and why

Three calls shaped everything after them, and I made each one to defend, not to assume.

**Electric drive, not a gas-generator turbine.** A real turbopump is spun by burning
propellant. For one person to build and control, an electric motor is far simpler, and it
is flight-proven now, so I get the simplicity without the hand-waving.

**Two independent pumps, one per propellant,** instead of one shaft driving both. LOX and
ethanol want different speeds and behave differently. Splitting them removes a whole class
of compromise.

**No inducer.** My NPSH analysis showed saturated LOX at ambient tank pressure gives
negative suction margin: the pump would flash to vapor at the inlet before it did any work.
The textbook fix is an inducer, a little screw ahead of the impeller, and it is also the
highest-risk, hardest-to-machine part in the pump. Instead of adding it to buy the margin
back, I turned the finding into a hard requirement: pad the LOX tank to 3 to 4 bar. That
fixes it upstream and lets me delete the riskiest part.

## The LOX pump

The first-cut LOX impeller is a 20,000 rpm, 83.6 mm semi-open centrifugal wheel: six blades,
25° backsweep, Wiesner slip factor, and an eye sized to hold off cavitation, closing
self-consistently to the 441 m of head the engine needs. The number that scared me was
axial thrust: 7.8 kN trying to shove the rotor into its housing. I brought it down to about
300 N with a wear ring and balance holes, and checked the shaft for 3.3x rotordynamic
margin so it runs well below its first critical speed. The whole pump is parametric CAD in
Python (CadQuery), so all five parts regenerate from the inputs and export to STEP and STL.
Change one number and the pump redraws.

## Where the design fought back

This is the part I most want to show, because it is where the engineering actually
happened.

- **The ethanol pump passed every analysis, then failed at the drawing board.** On paper it
  closed. In geometry, its low specific speed drove the impeller exit width down to 0.7 mm,
  the classic low-Ns pathology, where the passage gets too narrow to machine or to flow
  cleanly. I did not force it. I laid out three escape routes, spin it faster, split it into
  two stages, or switch pump type, and gated the choice on which motor I could actually buy.
- **I found a hundred-dollar motor that looked perfect and rejected it.** A power-balance check,
  $P = \tau\,\omega$, put it about 200 times undersized. The useful part was not the
  rejection, it was the one-line shopping rule I pulled out of it, so I can size any motor
  candidate before spending a cent. The real target is 8 to 9 N·m continuous, an
  eVTOL-class 15 to 25 kW inrunner.
- **I corrected my own work more than once.** Re-optimizing the impeller eye invalidated a
  blade wrap angle I had already called done, so I redid it, 150° to 201°. A self-review of
  my first CAD caught a volute sized 2.6x too big for the flow, fixed in v1.
- **A design review challenged my blade count.** Instead of defending it, I ran it against
  Pfleiderer's criterion, found the challenge was partly right, and queued a splitter-blade
  experiment rather than win the argument on the spot.

## Validation

I cannot hot-fire a LOX pump in a garage, so I wrote a water-similarity test program to
prove the design safely. It runs the pump on water and scales the results with the affinity
laws, collapsing head and flow onto their dimensionless coefficients, $\psi$ and $\phi$, so
that water data predicts LOX behavior. Staged the right way it needs only about 4% of full
power, the same trick ESA and published LOX/methane electric-pump programs use to de-risk on
the bench. I sized and priced the whole rig at roughly 600 to 1,100 dollars in parts, with
abort criteria and containment written in from the start.

## Status and what is next

I am keeping this honest about where it stands. The LOX pump and its test program are done
on paper and in CAD. The ethanol pump has one open architecture decision waiting on which
motor I source. Nothing is built yet. Next is buying the drive, machining the first parts,
and running Stage A on water. Every number traces to a derivation and every decision to a
logbook entry, so this is built to be picked up and pushed forward, not admired as finished.
