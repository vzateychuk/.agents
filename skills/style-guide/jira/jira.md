---
name: jira-ticket
description: Concise, decision-oriented style for Jira tickets, stories, and epic descriptions written by engineers and leads.
applies_to: [jira]
tone: concise
audience: [developer, team lead, manager, colleague]
version: 3
---

# Jira Style — Concise & Decision-Oriented

## Tone
- Concise, factual, and scannable in a Jira description field.
- Active voice. State impact and blockers in concrete terms.
- Decision-oriented when options exist: make tradeoffs easy to compare.

## Structure
Core sections (in order):
- Summary (title): 50-80 characters. Lead with the component or outcome.
- Problem: what is blocked or delayed, and why it matters now. For upgrades, list flagged items as `package — current: x.y.z` (runtime separate from libraries).
- Goal: desired end state in one or two sentences.
- Deliverables: concrete, checkable outcomes.

Add when needed:
- Options: numbered choices when a decision is required. One line per option plus tradeoff.
- Scope / Out of scope: what is in and what is explicitly out.
- Acceptance criteria: checkable "done" behavior (bullets or Given/When/Then).
- Dependencies: tickets, teams, services, or releases that block or are blocked.
- Constraints: sync rules, ownership gaps, platform limits, approach notes.
- Open questions: unresolved items that block estimate or decision.
- Verification: how to confirm in the target environment.
- Links / References: repo URLs, scans, Confluence, CALM, pull requests, runbooks.

## Vocabulary
- "Problem", "Goal", "Options", "Scope", "Out of scope", "Acceptance criteria"
- "Dependencies", "Constraints", "Open questions", "Deliverables", "Verification"
- "Depends on", "Blocked by", "Ownership", "PoC (proof of concept)"
- Exact ticket IDs, repo URLs, package names, versions, and environment names.

## Formatting
- Bold section labels (`**Problem:**`, `**Goal:**`).
- Numbered lists for options; bullets for criteria, deliverables, scope, and dependencies.
- One blank line between sections. Prefer plain text. Always English.

## Edge Cases
- Simple task: Problem, Goal, Acceptance criteria or Deliverables only.
- Simple upgrade: Problem (inventory) → Goal → Scope checklist → References. The Scope checklist may replace Deliverables and Verification when each scope line is already checkable (analyze, bump, PR, tests, audit).
- Decision or spike: add Options, Constraints, Open questions; keep Deliverables measurable.
- Bug reports: use the support style (steps, expected, actual, environment).
