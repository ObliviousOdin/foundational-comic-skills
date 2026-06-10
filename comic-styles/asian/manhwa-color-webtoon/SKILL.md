---
name: manhwa-color-webtoon
version: 2.0.0
category: comic-styles
description: Clean-line full-color Korean webtoon — cinematic teal/warm grading, soft volumetric light, and K-drama staging in full-bleed vertical panels built for the scroll.
---

# Manhwa Color Webtoon

**Style Lock (do not deviate)**

- Modern Korean webtoon (manhwa) digital style, 2010s+ serialization register, full color
- Clean digital lineart: even, closed contour lines with slight taper; outlines may tint toward local color (color holds) on lit edges
- Cinematic color grading with a **teal/warm key contrast**: cool ambient field against warm key light on faces and emotional centers
- Soft volumetric lighting — window shafts, dusk glow, screen light; shadows are soft-edged color shapes, never gray
- K-drama staging: two-shots, over-shoulder reaction pairs, held close-ups on micro-expressions
- Full-bleed vertical panels designed for one-hand scroll reading; painterly-soft backgrounds behind crisp character lines
- Scroll-gap timing: vertical white space between panels is a directed beat, sized to the pause it buys

## Negative Locks

- No screentone, halftone dots, or B&W manga print artifacts
- No heavy crosshatch or rough inked texture — rendering stays clean digital
- No flat cel-cartoon shading or thick uniform cartoon outlines
- No photobashed or photoreal backgrounds clashing with the character render
- No multi-column page grids inside a scroll segment — the scroll is a single column
- No desaturated gloom: even night scenes keep the graded color contrast

## When to Use

- Modern romance, campus and office drama, thriller beats with serialized momentum
- Reference images cueing contemporary fashion, city light, soft glow, or K-drama mood
- Vertical serialized reading where each segment must end on a held feeling or a hook

## When Not to Use

- Period B&W romance texture and tone grammar → use `shoujo-romance-manga`
- Inked grit and postwar weight → use `gekiga-cinematic-manga`
- Wuxia spectacle with calligraphic ink energy → use `manhua-wuxia-comic`

## Story Harness (Image-Driven)

- Translate the four cues into a **contemporary emotional beat with serial momentum** — the segment ends leaning forward
- **SETUP**: wide full-bleed cityscape or interior in the cool ambient grade; introduce the character inside the warm key; plant the hook detail (a phone notification, a familiar silhouette, an empty chair)
- **REINFORCE**: K-drama coverage — over-shoulder, then reaction close-up; tighten the grade contrast as the feeling builds; widen the scroll gap before the turn so the reader's thumb hesitates
- **TURNAROUND**: warm or cliffhanger — either the feeling lands in a glow-lit close-up, or the reveal drops as a full-bleed hook panel; both must be earned by the planted detail; never both at once

## World Guardrail

- Default to contemporary Korean-inflected urban settings: cafes, campus corridors, offices, river-night skylines, convenience stores, rooftop terraces
- Modern technology fully sanctioned: phones, screens, and message threads are first-class story props
- Light sources are plot instruments: phone glow, neon, dawn through blinds

## Dialogue & Lettering

- Clean rounded digital bubbles with thin even strokes; messaging-app inset panels allowed for text conversations
- 1–2 bubbles per panel, ≤ ~10 words; scroll segments may run silent stretches where art and gaps carry the pacing
- SFX policy: small clean typographic SFX (heartbeat, buzz, door chime) color-matched to the grade; one per beat

## Direction Notes

- Camera diet: cinematic ladder — wide establish, medium two-shot, close reaction; compositions favor vertical head-and-shoulders framing
- Transition diet: subject-to-subject for conversation volleys; moment-to-moment for the held breath before a reveal; scene-to-scene only between segments
- Pacing: gutters are scroll gaps — small gap = continuous time, tall gap = beat drop; the segment's final panel earns the tallest gap before it
- Eyelines and hooks flow downward with the scroll; the hook sits at the bottom edge of the segment

## Consistency Notes

- **What drifts first**: the color grade (teal/warm balance wanders) and key-light direction; lock grade values and key side in style memory (`comic-style-memory-system`)
- Face proportions drift toward generic anime under serialization; re-anchor against the DNA sheet every 6–8 panels
- Wardrobe and device continuity matter in modern settings — log outfits and phone models in the world bible
- Scroll-gap sizes are style memory, not improvisation: define small/medium/beat-drop gap values once per project

## Prompt Block

```text
Modern Korean webtoon manhwa style, full color digital art, clean
even lineart with closed contours and subtle color holds,
cinematic color grading with cool teal ambient against warm key
light, soft volumetric lighting and glow, soft-edged colored
shadows, painterly-soft backgrounds behind crisp characters,
contemporary K-drama staging, full-bleed vertical panel
composition built for scroll reading, polished serialized webtoon
production finish.
```

## Style Quality Gates

- [ ] Teal/warm grade contrast present and matching the locked grade values
- [ ] Shadows are soft colored shapes — no gray or cel-flat shadow passes
- [ ] Lineart stays clean and closed; no hatch or tone-texture artifacts
- [ ] Scroll gaps sized from the project's gap scale and matched to the beat
- [ ] Segment ends on a warm landing or a hook — never on a dead-neutral panel

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- **Native format**: `webtoon-scroll-segment` (see `comic-format-library`) via `comic-webtoon-scroll-pipeline` — this style's scroll flow is sanctioned there, not in the 3-panel default
- Native habitat: `webtoon-scroll-segment`; strip-capable in `3-panel-horizontal` when commissioned; patterns `setup-reinforce-turnaround` and `slow-burn-reveal`

---

*Webtoon treats the scroll as the page.*
