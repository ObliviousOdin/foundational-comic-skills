---
name: saturday-morning-cartoon-comic
version: 2.0.0
category: comic-styles
description: 1980s–90s Saturday-morning TV animation cel style — uniform closed outlines, flat cel fills with one two-tone shadow pass, squash-and-stretch energy over painted-gouache backgrounds.
---

# Saturday Morning Cartoon Comic

**Style Lock (do not deviate)**

- 1980s–90s Saturday-morning TV animation cel look: broadcast-era production discipline transposed to the comics page
- Bold uniform outlines: single consistent weight, every shape closed and clean — like a xeroxed cel line
- Flat cel color fills plus **exactly one two-tone shadow pass** per color (base + one darker shade); no third tone, no gradients
- Saturated, optimistic palette tuned for CRT brightness — primaries and friendly secondaries
- Squash-and-stretch pose language: anticipation, extreme, settle; expressions exaggerated but always on-model
- Painted-gouache background feel (soft brushy fields, simplified shapes) deliberately contrasting cel-flat characters — animation's cel-over-background look
- Model-sheet discipline: characters drawn as if traced from a turnaround sheet, same head construction every panel
- Rounded panel corners and bouncy staging energy

## Negative Locks

- No rendered lighting, gradients, airbrush glow, or rim light on characters — cel flats and one shadow tone only
- No line-weight variation or sketchy, rough inking; outlines stay uniform and closed
- No gritty, muted, or noir palettes; no horror imagery
- No anime grammar (tone fields, sweat drops, chibi snaps) — this is Western broadcast cartoon language
- No off-model drift: proportions change only through sanctioned squash-and-stretch, then snap back
- No painterly rendering on characters (painterly belongs to backgrounds alone)

## When to Use

- All-ages adventure, chase comedy, team hijinks, big-hearted action with zero real danger
- Reference images cueing brightness, motion, toy-like color, or playful confidence
- Gag-escalation strips where energy must rise panel by panel

## When Not to Use

- Cute-proportion sticker humor → use `chibi-kawaii-comic`
- Vintage four-color superhero print texture → use `golden-age-superhero-comic` or `silver-age-pop-comic`
- Pen-and-ink domestic strip humor → use `classic-newspaper-comic`

## Story Harness (Image-Driven)

- Translate the four cues into a **mission-sized want**: catch it, win it, fix it before the commercial break
- **SETUP**: full-body pose stating the want against a bright painted establishing background; plant the gag prop (skateboard, gadget, runaway sandwich)
- **REINFORCE**: escalate with animation language — anticipation pose, then the extreme: stretch on launch, squash on impact; smear-frame and dust-cloud devices sanctioned; background simplifies as speed rises
- **TURNAROUND**: triumphant or silly — the win lands big or the backfire lands funny; hero pose or dazed-stars pose, always safe, always recoverable; biggest panel with the brightest palette hit

## World Guardrail

- Default to bright suburban-adventure settings: backyards, treehouses, school gyms, malls, secret clubhouses, cartoon cityscapes
- Gadgets welcome but toyetic — chunky, rounded, candy-colored; nothing genuinely dangerous ever fires
- Era anchor circa broadcast-1990: boomboxes, walkie-talkies, arcade cabinets over smartphones

## Dialogue & Lettering

- Bouncy rounded bubbles with thick even strokes; bold hand-lettered caps with emphasis swells
- 1–2 bubbles per panel, ≤ ~10 words; the catchphrase lands in the turnaround
- SFX policy: big outlined cartoon SFX (WHAM, ZIP, SPROING) allowed whenever the action demands — color-filled, integrated with the impact, one per panel maximum

## Direction Notes

- Camera diet: full-body and medium shots dominate (poses are the acting); dutch tilts for chaos; close-up only for the reaction take
- Transition diet: action-to-action almost exclusively — the gag escalator; one moment-to-moment hold for the anticipation beat before the payoff
- Pacing: tight, even gutters keep broadcast tempo; payoff panel widest; no panel goes static — every frame holds a pose, not a stand
- Backgrounds carry painted detail in setup, then collapse to color fields at the climax

## Consistency Notes

- **What drifts first**: outline weight and palette saturation; both are single project-wide values — lock them in style memory (`comic-style-memory-system`)
- Model-sheet discipline is the consistency system: the DNA template stores the turnaround (front, three-quarter, profile) and the base+shadow tone pair for every costume color
- Squash-and-stretch is sanctioned distortion, but silhouettes must snap back on-model in the next panel; re-anchor every 6–8 panels
- Background painter and cel inker are different "hands": keep the gouache-vs-flat contrast constant or the world merges into the characters

## Prompt Block

```text
1980s-90s Saturday-morning TV cartoon cel style, bold uniform
closed outlines at a single weight, flat cel color fills with
exactly one darker two-tone shadow pass, bright saturated
optimistic palette, squash-and-stretch character poses with
exaggerated readable expressions, soft painted-gouache
backgrounds contrasting crisp cel-flat characters, on-model
animation construction, rounded panel corners, bouncy energetic
staging, clean broadcast animation finish.
```

## Style Quality Gates

- [ ] Outline weight uniform across every character in every panel
- [ ] Exactly two tones per color region (base + one shadow); zero gradients
- [ ] Characters on-model against the turnaround sheet — squash-and-stretch snaps back
- [ ] Backgrounds read painted-gouache while characters read cel-flat; the contrast is visible
- [ ] SFX appear only on genuine impacts, one per panel at most

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal`; patterns `gag-escalation` and `setup-reinforce-turnaround`

---

*Cartoons earn their energy with discipline: every wild pose sits on a locked model sheet.*
