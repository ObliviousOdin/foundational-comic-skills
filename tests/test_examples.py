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
    """The Director works inside the Producer's contract, not beside it."""
    brief_path, plan_path = project / "production-brief.yaml", project / "shot-plan.yaml"
    if not (brief_path.is_file() and plan_path.is_file()):
        pytest.skip(f"{project.name} does not carry both artifacts")

    contract = yaml.safe_load(brief_path.read_text(encoding="utf-8"))["contract"]
    plan = yaml.safe_load(plan_path.read_text(encoding="utf-8"))["shot_plan"]
    for field in ("format", "narrative_pattern"):
        assert plan[field] == contract[field], (
            f"{project.name}: shot plan {field} `{plan[field]}` contradicts the "
            f"contract's `{contract[field]}`"
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
