---
name: mcp-diagnostics
description: Health check for MCP server dependencies (WhatsApp bridge, Google Workspace, etc.). Auto-invoke during hourly pulses to detect silent failures early. Also invoke manually when MCP tools seem broken.
disable-model-invocation: false
---

# MCP Diagnostics

Run health checks on MCP server dependencies to detect silent failures.

## When to Run

- **Every hourly pulse**: Quick checks only (silent unless something is wrong)
- **On-demand**: When MCP tools return errors, stale data, or auth failures
- **After restarts**: Verify services recovered

## Quick Check (Hourly Pulses)

Run silently. Only notify the user if something is degraded or down.

| MCP Server | Quick Check | Guide |
|------------|-------------|-------|
| WhatsApp | Container running + DB fresh | [whatsapp.md](whatsapp.md) |

<!--
ONBOARDING: Add rows for each MCP server you use. Create a corresponding
<mcp-name>.md diagnostic guide in this directory.
Example: | Google Workspace | List calendars succeeds | [google-workspace.md](google-workspace.md) |
-->

## Full Diagnostic (On-Demand)

When invoked manually, run the full suite from each MCP's guide. Also check:

```bash
# Which MCP servers are configured?
cat ~/.config/claude-code/mcp_config.json   # Global
cat [YOUR_DESK_PATH]/.mcp.json              # Project-level
```

## Notification Policy

| Status | Action |
|--------|--------|
| **Healthy** | Silent — log to Diary only if running full diagnostic |
| **Degraded** (auto-remediated) | Normal priority notification |
| **Failed** (can't fix) | Critical priority notification |

## Adding New MCP Checks

Create a new `<mcp-name>.md` in this directory following the pattern:
1. Quick check (process alive + basic connectivity test)
2. Common failures with decision matrix
3. Troubleshooting guide for known issues
4. Auto-remediation steps where possible

## History

<!--
ONBOARDING: Log outages and incidents here to build institutional memory.
Example:
- **2026-02-04**: First WhatsApp bridge outage (25 hours unnoticed)
-->
