---
name: moebius-metal-hurlant-sci-fi
version: 2.0.0
category: comic-styles
description: Moebius / Métal Hurlant sci-fi — fine constant-weight pen line, micro-stipple shading, vast desert-mesa vistas, crystalline organic technology, and luminous flat color for wordless wonder.
---

# Moebius Metal Hurlant Sci-Fi

**Style Lock (do not deviate)**

- French **Métal Hurlant** science-fiction tradition in the Moebius lineage (1975–85 era)
- **Fine constant-weight pen line** (crowquill/Rotring fineness): high detail density with zero line-weight drama — the line describes, never performs
- Shading by **micro-stipple** and sparse parallel ticks only; no crosshatch mass, no spot-black pools
- **Vast desert-mesa vistas**: tiny figures against enormous emptiness — scale built from negative space and a low, sacred horizon
- **Crystalline and organic technology**: ships, gates, and engines that look grown or carved, never riveted or greebled
- **Luminous flat color washes** — airy blues, sand pinks, mineral turquoise; flat zones with watercolor light in them
- **Silent grandeur**: long wordless passages are native, not exceptional
- Floating figures and levitation as a recurring visual signature; gravity is polite, not absolute

## Negative Locks

- No variable brush line, heavy spot blacks, or chiaroscuro shadow masses
- No murky, desaturated, or grimdark palettes — color stays luminous and clean
- No riveted retro-rockets, greebled hull plating, or used-future grime; tech reads crystalline or grown
- No photorealistic texture, 3D-render surfaces, or lens effects
- No horizon-to-horizon clutter — emptiness is structural and must survive

## When to Use

- Speculative, philosophical, or dreamlike journeys: pilgrimages, first contact, awakenings, silent crossings
- Reference images suggesting wonder, isolation, immensity, or serene strangeness
- When the story can afford silence and the panel must feel like a window onto another world

## When Not to Use

- Neon urban dystopia and chrome → use `cyberpunk-sci-fi-comic`
- Brass-and-steam Victorian machinery → use `steampunk-victorian-comic`
- Documentary clear-line adventure → use `ligne-claire-franco-belge`

## Story Harness (Image-Driven)

- Translate the four cues into a **crossing toward a mystery** — a traveler, a threshold, a phenomenon that answers with a bigger question
- **SETUP**: vast establishing — tiny figure, immense mesa horizon, one anomalous form in the distance; stipple carries the ground, the sky stays clean
- **REINFORCE**: the approach — aspect-to-aspect fragments of the phenomenon (a crystalline surface, a hovering shape, the traveler's upturned face); detail density rises, words do not
- **TURNAROUND**: **wondrous or enigmatic** — the encounter reframes scale or reality; ambiguity is a legal ending; "earned" means the silence and space prepared the reader to feel small at exactly the right moment

## World Guardrail

- Default worlds: white-sand deserts, mesa labyrinths, salt flats, monolithic ruins, floating stones, robed wanderers, bird-like mounts
- Technology policy: crystalline, biological, or mineral — interfaces glow softly, vessels drift; no exhaust, no rivets
- Era timeless; weather minimal and luminous (heat shimmer, thin moons; twin suns allowed)

## Dialogue & Lettering

- Inherits comic-lettering-and-balloons defaults; deltas: small, calm, mixed-case European hand lettering
- Thin-bordered oval balloons used sparsely; brief philosophical captions allowed at section turns
- 0–1 balloons per panel, ≤ 10 words; entire wordless pages are encouraged
- SFX policy: essentially none — at most a faint ambient hum lettered small; sound is depicted, not shouted

## Direction Notes

- Camera diet: extreme wide establishing shots, calm middle-distance follows, occasional sky-up reverence shots; close-ups saved for awe on a face
- Transition diet: **aspect-to-aspect rich**, with moment-to-moment drift and scene-to-scene jumps across vastness — McCloud's slow registers are home
- Pacing: panoramic panels, wide gutters, generous dwell; vary panel height sharply to deliver scale shock at the turn
- Let one panel per page be almost empty — the breath is part of the grammar

## Consistency Notes

- **What drifts first**: line weight thickens and color saturates toward generic sci-fi; pin pen width, stipple density, and the luminous swatch set in `comic-style-memory-system`
- Horizon discipline decays second — keep the low-horizon, big-sky ratio constant across the chapter
- Tech silhouettes drift toward riveted convention; anchor crystalline/organic forms in the world bible
- Re-anchor the traveler's silhouette (robe, mount, gait) against the DNA sheet every 6–8 panels; faces are simple and drift quietly

## Prompt Block

```text
French Métal Hurlant science-fiction comic style in the Moebius
tradition, fine constant-weight pen line, micro-stipple and sparse
tick shading with no heavy blacks, vast empty desert-mesa vistas
with tiny figures and low horizons, crystalline and organic
technology, luminous flat watercolor-like color washes in airy
blues and sand pinks, floating figures, serene wordless grandeur,
clean European album print feel.
```

## Style Quality Gates

- [ ] Line weight fine and constant — no brush swell, no spot-black pools
- [ ] Stipple density consistent panel to panel; shading never becomes crosshatch mass
- [ ] At least one vast-scale panel with a tiny figure per page
- [ ] Palette luminous and clean — no mud, no grimdark grading
- [ ] Technology reads crystalline or grown; zero rivets, panels stay uncluttered
- [ ] Silence respected: wordless beats left wordless

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `multi-page-chapter`; patterns `kishotenketsu`, `slow-burn-reveal`, `silent-strip`

---

*The emptier the desert, the louder the wonder — let the line whisper and the scale speak.*
