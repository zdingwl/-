from __future__ import annotations

import argparse
from pathlib import Path
import zipfile

SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parents[1]
VERSION_FILE = SKILL_ROOT / "VERSION"

EXCLUDED_NAMES = {
    ".DS_Store",
}

EXCLUDED_PARTS = {
    "__pycache__",
    ".git",
}


def iter_files():
    for path in sorted(SKILL_ROOT.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(SKILL_ROOT)
        if path.name in EXCLUDED_NAMES:
            continue
        if any(part in EXCLUDED_PARTS for part in rel.parts):
            continue
        if path.suffix == ".pyc":
            continue
        yield path, rel


def build_zip(output: Path) -> Path:
    output.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for source, rel in iter_files():
            arcname = Path("screenplay-studio") / rel
            info = zipfile.ZipInfo(str(arcname).replace("\\", "/"))
            # Stable timestamp for deterministic archives.
            info.date_time = (1980, 1, 1, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zf.writestr(info, source.read_bytes())

    return output


def main() -> None:
    version = VERSION_FILE.read_text(encoding="utf-8").strip()
    default_output = REPO_ROOT / "dist" / f"screenplay-studio-{version}.zip"

    parser = argparse.ArgumentParser(description="Package screenplay-studio as a single Skill bundle.")
    parser.add_argument("--output", type=Path, default=default_output)
    args = parser.parse_args()

    output = build_zip(args.output.resolve())
    print(output)


if __name__ == "__main__":
    main()
