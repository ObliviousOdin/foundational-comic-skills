---
name: ink-wash-storybook-manga
version: 2.0.0
category: comic-styles
description: Sumi-e ink-wash storybook manga — two-to-three-value gray washes on toothy handmade paper with generous negative space, for quiet, poignant strips that often need no words.
---

# Ink Wash Storybook Manga

**Style Lock (do not deviate)**

- Sumi-e ink-wash manga in the quiet storybook register: traditional brush-and-water rendering, no screentone anywhere
- Layered gray washes at **2–3 value steps** (light mist, mid gray, dark accent) plus the reserved white of the paper — values are discrete washes, never continuous gradients
- Handmade paper tooth visible throughout: wash edges granulate, brush strokes dry-break on the texture
- Minimal but expressive linework: a few confident brush lines define each figure; interior detail is suggested, not drawn
- Stippling reserved for texture accents (stone, bark, falling snow) — sparse and hand-placed
- Generous negative space: at least a third of every panel breathes empty; emptiness is composition, not absence
- Borderless wash edges allowed: a wash fading into paper is a legitimate panel border; hard rules only when structure demands

## Negative Locks

- No screentone, digital gradients, or airbrush softness — all tone is brushed wash with real edges
- No dense linework, crosshatch fields, or heavy spot blacks
- No color — gray ink values on paper white only
- No crowded compositions; panels never fill edge-to-edge with detail
- No cartoon emotion icons (sweat drops, speed lines, sparkle fields)
- No vector-clean line or sterile digital flatness; every mark shows its brush origin

## When to Use

- Quiet, literary, contemplative stories: memory, seasons, partings, small kindnesses, grief settling into peace
- Reference images cueing stillness, nostalgia, rain, mist, or soft natural light
- Strips meant to land wordless — this is the house style of the silent strip

## When Not to Use

- Warm everyday comedy with era tropes and tone → use `retro-hand-inked-manga-comic`
- Gritty urban drama needing dense ink pressure → use `gekiga-cinematic-manga`
- Color picture-book softness → use `watercolor-storybook-comic`

## Story Harness (Image-Driven)

- Translate the four cues into **a single quiet observation** — weather, an object left behind, a small gesture; the stakes are a feeling shifting
- **SETUP**: wide, airy composition, character small against landscape or interior; the first wash layer sets weather and mood; the focal object carries the darkest accent value
- **REINFORCE**: come gently closer; the second wash layer deepens; an aspect-to-aspect or moment-to-moment beat — the character notices, pauses, holds
- **TURNAROUND**: poignant and gentle — an acceptance, a small letting-go, a warmth surfacing through stillness; the most negative space of the strip, often fully silent; the darkest value touches only the emotional center

## World Guardrail

- Default to natural and timeless settings: riverbanks, mountain paths, temple steps, old wooden houses, rain on tile roofs
- Props minimal and handmade: paper umbrellas, lanterns, teacups, letters; no modern technology unless the reference insists
- Weather and season are the lead instruments: mist, snow, blossom fall, summer rain

## Dialogue & Lettering

- Small unobtrusive bubbles with soft hand-drawn borders, or border-free text floating in empty wash
- 0–1 bubbles per panel, ≤ ~6 words; the default is silence — any text must justify itself against the quiet
- SFX policy: none; sound is depicted by wash and stipple (rain streaks, snow dots), never lettered

## Direction Notes

- Camera diet: wide and medium-wide dominate; close-ups are rare and reserved for the turn
- Transition diet: aspect-to-aspect is the native gait (mood circling a moment); moment-to-moment for the held pause; avoid action-to-action chains entirely
- Pacing: wide, even gutters — or no borders at all, washes separated by paper white; adjacent panels may share weather across the gutter
- Eyelines exit right (or left under an RTL contract — this style is RTL-eligible)

## Consistency Notes

- **What drifts first**: wash value count (2–3 layers creep into full grayscale rendering) and paper tooth dissolving into digital smoothness; lock both in style memory (`comic-style-memory-system`)
- Fix the value recipe project-wide — name the steps (e.g., 15% mist / 45% mid / 80% accent) and where each is allowed
- With this little linework the silhouette IS the character: the DNA template must define each silhouette, re-anchored every 6–8 panels
- The negative-space ratio is a contract: when panels start filling, the style is failing — re-anchor composition against the canonical strip

## Prompt Block

```text
Quiet sumi-e ink-wash manga storybook style, layered gray brush
washes in two to three discrete value steps on toothy handmade
paper, granulated wash edges and dry-brush breaks, reserved
paper-white negative space, minimal confident brush linework,
sparse hand-placed stippling for texture, soft borderless panels
where washes fade into the page, misty atmospheric depth, gentle
natural light, contemplative stillness, traditional Japanese
brush painting feel.
```

## Style Quality Gates

- [ ] Wash layers are countable: 2–3 values plus paper white, no continuous-gradient rendering
- [ ] Paper tooth visible in wash edges and dry-brush breaks in every panel
- [ ] At least one third of each panel is negative space
- [ ] Stippling stays sparse and purposeful (texture accents only, never overall shading)
- [ ] Silent panels read clearly with no text support

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal`; patterns `silent-strip` and `kishotenketsu`; RTL eligible

---

*Ink wash treats tone as atmosphere.*
