# Walkthrough — Grid Pieces 002, "Both Hands"

The sixth worked project, and the last unbuilt sanctioned format. **All six formats in `comic-format-library` now have a filled-in artifact.**

## What building it found before a single panel was planned

Counting which styles claim each format turned up a dead end:

| Format | Styles claiming it |
|--------|-------------------|
| `3-panel-horizontal` | 26 |
| `multi-page-chapter` | 13 |
| `single-panel-gag` | 5 |
| `4koma-vertical` | 3 |
| `webtoon-scroll-segment` | 2 |
| **`2x2-grid-page`** | **0** |

Fully specified in the library, wired to a pipeline, and **nothing in the style layer pointed at it**. A Producer locking this format got no routing guidance at all — the index would answer the question "which style suits a 2x2 grid?" with silence.

This is a different shape from the seven format-scope defects fixed in earlier cycles. Those were rules stated too broadly. This is a sanctioned option nothing referenced, and it needs a different audit: **count the claims, don't just resolve the names.** The validator was already checking that every habitat name resolves; no check asks whether every format is claimed.

Fixed before planning. Ligne claire's own Direction Notes already said *"regular waffle-grid discipline with even gutters"* — it was a grid style that did not claim the grid format. Chibi kawaii is native to `4koma-vertical`, and a 2x2 is the same four beats folded into a grid instead of a column.

## Two constraints that exist in no other format

### The Z-path puts parallel action on the diagonal

The reader goes top-left → top-right → bottom-left → bottom-right. So a two-thread structure cannot run in columns; it runs on the **diagonal**. Thread A holds TL and BR, thread B holds TR and BL.

That is why `comic-narrative-patterns` names `parallel-action` native here, and the shot plan shows what it buys. Perrin's thread is panel 2 (pen above the form) and panel 3 (pen stopped, ink blot spreading). Those two beats are separated by a panel of Ada. **The stopped pen only reads as hesitation because of the interruption** — placed adjacently it would read as a continuous action, and the character's doubt would vanish into a sequence.

### The T-rule is a layout decision the Director owns

Four panels in a grid want to meet at a clean `+`. `comic-format-library` forbids it: stagger one gutter slightly.

The shot plan carries a `layout` block recording that the vertical gutter is offset 6mm between the upper and lower rows, so no four corners ever touch. This is recorded in the plan rather than left to whoever assembles the page, because it is not a rendering detail — it is what makes four panels read as one page.

The final-cut note records the proof: the first render aligned the gutters into a perfect cross, and the page fell apart into four unrelated pictures. A 6mm stagger fixed it. Startlingly small change, whole-page effect.

## Pacing with geometry locked, again

`2x2-grid-page` is the second format on the Director's locked-geometry list, alongside `4koma-vertical`. Panel size and gutter width are unavailable as tempo instruments, so the pacing table's remaining four apply — and this page uses the same one the 4-koma example did: **content density.**

Panel 4 is the widest and emptiest thing on the page. Ada from behind, small against the span, the ninth standard now dark.

## Convergence that changes both threads

`parallel-action`'s payoff rule is strict: the convergence beat must change the meaning of *both* threads, and threads stay visually distinct until they meet.

They never meet here. Ada is on the bridge, Perrin is in the hut, and the page ends with them apart — but panel 4 shows the standard she has just put out herself. That reframes both halves at once: her round becomes a choice rather than a duty, and his form becomes a record of something already done rather than an order being carried out.

Convergence of meaning, not of bodies. The pattern's requirement is about what the reader understands, not about who is in frame.

## A second grammar over the same cast

This project reuses the Lamplighter bible and switches the style — painted prestige for the chapter, ligne claire for the companion pieces. Third time the repository has shown a variant grammar over one cast, and the first time the switch is between two *fully different* line philosophies rather than a mode of one.

The uniform line weight is doing thematic work the walkthrough is worth pausing on: ligne claire gives the arc lamps behind Ada exactly the same nib as her hands. The style **refuses to rank them**, which is the argument the chapter spent six pages making.

---

*Four panels are not a small page. They are the format with the least room to hide a layout decision.*
