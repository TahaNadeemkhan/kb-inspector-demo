"""The format check every skills change must pass before a pull request is opened.

Each skills/<folder>/SKILL.md needs frontmatter with a `name` equal to its folder and a non-empty
`description`, and a body under 500 lines. No skill may contain a link: knowledge comes from the
platform's code and docs, and a link is the easiest thing for injected text to add.
"""

import re
import sys
from pathlib import Path

SKILLS = Path(__file__).resolve().parents[1] / "skills"
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK = re.compile(r"https?://|www\.", re.IGNORECASE)


def check(path: Path) -> list[str]:
    problems: list[str] = []
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not match:
        return [f"{path}: no frontmatter between --- lines"]
    front, body = match.groups()
    fields = dict(line.split(":", 1) for line in front.splitlines() if ":" in line)
    name = fields.get("name", "").strip()
    description = fields.get("description", "").strip()
    folder = path.parent.name
    if name != folder:
        problems.append(f"{path}: name {name!r} does not match folder {folder!r}")
    if not NAME.match(name) or len(name) > 64:
        problems.append(f"{path}: name {name!r} is not lowercase-with-hyphens, max 64")
    if not description or len(description) > 1024:
        problems.append(f"{path}: description is empty or over 1024 characters")
    if len(body.splitlines()) > 500:
        problems.append(f"{path}: body is over 500 lines")
    if LINK.search(text):
        problems.append(f"{path}: contains a link")
    return problems


def main() -> int:
    files = sorted(SKILLS.glob("*/SKILL.md"))
    if not files:
        print("no skills found")
        return 1
    problems = [p for f in files for p in check(f)]
    for problem in problems:
        print(problem)
    print(f"{len(files)} skills checked, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
