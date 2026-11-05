# Security model

This hub is an index, not a package manager. That's a deliberate choice,
not a missing feature.

## What's reviewed before a listing is merged

A pull request adding an entry to `index.json` is checked for:
- valid JSON matching the schema in [README.md](./README.md),
- a unique `id` that isn't already listed,
- a `repo_url` that resolves to a public repo.

## What's *not* reviewed

Nobody on this project reads, audits, or sandboxes the code at a listed
`repo_url`. A listing being merged here is not a safety claim about the
plugin it points to — it means the *listing* is well-formed, nothing
more.

## Why installation is a manual copy, not a button

The sticky-claude dashboard shows this index but never fetches, builds,
or executes a plugin's code on its own. Installing one means a human
clones the repo into `backend/plugins/` and restarts the backend
themselves. A plugin that's installed runs with the same access the
backend process has — your Anthropic API key, and whatever your other
configured plugins can already do (writing calendar events, todos,
etc.) — so that step is a deliberate point for a person to look at what
they're about to run before it has any of that access.

If you maintain a plugin, say so in your own repo's README, and keep its
`LICENSE` and source visible — that's what lets someone reviewing it
before installing actually do so.

## Reporting a problem with a listed plugin

Open an issue on this repo naming the listing (not the plugin's own
repo, unless you're also the one who'd fix it there) and we'll remove the
entry while it's looked at. This repo can only ever remove a *listing* —
removing or fixing the plugin's actual code is up to its own
maintainer.
