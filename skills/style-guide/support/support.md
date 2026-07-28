---
name: support-ticket
description: Professional, factual style for writing IT support tickets. Use when creating or polishing a ticket describing a technical problem to the IT support team.
applies_to: [support]
tone: professional
audience: [it-support, helpdesk, sysadmin]
version: 2
---

# Support Ticket Style — IT Support

## Tone
- Professional, factual, and concise.
- Active voice.
- Technical and direct. Apologies only when work is blocked.
- Clear factual statements. Gender-neutral pronouns (they, them).

## Structure
Write the ticket with these sections in order:
- Title: 50-80 characters. Lead with the affected component or system. Example: "API returns 500 on POST /users in production".
- Summary: 1-2 sentences. State impact in concrete terms.
- Steps to Reproduce: numbered list, one step per line. Exact command, URL, or click path. Note frequency (always, sometimes, once).
- Expected Behavior: 1-2 sentences. Reference docs or specs when relevant.
- Actual Behavior: 1-2 sentences. Include the exact error message or code.
- Environment: OS, version, browser, application, build, region as bullet points.
- Logs and Screenshots: link, attachment, or short excerpts. Note the timestamp.
- Severity: Critical (blocks all work, workaround unavailable) or Low (minor issue, workaround available).
- Workaround: temporary fix if any; note cost or side effects.

## Vocabulary
- "Steps to reproduce", "Expected", "Actual", "Environment"
- "Blocks work", "Production down", "Cannot reproduce"
- "Intermittent", "Happens 100% of the time", "Workaround available"
- "Critical", "Low"

## Formatting
- Bullet points for environment, logs, and workarounds.
- Numbered lists for steps to reproduce.
- One blank line between sections.
- Always write in English. Plain text preferred.

## Edge Cases
- If the report is vague, ask for missing details before writing the ticket.
- If the issue is not yet reproducible, state that clearly and note what was tried.
