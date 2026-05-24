# Style-Specific Technical Mastery: Computational Simulation of Manga & Printmaking Techniques
## Overview
Five foundational art styles — retro manga screentone, gekiga cinematic framing, ligne claire, Junji Ito body horror, and woodcut/printmaking — each have distinct, technically definable visual grammars. Computational approaches to simulating these styles range from classical signal-processing and physics-based fluid dynamics to deep learning methods including VAEs, GANs, and diffusion models. Understanding the underlying mechanics of each style is prerequisite for any credible simulation or generation system.

***
## 1. Retro Manga Screentone + Brush Pen Simulation
### What Screentone Actually Is
Screentone (スクリーントーン) in traditional manga is a physical adhesive film bearing pre-printed halftone dot or line patterns, applied to black-and-white artwork to create tonal gradation without continuous grayscale. The physical technique creates a fundamentally binary medium — pure black and pure white pixels only — using spatial frequency (dots-per-inch, angle, dot size) to create the *perception* of gray. The key parameters are:[^1]

- **Screen ruling** (lines per inch): typical manga screentone runs 25–65 lpi
- **Dot shape**: circular, elliptical, square, or line-based patterns
- **Screen angle**: typically 45° to minimize moiré when multiple tones are overlapped
- **Dot size (relative to tone value)**: larger dots = darker apparent tone at fixed ruling[^2][^3]

Moire artifacts emerge when screentones are digitally rescaled because the periodic grid pattern creates aliasing against the display pixel grid. This is a core engineering problem in manga digitization and rendering.[^4]
### Computational Screentone Generation
The classical approach models screentone generation as a **halftoning problem**. Given an intensity value \(I \in [0, 1]\) at a pixel, the screentone renders it as a dot whose area fraction equals \(I\) within each screen cell. The three dominant algorithms are:[^2]

- **Ordered (Bayer) dithering**: maps intensity against a precomputed threshold matrix, producing a regular, patterned output ideal for faithful screentone simulation
- **Error diffusion (Floyd-Steinberg)**: distributes quantization error to neighboring pixels, producing stochastic dispersion — less "authentic" to manga screentone but perceptually smooth[^5][^2]
- **Stochastic (FM) screening**: uses simulated annealing or dot-placement to generate dispersed, non-periodic patterns — appropriate for modern manga digital screentone tools[^5]

Krita's screentone generator implements this directly, offering configurable screen cell shapes (circle, diamond, line), ruling, and alignment-to-pixel-grid to prevent moiré. The grid-alignment parameter controls how often screen cell corners fall on integer pixel coordinates, suppressing aliasing artifacts.[^1][^3]
### Deep Learning Approaches
The SIGGRAPH Asia 2020 paper **"Manga Filling Style Conversion with Screentone Variational Autoencoder" (ScreenVAE)** by Xie et al. is the authoritative deep learning work in this area. The architecture:[^6][^7]

1. Trains a VAE to map screened manga regions into a **continuous intermediate latent domain** that encodes local texture characteristics — essentially a "semantic screentone descriptor"
2. This latent space is **interpolative**: blending two screentone descriptors yields plausible in-between patterns
3. A second network translates between this intermediate domain and color comics, enabling **bidirectional conversion** (color→screentone and screentone→color)

The critical insight is that screened and color fills are fundamentally incompatible: color fills have continuous spatial variation, while screentone fills are spatially uniform patterns. The VAE intermediate domain bridges this by abstracting the tonal *intent* from the physical *encoding*.[^8][^9]

For super-resolution, a 2023 arxiv paper addresses the specific problem that naive upsampling destroys screentone density semantics — it first classifies each region's screentone type, then applies specialized SR models per class, preserving the density relationship between dots and tone value.[^10][^11]

The 2025 paper on **inference-time trajectory optimization for manga image editing** (arXiv 2603.27790) extends this to screentone synthesis in editing contexts, comparing against task-specific trained models.[^12]

For vectorization, Yao et al. (IEEE TVCG 2017) present a full pipeline: adaptive binarization → screentone detection → classification as simple (dots/lines with extractable parameters) vs. complex (irregular) → procedural shader reconstruction for resolution-independent rendering.[^13]
### Brush Pen Simulation
Japanese brush pen (fude pen) simulation is substantially more complex than screentone. The physics involves:

