# Story Point Examples

Estimates are explained in Russian; ticket keys, package names and field names stay as in the source.

All four cases are real project tickets, so the numbers show how the rules interact: known scope, unknown cause, partially delivered work, and a ticket that must be split.

## Example 1: Known scope, nothing external — 2

Input: `C175021A-2620`, remove three deprecated config fields on the 3.0 branch, acceptance criteria written.

```markdown
**Story Points:** 2
**Confidence:** high

**Why:**
- Complexity: правка на уровне полей в одном компоненте, путь решения известен заранее
- Effort: код, sample-конфиг и README; загрузка конфига покрыта существующими тестами
- Uncertainty: низкая, внешние стороны не участвуют; единственный риск — привязка к готовности 3.0

**vs anchors:** like the 2 anchor — это и есть якорь `C175021A-2620`
```

## Example 2: Unknown root cause — 5, ceiling

Input: `C175021A-2875`, reproducible HTTP 504 on `git push` in UAT, no diagnosis yet.

```markdown
**Story Points:** 5
**Confidence:** low

**Why:**
- Complexity: неизвестно, где ломается — прокси, таймауты или сетевой путь
- Effort: воспроизведение есть, значит диагностика конечна, но объём самого фикса неизвестен
- Uncertainty: высокая, причина не найдена; возможен выход на платформенную команду

**vs anchors:** between the 5 and 8 anchors — по неизвестности тяжелее `C175021A-2899`, по объёму легче `C175021A-2507`

**Missing for a tighter estimate:**
- Причина 504: прокси, таймаут или сеть
- Действующие на UAT значения таймаутов и логи запроса

Оценка — верхняя граница до диагностики. Когда причина найдена, пересмотреть: правка одного таймаута это 1-2, переделка обработки соединений — 8 и выше. Если упрётся во внешнюю команду, поднять до 8.
```

Two rules at work: причина не найдена — не ниже 5, и при противоречивых сигналах (критерии написаны, причина неизвестна) берётся низший уровень уверенности.

## Example 3: Part of the work already delivered — 8

Input: `C175021A-2507`, upgrade `@finos/git-proxy` 1.19.2 to 2.1.0. Entry points already adapted in commit `85344ca`; remaining: version pin, plugin subpath exports, config schema, commit author identity.

```markdown
**Story Points:** 8
**Confidence:** medium

**Why:**
- Complexity: четыре независимых breaking change, включая identity в onboarding
- Effort: остаток, а не весь апгрейд: entry points закрыты коммитом `85344ca`
- Uncertainty: changelog 2.0.0 → 2.1.0 не разобран, отвергнутые схемой Citi-ключи заранее неизвестны

**vs anchors:** like the 8 anchor — это и есть якорь `C175021A-2507`

**Missing for a tighter estimate:**
- Влит ли `85344ca` в ветку, с которой идём на 2.1.0
- Список breaking changes между 2.0.0 и 2.1.0

Апгрейд целиком, без учёта `85344ca`, был бы 13 и требовал дробления. Промоушен на UAT и PROD в эту оценку не входит — отдельный тикет.
```

Note what moves the number down: already delivered work is excluded from the estimate, the same way it is excluded from the ticket body.

## Example 4: Oversized ticket — 20 and a split

Input: `C175021A-2615`, one ticket covering the Citi fork inside project #176099, the existing pipeline, the dependency swap in the wrapper, an upstream sync runbook and a DEV proof of concept.

```markdown
**Story Points:** 20
**Confidence:** medium

**Why:**
- Complexity: пять разнородных работ в одном тикете, от создания репозитория до proof of concept
- Effort: несколько компонентов плюс согласования вне команды
- Uncertainty: высокая на шагах onboarding, низкая на самом форке — ownership уже выяснен

**vs anchors:** heavier than the 8 anchor — заметно крупнее `C175021A-2507`

**Split:**
- Создать репозиторий fork внутри Lightspeed #176099 — 3
- Подключить репозиторий к существующему pipeline #176099 — 5
- Заменить зависимость `@finos/git-proxy` на артефакт fork в wrapper — 5
- Runbook синхронизации с upstream (merge и cherry-pick) — 3
- Proof of concept: wrapper на fork в DEV — 5

20 в поле Jira означает «дробить», а не размер. Сумма кусков не обязана совпадать с 20: после дробления неизвестность падает.
```
