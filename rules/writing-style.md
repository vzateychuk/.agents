---
name: writing-style
description: Plain, human-style writing for all text and files. Hard rules on punctuation, emoji, lists and file formatting.
alwaysApply: true
---

Applies to chat replies, documentation, comments and any text files. Git commit format and language-specific code style take precedence where they differ.

# Hard rules

Write mostly in short paragraphs. Use a list only for parallel items or ordered steps, never for explanations. Two or three related points go into one sentence. Do not nest lists.

Do not use bold except for a warning the reader must not miss. Do not use bold for list item names or section labels.

Use only the hyphen-minus (U+002D) as a dash. Never use the characters U+2013 and U+2014. Write "a - b", not an em dash.

Write arrows as "->". Never use the character U+2192.

Never use emoji or pictographic symbols (check marks, crosses, stars, warning
signs) anywhere, including code comments.

Files must use LF line endings and have no trailing spaces or tabs.

# Style

Use descriptive headers and a logical order. Keep formatting consistent within a document. Write natural, plain language without filler or formal phrasing.

# Examples

Bad: "Key points: - **Speed** - fast. - **Cost** - low."
Good: "The service is fast and cheap to run."

Bad: "Step 1 -> done" with a check mark and an em dash.
Good: "Step 1 -> done"

# Before finishing

Re-read the text once and fix any use of the forbidden characters, bold labels, or lists that should be prose.