- **Bristle bundle deformation**: individual bristle dynamics under pressure/velocity
- **Ink transfer**: ink loading of bristles as a finite reservoir that depletes per stroke
- **Capillary flow into paper**: ink migration along cellulose fibers governed by the Lucas-Washburn equation \( L = \sqrt{\frac{r \gamma \cos\theta}{2\eta} \cdot t} \) where \(L\) is penetration depth, \(r\) is pore radius, \(\gamma\) is surface tension, \(\theta\) is contact angle, and \(\eta\) is viscosity[^14][^15]

**MoXi** (SIGGRAPH 2005) is the canonical real-time ink dispersion paper. It models paper as a disordered porous medium and uses the **lattice Boltzmann equation (LBE)** for fluid simulation, chosen because LBE handles percolation in irregular media efficiently at real-time speeds. The simulation tracks:[^16][^17]
- Ink concentration in paper fibers
- Capillary-driven lateral spread (the "blooming" visible in wet brush strokes)
- Pressure-dependent flow rate

A 2025 Georgia Tech breakthrough extended ink-in-water diffusion simulation using a novel **vorticity-viscosity interaction model** from a particle flow map perspective, achieving the most physically accurate ink dispersion simulations to date.[^18]

For stroke shape synthesis, pressure-sensitive Bézier spline interpolation is the practical standard: sample points \(P_i\) from a tablet → compute tangents \(T_i = P_{i+1} - P_{i-1}\) → build piecewise cubic Bézier with control points at \(Q_2 = P_i + 0.3T_i\) and \(Q_3 = P_{i+1} - 0.3T_{i+1}\) → modulate stroke width via pressure mapping.[^19]

The Murdoch University paper **"Shape-Driven Oriental Brush Stroke Synthesis"** approaches this from the contour side: given a shape's outline, it synthesizes Oriental brush strokes along those contours following traditional stroke direction rules.[^20]

***
## 2. Gekiga: Cinematic Framing and Realism
### The Gekiga Visual Grammar
Gekiga (劇画, "dramatic pictures") was coined by Yoshihiro Tatsumi in 1957 as a deliberate counter to mainstream children's manga. The defining visual characteristics, as distinguished from standard manga:[^21]

| Feature | Standard Manga | Gekiga |
|---|---|---|
| Character proportions | Exaggerated (large eyes, small mouth) | Realistic, anatomically plausible |
| Shading | Screentone for tonal fill | Heavy ink brush, crosshatch, spot blacks |
| Panel layout | Uniform grids, dynamic irregular for action | Cinematic cuts, deep staging, noir compositions |
| Page rhythm | Rapid, energetic pacing | Deliberate, film-like scene construction |
| Background | Suggestive / simplified | Detailed urban / gritty environmental realism |

The primary influence is cinema — specifically noir film and Italian neorealism — rather than animation. Saito Takao's work (Golgo 13) exemplifies the style: "cinematic visual expression with effective use of closeups or wide shots" is the defining visual characteristic according to manga critic Shimada Kazushi.[^22][^23][^24]
### Cinematic Panel Mechanics
Gekiga directly codes film grammar into panel sequences:

- **Closeup / extreme closeup**: isolates psychological interiority — a tightly cropped face mid-action communicates inner state without dialogue, borrowing from Eisenstein's montage theory[^22]
- **Wide establishing shots**: used for environmental grounding, drawn with precision linework to communicate social context (cramped apartments, industrial docks)
- **Depth staging**: characters arranged at multiple Z-depths in a single panel, often with heavy foreground occlusion — derived from deep-focus cinematography (Welles, Kurosawa)[^25]
- **Fisheye/wide-angle distortion**: Saito's work explicitly replicates wide-angle lens distortion in panel drawings, stretching foreground elements[^22]
- **Panel bleeding**: important action shots bleed to page edge, breaking grid — direct cinema analogy to the close-up push-in

The Comics Journal analysis of Tatsumi notes how gekiga artists experimented with "how a closeup might express the interiority of a character; how to synchronize a story's action with the pace of the reader's gaze as it covered the page" — treating panel sequence as a time-based medium.[^26]
### Heavy Inking as Computational Problem
Gekiga's heavy spot-black rendering (solid fills, deep shadow masses) is technically a thresholded ink fill where tonal regions below a luminance threshold collapse to pure black. Computationally, this maps to:

