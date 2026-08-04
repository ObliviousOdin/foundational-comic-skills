# Assembled Prompt — Grid Pieces 002, panel 3 (canonical order per `comic-image-generation-adapter`)

Backend: per-panel generation, stitched to the grid afterwards. Blocks assembled verbatim from their owning artifacts — nothing here was authored at generation time.

Panel 3 is shown because it carries the format's whole argument: it is thread B *resumed* after a panel away, and the pause only reads as hesitation because of where the grid puts it.

```text
[STYLE]
Ligne claire Franco-Belgian comic style in the Hergé school,
absolutely uniform ink line weight on every contour, zero hatching
or feathering, flat unmodulated gouache color zones, no cast
shadows, slightly cartooned economical faces over precise
documentary architecture, equal line treatment for foreground and
background, clean depth planes, rounded speech balloons with thin
uniform borders, neat hand lettering, mid-century European album
print feel, maximum clear-line readability.

[FORMAT]
One panel of a four-panel 2x2 grid page, square canvas, bottom-left
position, read on the Z-path. Single panel only, no internal
divisions, no grid inside the frame.

[CHARACTER: Perrin Vale]
Young man, early twenties, tall and narrow, municipal electrical
inspector's slate uniform, wire-rim spectacles, ink stain on the
right cuff.

[PANEL 3 — THREAD B]
Close-up, eye level. A hand holding a pen, the nib resting
stationary on a printed form, a small ink blot spreading outward
from where it has rested. Slate cuff at the frame edge. No face in
frame. No dialogue.

[SCENE]
Bridge Keeper's Hut: single oil lamp interior, warm and close, the
window admitting cold blue from outside.

[NEGATIVE]
line weight variation, hatching, crosshatching, feathering,
gradients, cast shadows, painterly texture, photorealistic faces,
sketchy background, text on image, multiple panels, panel grid,
panel borders inside the frame.
```

**`multiple panels, panel grid` is the load-bearing negative here.** Every panel of this page is generated alone and stitched, and a backend told the format is a 2x2 grid will happily draw the grid *inside* one panel. The format block says single panel; the negative block says it again, because this is the failure a grid format invites and the one Layer 0 exists to catch before a render is paid for.

Generation log: bible v1.0.0 (Lamplighter) · shot-plan kell-grid-002 · seeds 61180–61183 · 1 RETAKE (P3: gutters first assembled into a clean cross; re-laid with the 6mm stagger).
