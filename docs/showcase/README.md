# Visual Showcase

This folder contains repo-native visual artifacts that make the skill stack understandable at a glance.

## Assets

- [`../assets/foundational-comic-skills-hero.svg`](../assets/foundational-comic-skills-hero.svg) — animated comic-style hero art for the README.
- [`../assets/comic-skill-stack-map.svg`](../assets/comic-skill-stack-map.svg) — animated system map of the production stack.
- [`../assets/style-gallery-reel.svg`](../assets/style-gallery-reel.svg) — animated six-frame style reel: one scene re-skinned through six locked style contracts (Golden Age, Manhwa Webtoon, Ligne Claire, Gekiga, Cyberpunk, Watercolor). Each frame's palette, line weight, and texture honor the **Prompt Block** and **Style Quality Gates** of its `comic-styles/` skill.
- [`../assets/setup-reinforce-turnaround-strip.svg`](../assets/setup-reinforce-turnaround-strip.svg) — animated three-panel strip performing the flagship `setup → reinforce → turnaround` narrative pattern, including a `RETAKE`-worthy chaos panel and a Producer/Director `PASS` resolution.

## Style fidelity notes for the gallery reel

| Frame | Lock evidence in the SVG |
| --- | --- |
| Golden Age | Halftone dot pattern overlay, 5px uniform outlines, yellow caption + burst balloon, cream newsprint field |
| Manhwa Webtoon | Teal night gradient vs warm lamp glow (soft radial), thin closed 2.5px lines, soft glow filters |
| Ligne Claire | Single 3px line weight on every contour, flat unmodulated fills, zero shadows or gradients |
| Gekiga | Pure B&W, 35° crosshatch pattern wedges, solid spot-black diagonal, heavy 4.5px brush-weight borders |
| Cyberpunk | Two locked neon accents (cyan + magenta), one readable sign, neon blur filter rim light, scanline overlay, rain streaks |
| Watercolor | Gaussian-soft edges, pigment bloom circles, paper grain pattern, hand-wobbled border path, reserved paper whites |

## Why SVG instead of generated PNG?

SVG keeps the visuals versionable, lightweight, accessible, and diffable. The animation is CSS-only, so the README stays portable and does not depend on hosted image-generation URLs.

## Future visual upgrades

- Add generated sample panels for each flagship style once the repo has canonical art direction for those samples.
- Add side-by-side "bad prompt vs directed shot plan" examples.
- Add a webtoon-scroll demo strip assembled from the same world bible.
