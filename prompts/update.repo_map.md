# Task: Update repo_map.md

Update the existing `repo_map.md` project index without performing a full rescan unless the user explicitly asks for one.

`repo_map.md` is the primary AI-agnostic navigation index for the project. Keep it compact, evidence-based, and optimized for future agents.

---

# Preconditions

Before editing:

1. Confirm that the user asked to update `repo_map.md` or approved the update.
2. Read the current `repo_map.md`.
3. Identify which sections may be stale.
4. Read only the files needed to verify those sections.

If `repo_map.md` is missing, stop and use `prompts/init.repo_map.md` instead.

---

# Update Scope

Prefer incremental updates. Do not rewrite the whole file unless the existing index is structurally unusable.

Update sections affected by changes to:

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

---

# Evidence Rules

- Every changed value must come from actual file reads.
- Do not infer versions, commands, routes, entities, or environment variables.
- If evidence is unclear, write `unknown` or leave the previous confirmed value unchanged with a note only when necessary.
- Never record secret values. For environment variables, record key names and purpose only.
- Respect `rules/scan-ignore.md` and the project `.gitignore`.

---

# Minimal Verification Checklist

Use the checklist selectively according to the stale sections:

| Section | Verify from |
|---|---|
| PROJECT | build manifests, config files |
| COMMANDS | manifest scripts/tasks |
| STRUCTURE | directory tree, depth 2 |
| RUNTIME | Dockerfile, docker-compose, version files |
| ENTRYPOINTS | startup/bootstrap files |
| MODULES | directory structure and module files |
| KEY_FILES | entrypoints, config, schema, manifests |
| DEPENDENCIES | build/package manifests |
| ENV_CONFIG | env templates and env variable usage |
| API_SURFACE | routers/controllers/handlers |
| DATA_ENTITIES | models/entities/schemas/types |
| CONVENTIONS | linter/formatter/test configs |

---

# Output Rules

- Preserve the existing `repo_map.md` format where possible.
- Keep tables compact.
- Descriptions should be 10 words or fewer.
- Keep tree depth at 2 unless the existing map already uses a justified deeper path.
- Do not list individual files except in `KEY_FILES`.
- Remove obsolete rows only after verifying they are obsolete.
- Add new rows only after verifying them from files.

---

# Final Response

After updating, summarize:

1. which sections changed;
2. which files were read as evidence;
3. any sections intentionally left unchanged.
