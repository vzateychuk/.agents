---
name: testing
description: 'Creates unit/integration/E2E test code, coverage strategies, and gap analysis. Use when writing new tests or analyzing coverage. Do NOT execute tests (use language-specific tools: python-tools for Python, nodejs-ts-ops for JS/TS). Do NOT debug failing tests — use debug skill.'
---

## Scope

**This skill handles:**
- Writing new tests (unit, integration, E2E) — code and structure
- Test planning and design patterns
- Coverage gap analysis and strategic recommendations
- Proactive test improvements and test quality review
- Test framework selection and best practices

**This skill does NOT handle:**
- Executing/running tests (use **python-tools** for Python, **nodejs-ts-ops** for JS/TS)
- Debugging failing tests or investigating bugs (use **debug** skill)
- General code review outside of test code (use **review-quality** skill)
- Language-specific test commands and tooling

## Purpose
- Run all test types (unit, integration, E2E).
- Write tests for new functionality.
- Analyze coverage, surface and prioritize gaps.

## When to use
User triggers:
- "write tests for module X"
- "run tests"
- "what is covered by tests?"
- "analyze test coverage"
- "which functions need tests?"

(For "why are tests failing?" → use **debug** skill, not this one)

## Core tasks
| Task | How | Example command |
|------|-----|---------|
| Run tests | Read manifest, execute | `npm test` or `pytest` |
| Write unit tests | AAA pattern + mocks | Test single function behavior |
| Write integration tests | Test with real dependencies | Test API endpoint with DB |
| Analyze coverage | Generate report | `npm test -- --coverage` |
| Prioritize gaps | Start with entry points, then business logic | Which functions have no tests? |

## Correctness verification
Ask to show a failing test → propose a minimal fix → re-run test.

## Related skills
- For **code/test review**: `review-quality`
- For **flaky tests**: `debug`
