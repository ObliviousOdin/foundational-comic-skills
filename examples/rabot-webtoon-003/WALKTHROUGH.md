# Walkthrough — Long Night ep-01, "Amber"

The third format in the same world, and the first **serialized** one. Read `rabot-strip-001/WALKTHROUGH.md` for the full loop and `rabot-4koma-002/` for the format-delta pattern; this one covers what only a serial can show.

## What this example exists to prove

| Thing | Why the earlier examples could not show it |
|-------|--------------------------------------------|
| The **arc ledger**, filled in | A single strip has no throughline to track. The template had no worked instance anywhere in the repository until now |
| **Arc debt** — a missed emotional target, recorded rather than re-rolled | Requires an episode that ships imperfect and a next episode that owes something |
| The **scroll gap** as the primary pacing instrument | Strips pace with panel size; 4-koma cannot pace with geometry at all |
| A **third rendering grammar** over one cast | Two variants could be a coincidence; three is a system |
| A **reserved color** | Needs a multi-episode arc for scarcity to mean anything |

## 1. Contract (`comic-producer`)

`webtoon-scroll-segment` × `slow-burn-reveal` × `manhwa-color-webtoon` — the style's own declared native format, unlike the 4-koma example where the contract deliberately departed from the listed habitat.

One greenlight box appears here that the earlier briefs do not carry: `arc_ledger_registered`. Serialized work greenlights an **arc**, not an episode. Without it, episode 1 is free to invent an emotional destination that episode 6 has to honour.

## 2. The Arc Ledger (`comic-emotional-arc-orchestrator`)

`arc-ledger.yaml` is the artifact this example was really built for. A shot plan covers one episode; nothing in a shot plan can hold "Echo reaches dry-amusement by episode 6". The division is strict:

- **The ledger owns the destination** — arc shape, exit state, which episode it lands
- **The episode owns the route** — how this week's beats move one step along it

`forbidden_resets` is the field that earns the file. Rabot may not be *surprised at Echo's company* again: that was spent in strip-001, and a serial that re-spends an earned beat is not a serial, it is a loop. Encoding it means a later shot plan cannot quietly undo a season of work.

### The debt, which is the honest part

Episode 1 **missed** Echo's target. The plan called for `attentive`; the panel that proves her state shows her reading the board, which is `processing` — machine competence, not the beginning of a thaw. One state off.

The panel is good. It was shipped. The miss was written into the ledger as debt:

> Episode 2 owes an early beat where she is plainly watching Rabot rather than the board — otherwise the thaw reads as machine competence and the arc shape is lost.

This is the behaviour the ledger exists to produce. Without it the options are re-roll a good panel or quietly accept the drift, and the second one is how six episodes arrive somewhere nobody planned. A ledger converts a miss into a *scheduled obligation*.

It also surfaced a bible gap: Echo has no registered expression for concern about a **person** rather than a system. That is now an open `bible_change_requests` entry blocking the episode-2 shot plan — the arc found a hole in the character's expression library that no single strip would have exposed.

## 3. Bible Delta v4 (`comic-world-bible-system`)

Same pattern as v3: canon is referenced, never copied. Three registered grammars now sit over one cast — black-and-white main series, chibi side series, webtoon color. That is the variant system doing its job: `comic-style-memory-system` holds them separately and prevents bleed in any direction.

**The reserved swatch is new.** `alert-amber` may appear only on the ground-link board and light cast by it. A six-episode slow burn depends on the dread signal staying scarce, and "amber is the alarm colour" written as prose would erode by episode 3 the first time a warm prop wanted a highlight. Registering it as reserved makes the scarcity enforceable — and it propagates: Echo's temple light is explicitly barred from amber, because an amber temple light would make the character look like the alarm.

## 4. Shot Plan (`comic-director`) — pacing with gaps

Panel geometry *is* variable in this format, so the strip-001 instrument is available. The format's stronger one is the **scroll gap**, and the plan directs gap height per panel in screen-fractions rather than leaving it to layout.

The segment's spine is two consecutive half-screen gaps around panel 5 — an empty room with nobody in it, held between them. That is the pre-reveal breath, the webtoon equivalent of a page turn, and `comic-webtoon-scroll-pipeline` names protecting it as a format rule. The reveal must land *after* the gap, never beside it.

Panel 4 breaks the down-vector rule on purpose: Echo's gaze exits the **top** of the frame. Licensed because it points at the withheld thing, and the half-screen gap beneath holds that pointing long enough for the reader to feel it before scrolling into the empty room.

**The hint has to be honest and missable at once.** Panel 3 is the thermos's steel curve with a smear of the wrong colour in its reflection. Legible at 100%, ignorable at scroll speed. `slow-burn-reveal`'s payoff rule requires the reveal to be retroactively legible — re-scrolling, that reflection is obviously the board, and the camera hid honestly rather than cheating.

## 5. The lettering budget, in its first non-strip test

`comic-lettering-and-balloons` was corrected last cycle so scarce elements ration per **budget unit**, with the unit set by the format. This is the first worked project to use a non-strip unit, and it behaves:

> **Segment = episode = one budget unit.** Not the arc.

So this episode may spend one burst balloon, one off-panel line, one SFX, and owes at least one silent panel. It spends zero bursts, one off-panel (P6), one SFX (P4), and runs four silent panels. Had the unit been the *arc*, one SFX across six episodes would have been absurd; had it been the *panel*, nothing would be scarce at all.

## 6. Prompt Assembly and the RETAKE

`assembled-prompt.md` shows the two format-forced changes: `[FORMAT]` is per-panel plus a stitching contract carrying the directed gap, and the negative block states `side-by-side panels` because backends reach for grids when handed several beats.

The RETAKE was pure format: panel 5's bubble straddled the boundary between screens 2 and 3, so a reader mid-scroll saw half a sentence. `comic-webtoon-scroll-pipeline` forbids it and the shot plan's `scroll_check` block now records it as a standing check. Corrective field, one placement change, re-render — not a re-roll.

## 7. Sign-Off

Bible stamped v4, exports per the platform matrix, ledger updated with episode 1's actual exit states and the debt carried into episode 2. The episode ships; the arc keeps the receipt.

---

*A strip can be judged on its own. A serial can only be judged against where it said it was going.*
