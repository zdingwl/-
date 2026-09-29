from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

errors: list[str] = []

required = [
    ROOT / "SKILL.md",
    ROOT / "VERSION",
    ROOT / "references" / "knowledge-map-120.md",
    ROOT / "references" / "knowledge-map-level2.md",
    ROOT / "references" / "adaptation-engine.md",
    ROOT / "references" / "source-ingestion.md",
    ROOT / "references" / "project-state-continuity.md",
    ROOT / "workflows" / "long-novel-to-screenplay.md",
    ROOT / "workflows" / "story-to-screenplay.md",
    ROOT / "templates" / "Source_Index_Template.md",
    ROOT / "templates" / "Adaptation_Matrix_Template.md",
    ROOT / "templates" / "Project_State_Template.md",
]

for path in required:
    if not path.exists():
        errors.append(f"missing required file: {path.relative_to(ROOT)}")

# A single Skill bundle must contain exactly one SKILL.md (case-insensitive).
skill_manifests = [
    p for p in ROOT.rglob("*")
    if p.is_file() and p.name.lower() == "skill.md"
]
if len(skill_manifests) != 1:
    errors.append(f"expected exactly one SKILL.md, found {len(skill_manifests)}")

skill = ROOT / "SKILL.md"
if skill.exists():
    text = skill.read_text(encoding="utf-8")

    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML front matter")

    front = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not front:
        errors.append("SKILL.md front matter is malformed")
    else:
        fm = front.group(1)
        if not re.search(r"^name:\s*screenplay-studio\s*$", fm, flags=re.M):
            errors.append("SKILL.md missing expected name")
        if not re.search(r"^description:\s*>", fm, flags=re.M):
            errors.append("SKILL.md missing folded description")

    # Check local paths explicitly referenced by SKILL.md.
    references = set(
        re.findall(
            r"(?:references|workflows|templates|docs|scripts)/"
            r"[A-Za-z0-9_.\-/]+",
            text,
        )
    )
    for ref in sorted(references):
        target = ROOT / ref.rstrip(".,;:)")
        if not target.exists():
            errors.append(f"SKILL.md references missing path: {ref}")

# Validate Level 2 coverage.
level2 = ROOT / "references" / "knowledge-level2"
expected_modules = [
    "01-premise-story-engine.md",
    "02-causality-theme.md",
    "03-character.md",
    "04-relationships-opposition.md",
    "05-structure.md",
    "06-scene.md",
    "07-visual-action.md",
    "08-dialogue.md",
    "09-information-suspense.md",
    "10-series-short-drama.md",
    "11-genre-medium.md",
    "12-adaptation-revision-format.md",
]

numbers: list[int] = []
for name in expected_modules:
    path = level2 / name
    if not path.exists():
        errors.append(f"missing Level 2 module: {name}")
        continue
    content = path.read_text(encoding="utf-8")
    numbers.extend(
        int(x) for x in re.findall(r"^## (\d+)\.", content, flags=re.M)
    )

if len(numbers) != 120:
    errors.append(f"Level 2 knowledge count must be 120, got {len(numbers)}")

if numbers and sorted(numbers) != list(range(1, 121)):
    errors.append("Level 2 numbering must contain every number from 1 to 120 exactly once")

# Check published bundle limits that can be validated statically.
all_files = [p for p in ROOT.rglob("*") if p.is_file()]
if len(all_files) > 500:
    errors.append(f"skill file count exceeds 500: {len(all_files)}")

max_file_size = 25 * 1024 * 1024
for path in all_files:
    if path.stat().st_size > max_file_size:
        errors.append(
            f"file exceeds 25 MB limit: {path.relative_to(ROOT)} "
            f"({path.stat().st_size} bytes)"
        )

if errors:
    print("screenplay-studio validation failed:")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("screenplay-studio validation passed")
print(f"- Skill manifests: {len(skill_manifests)}")
print(f"- Level 2 knowledge points: {len(numbers)}")
print(f"- Files: {len(all_files)}")
