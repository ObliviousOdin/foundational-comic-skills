---
name: bold-woodcut-adventure
version: 2.0.0
category: comic-styles
description: Lynd Ward / Frans Masereel woodcut-novel style — carved white-on-black strokes, monumental silhouettes, and high-contrast moral light for wordless folkloric adventure.
---

# Bold Woodcut Adventure

**Style Lock (do not deviate)**

- Woodcut / wood-engraving novel style in the **Lynd Ward–Frans Masereel lineage**: relief-print black and white, one block, one ink
- **Carved white-on-black strokes**: every mark reads as a gouge cut removing white from a black block — cut logic, never pen logic
- **Directional gouge texture**: parallel cut bundles follow form and light; texture direction always means something, never random fill
- Strong silhouettes carry the storytelling — every figure must read as a pure black or white shape on its own
- **Monumental simplified figures**: heavy limbs, archetypal faces, gesture over facial nuance
- **High-contrast moral lighting**: light = hope/justice, black mass = threat/oppression, applied consistently from first panel to last
- Slight ink-squeeze edge wobble and print imperfection; each panel feels like one carved plate
- Heavy black panel borders like plate edges

## Negative Locks

- No gray values, washes, or gradients — only carved black and white
- No fine pen crosshatch or delicate contour line; tone is built from cut bundles, not hatching
- No color; the print is one block, one ink
- No photorealistic detail or digital smoothness
- No small-scale facial nuance that breaks the monumental register

## When to Use

- Mythic journeys, folk tales, labor epics, moral fables
- Reference images that read monumental, archetypal, or struggle-and-triumph
- When the strip must work with zero dialogue — `silent-strip` is native (the wordless-novel tradition)

## When Not to Use

- Talky character comedy → use `classic-newspaper-comic` or `underground-zine-comix`
- Atmospheric mid-tone urban noir → use `noir-expressionist-comic`
- Warm color spectacle adventure → use `pulp-adventure-comic`

## Story Harness (Image-Driven)

- Runs `silent-strip` natively: every beat must be readable from posture, silhouette, and light alone — no dialogue crutch exists
- **SETUP**: the protagonist's want stated as pure gesture — a reaching figure, a closed gate, a far light on the horizon; the silhouette introduces the character instantly
- **REINFORCE**: the obstacle grows as black mass; gouge texture steepens and densifies; the figure stands smaller or bent — but the light source persists somewhere in frame
- **TURNAROUND**: **triumphant or folkloric justice** — figure and light unite, or the oppressor is consumed by his own black mass; biggest panel, simplest shapes, the light visibly wins

## World Guardrail

- Default timeless folkloric-industrial world: villages, forests, harbors, factory towns, mountain roads — early-20th-century at its most modern
- Props archetypal: lanterns, axes, looms, bells, ships, hammers; no contemporary technology
- Nature and architecture are moral actors: storms oppress, dawn vindicates, smokestacks loom

## Dialogue & Lettering

- Default **silent**: no bubbles, no captions — meaning is carried by image alone, per the wordless-novel doctrine; inherits `comic-lettering-and-balloons` only for the exceptions
- Exception budget: one carved-style caption per strip maximum (a place name, a single word like STRIKE), lettered as if cut from the block
- SFX policy: none — impact is drawn as radiating cut bundles, never lettered

## Direction Notes

- Camera diet: full-figure wides and monumental low angles; close-ups rare and reserved for the turn, where a face becomes a mask of light
- Transition diet: moment-to-moment and aspect-to-aspect, per the `comic-narrative-patterns` silent-strip law; no dialogue substitutes of any kind
- Pacing: generous gutters — silence needs air; one idea per panel, compositions held simple
- Stage the journey moving left-to-right; reverse the direction only to signal defeat or retreat

## Consistency Notes

- **What drifts first**: gouge-texture direction logic — cut bundles start ignoring form and light and decay into generic hatching; lock the direction rules (follow form, radiate from light) in `comic-style-memory-system`
- Silhouette is identity: lock each figure's silhouette profile in `comic-character-consistency-system`; any panel where a character fails the silhouette test is regenerated
- The light=hope / black=threat moral coding must never flip mid-story; log the assignment in the world bible
- Border weight and ink-squeeze wobble are style-memory assets — keep the print imperfection constant, not random

## Prompt Block

```text
Woodcut novel style in the Lynd Ward and Frans Masereel tradition,
relief print black and white, carved white-on-black strokes,
directional gouge texture following form and light, strong readable
silhouettes, monumental simplified figures with heavy limbs and
archetypal faces, high-contrast moral lighting, slight ink-squeeze
print wobble, heavy black panel borders like plate edges, folkloric
early-industrial world, wordless storytelling clarity.
```

## Style Quality Gates

- [ ] Every mark reads as a carved cut, never a drawn pen line
- [ ] All figures pass the silhouette test in every panel
- [ ] Gouge texture direction follows form or light — no random fill anywhere
- [ ] The strip reads completely with all text removed
- [ ] Light/dark moral coding consistent from first panel to last

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal`; patterns `silent-strip` (native), `setup-reinforce-turnaround`

---

*Every mark is a cut: the light is whatever the knife spared.*
