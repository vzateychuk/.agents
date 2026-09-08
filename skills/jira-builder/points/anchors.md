# Story Point anchors — CSI 176099 / git-proxy

Anchors are **concrete estimated tickets**, not adjectives. Ask one question: is this ticket lighter or heavier than the anchor?

| SP | Anchor ticket | Why it sits there |
|----|---------------|-------------------|
| **2** | `C175021A-2620` — remove deprecated config fields `proxyUrl`, `sslKeyPemPath`, `sslCertPemPath` | Field-level cleanup in one component; path known before starting; nobody else involved |
| **5** | `C175021A-2899` — get network data from Drift (AppInsight Resiliency) | One external system; moderate effort; details surface while doing it |
| **8** | `C175021A-2507` — remaining work of the `@finos/git-proxy` 1.19.2 → 2.1.0 upgrade | Several components plus external dependencies and promotion steps; fits a sprint only as a whole |

**Oversized reference (20).** `C175021A-2615` — Citi fork plus upstream sync plus Lightspeed onboarding as one ticket: new repo, pipeline, dependency swap, sync runbook, DEV proof of concept. That must be split, not estimated.

These anchors deliberately replace the source guide's generic baselines (`Domain creation` = 2, `Logical Model example` = 5), which belong to another team's domain and are not comparable to git-proxy work.

## Recalibration

- An anchor only works if the user remembers the ticket. An anchor named by the user in the conversation always wins.
- Replace an anchor when it goes stale or when a closed ticket describes the size better.
- A project may override this file at `.cursor/skills/jira-builder/points/anchors.md`; that copy wins over this one.
- In a project with no anchors, fall back to the signals column in `points.md` and set anchors after two or three tickets are estimated and closed.
