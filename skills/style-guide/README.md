# Style Guide Skill

Applies the brand writing style to emails, messenger messages, technical documentation, and support content. JIRA tickets are handled by the `jira-builder` skill.

## Structure

```
style-guide/
├── SKILL.md          # main manifest
├── _common.md        # shared rules for all content types
├── emails/
│   ├── email.md
│   └── example.md
├── messenger/
│   ├── messenger.md
│   └── example.md
├── techdocs/
│   ├── techdocs.md
│   └── example.md
└── support/
    ├── support.md
    └── example.md
```

## Triggers

The skill activates on user requests to:
- rewrite, edit, polish, format text
- check or improve tone
- make text more friendly or more formal
- apply the style guide
- explain the rules for emails, messenger, techdocs, or support
- convert text to a specific content type

## Rules

- Always English
- No emojis
- Prefer bullet points over tables
- For email and messenger: plain text without `**` bold markers
- No AI traces
- No prohibitions in style descriptions
- Expand or avoid abbreviations

## Topics

- **emails/** — friendly peer emails and formal HR, operations, bank, or advisor requests.
- **messenger/** — compact, conversational tone for messenger apps (Slack, Teams, Telegram, Discord).
- **techdocs/** — structured, precise tone for runbooks, technical guides, API references.
- **support/** — professional, factual tone for IT support tickets written by the person reporting the issue.
