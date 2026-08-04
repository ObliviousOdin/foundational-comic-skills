# Assembled Prompt — 4koma-002 (canonical order per `comic-image-generation-adapter`)

Backend: GPT-Image-class (single-call multi-panel). Blocks assembled verbatim from their owning artifacts — nothing here was authored at generation time.

Note the block that changed shape from strip-001: `[FORMAT]` now states equal panel heights and uniform gutters explicitly, because the 4-koma constraint is the one thing a backend will silently violate if left unsaid. It defaults to varying panel sizes for emphasis, which is exactly the tempo mechanism this format forbids.

```text
[STYLE]
Chibi kawaii comic style, locked two-head super-deformed
proportions, thick rounded uniform outlines in soft charcoal,
sticker-flat pastel fills from a small fixed swatch set of
blossom pink, cream, mint and powder blue, single flat pastel
shadow tone, emoji-style symbolic faces with dot eyes and simple
mouth shapes, oversized cute emotion icons, flat pastel
backgrounds with simple dot or stripe patterns, adorable toy-like
sticker finish.

[FORMAT]
One tall 1:3 image, exactly four panels in a single column, read
top to bottom. All four panels exactly equal in height. Uniform
horizontal gutters throughout - no panel is larger or set apart.

[CHARACTER: Rabot — screen left]
Two-head chibi young man, short dark hair, navy work jacket, dot
eyes, tiny single-stroke scar mark on the cheek, collar up.

[CHARACTER: Echo — screen right]
Two-head chibi android girl, short silver hair, round indicator
light at the left temple drawn as a full circle, matte gray
coverall.

[PANEL 1 — KI]
Medium full shot, eye level. Chibi Rabot centred on a flat mint
field, both hands wrapped around a toy-round dented thermos,
squint-arc eyes, looking down into it. One puffy rounded bubble
upper-left, clear of the head: "Still warm."

[PANEL 2 — SHO]
Medium full shot, eye level. Chibi Echo enters from frame right on
the same flat mint field, sparkle-O eyes, holding a second cup in
both hands, looking toward Rabot. Rabot unchanged, still looking
down. One puffy rounded bubble upper-right, clear of the temple
light: "Mine's cold."

[PANEL 3 — TEN]
Extreme wide exterior. The whole station seen small against a dark
flat hull field, drawn in the same rounded sticker grammar. One
tiny lit window. No figures. No text of any kind.

[PANEL 4 — KETSU]
Medium full shot from behind, eye level. Back inside on the mint
field: both chibis side by side seen from behind, Rabot screen left
and Echo screen right, two cups, both facing a small bright window.
No dialogue.

[SCENE]
Control Room in chibi mode: flat pastel fields instead of rendered
light, one soft shadow tone. Station Exterior: dark flat hull, one
lit window, no starfield glare.

[NEGATIVE]
realistic proportions, adult body ratio, gradients, rendered
lighting, harsh pure black outlines, photorealistic, text on image,
deformed hands, panels of differing heights, varied gutter widths;
for Rabot: silver hair, temple light; for Echo: facial scar, navy
jacket.
```

Generation log: bible v3 (2026-08-04, chibi mode) · shot-plan 4koma-002 · seed 118803 · 0 RETAKEs.
