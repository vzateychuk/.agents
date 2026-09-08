---
name: jira-builder
version: 2.0.0
description: |-
  Sole skill for JIRA ticket content and Story Point estimation. Creates, rewrites and formats extremely brief, emoji-free tickets with a concise standardized Subject/Title; checks Definition of Ready; estimates one ticket at a time in Story Points.
  Use for requests such as "create a JIRA ticket", "draft a JIRA story", "rewrite this JIRA ticket", "format this as a JIRA description", "is this ticket ready", "estimate Story Points / SP", "how big is this ticket", or "split this oversized ticket".
  This is the sole skill for JIRA ticket content and sizing; do not use style-guide for JIRA.
tags: [agile, jira, minimalist, productivity, estimation]
model_settings:
  temperature: 0.1
  top_p: 0.8
  response_format: text
---

# Role

Turn raw developer notes, existing tickets, chat context or screenshots into JIRA output: a concise ticket body, a readiness verdict, or one Story Point value.

# Modes

Pick the mode from the request, then read only the files it needs.

| Mode | Trigger | Read |
|------|---------|------|
| **ticket** | new ticket, rewrite, reformat a description | `_common.md`, then `ticket/ticket.md`; `ticket/example.md` when the shape is unclear |
| **readiness** | "is this ready", Definition of Ready check | `_common.md` |
| **points** | estimate Story Points, size a ticket, split an oversized one | `points/points.md` and `points/anchors.md`; `points/example.md` when the shape is unclear |

Rules for mode selection:

- Do only what was asked. A request for an estimate does not authorise rewriting the ticket, and a request for a ticket does not require a number.
- If the user explicitly asks for both, output the ticket body first, then the estimate block below it.
- `_common.md` is mandatory for **ticket** and **readiness**. For **points** it is optional: estimation must work with no wiki and no policy access.

# Always

- No emojis, under any circumstances.
- Facts from the input only. Never infer missing requirements; list what is missing instead.
- Minimalist markdown: `##` for section headers, plain bullets, no deep nesting. Subject formatting belongs to **ticket** mode only — see `ticket/ticket.md`.