1. Grayscale input → luminance thresholding with a configurable shadow threshold \(T_{shadow}\)
2. Midtones rendered as coarse crosshatch or parallel ink lines (not screentone dots)
3. Ink line variability: slight irregularity in hatching line spacing and pressure to avoid mechanical uniformity

This is substantially different from screentone manga and closer to the crosshatching NPR literature. The SIGGRAPH 2017 generalized crosshatching paper by Du and Akleman formalizes this: map scene intensity to progressively eroded/dilated crosshatch textures, interpolating between slices in a texture array.[^27]

***
## 3. Ligne Claire: Uniform Line Weight + Color Flatness
### Definitional Properties
Ligne claire (clear line) was developed by Hergé across the Tintin series beginning 1929 and named by Joost Swarte in 1977. The defining formal constraints are:[^28]

- **Uniform line weight throughout**: all contours — foreground objects, background buildings, grass blades — drawn with the *same* stroke width. No line weight hierarchy to denote depth or lighting[^29][^30]
- **No hatching or crosshatch shading**: tone is communicated exclusively through flat color fill, never through line density variation
- **Cartoonish figures against realistic backgrounds**: a cognitive tension that paradoxically enhances legibility by keeping character silhouettes clean against detailed environments[^31][^30]
- **Cast shadows as filled shapes, not gradients**: shadow areas are hard-edged flat fills, typically a slightly darker hue of the surface color, not gradients or crosshatch

Hergé's own articulation: "the biggest difficulty with comics is to show exactly what is necessary and sufficient to understand the story; nothing more, nothing less". The visual philosophy is one of maximum narrative clarity through formal restraint.[^31]
### Technical Implementation
The line weight uniformity rule creates an interesting constraint for digital rendering. In standard NPR/illustration practice, line weight encodes depth (thicker foreground, thinner background), light direction (thinner lit side, thicker shadow side), and occlusion (heavier where surfaces meet). Ligne claire deliberately violates all three conventions, creating a "democracy of lines".[^32][^33][^34]

Computationally simulating ligne claire requires:

1. **Contour extraction** at uniform thickness: this is a straightforward edge detection → stroke rendering problem, but the critical constraint is enforcing *constant* stroke width regardless of depth buffer, normal variation, or luminance
2. **Semantic region segmentation** for flat fill: each closed region receives a single flat color. The challenge is correctly identifying region boundaries — regions are defined by the contour lines, not by color bleeding or gradient fill
3. **Color palette constraint**: ligne claire uses a limited, saturated palette with flat application. No gradients, no specular highlights modeled as color variation — highlights, if present, are white hard-edged shapes
4. **Background-foreground style split**: realistic-detail backgrounds require separate handling from simplified-figure foregrounds

For AI style transfer to ligne claire, the key loss terms in a GAN-based approach would need to enforce: (a) uniform stroke width in extracted contours, (b) minimal color variance within semantic segments, (c) hard shadow boundaries rather than gradient penumbrae. Standard neural style transfer (Gatys et al.) typically fails here because it captures texture statistics globally rather than enforcing structural constraints per segment.[^35]

***
## 4. Junji Ito: Body Horror Distortion Methods
### The Visual Grammar of Ito's Horror
Junji Ito's technique operates on a principle of **controlled contrast** as a storytelling mechanism. His work is structurally organized in two modes, deployed sequentially within each story:[^36][^37]

**Mode 1 — Normative baseline (pre-horror):** 
- Clean, uniform linework with controlled, parallel hatching
- Realistic character proportions with fine, precise detail
- Restrained mark-making that reads as conventionally attractive
- Characters rendered with delicate linear strokes suggesting normalcy

**Mode 2 — Horror escalation:**
- Hatch lines become irregular, densely packed, and "panicked" in rhythm
- Character proportions begin distorting: elongation, compression, surface proliferation (spirals, appendages, mouths)
- Mark pressure increases: strokes thicken and become erratic
- Background rendering becomes more aggressively detailed precisely as figures deform

This contrast is the psychological mechanism: the transition between modes signals horror to the reader neurologically before the narrative confirms it.[^37][^36]
### Body Distortion Techniques
Ito's body horror operates on several specific deformation types:[^38][^39][^40]

