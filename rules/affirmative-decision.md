---
name: affirmative-text
description: In any text for a human or an agent (answers, instructions, docs, ADRs, comments), state what to do and what is true. Omit obvious prohibitions, invented negations, and rejected options.
alwaysApply: true
---

# Affirmative Text

Rule: write what the reader should do, and what the system does, stores, or calls. Silence means an unused or rejected path is not part of the message.

Rewrite a prohibition as the chosen action: "Do not call POST /export" -> "Ingest calls GET .../download-file".

## Self-check for each sentence

1. Does it state an action, a fact, or a result?
2. Is it backed by a source in this conversation or by an explicit request?
3. Would a competent reader do the wrong thing without it?

Omit the sentence when (1) or (2) is "no", or when (3) is "no".

## Allowed negations

- Real results: what failed, what was not run, what is unknown or unverified. Report these plainly, they are facts.
- Non-obvious, costly mistakes: one short sentence, phrased affirmatively where possible ("Send the archive request without an Authorization header; a signed URL breaks otherwise").
- Safety-critical warnings (data loss, security, irreversible actions).
- Anything the owner explicitly asked to include.

## Examples

BAD: `Update the timeout in config.yaml. Do not delete the file. Do not change other keys. Do not restart unrelated services.`
GOOD: `Set timeout to 30 in config.yaml, then restart the api service.`

BAD: `v1 does not call POST /export. Retention of deactivated rows is out of scope.`
GOOD: `Ingest uses GET .../download-file, then GET of the archive url.`

