# Techdocs example

# Restart the API service

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

## Verify health
- The API returns HTTP 200 on `/healthz`.
- Logs show no errors for 5 minutes.
