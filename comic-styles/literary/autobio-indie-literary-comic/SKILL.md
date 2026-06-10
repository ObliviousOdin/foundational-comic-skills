---
name: autobio-indie-literary-comic
version: 2.0.0
category: comic-styles
description: Memoir-register indie literary comics — precise thin pen line, flat two-tone or grayscale palette, deadpan grids, and caption-led introspection where mundane detail carries the feeling.
---

# Autobio Indie Literary Comic

**Style Lock (do not deviate)**

- One coherent memoir register held project-wide: **precise thin pen line** (fine technical nib, near-uniform weight), observational and unglamorous figure drawing — bodies slouch, clothes wrinkle
- Palette: **flat restrained two-tone** (grayscale plus one muted spot color) **or pure grayscale** — chosen once per project and never expanded
- **Deadpan grid layouts**: regular 4/6/9-panel grids with even gutters; no diagonal panels, no splash drama, no bleeds
- **Mundane detail as emotional carrier**: kettles, bus seats, inboxes, kitchen tables drawn with patient specificity — the props do the testifying
- **Caption-driven introspection is native here**: the remembering "I" speaks in rectangular caption boxes while the panels show the unremarkable scene
- Backgrounds minimal but truthful — a believable room with three honest objects beats a rendered one
- Era anchor: 1990s–2000s alternative/literary comics print register, zine-to-graphic-novel lineage

## Negative Locks

- No heroic anatomy, action posing, or dynamic foreshortening
- No drama lighting, speedlines, glow, or rendered atmosphere
- No spectacle props — explosions, monsters, fantasy gear; the stakes are interior
- No saturated multi-hue palettes or gradient fills
- No exaggerated cartoon emotion faces; the expression range stays small and human

## When to Use

- Memoir, personal essay, quiet fiction: family, work, illness, moving away, the email never sent
- Reference images cueing ordinary rooms, errands, solitary figures, gray weather
- When the meaning should arrive in a caption laid over an unremarkable image

## When Not to Use

- Concept-gag economy with no interiority → use `minimalist-line-webcomic`
- Raw transgressive satire and scratchy excess → use `underground-zine-comix`
- Cinematic adult drama in heavy blacks → use `gekiga-cinematic-manga`

## Story Harness (Image-Driven)

- Translate the four cues into a remembered moment narrated from a small distance — what happened, and what the narrator only now notices about it
- **SETUP**: the ordinary scene established in flat grid calm — figure mid-task (washing up, waiting, scrolling); the first caption sets the remembering voice; plant one mundane object drawn with care
- **REINFORCE**: the moment continues almost unchanged — small action-to-action steps; the captions begin to diverge from the image (the voice admits what the body won't show); the planted object recurs
- **TURNAROUND**: **poignant, ambiguous, or quietly revelatory — never a punchline**; the planted object or a near-identical repeated panel returns carrying new weight; earned when caption and image say two true things at once; often the caption falls silent here

## World Guardrail

- Default settings: apartments, kitchens, buses and trains, offices, clinics, parents' houses — present-day or recent-past ordinary life
- Props contemporary and specific (the right mug, the right phone era for the memory); brand-adjacent, never logo-forward
- Weather is allowed to be gray; seasons mark chapters of a life, not spectacle

## Dialogue & Lettering

- **Caption boxes are this style's licensed exception** (per `comic-lettering-and-balloons`, captions are forbidden by default elsewhere): rectangular, thin-ruled, first-person memoir voice — ≤ 2 per panel, ≤ ~15 words each, and each must add interiority or hindsight, never describe what the panel already shows
- Speech in plain small ovals, lowercase hand-lettered feel, ≤ 2 per panel; spoken lines stay banal on purpose — the captions carry the meaning
- SFX policy: near-zero — tiny lowercase sounds (tick, hum, ding) at most once per strip

## Direction Notes

- Camera diet: locked-off medium shots at eye level; repeated compositions welcome (same chair, same angle, different day); close-ups rationed to one per strip
- Transition diet: moment-to-moment and action-to-action for lived time; one scene-to-scene jump (then/now) is the memoir's signature cut
- Pacing: metronomic — even gutters, equal panel sizes; meaning comes from repetition with one small difference, never from layout emphasis

## Consistency Notes

- **What drifts first**: the register itself — the line thickens toward cartoon or renders toward realism, and the spot color saturates; restate "thin uniform pen, flat two-tone" in `comic-style-memory-system` and recheck every batch
- The narrator's face must stay plain and repeatable; lock a simple feature recipe in the DNA template and re-anchor every 6–8 panels
- Recurring rooms and objects are continuity anchors — give the apartment and the planted object their own bible entries
- Caption discipline erodes toward narrating the obvious; audit every caption against its panel at review

## Prompt Block

```text
Indie autobiographical literary comic style, precise thin technical-pen
linework with near-uniform weight, flat restrained grayscale with one
muted spot color, regular deadpan panel grid with even gutters,
observational unglamorous figures in ordinary interiors, patient
mundane detail of household objects, rectangular first-person caption
boxes, lowercase hand-lettered feel, quiet 1990s-2000s alternative
comics print register, no drama lighting or action posing.
```

## Style Quality Gates

- [ ] Line weight thin and near-uniform throughout; no rendered-shading creep
- [ ] Palette holds to grayscale plus at most one muted spot color
- [ ] Grid regular with even gutters; no diagonal, bleed, or splash panels
- [ ] Every caption adds interiority or hindsight — none merely describes its image
- [ ] The turnaround lands without a joke: poignant, ambiguous, or quietly revelatory

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` or `multi-page-chapter`; patterns `setup-reinforce-turnaround`, `slow-burn-reveal`, `kishotenketsu`

---

*Draw the dishes honestly enough and the grief will be in them.*
