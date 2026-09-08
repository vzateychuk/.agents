# Ticket Examples

Ticket bodies are English. Each example shows the raw input and the finished ticket.

Facts come from real project tickets, so the shape is realistic: what a ticket looks like when the cause is known, when it is not, and when part of the work is already done.

## Example 1: Config cleanup, scope fully known

Input: "надо выпилить старые поля конфига proxyUrl, sslKeyPemPath, sslCertPemPath, они deprecated, но всё ещё принимаются. Делаем в 3.0."

Output:

```markdown
# [GitProxy] Remove deprecated proxy and TLS config fields in 3.0

## Business Context
Two configuration paths are alive at once, so every onboarding team has to ask which one is authoritative.

## Problem Statement
`proxyUrl`, `sslKeyPemPath` and `sslCertPemPath` are deprecated but still accepted by the config loader. Code, sample configs and docs disagree on the supported set.

## Acceptance Criteria
- Config loading fails with an error naming the replacement field when any of the three is present.
- No reference to the removed fields remains in code, sample configs or docs.
- A test covers the rejection path; the existing suite passes.

## Actions & Outcomes
Fields removed on the 3.0 branch, sample config and README updated, PR raised against 3.0.
```

## Example 2: Reproducible bug, cause unknown

Input: "push в UAT валится 504, воспроизводится. Причина непонятна — то ли прокси, то ли таймауты, то ли сеть."

Output:

```markdown
# [GitProxy] Fix HTTP 504 on git push in UAT

## Business Context
UAT is the last gate before production, so a failing push blocks release validation for every onboarding team.

## Problem Statement
`git push` through the proxy in UAT returns HTTP 504 and reproduces reliably. The root cause is not identified: proxy behaviour, timeout configuration and the network path are all candidates.

## Acceptance Criteria
- Root cause identified and named in a comment on this ticket.
- `git push` in UAT completes without a 504 after the fix.
- Timeout values in effect for UAT are written down in the runbook.

## Actions & Outcomes
Cause diagnosed, fix applied, push verified in UAT, timeout values recorded in the runbook.
```

Note the wording: the first acceptance criterion is finding the cause, not fixing it. When the cause is unknown, naming it is part of Done.

## Example 3: Rewrite of a vague ticket

Input, existing ticket: "Certificate error on Dev VDI. Fix certificates."

Output:

```markdown
# [GitProxy] Resolve ERR_CERT_AUTHORITY_INVALID on Dev VDI

## Business Context
Developers cannot reach the proxy from Dev VDI, which pushes them into local workarounds instead of the supported path.

## Problem Statement
Requests through the proxy from Dev VDI fail with `ERR_CERT_AUTHORITY_INVALID`. It is unknown whether the corporate CA is missing from the VDI trust store or the chain served by the proxy is incomplete.

## Acceptance Criteria
- The failing link in the certificate chain is identified and named.
- A request through the proxy from a clean Dev VDI succeeds without certificate warnings.
- The required trust store setup is documented for new VDI machines.

## Actions & Outcomes
Chain diagnosed, missing certificate or configuration corrected, clean-VDI check passed, setup documented.
```

Readiness note reported separately, not inside the body: **Dependencies known — fail**, the owner of the corporate CA on VDI is not named.

## Example 4: Upgrade where part of the work is already done

Input: "апгрейд @finos/git-proxy с 1.19.2 на 2.1.0. Entry points уже переделаны коммитом 85344ca, это не переписывать. Остаются pin версии, плагин на новые subpath exports, схема конфига и onboarding по author email."

Output:

```markdown
# [GitProxy] Pin @finos/git-proxy 2.1.0 and close remaining v2 breaking changes

## Business Context
The wrapper is stuck on 1.19.2, so upstream fixes and security updates from FINOS v2 cannot be picked up.

## Problem Statement
Four v2 breaking changes remain open: version pin, plugin subpath exports, stricter `proxy.config.json` schema, and commit author identity moving from username to email. Startup entry points are out of scope — already adapted in commit `85344ca`.

## Acceptance Criteria
- `@finos/git-proxy` pinned to 2.1.0 in `package.json`.
- The check-training plugin loads through the v2 subpath export API.
- Runtime config passes the 2.1.0 schema; rejected Citi-specific keys are listed or replaced.
- `/health` and `/api/v1/healthcheck` pass locally and on DEV.

## Actions & Outcomes
Version pinned, plugin migrated, config diffed against the 2.1.0 schema, DEV deploy verified. Promotion to UAT and PROD is a separate ticket.
```

Two things this example teaches: work already delivered is named as out of scope instead of being restated, and promotion to other environments is split off rather than hidden in one ticket.

No example here carries a Story Point value or a time estimate. Sizing is **points** mode — see `../points/example.md`.
