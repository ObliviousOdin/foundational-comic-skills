from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")


def test_readme_surfaces_visual_showcase_assets():
    required = [
        "docs/assets/foundational-comic-skills-hero.svg",
        "docs/assets/comic-skill-stack-map.svg",
        "docs/assets/style-gallery-reel.svg",
        "docs/assets/setup-reinforce-turnaround-strip.svg",
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
        "## Style Gallery Reel",
        "## The Pattern, Performed",
    ]
    for section in required:
        assert section in README


def test_style_gallery_reel_credits_real_style_skills():
    referenced = [
        "comic-styles/western/golden-age-superhero-comic/SKILL.md",
        "comic-styles/asian/manhwa-color-webtoon/SKILL.md",
        "comic-styles/european/ligne-claire-franco-belge/SKILL.md",
        "comic-styles/manga/gekiga-cinematic-manga/SKILL.md",
        "comic-styles/sci-fi/cyberpunk-sci-fi-comic/SKILL.md",
        "comic-styles/decorative/watercolor-storybook-comic/SKILL.md",
    ]
    for rel in referenced:
        assert rel in README, f"README gallery table must link {rel}"
        assert (ROOT / rel).is_file(), f"linked style skill missing on disk: {rel}"


def test_showcase_assets_exist_and_are_svg():
    for rel in [
        "docs/assets/foundational-comic-skills-hero.svg",
        "docs/assets/comic-skill-stack-map.svg",
        "docs/assets/style-gallery-reel.svg",
        "docs/assets/setup-reinforce-turnaround-strip.svg",
    ]:
        path = ROOT / rel
        assert path.is_file(), f"missing {rel}"
        text = path.read_text(encoding="utf-8")
        assert "<svg" in text
        assert (
            "foundational-comic-skills" in text
            or "Comic Skill Stack" in text
            or "STYLE GALLERY REEL" in text
            or "SETUP" in text
        )


def test_animated_assets_are_wellformed_xml_and_motion_safe():
    import xml.etree.ElementTree as ET

    for rel in [
        "docs/assets/style-gallery-reel.svg",
        "docs/assets/setup-reinforce-turnaround-strip.svg",
    ]:
        path = ROOT / rel
        ET.parse(path)  # raises on malformed XML
        text = path.read_text(encoding="utf-8")
        assert "@keyframes" in text, f"{rel} should be animated"
        assert "prefers-reduced-motion" in text, f"{rel} must respect reduced motion"
