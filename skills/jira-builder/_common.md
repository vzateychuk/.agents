# Common JIRA rules

Read this before **ticket** and **readiness** modes.

## Source of truth

- The Sprint Health Guide wiki Policy is the canonical source for ticket sections and Definition of Ready.
- Read the policy when it is linked, provided, or otherwise accessible in the current context.
- Follow the policy instead of defining a competing ticket structure.
- Do not copy the full policy text into this skill. The four criteria below are a working checklist, not a replacement: if the policy is accessible and its wording differs, the policy wins.
- If policy-specific guidance is required but the policy is unavailable, ask for its link or content. Never invent its rules.
- **Exception — Story Points.** The scale, anchors and estimation rules live in `points/points.md` and are deliberately self-contained. Never take a scale from the wiki, the policy or any external source.

## Definition of Ready

Check the ticket against these criteria. Identify missing information briefly instead of filling gaps with assumptions.

| Criterion | Met when |
|-----------|----------|
| **Clear** | Business context and problem statement are present |
| **Actionable** | Verifiable acceptance criteria are present |
| **Feasible** | Fits a single sprint — in Story Points that means below 13 (see `points/points.md`) |
| **Dependencies known** | External dependencies and other teams are named |

A ticket failing **Feasible** is not ready as a whole: propose a split rather than a readiness verdict.

## Output format — readiness

Verdict first, then one line per criterion. No prose padding, no repeated lists.

```markdown
**Ready:** yes | no

- **Clear** — pass | fail: what is missing
- **Actionable** — pass | fail: what is missing
- **Feasible** — pass | fail: what is missing
- **Dependencies known** — pass | fail: what is missing
```

Omit the colon and the text when a criterion passes. If **Feasible** fails, replace the verdict with a split proposal from **points** mode — a ticket that does not fit is not "not ready", it is the wrong ticket.

Example — real ticket `C175021A-2615`, which carries five deliverables at once:

```markdown
**Ready:** no

- **Clear** — pass
- **Actionable** — fail: deliverables name outcomes (ownership, integration option, sync runbook, DEV proof of concept), not verifiable criteria per outcome
- **Feasible** — fail: five separate deliverables, sized 20 — split required
- **Dependencies known** — pass

**Split proposal:** see points mode — the ticket is not "not ready", it is cut wrong.
```

Never lower a criterion to make a ticket look ready.
