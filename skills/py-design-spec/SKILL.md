---
name: py-design-spec
description: >-
  Produces a practical, developer-ready design specification for a change in the
  current Python repository: requirements analysis, repo-fit design, components,
  interactions, data flow, and implementation order. 
disable-model-invocation: true
---

# Python design specification (spec-driven)

Design first. Do not write production code, tests, or commits unless the user
explicitly asks for implementation after the design.

Output the design in chat only. Do not create or edit repository files for the
design document unless the user asks to save it.

## Goal

Turn the user's prompt into a **working design** a developer can implement from: concrete components, how they talk to each other, data flow, where code lands, and a sensible build order. Prefer fit with the existing codebase over greenfield architecture.

## Workflow

Copy and track:

```
Design progress:
- [ ] 1. Restate requirements
- [ ] 2. Map the current repository
- [ ] 3. Propose the design
- [ ] 4. Open questions / risks
- [ ] 5. Deliver the working design in chat
```

### 1. Restate requirements

From the user prompt only, extract:

- Outcome the change must achieve
- Inputs and outputs
- Constraints the user stated (performance, compatibility, deadlines, APIs)

If a requirement is ambiguous and blocks design, ask a short question. Otherwise state an `Assumption:` and continue.

### 2. Map the current repository

Inspect the **current workspace root** (or the path the user named). Prefer existing project layout and conventions over inventing new ones.

Read only what is needed:

- Package/dependency manifests: `pyproject.toml`, `setup.cfg`, `requirements*.txt`, `uv.lock`, `Pipfile`, `conda.environment.yml`
- Layout clues: `src/`, package dirs, `tests/`, `scripts/`, apps under `app/` or  similar
- Entry points and wiring: `__main__.py`, CLI entry points in manifests, Flask / FastAPI / Django app factories, workers, `Makefile` targets that show how the project is run
- Nearby modules that already solve a similar problem (same layer, same pattern)

Summarize in a few lines:

- How the project is packaged and run
- Where new code of this kind usually lives
- Patterns to reuse (naming, layers, error handling, config, testing style)

If the directory is not a project, say so and stop after stating what is missing.

### 3. Propose the design

Follow common Python practice:

- Small, single-purpose modules; clear package boundaries
- Explicit dependencies (constructors / functions), avoid hidden globals
- Thin IO at the edges (HTTP, filesystem, DB); logic in plain functions or small classes
- Match existing test style (pytest layout, fixtures) when proposing verification
- Prefer extending an existing module over a new package when the change is local

Cover follow (if applicable):

| Section | What to decide |
| --- | --- |
| Components | Names, responsibility, owning package/module path |
| Interactions | Who calls whom; sync vs async; events/queues if already used |
| Data flow | Request/event in -> transforms -> side effects / response out |
| Contracts | Function/class signatures, key types, error cases worth naming |
| Persistence / IO | What is read/written and where (only if relevant) |
| Config | New settings and where they belong in *this* project |
| Touch list | Files to add or change (paths relative to repo root) |
| Verification | How a developer will know it works (tests, manual checks) |
| Build order | Numbered steps from foundation to wiring to tests |

Reject ceremony: no enterprise templates, no mandatory UML, no standard document numbers. Include a Mermaid diagram only when it clarifies interactions or data flow.

### 4. Open questions and risks

List only items that affect implementation:

- Unknowns that need a product owner or code owner answer
- Coupling or migration risks inside this repo
- Assumptions that, if wrong, force a redesign

### 5. Chat deliverable format

Use this structure in the reply (Russian is preferable):

```markdown
# Design: <short title>

## Requirements
- ...

## Assumptions
- Assumption: ...

## Current repo fit
- Packaging / runtime: ...
- Conventions to follow: ...
- Anchors to reuse: `<path>` — why

## Components
- Component, Responsibility, Module path ...

## Interactions
- ...
(optional Mermaid sequence or flowchart)

## Data flow
1. ...
2. ...

## Contracts
- `module.function(...)` -> ... ; errors: ...

## Files to touch
- Path, Action, Why

## Verification
- ...

## Implementation order
1. ...
2. ...

## Open questions
- ...
```

End with one line: ready to implement on request (or blocked on a listed question).

## Hard rules

- Explicit skill use only; do not run this workflow from ambient chat.
- No production implementation in the same turn as the design.
- Label guesses as `Assumption:` or `[NOT CONFIRMED: ...]`.
- Prefer the repository's existing patterns over generic "clean architecture" when they conflict.
- Keep the design short enough to act on in one sitting; split only if the user asked for a multi-phase change.

