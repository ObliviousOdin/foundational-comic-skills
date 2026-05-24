# World Bible Validation Rules v1.0

## Structural Rules
- Must contain all top-level keys: visual_grammar, character_compendium, world_register, negative_library, version_history
- character_compendium must have at least 1 entry
- Every character must have a non-empty dna_template

## Content Rules
- visual_grammar.linework.weight must be one of: thin, medium, bold
- Every character must have at least 3 canonical views defined
- negative_library.global must not be empty

## Consistency Rules
- No duplicate character names
- All referenced asset paths must exist relative to the bible file
- Version history must have entries in reverse chronological order

## Severity Levels
- ERROR: Blocks usage
- WARNING: Allows usage but flags for review
- INFO: Informational only

## Automated Checks (Planned)
- JSON Schema validation
- Asset path existence check
- Cross-character consistency scan
- Style grammar completeness check