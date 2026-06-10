---
name: pulp-adventure-comic
version: 2.0.0
category: comic-styles
description: 1930s–40s pulp adventure serial — brush-inked heroes over a warm aged-paper palette and matte-painted exotic locales, built for low heroic angles, cliffhangers, and clever reversals.
---

# Pulp Adventure Comic

**Style Lock (do not deviate)**

- 1930s–40s pulp adventure serial comic (Raymond/Foster newspaper-strip lineage): **brush-inked figures with strong spot blacks** and confident thick-to-thin swells
- **Warm saturated palette over an aged pulp-paper base tone** — ochres, crimsons, jungle greens; flat fills only, no gradients
- **Bold staging with low heroic angles**: protagonists framed from below at decisive beats; perils loom from above
- **Exotic-locale backgrounds rendered like matte paintings**: temples, aerodromes, jungle rivers, dirigibles — painted depth behind crisply inked figures
- Idealized athletic anatomy in the classical illustration tradition; clear hero/villain visual language at silhouette distance
- **Cliffhanger framing**: strip and chapter endings stage unresolved physical peril or a reversal caught mid-action
- Serial narrator voice in rectangular caption boxes ("Meanwhile, at the hidden airfield…")

## Negative Locks

- No modern digital rendering: no gradients, glow, lens flares, or painter-software blends
- No desaturated grime realism — pulp stays warm, saturated, and optimistic even in danger
- No photorealistic faces; anatomy is idealized and brush-described
- No technology past the 1940s aviation/radio era unless the reference image insists
- No capes-and-tights superhero iconography — that belongs to `golden-age-superhero-comic`

## When to Use

- Swashbuckling, exploration, aviation derring-do, lost-world adventure
- Reference images that read warm, energetic, heroic, or wide-horizon
- Multi-chapter serials that need momentum and an ending hook every page

## When Not to Use

- Caped metropolis heroics → use `golden-age-superhero-comic`
- Mythic wordless gravity → use `bold-woodcut-adventure`
- Hard-edged speculative worlds → use `moebius-metal-hurlant-sci-fi` or `cyberpunk-sci-fi-comic`

## Story Harness (Image-Driven)

- Translate the four cues into a physical objective in a vivid place: someone must reach, rescue, recover, or escape — visibly
- **SETUP**: hero and goal staged against the locale's widest vista — matte-painted establishing depth; narrator caption names the place and the stakes; low angle introduces the hero
- **REINFORCE**: the obstacle strikes mid-action — diagonal compositions, action-to-action momentum, spot blacks deepening; the peril must be physical and visible, never abstract
- **TURNAROUND**: **triumphant or clever reversal** — skill or wits flip the peril; biggest panel, fullest heroic angle, warm palette at peak; in `multi-page-chapter` work this beat may instead land as cliffhanger framing — peril unresolved, next-chapter promise explicit

## World Guardrail

- Default 1930s–40s globe-trotting adventure world: jungle temples, desert aerodromes, tramp steamers, mountain kingdoms, dirigible docks
- Tech ceiling: prop planes, radios, revolvers, steam and early diesel
- Locales exotic but respectful — architecture and landscape carry the wonder; no ethnic caricature

## Dialogue & Lettering

- Serial narrator caption boxes (rectangular, warm-toned) open and close beats; inherits `comic-lettering-and-balloons`
- Crisp hand-lettered bubbles; heroes speak in short declaratives; budget 1 caption + ≤ 2 bubbles per panel
- SFX policy: bold brush SFX at action peaks (RAT-TAT, CRASH) — one per panel, two per strip maximum

## Direction Notes

- Camera diet: low heroic angles on protagonists, wide establishing vistas, diagonal action staging; dutch angle reserved for peril beats
- Transition diet: action-to-action dominant; scene-to-scene with narrator captions for locale jumps — the serial grammar; `parallel-action` cross-cutting available in chapters
- Pacing: brisk, no dead panels; in strips, wide gutter before the reversal; in chapters, end every page on a question or a peril
- Hold horizon lines consistent within a scene so the matte-painting depth stays credible

## Consistency Notes

- **What drifts first**: palette warmth — the aged-paper base cools toward modern neutral white; lock the paper-base swatch and palette set in `comic-style-memory-system`
- The two-layer look (painted depth behind, inked figures in front) can collapse into one treatment; store the background/figure treatment split as a style-memory asset
- Idealized heroic anatomy drifts toward generic; anchor jawline, build, and costume in the `comic-character-consistency-system` DNA sheet
- Narrator caption style (tone, border, placement) stays constant across chapters via `comic-world-bible-system`

## Prompt Block

```text
1930s-40s pulp adventure serial comic style, brush-inked figures with
confident thick-to-thin line and strong spot blacks, warm saturated
flat colors over an aged pulp paper base, ochre crimson and jungle
green palette, exotic locale backgrounds painted like matte paintings,
low heroic camera angles, idealized athletic anatomy, dynamic diagonal
action staging, serial narrator caption boxes, cliffhanger framing,
vintage adventure magazine energy.
```

## Style Quality Gates

- [ ] Palette sits on the warm aged-paper base in every panel — no cool digital white
- [ ] Figures brush-inked with visible swell; backgrounds keep the painted-depth treatment
- [ ] Hero staged from a low angle at least once per strip or page
- [ ] Action beats connect action-to-action with no dead panels
- [ ] Final panel lands a true reversal or a true cliffhanger — never a shrug

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` or `multi-page-chapter`; patterns `setup-reinforce-turnaround`, `parallel-action`

---

*Momentum is the contract: every panel a promise, every ending a hook.*
