"""Contract tests for the worked projects under examples/.

Examples are the repository's proof that the layers connect. A stale
example is worse than a missing one: it demonstrates a workflow nobody
can run, using a style or format that may no longer exist.
"""

import importlib.util
import re
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"

_spec = importlib.util.spec_from_file_location(
    "comic_validate", ROOT / "tools" / "validate.py"
)
validate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(validate)


def example_dirs() -> list[Path]:
    return sorted(p for p in EXAMPLES.iterdir() if p.is_dir())


def test_examples_exist():
    assert example_dirs(), "examples/ must hold at least one worked project"


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_every_project_narrates_itself(project):
    assert (project / "WALKTHROUGH.md").is_file(), (
        f"{project.name} needs a WALKTHROUGH.md — artifacts without narration "
        f"show what was produced but never why"
    )


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_every_project_is_listed_in_the_index(project):
    index = (EXAMPLES / "README.md").read_text(encoding="utf-8")
    assert f"`{project.name}/`" in index, (
        f"{project.name} is missing a row in examples/README.md"
    )


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_every_project_yaml_parses(project):
    files = sorted(project.glob("*.yaml"))
    assert files, f"{project.name} has no YAML artifacts"
    for path in files:
        yaml.safe_load(path.read_text(encoding="utf-8"))


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_every_project_contract_names_things_that_exist(project):
    """A brief routes to a format, a pattern, and a style. All three must be real."""
    brief_path = project / "production-brief.yaml"
    if not brief_path.is_file():
        pytest.skip(f"{project.name} carries no production brief")

    contract = yaml.safe_load(brief_path.read_text(encoding="utf-8"))["contract"]
    vocabulary = validate.library_vocabulary()
    styles = {p.parent.name for p in ROOT.glob("comic-styles/*/*/SKILL.md")}

    assert contract["format"] in vocabulary, (
        f"{project.name} contracts format `{contract['format']}`, "
        f"which comic-format-library does not define"
    )
    assert contract["narrative_pattern"] in vocabulary, (
        f"{project.name} contracts pattern `{contract['narrative_pattern']}`, "
        f"which comic-narrative-patterns does not define"
    )
    assert contract["style_skill"] in styles, (
        f"{project.name} contracts style `{contract['style_skill']}`, "
        f"which has no directory under comic-styles/"
    )


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_shot_plan_agrees_with_the_brief(project):
    """The Director works inside the Producer's contract, not beside it.

    Format must always match. Pattern is format-dependent: most formats lock
    one pattern per project, but `multi-page-chapter` assigns a pattern per
    scene, so a page plan legitimately differs from the contract's spine and
    is checked against the chapter map instead.
    """
    brief_path = project / "production-brief.yaml"
    plans = sorted(project.glob("shot-plan*.yaml"))
    if not (brief_path.is_file() and plans):
        pytest.skip(f"{project.name} does not carry both artifacts")

    contract = yaml.safe_load(brief_path.read_text(encoding="utf-8"))["contract"]
    scene_patterns = chapter_scene_patterns(project)

    for plan_path in plans:
        plan = yaml.safe_load(plan_path.read_text(encoding="utf-8"))["shot_plan"]
        assert plan["format"] == contract["format"], (
            f"{project.name}/{plan_path.name}: shot plan format `{plan['format']}` "
            f"contradicts the contract's `{contract['format']}`"
        )

        pattern = plan["narrative_pattern"]
        if contract["format"] == "multi-page-chapter":
            assert scene_patterns, (
                f"{project.name}: a chapter must carry a chapter-map.yaml — the "
                f"pipeline requires it before any page is planned"
            )
            assert pattern in scene_patterns, (
                f"{project.name}/{plan_path.name}: page pattern `{pattern}` is not "
                f"assigned to any scene in the chapter map {sorted(scene_patterns)}"
            )
        else:
            assert pattern == contract["narrative_pattern"], (
                f"{project.name}/{plan_path.name}: shot plan pattern `{pattern}` "
                f"contradicts the contract's `{contract['narrative_pattern']}`"
            )


def chapter_scene_patterns(project: Path) -> set[str]:
    """Patterns the chapter map assigns across scenes, empty if not a chapter."""
    path = project / "chapter-map.yaml"
    if not path.is_file():
        return set()
    scenes = yaml.safe_load(path.read_text(encoding="utf-8")).get("scenes") or []
    return {s["narrative_pattern"] for s in scenes if s.get("narrative_pattern")}


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_chapter_map_patterns_resolve(project):
    """Every pattern a chapter map assigns must exist in the pattern library."""
    patterns = chapter_scene_patterns(project)
    if not patterns:
        pytest.skip(f"{project.name} is not a chapter project")
    vocabulary = validate.library_vocabulary()
    for pattern in sorted(patterns):
        assert pattern in vocabulary, (
            f"{project.name}: chapter map assigns `{pattern}`, which "
            f"comic-narrative-patterns does not define"
        )


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_chapter_grants_at_most_one_splash(project):
    """The pipeline caps a chapter at one splash, granted only by the map."""
    path = project / "chapter-map.yaml"
    if not path.is_file():
        pytest.skip(f"{project.name} is not a chapter project")
    chapter_map = yaml.safe_load(path.read_text(encoding="utf-8"))
    climax = chapter_map.get("climax") or {}
    if climax.get("splash"):
        assert climax.get("justification"), (
            f"{project.name}: the chapter map grants a splash with no justification"
        )


# Blocks 1-7 of the assembly contract, in order. CONSISTENCY ANCHORS (6) is a
# backend-dialect section and does not appear in every worked prompt, so the
# check enforces relative order rather than presence of all seven.
CANONICAL_BLOCKS = [
    "STYLE",
    "FORMAT",
    "CHARACTER",
    "PANEL",
    "SCENE",
    "NEGATIVE",
]


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_assembled_prompt_follows_canonical_block_order(project):
    """Layer 0 checks this before a render is paid for; the examples must model it."""
    path = project / "assembled-prompt.md"
    if not path.is_file():
        pytest.skip(f"{project.name} carries no assembled prompt")

    text = path.read_text(encoding="utf-8")
    # Only bracketed block headers at line start, inside the fenced prompt.
    found = re.findall(r"^\[([A-Z][A-Z ]*)", text, re.MULTILINE)
    assert found, f"{project.name}: no [BLOCK] headers found in the assembled prompt"

    seen = [b for b in found if b.split()[0] in CANONICAL_BLOCKS]
    order = [CANONICAL_BLOCKS.index(b.split()[0]) for b in seen]
    assert order == sorted(order), (
        f"{project.name}: assembled prompt blocks are out of canonical order — "
        f"got {seen}. comic-image-generation-adapter fixes this order so two "
        f"panels never differ because their prompts were organized differently"
    )


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_assembled_prompt_opens_with_the_style_block(project):
    """Style lock is block 1 and is never truncated by the budget rule."""
    path = project / "assembled-prompt.md"
    if not path.is_file():
        pytest.skip(f"{project.name} carries no assembled prompt")
    found = re.findall(r"^\[([A-Z][A-Z ]*)", path.read_text(encoding="utf-8"), re.MULTILINE)
    assert found[0].strip() == "STYLE", (
        f"{project.name}: assembled prompt opens with [{found[0].strip()}], not [STYLE]"
    )


def test_world_bibles_in_examples_validate():
    bibles = sorted(EXAMPLES.glob("**/world-bible*.yaml"))
    assert bibles, "at least one example must carry a canonical world bible"
    for path in bibles:
        assert validate.validate_bible(path) == [], f"{path.name} failed validation"
