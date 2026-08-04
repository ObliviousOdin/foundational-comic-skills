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


# --- Arc ledger -----------------------------------------------------------


def arc_ledger(project: Path) -> dict | None:
    path = project / "arc-ledger.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8")) if path.is_file() else None


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_arc_ledger_steps_prove_their_exit_states(project):
    """A recorded exit state without a proof panel is tracking by vibes."""
    ledger = arc_ledger(project)
    if ledger is None:
        pytest.skip(f"{project.name} carries no arc ledger")

    for line in ledger["throughlines"]:
        for step in line.get("steps") or []:
            if not step.get("exit_actual"):
                continue  # not yet delivered
            assert step.get("proof_panel"), (
                f"{project.name}: {line['character']} episode {step['episode']} "
                f"records exit_actual `{step['exit_actual']}` with no proof_panel — "
                f"the orchestrator requires a panel reference, not vibes"
            )


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_arc_ledger_records_debt_when_a_target_is_missed(project):
    """A miss is a continuity debt the next episode owes; silence is drift."""
    ledger = arc_ledger(project)
    if ledger is None:
        pytest.skip(f"{project.name} carries no arc ledger")

    for line in ledger["throughlines"]:
        for step in line.get("steps") or []:
            actual, target = step.get("exit_actual"), step.get("exit_target")
            if not actual or actual == target:
                continue
            assert step.get("debt"), (
                f"{project.name}: {line['character']} episode {step['episode']} "
                f"exited at `{actual}` against a target of `{target}` and records "
                f"no debt — an unrecorded miss is how an arc drifts silently"
            )


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_arc_ledger_states_exist_in_the_bible(project):
    """States must reference the world bible's expression library."""
    ledger = arc_ledger(project)
    if ledger is None:
        pytest.skip(f"{project.name} carries no arc ledger")

    known: set[str] = set()
    for bible in EXAMPLES.glob("**/world-bible*.yaml"):
        for entry in yaml.safe_load(bible.read_text(encoding="utf-8"))["character_compendium"]:
            known |= set(entry.get("expression_library") or [])

    for line in ledger["throughlines"]:
        for field in ("baseline_state", "destination_state"):
            assert line[field] in known, (
                f"{project.name}: {line['character']} {field} `{line[field]}` is not "
                f"in any world bible expression library"
            )


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_arc_ledger_moves_one_step_per_episode(project):
    """An episode moves each character at most one step; jumps are finales."""
    ledger = arc_ledger(project)
    if ledger is None:
        pytest.skip(f"{project.name} carries no arc ledger")

    for line in ledger["throughlines"]:
        episodes = [s["episode"] for s in line.get("steps") or []]
        assert len(episodes) == len(set(episodes)), (
            f"{project.name}: {line['character']} has more than one step in a "
            f"single episode — the orchestrator caps it at one"
        )


# --- Chapter map page grammar --------------------------------------------


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_chapter_pages_alternate_recto_and_verso(project):
    """Page turns only work if sides alternate; the turn is the instrument."""
    path = project / "chapter-map.yaml"
    if not path.is_file():
        pytest.skip(f"{project.name} is not a chapter project")

    pages = yaml.safe_load(path.read_text(encoding="utf-8"))["page_grammar"]
    for entry in pages:
        expected = "recto" if entry["page"] % 2 else "verso"
        assert entry["side"] == expected, (
            f"{project.name}: page {entry['page']} is marked {entry['side']}; "
            f"with page 1 on the recto, odd pages are recto and even are verso"
        )


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_chapter_page_grammar_matches_the_scene_list(project):
    """Every page belongs to exactly one scene, and every scene page is planned."""
    path = project / "chapter-map.yaml"
    if not path.is_file():
        pytest.skip(f"{project.name} is not a chapter project")

    chapter_map = yaml.safe_load(path.read_text(encoding="utf-8"))
    scene_pages = {p for s in chapter_map["scenes"] for p in s["pages"]}
    grammar_pages = {e["page"] for e in chapter_map["page_grammar"]}
    assert scene_pages == grammar_pages, (
        f"{project.name}: scenes cover pages {sorted(scene_pages)} but page "
        f"grammar covers {sorted(grammar_pages)}"
    )
    assert grammar_pages == set(range(1, chapter_map["chapter"]["page_count"] + 1)), (
        f"{project.name}: page grammar does not cover 1..{chapter_map['chapter']['page_count']}"
    )


@pytest.mark.parametrize("project", example_dirs(), ids=lambda p: p.name)
def test_chapter_panel_counts_sit_inside_the_format_range(project):
    """comic-format-library sets 4-9 panels per chapter page; a splash is 1."""
    path = project / "chapter-map.yaml"
    if not path.is_file():
        pytest.skip(f"{project.name} is not a chapter project")

    chapter_map = yaml.safe_load(path.read_text(encoding="utf-8"))
    splash_page = (chapter_map.get("climax") or {}).get("page")
    for entry in chapter_map["page_grammar"]:
        count = entry["panel_count"]
        if entry["page"] == splash_page and (chapter_map["climax"] or {}).get("splash"):
            assert count == 1, (
                f"{project.name}: page {entry['page']} is the designated splash "
                f"but declares {count} panels"
            )
            continue
        assert 1 <= count <= 9, (
            f"{project.name}: page {entry['page']} declares {count} panels; "
            f"the format library allows 4-9 (1 only for the designated splash)"
        )


def test_world_bibles_in_examples_validate():
    bibles = sorted(EXAMPLES.glob("**/world-bible*.yaml"))
    assert bibles, "at least one example must carry a canonical world bible"
    for path in bibles:
        assert validate.validate_bible(path) == [], f"{path.name} failed validation"
