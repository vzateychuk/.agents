---
name: handoff
description: >-
  Handoff / session transfer: write a thorough handoff document so another
  agent can continue the work without losing context. Use only when the user
  asks for handoff, session transfer, or to prepare work for the next agent.
  Do not use for ordinary summaries.
argument-hint: "What will the next session be used for?"
---

# Handoff

Write a handoff document so a fresh agent can continue the work seamlessly.

## Priority
Transfer what lives only in this conversation and cannot be rediscovered from the repo: intent, agreements, constraints, decisions, rejected approaches, and open threads. Do not dump repository state the next agent can rebuild with read-only checks (`git status`, `git log`, `git diff`). The goal is context from the chat, not instructions or command lists.

## Output
- Save to the temporary directory of the user's operating system, not the workspace. Use a unique file name with date/time and a short slug so parallel handoffs never overwrite each other.
- Write in the language the user used in the conversation.
- Final reply to the user MUST contain: (1) the exact absolute file path, (2) a short summary, (3) a ready-to-paste start prompt for the next agent.

## Rules
- Completeness over brevity for chat-only context: include everything the next agent would otherwise miss or have to ask about. Prefer bullet points over prose; avoid filler.
- Never drop decisions, constraints, dead ends, or the next step for the sake of shortness.
- Do not duplicate content from persistent artifacts (requirements, plans, ADRs, issues, commits). Reference them by path or URL.
- Do not restate rediscoverable repo facts (branch, commit, full status). Mention working state only when it is non-obvious or chat-specific: in-flight leftovers, temporary changes that must be reverted, debug instrumentation, log locations, running services that matter to the next step.
- Mark anything inferred rather than stated in the conversation as `[Assumption]`.
- Redact secrets: API keys, tokens (including in URLs), passwords, `.env` contents, connection strings, personally identifiable information. Replace with `[REDACTED]`.
- In "Suggested skills", list names only, taken from the available skills list. Do not open or read other skill files. Write `none` if nothing applies.

## Document sections
1. **Next step (TL;DR):** one line with the exact immediate action for the new agent.
2. **Goal of next session:** if the user passed arguments, treat them as the focus. Otherwise infer from open work and label `[Assumption]`.
3. **User constraints & preferences:** explicit rules, style preferences, bans, agreements from this conversation (e.g. "do not touch file X"). This is the highest-priority section after the next step.
4. **Done so far:** key facts from the conversation. EVERY bullet ends with `[verified]` (executed/tested; briefly say how) or `[unverified]` (assumed/untested).
5. **Decisions & rejected approaches:** accepted solutions with reasons; abandoned paths, dead ends, mistakes to avoid — as discussed in chat.
6. **Open work & blockers:** prioritized list; item 1 must match the Next step.
7. **Non-obvious working state (only if needed):** leftovers the next agent would not notice from a normal repo scan (debug instrumentation, temporary edits to revert, relevant running processes, log paths). Omit this section if empty.
8. **Key paths / URLs:** files changed or to be changed in this work, plus persistent artifacts (requirements, plans, ADRs, issues). Exclude unrelated scratch files.
9. **Suggested skills:** names only.
