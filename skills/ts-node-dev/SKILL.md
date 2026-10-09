---
name: ts-node-dev
description: >-
  Strict TypeScript and Node.js checklist for refactoring, typing fixes, and
  test generation. Use only when the user asks to refactor TypeScript or Node
  code, tighten types, or write tests - not for every TypeScript question.
---

# TypeScript / Node checklist

Follow the project's existing layout. Do not invent Controllers / Services / Repositories layers unless the codebase already uses them.

## Rules
1. No `any`. Prefer `unknown`, generics, discriminated unions, and runtime checks.
2. Avoid non-null assertions (`!`) unless the invariant is proven nearby.
3. Handle async errors explicitly; do not leave unhandled promise rejections.
4. Do not block the Node.js event loop with heavy synchronous work.
5. Match existing patterns for modules, errors, and dependency wiring.
6. Add or update tests (Vitest or Jest, Arrange-Act-Assert) only when the user asks or the change needs a regression check.
7. Return production-ready TypeScript in `ts` code blocks; keep explanations short (edge cases and trade-offs).