- **Spiral integration** (Uzumaki): anatomical structures — hair, limbs, the body itself — are progressively replaced by spiral topologies. The horror emerges from the uncanny recognition that the form is still anatomically legible as human while being geometrically impossible. Spirals appear first in scenery and character details before infecting the body itself, building dread through repetition of the motif
- **Anthropometric inversion**: faces rendered with hyper-realistic detail — precise pore texture, wet-looking eyes, subtle facial asymmetry — placed against bodies with impossible proportions. The face's hyperrealism makes the body's distortion more disturbing than if both were equally stylized
- **Surface proliferation**: normal skin surfaces sprout additional faces, mouths, or eyes. Ito renders these additions with the same precise linework as the "real" features, refusing visual hierarchy that would otherwise identify them as foreign
- **Elongation under persistence**: bodies stretched beyond anatomical limits while the character survives and remains psychologically present — the horror is the continued consciousness inside an impossible form[^38]
### Hatching as Psychological Signal
The hatching gradient in Ito's work is computationally definable. In calm scenes, hatching lines are:
- Spaced regularly (2-4px at print resolution)
- Parallel, following anatomical form direction
- Consistent pressure (uniform stroke weight)

In horror peaks, the same regions use:
- Irregular, compressed spacing (often 1px gaps)
- Crossing directions (crosshatch becoming frantic multi-directional)
- Variable pressure creating thicker/thinner erratic strokes
- Lines that overshoot boundaries, creating a "bleeding" effect[^36][^37]
### Computational Modeling
Simulating Ito-style distortion computationally involves two distinct challenges:

**Hatching density modulation**: map a "horror intensity" scalar to hatching parameters. At \(h = 0\) (calm), generate ordered parallel hatching using the crosshatch shader approach (Du & Akleman 2017). As \(h \to 1\), inject angular noise into stroke direction, reduce inter-stroke spacing, and add stroke width variation via Perlin noise.[^27]

**Body morphology distortion**: this is a non-rigid deformation problem. Ito's spirals suggest conformal mapping: a spiral warp field \(W(x, y) = r \cdot e^{i(\theta + k \cdot r)}\) in polar coordinates introduces winding distortion proportional to \(k\). Elongation is a simpler affine stretch with limb-boundary-aware masking to avoid breaking figure-ground separation.

The uncanny effect arises not from the distortion itself but from the preservation of fine detail *within* the distorted regions — this argues for distortion applied to the geometry rather than the texture, so surface detail remains crisp within the transformed space.

***
## 5. Woodcut / Printmaking Simulation
### Physical Process Model
Traditional woodcut is a relief printing process: carve away areas that should remain white (the recesses), leaving only the image-bearing ridges in relief; ink the surface; press paper. The visual characteristics that result from this physical process:[^41]

- **Ink squeeze**: ink is mechanically pressed outward from ridges, creating slightly heavier edges ("ink spread")
- **Grain directionality**: wood grain runs parallel to the plank's long axis; carving perpendicular to grain is difficult, so linework tends to align with grain direction — creating characteristic parallel-line shading in that axis
- **Relief texture**: carved areas often retain faint texture from the gouging tool, visible as micro-irregularity in the white areas
- **Registration error** (multi-block color prints): each color plate is printed separately, and slight misalignment creates colored outlines or halos around shapes
### Computational Approaches
**Virtual Woodcuts from Images** (Mello & Jung, ACM 2007) is the foundational paper for image-to-woodcut conversion. The pipeline:[^42][^43]
1. Image segmentation into regions
2. Computation of orientation fields (analogous to grain direction)
3. Generation of wood-grain-aligned parallel lines within each region at density proportional to luminance
4. Thresholding and binary rendering with ink-spread simulation

**Reaction-Diffusion Woodcuts** (Mesquita & Walter, GRAPP 2019) takes a markedly different approach: Rather than orientation-field line generation, it uses Turing's reaction-diffusion system to generate the patterns. The pipeline:[^44][^45]

1. Segment input image
2. Generate a **parameter map** that encodes desired pattern type per region: spots (Turing spots), stripes (Turing stripes), or plain black/white
3. Run reaction-diffusion on the parameter map, allowing different regions to evolve under different kinetic parameters
4. Apply binary threshold to produce final woodcut appearance

The reaction-diffusion approach naturally produces organic, non-mechanical texture that better resembles actual woodcut grain compared to purely geometric line generation.[^44]

