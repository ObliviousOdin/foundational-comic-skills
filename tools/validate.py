#!/usr/bin/env python3
"""Repository validator for foundational-comic-skills.

Modes
-----
  python3 tools/validate.py                     whole repository
  python3 tools/validate.py --style <SKILL.md>  one style, while authoring
  python3 tools/validate.py --bible <bible>     one world-bible YAML

Exit code 0 = contracts hold; 1 = violations found.

Checks
------
1. Frontmatter: every SKILL.md has name/version/category/description;
   name matches its directory; version is semver.
2. Aphorism: every SKILL.md ends with a closing italic line.
3. Style Schema v2: every comic-styles/*/*/SKILL.md has the required
   sections in order with minimum content (see CONTRIBUTING.md), and its
   Prompt Block fits the 40-90 word injectable budget and stays a pure
   declarative style description (no pronouns, imperatives, or story).
4. Style index sync: comic-styles/SKILL.md table rows match the
   directory tree exactly (presence, category, declared count), the
   index habitat column agrees with each skill's Integration line, no
   two styles inject near-identical Prompt Blocks, every native-habitat
   name resolves against the core libraries, and every sanctioned
   format and pattern is claimed by at least one style.
5. Cross-references: backticked `comic-*` tokens resolve to a real
   skill or the planned-skills allowlist, and every `When Not to Use`
   redirect names a style that exists.
6. YAML health: all template/example YAML files and fenced ```yaml
   blocks inside SKILL.md files parse.
"""

from __future__ import annotations

import itertools
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
PROMPT_BLOCK_RE = re.compile(r"## Prompt Block\s*\n+```text\n(.*?)\n```", re.DOTALL)
WHEN_NOT_RE = re.compile(r"## When Not to Use\n(.*?)\n## ", re.DOTALL)
INTEGRATION_RE = re.compile(r"## Integration\n(.*?)(?:\n---|\Z)", re.DOTALL)
BACKTICK_RE = re.compile(r"`([^`]+)`")
LIB_ENTRY_RE = re.compile(r"^### \d+\. `([a-z0-9-]+)`", re.MULTILINE)

# Canvases and beat arcs are defined once, in the core libraries. Native
# habitat vocabulary is read from them rather than restated here, so the
# check cannot drift from the thing it validates.
LIBRARY_PATHS = (
    "comic-core/comic-format-library/SKILL.md",
    "comic-core/comic-narrative-patterns/SKILL.md",
)

# The Prompt Block is injected verbatim into a generation prompt alongside
# character, scene, and negative blocks. Too short starves the backend of
# style signal; too long crowds the blocks that carry identity and staging.
PROMPT_BLOCK_MIN_WORDS = 40
PROMPT_BLOCK_MAX_WORDS = 90

# Two styles whose fragments overlap this far are the same style wearing
# two names. Measured against the corpus, the closest legitimately adjacent
# pair (golden-age vs. silver-age superhero) sits at 0.27, so this leaves
# wide headroom for real neighbours while catching copy-paste authorship.
PROMPT_BLOCK_COLLISION_RATIO = 0.60

