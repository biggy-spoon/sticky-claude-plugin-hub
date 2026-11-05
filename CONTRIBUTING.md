# Contributing a plugin listing

This repo only holds `index.json` — a list of pointers to plugin repos.
Your plugin's code lives in *your own* repo, published however you like
(a solo repo, a fork of the
[plugin template](https://github.com/biggy-spoon/sticky-claude/blob/master/backend/plugins/base.py)
as a starting point, whatever).

## Before you submit

1. **Write the plugin.** It needs to implement the `Plugin` contract in
   [`backend/plugins/base.py`](https://github.com/biggy-spoon/sticky-claude/blob/master/backend/plugins/base.py)
   of the main `sticky-claude` repo. `calendar_plugin.py` (settings +
   an external service) and `todo_plugin.py` (no settings, pure local
   state) are the two reference implementations — pick whichever is
   closer to your plugin's shape.
2. **Publish it in its own public repo**, with:
   - a `LICENSE` file (any OSI-approved license is fine),
   - a short README that at minimum states what the plugin does and
     confirms the one-line install (`git clone <your repo>
     backend/plugins/<id>`, restart),
   - the plugin's `.py` file(s) at the repo root (that's what gets
     cloned straight into `backend/plugins/<id>/`).
3. Pick an `id` (lowercase, `a-z0-9_-` only) that matches your plugin
   class's `Plugin.id` property exactly — this is what `backend/plugins/`
   discovery keys off of, and what the hub suggests as the clone-target
   directory name.

## Submitting the listing

1. Fork this repo.
2. Add one entry to `index.json`, keeping the array sorted by `id`. See
   [README.md](./README.md) for the field schema. Keep `description` to
   one plain sentence.
3. Open a PR. CI checks that `index.json` is still valid JSON, every
   entry has the required fields, `id`s are unique and match the slug
   pattern, and `repo_url` points at a (reachable, public) GitHub repo.
4. A maintainer merges once CI passes and the entry looks sane (right
   schema, plausible description, `repo_url` isn't this hub repo itself
   or the main sticky-claude repo). This is a schema/sanity check, not a
   code review — see [SECURITY.md](./SECURITY.md) for what that does and
   doesn't mean.

## Updating or removing your listing

Same process — a PR editing or deleting your entry. If your plugin repo
moves or you stop maintaining it, please open that PR yourself rather
than leaving a stale pointer.
