#!/usr/bin/env python3
"""Read-only validation for WorkFn SKILL.md YAML front matter."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


CATEGORIES = (
    "00_skill_orchestration",
    "01_customer_communication",
    "02_rfq_and_quotation",
    "03_order_and_delivery",
    "04_complaint_and_aftersales",
    "05_customer_management",
    "06_internal_collaboration",
    "07_personal_productivity",
    "08_platform_specific",
    "09_product_intelligence",
    "10_market_intelligence",
)

NAME_PATTERN = re.compile(r"^zayn-[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(path: Path) -> tuple[str | None, str | None, list[str]]:
    issues: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return None, None, [f"cannot read as UTF-8: {exc}"]

    if not text.startswith("---"):
        return None, None, ["file does not start with ---"]
    if not (text.startswith("---\n") or text.startswith("---\r\n")):
        issues.append("content appears before or on the opening delimiter")

    lines = text.splitlines()
    closing_indexes = [i for i, line in enumerate(lines[1:], start=1) if line == "---"]
    if not closing_indexes:
        return None, None, issues + ["YAML front matter is not closed"]

    closing = closing_indexes[0]
    yaml_lines = lines[1:closing]
    yaml_text = "\n".join(yaml_lines)

    name_match = re.search(r"(?m)^name:\s*(\S+)\s*$", yaml_text)
    description_match = re.search(r"(?m)^description:\s*(.+?)\s*$", yaml_text)
    name = name_match.group(1).strip() if name_match else None
    description = description_match.group(1).strip() if description_match else None

    if not name:
        issues.append("missing name")
    else:
        if not name.startswith("zayn-"):
            issues.append("name does not start with zayn-")
        if name != name.lower():
            issues.append("name is not lowercase")
        if "_" in name:
            issues.append("name contains underscore")
        if not NAME_PATTERN.fullmatch(name):
            issues.append("name contains invalid characters or separators")

    if not description:
        issues.append("missing or empty description")
    else:
        if "#" in description:
            issues.append("description contains Markdown heading marker")
        if "\n" in description:
            issues.append("description is not one line")

    remaining = "\n".join(lines[closing + 1 :])
    if re.search(r"(?m)^---\s*\nname:\s*", remaining):
        issues.append("multiple YAML front matter blocks")

    return name, description, issues


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    files: list[Path] = []
    for category in CATEGORIES:
        category_root = project_root / category
        if category_root.exists():
            files.extend(category_root.rglob("SKILL.md"))

    files = sorted(set(files))
    results: list[tuple[Path, str | None, str | None, list[str]]] = []
    names: list[str] = []

    for path in files:
        name, description, issues = parse_frontmatter(path)
        results.append((path, name, description, issues))
        if name:
            names.append(name)

    duplicate_names = {name for name, count in Counter(names).items() if count > 1}
    if duplicate_names:
        for index, (path, name, description, issues) in enumerate(results):
            if name in duplicate_names:
                results[index] = (path, name, description, issues + ["duplicate name"])

    failed = [(path, issues) for path, _, _, issues in results if issues]

    print(f"Scanned: {len(files)}")
    print(f"Valid: {len(files) - len(failed)}")
    print(f"Invalid: {len(failed)}")
    print(f"Unique names: {len(set(names))}")
    print(f"Duplicate names: {len(duplicate_names)}")
    print(f"Missing descriptions: {sum(1 for _, _, desc, _ in results if not desc)}")

    for path, issues in failed:
        relative = path.relative_to(project_root)
        print(f"FAIL {relative}: {'; '.join(issues)}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
