You MUST explicitly READ and follow the following rules files:

# [READ-RULES]
/home/vez/.agents/rules/enforce-clarity.md
/home/vez/.agents/rules/no-guessing.md
/home/vez/.agents/rules/writing-style.md
/home/vez/.agents/rules/tool-priority.md
# [/READ-RULES]

### File Access & Web Rules

1. LOCAL FIRST: Always prioritize local workspace files and directories before querying external networks. Inspect local context using dedicated built-in tools (`find`, `grep`, `read`) according to `tool-priority.md`. Do not run recursive bash listings (`ls -R`).

2. FETCH REMOTE WEB PAGES: When reading an external article, documentation page, or URL, use Jina Reader via curl to strip HTML clutter and save tokens:
   `curl -sSL https://r.jina.ai/<URL>`

3. EXTERNAL SOURCES DISCIPLINE: When retrieving facts from the web, prefer authoritative, primary, or official sources. Cross-reference claims and never rely on unverified search snippets alone.
