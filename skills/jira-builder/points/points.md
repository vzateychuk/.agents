# Story Point estimation

**Self-contained.** The rules below are the source of truth for the scale. Never take a competing scale from the wiki, the policy or any external page — estimation must work with no wiki access.

Solo estimation for the assignee: the output is the user's working number, not a draft for a team vote and not a planning poker result.

**One ticket per request.** Never score a batch, a backlog or a whole board.

## What a Story Point is

- Relative **size** of the ticket (bigger/smaller than anchors), **not** hours.
- Combines three factors:
  - **Complexity** — how hard / non-standard
  - **Effort** — how much work
  - **Uncertainty** — how much is unknown (env, other systems, other teams, missing AC, unknown root cause)

Never convert SP to days/hours.

## Scale

Only these values: `1, 2, 3, 5, 8, 13, 20`.

Anchors live in `anchors.md` — read it and position the ticket against those tickets first. If the project provides its own `.cursor/skills/jira-builder/points/anchors.md`, that file wins. With no anchors available, use the signals column alone.

The last column is an **internal sanity check only**. Never put hours, days or sprint fractions in the output; justify the number with signals and anchors instead.

| SP | Signals (observable) | Time feel (internal, never output) |
|----|----------------------|------------------------------------|
| **1** | One trivial change in one place; correctness obvious on review; no risk | Minimal |
| **2** | One component; solution known before starting; existing tests cover it; nobody else involved | ~few hours |
| **3** | Several files in one component, or one open question / one person to consult; path still known | ~a day |
| **5** | Several components, or one external system or team; some unknowns surface while doing it | Multiple days |
| **8** | Several components plus external dependencies and many unknowns; heavy coordination; fits a sprint only as a whole | Most of a sprint |
| **13** | Does not fit, or root cause and scope cannot be bounded → **break down** | — |
| **20** | Epic-sized or unclear → refine and split | — |

**20 is the ceiling.** Put 20 in the Jira field; it means "must be split", not a size. Never invent 20+, 30 or 40.

### Anti-examples

The examples show the actual reply, so they are in Russian.

Плохо: «**5**, потому что работы дня на три.» — это прогноз времени в костюме Story Points; внутренняя колонка протекла в ответ.
Хорошо: «**5** — как якорь `C175021A-2899`: одна внешняя система, путь ясен, детали всплывут по ходу.»

Плохо: «**3**, критериев нет, но выглядит несложно.» — уверенность не понижена, отсутствие критериев не вынесено в «Missing».
Хорошо: «**3**, confidence **low**: критериев приёмки нет, открытый вопрос вынесен в блок Missing.»

Плохо: «**8**, потому что это почти весь спринт.» — снова время вместо сигналов.
Хорошо: «**8** — как якорь `C175021A-2507`: несколько компонентов, внешние зависимости, шаги промоушена.»

## Hard rules

- **13 or 20** → always propose a split into tickets each below 13 SP, with a suggested SP per piece.
- **Split sums need not match** the original number: uncertainty drops once the work is broken down. Never justify a split by arithmetic.
- **Unknown root cause** (bug with no diagnosis yet) → not below **5**, and state explicitly that the number is a ceiling to be revised after diagnosis.
- **Blocked by another team or an external system** → move one step up the scale.
- **Torn between two values** → go up only when Uncertainty is high; when the path is known, go down. Never invent an intermediate value: the gaps in the scale exist because precision drops as size grows, and habitual rounding up makes the scale drift so past estimates stop being comparable.
- **No invented scope.** Use only facts present in the input; anything missing goes to the "missing" list, not into the number.

## Confidence

| Level | When |
|-------|------|
| **high** | Verifiable acceptance criteria exist and the scope of change is clear |
| **medium** | The goal is clear, but acceptance criteria are missing |
| **low** | No acceptance criteria, or root cause / dependencies unknown |

**Contradictory signals — take the lowest matching level.** Acceptance criteria written well but root cause unknown is **low**, not high: an unknown cause outweighs a well-written ticket, because the scope of the fix is still unknown. Same for a clear goal with unnamed external dependencies.

## Algorithm

1. Use only facts in the input. Do not invent scope or AC.
2. Rate Complexity, Effort, Uncertainty as low / medium / high.
3. Compare against the anchors from `anchors.md`.
4. Pick **one** value from the scale.
5. Apply the hard rules: split, unknown root cause, external blocker.
6. Set confidence from the table above.
7. Reply in the output format below.

**Always output a number.** If the goal is vague or acceptance criteria are missing, still estimate with **low** confidence and put the open questions in the "missing" list. Never reply with questions instead of an estimate.

Worked examples, including a bug with unknown cause and an oversized ticket with its split: `example.md`.

## Output format

```markdown
**Story Points:** N
**Confidence:** high | medium | low

**Why:**
- Complexity: …
- Effort: …
- Uncertainty: …

**vs anchors:** lighter than the 2 anchor | like the 2 anchor | between the 2 and 5 anchors | like the 5 anchor | between the 5 and 8 anchors | like the 8 anchor | heavier than the 8 anchor

**Split:** (only if 13 or 20)
- … — SP
- … — SP

**Missing for a tighter estimate:** (if any)
- …
```

## Out of scope

- Writing or rewriting ticket bodies → **ticket** mode
- Definition of Ready checks → `../_common.md`
- Estimating a batch, a backlog or a board in one reply
- Inventing Acceptance Criteria just to justify a number
- Hour/day forecasts
- Reading the wiki for a competing scale
