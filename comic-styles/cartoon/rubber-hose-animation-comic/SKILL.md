---
name: rubber-hose-animation-comic
version: 2.0.0
category: comic-styles
description: Late-1920s to early-1930s theatrical cartoon grammar — boneless hose limbs, circular construction, pie-cut eyes, grey-wash monochrome, and a world where the scenery performs on the beat.
---

# Rubber-Hose Animation Comic

**Style Lock (do not deviate)**

- Late-1920s to early-1930s **theatrical rubber-hose** animation — the early sound-cartoon era, transcribed to panels
- **Boneless hose limbs**: arms and legs curve in continuous arcs with no elbows, knees, or articulation — a hose, never a skeleton
- **Circular construction**: heads, torsos, hands, props, and vehicles all built from circles and ovals
- Black and white with **grey wash** value only — a three-value range of paper white, mid wash, and spot black; the palette is film stock, not paint
- **Pie-cut eyes**, four-finger white gloves, oversized rounded shoes
- **Everything is alive**: tenements sway, trees smile, furniture dances — the inanimate world is a supporting cast, never set dressing
- **Visible boil**: contour and volume wobble slightly, as hand-inked cels do; the imperfection is the signature, not an error to correct
- Perpetual **musical rhythm** — the world moves on a beat and poses land on the downbeat

## Negative Locks

- No joints, elbows, knees, or anatomical articulation anywhere
- No color — grey wash only, unless the project contract explicitly grants a hand-tinted pass
- No clean vector line, uniform digital stroke, or perfectly steady contour; smoothing out the boil kills the style
- No realistic anatomy, proportion, or musculature
- No cel-era two-tone shadow blocking or bright saturated palettes — that is `saturday-morning-cartoon-comic`
- No post-1934 props, technology, or signage; the era lock is absolute

## When to Use

- Slapstick, musical, and vaudeville-shaped gags where physics is negotiable
- Reference images of round bouncy forms, dancing figures, animals, or absurd machinery
- When the *world itself* should perform rather than merely contain the action

## When Not to Use

- Bright saturated TV-cel action and on-model heroics → use `saturday-morning-cartoon-comic`
- Cute rounded modern character comedy → use `chibi-kawaii-comic`
- Scratchy transgressive underground humour → use `underground-zine-comix`

## Story Harness (Image-Driven)

- Translate the four cues into a **musical escalation**: an ordinary task becomes a dance, the dance becomes chaos, the chaos resolves exactly on the beat
- **SETUP**: establish tempo and place — the figure already moving to an implied rhythm, the scenery swaying along with it
- **REINFORCE**: the world joins in. Props animate, the environment participates, the complication is physical and absurd — never cruel, never mean
- **TURNAROUND**: **the beat lands** — an impossible physical payoff: a stretch, a swallow, a body becoming a shape. "Earned" means the gag obeyed the cartoon's own physics consistently, not that it obeyed real ones

## World Guardrail

- 1928–1934 America and its cartoon dreamscape: vaudeville stages, steamboats, farmyards, swaying city tenements
- Technology period-locked — crank telephones, gramophones, jalopies, steam whistles, hand-cranked machinery
- Cartoon physics apply, but *consistently*: gravity waits for the punchline and elasticity is universal, so a rule bent once is bent for everyone
- Signage and printed matter stay period-plausible and sparse

## Dialogue & Lettering

- Inherits comic-lettering-and-balloons defaults; deltas: bouncy hand-lettered caps carrying the same wobble as the line boil
- Round oval balloons with curving tails, ≤ 2 per panel and ≤ 10 words — this style talks less and moves more
- **SFX are this style's licensed excess** (the sparse-SFX default is suspended): BOING, TOOT, PLINK lettered in rounded rubbery forms, one or two per beat
- Musical notes are permitted as lettering elements and often carry a beat better than a balloon

## Direction Notes

- Camera diet: flat theatrical staging, eye-level and side-on — a proscenium view, the reader in an audience seat
- Transition diet: action-to-action almost exclusively; the beat must feel continuous, so avoid scene-to-scene inside a gag
- Pacing: even panels and even gutters — a steady tempo is the joke's metronome; break the grid only for the payoff panel
- Stage **full figures**; this style lives in whole-body motion, and tight close-ups starve it of the thing that makes it work

## Consistency Notes

- **What drifts first**: joints appear. Limbs acquire elbows, the hose grammar dies, and the style becomes generic cartooning — re-assert the hose lock every batch in `comic-style-memory-system`
- Grey wash collapses toward a flat mid-grey second; pin the three-value range explicitly and check it per batch
- The boil gets "cleaned up" into vector smoothness across a sequence — re-request uneven hand-inked contour on every generation
- Glove, shoe, and eye-shape designs drift; lock them as fixed character assets rather than per-panel decisions
- Era props creep modern; re-anchor the 1928–1934 technology set every 8–10 panels

## Prompt Block

```text
Rubber-hose animation comic style, late 1920s to early 1930s
theatrical cartoon, black and white with grey wash values, boneless
noodle limbs curving without elbows or knees, circular construction
bodies, pie-cut eyes and four-finger white gloves, rounded organic
shapes throughout, smiling anthropomorphic buildings and trees,
visible line boil with uneven hand inking, vintage film grain and
soft vignette, hand-ruled rounded panel borders, bouncing musical
staging, early sound-cartoon print feel.
```

## Style Quality Gates

- [ ] Zero joints — every limb reads as one continuous curve at any zoom
- [ ] Monochrome with the three-value range intact: paper white, grey wash, spot black
- [ ] Line boil visible — no perfectly smooth vector contour survived the batch
- [ ] At least one inanimate element performs in the sequence (sways, smiles, dances)
- [ ] Full-figure staging dominant, and every prop verified against the 1928–1934 era lock

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` or `4koma-vertical`; patterns `gag-escalation`, `silent-strip`

---

*A hose bends where a bone would break — that is the entire physics of the era.*
