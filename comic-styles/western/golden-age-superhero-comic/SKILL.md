---
name: golden-age-superhero-comic
version: 2.0.0
category: comic-styles
description: Golden Age superhero comic (1938–55) — four-color newsprint palette, flat Ben-Day fills, heavy outlines, square-jawed heroic anatomy, and caption-box mythmaking on aged pulp paper.
---

# Golden Age Superhero Comic

**Style Lock (do not deviate)**

- Golden Age American superhero comic, 1938–55 era — the hero as civic myth, drawn for pulp newsprint
- **Four-color process palette**: flat CMYK-limited newsprint combinations (the classic ~64-swatch set); slight off-register charm allowed, but consistent across panels
- **Ben-Day dots and flat fills** for every mid-tone — no gradients, no rendered blends; the sky is one blue, the cape is one red
- Heavy, uniform black outline on every form with **minimal feathering** — a few tapered strokes at muscle and cape shadow, nothing more
- **Square-jawed heroic anatomy**: idealized eight-heads-tall figures, barrel chests, fists like anvils; civilians drawn softer and simpler
- Caption-box era conventions: yellow rectangular narration boxes ("MEANWHILE, ACROSS TOWN…") steering the story
- **Aged newsprint tooth**: warm cream paper, visible pulp grain, ink sitting slightly fat on cheap stock
- Thick hand-ruled rectangular panel borders on a steady grid

## Negative Locks

- No digital gradients, glow, lens flare, or painted rendering — every color is a flat printed shape
- No modern muted or cinematic desaturated palettes; the four-color set is the law
- No manga conventions: no screentone, no speed-line emotion grammar, no oversized eyes
- No gritty crosshatch density or photorealistic faces — those belong to later eras
- No clean bright-white digital paper; the page is warm newsprint, always

## When to Use

- Classic hero-versus-wrongdoer tales: rescues, foiled schemes, masked villains, civic peril
- Reference images that support iconic, idealized treatment — capes, uniforms, determined jaws
- When the story wants sincerity played absolutely straight, with zero irony

## When Not to Use

- Kinetic cosmic action with extreme foreshortening → use `silver-age-pop-comic`
- Ironic, self-aware pop framing → use `pop-art-lichtenstein-comic`
- Painted reverence and realism → use `painted-prestige-comic`

## Story Harness (Image-Driven)

- Translate the four cues into a **wrong to be righted** — a threat, a victim, and a hero whose deed restores order
- **SETUP**: establish the threat with a caption box and a worried civilian or looming villain; the hero present or arriving, low-angle, cape catching wind
- **REINFORCE**: the hero acts — power displayed plainly (lifting, leaping, shielding); action-to-action beats with one bold SFX; the villain's scheme visibly straining
- **TURNAROUND**: **triumphant** — the wrong is righted on-panel, villain foiled, civilians safe; the hero lands an iconic full-figure pose; "earned" means the deed in panel 2 directly causes the victory in panel 3

## World Guardrail

- Default to a 1940s American metropolis: art-deco skylines, newsstands, fedoras and trench coats, prop planes, dirigibles, dockyards
- Technology period-locked — rotary phones, radio towers, getaway sedans; villain gadgetry stays theatrical, not futuristic
- The city is upright and worth saving; weather dramatic but legible (searchlight beams, flat navy night skies)

## Dialogue & Lettering

- Inherits comic-lettering-and-balloons defaults; deltas: hand-lettered caps with bold double-stroke emphasis words
- Yellow caption boxes carry narration and scene shifts; oval balloons with straight tails; jagged burst balloons for shouts
- 1–2 balloons per panel plus an optional caption, ≤ 12 words total; heroes declare, villains gloat
- SFX policy: big hand-drawn onomatopoeia (POW! CRASH!) — one per action beat, colored from the four-color set

## Direction Notes

- Camera diet: low angles for the hero, eye-level for civilians, high angles for peril; full figures favored — the costume is the icon
- Transition diet: action-to-action dominant, with scene-to-scene cuts bridged by caption boxes
- Pacing: steady grid with even gutters; the triumphant beat takes the widest panel; a splash-style entrance is allowed once per chapter
- Eyelines and motion exit right; the hero faces the reader for the final pose

## Consistency Notes

- **What drifts first**: costume detail (emblem shape, belt, boot line) and palette purity sliding toward modern rendering; lock costume DNA in the character template
- Fix the exact four-color swatch set and the off-register offset in `comic-style-memory-system` — drifting registration reads as error, consistent registration reads as era
- Newsprint tooth must match across panels; re-anchor the paper texture with every generation batch
- Re-anchor the hero's face and chest emblem against the canonical sheet every 6–8 panels

## Prompt Block

```text
Golden Age American superhero comic style, 1938 to 1955 era,
four-color process palette within CMYK newsprint limits, flat
Ben-Day dot fills with no gradients, heavy uniform black outlines
with minimal feathering, square-jawed idealized heroic anatomy,
thick hand-ruled rectangular panel borders, yellow caption boxes,
hand-lettered all-caps dialogue with burst balloons, bold printed
onomatopoeia, warm aged cream newsprint texture with slight
misregistration, vintage pulp comic book print feel.
```

## Style Quality Gates

- [ ] Every color resolves to the flat four-color set — zero gradients, zero blends
- [ ] Outline weight heavy and uniform; feathering held to a few tapered strokes
- [ ] Anatomy heroic-idealized, not modern hyper-rendered
- [ ] Newsprint tooth and registration offset consistent across all panels
- [ ] Caption boxes and balloons follow 1940s conventions (yellow narration, burst shouts)

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` or `multi-page-chapter`; patterns `setup-reinforce-turnaround`, `parallel-action`

---

*Golden Age prints the hero as myth — four flat colors, one square jaw, and the register slightly off.*
