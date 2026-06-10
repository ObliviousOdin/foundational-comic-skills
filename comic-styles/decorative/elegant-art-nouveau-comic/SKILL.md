---
name: elegant-art-nouveau-comic
version: 2.0.0
category: comic-styles
description: Mucha-lineage Art Nouveau — whiplash contour lines, halo and arch framing, flat muted jewel tones with gold, and botanical borders for graceful ornamental storytelling.
---

# Elegant Art Nouveau Comic

**Style Lock (do not deviate)**

- Mucha-lineage poster sensibility, 1890s–1900s lithograph era — figures composed as decorative panels, never as snapshots
- **Whiplash contour lines**: long unbroken S-curves; the outer contour carries the heaviest weight, interior detail runs in finer line — never sketchy, never broken
- **Ornamental halo/arch framing**: the principal figure backed by a circle, horseshoe arch, or mosaic ring integrated into the composition
- Color discipline: **flat muted jewel tones with gold accents** laid as lithograph fills — or pure B&W-with-gold; one limited palette locked per project; no gradients, no rendered shading beyond line
- **Botanical border integration**: lilies, irises, vines, and poppies grow from the panel frame into the scene; ornament frames figures and never crosses a face or hands
- **Hair as a decorative line system**: strands drawn as flowing arabesques that merge into the surrounding ornament
- Panel borders are drawn architecture — ruled frames with ornamental corners, arch-topped where the beat is ceremonial

## Negative Locks

- No painterly gradients, airbrush, bloom, or photoreal rendering
- No grime, gore, or gritty urban texture
- No modern props — phones, cars, streetwear — unless the contract explicitly demands anachronism
- No saturated primary pop palettes or heavy black fills
- No ornament over faces or hands; legibility outranks decoration

## When to Use

- Romantic, mythic, allegorical, or fairy-tale material — beauty, longing, seasons, ceremony
- Reference images cueing elegance, flowing hair or fabric, florals, or poster composition
- Pieces that must work as decorative objects: covers, posters, a `single-panel-gag` played for grace instead of slapstick

## When Not to Use

- Soft painterly children's warmth → use `watercolor-storybook-comic`
- Floral-emotional romance in manga grammar → use `shoujo-romance-manga`
- Flat graphic irony and halftone pop → use `pop-art-lichtenstein-comic`

## Story Harness (Image-Driven)

- Translate the four cues into a small ceremony of feeling — a meeting, a season turning, a gift, a vow; the ornament must participate in the telling
- **SETUP**: figure introduced inside an ornamental frame — arch or halo establishing them as the panel's icon; the botanical border plants the strip's motif flower; pose elongated, serene
- **REINFORCE**: the motif develops — vines reach further into the frame, hair and drapery answer the emotion in longer curves; a second figure or object enters the arch's space; the palette deepens one step
- **TURNAROUND**: **graceful revelation** — the beauty reframes its meaning (the stranger was the season itself; the bouquet was a farewell); earned when the border motif completes itself around the final image and the halo now belongs to the revelation; largest, most ornamental panel

## World Guardrail

- Default setting: a belle-époque dream register — salons, gardens, theatres, riverbanks, terraces at dusk; myth and allegory welcome
- Props period or timeless: letters, mirrors, instruments, lanterns, garlands; technology ends at the gas lamp
- Seasons and flowers are the native vocabulary of mood; assign each story one motif bloom and keep it

## Dialogue & Lettering

- Sparse dialogue; smooth oval bubbles with thin ruled outlines, or lines set in small ornamental cartouches at the panel base — per `comic-lettering-and-balloons`, these are the only deltas; caption boxes remain forbidden
- ≤ 2 bubbles per panel, ≤ ~10 words, elevated but plain diction; the turnaround is often silent or single-line
- SFX policy: effectively none — at most one hand-drawn chime or musical mark woven into the ornament, once per strip

## Direction Notes

- Camera diet: frontal and three-quarter medium-full shots presenting figures like poster subjects; close-ups rare and reserved for the revelation
- Transition diet: subject-to-subject and aspect-to-aspect (face → flower → drapery) — this style thinks in motifs more than actions; avoid rapid action-to-action chains
- Pacing: generous, even gutters; the strip reads as a triptych altarpiece — symmetrical weight, final panel widest, carrying the completed border

## Consistency Notes

- **What drifts first**: ornament density (borders metastasize) and the gold accent spreading into full gilding; lock palette swatches and a per-strip ornament budget in `comic-style-memory-system`
- The motif flower must stay one species throughout — record it in the world bible; under drift, models substitute generic blooms
- The whiplash weight hierarchy (heavy contour, fine interior) flattens over iterations; re-anchor against the canonical sheet every 6–8 panels
- Halo/arch geometry must repeat identically when the same figure recurs

## Prompt Block

```text
Art Nouveau comic style in the Mucha poster lineage, flowing whiplash
contour lines with weighted outer line and fine interior detail, figures
framed by ornamental halos and horseshoe arches, flat muted jewel-tone
lithograph fills with gold accents, botanical borders of lilies and
vines growing from the panel frame, hair drawn as flowing decorative
arabesques, elongated serene figures, 1890s belle-epoque elegance,
ornamental ruled panel borders, no gradients or painterly shading.
```

## Style Quality Gates

- [ ] Outer contours visibly heavier than interior lines; curves long and unbroken
- [ ] Color fills flat lithograph-style; palette matches the project lock, gold placement included
- [ ] Halo or arch framing present behind the principal figure where the beat calls for it
- [ ] Border botany never overlaps faces or hands; the motif flower is one species throughout
- [ ] The final panel's ornament completes the strip's motif rather than introducing a new one

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` or `single-panel-gag`; patterns `setup-reinforce-turnaround`, `kishotenketsu`

---

*Ornament is not around the story; it is how the story is told.*
