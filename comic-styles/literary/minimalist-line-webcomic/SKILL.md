---
name: minimalist-line-webcomic
version: 2.0.0
category: comic-styles
description: Radical-economy webcomic — thin uniform line, stick-to-simple figures, vast white space, one essential prop, and timing carried entirely by placement and silence.
---

# Minimalist Line Webcomic

**Style Lock (do not deviate)**

- **Thin uniform line** with zero weight variation — fixed-width fineliner feel (~0.3mm), identical on figures, props, and borders
- **Stick-to-simple figures**: heads as plain circles, dot eyes, bodies in a few strokes; expression carried by posture and at most two facial marks
- **Vast white space**: at least ~60% of every panel left empty; placement inside that emptiness IS the composition
- **No backgrounds beyond one essential prop** per scene (a chair, a door, a ledge); a ground line is optional, and nothing else exists
- Black on white only — no shading, no gray fills, no texture, no color
- Panel borders thin single rules or absent entirely; gutters generous
- **Timing carried by placement and silence**: an empty beat panel and a figure shifted two steps left are this style's special effects
- Era anchor: 2000s–2010s web-native minimal strip lineage — drawn like a diagram, timed like standup

## Negative Locks

- No shading, hatching, gradients, screentone, texture, or color of any kind
- No scenery or environmental detail beyond the single essential prop
- No rendered anatomy, hairstyles, fashion detail, or facial rendering beyond minimal marks
- No line-weight variation, brush taper, or sketchy construction lines
- No decorative lettering, display SFX, or emanata clusters (one small mark allowed only when load-bearing)

## When to Use

- Concept-driven humor, observational or philosophical strips, absurd premises played straight
- Reference images whose cues suggest wit, irony, or quiet absurdity over atmosphere
- When the idea must carry everything and any rendering would dilute the timing

## When Not to Use

- Memoir interiority with captions and lived detail → use `autobio-indie-literary-comic`
- Polished family-strip charm with sets and props → use `classic-newspaper-comic`
- Cute reaction-face energy and mascots → use `chibi-kawaii-comic`

## Story Harness (Image-Driven)

- Translate the four cues into one clean premise stated visually, then escalated by its own logic; strip away everything that is not the idea
- **SETUP**: the premise in its plainest form — figure plus the one essential prop, placed off-center with intent; the first line establishes the rule of the bit
- **REINFORCE**: the rule applied once more, slightly escalated — near-identical composition with one deliberate delta (a step closer, a second figure, the prop moved); the repetition is the joke's load-bearing wall; a silent beat panel is legal here
- **TURNAROUND**: **deadpan insight** — the logical endpoint stated flatly, the visual barely changing while the meaning flips; earned when panels 1–2 built a pattern the last line completes or quietly breaks; no mugging, no exclamation

## World Guardrail

- Default setting: nowhere — white void plus one prop; if a place must exist, it is named in dialogue or implied by the prop, never drawn
- Props timeless-generic (chair, phone, door, plant): whatever the premise needs, and only that
- Physics and continuity bend freely in service of the bit, but the rule established in panel 1 is never violated unannounced

## Dialogue & Lettering

- Plain text floated near the speaker, or thin-line ovals with straight tails; hand-set lowercase or small caps at one size throughout — per `comic-lettering-and-balloons`, these are the only deltas; caption boxes remain forbidden
- ≤ 2 short lines per panel, ≤ ~12 words; word choice is this style's only ornament — edit lines like jokes, because they are
- SFX policy: none; silence is the soundtrack, and a beat panel outranks any sound effect

## Direction Notes

- Camera diet: one flat eye-level "stage" framing per strip, held; the camera never moves unless the move IS the joke
- Transition diet: subject-to-subject and action-to-action across near-identical frames; moment-to-moment repetition supplies the beat panel; never scene-to-scene mid-strip
- Pacing: even panels, wide gutters; in `gag-escalation`, keep the deltas between panels small and countable — readers must be able to diff the panels at a glance

## Consistency Notes

- **What drifts first**: rendering creep — the line gains weight variation, faces grow features, props acquire neighbors; restate "fixed-width line, two face marks, one prop" in `comic-style-memory-system` every batch
- Identity is silhouette plus one signature mark (a hat brim, glasses, a hair squiggle); lock it in the DNA template — it is the entire costume department
- Figure scale and baseline must hold across panels or the placement-timing collapses; grid-check alignment at review
- White space erodes panel by panel; measure it — emptiness is a tracked asset here

## Prompt Block

```text
Minimalist line webcomic style, thin fixed-width black pen line with no
weight variation, stick-to-simple figures with circle heads and dot
eyes, expression through posture alone, vast empty white space filling
most of each panel, no background beyond one essential prop, optional
ground line, black on white only with no shading or texture, thin or
absent panel borders, deadpan diagram-clean web-native cartooning.
```

## Style Quality Gates

- [ ] Line width uniform everywhere — no taper, no thick-thin modulation
- [ ] White space ≥ ~60% per panel; nothing drawn that the premise does not require
- [ ] One essential prop maximum per scene; zero environmental detail beyond it
- [ ] Panels 1–2 differ by small countable deltas; the repetition pattern is legible
- [ ] Turnaround delivered deadpan — no exclamation marks, emanata bursts, or mugging

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` or `single-panel-gag`; patterns `gag-escalation`, `setup-reinforce-turnaround`, `silent-strip`

---

*Minimalism is not less effort. It is all the effort, made invisible.*
