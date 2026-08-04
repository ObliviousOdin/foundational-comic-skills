---
name: reportage-comics-journalism
version: 2.0.0
category: comic-styles
description: Drawn nonfiction in the alternative-press reportage tradition — dense pen-and-ink crosshatch, researched specificity, unidealized faces, and caption boxes that carry observed fact rather than invented interiority.
---

# Reportage Comics Journalism

**Style Lock (do not deviate)**

- Comics-journalism reportage in the alternative-press documentary tradition — **drawn nonfiction**, not fiction rendered in a gritty finish
- Black pen-and-ink on white; **every tone value built from variable crosshatch, contour hatch, and stipple** — density carries value, never a wash or a tone sheet
- Line weight varies by **observation, not decoration**: heavier contour on the near witness, finer nib as detail recedes
- **Researched specificity is the lock** — architecture, vehicles, uniforms, signage, terrain, and dress drawn from reference rather than invented from genre memory
- Unidealized faces: asymmetric features, real body ranges, visible age and fatigue; nobody is drawn handsome by default
- Environments cluttered and lived-in — wiring, rubble, laundry, litter, worn paint; an empty background reads as a place nobody visited
- Thin hand-ruled rectangular borders on an irregular but dense grid (6–9 panels per page in chapter work)
- Reportorial caption boxes are **structural to the form**, not an optional garnish — the narrating voice is part of the style

## Negative Locks

- No screentone, grey wash, halftone dots, or digital gradients — value is hatched or it is absent
- No idealized or symmetrical faces, heroic anatomy, or glamour lighting
- No empty, generic, or placeless backgrounds; a panel that could be anywhere has failed in this style
- No color by default — monochrome ink unless the project contract explicitly grants a spot-color pass
- No cinematic genre lighting: rim light, lens flare, god-rays, or dramatic underlighting
- **No fabricated documentary detail** — invented insignia, made-up signage, or plausible-looking evidence that no source supports

## When to Use

- Nonfiction and testimony-driven work: field reporting, oral history, labor and infrastructure stories, process-and-place explainers
- Reference images showing real, specific, worn places and ordinary bodies at work
- When credibility is the contract — the reader must be able to trust that what is drawn was observed

## When Not to Use

- Interior memoir, hindsight, and personal feeling → use `autobio-indie-literary-comic`
- Mood-first painted atmosphere → use `painted-prestige-comic`
- Clean pictographic reduction → use `minimalist-line-webcomic`

## Story Harness (Image-Driven)

- Translate the four cues into an **observed sequence** — a place, a practice, and what the practice costs. The strip reports; it does not resolve
- **SETUP**: wide establishing shot of the real place, dense with specific detail; the subject at work inside it, scale and conditions legible at a glance
- **REINFORCE**: move closer — hands, tools, a document, a queue, a repair. The complication is *conditions*, never villainy; the camera stays a witness
- **TURNAROUND**: **recontextualization, not a punchline** — a pull-back that shows what surrounded the first panel, or a plainly stated fact in caption. "Earned" means panel 1 now reads differently *and* nothing was invented to get there

## World Guardrail

- Contemporary or recent-historical real world; technology, signage, and dress period-locked and verified against reference
- Specific-feeling but unnamed by default — the Producer's contract decides whether a real place, person, or event is identified
- Weather, damage, and infrastructure drawn as observed conditions rather than atmosphere effects
- When the project depicts real people or events, the world bible carries the source note beside the character entry; unsourced detail is out of bounds

## Dialogue & Lettering

- **Caption boxes are this style's licensed exception** (per comic-lettering-and-balloons, captions are forbidden by default elsewhere): thin-ruled rectangles, dense hand script, ≤ 2 per panel, ≤ ~20 words each
- Captions carry **observed fact, attribution, and context** — never invented interiority for a real subject; a caption that speculates about a mind is a violation, not a flourish
- Speech in small plain ovals with straight tails, ≤ 2 per panel; quoted testimony keeps the speaker's own register and grammar
- SFX policy: near-zero and unglamorous — small lettered ambience (generator hum, rain on tin) at most once per beat

## Direction Notes

- Camera diet: observational middle distance and over-the-shoulder; the frame admits that a witness was standing somewhere
- Eye level is the **ethical default** — heroic low angles editorialize on the subject, and this style does not editorialize with the lens
- Transition diet: subject-to-subject and aspect-to-aspect (aspect carries place, weather, and elapsed time in documentary work); scene-to-scene bridged by a caption
- Pacing: dense regular grid; the recontextualizing beat earns a widened panel and the wider preceding gutter — splash pages are almost always the wrong instrument

## Consistency Notes

- **What drifts first**: hatch density — successive batches lighten until the tone range collapses to mid-grey; pin stroke density per value step in `comic-style-memory-system`
- Faces drift second, toward symmetry and attractiveness; re-anchor against the canonical sheet every 6–8 panels and re-assert the unidealized lock explicitly
- Background specificity decays into generic rubble and repeated props; re-inject the reference set every batch
- Caption-box ruling weight and script size drift across a chapter — lock them as fixed art assets, not per-panel decisions

## Prompt Block

```text
Comics-journalism reportage style, black pen-and-ink on white paper,
dense variable crosshatch and stipple building every tone value, no
screentone and no grey wash, observational documentary drawing with
researched architecture, vehicles, and clothing, unidealized faces
with specific asymmetric features, cluttered lived-in environments
showing visible wear, thin hand-ruled rectangular panel borders,
thin-ruled caption boxes in dense hand script, small plain oval
balloons, alternative-press ink-on-newsprint print feel.
```

## Style Quality Gates

- [ ] Every tone value hatched or stippled — zero wash, screentone, or gradient at 200% zoom
- [ ] Every background carries at least three specific, non-generic observed details
- [ ] Faces asymmetric and unidealized; no glamour pass survived the batch
- [ ] No fabricated documentary detail — every insignia, sign, and document traces to a source note in the world bible
- [ ] Every caption adds fact, attribution, or context; none restates what the panel already shows

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `multi-page-chapter` or `3-panel-horizontal`; patterns `parallel-action`, `slow-burn-reveal`

---

*Draw only what was seen — in reportage, the hatching is the argument that someone was standing there.*
