  ---
   name: tool-priority
   description: Recommended priority for file exploration and search tools.
   alwaysApply: true
   ---

   # Tool Selection Priority

   To optimize token usage and search accuracy, prefer specialized FFF tools over general bash commands for project exploration.

   ## Priority

   1. **File Search**: Prefer `find` over `bash find` or `ls -R`. It is faster and frecency-ranked.
   2. **Content Search**: Prefer `grep` over `bash grep`. It provides paginated output and better context.
   3. **Multi-Pattern Search**: Use `fff_multi_grep` when searching for multiple related terms or symbols in one pass.
   4. **Companion Files**: Use `related_files` to quickly find corresponding tests, types, or styles for a module.
   5. **Fuzzy Path Resolution**: Use `resolve_file` to convert a vague reference into an exact file path.

   ## When to use Bash
   Continue using `bash` for tasks that FFF tools cannot perform, such as:
   - Checking file permissions or ownership.
   - Using specialized system utilities (e.g., `du`, `df`, `chmod`).
   - Operations requiring complex shell piping or redirection.
