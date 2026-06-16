---
name: repo-map
description: Use and maintain repo_map.md as the primary AI-agnostic project index. Read it when present, detect when it is missing or stale, and ask before creating or updating it.
---

# Repo Map Skill

`repo_map.md` is the primary AI-agnostic navigation index for a project.

Use this skill to decide how to read, trust, create, or update that index.
Do not inline the full generation or update workflow here.

## Behavior

When working in a project:

1. If `repo_map.md` exists in the project root, read it before broad exploration.
2. Treat `repo_map.md` as a navigation index, not as absolute truth.
3. If code evidence contradicts `repo_map.md`, trust the code.
4. Do not silently create or update `repo_map.md`.
5. If `repo_map.md` is missing, tell the user that the primary AI-agnostic project index is missing and offer to run `prompts/init.repo_map.md`.
6. If `repo_map.md` appears stale, tell the user why and offer to run `prompts/update.repo_map.md`.
7. Continue normal code exploration only when the current task can proceed safely without creating or updating the index.

## Staleness Signals

`repo_map.md` may be stale when changes affect:

- project structure;
- modules;
- entrypoints;
- commands/scripts;
- runtime config;
- environment variables;
- API surface;
- data entities;
- dependencies;
- conventions.

## Confirmation Policy

Never create or update `repo_map.md` silently.

Before editing `repo_map.md`, ask the user for confirmation.

Use this form:

```text
repo_map.md may be stale because <reason>. Do you want me to update it using prompts/update.repo_map.md?
```

For a missing index, use this form:

```text
repo_map.md is missing. Do you want me to create it using prompts/init.repo_map.md?
```

## Delegation

Creation is handled by:

```text
prompts/init.repo_map.md
```

Update is handled by:

```text
prompts/update.repo_map.md
```

Do not duplicate the generation or update algorithms in this skill.
