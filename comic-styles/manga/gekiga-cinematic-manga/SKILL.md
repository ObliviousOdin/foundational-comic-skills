---
name: gekiga-cinematic-manga
version: 2.0.0
category: comic-styles
description: Cinematic realist gekiga in the Tatsumi/Saito lineage — heavy sumi brushwork, crosshatch, spot blacks, and film framing for mature, gritty, emotionally honest stories.
---

# Gekiga Cinematic Manga

**Style Lock (do not deviate)**

- Gekiga realism in the Tatsumi/Saito lineage: late-1950s–70s kashihon (rental-manga) grit, adult register, black-and-white print feel
- Realistic character proportions and anatomy — lived-in faces, heavy jaws, tired eyes; no cute stylization anywhere
- Heavy sumi brush linework: thick, confident strokes on figures; all shading from crosshatch and spot blacks, never tone fields
- Spot blacks placed by **luminance thresholding** — the darkest third of the value range drops to solid black, applied with one consistent threshold
- Crosshatching density mapped to emotional intensity: calm scenes stay open and airy, pressure scenes tighten the hatch
- Cinematic staging: closeups, wide establishing shots, deep foreground/midground/background layering like a film frame
- Wide-angle lens distortion permitted on key shots (looming buildings, stretched alleys) when threat or alienation peaks
- Detailed urban environmental realism — postwar streets, bars, tenements in careful ruled perspective
- Panel bleeds reserved for key moments; otherwise hard hand-ruled rectangular borders

## Negative Locks

- No color; no digital gray gradients, airbrush, blur, or bloom — every value is ink (hatch, black, white)
- No big-eye manga stylization, chibi drops, or era emotion icons (sweat drop, puff sigh, sparkle)
- No clean screentone gloss standing in for hand crosshatch
- No gag staging, bouncy bubbles, or cartoon SFX lettering
- No photoreal rendering or 3D-perspective sterility; realism is drawn, not rendered

## When to Use

- Noir, crime, postwar drama, working-class struggle, moral ambiguity, quiet desperation
- Reference images whose mood cues read fatigue, regret, resolve, or simmering tension
- Stories that need cinematic time: slow reveals, held silences, consequence that lands late

## When Not to Use

- Warm slice-of-life or first-crush softness → use `retro-hand-inked-manga-comic`
- Supernatural dread and anatomical wrongness → use `junji-ito-body-horror`
- High-contrast Western noir of pure white-on-black shapes → use `sin-city-graphic-noir`

## Story Harness (Image-Driven)

- Translate the four cues into a **moment with consequence** — stakes are personal and material (rent, debt, pride, a promise)
- **SETUP**: establish place before person — wide urban shot, character small in the frame; plant one concrete pressure detail (an unpaid bill, a waiting figure, a last cigarette); calm, open hatching
- **REINFORCE**: move the camera in; tighten crosshatch as pressure mounts; spot blacks begin eating the background; one held moment-to-moment beat lets the silence work
- **TURNAROUND**: earned, honest, sometimes bitter — a hard choice made, a truth admitted, a small dignity kept or lost; the strip's one panel bleed may land here; never a cheap twist, never cynicism without cost

## World Guardrail

- Default to postwar-to-1970s Japanese urban settings: tenement rooms, alley bars, pachinko parlors, rail crossings, dockyards
- Props are worn and material — cigarettes, cheap radios, paper money, payphones at most; no smartphones or modern tech unless the reference insists
- Weather is a pressure instrument: rain, humidity haze, hard summer light

## Dialogue & Lettering

- Rectangular-leaning bubbles with hand-inked borders; narration in square caption boxes, sparse and declarative
- 1–2 bubbles per panel, ≤ ~10 words; silence is a legitimate beat — held panels may carry no text at all
- SFX policy: rough hand-brushed effects only for physical impact (a train, a slammed door), never decorative; one per strip or page maximum

## Direction Notes

- Camera diet: film coverage ladder — wide establish, medium, closeup; low angles and over-shoulder shots welcome
- Transition diet: action-to-action spine; moment-to-moment for held silences; subject-to-subject to withhold the reveal until it must land (the slow-burn engine)
- Pacing: wide gutters buy time; the pre-turn panel runs silent; a panel bleed marks the one irreversible moment
- Eyelines exit right (or left under an RTL contract — this style is RTL-eligible)

## Consistency Notes

- **What drifts first**: hatch-density discipline and face realism (degrades toward generic anime); lock jaw, eye, and wear pattern in the DNA template
- The spot-black luminance threshold is a style-memory value (`comic-style-memory-system`) — fix it once or blacks wander between panels
- Re-anchor faces against the canonical sheet every 6–8 panels; gekiga faces are weathered, and the weathering must not migrate
- The crosshatch-to-emotion mapping is a contract: calm = open, tense = dense; log it in the world bible so direction can call it by name

## Prompt Block

```text
Gekiga cinematic manga style, black and white, Tatsumi and Saito
lineage, realistic adult proportions, heavy sumi brush outlines,
dense crosshatch shading that tightens with tension, solid spot
blacks placed by luminance, detailed postwar Japanese urban
backgrounds in ruled perspective, film-like staging with deep
foreground and background layers, occasional wide-angle lens
distortion, hard hand-ruled rectangular panel borders, gritty
1960s rental-manga print texture.
```

## Style Quality Gates

- [ ] Spot blacks obey the locked luminance threshold (ink coverage logic consistent across panels)
- [ ] Crosshatch density tracks the emotional beat — calm open, tense dense — against the beat sheet
- [ ] Faces stay realist: no big-eye drift, no emotion icons
- [ ] At most one panel bleed, and it lands on the irreversible moment
- [ ] Establishing shots hold ruled perspective and period detail

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` or `multi-page-chapter`; patterns `slow-burn-reveal` and `setup-reinforce-turnaround`; RTL eligible

---

*Gekiga treats the panel as a film frame, not a cartoon box.*
