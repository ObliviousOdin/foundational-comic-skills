from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")


def test_readme_surfaces_visual_showcase_assets():
    required = [
        "docs/assets/foundational-comic-skills-hero.svg",
        "docs/assets/comic-skill-stack-map.svg",
        "docs/showcase/README.md",
    ]
    for marker in required:
        assert marker in README


def test_readme_has_operator_quickstart_and_outcomes():
    required = [
        "## Make a Comic in 10 Minutes",
        "## What You Can Build",
        "## Choose Your Path",
        "## Visual System Map",
    ]
    for section in required:
        assert section in README


def test_showcase_assets_exist_and_are_svg():
    for rel in [
        "docs/assets/foundational-comic-skills-hero.svg",
        "docs/assets/comic-skill-stack-map.svg",
    ]:
        path = ROOT / rel
        assert path.is_file(), f"missing {rel}"
        text = path.read_text(encoding="utf-8")
        assert "<svg" in text
        assert "foundational-comic-skills" in text or "Comic Skill Stack" in text
