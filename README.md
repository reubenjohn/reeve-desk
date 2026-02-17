# Reeve Desk

Welcome to your **Reeve Desk** - the transparent, editable workspace where Reeve (your AI Chief of Staff) stores all knowledge about you.

## What is the Desk?

The Desk is a collaborative workspace between you and Reeve. Everything Reeve knows about you lives here in plain Markdown files. There are no hidden databases, no black-box algorithms - just transparent, human-readable text files you can edit anytime.

## Directory Structure

```
reeve_desk/
├── README.md              ← You are here
├── CLAUDE.md              ← Reeve's identity & operating instructions
├── .claude/skills/        ← Reeve's workflow skills (invocable with /skill-name)
│
├── Goals/                 ← Your North Star (long-term objectives)
├── Responsibilities/      ← Your Operational Manual (recurring duties)
├── Preferences/           ← Your User Manual (how you want Reeve to behave)
├── Tasks/                 ← Discrete action items with deadlines
│
└── Knowledge/             ← Everything Reeve "knows"
    ├── Diary/             ← Activity logs, patterns, investigations
    │   ├── YYYY-MM/       ← Monthly folders for daily logs
    │   ├── Investigations/ ← Deep-dive research sessions
    │   ├── Patterns/      ← Recurring behavioral patterns
    │   └── Archive/       ← Old monthly roll-ups
    ├── Infrastructure/    ← MCP servers, health checks, runbooks
    │   └── Runbooks/      ← Per-service troubleshooting guides
    └── Relationships/     ← People, contacts, interaction tracking
```

## Quick Start

### 1. Understand How Reeve Works

Read these files to understand Reeve's operating model:

1. **[CLAUDE.md](CLAUDE.md)** - Reeve's core identity, decision-making framework, and pulse workflow
2. **`.claude/skills/`** - Reeve's workflow skills (auto-invoked or manual with `/skill-name`)
   - `/morning-briefing` - Daily morning briefing at 8 AM
   - `/evening-wrapup` - Daily evening wrap-up at 6 PM
   - `/emergency-response` - Handle critical/urgent events
   - `/schedule-followup-pulse` - Schedule follow-up pulses
   - `/goal-check` - Weekly goal review (manual-only)
   - `/diary-log` - Log activities to Diary

### 2. Tell Reeve About Yourself

Fill in these template files with your information:

1. **[Goals/Goals.md](Goals/Goals.md)** - What are you trying to achieve? (3-5 major objectives)
2. **[Responsibilities/Responsibilities.md](Responsibilities/Responsibilities.md)** - What recurring duties do you have?
3. **[Preferences/Preferences.md](Preferences/Preferences.md)** - How should Reeve communicate with you?

### 3. Start Using Reeve

Once you've personalized the Desk:

1. **Ensure reeve-bot is configured** to point to this directory (default: `~/reeve_desk`)
2. **Complete reeve-bot Phase 5+** (Daemon, API, integrations)
3. **Test the integration** by scheduling a test pulse
4. **Iterate** - adjust files based on how Reeve behaves

## Key Principles

### 1. The "Glass Box" - Complete Transparency

**Traditional AI assistants are "black boxes"** - you don't know why they make decisions.

**Reeve is a "glass box"** - every preference, every goal, every decision rationale is visible in plaintext files you can edit.

**Example:**
```
Why did Reeve decline that 8 AM meeting?
→ Check Preferences/Preferences.md: "No meetings before 9 AM"
→ Don't like that rule? Edit the file or delete the line.
```

### 2. The "Push" Paradigm - Proactive, Not Reactive

**Traditional assistants wait for you to ask.**

**Reeve anticipates needs and initiates conversations:**
- Checks flight status before your departure and notifies you of delays
- Notices you haven't exercised in 5 days and suggests a workout
- Sees a snowstorm coming to your favorite ski resort and proposes a trip

**How it works:**
- Reeve wakes up on three types of pulses:
  - **Periodic pulses** (automatic, every hour on the hour)
  - **Aperiodic pulses** (Reeve schedules these for non-hour times using `schedule_pulse()`)
  - **Event-triggered pulses** (external events like Telegram messages)
- When a pulse fires, Reeve reads the Desk and takes action
- You're only interrupted when something truly requires your attention

For the full pulse workflow, see [CLAUDE.md](CLAUDE.md) § Workflow for Each Pulse.

### 3. Edit Anything, Anytime

**This is YOUR workspace.** Feel free to:
- Edit any file to change Reeve's behavior
- Reorganize directories
- Delete sections that don't apply
- Add new files for specialized preferences
- Evolve the structure over time

**Reeve will adapt to whatever you create.**

## What to Edit First

### For Minimal Setup (10 minutes):

1. **Goals/Goals.md** - Add 1-3 current goals (examples provided)
2. **Preferences/Preferences.md** - Set notification times and DND hours
3. **Responsibilities/Responsibilities.md** - Add morning/evening routines

### For Full Setup (30-60 minutes):

- Complete all sections in Goals, Responsibilities, and Preferences
- Add detailed communication rules and calendar preferences
- Define priority frameworks

## How Reeve Uses the Desk

Each time Reeve wakes up on a pulse, it reads your Goals, Responsibilities, Preferences, and recent Diary entries to understand your context — then takes action (notifications, scheduling, logging). For the detailed workflow, see [CLAUDE.md](CLAUDE.md) § Workflow for Each Pulse.

## Troubleshooting

### Reeve Isn't Behaving As Expected

1. **Check CLAUDE.md** - Does it define the behavior you want?
2. **Check Preferences/Preferences.md** - Is there a rule causing this?
3. **Read Knowledge/Diary/** - Look at recent logs to understand reasoning
4. **Check Knowledge/Infrastructure/** - Is an MCP server down?
5. **Edit the relevant file** to change the behavior

### Infrastructure Issues

See [Knowledge/Infrastructure/README.md](Knowledge/Infrastructure/README.md) for MCP health checks and per-service runbooks.

## File Editing Tips

All Desk files use standard Markdown. Edit with any text editor — Reeve reads them directly from the filesystem.

### Version Control

Changes are tracked with git automatically by Reeve. You can also commit manually:

```bash
cd ~/reeve_desk
git add .
git commit -m "Updated preferences: added DND hours"
```

## Privacy & Security

### What's Stored Here

- Your goals and priorities (plaintext)
- Your preferences (plaintext)
- Reeve's activity logs (plaintext)

**NOT stored here:**
- Passwords or API keys (those go in `.env` files in reeve-bot/)
- Sensitive data (you control what goes in these files)

### Who Can Access This

- **You** - Full read/write access
- **Reeve** - Read/write access (for Knowledge/Diary/, Tasks/)
- **Anyone with filesystem access** - These are plaintext files

## Further Reading

- **[CLAUDE.md](CLAUDE.md)** - Deep dive into Reeve's operating principles
- **[Knowledge/README.md](Knowledge/README.md)** - Index of all knowledge (Diary, Infrastructure, Relationships)
- **[Knowledge/Diary/README.md](Knowledge/Diary/README.md)** - How Reeve's memory system works
- **[Preferences/Preferences.md](Preferences/Preferences.md)** - Example preferences with detailed explanations

---

**Created:** 2026-01-20
**Updated:** 2026-02-17
**Version:** 2.0
**Maintainer:** You (the user)

Remember: This is YOUR workspace. Shape it however makes sense to you. Reeve will adapt.
