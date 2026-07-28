# Jira Examples — Concise & Decision-Oriented

## Example 1: Decision ticket (fork ownership)

**Summary:** Activate Citi/git-proxy fork and define upstream sync

**Problem:** Lightspeed # 176099 depends on `@finos/git-proxy`; PROD is delayed by the FINOS release cadence. A fork exists at https://github.com/Citi/git-proxy but has no clear owner; the wrapper still uses the FINOS npm package.

**Goal:** Activate the existing fork — ownership, integration model, and switch the wrapper to the internal fork.

**Options:**
1. Manage the fork inside # 176099 and reuse the existing pipeline.
2. Take over the existing Citi/git-proxy repo and its pipeline. No new pipeline.

**Scope / Out of scope:**
- In: ownership, wrapper switch, sync model, PoC in dev
- Out: new CI pipeline, PROD cutover in this ticket

**Constraints:**
- Upstream sync must cover Citi-ahead and FINOS-ahead cases (upstream-first, periodic merge, cherry-pick blocking pull requests, internal versioning, conflict-resolution runbook).

**Open questions:**
- Who owns https://github.com/Citi/git-proxy today?
- Which option reuses the existing pipeline with less risk?

**Deliverables:**
- Ownership identified
- Option chosen
- Sync runbook written
- PoC (proof of concept) in dev

**Verification:**
- Dev build installs the internal package and starts git-proxy successfully

**Links:**
- Parent: Lightspeed # 176099
- Fork: https://github.com/Citi/git-proxy

---

## Example 2: Simple dependency upgrade

**Summary:** Upgrade flagged git-proxy dependencies for security alerts

**Problem:** Security and maintenance alerts flag dependencies in finos/git-proxy:
- nodemailer — current: 6.10.1
- simple-git — current: 3.27.0
- lodash — current: 4.17.23
- axios — current: 1.13.5
- Node.js runtime — current: 22.18.0

**Goal:** Upgrade each flagged dependency to the latest stable version, clear high/critical alerts, and stay compatible with the current Node.js LTS runtime.

**Scope:**
- Analyse `package.json` and `package-lock.json` in upstream finos/git-proxy
- Identify the minimum safe target versions for each flagged dependency
- Open an upstream pull request with the version bumps
- Verify unit tests (Mocha/Chai) and E2E tests (Cypress) pass
- Confirm `npm audit` reports no remaining high or critical vulnerabilities

**References:**
- Upstream repo: https://github.com/finos/git-proxy
- Alerts flagged by: internal dependency scan

---

## Example 3: Spike with open questions

**Summary:** Spike AD group mapping for OpenShift Edit Route (UAT)

**Problem:** Engineers in `cti-ciso-fosst-176099` cannot patch Routes. The `_view` AD group exists; `_edit` appears missing.

**Goal:** Identify which AD group grants Edit Route and how membership is requested.

**Scope / Out of scope:**
- In: mapping and request path for UAT
- Out: creating production groups

**Open questions:**
- Is `app_ecs_uat_cti-ciso-fosst-176099_edit` created in CMP, ASDA, or marketplace?
- How is the group bound to OpenShift (Lightspeed or separate)?

**Deliverables:**
- AD group to project mapping documented
- Membership request path identified
- Findings posted on the parent ticket

**Verification:**
- After membership, `oc auth can-i patch routes` returns yes in the fosst project
