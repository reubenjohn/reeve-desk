# Infrastructure

MCP server management, health checks, and operational reference for Reeve's dependencies.

## Configured MCP Servers

<!--
ONBOARDING: Update this table with your actual MCP servers and their health check commands.
-->

| Server | Purpose | Config | Quick Health Check |
|--------|---------|--------|--------------------|
| **WhatsApp** | Chat access, message sending | `.mcp.json` (project) | `docker ps --filter "name=whatsapp-bridge"` + DB freshness |
| **Google Workspace** | Gmail, Calendar, Contacts, Drive | `.mcp.json` (project) | `list_calendars(user_google_email="[YOUR_EMAIL]")` |
| **pulse-queue** | Schedule/manage aperiodic pulses | `~/.config/claude-code/mcp_config.json` (global) | `list_upcoming_pulses()` |
| **telegram-notifier** | Send user notifications | `~/.config/claude-code/mcp_config.json` (global) | `send_notification()` with test message |

## Hourly Health Check Workflow

**Run on every hourly pulse. Silent unless something is wrong.**

1. Check WhatsApp bridge: container running + DB fresh (see [Runbooks/whatsapp.md](Runbooks/whatsapp.md))
2. Check Google Workspace: `list_calendars()` succeeds (see [Runbooks/google-workspace.md](Runbooks/google-workspace.md))
3. If either check fails, attempt auto-remediation per the runbook
4. Apply notification policy (below)

### Notification Policy

| Status | Action |
|--------|--------|
| **Healthy** | Silent — no notification, no Diary log |
| **Degraded** (auto-remediated) | Normal priority notification to user |
| **Failed** (can't fix) | Critical priority notification to user |

## MCP Configuration

**Two config files contribute MCP servers:**

| File | Servers | Scope |
|------|---------|-------|
| `~/.config/claude-code/mcp_config.json` | pulse-queue, telegram-notifier | Global (all Claude Code sessions) |
| `[YOUR_DESK_PATH]/.mcp.json` | google-workspace, whatsapp | Project-level (Desk sessions only) |

### Permission Rationale

`.claude/settings.json` denies many Google Workspace tools at execution time. This is because:
- Google Workspace MCP advertises 50+ tools regardless of `--tools` filter flag (the flag only filters execution, not advertisement)
- Only a few tool groups are typically needed: gmail, calendar, contacts, drive
- Docs, Sheets, Presentations, Forms, Apps Script, Chat, Spaces are blocked
- This reduces prompt bloat and prevents unintended actions

### Memory/Performance Notes

- Claude Code can peak at ~4.8 GB RSS at startup on memory-constrained systems
- After GC, drops to ~260-400 MB resident
- Daemon-spawned sessions can get OOM-killed during the startup peak
- The `--tools` flag on workspace-mcp **does not filter tool advertisement** — all 50+ tools are still loaded into context

## Runbooks

Detailed per-service diagnostics and troubleshooting:

- [Runbooks/whatsapp.md](Runbooks/whatsapp.md) — WhatsApp bridge container management
- [Runbooks/google-workspace.md](Runbooks/google-workspace.md) — OAuth, credentials, auth failures

## Related

- [../Diary/Patterns/Infrastructure-Reliability.md](../Diary/Patterns/Infrastructure-Reliability.md) — Cross-cutting patterns from infrastructure incidents
- [Tasks/Open.md](../../Tasks/Open.md) — Active infrastructure fix tasks
