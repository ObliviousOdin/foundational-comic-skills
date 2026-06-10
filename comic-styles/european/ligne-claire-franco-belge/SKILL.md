---
name: ligne-claire-franco-belge
version: 2.0.0
category: comic-styles
description: Hergé-school ligne claire — one uniform line weight, zero hatching, flat unmodulated color zones, and documentary-precise backgrounds in the Franco-Belgian album tradition.
---

# Ligne Claire Franco-Belge

**Style Lock (do not deviate)**

- Hergé-school **ligne claire** (Brussels clear line), Franco-Belgian album tradition of the 1930s–70s
- **Absolutely uniform line weight** on every contour — the same pen width for a face, a teacup, and a distant cathedral
- **Zero hatching, zero feathering, zero screentone**: volume is implied by drawing and color placement, never by rendered shading
- **Flat unmodulated color zones** — album-gouache flats, one exact hue per zone, edge to edge
- **No cast shadows** by default; when the narrative demands one, it is a single stylized flat shape, not a gradient
- Precise, documentary-accurate architectural and mechanical backgrounds receiving **equal line treatment** to the figures — nothing sketched, nothing faded
- Slightly cartooned, economical faces over realistic settings — the signature ligne claire contrast
- Clear-line readability doctrine: every object in the panel identifiable at a glance

## Negative Locks

- No line-weight variation, brush swell, or tapering — modulation is the cardinal violation
- No crosshatching, stipple, feathering, or texture rendering of any kind
- No gradients, airbrush, soft shadows, or atmospheric haze; depth comes from drawing, not blur
- No painterly or sketchy passages — backgrounds may never drop to a looser finish than figures
- No photorealistic faces; the cast stays economically cartooned

## When to Use

- Adventure, mystery, travelogue, and procedural stories where the world's machinery matters
- Reference images suggesting curiosity, competence, and well-made places — trains, ports, observatories
- When maximum readability is the contract: every clue visible, every prop legible

## When Not to Use

- Shadow-built mood and moral murk → use `noir-expressionist-comic`
- Dense visionary sci-fi linework → use `moebius-metal-hurlant-sci-fi`
- Soft painted texture and lyric wash → use `watercolor-storybook-comic`

## Story Harness (Image-Driven)

- Translate the four cues into a **fair-play mini-mystery or errand** — a question the reader can solve from what is drawn
- **SETUP**: legible establishing shot — the figure in a precise, named-feeling place; the significant prop or detail plainly visible (clear-line doctrine forbids hiding it)
- **REINFORCE**: the complication staged through architecture and objects — a door ajar, a missing valise, a wrong uniform; camera steady, world calmly exact
- **TURNAROUND**: a **clever, tidy resolution** — the answer was on-panel from the start; "earned" means a re-reader can trace the clue chain; the world ends the strip back in good order

## World Guardrail

- Default to mid-century Europe and its routes outward: Brussels streets, grand hotels, steamships, sleeper trains, biplanes, consulates, mountain passes
- Vehicles, signage, and buildings drawn with researched plausibility — the reader should trust the world like a map
- Technology period-locked; weather rendered as drawn shapes (rain strokes, snow dots), never as atmosphere filters

## Dialogue & Lettering

- Inherits comic-lettering-and-balloons defaults; deltas: neat, even hand lettering with calm typeset regularity
- Rounded-rectangle and oval balloons with thin uniform borders — the same line weight as the art
- 1–2 balloons per panel, ≤ 12 words; information delivered crisply, exclamations reserved for real surprises
- SFX policy: small clean onomatopoeia (CRAC! BOUM!) in the uniform line, at most one per beat

## Direction Notes

- Camera diet: steady eye-level middle distance — the theatre-stage view; extreme angles only when the story physically requires them (a fall, a summit)
- Transition diet: action-to-action and subject-to-subject; scene-to-scene cuts bridged by a small caption
- Pacing: regular waffle-grid discipline with even gutters; panel size varies rarely and meaningfully
- Compose in clean depth planes — foreground figure, midground action, background architecture, all equally inked

## Consistency Notes

- **What drifts first**: line weight starts modulating and shadows creep under figures; pin the nib width and the no-shadow rule in `comic-style-memory-system`
- Color zones drift second — flats must reuse exact project swatches or the album look shimmers
- Background precision decays into sketchiness across a sequence; re-assert equal-treatment inking every batch
- Re-anchor faces against the canonical sheet every 8–10 panels; economical features drift toward realism fast

## Prompt Block

```text
Ligne claire Franco-Belgian comic style in the Hergé school,
absolutely uniform ink line weight on every contour, zero hatching
or feathering, flat unmodulated gouache color zones, no cast
shadows, slightly cartooned economical faces over precise
documentary architecture, equal line treatment for foreground and
background, clean depth planes, rounded speech balloons with thin
uniform borders, neat hand lettering, mid-century European album
print feel, maximum clear-line readability.
```

## Style Quality Gates

- [ ] One line weight everywhere — zoom test shows no swell, taper, or sketch strokes
- [ ] Zero hatching, gradients, or rendered shading in any panel
- [ ] Color zones perfectly flat and reused from the project swatch set
- [ ] Backgrounds as fully and precisely inked as the figures
- [ ] No cast shadows (or only the single stylized shape the beat demands)

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` or `multi-page-chapter`; patterns `setup-reinforce-turnaround`, `parallel-action`

---

*One line width for the whole world — clarity is the style's entire morality.*
