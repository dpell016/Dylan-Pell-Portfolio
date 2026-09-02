---
slug: turbopump
title: Project Turbopump
subtitle: Electric-drive propellant pumps, from first principles to first prints
tag: TM-01
role: Sole designer
org: Personal project
period: 2026 - Present
status: active
order: 2
featured: true
summary: >
  A self-directed design of the pump end of a rocket turbopump for Clementine's 8.8 kN
  ethanol/LOX engine, driven electrically for now with turbine drive as a later phase. I
  took it from engine data sheets to a full first-cut LOX pump, a reusable sizing tool, and
  the first 3D-printed hardware, deriving every number from first principles and logging
  every decision, correction, and mistake along the way.
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
and ethanol to move them through the system. It works, but the gas and the vessels that hold
it are dead weight, and tank pressure caps how hard I can run the engine. I wanted to know
if I could pump instead. Two small motor-driven pumps, one per propellant, that add the
pressure actively instead of storing it. That is the electric pump-fed idea, the one Rocket
Lab flies on Rutherford, and I wanted to see if I could design it myself. So I started a
personal project, branched it off Clementine, and worked backward from the engine: an 8.8 kN
ethanol/LOX engine running 600 psig chamber pressure.

One point of precision, because a good reviewer will check it: a "turbopump" strictly means
a pump spun by a turbine. What I designed is the pump end, which is identical either way,
driven by an electric motor for now. Turbine drive is a planned later phase. I keep the name
Project Turbopump because that is where it is headed.

## Constraints

- **First principles, alone.** No team, no inherited design. If I could not derive a number
  and cite where the method came from, I did not use it.
- **Cryogenic oxygen service.** LOX is not water. Material compatibility, cavitation, and
  cleanliness all come with it, held to oxygen-service standards (CGA G-4.1, ASTM G93).
- **Buildable and testable by one student.** The design had to end in parts I could print or
  machine and actually spin, on a student budget, not a report that stops at a render.
- **A logbook, not a highlight reel.** Every decision, correction, and dead end gets written
  down as it happens. Eighteen sessions and counting.

## Deriving the requirements

Everything starts at the engine. From thrust and specific impulse I worked back to mass
flow,

$$ \dot{m} = \frac{F}{I_{sp}\,g_0} $$

and from there to what each pump has to deliver: 441 m of head on the LOX side and 806 m on
the ethanol, which also has to feed the regen jacket, at 1.86 and 1.68 L/s, for 30 to 44 kW
of shaft power. The first useful result was not a calculation, it was a catch. My
first-principles mass flow disagreed with the data sheet I was handed, and the reason was a
units-label error on the sheet: it read lbm/s for a number that was really kg/s. That set
the rule for the whole project. Derive it myself, then trust it.

## The architecture, and why

Three calls shaped everything downstream, and I made each to defend, not to assume.

**Electric drive, not a gas-generator turbine.** A real turbopump burns propellant to spin a
turbine. For one person to build and control, a motor is far simpler, and it flies now, so I
get the simplicity without the hand-waving. The pump end carries straight over to a turbine
later, so nothing here is wasted.

**Two independent pumps, one per propellant,** instead of one shaft driving both. LOX and
ethanol want different speeds and behave differently, and splitting them kills a whole class
of compromise.

**No inducer.** My NPSH analysis was the make-or-break of the project. LOX comes in at
90.2 K, which is its boiling point at one atmosphere, so at ambient tank pressure the suction
margin is actually negative and the pump would flash to vapor before it did any work. The
textbook fix is an inducer, a little screw ahead of the impeller, and it is also the hardest
part to machine. Instead of adding it, I turned the finding into a hard requirement, pad the
LOX tank to 3 to 4 bar, and deleted the riskiest part of the pump. I spent tank pressure to
buy the margin back.

## The LOX pump

