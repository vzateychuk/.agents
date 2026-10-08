---
name: respect-gitignore
description: Exclude paths listed in .gitignore when listing project structure, finding files or searching file contents. Use for any task that explores the project.
alwaysApply: true
---

# File rules

- Treat every path listed in .gitignore as excluded from the project.
- Never list, search or read excluded paths (e.g. node_modules/ if it is in .gitignore).
- Exclude them from command or tool call (ls, find, grep, tree, glob).
- If you must look inside an excluded path, ask me first.
