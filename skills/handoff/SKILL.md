---
name: handoff
description: >-
  Handoff / session transfer: write a handoff document so another agent can
  continue. Use only when the user asks for handoff, session transfer, or to
  prepare work for the next agent. Do not use for ordinary summaries.
argument-hint: "What will the next session be used for?"
---

# Handoff

Write a handoff document so a fresh agent can continue the work. Save it to the temporary directory of the user's operating system - not the current workspace.

## Rules
- If the user passed arguments, treat them as the focus of the next session and tailor the document.
- Do not duplicate content already in other artifacts (product requirements, plans, architecture decision records, issues, commits, diffs). Reference them by path or URL.
- Redact secrets: API keys, passwords, personally identifiable information.
- In "suggested skills", list skill names only. Do not open or read other skill files for this handoff.

## Document sections
1. Goal of the next session
2. Done so far (facts from this conversation)
3. Open work and blockers
4. Key paths / URLs
5. Suggested skills (names only)