# A Prompt Block is a pure declarative style description. Anything that
# addresses a reader, commands a model, or carries story content is an
# injection surface once the block is concatenated into a live prompt.
PROMPT_BLOCK_FORBIDDEN = [
    (
        r"\b(?:i|me|my|mine|we|us|our|ours|you|your|yours)\b",
        "first- or second-person pronoun — the block describes rendering, "
        "it never addresses anyone",
    ),
    (
        r"\b(?:he|him|his|she|her|hers|they|them|their|theirs)\b",
        "third-person pronoun — identity belongs to the character block, "
        "never the style block",
    ),
    (
        r"\b(?:ignore|disregard|override|forget|instead|actually|must|should|"
        r"shall|please|ensure|remember|do not|don't|never|always|make sure)\b",
        "imperative or instruction verb — style is declared, not commanded",
    ),
    (
        r"\b(?:system prompt|instruction|instructions|assistant|as an ai|"
        r"this prompt|previous|prior)\b",
        "meta-instruction token — a style fragment must not reference the "
        "prompt it lives in",
    ),
    (
        r"\b(?:named|protagonist|antagonist|villain|storyline|plot|backstory|"
        r"subplot|scene where|dialogue that)\b",
        "story or character content — the Story Harness section owns this",
    ),
    (
        r"[\"“”]",
        "quoted literal — lettering copy belongs in the shot plan, "
        "never baked into a reusable style fragment",
    ),
]

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return str(p)  # --style/--bible accept paths from outside the tree


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
    # Routing sections: one bullet cannot express a choice between styles.
    for section in ("## When to Use", "## When Not to Use"):
        if bullet_count(section) < 2:
            err(
                f"{rel(path)}: `{section.lstrip('# ')}` needs >= 2 bullets — "
                f"a single line cannot route a Producer between styles"
            )
    if "```text" not in section_body("## Prompt Block"):
        err(f"{rel(path)}: Prompt Block needs a fenced ```text block")
    else:
        check_prompt_block_budget(path, text)
        check_prompt_block_purity(path, text)
    if len(re.findall(r"^- \[ \]", section_body("## Style Quality Gates"), re.MULTILINE)) < 3:
        err(f"{rel(path)}: Style Quality Gates needs >= 3 checkboxes")


def prompt_block(text: str) -> str | None:
    """The fenced ```text payload of a style's Prompt Block, or None."""
    m = PROMPT_BLOCK_RE.search(text)
    return m.group(1) if m else None


def check_prompt_block_budget(path: Path, text: str) -> None:
    body = prompt_block(text)
    if body is None:
        err(f"{rel(path)}: Prompt Block fence is malformed (expected ```text … ```)")
        return
    words = len(body.split())
    if words < PROMPT_BLOCK_MIN_WORDS:
        err(
            f"{rel(path)}: Prompt Block is {words} words, under the "
            f"{PROMPT_BLOCK_MIN_WORDS}-word floor — too thin to hold the style "
            f"against a backend's defaults"
        )
    elif words > PROMPT_BLOCK_MAX_WORDS:
        err(
            f"{rel(path)}: Prompt Block is {words} words, over the "
            f"{PROMPT_BLOCK_MAX_WORDS}-word ceiling — it will crowd out the "
            f"character, scene, and negative blocks it ships beside"
        )


def check_prompt_block_purity(path: Path, text: str) -> None:
    """Keep injectable style fragments free of instructions and story."""
    body = prompt_block(text)
    if body is None:
        return
    for pattern, reason in PROMPT_BLOCK_FORBIDDEN:
        m = re.search(pattern, body, re.IGNORECASE)
        if m:
            err(
                f"{rel(path)}: Prompt Block contains {m.group(0)!r} — "
                f"{reason}"
            )


def library_vocabulary() -> set[str]:
    """Sanctioned format and pattern names, read from the core libraries."""
    vocab: set[str] = set()
    for rel_path in LIBRARY_PATHS:
        path = ROOT / rel_path
        if path.is_file():
            vocab |= set(LIB_ENTRY_RE.findall(path.read_text(encoding="utf-8")))
    return vocab


def check_library_coverage(style_texts: dict[Path, str]) -> None:
    """Every sanctioned format and pattern must be claimed by some style.

    Resolving habitat names catches a style pointing at nothing. This
    catches the opposite and rarer failure: a library entry nothing points
    at. `2x2-grid-page` sat fully specified, pipelined, and unclaimed by
    all 30 styles, so the Producer's routing table answered "which style
    suits this format?" with silence.
    """
    vocab = library_vocabulary()
    if not vocab:
        return  # library unreadable; check_native_habitats already warned

    claimed: set[str] = set()
    for text in style_texts.values():
        m = INTEGRATION_RE.search(text)
        if m:
            claimed |= set(BACKTICK_RE.findall(m.group(1)))

    for entry in sorted(vocab - claimed):
        err(
            f"comic-core: `{entry}` is sanctioned in the core libraries but no "
            f"style claims it as native habitat — a format or pattern nothing "
            f"points at cannot be routed to"
        )


