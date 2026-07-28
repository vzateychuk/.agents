# Email Examples — Friendly & Formal

## Example 1: Formal HR / operations request

**Subject:** Temporary salary payment method (Mar–May 2026)

**Body:**
Dear Operations and HR Team,

I would like to request a temporary change to my salary payment method for March–May 2026.

My salary is currently paid via Rippling to my bank account in Georgia. New regulatory requirements mean that, as an individual entrepreneur, I need a valid residence permit to keep using that account. Obtaining the permit may take up to three months; I plan to apply in April 2026.

Could you temporarily switch my salary payments to the Deel platform for March–May 2026?

If Deel is not feasible, could you consider salary payments in cryptocurrency for the same period?

This is a temporary measure until the residence permit process is complete and the standard Rippling setup can resume. I am happy to provide any additional documentation if needed.

Kind regards,
Vladimir Zateychuk

---

## Example 2: Formal FYI / compliance heads-up

**Subject:** Heads-up: outbound SWIFT transfer USD 100 (TBC → brokerage)

**Body:**
Dear Salome,

I have initiated a small outbound SWIFT transfer of 100 USD from my TBC USD account to my personal brokerage account at Freedom Finance Global PLC (Kazakhstan). Screenshot attached.

This is a standard transfer to fund my investment portfolio. The description field was filled in manually, so I wanted to give your team a proactive heads-up.

If compliance or processing needs any additional confirmation or documents, please let me know directly — I will provide them immediately.

Kind regards,
Vladimir Zateychuk

---

## Example 3: Internal update

**Subject:** Notes from today's sync

**Body:**
Hi team,

Quick notes from our meeting today:
- We agreed to push the release to next Tuesday.
- Maria will own the QA pass.
- I'll send the updated timeline tomorrow.

Let me know if I missed anything.

Thanks,
Alex

---

## Example 4: Help request with due diligence

**Subject:** AD groups for OpenShift Edit Route (UAT)

**Body:**
Hi Noel, colleagues,

I'm writing runbooks for git-proxy (#176099) and using CALM 175021 as a reference. I need help understanding how to create AD groups and set up Edit Route access in UAT — I could not figure it out on my own.

What I checked (UAT):
- `oc login` works against the UAT API (user `vz42555`)
- Only project: `cti-ciso-fosst-176099` (Route `git-proxy-vanity`)
- `oc auth can-i patch routes` → no
- `oc get rolebinding` → Forbidden
- AD: `...fosst..._view` exists and I am in it; `...fosst..._edit` → 404
- AD: `...icg-msst..._edit` exists, but that membership still gives no Edit Route in fosst

So: for manual Edit Route in fosst we lack rights; icg-msst `_edit` does not help; fosst `_edit` may not exist.

Questions:
1. Where do we map AD groups to `cti-ciso-fosst-176099` vs `icg-msst-git-proxy-176099`?
2. How do we create `app_ecs_uat_cti-ciso-fosst-176099_edit`, and how is it bound to OpenShift?
3. For UAT, is primary SOEID plus `app_ecs_uat_users` enough, or do we also need EMER_ECS?
4. How do we request membership once the right group exists?
5. Could you share links or docs (CMP, ECS/OpenShift onboarding, CALM) instead of a call? I follow written material better.

Thanks,
Vladimir
