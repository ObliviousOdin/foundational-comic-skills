---
name: comic-lettering-and-balloons
version: 1.1.0
category: comic-core
description: The craft contract for balloons, captions, tails, and lettering — taxonomy, placement law, reading-order rules, and per-style deltas. Bubbles hide art and order the reader's ear; this skill makes both deliberate.
---

# Comic Lettering & Balloons

**Core principle**: A balloon is a camera decision and a timing decision wearing a text costume. Placement, shape, and order are directed — never left to chance.

The quality gates already police text *quantity* (Layer 5). This skill supplies the missing *positive* craft: what good balloons are and where they live.

## When to Use

- During Director shot planning (the `dialogue` block of every shot plan)
- When a panel's text placement hides key art or breaks reading order
- When defining a style skill's `Dialogue & Lettering` section (state deltas from this contract)

## Balloon Taxonomy

| Type | Shape Grammar | Use For | Default Limit |
|------|---------------|---------|---------------|
| **Speech** | Smooth oval, single pointed tail | Spoken lines | ≤2 per panel |
| **Thought** | Cloud edge, bubble-chain tail | Interior voice | ≤1 per panel |
| **Whisper** | Dashed outline | Secrets, asides | Rare; counts as speech |
| **Burst/Shout** | Spiked outline | Yelled lines, alarm | ≤1 per budget unit; must be earned by the beat |
| **Caption box** | Rectangle, no tail | Narration/time stamps | **Forbidden by default**; permitted only where a style or format explicitly allows (e.g., `autobio-indie-literary-comic`, `single-panel-gag`) |
| **Off-panel** | Tail points to panel edge | Unseen speaker | ≤1 per budget unit; the reveal must pay it off |

## Placement Law

1. **Dead-zone rule**: balloons live in compositional dead zones — sky, walls, negative space. Never over faces, hands, the inciting prop, or the panel's focal point.
2. **Reserve the zone in the shot plan**: the Director stages each panel with balloon space already budgeted; lettering squeezed in after staging is a planning failure.
3. **Tail discipline**: tails point to the speaker's mouth level, take the shortest believable path, never cross panel borders, other balloons, or a face.
4. **Margin law**: text padding inside the balloon ~20% of balloon width; balloons never touch panel borders (minimum one line-width gap) and never overlap the gutter unless the style sanctions border breaks.
5. **Stacking**: when two balloons share a panel, the first-read balloon sits higher and/or further toward the reading-direction origin; joined balloons (same speaker) connect with a short bridge, not a shared outline.

## Reading-Order Rules

- **LTR formats**: first balloon top-left region, conversation descends left→right; a reply must never sit left of (or above) its prompt.
- **RTL (manga-family lock)**: mirror everything — first balloon top-right; tails and eyelines obey the mirrored flow.
- **Vertical scroll**: one balloon zone per panel; dialogue order = scroll order; never two balloons side-by-side competing for the same scroll moment.
- **The order test**: cover the art; read only balloons in position order. If the conversation still makes sense, order passes.

## Text Budget (Inherited by All Styles)

- ≤ ~8 words per balloon; ≤ 2 balloons per panel (taxonomy limits above are stricter for special types)
- Hyphenation forbidden; line breaks at phrase boundaries; ALL-CAPS only where the style's lettering tradition uses it

### What "per budget unit" means

Scarce elements — burst balloons, off-panel speakers, SFX, and the silent panel — are rationed per **budget unit**, not per project and not per panel. The unit is set by the locked format, because "one shout per strip" means nothing in a format that has no strips:

| Format | One budget unit = | Silent-panel rule |
|--------|-------------------|-------------------|
| `3-panel-horizontal` | the strip (3 panels) | ≥ 1 silent panel |
| `4koma-vertical` | the strip (4 panels) | ≥ 1 silent panel — the *ten* is the usual choice |
| `2x2-grid-page` | the page (4 panels) | ≥ 1 silent panel |
| `webtoon-scroll-segment` | the **segment**, never the episode | ≥ 1 silent panel per segment |
| `multi-page-chapter` | the **page**, never the chapter | ≥ 1 silent panel per page |
| `single-panel-gag` | the panel | **Exempt** — see below |

`single-panel-gag` is exempt on purpose. The format sanctions one bubble *or* one caption, and a silent-panel rule applied to a one-panel format would forbid the only text the format allows. Silence there is a style choice, not a budget obligation.

The long formats matter most here. Rationing one shout across a whole chapter would be absurd, and a chapter that satisfies "one silent panel" once in forty is not obeying a rhythm rule — it is exploiting a unit that was never defined.

## Lettering Feel by Style Family (Deltas Live in Each Style Skill)

| Family | Default Feel |
|--------|--------------|
| Manga-family | Hand-lettered, rounded; small katakana-flavored SFX where sanctioned |
| Newspaper/cartoon | Confident hand-caps, uniform weight |
| Painted/prestige | Set-apart formal lettering; restrained caption styling where allowed |
| Zine/underground | Wobbly hand-letters; ransom-note energy sanctioned |
| Minimalist | Typewriter-plain, small, generous air |

## SFX Policy

- Default: **no sound effects** (universal rule). Styles that sanction SFX must cap count (typically 1 per budget unit) and bind SFX to the inciting action, not decoration
- SFX are drawn as art (integrated perspective and overlap), never pasted flat text

## Failure Modes to Catch

- Balloon covers the expression that carries the beat (the #1 lettering failure)
- Reply-before-prompt order inversion at a glance
- Tail crossing a border or pointing at the wrong character
- Burst balloon on a quiet beat (tone mismatch)
- Caption sneaking into a style that forbids it

## Integration

- The Director's shot plan `dialogue.placement` field is governed by this contract
- `comic-quality-gates` Layer 5 checks quantity; this skill defines the placement/ordering checks the Director applies in the flow-first final cut
- Style skills inherit this contract and state only their deltas in `Dialogue & Lettering`

---

*The reader hears with their eyes. Letter like it.*
