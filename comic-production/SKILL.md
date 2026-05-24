---
name: comic-production
version: 1.0.0
category: comic-production
description: Production and integration layer. Handles Hermes skill registration, CLI adapters, external tool integration (Higgsfield, Remotion, ComfyUI), and export workflows.
---

# Comic Production Layer

**Purpose**: This is the outermost layer that connects the comic skill system to real-world usage — Hermes, CLI tools, and external generation platforms.

## Planned Skills

| Skill | Description | Status |
|-------|-------------|--------|
| `comic-hermes-registration` | Registers all comic skills with Hermes | Planned |
| `comic-cli-adapter` | Command-line interface for the full system | Planned |
| `comic-higgsfield-adapter` | Direct integration with Higgsfield for generation | Planned |
| `comic-remotion-adapter` | Export to Remotion for animation/video | Planned |

## Design Goals
- Make the entire system usable from Hermes and terminal
- Provide clean adapters to popular generation tools
- Support both interactive and batch production workflows

---

*The production layer turns the skill library into a usable creative tool.*