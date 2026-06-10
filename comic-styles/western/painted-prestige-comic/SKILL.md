---
name: painted-prestige-comic
version: 2.0.0
category: comic-styles
description: Fully painted prestige-format comic — gouache/oil realism in the Alex Ross tradition, no ink outlines, classical portrait lighting, and monumental history-painting staging for reverent stories.
---

# Painted Prestige Comic

**Style Lock (do not deviate)**

- Fully painted rendering (gouache/oil feel) — **no ink outlines anywhere**; every edge resolves through value and color, the painter's contract
- Realistic anatomy and fabric weight; figures lit like **classical portraiture** — one dominant key light, warm museum glow, honest falloff
- Controlled naturalistic palette with soft atmospheric depth; color shifts are mixed on the brush, never filtered on
- Panel compositions staged like **history paintings**: dignified, monumental framing — heroes at human scale, witnessed rather than exaggerated
- Visible brush evidence at close range — soft blends, opaque gouache passages, dry-brush texture on fabric and stone
- **Hand-painted caption boxes** (cream or parchment plates) and restrained lettering; no screentone, no flat fills
- Alex Ross-tradition prestige-format finish: gallery-grade realism in service of sequential storytelling

## Negative Locks

- No ink outlines, contour lines, or cel-style edge strokes — a line-drawn edge breaks the style
- No flat fills, Ben-Day dots, screentone, or graphic color zones
- No speed lines, impact stars, or cartoon emotion grammar; motion lives in pose and composition
- No neon, oversaturated, or stylized digital palettes; light stays plausible
- No plastic 3D-render smoothness or photo-collage texture — the surface is paint

## When to Use

- Mythic, reverent, or retrospective stories — heroes seen as history, legacies weighed, eras remembered
- Reference images whose mood cues suggest gravity, nostalgia, awe, or quiet grief
- When the reader should slow down and study panels the way they study paintings

## When Not to Use

- Kinetic action that wants energy effects and bleeds → use `silver-age-pop-comic`
- Four-color pulp sincerity on newsprint → use `golden-age-superhero-comic`
- Soft, lyrical washes for gentle tales → use `watercolor-storybook-comic`

## Story Harness (Image-Driven)

- Translate the four cues into a **weighty moment seen from history's distance** — a vigil, a return, a reckoning, a legacy changing hands
- **SETUP**: monumental establishing — the figure placed in a real, light-filled environment; composition formal, key light declared, the question posed by what the figure regards
- **REINFORCE**: move into portrait range — hands, gaze, the held object; `slow-burn-reveal` logic, with lighting and composition quietly converging on the hidden truth
- **TURNAROUND**: **reverent or bittersweet** — the revelation reframes what the figure means; "earned" means the key light and staging were pointing at the truth from panel one; never a cheap shock

## World Guardrail

- Default to plausible civic and historical spaces: museum halls, memorial steps, city avenues at golden hour, farmhouse kitchens, hangars and chapels
- Props carry material truth — worn leather, brushed steel, folded cloth rendered with weight; costume treated as real tailored fabric
- Era ranges mid-century to present; the fantastic is grounded by daylight physics

## Dialogue & Lettering

- Inherits comic-lettering-and-balloons defaults; deltas: sparse, formal, caption-led
- Hand-painted caption plates carry narration; balloons are clean ovals used sparingly so the paint stays unobstructed
- 1–2 text elements per panel maximum, ≤ 14 words; silence is a prestige instrument
- SFX policy: effectively forbidden — sound is implied by light and gesture, not lettering

## Direction Notes

- Camera diet: formal frontal portraiture, low monument angles for awe, wide establishing shots for context; movement between panels is deliberate
- Transition diet: scene-to-scene and subject-to-subject; moment-to-moment only when a gesture must be witnessed in stages
- Pacing: wide gutters, large panels, generous dwell time; the reveal merits a full-page or near-full-width painting
- Stage figures as tableau — overlapping witnesses, depth through atmosphere, eyelines converging on the meaning

## Consistency Notes

- **What drifts first**: faces — painted realism is unforgiving of likeness drift; lock likeness anchors via `comic-character-consistency-system` and re-anchor every 4–6 panels
- Palette temperature and key-light direction drift second; pin both in `comic-style-memory-system` as the project's lighting grammar
- Brush granularity must stay constant — panels that sharpen into photo-render or soften into mush both fail
- Negative block above merges with character negatives via the world bible — never hand-edit merged output

## Prompt Block

```text
Fully painted prestige comic style in the Alex Ross tradition,
gouache and oil realism with no ink outlines, edges resolved by
value and color, classical portrait lighting with a single warm key
and museum glow, realistic anatomy and heavy fabric weight,
monumental history-painting composition, soft atmospheric depth,
controlled naturalistic palette, visible brushwork and dry-brush
texture, hand-painted caption plates, restrained formal lettering,
gallery-grade painted finish.
```

## Style Quality Gates

- [ ] Zero contour lines — every edge made by value or color difference
- [ ] One consistent key light per scene; shadows obey it in every panel
- [ ] Faces hold likeness across panels at painted-realism fidelity
- [ ] Palette stays controlled and naturalistic — no neon or filter-grade shifts
- [ ] Caption boxes read as hand-painted plates, not digital rectangles

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `multi-page-chapter`; patterns `slow-burn-reveal`, `setup-reinforce-turnaround`

---

*Prestige painting asks the reader to believe the hero once stood still for a portrait.*
