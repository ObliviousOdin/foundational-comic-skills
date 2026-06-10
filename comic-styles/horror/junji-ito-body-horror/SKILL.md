---
name: junji-ito-body-horror
version: 2.0.0
category: comic-styles
description: Junji Ito body-horror manga — pristine faces and clinical whites against escalating fine-line wrongness, spiral fixation, and slow-burn reveals where the dread was already here.
---

# Junji Ito Body Horror

**Style Lock (do not deviate)**

- Junji Ito school horror manga: black and white, pre-digital ink feel, maru-pen fine-line patience throughout
- **Two-mode rendering contract**: normative baseline (clean faces, sparse texture, ordinary rooms) → horror escalation; the modes must be visibly distinct
- Obsessive fine-line detail density **escalates with wrongness** — hatching and stippling are the dread dial; calm panels stay clinical and sparse
- **Spiral/pattern fixation**: each project fixes ONE motif (spiral, holes, scales, strands…) logged in the world bible; all distortion grows from that motif
- Pristine, hyper-realistic faces that distort **only at the reveal**; impossible anatomy rendered with full anatomical precision, never simplified
- Dense pooled blacks against clinical white negative space; controlled contrast is a psychological signal, not decoration
- Stippled decay textures (pores, rot, proliferating surfaces) built from individual dots, not gray fills
- Thin ruled panel borders — the page stays orderly while its contents stop being

## Negative Locks

- No color; no digital gradients, airbrush glow, bloom, or lens blur
- No splatter-gore shock language (spurting blood, slasher framing) — wrongness beats gore
- No distortion, texture creep, or warped anatomy in WITHHOLD/setup panels; the baseline must read genuinely normal
- No cartoon-horror shorthand (jagged scream bubbles everywhere, googly monster eyes)
- No photo textures or 3D-render sheen; every texture is hand-stippled ink

## When to Use

- Body horror, curses, cosmic and psychological dread, obsession stories
- Reference images that read uneasy, fixated, or slightly *off* in one detail
- When the brief asks for `slow-burn-reveal` — this style is its native habitat

## When Not to Use

- Lurid moralistic twist-horror with a narrator → use `horror-ec-comics-style`
- Hard-boiled human crime and stark contrast → use `sin-city-graphic-noir` or `noir-expressionist-comic`
- Gritty realist drama with nothing impossible → use `gekiga-cinematic-manga`

## Story Harness (Image-Driven)

- Runs `slow-burn-reveal` natively: SETUP carries WITHHOLD, REINFORCE carries HINT, TURNAROUND carries REVEAL
- **SETUP** (WITHHOLD): pristine ordinary scene, clean line, sparse hatching; the fixated motif is already present but innocuous — wallpaper, a teacup, a curl of hair; level medium shot
- **REINFORCE** (HINT): detail density rises; the motif repeats in a second and third place; faces stay pristine while one feature begins to fixate (a stare, a tilt); camera steps closer
- **TURNAROUND** (REVEAL): eerie and ironic — the dread was already here from panel one; face or body distorts with full fine-line commitment, biggest panel, dense blacks behind the distortion so the white wrongness glows

## World Guardrail

- Default modern-mundane Japanese settings: small coastal towns, school corridors, family homes, narrow streets — ordinary enough that wrongness has contrast
- Technology unremarkable and period-loose; no sci-fi hardware, no gadget plot devices
- The wrong thing obeys its own consistent curse-logic, recorded in the world bible and never broken for convenience

## Dialogue & Lettering

- Rounded bubbles with calm, even hand-lettering — the lettering stays composed even as the imagery distorts; inherits `comic-lettering-and-balloons`
- 1–2 bubbles per panel, ≤ ~10 words; the REVEAL is often silent or carries a single flat line of denial
- SFX policy: minimal; at most one creeping organic SFX at the reveal — silence is the louder instrument

## Direction Notes

- Camera diet: level, composed medium shots early — the camera must not editorialize before the reveal; close-up is reserved for REVEAL
- Transition diet: moment-to-moment and subject-to-subject; scene-to-scene only to relocate the dread (per `comic-narrative-patterns`)
- Pacing: even gutters through WITHHOLD and HINT, then one wide gutter — a held breath — before the reveal panel
- RTL eligible: lock reading direction in the contract; eyelines exit per the locked direction

## Consistency Notes

- **What drifts first**: the hatching-density floor — calm panels start inheriting reveal-level texture, killing the escalation; lock baseline vs escalated density values in `comic-style-memory-system`
- The fixated motif's geometry must repeat exactly; store it as a style-memory asset, not a re-described prompt
- Pristine faces drift toward stylization under load; re-anchor against the canonical `comic-character-consistency-system` DNA sheet every 8–10 panels
- Multi-page escalation curves are scheduled by `comic-long-sequence-orchestrator` so density climbs by plan, not by accident

## Prompt Block

```text
Junji Ito style Japanese horror manga, black and white ink, pristine
hyper-detailed realistic faces, obsessive fine-line hatching and
stippling whose density escalates with wrongness, spiral and pattern
fixation motifs, body distortion rendered with anatomical precision,
dense pooled blacks against clinical white negative space, stippled
decay textures, thin ruled panel borders, quiet ordinary settings
hiding dread, pre-digital manga ink feel.
```

## Style Quality Gates

- [ ] SETUP panels read genuinely normal — no premature distortion or texture creep
- [ ] Detail density visibly increases panel-over-panel toward the reveal
- [ ] The fixated motif appears in every panel and stays innocuous until the reveal
- [ ] Reveal distortion preserves fine detail (no muddy blobs or gray fills)
- [ ] Blacks pooled and deliberate, whites clinical — no ambient mid-gray wash

## Integration

- Loads `comic-core` and `comic-consistency`; rendered via `comic-image-generation-adapter`
- Native habitat: `3-panel-horizontal` or `multi-page-chapter`; patterns `slow-burn-reveal` (native), `setup-reinforce-turnaround`, `kishotenketsu`; RTL eligible

---

*The horror is in the transition: the dread was already in panel one, waiting to be noticed.*
