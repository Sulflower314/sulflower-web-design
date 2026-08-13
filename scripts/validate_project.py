#!/usr/bin/env python3
"""Validate the publishable repository and installable skill with stdlib only."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "sulflower-web-design"
EXPECTED_NAME = "sulflower-web-design"
EXPECTED_VERSION = "2.0.0"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_layout() -> None:
    required = [
        ROOT / "README.md",
        ROOT / "README.en.md",
        ROOT / "LICENSE",
        ROOT / "NOTICE.md",
        ROOT / "CONTRIBUTING.md",
        SKILL / "SKILL.md",
        SKILL / "manifest.json",
        SKILL / "agents" / "openai.yaml",
        SKILL / "references" / "design-foundations.md",
        SKILL / "references" / "workflow-modes.md",
        SKILL / "references" / "quality-assurance.md",
        SKILL / "references" / "style-recipes" / "INDEX.md",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        fail("Missing required files: " + ", ".join(missing))


def validate_frontmatter() -> None:
    content = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        fail("SKILL.md has no valid YAML frontmatter block")
    frontmatter = match.group(1)
    name = re.search(r"^name:\s*([^\n]+)$", frontmatter, re.MULTILINE)
    description = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    if not name or name.group(1).strip().strip('"\'') != EXPECTED_NAME:
        fail(f"SKILL.md name must be {EXPECTED_NAME}")
    if not description or len(description.group(1).strip().strip('"\'')) < 80:
        fail("SKILL.md description is missing or too short")


def validate_manifest() -> None:
    manifest = json.loads((SKILL / "manifest.json").read_text(encoding="utf-8"))
    expected = {
        "name": EXPECTED_NAME,
        "version": EXPECTED_VERSION,
        "author": "Sulflower",
        "license": "MIT",
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            fail(f"manifest.json {key!r} must be {value!r}")


def validate_interface() -> None:
    content = (SKILL / "agents" / "openai.yaml").read_text(encoding="utf-8")
    if 'display_name: "Sulflower Web Design"' not in content:
        fail("agents/openai.yaml has the wrong display name")
    if "$sulflower-web-design" not in content:
        fail("agents/openai.yaml default prompt does not invoke the renamed skill")


def validate_skill_references() -> None:
    content = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    references = sorted(set(re.findall(r"`(references/[^`<>]+\.md)`", content)))
    missing = [reference for reference in references if not (SKILL / reference).is_file()]
    if missing:
        fail("Broken SKILL.md references: " + ", ".join(missing))


def validate_repository_links() -> None:
    for source in ROOT.rglob("*.md"):
        content = source.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
            if "://" in target or target.startswith("#"):
                continue
            path = (source.parent / target.split("#", 1)[0]).resolve()
            if not path.exists():
                fail(f"Broken link in {source.relative_to(ROOT)}: {target}")


def validate_publish_safety() -> None:
    local_windows = re.compile(r"[A-Za-z]:" + re.escape("\\") + r"Users" + re.escape("\\"), re.IGNORECASE)
    local_unix = re.compile(r"/(?:Users|home)/[^\s/]+/")
    email = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
    private_key = re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY")
    violations: list[str] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if not path.is_file() or path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".gif", ".zip"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if local_windows.search(text) or local_unix.search(text) or email.search(text) or private_key.search(text):
            violations.append(str(path.relative_to(ROOT)))
    if violations:
        fail("Potential personal or secret material in: " + ", ".join(violations))


def main() -> None:
    validate_layout()
    validate_frontmatter()
    validate_manifest()
    validate_interface()
    validate_skill_references()
    validate_repository_links()
    validate_publish_safety()
    print(f"Repository and skill are valid: {EXPECTED_NAME} {EXPECTED_VERSION}")


if __name__ == "__main__":
    main()
