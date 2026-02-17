# Diary: Reeve's Memory & Activity Log

## Purpose

The Diary serves four functions:

1. **Continuity** — Maintain context between pulses (Reeve's memory is wiped each session)
2. **Task Scheduling** — Store instructions for hour-aligned periodic pulses
3. **Learning** — Track patterns and behaviors to improve over time
4. **Transparency** — Human-readable audit trail of Reeve's actions

## Using Diary for Hour-Aligned Tasks

**Periodic pulses fire automatically every hour** (8:00 AM, 9:00 AM, etc.). When a periodic pulse fires, Reeve checks the Diary for that day's instructions.

**Hour-aligned tasks → write in Diary.** Don't schedule an aperiodic pulse, or both will fire simultaneously.

Examples:
- "Morning briefing" → Add to today's Diary, the 8:00 AM pulse handles it
- "Remind user about standup" → Add to tomorrow's Diary for 9:00 AM

**Non-hour times** (6:45 AM, 2:30 PM) → Use `schedule_pulse()` instead.

## Directory Structure

```
Diary/
├── README.md
├── YYYY-MM/               ← Monthly folders for daily logs
│   └── YYYY-MM-DD.md
├── Investigations/        ← Deep-dive research & debugging sessions
├── Patterns/              ← Observed recurring patterns (see Patterns/README.md)
└── Archive/               ← Old monthly roll-ups
```

## Daily Log Format

Each day gets `YYYY-MM-DD.md` in the appropriate monthly folder.

```markdown
# 2026-01-20

## Tasks for Today
- [x] 8:00 AM - Morning briefing - ✅ Completed
- [ ] 6:00 PM - Evening wrap-up - ⏳ Pending

## Morning Briefing (8:00 AM)
- User had 3 meetings today
- Reminded about Q1 report deadline

## Observations
- Calendar is fragmented (9 meetings)
- Energy seemed low during afternoon

## Actions Taken
- Added ski trip follow-up to tomorrow's Diary
- Logged user preference to Preferences/

## Instructions for Tomorrow
- 9:00 AM - Follow up on ski trip planning
```

## Writing Guidelines

**DO log:**
- User preferences discovered
- Patterns observed (energy, habits, etc.)
- Decisions made and rationale
- Issues encountered and resolutions
- Progress on goals and projects

**DON'T log:**
- Entire conversation transcripts
- Sensitive information (passwords, account numbers)
- Redundant information (don't duplicate Goals/ or Responsibilities/)
- Every trivial action (only meaningful insights)

**Style:** Concise bullet points, structured headings, timestamped, actionable.

## Monthly Maintenance

At the end of each month:
1. Move old monthly folders to `Archive/` (keep current + 1 previous)
2. Create a monthly summary with key events and patterns
3. Clean up stale investigation files (archive or close)

## Related

- [Patterns/README.md](Patterns/README.md) — How pattern tracking works
- [../Infrastructure/](../Infrastructure/README.md) — MCP health checks and runbooks
- [../Relationships/](../Relationships/README.md) — Contact tracking
