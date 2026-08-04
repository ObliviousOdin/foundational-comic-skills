# Research Foundation — Traceability Map

Six studies ground the system. Research is only useful here when a skill operationalizes it; this map shows where each finding became a contract.

| Research Document | Key Findings | Operationalized In |
|-------------------|--------------|--------------------|
| `PANEL-COMPOSITION-THEORY.md` | McCloud's 6 transitions, gutter closure, T-rule, rule of thirds, eyelines | `comic-narrative-patterns` (transition guidance), `comic-director` (camera grammar, eyeline choreography), `comic-format-library` (T-rule, reading direction) |
| `COMIC-TIMING-AND-PACING.md` | Space = time; panel size & gutter width as tempo; silence for payoff | `comic-director` (pacing & emotional modulation), `comic-structural-contract` (visual rhythm), `comic-webtoon-scroll-pipeline` (scroll-gap timing) |
| `ARTISTIC-DECISION-MAKING-PROCESS-MODELING.md` | The manga *name* system & its 5 editor criteria; four crop questions; PINS narrative grammar; decision layering | `comic-director` (shot plan = digital *name*, crop check), shot-plan template (`name_criteria` block) |
| `COMIC-ART-EVALUATION-FRAMEWORKS.md` | Flow-first editorial rubric; 180° rule; gesture > polish; AI failure tells | `comic-director` (final cut order), `comic-quality-gates` (Layer 6 Artistic Life), `comic-producer` (review policy) |
| `ADVANCED-CONSISTENCY-SYSTEMS.md` | Layered conditioning, IP-Adapter/LoRA orchestration, world bible architecture | `comic-world-bible-system`, `comic-character-consistency-system`, `comic-image-generation-adapter` (assembly contract) |
| `STYLE-SPECIFIC-TECHNICAL-MASTERY.md` | Screentone physics, ligne claire doctrine, gekiga framing, ink behavior | Style skills (Schema v2 locks & consistency notes), `comic-style-memory-system` |

## Contracts That Trace to No Study

The table above runs one direction: research is trivia unless a skill enforces it. The map is only honest if it runs the other way too. Several enforced contracts cite nothing above, and the distinction that matters is whether that is *legitimate* or *unexamined*.

| Contract | Actual basis | Verdict |
|----------|--------------|---------|
| **Prompt Block trust boundary** (`tools/validate.py`, quality-gates Layer 0) | Engineering, not art. The block is concatenated verbatim into a live generation prompt, so every contributed style skill is an untrusted-input boundary | **Legitimate.** No comics study could ground this — it is a property of the generation pipeline, not of comics. Cite the threat model |
| **Prompt Block collision threshold (0.60)** | Measured across this corpus: the closest legitimately adjacent pair sits at 0.27 | **Legitimate but local.** The number describes these 30 styles and should be re-measured, not inherited, if the corpus changes character |
| **Format-scope rule** (`CONTRIBUTING.md`) | Five defects found and fixed, not a study | **Legitimate.** An internal finding, labelled as one |
| **Nonfiction `source_register`** (`comic-world-bible-system`) | Journalism sourcing and attribution norms | **Gap.** The repository holds no documentary-comics study, so a shipped style's central ethical lock rests on assumed practice rather than a cite-able foundation |

## Gaps the Research Names That Remain Open

- Real-time micro-decision capture during execution (the *name* → final-art translation) — partially mitigated by the Director's decision log
- Cross-cultural production differences (manga vs. Western vs. BD planning) — reading-direction rule covers the structural piece only
- Statistical aesthetics residuals (~25–50% of judgment unexplained) — Layer 6 stays a human/Director call by design
- **Documentary and comics-journalism practice** — named above as the one contract resting on assumed practice; a study covering sourcing standards, consent, and the ethics of depicting real subjects would put `reportage-comics-journalism` on the same footing as every other style

---

*Research that no skill enforces is trivia; a contract that cites nothing is either engineering or an assumption. This map names which.*
