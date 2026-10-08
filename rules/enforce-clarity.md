---
name: enforce-clarity
description: Explain every term in plain words. No abbreviations. Clarity over brevity.
alwaysApply: true
---

# Explain Every Term

MAIN RULE: Every technical term must be explained in plain words. Abbreviations are forbidden.
- Never use abbreviations. Always write the full words: "pull request", not "PR".
- Explain every technical term, tool name, and internal name at first use: "Maven (a build tool for Java projects)".
- Never show a code name without explaining it: "`bom_lookup` (the check that finds library versions in the approved list)".
- Never write arrow chains like `Path A -> SA -> POC`. Write full sentences.

Clarity always wins over brevity. A short but unclear answer is a violation.
When asked to be brief: cut intros and minor details, but keep every explanation.
- Write for a reader who has not seen the previous conversation.
- Use short, simple sentences and bullet lists.
- Say who does each action: the user, the code, or the system.
- In chat, never copy Case status text verbatim.
- After save or lint: 2-5 plain bullets: what is done, what is next.

BAD: `Ticket Open / High. Done: tests/bom_lookup. Next: parent POM + PR.`
GOOD: `The task in Jira (the team task tracker) is open with high priority. The scanner already finds the Spring Framework version when a project lists only Spring Boot. Next: read versions from the parent Maven file (the shared list of library versions) and send the changes for review as a pull request.`

Before sending, check every sentence:
1. Is every abbreviation replaced with full words?
2. Is every technical term explained in plain words?
3. Would a newcomer understand it without the previous conversation?
If any answer is "no", rewrite.
