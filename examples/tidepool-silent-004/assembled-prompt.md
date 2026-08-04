# Assembled Prompt — Tidepool 004 (canonical order per `comic-image-generation-adapter`)

Backend: GPT-Image-class, single-call multi-panel. Blocks assembled verbatim from their owning artifacts — nothing here was authored at generation time.

The block order is unchanged, but two blocks behave differently under this pattern and the difference is the point of reading it.

```text
[STYLE]
Ink-wash storybook manga style, brush-drawn contour with natural
pressure variation, sumi ink wash in three value steps with no flat
fills and no hatching, overcast diffuse light with no cast shadows,
value carried by wash density, warm paper ground with visible fibre,
soft edges where wash meets paper, restrained composition with
generous empty ground, hand-brushed panel borders, quiet storybook
print feel.

[FORMAT]
One wide 21:9 image, exactly three panels, read left to right, clean
vertical gutters, wide gutter before the third panel. No lettering
of any kind anywhere in the image.

[CHARACTER: Mira]
Child around seven, dark bobbed hair, oversized yellow raincoat worn
unbuttoned, bare feet, rolled trousers.

[PANEL 1 — SETUP]
Wide shot, eye level. Wet rock tidepool shelf in three wash values.
Mira entering from the left, stopped mid-stride with one foot still
raised, looking toward the right of the frame. A small five-armed
starfish on the rock at the right, off-centre. No text.

[PANEL 2 — REINFORCE]
Close-up, high angle. Two small hands entering the frame palms up
beside the starfish, not touching it. Brush weight on the starfish
identical to the brush weight on the fingers. Mouth not visible. No
text.

[PANEL 3 — TURNAROUND]
Wide shot, eye level, largest panel. The waterline, the starfish just
below the surface and already fading into the wash. Mira small in the
upper left, her back turned, walking away toward the next pool. No
text.

[SCENE]
Tidepool Shelf and Waterline at low tide: overcast diffuse light, wet
rock, no sun glare, no cast shadows.

[NEGATIVE]
speech balloon, thought balloon, caption box, sound effect lettering,
onomatopoeia, text on image, open shouting mouth, flat colour fills,
hatching, cast shadows, deformed hands, extra fingers, adult
proportions, footwear.
```

**`[FORMAT]` carries the pattern lock, not just the canvas.** "No lettering of any kind anywhere in the image" is a *pattern* constraint sitting in the format block, because that is the block a backend reads for what the picture must physically be. A pattern that forbids an element has to state it where elements are described.

**The negative block spends six of its entries on silence.** Balloon, thought balloon, caption, SFX lettering, onomatopoeia, text — plus `open shouting mouth`, which is the subtle one. A backend given a child reacting to something will draw a shout, and a shouting face imports speech without drawing a single letter. Silent does not mean *soundless-looking*; it means the strip cannot smuggle a line in through a face. That negative is why panel 2 took two retakes.

Under the bleed taxonomy these are **pattern bleed** — a class the world bible's four buckets do not name, because the taxonomy was written for identity, style, era, and anatomy. Recorded here as a finding; the bible currently files them under `project_wide_negatives`.

Generation log: bible v1.0.0 · shot-plan tidepool-004 · seed 33907 · 2 RETAKEs (P2 open mouth, twice).
