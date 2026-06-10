#!/usr/bin/env python3
"""Repository validator for foundational-comic-skills.

Run from anywhere:  python3 tools/validate.py
Exit code 0 = repository contracts hold; 1 = violations found.

Checks
------
1. Frontmatter: every SKILL.md has name/version/category/description;
   name matches its directory; version is semver.
2. Aphorism: every SKILL.md ends with a closing italic line.
3. Style Schema v2: every comic-styles/*/*/SKILL.md has the required
   sections in order with minimum content (see CONTRIBUTING.md).
4. Style index sync: comic-styles/SKILL.md table rows match the
   directory tree exactly (presence, category, declared count).
5. Cross-references: backticked `comic-*` tokens resolve to a real
   skill or the planned-skills allowlist.
6. YAML health: all template/example YAML files and fenced ```yaml
   blocks inside SKILL.md files parse.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
    HAVE_YAML = True
except ImportError:  # pragma: no cover - degraded mode
    HAVE_YAML = False

ROOT = Path(__file__).resolve().parent.parent

# Skills that may be referenced but intentionally do not exist yet.
# Keep this list short; every entry must appear as `Planned` in a layer index.
PLANNED_SKILLS = {
    "comic-hermes-registration",
    "comic-cli-adapter",
    "comic-higgsfield-adapter",
    "comic-remotion-adapter",
    "comic-emotional-arc-tracking",
}

# Non-skill backticked comic-* vocabulary (formats, patterns, files).
NON_SKILL_TOKENS = {
    "comic-strip",
}

STYLE_CATEGORY_NAMES = {
    "adventure": "Adventure",
    "asian": "Asian",
    "cartoon": "Cartoon",
    "decorative": "Decorative",
    "european": "European",
    "horror": "Horror",
    "literary": "Literary",
    "manga": "Manga",
    "noir": "Noir",
    "pop-art": "Pop Art",
    "sci-fi": "Sci-Fi",
    "western": "Western",
}

STYLE_SECTIONS_IN_ORDER = [
    "**Style Lock (do not deviate)**",
    "## Negative Locks",
    "## When to Use",
    "## When Not to Use",
    "## Story Harness (Image-Driven)",
    "## World Guardrail",
    "## Dialogue & Lettering",
    "## Direction Notes",
    "## Consistency Notes",
    "## Prompt Block",
    "## Style Quality Gates",
    "## Integration",
]

SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
REF_RE = re.compile(r"`(comic-[a-z0-9-]+)`")

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        err(f"{rel(path)}: missing YAML frontmatter block")
        return {}
    fields: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t", "#")):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def skill_files() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("SKILL.md")
        if ".git" not in p.parts
    )


def check_frontmatter_and_aphorism(path: Path, text: str) -> str | None:
    """Returns the skill name if valid."""
    fields = parse_frontmatter(text, path)
    name = fields.get("name")
    for field in ("name", "version", "category", "description"):
        if not fields.get(field):
            err(f"{rel(path)}: frontmatter missing `{field}`")
    if fields.get("version") and not SEMVER_RE.match(fields["version"]):
        err(f"{rel(path)}: version `{fields['version']}` is not semver")
    expected = path.parent.name
    if name and name != expected:
        err(f"{rel(path)}: frontmatter name `{name}` != directory `{expected}`")

    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if not lines or not re.match(r"^\*[^*].*[^*]\*$", lines[-1]):
        err(f"{rel(path)}: must end with a closing italic aphorism line")
    return name


def check_style_schema(path: Path, text: str) -> None:
    fields = parse_frontmatter(text, path)
    if fields.get("category") != "comic-styles":
        err(f"{rel(path)}: style skill category must be `comic-styles`")

    pos = 0
    for section in STYLE_SECTIONS_IN_ORDER:
        idx = text.find(section, pos)
        if idx == -1:
            if section in text:
                err(f"{rel(path)}: section `{section}` is out of order")
            else:
                err(f"{rel(path)}: missing required section `{section}`")
            continue
        pos = idx

    def section_body(header: str) -> str:
        start = text.find(header)
        if start == -1:
            return ""
        start += len(header)
        nxt = re.search(r"\n(## |\*\*Style Lock|---\n)", text[start:])
        return text[start:start + nxt.start()] if nxt else text[start:]

    def bullet_count(header: str) -> int:
        return len(re.findall(r"^- ", section_body(header), re.MULTILINE))

    if bullet_count("**Style Lock (do not deviate)**") < 5:
        err(f"{rel(path)}: Style Lock needs >= 5 bullets")
    if bullet_count("## Negative Locks") < 3:
        err(f"{rel(path)}: Negative Locks needs >= 3 bullets")
    if "```text" not in section_body("## Prompt Block"):
        err(f"{rel(path)}: Prompt Block needs a fenced ```text block")
    if len(re.findall(r"^- \[ \]", section_body("## Style Quality Gates"), re.MULTILINE)) < 3:
        err(f"{rel(path)}: Style Quality Gates needs >= 3 checkboxes")


def check_style_index(style_dirs: dict[str, str]) -> None:
    """style_dirs: skill-name -> category folder."""
    index_path = ROOT / "comic-styles" / "SKILL.md"
    text = index_path.read_text(encoding="utf-8")

    m = re.search(r"## Current Skills \((\d+)\)", text)
    if not m:
        err(f"{rel(index_path)}: heading `## Current Skills (N)` not found")
        declared = -1
    else:
        declared = int(m.group(1))
    if declared not in (-1, len(style_dirs)):
        err(
            f"{rel(index_path)}: declares {declared} skills, "
            f"directory tree has {len(style_dirs)}"
        )

    rows: dict[str, str] = {}
    for cat, skill in re.findall(r"^\| ([A-Za-z -]+) \| `([a-z0-9-]+)` \|", text, re.MULTILINE):
        rows[skill] = cat.strip()

    for skill, folder in sorted(style_dirs.items()):
        expected_cat = STYLE_CATEGORY_NAMES.get(folder, folder.title())
        if skill not in rows:
            err(f"{rel(index_path)}: missing index row for `{skill}`")
        elif rows[skill] != expected_cat:
            err(
                f"{rel(index_path)}: `{skill}` listed under "
                f"`{rows[skill]}`, folder says `{expected_cat}`"
            )
    for skill in rows:
        if skill not in style_dirs:
            err(f"{rel(index_path)}: index row `{skill}` has no directory")


def check_cross_references(known: set[str]) -> None:
    allowed = known | PLANNED_SKILLS | NON_SKILL_TOKENS
    skip_parts = {".git", "research", "skills"}
    for path in sorted(ROOT.rglob("*.md")):
        if skip_parts & set(path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        for token in sorted(set(REF_RE.findall(text))):
            if token not in allowed:
                err(f"{rel(path)}: reference `{token}` does not resolve to any skill")


def check_yaml_health() -> None:
    if not HAVE_YAML:
        warn("pyyaml not installed - skipping YAML checks (pip install pyyaml)")
        return
    yaml_files = [
        p for p in list(ROOT.rglob("assets/templates/*.yaml")) + list(ROOT.rglob("examples/**/*.yaml"))
        if ".git" not in p.parts
    ]
    for path in sorted(set(yaml_files)):
        try:
            yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            err(f"{rel(path)}: invalid YAML - {exc}")
    for path in skill_files():
        text = path.read_text(encoding="utf-8")
        for i, block in enumerate(re.findall(r"```yaml\n(.*?)```", text, re.DOTALL), 1):
            try:
                yaml.safe_load(block)
            except yaml.YAMLError as exc:
                err(f"{rel(path)}: fenced yaml block #{i} invalid - {exc}")


def main() -> int:
    known_skills: set[str] = set()
    style_dirs: dict[str, str] = {}

    for path in skill_files():
        text = path.read_text(encoding="utf-8")
        name = check_frontmatter_and_aphorism(path, text)
        if name:
            known_skills.add(name)
        parts = path.relative_to(ROOT).parts
        if parts[0] == "comic-styles" and len(parts) == 4:
            style_dirs[parts[2]] = parts[1]
            check_style_schema(path, text)
            if parts[1] not in STYLE_CATEGORY_NAMES:
                err(f"{rel(path)}: unknown style category folder `{parts[1]}`")

    check_style_index(style_dirs)
    check_cross_references(known_skills)
    check_yaml_health()

    print(f"Checked {len(skill_files())} skills ({len(style_dirs)} styles).")
    for w in warnings:
        print(f"  WARN  {w}")
    if errors:
        for e in errors:
            print(f"  FAIL  {e}")
        print(f"\n{len(errors)} violation(s).")
        return 1
    print("All repository contracts hold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
