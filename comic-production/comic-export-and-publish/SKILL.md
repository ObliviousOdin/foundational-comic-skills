---
name: comic-export-and-publish
version: 1.0.0
category: comic-production
description: Platform delivery contract — canvas/resolution/color specs per destination (Instagram, X, webtoon platforms, print zine, PDF chapter), lettering minimums, file naming, and archival rules for the Producer's sign-off.
---

# Comic Export & Publish

**Core principle**: A comic isn't delivered until it survives its platform. Export specs are part of the project contract, not an afterthought at sign-off.

The Producer selects target platforms at brief intake; this skill supplies the specs those choices imply.

## Platform Matrix

| Destination | Canvas | Resolution | Color | Notes |
|-------------|--------|------------|-------|-------|
| Instagram feed | 1:1 or 4:5 | 1080×1080 / 1080×1350 | sRGB | 3-panel strips re-cut to carousel (one panel per card) read better than one squeezed wide image |
| X / horizontal social | 16:9 | ≥1600×900 | sRGB | The native home of `3-panel-horizontal`; preview crop ~2:1 — keep balloons off the extreme edges |
| Webtoon platforms | 800 px wide column | slices ≤1280 px tall | sRGB | Export scroll segments as sequential slices; never split a panel or balloon across a slice boundary |
| Print zine (B&W) | A5/half-letter + 3 mm bleed | 600 dpi line art / 300 dpi tone | Grayscale or 1-bit | Screentone styles export 1-bit to avoid rescreening moiré; check tone ruling survives the print lpi |
| Print (color) | per spec + 3 mm bleed | 300 dpi | CMYK (coated/uncoated profile per printer) | Four-color era styles (`golden-age-superhero-comic`, `pop-art-lichtenstein-comic`) preview in CMYK from the start |
| PDF chapter | 2:3 page | 300 dpi | sRGB (screen) / CMYK (print-on-demand) | Embed fonts if real text layers exist; otherwise flatten lettering |

## Lettering Minimums (Legibility Floor)

- On-screen: rendered text ≥ ~12 px x-height at the platform's default zoom; phone-width test for webtoon and social
- Print: ≥ 6 pt effective; never let bleed-safe margins crop a balloon (balloons live inside the safe area, 5 mm from trim)
- Re-cuts (e.g., strip → carousel) re-run the `comic-lettering-and-balloons` order test per crop

## Re-Cut Rules (One Master, Many Deliverables)

- The locked format from `comic-format-library` is the **master**; platform variants are derived crops/re-slices, never re-generations
- A re-cut may change panel framing margins, never panel content or order
- If a platform demands a different aspect than the master can honestly give, the Producer adds it to the contract as a second deliverable — at panel-budget cost — rather than distorting the master

## File Naming & Structure

```
exports/deliverables/
└── <project>/<episode>/
    ├── master/        strip-007-master.png        (full resolution, locked format)
    ├── instagram/     strip-007-ig-p1.png …       (per-card)
    ├── webtoon/       ep03-slice-01.png …         (sequential slices)
    └── print/         ep03-pages-cmyk.pdf
```

- Names carry project, episode/strip number, platform, and sequence — sortable, no spaces
- Every deliverable folder includes a `manifest.txt`: bible version, shot-plan ids, generation-log references

## Archival Rules (Sign-Off Requirement)

- Keep: masters, generation logs, shot plans, the production brief, and the bible version used — enough to reproduce or extend the episode a year later
- The Producer's sign-off checklist item "exports generated" means **this matrix**, not "some PNGs exist"

## Integration

- Specs feed the Producer's brief intake (platform field) and sign-off protocol
- Consumes masters produced by the pipelines; lettering checks per `comic-lettering-and-balloons`
- Slicing rules for scroll work follow `comic-webtoon-scroll-pipeline`

---

*The platform is the last panel of every comic — design for it like one.*
