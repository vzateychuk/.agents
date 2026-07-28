---
name: techdocs-structured
description: Structured, precise tone for runbooks, technical guides, and API references.
applies_to: [techdocs]
tone: precise
audience: [developer, team lead, manager]
version: 4
---

# Tech Docs Style — Structured & Precise

## Tone
- Precise and factual.
- Use imperative voice for how-to steps ("Run the command", "Configure the proxy").
- For failures, explain cause: what broke, why, and which later step depends on the fix.
- Keep sections short. Each section covers one topic.

## Structure
- H1: document title or outcome ("Configure git-proxy for the corporate network").
- State target scenarios early (who and where: developer workstation, pod, region).
- H2: major sections. H3: subsections.
- How-to: numbered lists for steps; bullets for non-sequential lists.
- Troubleshooting: for each failure use Problem → Result → Root cause. Order sequential failures when fixing one unlocks the next.
- Outcome-focused headings ("Deploy the API service", "Verify the rollout").
- Code blocks for commands, paths, and snippets.

## Vocabulary
- "Run", "Configure", "Verify", "Deploy".
- "Target scenarios", "Problem", "Result", "Root cause".
- Exact technical terms, hostnames, ports, error strings, and CA or issuer names.
- Expand acronyms on first use ("API (application programming interface)", "TLS (transport layer security)").
- Reference other docs by relative path or link.

## Formatting
- Put reproduction commands and exact error output in code blocks.
- One sentence per line in code blocks where possible.
- Sentence case for headings.
- Always write in English.
- Prefer plain text where markdown adds little clarity.

## Edge Cases
- If the user provides non-English text, translate to English first, then apply the style.
- If the draft is only a problem statement, keep the diagnostic structure and add Configure / Verify steps when the user asks for a full runbook.
