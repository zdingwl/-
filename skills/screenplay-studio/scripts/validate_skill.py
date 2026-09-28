from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

required = [
    ROOT / "SKILL.md",
    ROOT / "VERSION",
    ROOT / "references" / "knowledge-map-120.md",
    ROOT / "references" / "knowledge-map-level2.md",
    ROOT / "references" / "adaptation-engine.md",
    ROOT / "references" / "source-ingestion.md",
    ROOT / "workflows" / "long-novel-to-screenplay.md",
    ROOT / "workflows" / "story-to-screenplay.md",
    ROOT / "templates" / "Source_Index_Template.md",
    ROOT / "templates" / "Adaptation_Matrix_Template.md",
    ROOT / "templates" / "Project_State_Template.md",
]

errors = []

for path in required:
    if not path.exists():
        errors.append(f"missing required file: {path.relative_to(ROOT)}")

skill = ROOT / "SKILL.md"
if skill.exists():
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML front matter")
    if "name: screenplay-studio" not in text:
        errors.append("SKILL.md missing expected name")
    if "description:" not in text:
        errors.append("SKILL.md missing description")

level2 = ROOT / "references" / "knowledge-level2"
expected = [
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

count = 0
numbers = []
for name in expected:
    path = level2 / name
    if not path.exists():
        errors.append(f"missing Level 2 module: {name}")
        continue
    content = path.read_text(encoding="utf-8")
    found = [int(x) for x in re.findall(r"^## (\d+)\.", content, flags=re.M)]
    count += len(found)
    numbers.extend(found)

if count != 120:
    errors.append(f"Level 2 knowledge count must be 120, got {count}")

if numbers and sorted(numbers) != list(range(1, 121)):
    errors.append("Level 2 numbering must contain every number from 1 to 120 exactly once")

if errors:
    print("screenplay-studio validation failed:")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("screenplay-studio validation passed")
print(f"- Level 2 knowledge points: {count}")
