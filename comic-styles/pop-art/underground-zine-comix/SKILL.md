---
name: underground-zine-comix
version: 2.0.0
category: comic-styles
description: 1960s–70s underground comix and punk zine style — scratchy dip-pen wonk, obsessive crosshatch, and photocopier grit for biting, absurd gag-escalation strips.
---

# Underground Zine Comix

**Style Lock (do not deviate)**

- 1960s–70s underground comix / punk zine: black and white **photocopy aesthetic**, built for the mimeograph and the merch table
- **Scratchy rapidograph and dip-pen line**: nibs catch, ink blots, strokes overshoot — deliberate wonk is the contract, not a defect
- Dense **obsessive crosshatching** for all tone; no screentone, no wash, no gray fills
- **Photocopier grit** baked into the page: toner blotch, edge burn, slight skew, generation-loss speckle — one consistent treatment project-wide
- **Hand-cut paste-up borders**: uneven rules, collage edges, visible correction patches
- Rubbery exaggerated cartoon anatomy: big feet, sweat beads, bulging eyes, straining necks
- **Anti-polish doctrine**: if a panel looks like a professional product, it is wrong — regenerate it scuzzier

## Negative Locks

- No digital cleanliness: no vector line, anti-aliased smoothness, or uniform stroke weight
- No color, gradients, airbrush, or screentone
- No corporate-comic polish: no heroic idealized anatomy, no glossy rendering
- No sanitized layout: borders must not be ruler-straight, lettering must not sit on perfect baselines
- No photo textures beyond the locked photocopier-grit treatment

## When to Use

- Satire, rants, confessionals, counterculture gags, biting social commentary
- Reference images that read raw, defiant, scuzzy, or DIY
- When escalation into absurdity is the engine — `gag-escalation` is native here

## When Not to Use

- Sincere quiet introspection without bite → use `autobio-indie-literary-comic` or `minimalist-line-webcomic`
- Slick ironic pop with Ben-Day dots → use `pop-art-lichtenstein-comic`
- Family-friendly syndicated gags → use `classic-newspaper-comic`

## Story Harness (Image-Driven)

- Runs `gag-escalation` natively — the rule of three: state the premise, escalate it, break the scale
- **SETUP** (beat 1): the grievance stated deadpan in scuzzy normalcy — crank character, mundane complaint, crosshatched clutter; locked framing
- **REINFORCE** (beat 2): same framing, bigger absurdity — the grievance escalates one notch; hatching density, sweat beads, and bubble cramming escalate with it; parallel framing is the joke's metronome
- **TURNAROUND** (blow-off): **absurd or biting** — the scale breaks: cosmic, grotesque, or bluntly political; the panel may rupture its own border; never a polite chuckle, always a snort or a sting

## World Guardrail

- Default scuzzy counterculture spaces: head shops, basement shows, kitchen tables, picket lines, late-night diners — 60s–70s or timeless punk
- Authority figures and brand-like parodies are fair targets; keep parody generic (invented logos, no real trademarks)
- Tech stays analog: tube TVs, mimeographs, payphones, beater cars

## Dialogue & Lettering

- Hand-scrawled lettering on uneven baselines; crammed bubbles that bump their contents; inherits `comic-lettering-and-balloons` budgets but defies its tidiness on purpose
- Budget: up to 2 bubbles plus optional scrawled marginalia per panel; a rant is permitted in beat 2, ≤ ~15 words
- SFX policy: liberal and hand-scrawled, integrated into the hatching — one per panel is fine

## Direction Notes

- Camera diet: locked, repeated framing across beats 1–2 (the deadpan metronome), then one violent reframe — extreme wide or grotesque close-up — for the blow-off
- Transition diet: action-to-action with parallel framing; keep transitions invisible per `comic-narrative-patterns` gag-escalation law
- Pacing: tight, even gutters; the blow-off panel may be widest and may break its border
- Background clutter is content: hide secondary jokes in the crosshatch for the second read

## Consistency Notes

- **What drifts first**: the wonk gets sanitized — lines straighten and borders square up under generation pressure; lock a "wobble floor" reference set in `comic-style-memory-system` and regenerate anything cleaner
- Photocopier grit must be one consistent treatment, not a random filter per panel; store it as a style-memory texture asset
- Anatomy is rubbery but bounded: record exaggeration *ranges* (not fixed measures) in the `comic-character-consistency-system` DNA sheet
- The artist-hand hatching direction habit must stay constant across the strip

## Prompt Block

```text
1960s-70s underground comix zine style, black and white, scratchy
rapidograph and dip-pen linework with ink blots and deliberate wobble,
dense obsessive crosshatching, rubbery exaggerated cartoon anatomy
with big feet and sweat beads, photocopier grit with toner blotches
and edge burn, hand-cut paste-up panel borders, hand-scrawled
lettering, cluttered scuzzy backgrounds, raw DIY punk print energy,
defiantly unpolished.
```

## Style Quality Gates

- [ ] Line wobble and ink accidents visible in every panel — zero vector cleanliness
- [ ] Beats 1–2 share framing; the blow-off panel visibly breaks the pattern
- [ ] Photocopier grit treatment identical across all panels
- [ ] Borders and lettering read hand-made: uneven, alive, unsanitized
- [ ] At least one background detail rewards a second read

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` (also `single-panel-gag`); patterns `gag-escalation` (native), `setup-reinforce-turnaround`

---

*Zine comix treats imperfection as voice: the smudge is the signature.*
