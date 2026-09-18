#!/usr/bin/env python3
"""Validate overseas short drama skill structure."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "CHANGELOG.md",
    "references/market-research.md",
    "references/output-templates.md",
    "evaluations/quality-check-cases.md",
]


def main():
    errors = []

    for file in REQUIRED_FILES:
        if not (ROOT / file).exists():
            errors.append(f"missing: {file}")

    references = list((ROOT / "references").glob("*.md"))
    evaluations = list((ROOT / "evaluations").glob("*.md"))

    if len(references) < 5:
        errors.append("reference coverage too low")

    if len(evaluations) < 1:
        errors.append("evaluation coverage missing")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if "version:" not in skill:
        errors.append("SKILL.md missing version metadata")

    if errors:
        print("FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
