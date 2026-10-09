---
name: style-guide
description: >-
  Apply brand writing style to email, messenger, techdocs, or support text.
  Use when the user names that content type or asks to apply the style guide.
  Always English, no emojis. Prefer bullets over tables.
---

# Style Guide (router)

Load only what the request needs. Never read all four topic folders in one turn.

## Workflow
1. Identify one content type: `emails`, `messenger`, `techdocs`, or `support`.
2. For small / weak models: prefer `style-guide-lite.md` alone when the ask is a short rewrite and the type is clear.
3. Otherwise read `_common.md`, then only the matching topic rule file:
   - email → `emails/email.md`
   - messenger → `messenger/messenger.md`
   - techdocs → `techdocs/techdocs.md`
   - support → `support/support.md`
4. Read `example.md` in that folder only if the user asks for an example or few-shot.
5. Do not read `README.md` (human docs only).

## Topics
- **emails/** - peer email or formal HR / ops / bank / advisor
- **messenger/** - Slack, Teams, Telegram, Discord
- **techdocs/** - runbooks, guides, API references
- **support/** - IT support tickets written by the reporter
