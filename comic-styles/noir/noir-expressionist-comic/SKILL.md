---
name: noir-expressionist-comic
version: 2.0.0
category: comic-styles
description: Film-noir expressionist comic — grayscale wash and brush ink under a single hard key light, blind-bar shadows, dutch angles, and smoke-led compositions for morally ambiguous city stories.
---

# Noir Expressionist Comic

**Style Lock (do not deviate)**

- Film-noir / German-expressionist comic: **grayscale ink wash over brush-ink line** — no color, ever
- **Chiaroscuro with a single hard key light per panel**; every shadow must trace back to that one source
- Venetian-blind bars, stairwell rails, and window-frame shadows raking across faces and walls — the cage motif of the style
- **Dutch angles** as psychology: verticals lean exactly as much as the character's certainty does
- Cigarette smoke, steam, and fog drawn as deliberate compositional lines that lead the eye to the panel's subject
- Wet street reflections double every light source; the night city is a hall of mirrors
- Wash values held in locked bands between deep ink black and paper white — mid-tones are the medium, mud is the enemy
- Era anchor: 1940s–50s American noir city

## Negative Locks

- No color of any kind — not even a spot accent (that is `sin-city-graphic-noir` territory)
- No flat ambient lighting or multiple equal light sources in one panel
- No posterized pure black-and-white — the wash mid-tones must survive
- No digital gradients, lens flares, bloom, or photo textures
- No modern tech silhouettes: smartphones, LED signage, flat screens

## When to Use

- Detective fiction, betrayal, moral ambiguity, urban loneliness
- Reference images that read tense, isolated, rain-wet, or lit by one source
- Strips where the reveal is an emotional truth, not a monster

## When Not to Use

- Absolute graphic contrast with no mid-tones → use `sin-city-graphic-noir`
- Supernatural escalating dread → use `junji-ito-body-horror` or `horror-ec-comics-style`
- Warm humane city slice-of-life → use `autobio-indie-literary-comic` or `retro-hand-inked-manga-comic`

## Story Harness (Image-Driven)

- Runs `slow-burn-reveal` as interior noir: the WITHHOLD is what the protagonist refuses to admit
- **SETUP** (WITHHOLD): a figure alone with the key light; the shadow geometry hides one face or object; smoke or rain establishes the line of sight toward what is withheld
- **REINFORCE** (HINT): the key light narrows or shifts; blind-bar shadows tighten like a cell; the dutch angle increases; a reflection shows what the figure will not look at
- **TURNAROUND** (REVEAL): **earned, honest, sometimes bitter** — the truth steps into the key light; the angle rights itself or tips completely; the value range opens to its widest, deepest black beside cleanest white

## World Guardrail

- Default 1940s–50s noir city: rain-wet streets, office blinds, neon hotels, stairwells, dive bars, dockyards
- Props: trench coats, fedoras, rotary phones, desk lamps, big sedans, cigarettes
- Night and rain are the default weather; daylight appears only as an alibi — rare and ironic

## Dialogue & Lettering

- First-person caption boxes in a weary register: rectangular, unobtrusive, lower-third placement; inherits `comic-lettering-and-balloons`
- Budget: 1 caption OR 1–2 bubbles per panel, ≤ ~12 words; the reveal is often one bitter line, or silence
- SFX policy: nearly none — rain, footsteps, and gunshots earn at most one small SFX per strip

## Direction Notes

- Camera diet: medium and close shots through foreground obstructions (blinds, door frames, smoke); one high-angle "trapped" wide allowed per strip
- Transition diet: moment-to-moment and subject-to-subject; scene-to-scene only to relocate the dread (per `comic-narrative-patterns`)
- Pacing: even gutters, then a wide gutter before the reveal; hold one beat on an empty object panel (ashtray, dripping hat brim) before the turn
- Light continuity is a directing duty: log the key-light direction per scene in the shot plan and keep it

## Consistency Notes

- **What drifts first**: light-source discipline — shadows begin contradicting the key light; verify every panel against the logged key direction and regenerate violators
- Wash values drift toward uniform mid-gray mud; lock the value bands as a `comic-style-memory-system` asset
- Blind-bar geometry (slat spacing, angle) is a recurring prop — keep its ruling consistent across the strip
- Faces under heavy shadow lose identity first; re-anchor silhouette and jawline against the `comic-character-consistency-system` DNA sheet

## Prompt Block

```text
Film noir expressionist comic style, grayscale ink wash over brush
line, hard single-source chiaroscuro lighting, venetian blind and
stairwell shadows raking across faces, dutch angle compositions,
cigarette smoke drawn as leading lines, rain-wet streets doubling neon
and lamplight in reflection, deep ink blacks with controlled wash
mid-tones, 1940s American noir city, trench coats and desk lamps,
brooding cinematic framing.
```

## Style Quality Gates

- [ ] Every shadow in a panel traces to its single key light
- [ ] At least one panel uses blind-bar or rail shadows as a psychological cage
- [ ] Wash values hold their locked bands — no uniform gray mud
- [ ] Dutch angle degree tracks the character's certainty across the strip
- [ ] Smoke, steam, or rain lines lead the eye to the panel's subject

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal`; patterns `slow-burn-reveal` (native), `setup-reinforce-turnaround`

---

*Noir uses light as a character: it shows only what the city is ready to admit.*
