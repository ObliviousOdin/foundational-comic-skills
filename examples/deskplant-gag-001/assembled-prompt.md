# Assembled Prompt — Deskplant 001 (canonical order per `comic-image-generation-adapter`)

Backend: single-call. Blocks assembled verbatim from their owning artifacts — nothing here was authored at generation time.

This is the smallest legal assembled prompt in the repository, and it is worth reading for what it does *not* drop. Block order is unchanged, `[SCENE]` still appears even though the scene is a void, and the negative block is still merged rather than hand-written. A one-panel format shortens the prompt; it does not license skipping the contract.

```text
[STYLE]
Minimalist line webcomic style, thin fixed-width black pen line with no
weight variation, stick-to-simple figures with circle heads and dot
eyes, expression through posture alone, vast empty white space filling
most of each panel, no background beyond one essential prop, optional
ground line, black on white only with no shading or texture, thin or
absent panel borders, deadpan diagram-clean web-native cartooning.

[FORMAT]
One single square panel, 1:1. Exactly one panel. One caption line set
below the panel frame, plain lowercase, no box and no rule. No speech
balloon anywhere in the image.

[CHARACTER: Wren]
Stick-simple figure, circle head, dot eyes, two-stroke body, round
glasses as the only distinguishing mark.

[PANEL 1 — BREAK]
Medium shot, eye level. White void with an optional thin ground line.
Wren stands at frame right holding a full watering can, expression
flat. At frame left, a small potted plant with five leaves, clearly
thriving, and beside it a second smaller plant of the same kind. Wide
empty space between the figure and the plants. Roughly seventy percent
of the panel empty.

[SCENE]
Nowhere: white void, optional ground line, nothing else. No light
model, no weather, no horizon.

[NEGATIVE]
shading, gradients, texture, color, background scenery, line weight
variation, text on image, speech balloon, caption box, ruled caption
frame, facial features beyond dots, hair detail, multiple panels,
panel grid.
```

**Two negatives here exist because of the format, not the style.** `multiple panels, panel grid` is the single most likely failure: a backend handed a comic style reaches for a strip, and this format's whole definition is that it does not have one. And `caption box, ruled caption frame` protects the fix that made this project possible — the caption is permitted here, but boxless, so the negative has to distinguish *caption text* from *caption box* rather than banning captions wholesale.

Generation log: bible v1.0.0 · shot-plan deskplant-001 · seed 51204 · 0 RETAKEs.
