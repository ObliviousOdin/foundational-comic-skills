---
name: cyberpunk-sci-fi-comic
version: 2.0.0
category: comic-styles
description: Neon-noir cyberpunk — dark base values cut by 2–3 locked neon accents, rain-slick chrome, disciplined holographic clutter, and megacity verticality for high-tech low-life stories.
---

# Cyberpunk Sci-Fi Comic

**Style Lock (do not deviate)**

- Neon-noir value system: dark base — at least 70% of every panel sits below middle gray — cut by **2–3 neon accent hues locked per project** (e.g., magenta + cyan, or amber + teal); accents never multiply mid-story
- Heavy spotted blacks with **digital-glow rim light**: figures separate from darkness via a thin colored edge light sourced from signage, screens, or rain reflections — never from nowhere
- Rain and chrome reflectivity: wet asphalt mirrors the signage above it; chrome and glass carry streaked, smeared reflections; every exterior surface answers a visible light source
- Holographic clutter discipline — signal vs noise: at most **one readable hologram or sign per panel** (the signal); all other glow is defocused noise (bokeh smears, scanline ghosts)
- Megacity verticality: urban canyons shot up or down, stacked strata (street, skyway, tower); flat horizons are off-style
- Sharp angular linework with digital texture: hard bevels on tech, subtle scanline or chromatic fringe permitted only on glow edges
- Era anchor: 1980s–90s print cyberpunk lineage — first-wave neon-noir film and manga serialization feel; everything worn and retrofitted, never showroom-clean

## Negative Locks

- No daylight pastel or full-spectrum rainbow palettes; no accent hue outside the project lock
- No clean utopian tech: no pristine white interiors, no unscratched chrome
- No photorealistic faces or photo-composited cityscapes
- No fantasy elements — magic, creatures, medieval props
- No flat suburban or rural staging; no empty sky without structure cutting it

## When to Use

- Near-future stories of surveillance, alienation, hustle, and small humanity inside vast systems
- Reference images cueing night, rain, signage glow, tech-worn streets, or chrome
- When the payoff should feel bittersweet or defiant rather than triumphant

## When Not to Use

- Painterly, lyrical, wide-open sci-fi vistas → use `moebius-metal-hurlant-sci-fi`
- Brass-age invention and Victorian machinery → use `steampunk-victorian-comic`
- Pure black-and-white crime noir without tech → use `sin-city-graphic-noir` or `noir-expressionist-comic`

## Story Harness (Image-Driven)

- Translate the four cues into one human-scale want inside an indifferent megacity — stakes personal, systems vast
- **SETUP**: character small against verticality — high or low angle, rain falling, the locked accent hues claiming their territory; plant one tech detail (an implant flicker, a tailing drone, a glitching sign) as the inciting signal
- **REINFORCE**: step closer; the character engages the signal — hologram interaction, a chrome reflection revealing what stands behind them, rim light tightening; raise the noise density around them while the readable signal stays singular
- **TURNAROUND**: **bittersweet or defiant** — the system wins but the human keeps one thing, or the human stands back up inside the glow; earned when the panel-1 tech detail returns transformed; biggest panel, deepest blacks, accents at their purest

## World Guardrail

- Default setting: a layered near-future megacity — noodle stalls under skyways, server alleys, rooftop antenna farms, transit tubes
- Technology worn, modded, retrofitted: taped cables, aftermarket implants, cracked screens still working
- Corporate presence stays ambient (logos, drones, announcements); weather defaults to rain or post-rain wet; night is the native hour

## Dialogue & Lettering

- Hard-edged rectangular bubbles with sharp straight tails; comms, AI, and broadcast voices in angular bordered boxes keylined in one locked accent hue — per `comic-lettering-and-balloons`, these are the only deltas; caption boxes remain forbidden
- 1–2 bubbles per panel, ≤ ~10 words; the turnaround often carries one short defiant line, or silence
- SFX policy: glitch-type effects (stuttered, fragmented letterforms) for tech events only, one per strip; rain is never lettered

## Direction Notes

- Camera diet: extreme high and low angles to state verticality; medium-close at street level; reserve the level eye-line shot for the turnaround so the human beat lands plainly
- Transition diet: subject-to-subject and scene-to-scene carry the city's scale; one aspect-to-aspect beat (rain, signage, reflection) earns the atmosphere — in `webtoon-scroll-segment` runs, stretch that beat down the scroll
- Pacing: tight gutters through pressure, one wide gutter (or long scroll gap) before the turn; black inter-panel space is on-style — let darkness occupy the gutter

## Consistency Notes

- **What drifts first**: neon accent hues multiply and slide toward rainbow; lock exact hue names/values in `comic-style-memory-system` and recheck every panel against the swatch
- Rim light must trace to a visible source per panel — under drift it becomes sourceless outline glow
- Hologram density creeps upward; re-apply the one-readable-signal rule at every review pass
- Re-anchor faces against the canonical sheet every 6–8 panels; glow and rain erode facial structure fastest

## Prompt Block

```text
Neon-noir cyberpunk comic style, dark low-key base values cut by two to
three locked neon accent hues, heavy spotted blacks, thin digital-glow
rim light sourced from signage and screens, rain-slick streets with
chrome and glass reflections, one readable holographic sign amid
defocused glowing clutter, towering layered megacity verticality, sharp
angular linework with subtle scanline texture on glow edges, worn
retrofitted technology, 1980s-90s print cyberpunk atmosphere.
```

## Style Quality Gates

- [ ] Accent hues per panel ≤ 3 and all match the project lock exactly
- [ ] At most one readable hologram/sign per panel; remaining glow is defocused noise
- [ ] Every rim light traces to a visible source (sign, screen, reflection)
- [ ] Wet surfaces reflect their actual light environment — no dry asphalt under neon
- [ ] At least one panel per strip states megacity verticality (looking up or down)

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` or `webtoon-scroll-segment`; patterns `setup-reinforce-turnaround`, `slow-burn-reveal`

---

*The city sells light by the watt; the story belongs to whoever cannot afford it.*
