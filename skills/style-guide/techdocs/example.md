# Tech Docs Examples — Structured & Precise

## Example 1: Runbook snippet

# Restart the API service

## Prepare access
- SSH access to the staging host.
- Access to the `ops` namespace in Kubernetes.

## Restart the deployment

1. Connect to the staging host:
   ```bash
   ssh staging.internal
   ```

2. Restart the API deployment:
   ```bash
   kubectl rollout restart deployment/api -n ops
   ```

3. Verify the rollout:
   ```bash
   kubectl rollout status deployment/api -n ops
   ```

## Verify the service is healthy
- The API responds with HTTP 200 on `/healthz`.
- Logs show no errors for 5 minutes.

---

## Example 2: API reference snippet

# GET /users/{id}

## Return a user by ID
Returns the user with the specified ID.

## Accept these parameters
- `id` (path, required): the user ID.

## Interpret the response
- `200 OK`: user object.
- `404 Not Found`: user does not exist.

---

## Example 3: Troubleshooting snippet

# Configure git-proxy behind a corporate NTLM proxy

**Target scenarios:** developer workstations and internal pods

## Failure 1: NTLM proxy authentication

**Problem**
`git-proxy` cannot reach `github.com` through the corporate web proxy.

**Result**
```
HTTP 407 Proxy Authentication Required
```

**Root cause**
The proxy requires NTLM (NT LAN Manager) on CONNECT. Common Node.js proxy agents skip that handshake, so the connection stops before TLS (transport layer security) begins.

## Verify the fix
1. Start the proxy:
   ```bash
   npm run proxy
   ```
2. Confirm `curl` through the local proxy returns HTTP 200 from `github.com`.
