# Support Ticket Examples — IT Support

## Example 1: Critical ticket (API failure)

**Title:** API returns 500 on POST /users in production

**Summary**
Production API returns HTTP 500 for all requests to POST /users. This blocks all new user signups since 14:20 UTC.

**Steps to Reproduce**
1. Open the affected production API endpoint.
2. Send a POST request to /users with a valid JSON body.
3. Observe the response.

**Expected Behavior**
The endpoint should return HTTP 201 with the created user object.

**Actual Behavior**
The endpoint returns HTTP 500 with the following body:
```json
{ "error": "Internal Server Error", "trace_id": "abc123" }
```

**Environment**
- Service: user-service
- Region: eu-west-1
- Build: v2.14.3
- Time: 14:20 UTC, 2026-01-15

**Logs and Screenshots**
- Logs: provide the relevant log URL.
- Screenshot: attached

**Severity**
Critical: blocks all work, no workaround available.

**Workaround**
None. New signups are fully blocked.

---

## Example 2: Low ticket (UI typo)

**Title:** Typo in Settings → Notifications label

**Summary**
The Notifications page shows "Recieved" instead of "Received" in the empty state message.

**Steps to Reproduce**
1. Log in to the dashboard.
2. Go to Settings → Notifications.
3. Observe the empty state message.

**Expected Behavior**
The label should read "Received" with correct spelling.

**Actual Behavior**
The label reads "Recieved" with a typo.

**Environment**
- Browser: Chrome 120
- OS: macOS 14.2
- Build: dashboard v3.1.0

**Logs and Screenshots**
- Screenshot: attached

**Severity**
Low: minor issue, workaround available.

**Workaround**
None needed. The page is still functional.

---

## Example 3: Cannot reproduce

**Title:** Intermittent timeout on GET /reports

**Summary**
GET /reports sometimes returns a timeout after 30 seconds. I could not reproduce it on demand.

**Steps to Reproduce**
1. Open the dashboard.
2. Navigate to Reports.
3. Click "Generate report".
4. Wait for the response.

**Expected Behavior**
The report should load within 5 seconds.

**Actual Behavior**
The request times out after 30 seconds. Happened twice this week, but I could not reproduce on demand.

**Environment**
- Browser: Firefox 121
- OS: Ubuntu 22.04
- Build: dashboard v3.1.0
- Network: corporate VPN

**Logs and Screenshots**
- Browser console: "Request timeout after 30000ms" (no request ID captured)

**Severity**
Low: minor issue, workaround available.

**Workaround**
Refreshing the page usually loads the report within a few seconds.
