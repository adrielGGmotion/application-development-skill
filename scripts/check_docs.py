#!/usr/bin/env python3
"""Check repository documentation without network access or dependencies.

Supports inline Markdown links and images with plain labels, relative targets,
angle-bracket targets, and optional quoted titles. Bare targets can contain
escaped characters or one level of parentheses. Reference links and deeply nested
labels/targets are outside this check's scope. URL fragments are not validated.
Fenced code, inline code spans, and HTML comments are excluded from link/ID checks.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


INLINE_LINK = re.compile(
    r"""
    (?<!\\)\[[^\]\n]*\]\(\s*
    (?:
        <(?P<angle>[^<>\n]*)>
        |
        (?P<bare>(?:\\.|[^\\\s()]|\([^()\n]*\))*)
    )
    \s*(?:(?:"[^"\n]*"|'[^'\n]*')\s*)?\)
    """,
    re.VERBOSE,
)
CHECKLIST_ID = re.compile(r"^[ \t]*-[ \t]+\[[ xX]\][ \t]+([A-Z]\d{2}\.\d{2})\b", re.MULTILINE)
FENCE_START = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
BACKTICKS = re.compile(r"(?<!`)`+(?!`)")
EXCLUDED_DIRS = {".git", ".venv", "venv", "node_modules", "build", "dist", "__pycache__"}


def blank(text: str) -> str:
    """Preserve offsets and line numbers while hiding non-content text."""
    return re.sub(r"[^\r\n]", " ", text)


def visible_markdown(text: str) -> str:
    lines: list[str] = []
    fence: tuple[str, int] | None = None
    for line in text.splitlines(keepends=True):
        content = line.rstrip("\r\n")
        if fence:
            lines.append(blank(line))
            character, length = fence
            if re.fullmatch(rf" {{0,3}}{re.escape(character)}{{{length},}}[ \t]*", content):
                fence = None
            continue
        match = FENCE_START.match(content)
        if match and not (match[1][0] == "`" and "`" in match[2]):
            fence = (match[1][0], len(match[1]))
            lines.append(blank(line))
        else:
            lines.append(line)

    visible = "".join(lines)
    position = 0
    while opening := BACKTICKS.search(visible, position):
        closing = re.compile(r"(?<!`)" + re.escape(opening[0]) + r"(?!`)").search(
            visible, opening.end()
        )
        if closing is None:
            position = opening.end()
            continue
        visible = (
            visible[: opening.start()]
            + blank(visible[opening.start() : closing.end()])
            + visible[closing.end() :]
        )
        position = closing.end()
    return re.sub(r"<!--[\s\S]*?-->", lambda match: blank(match[0]), visible)


def check(root: Path) -> tuple[list[str], int, int]:
    errors: list[str] = []
    documents: dict[Path, str] = {}
    paths: list[Path] = []
    for directory, subdirectories, filenames in os.walk(root):
        subdirectories[:] = [name for name in subdirectories if name not in EXCLUDED_DIRS]
        paths.extend(
            Path(directory) / name
            for name in filenames
            if Path(name).suffix.lower() in {".md", ".markdown"}
        )
    paths.sort()

    for path in paths:
        label = path.relative_to(root).as_posix()
        if not path.resolve().is_relative_to(root):
            errors.append(f"{label}: Markdown file resolves outside the repository")
            continue
        try:
            text = path.read_bytes().decode("utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"{label}: cannot read UTF-8 text: {error}")
            continue
        if text.startswith("\ufeff"):
            errors.append(f"{label}: remove the UTF-8 byte-order mark")
        if "\r" in text:
            errors.append(f"{label}: use LF line endings")
        if text and not text.endswith("\n"):
            errors.append(f"{label}: add a final newline")
        for number, line in enumerate(text.splitlines(), 1):
            if line.endswith((" ", "\t")):
                errors.append(f"{label}:{number}: remove trailing whitespace")

        visible = visible_markdown(text)
        documents[path] = visible
        for match in INLINE_LINK.finditer(visible):
            target = match["angle"] if match["angle"] is not None else match["bare"]
            target = re.sub(r"\\([\\`*{}\[\]()#+\-.!_<> ])", r"\1", target)
            location = f"{label}:{visible.count(chr(10), 0, match.start()) + 1}"
            try:
                url = urlsplit(target)
                if url.scheme == "file" or re.match(r"^[A-Za-z]:[\\/]", target):
                    errors.append(f"{location}: use a repository-relative link: {target}")
                    continue
                if url.scheme or url.netloc:
                    continue
                destination = unquote(url.path)
                if not destination:  # Fragment-only links refer to this document.
                    continue
                if Path(destination).is_absolute():
                    errors.append(f"{location}: use a repository-relative link: {target}")
                    continue
                resolved = (path.parent / destination).resolve()
                if not resolved.is_relative_to(root):
                    errors.append(f"{location}: link escapes the repository: {target}")
                elif not resolved.exists():
                    errors.append(f"{location}: local link target does not exist: {target}")
            except (OSError, ValueError) as error:
                errors.append(f"{location}: invalid link target {target!r}: {error}")

    inventory = root / "docs" / "scope-inventory.md"
    seen: dict[str, int] = {}
    if not inventory.is_file():
        errors.append("docs/scope-inventory.md: inventory is missing")
    elif inventory in documents:
        text = documents[inventory]
        for match in CHECKLIST_ID.finditer(text):
            identifier = match[1]
            number = text.count("\n", 0, match.start()) + 1
            if identifier in seen:
                errors.append(
                    f"docs/scope-inventory.md:{number}: duplicate checklist ID "
                    f"{identifier} (first appears on line {seen[identifier]})"
                )
            else:
                seen[identifier] = number
    return errors, len(paths), len(seen)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to this script's parent repository)",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"repository root is not a directory: {root}")
    errors, files, identifiers = check(root)
    if errors:
        print(f"Documentation check failed ({len(errors)} issues):", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1
    print(f"Checked {files} Markdown files and {identifiers} inventory IDs; no issues found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
