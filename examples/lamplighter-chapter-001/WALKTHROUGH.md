# Walkthrough — The Lamplighter, chapter 001: "Eleven Standards"

The fourth worked project, the last unbuilt sanctioned format, and the first one **not** set in the Rabot world.

That last part is deliberate. Three projects sharing one world bible proved the delta pattern well; a fourth would have started to suggest the system depends on canon that already exists. This one is a cold start — new bible, new cast, nothing inherited.

## What only a chapter can show

| Thing | Why the other three could not show it |
|-------|---------------------------------------|
| **Composing several patterns in one work** | Strips, 4-koma and scroll segments lock one pattern. A chapter assigns one *per scene* |
| **The page turn as an instrument** | Requires physical pages, recto and verso |
| **The chapter map** | A planning artifact that must exist before any page is planned |
| **A splash, rationed** | One per chapter maximum, grantable only by the map |
| **Scene-boundary review** | Review cadence stops being per-episode and becomes per-scene |

## 1. Contract and the pattern that is only a spine

`multi-page-chapter` × `painted-prestige-comic`, and the brief records `narrative_pattern: slow-burn-reveal`.

That field means something different here than in the other three projects. It is the chapter's **spine**, not its instruction. The chapter map assigns a pattern per scene:

| Scene | Pages | Pattern | What the reader gains |
|-------|-------|---------|------------------------|
| 1 | 1–2 | `setup-reinforce-turnaround` | The round, the competence, the fact that the light is made by hand |
| 2 | 3–4 | `slow-burn-reveal` | What Perrin came to deliver — and that Ada already knew |
| 3 | 5–6 | `kishotenketsu` | The same bridge under inverted light, and what is actually handed over |

Scene 3 takes kishōtenketsu because the ending is a recontextualisation, not a conflict resolved. The bridge under arc light is the *ten* — the same place, no person in frame doing anything, the frame stepped outside of. The key changing hands is the *ketsu*. A turnaround pattern would have demanded a reversal the story does not contain.

**This broke a test, and the test was wrong.** `tests/test_examples.py` asserted that a shot plan's pattern equals the brief's — true for every format that locks one pattern, false by design for chapters. Fixed in the same cycle: chapters check their page patterns against the chapter map's scene assignments instead. It is the same defect class `CONTRIBUTING.md` ground rule 6 exists to prevent, this time living in the test suite rather than a skill.

## 2. The Chapter Map (`comic-multi-page-chapter-pipeline`)

`chapter-map.yaml` is authored **before any page shot plan**, and it had no template until this cycle — the pipeline mandated the artifact three times and gave no shape for it.

It holds the two decisions a per-page plan structurally cannot make. Pattern assignment is chapter-level. And the page turn cannot be planned one page at a time: by the time you are laying out page 4, it is too late to decide what page 3 should have withheld.

### Page grammar, recto and verso

Page 1 is a right-hand page, so odd pages are recto and even are verso. The rule is that a recto **ends on a question** the reader must physically turn to answer, and the verso opposite **opens with the consequence**:

- **Page 3** (recto) ends on Ada turning the notice over without reading it. *Why does she not need to?*
- **Page 4** (verso) opens on the drawer: eleven identical notices from eleven previous years.

Nothing continues across a turn. `turn_protected: true` on every page records the check the format exists to enforce — never split an action-to-action pair across a page turn, because the reader's hand interrupts it.

## 3. Pages 5 and 6 — the spread the chapter was built for

`shot-plan.yaml` is page 5; `shot-plan-p06.yaml` is page 6. One plan per page is the format's shape, and both answer to the map.

**Page 5 is wholly silent — four panels, no text.** The chapter silence rhythm asks for one wordless panel per spread; this spends the entire page. The reason is structural: the *ten* steps outside the frame the story established, and a caption would explain the step.

The page empties the bridge of purpose in four beats: the span before the arc lamps strike, the strike itself, then panel 5.3 — one gas standard still burning inside the flood, its amber invisible, *lit and contributing nothing*. That is the chapter's argument in one image, and it needs no words because the light does the arguing. Then a high wide of the whole span with both figures small at the far end, neither of them working.

Page 5 ends on its question: **is anything left to do here?**

**Page 6 is the answer and the chapter's only splash.** The map designated it with a justification, which is the only way a splash can be granted. Two pairs of hands, the brass key passing between them, cold light from above and one small warm reflection in the brass — the last warm light in the book.

Neither face is in frame, and the final-cut note records that this was close. The first plan had Ada's face, and it turned the page into mourning. Hands only, and the transfer reads as inheritance instead.

## 4. Why the bridge is in the bible twice

`world_register` carries **Kell Bridge** and **Kell Bridge (electrified)** as two canonical location sheets, not one location with a lighting note.

The chapter's whole argument is the difference between warm local light and cold total light. Registered as one location, the final scene generates as the same place slightly brighter and the point evaporates. Registered as two, the inversion is canon and every panel in scene 3 inherits it.

That is what a world bible is for: not describing places, but making the differences that carry meaning **non-negotiable**.

## 5. Prompt assembly, where negatives carry narrative

`assembled-prompt.md` shows panel 5.3. Two of its negatives are doing narrative work rather than hygiene:

- `warm ambient light filling the scene` — a backend handed the word "gaslight" reaches for warmth, which would restore exactly the atmosphere the chapter just removed
- `visible arc lamp fixtures in frame` — showing the fixture makes the new light a thing that could be argued with, rather than a condition

Both were justified in the shot plan and merged into the block by the adapter. Neither was hand-written at generation time, which is what Layer 0 checks before a render is paid for.

## 6. Review cadence changes shape

The other three projects review per episode. A chapter reviews at **scene boundaries** — three gates here, one after each scene, recorded in the map. The re-anchor interval also tightens to every 8 panels, because painted faces drift faster than line work and there are 29 panels of them.

The re-render reserve is raised from the default 20% to 25% for the same reason, and the production log shows where it went: p4.3 took two retakes because the drawer of eleven notices first rendered as a neat stack, which reads as *filing* rather than as years.

---

*A strip is read. A chapter is turned — and everything the format offers lives in that difference.*
