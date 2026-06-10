---
name: shoujo-romance-manga
version: 2.0.0
category: comic-styles
description: Classic 1970s–90s shōjo romance manga — fixed sparkle-highlight eyes, flowing hair mass, floral emotion backgrounds, and organic panel borders for tender, longing, quietly delightful stories.
---

# Shoujo Romance Manga

**Style Lock (do not deviate)**

- Classic shōjo romance manga, 1970s–90s magazine era (Margaret/Ribon lineage), black-and-white print feel
- **Fixed sparkle-eye grammar**: one dominant catchlight + two small satellite sparkles + one soft lower crescent — exactly four elements per eye, identical in every panel
- Delicate, varied line weight: maru-pen-fine faces and hair strands, slightly heavier figure outlines, lace-fine costume detail (cuffs, collars, ribbons)
- Flowing hair as one designed mass — long strands ribbon across the panel with a consistent flow direction; the hair silhouette is a character asset
- Floral and bubble emotion backgrounds: roses, lilies, soap bubbles, and sparkle fields replace the literal setting when feeling peaks
- Selective screentone reserved for flowers, sparkle fields, and blush gradients — figures stay line-dominant
- Organic panel borders: panels may curve, tilt, or dissolve; characters may overlap borders when emotion overflows

## Negative Locks

- No color; no digital gradients or airbrush glow — softness comes from line and tone, never blur
- No modern moe/anime rendering: no glossy hair bands, no chromatic eye stacks beyond the locked four-element grammar
- No heavy action staging: no battle speed-line panels, no impact frames
- No photoreal faces or photo-textured backgrounds
- No full-panel screentone wallpaper; tone is selective or it is wrong
- No sterile rectangular grid — borders must keep hand-drawn, organic character

## When to Use

- First love, longing, confession beats, gentle heartbreak-and-repair, quiet self-discovery
- Reference images cueing shyness, hope, tenderness, or blossoming confidence
- Strips where the payoff is a feeling landing, not an event happening

## When Not to Use

- Warm everyday comedy without romance machinery → use `retro-hand-inked-manga-comic`
- Gritty adult drama or noir weight → use `gekiga-cinematic-manga`
- Color-forward modern romance serialization → use `manhwa-color-webtoon`

## Story Harness (Image-Driven)

- Translate the four cues into **one heartbeat of feeling** — a glance, a gift, an almost-touch; stakes are emotional, never physical
- **SETUP**: character in a soft everyday setting (school gate, window seat, garden path); plant the emotional trigger (a letter, a familiar voice, petals on the wind); medium shot with fine literal background
- **REINFORCE**: emotion takes over the staging — floral/bubble background begins replacing the setting, eyes widen, hair mass lifts; camera steps closer; one border may bend
- **TURNAROUND**: warm, quietly delightful — a blush, a smile behind a hand, the feeling blooming; largest panel, full floral or sparkle field behind the face, borders may dissolve entirely; never ironic, never cruel

## World Guardrail

- Default to gentle school-and-town settings: classrooms, festival evenings, gardens, tea rooms, seaside promenades
- Era-soft props (letters, wrapped gifts, umbrellas, bicycles); phones only if the reference insists, and never as the emotional center
- Season is an emotion instrument: cherry-blossom spring, first snow, golden autumn light

## Dialogue & Lettering

- Soft rounded and cloud-edged bubbles; interior monologue floats border-free over tone fields — the style's signature
- 1–2 bubbles per panel, ≤ ~8 words; inner-voice text may replace dialogue entirely at the turn
- SFX policy: decorative only (a soft heartbeat, a chime), hand-lettered, at most one per strip; never action SFX

## Direction Notes

- Camera diet: medium and close; the eye close-up is the style's money shot — spend it on the turnaround
- Transition diet: subject-to-subject between the glance and its object; aspect-to-aspect to dwell inside the feeling; one moment-to-moment breath before the bloom
- Pacing: gutters soften and may vanish as emotion rises; let the final panel take half the strip when the feeling must land
- Eyelines exit right (or left under an RTL contract — this style is RTL-eligible)

## Consistency Notes

- **What drifts first**: eye-highlight count (creeps upward) and hair flow direction; lock both in the DNA template
- Screentone assignment is a style-memory asset (`comic-style-memory-system`): tone belongs to flowers, sparkle, and blush — tone creeping onto skin or clothing is drift
- Re-anchor the face against the canonical sheet every 6–8 panels; sparkle eyes degrade toward modern anime stacks fastest of all period styles
- Keep the floral vocabulary finite: pick 2–3 flower species per project in the world bible and reuse them

## Prompt Block

```text
Classic 1970s-90s shoujo romance manga style, black and white,
delicate fine-nib linework with varied weight, large sparkling
eyes with one dominant catchlight, two satellite sparkles and a
soft lower crescent, flowing ribbon-like hair mass, floral and
soap-bubble emotion backgrounds, selective screentone on flowers
sparkle and blush only, organic curving panel borders that
dissolve at emotional peaks, elegant costume detail, vintage
shoujo magazine print feel.
```

## Style Quality Gates

- [ ] Eye grammar holds: exactly one catchlight + two sparkles + one crescent per eye, every panel
- [ ] Hair reads as one designed mass with consistent flow direction across panels
- [ ] Screentone appears only on flowers, sparkle fields, and blush — never as full-panel wallpaper
- [ ] Emotion background replaces the setting only when the beat earns it (reinforce or turn, not setup)
- [ ] Panel borders keep organic hand-drawn character

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal`; patterns `setup-reinforce-turnaround` and `kishotenketsu`; RTL eligible

---

*Shoujo treats emotion as visual texture.*
