#!/usr/bin/env python3
"""Schema/sanity checks for index.json, run in CI on every PR. This is not
a code review of any listed plugin -- see SECURITY.md -- it only makes
sure a submission is well-formed enough for the dashboard to render.
"""
import json
import re
import sys
from pathlib import Path

INDEX_PATH = Path(__file__).resolve().parent.parent / "index.json"
ID_PATTERN = re.compile(r"^[a-z0-9_-]+$")
REQUIRED_FIELDS = ("id", "name", "description", "author", "repo_url")
DISALLOWED_REPOS = (
    "github.com/biggy-spoon/sticky-claude",
    "github.com/biggy-spoon/sticky-claude-plugin-hub",
)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def main() -> None:
    try:
        raw = INDEX_PATH.read_text()
    except OSError as exc:
        fail(f"could not read {INDEX_PATH}: {exc}")
        return

    try:
        entries = json.loads(raw)
    except json.JSONDecodeError as exc:
        fail(f"index.json is not valid JSON: {exc}")
        return

    if not isinstance(entries, list):
        fail("index.json must contain a JSON array")
        return

    seen_ids: set[str] = set()
    for i, entry in enumerate(entries):
        where = f"entry {i}"
        if not isinstance(entry, dict):
            fail(f"{where}: must be an object")
            return

        where = f"entry {i} ({entry.get('id', '?')!r})"
        missing = [field for field in REQUIRED_FIELDS if not entry.get(field)]
        if missing:
            fail(f"{where}: missing required field(s): {', '.join(missing)}")
            return

        plugin_id = entry["id"]
        if not isinstance(plugin_id, str) or not ID_PATTERN.match(plugin_id):
            fail(f"{where}: id must match {ID_PATTERN.pattern!r}")
            return
        if plugin_id in seen_ids:
            fail(f"{where}: duplicate id")
            return
        seen_ids.add(plugin_id)

        repo_url = entry["repo_url"]
        if not isinstance(repo_url, str) or not repo_url.startswith("https://github.com/"):
            fail(f"{where}: repo_url must be an https://github.com/... URL")
            return
        if any(disallowed in repo_url for disallowed in DISALLOWED_REPOS):
            fail(f"{where}: repo_url can't point at this hub or the main sticky-claude repo")
            return

        tags = entry.get("tags")
        if tags is not None:
            if not isinstance(tags, list) or not all(isinstance(t, str) for t in tags):
                fail(f"{where}: tags must be an array of strings")
                return

    print(f"OK: {len(entries)} entr{'y' if len(entries) == 1 else 'ies'} validated")


if __name__ == "__main__":
    main()
