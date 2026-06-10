---
name: manhua-wuxia-comic
version: 2.0.0
category: comic-styles
description: Chinese wuxia manhua — calligraphic brush lines, jewel-tone mineral palette, shanshui mist-and-mountain staging, and qi arcs drawn as ink flourishes for honor-bound martial epics.
---

# Manhua Wuxia Comic

**Style Lock (do not deviate)**

- Chinese wuxia manhua register: martial-arts epic drawn with traditional painting DNA in modern chapter format
- Calligraphic brush linework: strokes swell thick-to-thin like brush calligraphy, fastest lines on fastest motion — line is gesture first, contour second
- Jewel-tone **mineral palette**: malachite green, azurite blue, cinnabar red, ochre gold over ink-black structure — pigment-deep, never neon
- Flowing robes and ribbon physics: sashes, sleeves, and hair trail motion in long S-curves; cloth tells the wind and the strike
- Shanshui staging: mist bands, layered mountain silhouettes, pines and pavilions set scale — figures small against landscape in establishing shots
- Qi and motion arcs rendered as **ink flourishes** — calligraphic sweeps and controlled splatter, never glow effects
- Cinematic chapter pages; diagonal panel cuts sanctioned during duels, hard rules elsewhere

## Negative Locks

- No neon, candy, or pastel palettes — color stays mineral and pigment-deep
- No glow, bloom, or lens-flare energy effects; qi is ink, not light VFX
- No Japanese manga grammar artifacts: no screentone, no chibi drops, no sweat-drop icons
- No modern objects, clothing, or architecture in frame
- No stiff static fight poses — motion without gesture lines is wrong
- No photoreal rendering or 3D sterility

## When to Use

- Wuxia and xianxia: sect rivalries, sword duels, mountain journeys, oaths, cultivation arcs
- Reference images cueing flowing garments, misty landscapes, weapons, or ceremonial grace
- Chapters that interleave duel and consequence — built for parallel action

## When Not to Use

- Modern urban color drama on the scroll → use `manhwa-color-webtoon`
- Gritty realist ink drama → use `gekiga-cinematic-manga`
- Ornamental Western elegance → use `elegant-art-nouveau-comic`

## Story Harness (Image-Driven)

- Translate the four cues into **a matter of honor** — a debt, an oath, a master's name; stakes are moral before they are mortal
- **SETUP**: shanshui establishing shot, figure small against mist and mountain; plant the honor stake (a sword wrapped in cloth, a token, a grave marker)
- **REINFORCE**: commit to motion — robes and ribbons answer the wind, parallel-action cuts between duelists or between blade and consequence; qi arcs enter as intensity rises
- **TURNAROUND**: triumphant or honorable sacrifice — the blow lands or is deliberately withheld, and either way the oath is kept; largest panel, mist clearing or closing; victory without honor is a failed turnaround in this style

## World Guardrail

- Default to dynastic-era China: misty peaks, bamboo groves, temple courtyards, tea houses, river ferries, sect halls
- Props period-true: jian and dao swords, guqin, scrolls, seals, lanterns, teaware; no modern technology ever
- Nature participates: wind, mist, falling leaves, and water move with the emotional current

## Dialogue & Lettering

- Elegant rectangular-leaning bubbles with brush-edged borders; diction sparse and formal to suit the register
- 1–2 bubbles per panel, ≤ ~10 words; duels run silent except for one declaration
- SFX policy: brush-calligraphic SFX for strikes and qi release, drawn as ink gestures integrated with the flourish — one per action page

## Direction Notes

- Camera diet: extreme wides (landscape scale) to full-body action figures; close-ups reserved for the eyes before the decisive blow
- Transition diet: parallel-action interleave via scene-to-scene and subject-to-subject; action-to-action inside exchanges; aspect-to-aspect for the mist-and-mountain breath between movements
- Pacing: duels accelerate through smaller panels and diagonal cuts, then release into a wide silent landscape — the post-blow stillness panel is mandatory
- In chapter format, page turns land on strikes or reveals

## Consistency Notes

- **What drifts first**: palette discipline (jewel tones drift toward neon) and robe/ribbon design continuity; lock the mineral swatches in style memory (`comic-style-memory-system`) and garment flow in the DNA template
- The qi flourish vocabulary is finite: design 2–3 arc shapes per character and reuse them — random energy effects are drift
- Re-anchor faces and hair ornaments every 6–8 panels; period hairstyles collapse into generic anime under pressure
- Mist density is a continuity value per location — log it in the world bible

## Prompt Block

```text
Chinese wuxia manhua style, calligraphic brush linework with
thick-to-thin gestural strokes, jewel-tone mineral palette of
malachite green, azurite blue, cinnabar red and ochre gold over
ink black, flowing robes and ribbons trailing long S-curves,
shanshui staging with mist bands and layered mountain
silhouettes, qi and motion arcs drawn as ink flourishes and
controlled splatter, dynastic Chinese architecture and costume,
cinematic martial-arts chapter composition.
```

## Style Quality Gates

- [ ] Line weight varies calligraphically with motion speed — no uniform dead line
- [ ] Palette stays within the named mineral swatches; no neon drift
- [ ] Cloth and ribbon physics agree with the declared wind/motion direction
- [ ] Qi arcs use the character's designed flourish shapes, drawn as ink, not glow
- [ ] Every action sequence releases into at least one wide shanshui stillness panel

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `multi-page-chapter`; patterns `parallel-action` and `setup-reinforce-turnaround`

---

*Manhua wuxia treats movement as calligraphy.*
