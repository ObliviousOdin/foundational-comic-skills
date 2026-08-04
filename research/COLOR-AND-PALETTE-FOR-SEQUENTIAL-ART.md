# Color and Palette for Sequential Art – Foundational Study

**For palette discipline across panels: value structure, limited sets, reserved signals, and continuity**

Color in a single illustration is a composition problem. Color across a *sequence* is a continuity problem, and the two want opposite things — an illustrator tunes each image to itself, while a comic needs the same red to mean the same thing on page forty as it did on page one. Every finding below descends from that difference.

---

## 1. Value Carries Readability; Hue Carries Meaning

The oldest working rule in comics colouring is that a panel must read in greyscale first.

- **Value separation is what makes a figure legible against a ground.** Two colours of different hue but identical value merge into one shape at reading speed, no matter how different they look side by side.
- **Hue is nearly free for meaning** *because* value is doing the reading. That is why a colourist can assign a hue to a faction, a location, or a state without damaging legibility.
- **The greyscale test is diagnostic, not aesthetic.** Desaturate the panel: if the focal figure disappears, the palette failed regardless of how it looks in colour.

The practical consequence for AI-generated work is sharper than for hand work. A generator will happily produce a palette of beautiful, adjacent, identically-valued colours, because nothing in a prompt asks for value separation and the result is *attractive*. Attractive and unreadable is the characteristic failure.

## 2. The Limited Set Is a Feature, Not a Constraint

Historically, limited palettes were technological — four-colour process, spot-colour printing, risograph drums, single-ink manga. The constraint outlived the technology because it does three things at once:

1. **It makes colours mean something.** In a set of five, each colour is identifiable and can carry a job. In an unlimited set, no colour is distinguishable enough to signify.
2. **It makes drift visible.** A palette of five named swatches either matches or does not. A palette of "warm autumn tones" cannot be checked.
3. **It makes recolouring cheap.** Locations, times of day, and emotional registers can be swapped by re-mapping a small set.

**Anchor the set by name and value, not by hex alone.** A hex code says what a colour *is*; a name and a value step say what it is *for* and where it sits in the readability structure.

## 3. Reserved Colours

The strongest device in long-form colour work is the colour that is **not** used.

A reserved colour appears only in one context — one object, one emotional state, one faction — and is forbidden everywhere else. Its power is entirely a function of scarcity, and scarcity erodes silently: the reserved hue leaks into a warm highlight, then a sunset, then a jacket, and by the time anyone notices, the signal is gone and no single decision caused it.

Three properties make a reserved colour work:

- **A stated scope.** What it marks, exactly.
- **A stated prohibition.** Where it may not appear — including places that would be aesthetically defensible.
- **Propagation to neighbours.** If a character's signature mark is a light, and the reserved colour is an alarm, that light must be barred from the reserved hue or the character reads as the alarm.

The third is the one people miss, and it is not a colouring decision — it is a continuity decision that belongs in the bible.

## 4. Local Colour vs. Lighting Colour

A recurring source of drift is conflating the colour a thing *is* with the colour the light makes it.

- **Local colour is identity** and belongs to the character or prop: a navy jacket is navy in every scene.
- **Lighting colour is scene state** and belongs to the location: the same jacket reads cool under fluorescents and warm under a lamp.

Recording them together produces a character who changes clothes whenever the scene changes. Recording them separately lets a location's grade apply over stable identities — which is exactly how a bible with `character_compendium` and `world_register` is already shaped.

## 5. Colour as Continuity Anchor

In a sequence, a character's colour is part of their identity with the same force as their silhouette. Two consequences:

- **Contrast anchors between characters must include value**, not only hue. Two characters in equally-valued red and green are one shape in greyscale and, at small panel sizes, in colour too.
- **Costume changes are canon events.** A character in a different colour is, to a reader and to a conditioning model, a partially different character.

## 6. Known Failure Modes

- **The attractive mush** — a harmonious palette with no value separation; the commonest AI colour failure
- **Reserved-colour erosion** — the signal hue appearing decoratively until it signals nothing
- **Local/lighting collapse** — identity colours drifting with each scene's grade
- **Palette inflation** — the set growing panel by panel until nothing is nameable
- **Hue-only contrast anchors** — characters distinguished by colour that vanishes in greyscale
- **Per-panel tuning** — each panel colour-corrected to look good alone, and the sequence losing its through-line

---

## Operationalised In

| Finding | Enforced by |
|---------|-------------|
| Palette anchored as a named, limited set | `comic-world-bible-system` `visual_grammar.color_palette_anchors` |
| Reserved colours with scope, prohibition, and neighbour propagation | `comic-world-bible-system` `reserved_swatches` |
| Value carries readability — the greyscale test | `comic-quality-gates` Layer 4 |
| Local colour is identity, lighting colour is scene state | The `character_compendium` / `world_register` split, made explicit |
| Contrast anchors must separate in value | `comic-character-consistency-system` multi-character rules |
| Limited-set discipline as a style lock | Style skills that name palettes (`chibi-kawaii-comic`, `pop-art-lichtenstein-comic`, `manhwa-color-webtoon`) |

## Gaps This Study Leaves Open

- **No worked example of a reserved swatch eroding.** `rabot-webtoon-003` declares `alert-amber` correctly; nothing demonstrates the failure the reservation prevents
- **Value steps are unmodelled.** Swatches carry names and hex codes but no declared value step, so the greyscale test remains a human judgement rather than a checkable property
- **Print-gamut interaction is unaddressed here** — see `comic-export-and-publish` for the CMYK side

---

*Value decides whether the reader can see it. Hue decides what it means. Confusing the two is how a beautiful page becomes unreadable.*
