# Walkthrough — Deskplant 001, "Week Six"

The smallest format in the library, and the one that found a contradiction.

## Why this project was built

`single-panel-gag` was the only sanctioned format carrying an **explicit exemption** that no artifact had ever exercised. Cycle 6 exempted it from the lettering silence rule — a one-panel format cannot be required to hold a silent panel without forbidding the only text the format allows. An untested exemption is where a defect hides, so this project went looking.

It found one immediately, and not the one that was expected.

## The contradiction

`minimalist-line-webcomic` listed `single-panel-gag` in its own native habitat, and its Dialogue & Lettering section said, without qualification:

> caption boxes remain forbidden

But `single-panel-gag` grants a caption line below the panel — it is the format's *only* exception to the no-caption rule — and `comic-lettering-and-balloons` names the format explicitly in the caption row's exception list. `elegant-art-nouveau-comic` had the same sentence and the same habitat claim.

So an agent pairing either style with a format the style itself recommends inherited a direct contradiction. Worse, the plausible resolution is the wrong one: drop the caption. In a single-panel gag the caption is frequently where the joke lands — which is exactly what happens in this panel.

Fixed upstream before this panel was planned (`minimalist-line-webcomic` and `elegant-art-nouveau-comic`, both 2.1.0). Neither style refuses the allowance now, and neither accepts it plainly: the format grants the element, the style governs how it looks. Minimalist sets the line boxless like a title card; art nouveau takes an ornamental cartouche.

## The beats that were never drawn

`gag-escalation` is PATTERN → PATTERN → BREAK. This format has one panel.

`comic-narrative-patterns` resolves it: the single-panel variant compresses the pattern into **implied context** — the drawn panel is the BREAK, and the two PATTERN beats live in what the reader reconstructs. The shot plan therefore carries an `implied_beats` block listing two beats that were never rendered:

1. Wren buys the plant and resolves to water it Sundays
2. Wren misses a Sunday and resolves harder

They are planned anyway, and that is the point worth taking from this example. A BREAK only reads as a break against a pattern the reader can rebuild. If the Director cannot state the implied beats, the reader has nothing to break against and the panel is not a gag — it is a picture with a caption under it.

## What the panel spends its one budget on

The format allows **one bubble or one caption, never both**. The joke here is an admission, so it goes in the caption and the panel stays silent.

The break is the second plant. Wren stands holding a full watering can; the deskplant has thrived anyway and reproduced. The caption — *week six. i have not watered it once.* — supplies the implied pattern in seven words, and the drawing supplies the break.

The final-cut note records the one real temptation: a resigned expression on Wren. It was held flat, because a resigned face explains the joke the caption already lands.

## Rules that do not apply, written down

The shot plan carries a `not_applicable` block naming four rules a reviewer might otherwise go hunting for:

| Rule | Why it does not apply here |
|------|----------------------------|
| Shot ladder | Needs adjacent panels to vary against; there are none |
| Transition budget | No transitions exist in a one-panel format |
| Silence rhythm | The format is exempt — an obligation here would forbid the only text allowed |
| Page turn | No pages |

Recording these is not bookkeeping. Three of the four are rules that *sound* universal, and this repository has now fixed seven defects that came from exactly that. A shot plan that states which rules are out of scope makes the next reader's audit cheap.

## The smallest bible that still passes

`world-bible.yaml` is deliberately minimal: one character, one prop, a location that is a void with a note saying it has no weather.

It still carries every required section, because a single-panel project has no continuity across panels to protect but everything to protect across a *series* of them. The fields that look trivially small — one prop, one signature mark, six expressions — are precisely the ones that drift when the same gag character comes back next week. The re-anchor interval is set to 4, the tightest in any example here, for that reason.

---

*One panel is not less contract. It is the same contract with nowhere to hide.*