def check_index_habitats(style_texts: dict[Path, str]) -> None:
    """The index's habitat column must agree with each skill's Integration line.

    The column is the Producer's routing table — it is read to pick a style
    for a locked format. Two descriptions of one fact drift apart unless
    something holds them together, and the skill is the authority.
    """
    index_path = ROOT / "comic-styles" / "SKILL.md"
    if not index_path.is_file():
        return
    index = index_path.read_text(encoding="utf-8")

    integration: dict[str, set[str]] = {}
    for path, text in style_texts.items():
        m = INTEGRATION_RE.search(text)
        integration[path.parent.name] = set(BACKTICK_RE.findall(m.group(1))) if m else set()

    vocab = library_vocabulary()
    rows = re.findall(
        r"^\| [A-Za-z -]+ \| `([a-z0-9-]+)` \| ([^|]*) \|", index, re.MULTILINE
    )
    for skill, cell in rows:
        if skill not in integration:
            continue  # missing-directory case is reported by check_style_index
        for token in sorted(set(BACKTICK_RE.findall(cell))):
            if token not in vocab:
                err(
                    f"comic-styles/SKILL.md: `{skill}` habitat names `{token}`, "
                    f"which is neither a sanctioned format nor a pattern"
                )
            elif token not in integration[skill]:
                err(
                    f"comic-styles/SKILL.md: `{skill}` habitat names `{token}`, "
                    f"which its own Integration line does not list — the skill "
                    f"is the authority, the index follows it"
                )


def check_native_habitats(style_texts: dict[Path, str]) -> None:
    """A style's Integration line must route to canvases that exist.

    "Native habitat" tells the Producer which format and pattern a style
    is strongest in, so an unrecognised name routes a project to a canvas
    the pipelines cannot build.
    """
    vocab = library_vocabulary()
    if not vocab:
        warn("core libraries unreadable - skipping native-habitat checks")
        return
    for path, text in sorted(style_texts.items()):
        m = INTEGRATION_RE.search(text)
        if not m:
            continue
        for token in sorted(set(BACKTICK_RE.findall(m.group(1)))):
            # `comic-*` skills are resolved by the cross-reference pass.
            if token.startswith("comic-") or token in vocab:
                continue
            err(
                f"{rel(path)}: Integration names native habitat `{token}`, "
                f"which is neither a format in comic-format-library nor a "
                f"pattern in comic-narrative-patterns"
            )


def check_prompt_block_collisions(style_texts: dict[Path, str]) -> None:
    """No two styles may inject near-identical fragments.

    The Prompt Block is the only part of a style skill the backend ever
    sees. Two styles that resolve to the same fragment render the same
    way, so the Producer's one-style-per-project lock stops meaning
    anything and the style index promises a distinction it cannot keep.
    """
    vocab: list[tuple[Path, set[str]]] = []
    for path, text in sorted(style_texts.items()):
        body = prompt_block(text)
        if body:
            vocab.append((path, set(re.findall(r"[a-z0-9]+", body.lower()))))

    for (path_a, words_a), (path_b, words_b) in itertools.combinations(vocab, 2):
        union = words_a | words_b
        if not union:
            continue
        ratio = len(words_a & words_b) / len(union)
        if ratio >= PROMPT_BLOCK_COLLISION_RATIO:
            err(
                f"{rel(path_a)}: Prompt Block shares {ratio:.0%} of its "
                f"vocabulary with {rel(path_b)} — two styles that inject "
                f"near-identical fragments collapse into one visual grammar"
            )


