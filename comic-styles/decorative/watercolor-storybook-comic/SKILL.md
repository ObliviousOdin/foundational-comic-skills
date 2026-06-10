---
name: watercolor-storybook-comic
version: 2.0.0
category: comic-styles
description: Loose transparent watercolor storybook comics — visible pencil underdrawing, deliberate blooms, paper-white as the light source, and hand-wobble borders for tender, wonder-struck moments.
---

# Watercolor Storybook Comic

**Style Lock (do not deviate)**

- Loose transparent watercolor washes on cold-press paper; granulation and paper tooth visible in every wash
- **Deliberate blooms and bleeding edges**: back-runs and color creeping past contours are features, placed where softness serves the beat — never simulated with digital blur
- **Graphite pencil underdrawing left visible** beneath the washes — light, searching lines, slightly off-register from the paint
- **Paper-white as the light source**: highlights are reserved unpainted paper; no white paint, no digital white, no rendered glow
- Soft wet-in-wet skies and backgrounds; crisper wet-on-dry edges reserved for the focal subject only
- **Restrained palette per spread**: 3–4 pigments mixed throughout (e.g., ultramarine, burnt sienna, yellow ochre, one rose), locked before painting begins
- **Hand-wobble borders or borderless vignettes**: panel edges drawn freehand or dissolved into the paper margin; nothing ruler-hard anywhere

## Negative Locks

- No digital gradients, airbrush smoothness, or vector-clean linework
- No opaque flat fills or heavy black ink outlines
- No full-spectrum saturated palettes; no neon hues
- No hard-ruled mechanical panel borders or glossy rendering
- No grim textures — grime, gore, harsh cast shadow — anywhere in the register

## When to Use

- Gentle wonder, small kindnesses, child-and-creature tales, quiet seasonal moments
- Reference images cueing softness, nature, morning light, or picture-book warmth
- Wordless or near-wordless strips where atmosphere carries the story — this is the native `silent-strip` style

## When Not to Use

- East Asian brush-and-ink lyricism → use `ink-wash-storybook-manga`
- Ornament-driven elegance and poster composition → use `elegant-art-nouveau-comic`
- Bright flat-color kids' energy and gags → use `saturday-morning-cartoon-comic` or `chibi-kawaii-comic`

## Story Harness (Image-Driven)

- Translate the four cues into one small discovery in a large soft world — stakes no heavier than a held breath
- **SETUP**: wide, airy establishing vignette — wet-in-wet sky holding most of the panel, the small figure grounded by a few crisp wet-on-dry touches; plant the inciting wonder (a glow between trees, a paper boat, an unfamiliar footprint)
- **REINFORCE**: the approach — the figure moves toward the wonder; color deepens within the locked pigments, blooms gather where the mystery sits; exactly one crisp detail sharpens the object of attention
- **TURNAROUND**: **tender and wonder-struck** — the discovery is met, not explained; never ironic, never loud; the strip's largest reserve of paper-white surrounds the meeting so the light itself answers; borderless vignette preferred

## World Guardrail

- Default settings: meadows, woodland paths, window seats, garden ponds, attic corners, lantern-lit evenings — storybook-rural and season-forward
- Props natural or handmade: paper boats, wicker baskets, teacups, scarves, jam jars; technology ends at the bicycle and the postage stamp
- Creatures may be gently fantastical (a polite fox, a moss spirit) so long as they obey the palette lock

## Dialogue & Lettering

- Default toward silence; when words appear, small hand-lettered text in airy bubbles whose outlines wobble like the borders — per `comic-lettering-and-balloons`, these are the only deltas; caption boxes remain forbidden — the wash is the narrator
- ≤ 1 bubble per panel, ≤ ~8 words
- SFX policy: none lettered; sound is shown (ripples, scattered birds, tilted grass), never spelled

## Direction Notes

- Camera diet: wide and medium-wide so air and paper can breathe; one gentle close-up at the turnaround; no dramatic angles — the horizon stays level
- Transition diet: aspect-to-aspect and subject-to-subject — this style walks, it never cuts hard; `silent-strip` runs lean on aspect-to-aspect chains
- Pacing: soft, wide gutters of raw paper; panels may share one bled wash across the gutter when time flows continuously; the final vignette receives the most margin

## Consistency Notes

- **What drifts first**: palette creep — new pigments sneaking in panel by panel — and edge character hardening toward digital cleanness; lock the 3–4 pigment set and a "blooms are features" note in `comic-style-memory-system`
- Pencil underdrawing visibility fades under iteration; verify graphite reads in every panel
- Paper texture and granulation must match across panels (one paper, one sitting); re-anchor against the canonical sheet every 6–8 panels
- Character silhouettes may simplify safely — it is the wash behavior, not the drawing, that must stay identical

## Prompt Block

```text
Loose transparent watercolor storybook comic style, soft washes on
cold-press paper with visible granulation, deliberate blooms and
bleeding edges, light graphite pencil underdrawing showing through,
highlights reserved as unpainted paper white, wet-in-wet skies with
crisper wet-on-dry focal details, restrained three-to-four pigment
palette, hand-wobbled panel borders and borderless vignettes fading
into the page margin, gentle picture-book warmth.
```

## Style Quality Gates

- [ ] Pigment count per spread ≤ 4 and matches the project lock
- [ ] Highlights are reserved paper — no white paint or digital white anywhere
- [ ] Pencil underdrawing visibly present beneath the washes in every panel
- [ ] At least one deliberate bloom or bleed per panel, placed with intent (not uniform noise)
- [ ] No ruler-hard border or digital-clean edge anywhere in the strip

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal`; patterns `silent-strip`, `setup-reinforce-turnaround`, `kishotenketsu`

---

*Leave the light unpainted: paper remembers it better than pigment can.*
