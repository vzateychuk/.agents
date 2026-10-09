# Support ticket example

**Title:** API returns 500 on POST /users in production

**Summary**
Production API returns HTTP 500 for all POST /users requests. New signups blocked since 14:20 UTC.

**Steps to Reproduce**
1. Send POST /users with a valid JSON body.
2. Observe the response.

**Expected Behavior**
HTTP 201 with the created user object.

**Actual Behavior**
HTTP 500 with `trace_id` in the body.

**Environment**
- Service: user-service
- Region: eu-west-1
- Build: v2.14.3

**Severity**
Critical: blocks all work, no workaround.

**Workaround**
None.
