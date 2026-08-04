---
name: chibi-kawaii-comic
version: 2.1.0
category: comic-styles
description: Sticker-flat chibi kawaii comics — locked 2-head proportions, a five-swatch pastel palette, emoji-grammar faces, and thick rounded outlines for silly-sweet gag strips.
---

# Chibi Kawaii Comic

**Style Lock (do not deviate)**

- Chibi kawaii style with the **2-head proportion locked**: head height equals body height for every character in every panel, no exceptions
- Pastel palette discipline: 4–5 named swatches per project (default: blossom pink, cream, mint, powder blue, soft lilac) plus paper white — nothing outside the set
- Thick rounded outlines at one uniform heavy weight, drawn in soft charcoal or warm cocoa (never harsh pure black), every shape closed and sticker-like
- Emoji-grammar expressions: faces snap between a fixed symbolic set — dot eyes, squint arcs, sparkle-O eyes, wavy mouth — drawn symbols, never rendered emotion
- Sticker-flat shading: flat fills with at most one soft pastel shadow tone per swatch; no gradients, no rendered light
- Backgrounds in the same rounded grammar: flat pastel fields or simple dot/stripe patterns; props toy-round
- Oversized emotion props sanctioned (giant sweat drop, heart, anger cross, sparkle burst) — one per panel maximum, fixed designs

## Negative Locks

- No realistic anatomy or proportion drift — heads never shrink toward 3-head bodies
- No rendered shading, gradients, airbrush, or dramatic lighting
- No saturated neon or dark moody palettes; pastels only
- No fine detail linework (lace, hatching, texture); shapes stay sticker-simple
- No horror, gore, or genuinely mean beats — distress is always cute-coded
- No screentone or print-texture artifacts

## When to Use

- Gag strips, mascot humor, pet logic, snack-sized daily-life jokes, silly-sweet friendship beats
- Reference images cueing roundness, softness, toy-like charm, or exaggerated cuteness
- 4-koma rhythm where each panel is one clean, emoji-readable beat

## When Not to Use

- Romance with period texture and interiority → use `shoujo-romance-manga`
- All-ages action energy with cel-animation discipline → use `saturday-morning-cartoon-comic`
- Quiet contemplative atmosphere → use `ink-wash-storybook-manga`

## Story Harness (Image-Driven)

- Translate the four cues into **one tiny absurd want** (snack, nap, attention) — chibi stakes are huge feelings about small things
- **SETUP**: state the want with a full-body mid-pose against a flat pastel field; one toy-round prop carries the premise
- **REINFORCE**: escalate through the emoji grammar — expression snaps bigger, the emotion prop appears, body language inflates; this is `gag-escalation`'s rising rung
- **TURNAROUND**: silly-sweet — the want resolves sideways into cuteness (shared snack, accidental hug, triumphant nap); biggest expression of the strip; never mean, never sad without sweetness

## World Guardrail

- Default to cozy miniature worlds: kitchens, desks, sofas, parks, bakeries — anywhere snacks and naps live
- Props rounded and toy-like; technology allowed but drawn cute (round phone, smiling rice cooker)
- Animals and mascots are first-class citizens and obey the same 2-head law

## Dialogue & Lettering

- Puffy rounded bubbles matching the outline weight; tails short and thick
- 0–2 bubbles per panel, ≤ ~6 words; many beats land on expression alone
- SFX policy: cute onomatopoeia encouraged ("pyon", "munch", "zzz") in bubble-rounded letterforms filled from the palette — one per panel

## Direction Notes

- Camera diet: flat frontal and three-quarter mediums; full-body shots dominate because the proportion is the joke; close-ups only for expression snaps
- Transition diet: action-to-action up the escalation ladder; one moment-to-moment deadpan hold before the payoff; never scene-to-scene inside a strip
- Pacing: even 4-koma panel heights and even gutters — metronome regularity is what makes escalation read
- The final panel may break exactly one rule (a character leaning on the border) as the release valve

## Consistency Notes

- **What drifts first**: head-to-body ratio (creeps toward 3-head) and palette sprawl (stray tints sneak in); lock the ratio in the DNA template and the named swatches in style memory (`comic-style-memory-system`)
- The expression set is an asset: enumerate each character's allowed emoji-faces in the DNA sheet and reuse them exactly
- Outline weight is a single project-wide value; re-anchor against the canonical sheet every 8–10 panels
- Emotion props have fixed designs — draw the sweat drop, heart, and anger cross once, reuse forever

## Prompt Block

```text
Chibi kawaii comic style, locked two-head super-deformed
proportions, thick rounded uniform outlines in soft charcoal,
sticker-flat pastel fills from a small fixed swatch set of
blossom pink, cream, mint and powder blue, single flat pastel
shadow tone, emoji-style symbolic faces with dot eyes and simple
mouth shapes, oversized cute emotion icons, flat pastel
backgrounds with simple dot or stripe patterns, adorable toy-like
sticker finish.
```

## Style Quality Gates

- [ ] Every character measures exactly 2 heads tall in every panel
- [ ] All fills come from the named project swatch set — zero stray tints
- [ ] Outline weight uniform and rounded everywhere, bubbles included
- [ ] Expressions use the enumerated emoji set, never rendered realistic emotion
- [ ] At most one oversized emotion prop per panel, matched to the beat

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `4koma-vertical` or `2x2-grid-page` — the same four beats, folded into a grid instead of a column; patterns `gag-escalation` and `kishotenketsu`

---

*Chibi compresses emotion into proportion.*
