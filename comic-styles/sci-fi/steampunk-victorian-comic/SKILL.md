---
name: steampunk-victorian-comic
version: 2.0.0
category: comic-styles
description: Victorian-engraving steampunk — brass/copper/oxblood palette, etching-style hatching, functional clockwork, and gaslight glow for ingenious alternate-history adventures.
---

# Steampunk Victorian Comic

**Style Lock (do not deviate)**

- Victorian engraving sensibility: form modeled by **etching-style parallel hatching and cross-hatching** (steel-nib, 1880s periodical-plate feel), never by airbrush or soft gradients
- Palette locked to **brass, copper, and oxblood** over soot-brown and ivory neutrals; verdigris green allowed as the single cool counterpoint
- Metal sheen built from hatch density: lines compress into a burnished highlight band and open into shadow — no specular white "ping" dots, no gloss
- **Clockwork greeble discipline**: every gear, valve, gauge, and pipe implies workable function — meshed teeth, connected linkages, plausible plumbing; ornament that does nothing is off-style
- Gaslight glow: warm pooled light with soft falloff from lamps, fireboxes, and furnace doors; night exteriors lit in amber islands inside fog
- Period costume silhouettes, 1880s–90s: corsetry and bustles, frock coats, waistcoats, top hats; goggles and gauntlets worn as working tools, never as fashion garnish
- Ornate but legible panel frames: ruled double borders with engraved corner flourishes that never intrude into panel interiors

## Negative Locks

- No post-Victorian technology: no plastics, LEDs, screens, or digital readouts
- No chrome-and-neon palette, cyber glow, or lens flare
- No gear-spam — cogs glued onto surfaces without mechanical purpose
- No modern clothing, contemporary signage, or present-day architecture
- No cel-shade gloss, airbrush bloom, or photoreal rendering

## When to Use

- Alternate-history invention tales, airship heists, workshop dramas, gaslamp mysteries
- Reference images cueing brass, machinery, period dress, fog, or flame-light
- When the payoff should be cleverness made visible — a mechanism turning the tables

## When Not to Use

- Neon near-future megacities → use `cyberpunk-sci-fi-comic`
- Painterly cosmic vistas and silent wandering → use `moebius-metal-hurlant-sci-fi`
- Bold graphic adventure without ornament → use `bold-woodcut-adventure` or `ligne-claire-franco-belge`

## Story Harness (Image-Driven)

- Translate the four cues into a problem a machine — or its inventor — can answer; stakes mechanical on the surface, stakes of the heart underneath
- **SETUP**: character inside their working world — workshop bench, airship gantry, foggy gaslit street; plant the key mechanism in plain sight (a gauge climbing, a wound spring, an odd patent device) — Chekhov's gear
- **REINFORCE**: pressure mounts through the machinery — steam pressure rises, the clock hand advances, hatching densifies in the shadows; the character works the problem with visible, period-plausible action
- **TURNAROUND**: **ingenious reversal** — the planted mechanism resolves the jam in a way the reader can mechanically follow; earned only if panels 1–2 showed the parts; stage it in the warmest gaslight of the strip, largest panel

## World Guardrail

- Default setting: an 1880s–90s industrial metropolis that never left steam — foundries, observatories, dirigible docks, gaslit arcades, cobbled lanes in fog
- Power sources: steam, clockwork, pneumatics, galvanic cells at the bleeding edge; communication by speaking-tube, telegraph, and punched card
- Class texture welcome (soot versus drawing-room); violence stays adventure-grade, peril over gore

## Dialogue & Lettering

- Oval bubbles with fine double-rule outlines echoing the engraved frames; formal, lightly serifed hand-lettering — per `comic-lettering-and-balloons`, these are the only deltas; caption boxes remain forbidden
- 1–2 bubbles per panel, ≤ ~12 words; period diction without parody
- SFX policy: mechanical onomatopoeia (HISS, CLANK, TICK) hand-set in small engraved capitals, max one per panel, placed along the machinery that makes the sound

## Direction Notes

- Camera diet: medium and medium-wide to keep figure and machinery in one frame; insert close-ups on mechanisms (gauge, gear mesh, valve) are this style's signature cut
- Transition diet: action-to-action for work sequences, subject-to-subject between figure and mechanism; one moment-to-moment beat as the device engages sells the reversal
- Pacing: even gutters between ruled borders; widen the gutter before the turnaround and give that panel the richest corner flourishes of the strip

## Consistency Notes

- **What drifts first**: greeble density — machinery decays into decorative soup — and the palette warming toward generic sepia; lock the brass/copper/oxblood swatch and an "every mechanism functions" note in `comic-style-memory-system`
- Hatching direction and spacing must stay consistent per material (metal, cloth, stone); record the convention in the world bible
- Costume silhouettes drift modern at the waist and shoes first; re-anchor against the canonical sheet every 6–8 panels
- Recurring devices are characters: give signature machines their own DNA entries

## Prompt Block

```text
Victorian steampunk comic in engraved-plate style, steel-nib etching
linework with parallel and cross-hatching modeling all form, brass
copper and oxblood palette over soot and ivory neutrals, metal sheen
rendered by hatch density, functional clockwork with meshed gears
valves and gauges, warm pooled gaslight glow with soft falloff, 1880s
period costume silhouettes with working goggles, fog-bound industrial
metropolis, ornate engraved panel borders with corner flourishes, no
modern technology.
```

## Style Quality Gates

- [ ] Every visible mechanism could plausibly work — meshed gears, connected linkages, no orphan cogs
- [ ] Shading is hatch-based throughout; no airbrush or gradient patches
- [ ] Palette stays within brass/copper/oxblood plus neutrals (verdigris only as the cool accent)
- [ ] Light sources are gas, flame, or furnace — warm, pooled, soft falloff
- [ ] Frame ornament stays outside the live area; panel interiors remain legible

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` or `multi-page-chapter`; patterns `setup-reinforce-turnaround`, `slow-burn-reveal`, `parallel-action`

---

*Every gear must earn its teeth: ornament that does no work is rust.*
