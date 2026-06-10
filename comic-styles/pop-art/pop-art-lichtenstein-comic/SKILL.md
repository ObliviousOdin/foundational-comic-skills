---
name: pop-art-lichtenstein-comic
version: 2.0.0
category: comic-styles
description: Lichtenstein pop art — large fixed-ruling Ben-Day dots, primary red-yellow-blue plus black, thick uniform contours, and melodramatic romance/war-comic close-ups blown to gallery scale.
---

# Pop Art Lichtenstein Comic

**Style Lock (do not deviate)**

- Roy Lichtenstein pop-art idiom (1961–66 canvas era), built from 1950s romance and war comic panels enlarged until the printing shows
- **Large visible Ben-Day dots at one FIXED ruling** project-wide — the dots are subject matter; identical diameter and spacing in every panel
- Palette restricted to **primary red, yellow, blue, plus black and white** — flat, unmixed, unbroken
- **Thick uniform black contour** around every form — mechanical, stencil-clean, no sketch energy
- **Halftone gradients by dot density only**: skin shading, skies, and blushes are dot fields, never smooth blends
- **Melodrama close-ups**: tearful eyes, parted lips, brooding profiles, gloved hands on telephones, fighter-cockpit grimaces
- Period **romance/war-comic framing**: each panel cropped tight, like a single found panel torn from a 1950s page
- Crisp mechanical edges throughout — the surface pretends a printing press made it

## Negative Locks

- No smooth gradients, airbrush, or soft shading — tone changes only by dot density
- No change of dot ruling, diameter, or angle between panels
- No hues outside the primary set plus black and white; no pastels, no earth tones
- No sketchy, organic, or hand-wobbled linework — contours stay thick, even, and mechanical
- No photorealistic rendering or painterly texture; flatness is the point

## When to Use

- Stylized, ironic, or pop-culture stories — heartbreak, longing, and combat played at full volume
- Reference images that support graphic, high-impact, poster-like treatment
- When a single charged moment deserves to be monumentalized — `single-panel-gag` thinking at gallery scale

## When Not to Use

- Sincere 1940s heroics without irony → use `golden-age-superhero-comic`
- Kinetic Kirby-energy action → use `silver-age-pop-comic`
- Gentle everyday humor → use `classic-newspaper-comic`

## Story Harness (Image-Driven)

- Translate the four cues into a **charged melodramatic moment** — a confession, a goodbye, a trigger pulled, a phone unanswered
- **SETUP**: the found-panel frame — a face or gesture cropped tight, emotion already at full volume, a thought balloon loading the inner monologue
- **REINFORCE**: escalate the melodrama straight-faced — closer crop, dot fields reading as emotional weather, the monologue doubling down ("I CAN'T LET HIM KNOW…")
- **TURNAROUND**: **melodramatic irony** — the overwrought feeling undercut, reversed, or revealed as absurd by one cool visual fact; "earned" means panels 1–2 played the sincerity completely straight

## World Guardrail

- Default to early-1960s American romance/war milieux: diners, rotary telephones, venetian-blind interiors, convertibles, fighter cockpits, sunset horizons in dot fields
- Props period-locked and graphic — coffee cups, lipstick, radios, missiles; everything reducible to contour plus flat fill plus dots
- Cast conventions era-true: yellow hair, dot-shaded skin, navy suits, crimson lips

## Dialogue & Lettering

- Inherits comic-lettering-and-balloons defaults; deltas: bold mechanical caps with melodramatic ellipses and exclamation
- Scalloped thought balloons carry overwrought interior monologue — the style's signature text vessel; oval balloons for speech; jagged bursts for war beats
- 1 text element per panel preferred, ≤ 12 words; the monologue IS the melodrama
- SFX policy: one graphic-centerpiece onomatopoeia per strip maximum (WHAAM!-class), composed as art, not garnish

## Direction Notes

- Camera diet: extreme close-up dominant — faces fill the frame; medium shots only to introduce a prop the close-ups will obsess over
- Transition diet: subject-to-subject; each panel built to stand alone as a poster (single-panel logic even inside a strip)
- Pacing: slow, monumental gutters; crop tighter than comfortable; diagonal-cut compositions for war beats
- Steal the framing language of 1950s romance pages: tilted heads, three-quarter profiles, the unseen lover off-panel

## Consistency Notes

- **What drifts first**: dot ruling and palette purity — dots shrink into texture and off-primary hues leak in; fix dot diameter, spacing, and the five-swatch palette in `comic-style-memory-system` and audit every panel
- Contour thickness drifts second; pin the stroke width as a named style asset
- Cast color conventions (hair yellow, eyes blue, lips red) are DNA-level locks via `comic-character-consistency-system`
- Re-anchor against the canonical sheet every 6–8 panels; halftone faces drift toward photoreal shading fast

## Prompt Block

```text
Pop-art comic style in the Roy Lichtenstein tradition, large visible
Ben-Day dots at a single fixed ruling, flat primary red, yellow,
and blue with black and white only, thick uniform mechanical black
contour lines, halftone shading built purely from dot density,
melodramatic 1960s romance and war comic framing, tight close-up
compositions, crisp stencil-clean edges, scalloped thought balloons,
bold caps lettering, monumental printed-panel gallery aesthetic.
```

## Style Quality Gates

- [ ] Dot ruling identical in every panel — same diameter, spacing, and angle
- [ ] Palette audit passes: only primary red, yellow, blue, black, white
- [ ] Contour thick, uniform, and mechanical throughout
- [ ] All tonal transitions made by dot density — zero smooth gradients
- [ ] At least one melodrama close-up carrying the emotional beat

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` or `single-panel-gag`; patterns `setup-reinforce-turnaround`, `gag-escalation`

---

*Blow the panel up until the printing shows — the dots were the painting all along.*