def check_style_redirects(
    style_texts: dict[Path, str], style_names: set[str], known: set[str]
) -> None:
    """`When Not to Use` must name a style that exists.

    Schema v2 defines the section as honest mismatches plus the style to
    use instead. A redirect is a routing instruction an agent follows, so
    a typo sends it nowhere: `REF_RE` only covers `comic-*` tokens, and
    style names do not carry that prefix.
    """
    allowed = style_names | PLANNED_SKILLS
    for path, text in sorted(style_texts.items()):
        m = WHEN_NOT_RE.search(text)
        if not m:
            continue  # a missing section is already reported by the schema check
        for token in sorted(set(BACKTICK_RE.findall(m.group(1)))):
            if token in allowed:
                continue
            if token in known:
                err(
                    f"{rel(path)}: `When Not to Use` redirects to `{token}`, "
                    f"which is a skill but not a style — the section names the "
                    f"style to use instead"
                )
            else:
                err(
                    f"{rel(path)}: `When Not to Use` redirects to `{token}`, "
                    f"which resolves to no skill in this repository"
                )


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


def validate_bible(path: Path) -> list[str]:
    """Validate a world-bible YAML against comic-world-bible-system rules.

    Implements the structural/content checks from the skill's Validate
    section. Returns a list of violations (empty = valid).
    """
    problems: list[str] = []
    if not HAVE_YAML:
        return ["pyyaml required for bible validation"]
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return [f"invalid YAML - {exc}"]
    if not isinstance(data, dict):
        return ["bible must be a YAML mapping"]

    required = (
        "visual_grammar", "character_compendium",
        "world_register", "negative_library", "version_history",
    )
    for section in required:
        if section not in data:
            problems.append(f"missing top-level section `{section}`")

    grammar = data.get("visual_grammar") or {}
    for rule in ("linework_rules", "lighting_grammar"):
        if not grammar.get(rule):
            problems.append(f"visual_grammar.{rule} is required")

    characters = data.get("character_compendium") or []
    if not characters:
        problems.append("character_compendium needs >= 1 character")
    names: list[str] = []
    for ch in characters:
        label = ch.get("name", "<unnamed>")
        names.append(label)
        if not ch.get("dna_template"):
            problems.append(f"character `{label}` missing dna_template")
        if not ch.get("canonical_reference_sheet"):
            problems.append(f"character `{label}` missing canonical_reference_sheet")
    if len(names) != len(set(names)):
        problems.append("duplicate character names in compendium")

    negatives = data.get("negative_library") or {}
    if not negatives.get("project_wide_negatives"):
        problems.append("negative_library.project_wide_negatives is empty")

    history = data.get("version_history") or []
    if not history:
        problems.append("version_history needs >= 1 entry")
    elif not all(entry.get("rationale") for entry in history):
        problems.append("every version_history entry needs a rationale")

    problems.extend(check_provenance(data, characters))
    return problems


def check_provenance(data: dict, characters: list) -> list[str]:
    """Nonfiction bibles must be able to show their work.

    A nonfiction style locks out fabricated documentary detail; that lock
    only means something if the project holds a register of what is
    actually sourced. Fiction bibles omit `production_mode` entirely and
    never reach this check.
    """
    if str(data.get("production_mode", "fiction")).lower() != "nonfiction":
        return []

    problems: list[str] = []
    register = data.get("source_register") or []
    if not register:
        problems.append(
            "production_mode is nonfiction but source_register is empty — "
            "every depicted fact must trace to a source"
        )
    for i, entry in enumerate(register, 1):
        if not isinstance(entry, dict):
            problems.append(f"source_register entry #{i} must be a mapping")
            continue
        for field in ("claim", "source", "depicted_in"):
            if not entry.get(field):
                problems.append(f"source_register entry #{i} missing `{field}`")

    for ch in characters:
        if isinstance(ch, dict) and not ch.get("source_note"):
            problems.append(
                f"character `{ch.get('name', '<unnamed>')}` missing source_note "
                f"(required in a nonfiction bible)"
            )
    return problems


