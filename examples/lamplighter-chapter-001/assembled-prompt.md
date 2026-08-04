# Assembled Prompt — The Lamplighter ch-001, page 5 panel 3 (canonical order per `comic-image-generation-adapter`)

Backend: per-panel generation. Blocks assembled verbatim from their owning artifacts — nothing here was authored at generation time.

Panel 5.3 is shown because it is the chapter's argument in one image: a gas standard burning perfectly inside the arc-light flood, doing its job while the job ceases to exist. The remaining 28 panels follow the same block order.

```text
[STYLE]
Fully painted prestige comic style in the Alex Ross tradition,
gouache and oil realism with no ink outlines, edges resolved by
value and color, classical portrait lighting with a single warm key
and museum glow, realistic anatomy and heavy fabric weight,
monumental history-painting composition, soft atmospheric depth,
controlled naturalistic palette, visible brushwork and dry-brush
texture, hand-painted caption plates, restrained formal lettering,
gallery-grade painted finish.

[FORMAT]
One panel of a six-panel printed page, 2:3 portrait page, page 5 of
6, recto. Medium shot occupying the middle register of the page. No
panel border decoration; painted edges.

[CHARACTER]
No figures in frame. This panel is a location beat.

[PANEL 5.3 — TEN]
Medium shot, eye level. A single cast-iron gas standard still
burning, its flame and mantle clearly alight, standing inside a
flood of cold white arc light that erases its amber pool entirely.
The lamp is unmistakably lit and contributes nothing to the
illumination of the scene. Stone parapet behind, river fog below.
No dialogue, no caption.

[SCENE]
Kell Bridge (electrified): unbroken cold white from overhead arc
lamps, no warm pools, no dark between. Late autumn, first light,
river fog rising.

[NEGATIVE]
ink outlines, cel shading, flat colour fills, lens flare,
photorealistic skin texture, text on image, modern clothing,
warm ambient light filling the scene, visible arc lamp fixtures in
frame, figures, speech balloons.
```

**Two negatives here are doing narrative work, not hygiene.** `warm ambient light filling the scene` protects the whole point of the panel: a backend given "gaslight" reaches for a warm scene, which would restore exactly the atmosphere the chapter has just taken away. And `visible arc lamp fixtures in frame` keeps the new light sourceless and total — showing the fixture would make it a thing that could be argued with, rather than a condition.

This is the kind of check quality-gates Layer 0 catches before a render is paid for: the negative block is merged from the bible's `project_wide_negatives` plus per-panel additions the shot plan justified, and it is never hand-written at generation time.

Generation log: bible v1.0.0 · chapter-map ch-001 · shot-plan ch-001-p05 · seeds 90311–90339 · 4 RETAKEs across the chapter (see the production brief decision log; p4.3 took two).
