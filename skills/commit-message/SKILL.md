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

## Rules
1. Read the diff or staged files. Do not invent changes that are not there.
2. Subject: imperative mood, max 50 characters, format `(<type>) description` or `type(scope): description`.
3. Body (if needed): bullets with verbs, wrap at 72 characters; say what and why, not how.
4. Prefer business outcome wording. Technical wording only for mechanical changes (rename, deps).
5. No emojis, Unicode symbols, AI/tool mentions, or secrets (.env, credentials, keys).
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
