---
name: commit-message
description: >-
  Write a conventional commit message from a diff or staged changes.
  Use when the user asks to make a commit, write a commit message, or commit
  and push. Do not use for push-only or unrelated git questions.
license: MIT
allowed-tools: Bash
---

# Commit message

## Steps
1. Read the diff or staged files. Do not invent changes that are not there.
2. Subject: imperative mood, max 50 characters, format `(<type>) description` or `type(scope): description`.
3. Body (if needed): blank line after subject; bullets with verbs; wrap at 72; what and why, not how.
4. Prefer business outcome where it fits (preference, not hard rule). Technical wording for rename or dependencies.
5. Forbidden: emojis or decorative Unicode; AI/tool mentions (Claude, Copilot, Cursor, "Generated with…", `Co-Authored-By: Claude`); secrets (`.env`, credentials, keys, tokens).
6. Reference an issue when applicable (for example `Closes #42`).
7. Project-specific conventions override these rules.

## Types
- `feat` - new feature
- `fix` - bug fix
- `refactor` - restructure with no behavior change
- `test` - add or update tests
- `docs` - documentation only
- `chore` - maintenance, dependencies, cosmetics

## Example

```
(feat) Add customer review moderation
- Introduce ReviewModerator service
- Scan /reviews with moderation rules
- Store status for the admin panel
Closes #42
```
