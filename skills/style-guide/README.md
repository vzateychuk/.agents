# Style Guide Skill

Applies the brand writing style to emails, messenger messages, technical documentation, support content, and Jira tickets.

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
├── support/
│   ├── support.md
│   └── example.md
└── jira/
    ├── jira.md
    └── example.md
```

## Triggers

The skill activates on user requests to:
- rewrite, edit, polish, format text
- check or improve tone
- make text more friendly or more formal
- apply the style guide
- explain the rules for emails, messenger, techdocs, support, or jira
- convert text to a specific content type
- rewrite or draft a Jira ticket, story, or description

## Rules

- Always English
- No emojis
- Prefer bullet points over tables
- For email, messenger, and jira: plain text without `**` bold markers
- No AI traces
- No prohibitions in style descriptions
- Expand or avoid abbreviations

## Topics

- **emails/** — friendly peer emails and formal HR, operations, bank, or advisor requests.
- **messenger/** — compact, conversational tone for messenger apps (Slack, Teams, Telegram, Discord).
- **techdocs/** — structured, precise tone for runbooks, technical guides, API references.
- **support/** — professional, factual tone for IT support tickets written by the person reporting the issue.
- **jira/** — concise, decision-oriented tone for Jira tickets, stories, and epic descriptions.
