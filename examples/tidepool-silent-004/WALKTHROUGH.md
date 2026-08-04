# Walkthrough — Tidepool 004, "Low Tide"

The seventh worked project, and the first to lock a **pattern** nobody had built rather than a format.

All six formats were built by cycle 10, and every one surfaced a defect. `silent-strip` was the obvious next target: it is the only sanctioned pattern defined by the *absence* of something every other rule assumes.

## What it found, in a file that had already been audited

`comic-story-derivation` Step 4 said, without qualification:

> Generate 1–2 short lines per panel that **match the mood cue**

`silent-strip`'s defining rule is zero dialogue. An agent following both produces exactly what the pattern names as its own anti-pattern: silence as decoration — beats designed to be spoken, then merely unspoken.

**This file had already been audited for this defect class.** Cycle 5 fixed Step 2 of this same skill, which mapped cues to "the three-panel structure". That audit was scanning for panel-count phrasing, and Step 4 is the identical mistake wearing different words — an unqualified rule a sanctioned option contradicts — so it survived by never mentioning panels. Ground rule 6's diagnostic catches it; the grep that found its sibling did not.

Fixed before planning (1.2.0 → 1.3.0), and fixed by **replacement rather than exemption**.

## Gesture seeding

Skipping Step 4 would leave a gap where the beats get their intention. So under this pattern the step still runs — it just seeds the gesture that would have carried the line.

The shot plan records both halves, which is the artifact worth copying:

| Beat | The line that would have been | The gesture instead |
|------|------------------------------|---------------------|
| SETUP | *oh — you're stuck* | She stops walking, one foot still lifted mid-step |
| REINFORCE | *hold on, I've got you* | She crouches and turns both palms up before touching anything |
| TURNAROUND | *there you go* | She does not watch it leave; she is already looking at the next pool |

Writing the unspoken line down is not ceremony. It is how you check that the gesture carries the *same* beat — and if a beat has no gesture, if the only honest answer is a line, then the pattern is wrong for the story. That is a Producer decision, not something the Director can stage around.

## The retake that defines the pattern

Panel 2 took **two** retakes, both for the same thing: the first two renders gave Mira an open-mouthed reaction.

No letter appeared anywhere in the image. It still broke the pattern.

A shouting face imports speech without drawing a word — the reader hears it. **Silent does not mean soundless-looking; it means the strip cannot smuggle a line in through a face.** `open shouting mouth` is now a negative in the bible, and it is the entry a reader of this example should take away.

## Where the turnaround actually is

The instinct in panel 3 is to show Mira watching the starfish swim away. The plan resists it, and the final-cut note says why: a watching panel is the sentimental version, and it *wants a caption* — you can feel the missing line under it.

Instead she has already turned toward the next pool. That reframes the act as ordinary rather than heroic, which is the mood cue paid off, and it needs no words because nothing is being announced.

## Two things recorded that the schema does not yet hold

**`typography_rules: none`.** The bible sets it explicitly rather than leaving it empty. A silent strip has no lettering policy, and recording *that* stops a later episode from quietly acquiring one — the pattern lock lives in the contract, but the bible is where a generator looks.

**Pattern bleed.** Six of this project's negatives exist to prevent speech re-entering: balloon, thought balloon, caption, SFX lettering, onomatopoeia, shouting mouth. Under the bleed taxonomy added in cycle 11 these are none of identity, style, era, or anatomy — they are a **fifth class the taxonomy does not name**, filed for now under `project_wide_negatives`. Recorded as a finding rather than fixed here, because one example is thin evidence for a taxonomy change.

## The SFX question

`ink-wash-storybook-manga` sanctions sparse SFX. This strip spends none, and the shot plan records the reasoning in its `not_applicable` block:

> A sound effect in a silent strip is dialogue wearing a different font — the pattern removes words, not just balloons.

A style permission and a pattern lock met, and the pattern won. Worth noting that no rule in the tree says so explicitly; it follows from the pattern's payoff rule ("every beat carried by staging, expression, and closure alone") but a contributor could reasonably read the style permission as licence.

---

*Remove the words and every weak beat becomes visible at once. That is the whole reason to try it.*