**Virtual Drypoint** (Tasaki et al., CGF 2004) extends this to copperplate intaglio simulation, which shares formal similarities with woodcut but produces finer lines with characteristic "burr" — the rough metal edge that catches ink and creates slightly fuzzy line edges. The model uses physical modeling of the engraving tool's interaction with the plate material.[^46]

**NPR Crosshatching** as a general framework (SIGGRAPH 2017, Du & Akleman) applies directly to woodcut simulation because woodcut shading *is* crosshatching implemented in carved relief. The triplanar mapping approach maps scene luminance to a pre-generated crosshatch texture array (from light → dark, applied via erosion/dilation), providing real-time woodcut-style rendering of 3D scenes.[^27]

For digital painting workflows, the practical approach chains:
1. Start with a high-contrast black-and-white source
2. Apply grain-direction-aligned line patterns (using a texture aligned to wood grain direction)
3. Simulate ink spread via a small morphological dilation of black regions
4. Add registration jitter if simulating multi-color ukiyo-e woodblock prints
5. Apply paper texture (washi or similar) via multiply blend mode[^47]

***
## 6. Computational Simulation of Traditional Media: Key Papers
| Technique | Key Paper | Method | Venue |
|---|---|---|---|
| Screentone generation | Xie et al. (2020) ScreenVAE | Variational Autoencoder, bidirectional GAN | SIGGRAPH Asia 2020 |
| Screentone-aware SR | Yao et al. (2023) | DL region classification + specialized SR | arXiv cs.CV |
| Screentone retargeting | arXiv 2203.03396 (2022) | Hierarchical grid anchor + RPSM | CGF 2025 |
| Manga vectorization | Yao et al. (2017) | Adaptive binarization + procedural shaders | IEEE TVCG |
| Ink dispersion (paper) | MoXi — Chu & Tai (2005) | Lattice Boltzmann equation, porous media | ACM SIGGRAPH |
| Ink diffusion (real-time) | Grid-particle method (2012) | Grid-particle hybrid fluid simulation | NLPR/IAAC |
| Paint simulation | Mi et al. (2013) | SPH + Fick's law diffusion + Lucas-Washburn | CAV Journal |
| Brush stroke synthesis | Data-Driven Ink Painting (2023) | Neural stroke rendering | Simo-Serra Lab |
| Oriental brush strokes | Shape-Driven Synthesis | Sketch-based contour-driven algorithm | Murdoch Univ. |
| Woodcut from images | Mello & Jung (2007) | Orientation fields + luminance-mapped lines | ACM |
| Reaction-diffusion woodcut | Mesquita & Walter (2019) | Turing RD parameter maps + thresholding | GRAPP 2019 |
| Crosshatching NPR | Du & Akleman (2017) | Triplanar intensity-mapped texture array | SIGGRAPH |
| Virtual drypoint | Tasaki et al. (2004) | Physical tool-plate model | CGF |
| Watercolor/ink NPR | Various (SIGGRAPH post-1995) | Diffusion, absorption, paper fiber models | SIGGRAPH |
### Ink-Paper Physics: The Core Simulation Problem
Across all traditional media simulation, the underlying physics is consistent: ink or pigment deposited on a porous substrate undergoes capillary-driven lateral diffusion, depth absorption, and evaporation-driven fixation. The relevant physical equations:

- **Lucas-Washburn equation** (capillary penetration): \(L(t) = \sqrt{\frac{r \gamma \cos\theta}{2\eta} \cdot t}\)[^14]
- **Fick's second law** (diffusion of pigment concentration \(C\) through medium): \(\frac{\partial C}{\partial t} = D \nabla^2 C\)[^48][^14]
- **Lattice Boltzmann** (fluid dynamics in porous media): models percolation through disordered fiber networks at real-time speeds[^16]

Real-time ink simulation using a **grid-particle hybrid** (NLPR 2012) combines an Eulerian grid for global flow and Lagrangian particles for local pigment tracking, achieving visually realistic results at interactive framerates.[^49]

The 2025 Georgia Tech breakthrough introduced a new viscosity model solving for **vorticity-viscosity interaction from a particle flow map perspective**, enabling more physically accurate trajectory tracking of ink dispersion than prior Navier-Stokes approaches.[^18]

***
## Synthesis: Cross-Style Implementation Insights
For a generative AI system targeting any of these styles, the key architectural insight is that they exist on a spectrum of rule-based vs. emergent properties:

