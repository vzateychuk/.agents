# [managed]
@~/.agents/rules/clarify-before-planning.md
@~/.agents/rules/no-guessing.md
# [/managed]

### File Access & Web Rules

1. LOCAL FIRST: ALWAYS check local workspace files FIRST using bash commands (ls, find, cat) before making network requests, especially if the repository is in the current working directory.

2. READ WEB PAGES: When you need to read a remote web page or URL, use the Jina Reader bash command:
`curl -sSL https://r.jina.ai/<URL>`

3. READ RAW GITHUB FILES: For fetching raw code or files from GitHub, do not use Jina or /blob/ paths. Use the direct raw URL:
`curl -sSL https://raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>`

4. CHECK LATEST RELEASES: To check the latest release or version of an open-source project:
- Prefer GitHub API: `curl -sSL https://api.github.com/repos/<owner>/<repo>/releases/latest`
- Or use Jina on the releases page: `curl -sSL https://r.jina.ai/https://github.com/<owner>/<repo>/releases`