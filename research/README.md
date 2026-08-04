# Research Foundation — Traceability Map

Seven studies ground the system. Research is only useful here when a skill operationalizes it; this map shows where each finding became a contract.

| Research Document | Key Findings | Operationalized In |
|-------------------|--------------|--------------------|
| `PANEL-COMPOSITION-THEORY.md` | McCloud's 6 transitions, gutter closure, T-rule, rule of thirds, eyelines | `comic-narrative-patterns` (transition guidance), `comic-director` (camera grammar, eyeline choreography), `comic-format-library` (T-rule, reading direction) |
| `COMIC-TIMING-AND-PACING.md` | Space = time; panel size & gutter width as tempo; silence for payoff | `comic-director` (pacing & emotional modulation), `comic-structural-contract` (visual rhythm), `comic-webtoon-scroll-pipeline` (scroll-gap timing) |
| `ARTISTIC-DECISION-MAKING-PROCESS-MODELING.md` | The manga *name* system & its 5 editor criteria; four crop questions; PINS narrative grammar; decision layering | `comic-director` (shot plan = digital *name*, crop check), shot-plan template (`name_criteria` block) |
| `COMIC-ART-EVALUATION-FRAMEWORKS.md` | Flow-first editorial rubric; 180° rule; gesture > polish; AI failure tells | `comic-director` (final cut order), `comic-quality-gates` (Layer 6 Artistic Life), `comic-producer` (review policy) |
| `ADVANCED-CONSISTENCY-SYSTEMS.md` | Layered conditioning, IP-Adapter/LoRA orchestration, world bible architecture | `comic-world-bible-system`, `comic-character-consistency-system`, `comic-image-generation-adapter` (assembly contract) |
| `COMICS-JOURNALISM-AND-DEPICTION-ETHICS.md` | Drawing has no negative, so provenance is recorded or lost; three registers (observed / reconstructed / represented); confidence grading; consent as distinct from sourcing; angle as editorial claim | `comic-world-bible-system` (§6 `source_register`, `source_note`), `reportage-comics-journalism` (negative locks, eye-level default, no invented interiority), `comic-producer` (consent is a publisher decision) |
| `STYLE-SPECIFIC-TECHNICAL-MASTERY.md` | Screentone physics, ligne claire doctrine, gekiga framing, ink behavior | Style skills (Schema v2 locks & consistency notes), `comic-style-memory-system` |

## Contracts That Trace to No Study

The table above runs one direction: research is trivia unless a skill enforces it. The map is only honest if it runs the other way too. Several enforced contracts cite nothing above, and the distinction that matters is whether that is *legitimate* or *unexamined*.

| Contract | Actual basis | Verdict |
|----------|--------------|---------|
| **Prompt Block trust boundary** (`tools/validate.py`, quality-gates Layer 0) | Engineering, not art. The block is concatenated verbatim into a live generation prompt, so every contributed style skill is an untrusted-input boundary | **Legitimate.** No comics study could ground this — it is a property of the generation pipeline, not of comics. Cite the threat model |
| **Prompt Block collision threshold (0.60)** | Measured across this corpus: the closest legitimately adjacent pair sits at 0.27 | **Legitimate but local.** The number describes these 30 styles and should be re-measured, not inherited, if the corpus changes character |
| **Format-scope rule** (`CONTRIBUTING.md`) | Nine defects found and fixed, not a study | **Legitimate.** An internal finding, labelled as one |
| **Nonfiction `source_register`** (`comic-world-bible-system`) | `COMICS-JOURNALISM-AND-DEPICTION-ETHICS.md` | **Closed.** Was the one enforced contract resting on assumed practice; the study now grounds it, and names three sourcing distinctions the schema still cannot express |

## Gaps the Research Names That Remain Open

- Real-time micro-decision capture during execution (the *name* → final-art translation) — partially mitigated by the Director's decision log
- Cross-cultural production differences (manga vs. Western vs. BD planning) — reading-direction rule covers the structural piece only
- Statistical aesthetics residuals (~25–50% of judgment unexplained) — Layer 6 stays a human/Director call by design
- ~~Three sourcing distinctions the schema cannot express~~ — **closed the same cycle they were raised.** `register`, `identifiability`, and `composite_disclosure` are schema fields and validator-enforced. What remains open is narrower: no worked example yet carries a nonfiction bible, so the fields are enforced but undemonstrated

---

*Research that no skill enforces is trivia; a contract that cites nothing is either engineering or an assumption. This map names which.*
