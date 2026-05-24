# Negative Prompt Library Derivation Example

## Input (from World Bible)
```yaml
negative_library:
  global: "extra fingers, deformed hands, blurry, low quality, text, watermark"
  per_character:
    Akira: "modern clothing, bright colors, cartoonish proportions"
```

## Derived Negative Prompt (output)
```
extra fingers, deformed hands, blurry, low quality, text, watermark, modern clothing, bright colors, cartoonish proportions
```

## Usage
This combined negative prompt is appended to every generation call for Akira.