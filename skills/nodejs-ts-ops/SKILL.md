---
name: 'nodejs-ts-ops'
description: 'Node.js/TypeScript test execution and code quality via npm/pnpm (vitest, playwright, eslint, prettier). Runs tests and formats code. For test design/strategy use testing skill instead.'
---

# Skill: Node.js/TypeScript Operations

## When to use
- "run tests" / "execute tests"
- "run vitest" / "run playwright E2E"
- "generate test coverage"
- "lint TypeScript" / "format code"
- "verify types" / "check tsc"

NOT for: Test design, coverage strategy, or deciding which tests to write (use **testing** skill for that)

## Capabilities
- **Workspaces Management**: Support for `npm workspaces` or `pnpm`. Execution of commands in specific packages.
- **Testing**: Execute `vitest`, `supertest` (API), and `playwright/cypress` (E2E) test suites.
- **Environment**: Handling `.env` files and Docker-based environments.
- **Code Quality**: Integration with `eslint`, `prettier`, and `tsc` for type checking and linting.

## Tool Usage Rules
1. **`read_file` / `edit_file`**: Always check for existing `import` types and path aliases (`@/`).
2. **`execute(command)`**:
    - **Linting**: `npm run lint` or `npx eslint --fix <path>`.
    - **Testing**: `npx vitest run <path_to_test>`.
    - **Build/Check**: `npx tsc --noEmit` to verify type integrity after changes.
3. **Paths**: Be aware of the project root in monorepos. Always verify which `package.json` you are affecting.

## Constraints
- **No Sync I/O**: Never use `fs.*Sync` methods in the code you write.
- **Security**: Never hardcode secrets. Ensure new tools/packages are added to `package.json` correctly.
- **Indentation**: Detect and match the existing `.editorconfig` or Prettier config (usually 2 spaces for TS).