- **Screentone** and **ligne claire** are highly rule-based: their defining properties can be expressed as hard constraints (binary pixel values, uniform stroke width, flat fill). Rule-enforcement in loss functions or architectural constraints (e.g., quantization layers) is more reliable than pure generative approaches.

- **Gekiga** and **woodcut** are texture-defined: heavy inking patterns and relief marks have statistical texture properties amenable to style transfer (Gram matrix losses, perceptual losses on texture features).

- **Junji Ito's distortion** is semantically defined: the horror-escalation hatching gradient requires understanding of narrative tension, making it the most difficult to automate without semantic scene understanding. The spatial distortions are mathematically tractable (conformal maps, non-rigid deformation fields), but the *when* to apply them is a narrative parsing problem.

The most powerful current approaches combine segmentation (separating regions by style role), physics-based simulation for ink/media behavior, and GAN/diffusion-model generation for the non-rule-bound texture and mark-making elements.[^50][^51][^7]

---

## References

1. [Screentone](https://docs.krita.org/de/reference_manual/layers_and_masks/fill_layer_generators/screentone.html) - How to use Screen Tone generation in Krita.

2. [Algorithm to make halftone images?](https://stackoverflow.com/questions/1258047/algorithm-to-make-halftone-images) - What is a good algorithm to make halftone images (like this)? A quick google search brings up a bunc...

3. [Screentone — Krita Manual 5.3.0 documentation](https://docs.krita.org/en/reference_manual/layers_and_masks/fill_layer_generators/screentone.html) - How to use Screen Tone generation in Krita.

4. [Screentone-Preserved Manga Retargeting](https://ar5iv.labs.arxiv.org/html/2203.03396) - As a popular comic style, manga offers a unique impression by utilizing a rich set of bitonal patter...

5. [A Dot Placement Approach to Stochastic Screening Using ...](https://library.imaging.org/admin/apis/public/api/ist/website/downloadArticle/print4fab/20/1/art00074_1)

6. [Manga filling style conversion with screentone variational autoencoder](https://dl.acm.org/doi/10.1145/3414685.3417873) - Western color comics and Japanese-style screened manga are two popular comic styles. They mainly dif...

7. [GitHub - msxie92/ScreenStyle: Implementation for "Manga Filling Style Conversion with Screentone Variational Autoencoder" (SIGGRAPH ASIA 2020 issue)](https://github.com/msxie92/ScreenStyle) - Implementation for "Manga Filling Style Conversion with Screentone Variational Autoencoder" (SIGGRAP...

8. [Manga Filling Style Conversion with Sreen VAE](https://ttwong12.github.io/papers/screenstyle/screenstyle.html)

9. [Manga filling style conversion with screentone variational ...](https://research.monash.edu/en/publications/manga-filling-style-conversion-with-screentone-variational-autoen/)

10. [Screentone-Aware Manga Super-Resolution Using DeepLearning](http://arxiv.org/abs/2305.08325) - Manga, as a widely beloved form of entertainment around the world, have shifted from paper to electr...

11. [Screentone-Aware Manga Super-Resolution Using DeepLearning](https://arxiv.org/abs/2305.08325) - In this paper, we aims to address this issue by first classifying the regions and lines of different...

12. [Inference-time Trajectory Optimization for Manga Image Editing - arXiv](https://arxiv.org/html/2603.27790v1) - In our experiments, we evaluate two applications, text removal and screentone synthesis, and compare...

13. [Manga Vectorization and Manipulation With Procedural Simple ...](https://pubmed.ncbi.nlm.nih.gov/26863665/) - We classify detected screentone into simple and complex patterns: our system extracts simple screent...

14. [Realistic paint simulation based on fluidity, diffusion, and absorption](https://onlinelibrary.wiley.com/doi/full/10.1002/cav.1500) - We present a new method to create realistic paint simulation, utilizing the characteristics of paint...

15. [[PDF] Pressure based ink diffusion model for real-time simulation of ...](https://www.semanticscholar.org/paper/Pressure-based-ink-diffusion-model-for-real-time-of-Wang-Rokne/307a5e747aaf457bcb93031ff66542b1f45656e9) - This paper describes a novel approach to simulating Chinese calligraphy for digital image purposes t...

16. [MoXi: real-time ink dispersion in absorbent paper - ACM Digital Library](https://dl.acm.org/doi/10.1145/1073204.1073221) - We devise a novel fluid flow model based on the lattice Boltzmann equation suitable for simulating p...

17. [Paint program renders ink physics TRN 062905](http://www.trnmag.com/Stories/2005/062905/Paint_program_renders_ink_physics_Brief_062905.html) - The simulation is based on mathematics -- the lattice Boltzmann ... (MoXi: Real-Time Ink Dispersion ...

18. [Computer Graphics Team Makes Breakthrough in Simulating Ink ...](https://research.gatech.edu/computer-graphics-team-makes-breakthrough-simulating-ink-diffusion) - This new simulation lets you map physical quantities from a certain time frame, allowing us to see p...

19. [I need an algorithm for rendering soft paint brush strokes](https://stackoverflow.com/questions/85993/i-need-an-algorithm-for-rendering-soft-paint-brush-strokes) - I have an array of mouse points, a stroke width, and a softness. I can draw soft circles and soft li...

20. [[PDF] Shape-driven Oriental Brush Stroke Synthesis](https://researchportal.murdoch.edu.au/esploro/fulltext/conferencePaper/Shape-driven-Oriental-Brush-Stroke-Synthesis/991005544040207891?repId=12136257340007891&mId=13137069190007891&institution=61MUN_INST) - In this paper, we present a smart sketch-based algorithm for simulating Oriental brush strokes on sh...

21. [Yoshihiro Tatsumi - Wikipedia](https://en.wikipedia.org/wiki/Yoshihiro_Tatsumi)

22. [An Introduction to Gekiga, 6970 A.D. - Page 2 of 4](https://www.tcj.com/an-introduction-to-gekiga-6970-a-d/2/) - “An Introduction” describes the different ways in which Saitō's work, as representative of contempor...

23. [Manga: Gekiga Style](https://www.manga-me.me/resources/manga-gekiga-style) - Turn your photos into high-quality manga with MangaMe, the leading AI manga generator app. Create st...

24. [How Golgo 13 Creator Saitō Takao Changed Manga](https://www.nippon.com/en/japan-topics/g01210/) - Saitō Takao, creator of many manga including the wildly popular Golgo 13, passed away from pancreati...

25. [Kurosawa's Geometry Comes Alive in This Short Cinematic Essay](https://www.vice.com/en/article/kurosawas-geometry-comes-alive-in-this-short-cinematic-essay/) - The Geometry of a Scene is a new short from Every Frame a Painting film essayist Tony Zhou, who in t...

26. [Tracing the Genealogy of Gekiga _ the Japan Times](https://www.scribd.com/document/510509452/Tracing-the-Genealogy-of-Gekiga-the-Japan-Times) - Yoshihiro Tatsumi is considered the "grandfather of alternative manga" in Japan. He pioneered the ge...

27. [GitHub - JonGreenberg/Crosshatching: A simple implementation of a NPR crosshatching shader](https://github.com/JonGreenberg/Crosshatching) - A simple implementation of a NPR crosshatching shader - JonGreenberg/Crosshatching

28. [Ligne claire - Wikipedia](https://en.wikipedia.org/wiki/Ligne_claire)

29. [The Clear Line. Herge, Tintin and Ligne Claire](https://www.sausalitoferry.com/blogs/news/the-clear-line-herge-tintin-and-ligne-claire) - Comic art has seen countless styles throughout the decades. Some adhere to standard practices, like ...

30. [Ligne Claire | Aesthetics Wiki - Fandom](https://aesthetics.fandom.com/wiki/Ligne_Claire) - Ligne Claire, meaning "clear line," is an art style pioneered by Hergé, the creator of The Adventure...

31. [Hergé & The Clear Line](http://www.paulgravett.com/articles/article/herge_the_clear_line) - Explore the ever-changing worlds of Comics, Graphic Novels, and Manga, with the author of 'Comics Un...

32. [Lines in Technical Illustration - Northwestern Computer Science](https://users.cs.northwestern.edu/~bgooch/ITI/node4.html) - These static images represented edge lines with black lines of uniform weight. ... Middle: heavy lin...

33. [Line Weight Hierarchy - Gurney Journey](http://gurneyjourney.blogspot.com/2008/09/line-weight-hierarchy.html) - This “line weight hierarchy” follows specific rules. First, as an object gets closer to the viewer, ...

34. [How do you know what the line thickness should be? : r/learnart](https://www.reddit.com/r/learnart/comments/14sepvx/how_do_you_know_what_the_line_thickness_should_be/) - Lines on the shadow side should be thicker than lines on the light side. Lines on things that are cl...

35. [Your daily dose of machine learning : Neural style transfer...but fast!](https://www.reddit.com/r/learnmachinelearning/comments/qxdyx0/your_daily_dose_of_machine_learning_neural_style/) - With this approach, there are two neural networks working together. One network extracts the style f...

36. [Junji Ito Techniques | Longstride Illustration](https://longstrideillustration.com/junji-ito-techniques/) - Once again, he uses mark-making strokes to communicate a transformation from attractive to grotesque...

37. [Junji Ito Techniques | Master Study in Pen and Ink - YouTube](https://www.youtube.com/watch?v=V0X18-iushI) - In this video, I share observations about Junji Ito, the master of horror, as I render some of his i...

38. [Junji Ito Showcase, Part 1: Ito & Body Horror | Skirt Defense Force](https://skirtdefenseforce.wordpress.com/2016/01/01/junji-ito-showcase-part-1-ito-body-horror/) - Ito's stories often feature the human body being stretched and twisted in ways that are physically i...

39. [Junji Ito Techniques | Master Study in Pen and Ink - YouTube](https://www.youtube.com/watch?v=V0X18-iushI) - In this video, I share observations about Junji Ito, the master of horror, as I render some of his i...

40. [The Maddening Spirals of Junji Ito's Uzumaki - Panel Patter](https://www.panelpatter.com/2015/05/the-maddening-spirals-of-junji-itos.html?m=1) - The gut punch of Ito's horror lands in the images he draws, characters infected by spirals who under...

41. [Woodcut - The Metropolitan Museum of Art](https://www.metmuseum.org/perspectives/materials-and-techniques-printmaking-woodcut) - The oldest form of printmaking, woodcut is a relief process in which knives and other tools are used...

42. [Virtual woodcuts from images - ACM Digital Library](https://dl.acm.org/doi/10.1145/1321261.1321280) - We present in this paper a technique for synthesizing virtual woodcuts based on real images. Woodcut...

43. [Virtual woodcuts from images | Semantic Scholar](https://www.semanticscholar.org/paper/Virtual-woodcuts-from-images-Mello-Jung/fd0be22504c6607378bff165f31319e3803c7f55) - This paper presents a technique for synthesizing virtual woodcuts based on real images based on four...

44. [Reaction-diffusion Woodcuts - SciTePress](https://www.scitepress.org/PublishedPapers/2019/73859/) - In this paper, we present an approach for computer simulated woodcuts using reaction-diffusion as th...

45. [[PDF] Reaction-Diffusion - Semantic Scholar](https://www.semanticscholar.org/paper/Reaction-Diffusion-Mesquita-Walter/a9a61168a85a184a15590b84685f103ab49f2646) - In this paper, we present an approach for computer simulated woodcuts using reaction-diffusion as th...

46. [Virtual Drypoint by a Model‐driven Strategy - Tasaki - 2004](https://onlinelibrary.wiley.com/doi/0.1111/j.1467-8659.2004.00774.x) - In this paper we propose a method to synthesize a virtual copperplate print image based on physical ...

47. [How would I best produce my own faux woodblock print if I ... - Reddit](https://www.reddit.com/r/Design/comments/88vuqa/how_would_i_best_produce_my_own_faux_woodblock/) - How would I best produce my own faux woodblock print if I have a B&W image. Would an inkjet printer ...

48. [A non-photorealistic rendering method based on Chinese ink and ...](https://www.nature.com/articles/s40494-022-00825-z) - We use the empirical ink diffusion simulation model to process it, and use the background texture ge...

49. [[PDF] Real-time ink simulation using a grid-particle method](https://nlpr.ia.ac.cn/2012papers/gjkw/gk45.pdf) - This paper presents an effective method to simulate the ink diffusion process in real time that yiel...

50. [Stroke-based stylization by learning sequential drawing examples](https://www.sciencedirect.com/science/article/abs/pii/S1047320317302444) - This stroke-based rendering [13] underpins many artistic rendering algorithms, especially on those e...

51. [[PDF] Data-Driven Ink Painting Brushstroke Rendering - Simo-Serra Lab.](https://esslab.jp/publications/MadonoPG2023.pdf) - WetBrush [CKIW15] is a famous painting simulation framework that simulates brush movements and rende...