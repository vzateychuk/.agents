---
name: security
description: |-
  Conducts security reviews and hardens applications and APIs for vulnerabilities: authentication, authorization, secrets, injection, data leaks, open redirects, and CSRF.
  Triggers on user requests like "security review this PR", "does this leak secrets?", "check for SQL injection", "add security checklist", or "review auth setup".
  Not for general code quality or logic review (use **review-quality** skill).
---

## Scope

**This skill handles:**
- Authentication and authorization (JWT, OAuth, Spring Security, etc.)
- Hardcoded secrets and credential management
- Input validation and injection risks (SQL, command, XSS)
- Data leakage and PII exposure
- Open redirects and CSRF protection
- Secure headers and encryption

**This skill does NOT handle:**
- Code quality, style, architecture (use **review-quality** skill)
- Logic errors and testing approaches (use **review-quality** or **testing** skill)
- Runtime debugging (use **debug** skill)

## Purpose
- Security review for code, APIs, apps.
- Detect vulnerabilities: injection, auth failures, secrets leakage, weak crypto, open redirects.
- Provide checklist to assure robust authentication & authorization boundaries.

## When to use
User triggers:
- "security review this PR/service"
- "does this code leak secrets?"
- "add security checklist"
- "check authN/Z"

## Security checklist (core)
| Area | Check | Example risk |
|------|--------|------------|
| Auth | JWT/OAuth enforced on protected routes | Missing auth on /admin endpoints |
| Inputs | Sanitize & validate all user input | XSS via unescaped HTML |
| Secrets | No plaintext credentials in code | API keys hardcoded in files |
| Injection | Use prepared statements, ORM (no SQL literals) | SQL injection: /login?id=1 OR 1=1 |
| Headers | Security headers set (CORS, CSP, etc.) | Missing Content-Security-Policy |
| Logs | Never log PII, tokens, or credentials | SSN or API keys in logs |

## Review policy
- ✅ All new PRs ≥ 2 reviewers
- Require security sign-off for infra changes or new endpoints
- Rotate secrets on infra change