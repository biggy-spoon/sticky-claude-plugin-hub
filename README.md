# sticky-claude-plugin-hub

A community-maintained index of third-party plugins for
[sticky-claude](https://github.com/biggy-spoon/sticky-claude), a
push-to-talk voice assistant for the Seeed Studio reTerminal Sticky.

This repo is **metadata only** — a flat JSON list of plugins, where to
find each one's source, and a short description. It doesn't host any
plugin code itself, and the sticky-claude backend never fetches or runs
code from here automatically. The dashboard's "Plugin hub" card reads
`index.json` to show what's available; installing one is still a manual
step (see below), by design — see [SECURITY.md](./SECURITY.md).

## For users: installing a plugin from the hub

1. Open your dashboard's Plugin hub card, or browse `index.json` below,
   and pick a plugin.
2. **Read its source before installing it.** This hub only checks that a
   submission is well-formed (see [CONTRIBUTING.md](./CONTRIBUTING.md));
   nobody reviews plugin code for safety, and a plugin runs with the same
   access your backend has — including your Anthropic API key and
   whatever each configured plugin can already do (calendar writes,
   todos, etc.).
3. Clone it into your backend's `plugins/` directory:
   ```
   git clone <repo_url> backend/plugins/<id>
   ```
4. Restart the backend. `backend/plugins/__init__.py` auto-discovers any
   `Plugin` subclass in every `.py` file under `plugins/`, so there's
   nothing else to wire up.

## `index.json` schema

```json
[
  {
    "id": "weather",
    "name": "Weather",
    "description": "Ask for the current forecast by voice.",
    "author": "octocat",
    "repo_url": "https://github.com/octocat/sticky-claude-plugin-weather",
    "tags": ["weather"]
  }
]
```

| field         | required | notes                                                                 |
|---------------|----------|------------------------------------------------------------------------|
| `id`          | yes      | lowercase, `a-z0-9_-` only. Must match the plugin's `Plugin.id` and is what the dashboard suggests as the clone-target directory name under `backend/plugins/`. |
| `name`        | yes      | short human-readable name.                                            |
| `description` | yes      | one sentence, no markdown.                                            |
| `author`      | yes      | your GitHub username or org.                                          |
| `repo_url`    | yes      | the plugin's own public repo (not a fork of this one).                |
| `tags`        | no       | array of short lowercase strings, for future filtering.               |

## For plugin authors: publishing one

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the submission process, and
the main repo's
[`backend/plugins/base.py`](https://github.com/biggy-spoon/sticky-claude/blob/master/backend/plugins/base.py)
for the `Plugin` contract your code needs to implement.
`calendar_plugin.py` and `todo_plugin.py` in that same directory are the
two reference implementations.

## License

MIT, see [LICENSE](./LICENSE). That covers this repo's own
files (`index.json`, docs, CI) — it says nothing about the license of any
plugin listed in `index.json`, which is up to that plugin's own repo.
