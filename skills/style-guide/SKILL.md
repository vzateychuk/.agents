---
name: style-guide
description: |-
  Applies the brand writing style to emails, messenger messages, technical documentation, support content, and Jira tickets.
  Triggers on user requests to "rewrite", "edit", "polish", "format", "improve tone", "check tone", "make it more friendly", "make it more formal", "apply the style guide", "what are the rules for emails/messenger/techdocs/support/jira", "how should I write a runbook", "how to write a support reply", "convert this to a tech doc", "rewrite this Jira ticket", "format this as a Jira description", or "draft a Jira story".
  Always writes in English, no emojis, prefers bullet points over tables.
---

# Style Guide

## Purpose
Apply the correct writing style for the requested content type based on a shared set of rules and examples.

## Triggers
- "rewrite this email"
- "edit this message"
- "polish this draft"
- "format this text"
- "improve the tone"
- "check the tone"
- "make it more friendly"
- "make it more formal"
- "apply the style guide"
- "what are the rules for emails / messenger / techdocs / support / jira"
- "how should I write a runbook"
- "how to write a support reply"
- "convert this to a tech doc"
- "rewrite this Jira ticket"
- "format this as a Jira description"
- "draft a Jira story"

## Workflow
1. Read `_common.md` first — it contains the shared rules.
2. Identify the content type from the user's request (emails, messenger, techdocs, support, jira).
3. Read the corresponding `style.md` and `example.md` from the matching folder.
4. Apply the rules to the user's text.
5. If the user asks for examples, surface the relevant `example.md` content.

## Topics
Each topic lives in its own folder with a rule file and an example file.

- **emails/** — friendly peer emails and formal HR, operations, bank, or advisor requests.
- **messenger/** — compact, conversational tone for Slack, Teams, Telegram, Discord.
- **techdocs/** — structured, precise tone for runbooks, technical guides, API references.
- **support/** — professional, factual tone for IT support tickets written by the person reporting the issue.
- **jira/** — concise, decision-oriented tone for Jira tickets, stories, and epic descriptions.

## Common Rules
Always read `_common.md` before applying any style — it contains the shared grammar, formatting, and tone rules.
