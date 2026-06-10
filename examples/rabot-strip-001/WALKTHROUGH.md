# Walkthrough — Rabot strip-001, "Night Shift"

This narrates one complete pass through the system, artifact by artifact. Every step names the skill that governs it.

## 1. Brief → Contract (`comic-producer`)

The brief arrives loose: *"quiet sci-fi strips about a night-shift tech and a station AI."* Producer intake resolves it into `production-brief.yaml`:

- **Format**: `3-panel-horizontal` (X + Instagram targets; the strip is the master, Instagram gets a carousel re-cut per `comic-export-and-publish`)
- **Pattern**: `setup-reinforce-turnaround` (warm register → default arc; kishōtenketsu was considered and parked for a future 4-koma side series)
- **Style**: `retro-hand-inked-manga-comic` (mood cues in the references read tired-but-warm; gekiga would push it bitter)
- **Scope**: 12 weekly strips, 36 panels + 20% re-render reserve

## 2. Greenlight (`comic-producer` + `comic-world-bible-system`)

The bible (`world-bible.yaml`) starts with one character — but strip 001 is a two-hander, so the multi-character rules in `comic-character-consistency-system` force a v2 bible entry **before** greenlight:

- Echo gets contrast anchors against Rabot (silver vs dark hair, gray coverall vs navy jacket)
- Each character's negative block includes the *other's* signature marks (identity-bleed prevention)
- The change lands in `version_history` with rationale — nothing changes silently

All eight greenlight boxes check. Production may begin.

## 3. Cue Extraction (`comic-story-derivation`)

Four cues from the references — plus the fifth, because there are two characters:

> MOOD tired-but-settled · WARDROBE practical night-shift · SETTING control room · PROP dented thermos · **RELATIONSHIP: parallel solitude, easing toward company**

The arc belongs to the *relationship*: the turnaround must move it one step closer, and both characters must visibly react.

## 4. Shot Plan (`comic-director`)

See `shot-plan.yaml`. The load-bearing decisions:

- **Camera ladder** medium → close-up → wide: step in for the gesture, step back so the payoff is about *two people in a room*
- **Panel 2 is silent** — the retro-manga harness says the gesture carries the beat; a balloon would have explained it
- **180° axis locked**: Rabot screen-left, Echo screen-right, for the whole scene
- **Pacing**: wide gutter before panel 3, largest panel, tone-flat background so the warmth reads instantly
- All five *name* criteria pass before any generation

## 5. Prompt Assembly (`comic-image-generation-adapter`)

See `assembled-prompt.md`. Note what the adapter did **not** do: it authored nothing. Style block verbatim from the style skill; DNA verbatim from the bible; directives verbatim from the shot plan; negatives merged, not hand-written.

## 6. Final Cut (`comic-director`) — including the RETAKE

First render, flow-first review:

1. **Flow** ✓ one-pass read, balloon order fine
2. **Words** ✓ two lines, both inside budget
3. **Everything else** ✗ — **Layer 5 violation**: the panel-3 balloon sat over Echo's temple indicator light, her signature mark (a `comic-lettering-and-balloons` dead-zone failure)

Verdict: **RETAKE**, corrective field `panels[3].dialogue.placement` → upper-right dead zone. One field changed, re-render, not a re-roll of the whole strip. Second render passes all six gates; the Director signs the Artistic Life note.

## 7. Sign-Off (`comic-producer`)

The RETAKE is logged in the production state (1 of the reserve used). Exports per the platform matrix, manifest written, bible version stamped. Strip 001 ships; the arc ledger (`comic-emotional-arc-orchestrator`) records Echo's exit state: *attentive → quiet-warm, proof panel P3*.

---

*One strip, zero improvisation: every panel decision has an artifact, and every artifact has an owner.*
