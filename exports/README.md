# Exports

Generated consistency artifacts land here, derived from the World Bible by `comic-world-bible-system` (see its "Export Formats for Consumers" section).

## Expected Structure

```
exports/
├── dna-templates/           # per-character prompt fragments (YAML)
├── model-sheets/            # model sheet generation prompts + outputs
├── shot-plans/              # Director shot plans per strip/page (YAML)
├── production-briefs/       # Producer project contracts (YAML)
├── consistency-config.json  # LoRA / IP-Adapter weights, negative blocks
└── style-grammar.yaml       # linework, screentone, hatching rules
```

## Consumers

| Artifact | Consumed by |
|----------|-------------|
| `dna-templates/` | `comic-character-consistency-system` |
| `model-sheets/` | `comic-character-consistency-system` |
| `shot-plans/` | `comic-pipeline` skills, `comic-image-generation-adapter` |
| `production-briefs/` | `comic-producer`, all pipelines (contract check) |
| `consistency-config.json` | `comic-image-generation-adapter` |
| `style-grammar.yaml` | `comic-style-memory-system` |

Everything in this folder is **derived** — regenerate from the bible rather than editing by hand. Canonical truth lives in the World Bible.
