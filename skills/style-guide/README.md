# Style Guide Skill (human docs)

For agents: use `SKILL.md` as the router. Do not load this README into the prompt.

## Structure

```
style-guide/
├── SKILL.md              # router (load one topic only)
├── style-guide-lite.md   # compact rules for small models
├── _common.md            # shared rules
├── emails/
├── messenger/
├── techdocs/
└── support/
```

Each topic folder has a rule file and an optional `example.md` (load examples only on request).

## Rules of thumb
- Always English, no emojis, prefer bullets over tables
- Email / messenger: plain text without `**` bold
- Lazy load: one content type per turn
