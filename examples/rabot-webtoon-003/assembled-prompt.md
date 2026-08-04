# Assembled Prompt — Long Night ep-01 (canonical order per `comic-image-generation-adapter`)

Backend: per-panel generation (scroll segments are stitched, not produced in one call). Blocks assembled verbatim from their owning artifacts — nothing here was authored at generation time.

Two differences from the strip examples, both forced by the format:

- **`[FORMAT]` is per-panel plus a stitching contract.** A 7-panel scroll segment is not one image, so the format block carries the working unit (800×1280) and the gap that follows each panel. Gap height is a *directed* value from the shot plan, not a layout afterthought — it is this format's primary pacing instrument.
- **The negative block carries `side-by-side panels`.** Backends reach for multi-panel grids when given several beats; the one thing `webtoon-scroll-segment` forbids outright is horizontal adjacency, so it is stated as a negative rather than trusted to the format block.

Panel 4 shown in full; the remaining six follow the same block order.

```text
[STYLE]
Modern Korean webtoon manhwa style, full color digital art, clean
even lineart with closed contours and subtle color holds,
cinematic color grading with cool teal ambient against warm key
light, soft volumetric lighting and glow, soft-edged colored
shadows, painterly-soft backgrounds behind crisp characters,
contemporary K-drama staging, full-bleed vertical panel
composition built for scroll reading, polished serialized webtoon
production finish.

[FORMAT]
One vertical panel, 800x1280 working unit, full-bleed width, read
top to bottom as part of a seven-panel scroll segment. Panel 4 of
7. Followed by a half-screen vertical white gap before the next
panel. Single panel only.

[CHARACTER: Rabot — screen left]
Young man, short dark hair, navy work jacket over white shirt,
small scar on left cheek, clean digital lineart, cool ambient with
warm key.

[CHARACTER: Echo — screen right]
Compact android with feminine silhouette, short silver hair, round
indicator light at the left temple rendered cool white, matte gray
coverall, clean digital lineart.

[PANEL 4 — HINT]
Medium shot, eye level. Echo's head turning up and to the left,
her gaze exiting the top of the frame toward something unseen
above. Rabot in the same frame, unchanged, still working at the
console, not looking up. No dialogue. One small typographic sound
effect, a soft "tk", color-matched to the grade.

[SCENE]
Control Room, perpetual station night: cool teal ambient, warm
practical key from the console, monitor glow as fill. The status
board is out of frame above.

[NEGATIVE]
side-by-side panels, multi-panel grid, panel borders in the gutter,
speech bubble crossing the panel edge, black and white, screentone,
chibi proportions, gradients on lineart, text on image, deformed
hands; amber light of any kind in this panel; for Rabot: silver
hair, temple light; for Echo: facial scar, navy jacket, amber
temple light.
```

**On the panel-level amber negative.** `alert-amber` is a reserved swatch in bible v4 — it appears only on the status board and light cast by it. Panel 4 is the beat *before* the board enters frame, so amber leaking in here would spend the reveal three panels early. The reservation lives in the bible; enforcing it per panel is the adapter's job, and it is the kind of thing Layer 0 checks before a render is paid for.

Generation log: bible v4 (2026-08-04, webtoon color mode) · shot-plan webtoon-003-ep01 · seeds 44120–44126 · 1 RETAKE (P5 bubble straddled the screen-2/3 boundary; moved wholly above the fold).
