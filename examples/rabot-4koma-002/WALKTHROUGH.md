# Walkthrough — Small Hours 4koma-002, "One Window"

Strip-001's intake parked a 4-koma side series. This is that series, and it exists in the examples folder to demonstrate what changes when the **format and pattern change but the world does not**.

Read `rabot-strip-001/WALKTHROUGH.md` first if you have not. This one deliberately shows the deltas rather than repeating the flow.

## 1. Brief → Contract (`comic-producer`)

- **Format**: `4koma-vertical` — vertical feeds, and the tighter arc suits a side strip
- **Pattern**: `kishotenketsu` — the historically correct pairing for 4-koma per `comic-narrative-patterns`
- **Style**: `chibi-kawaii-comic`
- **Bible**: *referenced*, not copied — `../rabot-strip-001/world-bible.yaml` stays canon

**A contract choice worth pausing on.** The style index lists this style's native habitat as "4-koma; gag escalation", and the contract took `kishotenketsu` instead. That is allowed and it is not a loophole: native habitat is the Producer's *guidance*, telling you where a style is strongest, while the contract is the *lock*. The side series is fond rather than punchy, so the pattern was chosen for register and the decision was logged in the brief where a reviewer will find it.

## 2. The Bible Delta (`comic-world-bible-system`)

This project adds a whole second rendering grammar — chibi — over identities that already exist. The tempting move is to copy the bible and edit the copy. That produces two canons, and the second one drifts.

Instead, `bible-delta-v3.yaml` records **only what is added** and merges into the canonical bible at v3.0.0:

- Chibi mode registered as a visual-grammar **variant**, not a replacement
- Per-character chibi DNA, with Echo's temple light explicitly kept a full circle — it is her identity anchor, and shrinking it to a dot at 2-head scale would erase the thing that makes her recognisable
- `Station Exterior` added as a canonical location, because the *ten* beat needs one or it redraws differently every episode

The file is deliberately **not** named `world-bible-delta.yaml`: the validator treats `world-bible*.yaml` as a complete bible and would rightly reject a partial document. Naming it away from that pattern is the honest fix, not an exemption.

## 3. Reading Direction, Resolved by the Format

`comic-format-library`'s reading-direction rule has three clauses, and the third settles this strip: **vertical formats read top-to-bottom regardless of style.** The contract still records `reading_direction: ltr` for the project, but within a 4-koma it decides nothing. The shot plan carries `panel_flow: top-to-bottom` so no eyeline vector is ever planned against a horizontal axis that does not exist here.

## 4. Shot Plan (`comic-director`) — and the constraint that changes everything

See `shot-plan.yaml`. Strip-001 paced itself with panel size and gutter width: the payoff got the biggest panel and the widest gutter before it. **4-koma forbids that.** Panels are equal height, gutters uniform, and `comic-format-library` is explicit that pacing comes from content rather than geometry.

So tempo had to be built a different way: panel 3 is the emptiest drawing in the strip. No figures, no text, one lit window. The pause is made of *content density*, not layout.

**The `ten` is the hard beat.** `comic-narrative-patterns` warns that *ten* is not a punchline — it is a perspective shift — and that kishōtenketsu without a real *ketsu* is just an interrupted thought. Panel 3 cuts entirely outside: the station, small, one window lit. Nothing is revealed, nothing goes wrong, and both earlier panels change meaning. Panel 4 then reconciles by showing the same window from inside, which makes the exterior shot and the interior scene one place, and turns smallness into cosiness instead of isolation.

Panels 3 and 4 were both locked silent before generation. A caption on the *ten* would have explained the shift, and an explained perspective shift stops being one.

## 5. Prompt Assembly (`comic-image-generation-adapter`)

See `assembled-prompt.md`. One block genuinely changes shape from strip-001: `[FORMAT]` now states equal panel heights and uniform gutters explicitly, and the negative block carries `panels of differing heights, varied gutter widths`.

That is not belt-and-braces. Image backends default to varying panel size for emphasis, because that is what most comics do — which means the single defining constraint of this format is the one thing the backend will silently violate. A format rule that a generator actively works against belongs in the negative block, not just the format block.

## 6. Final Cut (`comic-director`)

Zero RETAKEs, and the flow-first review is worth reading for *what was checked first*: chibi proportion across the scale change. Panel 3 leaves the 2-head lock with nothing to attach to — no character in frame — and panel 4 has to come back at exactly the proportion panels 1 and 2 established. That is where this strip would have failed, so that is what the Director looked at before anything else.

Review cadence in the brief reflects the same risk: re-anchor every 8 panels here against the main series' 10, because chibi proportion drifts faster than a naturalistic figure does.

## 7. Sign-Off (`comic-producer`)

Bible stamped v3, exports per the platform matrix in `comic-export-and-publish`, arc ledger updated: the side series inherits the main strip's relationship state rather than restating it — Rabot and Echo are past negotiating company here, which is why panel 2 needs no reaction from Rabot at all.

---

*Change the format and the pattern, keep the world: what stays fixed is what proves the system is a system.*