def check_example_bibles() -> None:
    for path in sorted(ROOT.glob("examples/**/world-bible*.yaml")):
        for problem in validate_bible(path):
            err(f"{rel(path)}: {problem}")


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


def report(summary: str, clean_message: str) -> int:
    """Print the accumulated findings and return the process exit code.

    Violations are grouped under the file that owns them. A flat list
    across 56 skills forces the reader to re-sort it by hand before they
    can fix anything, and one broken file usually raises several.
    """
    print(summary)
    for w in warnings:
        print(f"  WARN  {w}")
    if not errors:
        print(clean_message)
        return 0

    grouped: dict[str, list[str]] = {}
    for e in errors:
        path, sep, detail = e.partition(": ")
        grouped.setdefault(path if sep else "(repository)", []).append(detail or e)
    for path in sorted(grouped):
        print(f"\n  {path}")
        for detail in grouped[path]:
            print(f"    FAIL  {detail}")
    print(f"\n{len(errors)} violation(s) across {len(grouped)} file(s).")
    return 1


def check_one_style(path: Path) -> int:
    """Validate a single style file — the authoring loop.

    Runs every check that can be answered from one file plus the tree it
    sits in, so an author gets a verdict in milliseconds instead of
    re-validating 56 skills after each edit. Whole-corpus checks (index
    sync, Prompt Block collisions) still need the full run.
    """
    if not path.is_file():
        err(f"{rel(path)}: no such file")
        return report(f"Checked {rel(path)}.", "Style contract holds.")

    warn(
        "single-file mode — index sync and Prompt Block collision checks need "
        "the whole corpus; run `python3 tools/validate.py` before committing"
    )
    text = path.read_text(encoding="utf-8")
    check_frontmatter_and_aphorism(path, text)
    check_style_schema(path, text)
    check_style_redirects(
        {path: text},
        {p.parent.name for p in ROOT.glob("comic-styles/*/*/SKILL.md")},
        {p.parent.name for p in skill_files()},
    )
    check_native_habitats({path: text})
    return report(f"Checked {rel(path)}.", "Style contract holds.")


def main() -> int:
    if len(sys.argv) == 3 and sys.argv[1] == "--style":
        return check_one_style(Path(sys.argv[2]).resolve())

    if len(sys.argv) == 3 and sys.argv[1] == "--bible":
        path = Path(sys.argv[2]).resolve()
        problems = validate_bible(path)
        if problems:
            for p in problems:
                print(f"  FAIL  {p}")
            print(f"\n{len(problems)} violation(s).")
            return 1
        print(f"{path.name}: valid world bible.")
        return 0

    known_skills: set[str] = set()
    style_dirs: dict[str, str] = {}
    style_texts: dict[Path, str] = {}

    for path in skill_files():
        text = path.read_text(encoding="utf-8")
        name = check_frontmatter_and_aphorism(path, text)
        if name:
            known_skills.add(name)
        parts = path.relative_to(ROOT).parts
        if parts[0] == "comic-styles" and len(parts) == 4:
            style_dirs[parts[2]] = parts[1]
            style_texts[path] = text
            check_style_schema(path, text)
            if parts[1] not in STYLE_CATEGORY_NAMES:
                err(f"{rel(path)}: unknown style category folder `{parts[1]}`")

    check_style_index(style_dirs)
    check_style_redirects(style_texts, set(style_dirs), known_skills)
    check_native_habitats(style_texts)
    check_index_habitats(style_texts)
    check_library_coverage(style_texts)
    check_prompt_block_collisions(style_texts)
    check_cross_references(known_skills)
    check_yaml_health()
    check_example_bibles()

    return report(
        f"Checked {len(skill_files())} skills ({len(style_dirs)} styles).",
        "All repository contracts hold.",
    )


if __name__ == "__main__":
    sys.exit(main())