The first-cut LOX impeller is a 20,000 rpm, 83.6 mm semi-open centrifugal wheel: six blades,
25 degrees of backsweep, Wiesner slip, and an inlet eye sized to hold off cavitation,
closing self-consistently to the 441 m the engine needs. I went semi-open because a closed
impeller with 1.4 mm internal passages is neither machinable nor inspectable at student
level, and inspectable matters when the oxygen-cleanliness rules make me verify every wetted
surface.

The number that scared me was axial thrust, near-discharge pressure on the back of the
impeller trying to shove the rotor into its housing. My first pass put it around 8 kN. A
later self-audit against my sizing tool caught that I had integrated the pressure over the
wrong radius, and the real figure is closer to 15 kN. Either way the fix holds: a back wear
ring plus six balance holes bleed the back face down and drop the residual to a few hundred
newtons, which an angular-contact bearing pair carries easily. I sized the shaft for a first
bending critical near 66,000 rpm, a 3.3x margin over running speed.

The whole pump is parametric CAD in Python (CadQuery), so every part regenerates from the
inputs and exports to STEP and STL. Change one number and the pump redraws. I also built a
pump sizing tool in a spreadsheet, a few hundred live formulas, that runs the entire chain
from engine data to impeller geometry, cavitation margin, and the minimum tank pressure, and
flags when a design lands in the un-machinable corner. It reproduces this pump exactly, and I
can point it at any pump I design next.

## Where the design fought back

This is the part I most want to show, because it is where the engineering actually happened.

- **The ethanol pump passed every analysis, then failed at the drawing board.** On paper it
  closed. In geometry, its very low specific speed drove the impeller exit width to 0.7 mm,
  too narrow to machine or to flow cleanly. I did not force it. I laid out three escape
  routes, spin it faster, split it into two stages, or switch to a partial-emission design,
  and gated the choice on which motor I can actually buy.
- **I found a cheap motor that looked perfect and rejected it.** A hundred-dollar NEMA 17,
  until a power-balance check, $P = \tau\,\omega$, showed it was about 200 times undersized.
  The useful part was the one-line rule I pulled out of it, so now I can size any motor
  before spending a cent. The real target is 8 to 9 N·m continuous, an eVTOL-class inrunner.
- **I keep catching my own work with a second method.** Re-optimizing the inlet eye
  invalidated a blade wrap angle I had already called done, so I redid it. A self-review of
  the first CAD caught a volute sized 2.6 times too big for the flow. And the thrust-radius
  error above came out of auditing the design doc against my sizing tool. None of them
  shipped, because I check every number twice.
- **The first 3D prints caught three bugs the math never would have.** When I printed the
  parts and dry-fit them, I found a discharge bore that stopped just short of breaking
  through the casing wall and pointed against the swirl, a bearing housing I had never
  actually modeled, and the worst one: the impeller perched on its own blade tips because I
  had cut a flat pocket floor against blades that taper from 8 mm tall at the eye to 1.4 mm
  at the rim. In a semi-open pump the stationary wall has to be contoured to the blade
  profile; it is part of the flow passage, not a lid. All three are fixed in the current CAD.
  Holding the part in your hand finds what the screen hides.

## Validation

I cannot hot-fire a LOX pump in a garage, so I wrote a water-similarity test program to prove
the design safely. It runs the pump on water and scales the results with the affinity laws,
collapsing head and flow onto their dimensionless coefficients so that water data predicts
the LOX behavior. Staged the right way it needs only about 4% of full power, the same route
ESA and published LOX/methane electric-pump programs use to de-risk on the bench. I wrote the
procedure with abort criteria and containment from the start, and priced the whole rig at
roughly 600 to 1,100 dollars in parts.

## Status and what is next

I am keeping this honest about where it stands. The LOX pump design, the sizing tool, and the
test program are done, and I have the first 3D-printed parts in hand and dry-fitting, which
is where the last three bugs came from. Nothing is in metal yet, and the ethanol pump has one
open decision waiting on which motor I source. Next is sourcing the drive, correcting the
prints, machining the first aluminum, and running the water test. Every number traces to a
derivation and every decision to a logbook entry, so this is built to be picked up and pushed
forward, not admired as finished.
