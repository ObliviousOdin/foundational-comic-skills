---
name: horror-ec-comics-style
version: 2.0.0
category: comic-styles
description: 1950s EC horror comic — lush brush inking, gothic underlit dread, four-color pulp palette with acid-green accents, and host-narrated twist tales of ironic comeuppance.
---

# Horror EC Comics Style

**Style Lock (do not deviate)**

- 1950s EC horror anthology comic (Tales-from-the-Crypt era), printed-on-aged-newsprint feel with visible four-color register
- **Lush brush inking** in the Craig/Davis/Ingels lineage: thick-to-thin brush strokes, feathered shadow edges, heavy spot blacks
- Gothic atmosphere stock: crumbling manors, swamps, cemeteries, storm light; heavy rain and shadow texture rendered in brush, never filter
- **Dramatic underlighting** on faces (lit-from-below ghoul light) reserved for dread beats
- Four-color pulp palette with flat fills; **acid greens and sickly purples are dread accents only** — they must not appear before dread does
- **Narration-box driven dread**: a leering host voice frames the tale from tilted caption boxes — the style's signature device
- Slightly exaggerated anatomy under stress: sweating brows, bulging eyes, white-knuckled hands
- Hand-ruled era-true panel borders

## Negative Locks

- No digital gradients, airbrush, glow, or lens effects — color stays flat four-color register
- No photorealism or painterly rendering; the brush line must read everywhere
- No explicit modern gore — horror lands by implication, shadow, and reaction shot (Code-era restraint with EC nerve)
- No clean uniform vector line or sterile digital borders
- No bright heroic primary-color cheer; the palette is pulp, lurid, and weathered

## When to Use

- Cautionary twist tales, ironic comeuppance, gothic anthology horror
- Reference images that read stormy, lurid, vintage, or smugly sinister
- Whenever a narrating host voice would sharpen the dread

## When Not to Use

- Quiet escalating dread with no irony and no narrator → use `junji-ito-body-horror`
- Stark crime contrast or urban moral fog → use `sin-city-graphic-noir` or `noir-expressionist-comic`
- Spooky but kid-safe fun → use `saturday-morning-cartoon-comic`

## Story Harness (Image-Driven)

- Runs `slow-burn-reveal` with an EC moral engine: WITHHOLD hides the sin, HINT gathers the bill, REVEAL is the comeuppance
- **SETUP** (WITHHOLD): introduce the sinner mid-misdeed or smug just after it; host caption opens the tale with relish; storm building in the background, palette still warm
- **REINFORCE** (HINT): consequences gather — shadows lengthen, acid green creeps into one element, underlighting begins on the guilty face; the host caption drips irony the character cannot hear
- **TURNAROUND** (REVEAL): **ironic comeuppance** in the EC twist-ending tradition — the punishment poetically fits the crime; biggest panel, full underlighting, acid palette floods, and the host gets the last leering word

## World Guardrail

- Default mid-century Americana with gothic edges: small towns, swamps, old estates, carnival lots, 1950s cars, rotary phones
- Supernatural agents are permitted and expected (revenants, curses, things in the bayou); they exist to enforce the moral ledger
- Weather is a dread instrument: rain, fog, and lightning escalate with the bill coming due

## Dialogue & Lettering

- Host narration in rectangular, slightly tilted caption boxes, lurid and gleeful in register — one per panel is the spine of the strip; inherits `comic-lettering-and-balloons`
- Bold hand-lettered bubbles; one jagged panic bubble allowed per strip, at the reveal only
- Budget: 1 caption + 1–2 bubbles per panel; SFX brushy and bold (THUMP, CRACK) — maximum two per strip

## Direction Notes

- Camera diet: theatrical medium and medium-wide staging, like a stage play seen from the stalls; the low-angle underlit close-up is reserved for the reveal
- Transition diet: moment-to-moment and subject-to-subject; scene-to-scene only to relocate the dread (per `comic-narrative-patterns`)
- Pacing: captions buy time — let panel 2 linger on gathering consequences; wide gutter before the reveal
- The reveal panel earns the loudest color: flood it with the acid accent and the deepest blacks

## Consistency Notes

- **What drifts first**: palette discipline — acid dread colors leak into setup panels and brush feathering goes mechanically uniform; lock the four-color swatch set and the dread-accent rule in `comic-style-memory-system`
- Underlighting is beat-bound: if a face is ghoul-lit before the turn approaches, regenerate the panel
- Host caption geometry (tilt angle, border weight) is a style-memory asset — identical across the strip
- Stress exaggeration drifts toward full cartoon; re-anchor faces against the `comic-character-consistency-system` DNA sheet each strip

## Prompt Block

```text
1950s EC horror comic style, lush brush inking with thick-to-thin
strokes and feathered shadow edges, heavy spot blacks, gothic stormy
atmosphere, dramatic underlighting on faces, four-color pulp palette
on aged newsprint with flat fills, acid green and sickly purple dread
accents, heavy rain and shadow texture, slightly exaggerated sweating
panicked anatomy, hand-ruled panel borders, tilted narration caption
boxes, vintage horror anthology energy.
```

## Style Quality Gates

- [ ] Brush line variation visible everywhere — no uniform digital stroke
- [ ] Acid dread accents absent from panel 1, dominant at the reveal
- [ ] Underlighting appears only as the turn approaches, never at setup
- [ ] Host caption present and geometrically consistent in every panel
- [ ] The comeuppance reads as poetically earned by the setup sin

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal`; patterns `slow-burn-reveal` (native), `setup-reinforce-turnaround`

---

*Dread is the setup; irony is the payment — and the host always collects.*
