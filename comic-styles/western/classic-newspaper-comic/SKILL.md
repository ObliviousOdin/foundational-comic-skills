---
name: classic-newspaper-comic
version: 2.0.0
category: comic-styles
description: Mid-century American syndicated daily strip — bold uniform Brause-nib ink on white, bigfoot-simplified anatomy, hand-lettered caps, and wholesome gag timing built for the funnies page.
---

# Classic Newspaper Comic

**Style Lock (do not deviate)**

- Mid-century American syndicated daily strip (1950s–70s funnies-page era), black India ink on white bristol — no color, no gray washes
- **Bold uniform ink line** with Brause-nib snap: one confident contour weight throughout, closed shapes, strong silhouettes that read at postage-stamp size
- **Bigfoot-school simplified anatomy**: oversized heads and feet, dot or button eyes, single-stroke mouths, mitt-shaped hands — expression carried by eyebrows and posture, never by rendering
- Minimal hatching: at most three or four parallel strokes for a shadow or blush; tone comes from spot blacks and white space, never gradients
- **White background discipline**: empty white behind figures by default; one or two props (a lamp, a fence line, a horizon stroke) only when the gag requires them
- Daily-strip economy — every line earns its ink; if a detail does not serve the gag, it does not exist
- Hand-lettered all-caps dialogue; hand-ruled rectangular panel borders with even gutters

## Negative Locks

- No color, gray gradients, screentone, or digital shading of any kind
- No realistic anatomy, rendered musculature, or detailed faces — simplification is the contract
- No background clutter: no detailed rooms, crowds, or texture creep behind the figures
- No variable brush calligraphy or sketchy multi-stroke linework; the contour is single, bold, and committed
- No manga emotion grammar (sweat drops, speed-line auras, chibi pop-outs)
- No cynical, gross-out, or mean-spirited visual punchlines — the strip stays syndicate-clean

## When to Use

- Family-friendly gags: domestic life, pets, kids, office mishaps, small everyday absurdities
- Reference images whose mood cues read cheerful, mischievous, or gently exasperated
- When the punchline must be readable in under two seconds on a crowded page

## When Not to Use

- Heroic action or spectacle → use `golden-age-superhero-comic` or `silver-age-pop-comic`
- Ironic, self-aware melodrama → use `pop-art-lichtenstein-comic`
- Transgressive or scratchy satire → use `underground-zine-comix`

## Story Harness (Image-Driven)

- Translate the four cues into one **small domestic premise with a clean reversal** — a single misunderstanding, scheme, or expectation
- **SETUP**: establish the normal in one readable beat — character plus one prop at eye level, full or three-quarter figure, white space framing the situation
- **REINFORCE**: escalate the same premise (`gag-escalation` logic) — the scheme proceeds, the expectation builds; repeat the staging so the change is the only thing that changes
- **TURNAROUND**: a **wholesome twist** — the tables turn kindly, the pet wins, the kid was right; never humiliating; the funniest drawing of the strip, often a deadpan stare or silent reaction beat

## World Guardrail

- Default to timeless mid-century suburbia: kitchens, backyards, sidewalks, school desks, doghouses, lemonade stands, office cubicles
- Props are everyday and durable — newspaper, rotary phone, sandwich, baseball mitt; no smartphones or screens unless the reference insists
- Weather as a gag instrument (one rain cloud, one snowball) drawn with the same economy as everything else

## Dialogue & Lettering

- Inherits comic-lettering-and-balloons defaults; deltas: hand-lettered all-caps, even letter height, generous bubble padding
- Smooth oval or rounded-rectangle balloons with short straight tails; thought balloons as cloud chains
- 1–2 balloons per panel, ≤ 10 words; the final panel earns the right to be silent
- SFX policy: one small hand-drawn effect maximum per strip (WHAM!, SPLAT!) in the same bold line as the art

## Direction Notes

- Camera diet: flat, eye-level, stage-play profile and three-quarter staging; full or medium-full shots; close-ups rare and saved for a reaction beat
- Transition diet: subject-to-subject and action-to-action; hold the same camera across panels so timing, not framing, delivers the joke
- Pacing: equal-width panels with even gutters — the metronome of the daily strip; a slightly wider final panel may hold the twist
- Repetition is a tool: identical compositions with one changed element are era-authentic comedy

## Consistency Notes

- **What drifts first**: head-to-body ratio and line weight — figures slide toward realism and the contour thins; lock both in the character DNA template
- White-space discipline erodes second: backgrounds accrete detail panel by panel; re-assert the empty-white default in `comic-style-memory-system`
- Re-anchor character silhouettes against the canonical sheet every 6–8 panels; bigfoot proportions are the identity
- Negative block above merges with character negatives via the world bible — never hand-edit merged output

## Prompt Block

```text
Classic mid-century American newspaper comic strip style, black India
ink on white, bold uniform nib line with confident closed contours,
bigfoot-school simplified cartoon anatomy with oversized heads and
feet and dot eyes, minimal hatching, solid spot blacks, empty white
backgrounds with at most one or two props, hand-ruled rectangular
panel borders, hand-lettered all-caps dialogue in smooth oval
balloons, clean syndicated funnies-page print feel.
```

## Style Quality Gates

- [ ] Line weight uniform across every panel — no thinning, no brush swell
- [ ] Backgrounds hold white-space discipline (two props maximum unless the gag demands more)
- [ ] Anatomy stays bigfoot-simplified; zero realistic rendering creep
- [ ] Punchline panel reads in under two seconds at thumbnail size
- [ ] Lettering is hand-lettered caps and sits balanced inside its balloon

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` or `single-panel-gag`; patterns `gag-escalation`, `setup-reinforce-turnaround`, `silent-strip`

---

*Three panels, one joke, no wasted ink — the funnies page forgives nothing else.*
