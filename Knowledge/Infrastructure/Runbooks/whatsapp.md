# WhatsApp Bridge Runbook

## Quick Diagnosis

```bash
# 1. Is the container running?
docker ps --filter "name=whatsapp-bridge" --format "{{.Status}}"
# Expected: "Up X hours/days"

# 2. Is the database fresh? (stale = bridge crashed silently)
stat -c %Y [YOUR_WHATSAPP_BRIDGE_PATH]/store/messages.db
# Compare against current time. Stale threshold: >2 hours behind.
```

## Decision Tree

| Container | DB Fresh | Action |
|-----------|----------|--------|
| Running | Yes | **Healthy** — log silently |
| Running | No | Bridge hung — restart container, notify user |
| Stopped | — | `docker start whatsapp-bridge`, notify user |

**Auto-remediation:** If stopped or hung, restart:
```bash
docker restart whatsapp-bridge
```
Verify it came back up. If restart fails, notify user as **Critical**.

## Full Diagnostic

```bash
# Container status with restart count
docker ps -a --filter "name=whatsapp-bridge" --format "table {{.Names}}\t{{.Status}}\t{{.RestartCount}}"

# Restart policy (should be "unless-stopped")
docker inspect whatsapp-bridge --format '{{.HostConfig.RestartPolicy.Name}}'

# Database sizes and last modified times
ls -lh [YOUR_WHATSAPP_BRIDGE_PATH]/store/*.db

# Recent container logs (look for errors)
docker logs --tail 50 whatsapp-bridge

# Test MCP connectivity — try listing recent chats
# Use list_chats() MCP tool and check if results are current
```

## Common Failures

### Silent bridge crashes
The bridge can stop syncing messages without the container going down. The DB freshness check catches this — if `messages.db` hasn't been modified in >2 hours during waking hours, the bridge is likely hung.

### Container exits without restart
Ensure the container has a restart policy: `--restart unless-stopped`.

## Related

- [../README.md](../README.md) — Infrastructure overview and health check workflow
