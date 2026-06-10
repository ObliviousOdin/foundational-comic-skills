---
name: retro-hand-inked-manga-comic
version: 2.0.0
category: comic-styles
description: B&W retro hand-inked manga (1970s–80s shōnen/shōjo) — G-pen brushwork, screentone shading, warm slice-of-life register for intimate, uplifting strips.
---

# Retro Hand-Inked Manga Comic

**Style Lock (do not deviate)**

- Retro hand-inked shōnen/shōjo manga, 1970s–80s magazine feel (pre-digital print era)
- Black and white only — no color, no digital gray gradients; all mid-tones come from **screentone** (consistent dot ruling, 40–60 lpi feel) or sparse hatching
- **G-pen line language**: outlines swell at curves and shadow sides, taper at speed and light sides; maru-pen-fine interior details (lashes, hair strands, fabric folds)
- Expressive period eyes — large, wet highlights (1–2 per eye, fixed count), no modern multi-sparkle rendering
- Emotion grammar of the era: speed lines, sweat drop, blush hatching, small floating "puff" sighs — used sparingly and only when the beat earns them
- Hand-drawn page texture: slight line wobble, visible tone edges, occasional white-out corrections; never vector-clean
- Clean rectangular panel borders (~2px feel, hand-ruled), rounded speech bubbles with hand-lettered character

## Negative Locks

- No color of any kind; no halftone moiré (mismatched tone rulings)
- No digital gradients, airbrush glow, lens blur, or bloom
- No modern anime rendering: no cel shading, no chromatic eye stacks, no glossy hair bands
- No photorealistic faces or photo-textured backgrounds
- No 3D-render perspective sterility; backgrounds are hand-perspective with ruler lines
- No watermark-like marginalia, mastheads, or print registration marks

## When to Use

- Intimate slice-of-life, gentle comedy, first-crush warmth, everyday courage
- Reference images whose mood cues read soft, hopeful, wistful, or quietly determined
- Default manga style for testing the consistency stack (high tolerance, well-anchored era)

## When Not to Use

- Hard noir, body horror, or gritty realism → use `gekiga-cinematic-manga` or `junji-ito-body-horror`
- Color-forward digital serialization → use `manhwa-color-webtoon`
- Decorative romance with floral emotion staging → use `shoujo-romance-manga`

## Story Harness (Image-Driven)

- Translate the four cues into a **small, recoverable moment** — stakes no larger than one feeling
- **SETUP**: character placed in a warm everyday setting matching wardrobe/mood; introduce one small inciting detail (a sound, a stray animal, a dropped item); medium shot, eye level
- **REINFORCE**: character engages the detail; deepen with era tropes — speed lines for hustle, a single sweat drop for fluster, screentone vignette for interiority; step the camera closer
- **TURNAROUND**: warm reframing — touched, surprised, or quietly delighted; **never sad, ironic, or mean**; biggest panel, simplest background, tone-flat or white behind the face so the feeling reads instantly

## World Guardrail

- Default to timeless pre-digital settings: shopping streets, school rooftops, train platforms, tatami rooms, summer-festival lanes
- Props natural or handmade (bento, letters, umbrellas, transistor radio at most); no phones or screens unless the reference insists
- Weather and season are allowed mood instruments (first snow, cicada heat, spring wind)

## Dialogue & Lettering

- Rounded bubbles, hand-lettered feel, generous padding; thought bubbles as cloud chains
- 1–2 bubbles per panel, ≤ ~8 words; panel 2 often strongest with one short line; turnaround may be silent
- SFX policy: small hand-drawn katakana-style effects allowed only for the inciting detail (one per strip maximum)

## Direction Notes

- Camera diet: medium and medium-close; reserve close-up for the turnaround beat
- Transition diet: action-to-action and subject-to-subject; one moment-to-moment beat before the turn is the era's signature breath
- Pacing: narrow gutters panels 1→2, wide gutter before panel 3; let the final panel carry 40%+ of the strip width when warmth must land
- Eyelines exit right (or left if the contract locks RTL — this style is RTL-eligible)

## Consistency Notes

- **What drifts first**: eye highlight count and hair-mass silhouette; lock both in the DNA template
- Screentone is a style-memory asset: fix ruling and dot shape project-wide (`comic-style-memory-system`), or panels will shimmer between tones
- Re-anchor faces against the canonical sheet every 8–10 panels; period eyes degrade toward modern anime under drift
- Negative block above merges with character negatives via the world bible — never hand-edit merged output

## Prompt Block

```text
1970s-80s retro hand-inked Japanese manga style, black and white,
G-pen brush outlines with natural swell and taper, fine maru-pen detail
lines, soft screentone shading with consistent dot ruling, gentle
cross-hatching, large expressive period eyes with single wet highlight,
hand-drawn page texture with slight line wobble, clean hand-ruled
rectangular panel borders, rounded hand-lettered speech bubbles,
vintage shōjo/shōnen magazine print feel.
```

## Style Quality Gates

- [ ] Screentone ruling consistent across all panels (no moiré, no digital gradient patches)
- [ ] Line weight visibly varies with curve and shadow (not mechanically uniform)
- [ ] Eye rendering matches period grammar (fixed highlight count, no modern stacking)
- [ ] At most one era emotion-trope per panel, and it matches the beat
- [ ] Turnaround panel background simplified so the emotional read is instant

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` or `4koma-vertical`; patterns `setup-reinforce-turnaround`, `kishotenketsu`, `silent-strip`; RTL eligible

---

*The warmth is in the wobble: a hand drew this, and the reader can feel it.*
