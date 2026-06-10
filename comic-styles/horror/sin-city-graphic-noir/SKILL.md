---
name: sin-city-graphic-noir
version: 2.0.0
category: comic-styles
description: Frank Miller Sin City graphic noir — absolute black-and-white shape design with one locked spot color, white-on-black reversals, and rain-slicked silhouettes for brutal hard-boiled crime.
---

# Sin City Graphic Noir

**Style Lock (do not deviate)**

- Frank Miller Sin City graphic noir: **ABSOLUTE black and white** — zero grays, zero gradients; every tone is a drawn shape, not a value
- **ONE optional spot color per project**, chosen once and locked in the world bible; it marks exactly one subject (a dress, blood, eyes) and nothing else
- **White-on-black reversal panels**: night and dread scenes flip to white line and shape on solid black fields
- Core vocabulary: rain as white slashes, venetian-blind shadow bars, full-silhouette figures — at least one of the three working in every scene
- Chiseled, chunky figures: heavy jaws, slab shoulders, blocky hands; anatomy carved in shapes, never modeled in tone
- Hand-bordered panels with rough brushy edges; borders may break for violence
- Negative space does the rendering: a face can be three white shapes on black and must still be the same face

## Negative Locks

- No gray values, screentone, halftone, or hatched mid-tones pretending to be gray; no gradients of any kind
- No second accent color — if the spot color is unset in the bible, the project is pure black and white
- No soft lighting, bloom, lens blur, or photographic texture
- No clean ruled vector borders or slick uniform digital line
- No delicate fashion-figure anatomy; figures are carved and heavy

## When to Use

- Hard-boiled crime, vengeance, brutal moral clarity, last-stand stories
- Reference images with extreme contrast or one dominant accent hue
- When silhouettes alone can carry the storytelling beat for beat

## When Not to Use

- Atmospheric grayscale mood with soft single-source light → use `noir-expressionist-comic`
- Supernatural slow dread or twist-horror → use `junji-ito-body-horror` or `horror-ec-comics-style`
- Four-color heroics and rescue optimism → use `golden-age-superhero-comic`

## Story Harness (Image-Driven)

- Translate the four cues into a debt: someone owes, someone collects, and the cost is shown
- **SETUP**: establish the figure and the wound (literal or moral) in one stark composition — silhouette against rain or blind-bars; clipped first-person caption opens the voice
- **REINFORCE**: pressure builds by reversal — flip to white-on-black as the situation darkens; the locked spot color enters or tightens its grip; shapes get bigger and fewer
- **TURNAROUND**: **earned, brutal honesty** — the cost is paid on-panel or admitted in caption; no consolation, no irony; biggest panel, simplest shapes, the resolution readable in pure silhouette

## World Guardrail

- Default rain-slicked city at night: bars, alleys, docks, penthouses, basement rooms; neon outside, one bare bulb inside
- Hardware stays chunky and analog in feel: revolvers, big sedans, switchblades, payphones — timeless mid-century-to-now noir
- Weather is permanent: rain, or the threat of it; daylight appears only to be lied to

## Dialogue & Lettering

- First-person caption boxes — rough white or black rectangles — carry the voice in clipped, declarative sentences; inherits `comic-lettering-and-balloons`
- Rough-edged bubbles that invert with the field: black-on-white panels take white bubbles, white-on-black panels take black bubbles
- Budget: ≤ 2 caption/bubble elements per panel, ≤ ~12 words; SFX rare — violence is drawn, not lettered (one brutal SFX per strip maximum)

## Direction Notes

- Camera diet: low angles and hard profiles; extreme close-up on eyes through blind-bars; full-figure silhouette wides for arrivals and deaths
- Transition diet: action-to-action and scene-to-scene hard cuts suit the voice; moment-to-moment only to stretch a dying second
- Pacing: thick black gutters; allow one near-abstract panel per strip or page that is pure shape composition
- Design each panel as positive/negative shape first, content second — if the shapes are weak, the panel is weak

## Consistency Notes

- **What drifts first**: grays creep in — anti-aliased edges, soft shadows, halftone residue; the no-gray rule is binary, regenerate on sight
- Spot color discipline: log the hue and its single assignment in `comic-world-bible-system`; any second colored object in any panel is a defect
- Silhouette is identity: lock each character's profile in `comic-character-consistency-system` and run the silhouette test every panel — chunky figures drift toward generic athletic
- Hand-border roughness and rain-slash stroke character are `comic-style-memory-system` assets; keep the edge personality constant

## Prompt Block

```text
Frank Miller Sin City style graphic noir, absolute black and white
with no grays or gradients, all tone carved as solid shapes,
white-on-black reversal night panels, rain as white slashes, venetian
blind shadow bars, full silhouette figures, chiseled chunky anatomy
with heavy jaws and slab shoulders, rough hand-bordered panels, stark
negative-space faces, single locked spot color at most, hard-boiled
crime atmosphere.
```

## Style Quality Gates

- [ ] Every tone is a black or white shape — zero grays, gradients, or halftones (spot color excepted)
- [ ] At most one spot color, matching the bible's locked hue and single assignment
- [ ] At least one white-on-black reversal panel where night or dread peaks
- [ ] Every figure passes the pure-silhouette readability test
- [ ] Panel borders read hand-cut and rough, never ruled

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` or `multi-page-chapter`; patterns `setup-reinforce-turnaround`, `slow-burn-reveal`, `parallel-action`

---

*Sin City treats color as punctuation: one mark, placed once, and the whole page listens.*
