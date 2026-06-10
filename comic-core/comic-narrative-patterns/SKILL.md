---
name: comic-narrative-patterns
version: 1.0.0
category: comic-core
description: The sanctioned library of narrative beat patterns beyond the default Setup→Reinforce→Turnaround — kishōtenketsu, gag escalation, slow-burn reveal, parallel action, and the silent strip — with panel mappings, payoff rules, and McCloud transition guidance.
---

# Comic Narrative Patterns

**Core principle**: Variation is sanctioned, not freeform. A project uses **one** pattern, locked in the project contract by the Producer — but the library offers six, not one.

This skill ends the single-pattern monoculture: `setup-reinforce-turnaround` remains the default, and five additional patterns are now first-class citizens, each with its own discipline.

## When to Use

- During Producer brief intake, to select the pattern that fits premise + format + style
- During Director shot planning, to map beats to panels
- When a story idea keeps fighting the 3-beat arc — the fix is usually the pattern, not the premise

## The Pattern Library

### 1. `setup-reinforce-turnaround` (Default)
- **Beats**: SETUP → REINFORCE → TURNAROUND
- **Panels**: 3 (native) — the contract defined in `comic-structural-contract`
- **Payoff rule**: Panel 3 reframes the emotion; tone per style (warm / earned / eerie / triumphant)
- **Best fit**: Almost everything; the proven short-form arc

### 2. `kishotenketsu` (起承転結 — Four-Act, Twist Without Conflict)
- **Beats**: **ki** (introduce) → **shō** (develop) → **ten** (unexpected recontextualization) → **ketsu** (reconcile)
- **Panels**: 4 (native to `4koma-vertical`; works in 2×2 grid)
- **Payoff rule**: *ten* is not a punchline — it is a perspective shift; *ketsu* must reconcile both threads without explaining the joke
- **Best fit**: Manga styles, slice-of-life, contemplative humor; the historically correct pattern for 4-koma
- **Anti-pattern**: Treating *ten* as the ending — kishōtenketsu without *ketsu* is just an interrupted thought

### 3. `gag-escalation` (Rule of Three)
- **Beats**: PATTERN → PATTERN (intensified) → BREAK
- **Panels**: 3 (native); single-panel variant compresses the pattern into implied context
- **Payoff rule**: Beats 1–2 must be *visibly parallel* (same framing family) so the break in beat 3 reads instantly; the break violates expectation, not logic
- **Best fit**: Newspaper strips, chibi/kawaii, underground comix, minimalist webcomics
- **Anti-pattern**: Three unrelated jokes in a row — escalation requires repetition with variation

### 4. `slow-burn-reveal`
- **Beats**: WITHHOLD → HINT → REVEAL
- **Panels**: 3–6; the reveal earns the largest panel and the widest preceding gutter
- **Payoff rule**: The reveal must be *retroactively legible* — re-reading panel 1 with the new knowledge must reward the reader; the camera conspires (crops and angles hide honestly, never cheat)
- **Best fit**: Horror, noir, gekiga, mystery; the native pattern for `junji-ito-body-horror` and `noir-expressionist-comic`
- **Anti-pattern**: A reveal the reader had no chance to anticipate — shock without setup is noise

### 5. `parallel-action`
- **Beats**: THREAD A → THREAD B → (alternate) → CONVERGE
- **Panels**: 4+ (needs `2x2-grid-page`, `webtoon-scroll-segment`, or multi-page)
- **Payoff rule**: The convergence panel must change the meaning of *both* threads; threads stay visually distinct (location palette, framing family) until they meet
- **Best fit**: Action, adventure, romance (two characters approaching one meeting)
- **Anti-pattern**: Cutting between threads without a convergence — parallel lines must eventually touch

### 6. `silent-strip`
- **Beats**: any pattern above, executed with **zero dialogue**
- **Panels**: format-native count
- **Payoff rule**: Every beat must be carried by staging, expression, and McCloud closure alone; if a beat needs words, the shot plan is wrong
- **Best fit**: Ink-wash, watercolor, woodcut, literary styles; the strongest test of directorial craft
- **Anti-pattern**: Silence as decoration — a silent strip with an illegible arc fails Layer 3

## Transition Guidance (McCloud, Operationalized)

| Pattern | Workhorse transitions | Spend sparingly |
|---------|----------------------|-----------------|
| setup-reinforce-turnaround | action-to-action, subject-to-subject | moment-to-moment (one, for the beat before the turn) |
| kishotenketsu | subject-to-subject | aspect-to-aspect (the *ten* often lives here) |
| gag-escalation | action-to-action (parallel framing) | none — keep transitions invisible |
| slow-burn-reveal | moment-to-moment, subject-to-subject | scene-to-scene (only to relocate the dread) |
| parallel-action | scene-to-scene (between threads) | non-sequitur never |
| silent-strip | moment-to-moment, aspect-to-aspect | dialogue substitutes of any kind |

## Selection Rules

1. The Producer locks **one pattern per project** in the contract; episodic projects may vary pattern per episode only if the contract says so
2. The pattern must be **format-compatible** (see `comic-format-library` — e.g., kishōtenketsu needs 4 beats, so not the 3-panel default)
3. The Director maps beats to panels in the shot plan; beats never split across two panels, and no panel carries two beats
4. Turnaround/payoff **tone** still follows the style's table in `comic-structural-contract`

## Integration

- Extends `comic-structural-contract` (which remains the default 3-beat contract)
- Consumed by `comic-producer` (selection) and `comic-director` (beat mapping)
- `comic-quality-gates` Layer 3 evaluates arc integrity against the **locked pattern**, not against the default

---

*One pattern is a formula. A library of patterns, each with discipline, is a craft.*
