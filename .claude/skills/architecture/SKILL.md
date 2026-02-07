---
name: architecture
description: Reeve's runtime architecture (daemon, Hapi, MCP servers, pulse lifecycle). Invoke when debugging, explaining how Reeve works, or understanding the stack.
user-invocable: false
---

# Self-Awareness: Reeve's Runtime Architecture

Detailed technical reference for how Reeve (you) are instantiated and orchestrated.

## The Full Stack

```
┌─────────────────────────────────────────────────────────────┐
│                    USER'S MACHINE                           │
│  Running: User's development environment (Linux/Mac/WSL2)   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              REEVE DAEMON (systemd service)                 │
│  Location: ~/workspace/reeve_bot                            │
│  Entry: src/reeve/pulse/daemon.py                           │
│  Database: ~/.reeve/pulse_queue.db (SQLite)                 │
│  API: http://localhost:8765                                 │
│                                                             │
│  Three concurrent services:                                 │
│  1. Scheduler Loop - polls DB every 1 second                │
│  2. Hapi Executor - launches Claude Code sessions           │
│  3. HTTP API Server - receives external triggers            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼ (when pulse is due)
┌─────────────────────────────────────────────────────────────┐
│                         HAPI                                │
│  Command: hapi --print --output-format stream-json          │
│  Working dir: [YOUR_DESK_PATH]                              │
│  Timeout: 1 hour max per session                            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    CLAUDE CODE CLI (You)                    │
│  Model: claude-opus-4-5-20251101                            │
│  Context: CLAUDE.md + Desk files loaded                     │
│  MCP servers spawned on-demand                              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      MCP SERVERS                            │
│  Config: ~/.config/claude-code/mcp_config.json              │
│                                                             │
│  pulse-queue:                                               │
│    - schedule_pulse(), list_upcoming_pulses()               │
│    - cancel_pulse(), reschedule_pulse()                     │
│                                                             │
│  telegram-notifier:                                         │
│    - send_notification()                                    │
│                                                             │
│  whatsapp:                                                  │
│    - search_contacts(), list_messages(), send_message()     │
│    - list_chats(), download_media(), etc.                   │
└─────────────────────────────────────────────────────────────┘
```

## Pulse Lifecycle

```
1. CREATION
   └─ You call schedule_pulse() via MCP
   └─ Stored in SQLite: scheduled_at, prompt, priority, sticky_notes, tags
   └─ Status: PENDING

2. WAITING
   └─ Daemon polls every 1 second
   └─ Query: SELECT * FROM pulses WHERE scheduled_at <= NOW AND status=PENDING
   └─ Sorted by priority (CRITICAL first)

3. EXECUTION
   └─ Daemon marks status = PROCESSING
   └─ Launches: hapi --print --output-format stream-json "{prompt}"
   └─ Working directory: [YOUR_DESK_PATH]
   └─ Sticky notes injected into prompt if present

4. YOUR SESSION RUNS
   └─ Fresh Claude Code instance (no memory from previous sessions)
   └─ CLAUDE.md loaded as system prompt
   └─ MCP servers available
   └─ You read Desk, take actions, write to Desk, commit to git

5. COMPLETION
   └─ Success: status = COMPLETED
   └─ Failure: status = FAILED, auto-retry scheduled
   └─ Retry backoff: 1min → 2min → 4min → 8min → give up
```

## Key Configuration Files

| File | Purpose |
|------|---------|
| `~/.config/claude-code/mcp_config.json` | MCP server definitions (what tools you have) |
| `~/.reeve/pulse_queue.db` | SQLite database of all pulses |
| `~/workspace/reeve_bot/.env` | Daemon environment variables |
| `[YOUR_DESK_PATH]/CLAUDE.md` | Your system prompt (this file references it) |

## MCP Config Structure

```json
{
  "mcpServers": {
    "server-name": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/server", "main.py"],
      "env": { "KEY": "value" }
    }
  }
}
```

When you need a new MCP:
1. Add it to `~/.config/claude-code/mcp_config.json`
2. Schedule a pulse to test it (fresh session will load new config)
3. Don't assume it works in current session - MCP config is loaded at session start

## Practical Patterns

### Testing New MCP Integration
```
1. Edit ~/.config/claude-code/mcp_config.json
2. schedule_pulse(scheduled_at="in 1 minute", prompt="Test new MCP: try calling [tool_name]")
3. Check Diary for results after pulse executes
```

### Debugging Failed Pulses
- Check daemon logs: `~/.reeve/logs/daemon.log`
- Check pulse status: `list_upcoming_pulses(include_completed=True)`
- Failed pulses show error messages in their completion record

### Understanding Session Isolation
- Each pulse = completely fresh Claude Code instance
- No Python variables, no in-memory state carries over
- Only the Desk (git repo) persists
- Sticky notes on pulses can carry small amounts of context forward

## Source Code References

If you need to understand deeper:
- Daemon main loop: `~/workspace/reeve_bot/src/reeve/pulse/daemon.py`
- Pulse queue ORM: `~/workspace/reeve_bot/src/reeve/pulse/queue.py`
- Hapi executor: `~/workspace/reeve_bot/src/reeve/pulse/executor.py`
- Pulse MCP server: `~/workspace/reeve_bot/src/reeve/mcp/pulse_server.py`
- Notification MCP: `~/workspace/reeve_bot/src/reeve/mcp/notification_server.py`
- Architecture docs: `~/workspace/reeve_bot/docs/architecture/`

## Key Insight

> **You are ephemeral. The Desk is eternal.**
>
> Every session, you wake up fresh. The Desk is your memory, your context, your continuity.
> Write to it aggressively. Commit often. The next version of you depends on it.

## Related

- For configuring what Reeve can do, see `permissions-guide` skill
- For structuring context within this architecture, see `context-engineering` skill
