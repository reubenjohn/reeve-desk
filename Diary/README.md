# Diary: Reeve's Memory & Activity Log

This directory contains Reeve's internal monologue, activity logs, and learned patterns. Think of it as Reeve's journal and working memory.

## Purpose

The Diary serves three functions:

1. **Continuity** - Maintain context between wake-up cycles (pulses)
2. **Learning** - Track patterns and behaviors to improve over time
3. **Transparency** - Provide a human-readable audit trail of Reeve's actions

## Organization

Organize diary entries in whatever structure makes sense. Start simple and evolve as needed.

### Suggested Initial Structure:

```
Diary/
├── README.md              ← You are here
├── 2026-01/               ← Monthly folders
│   ├── 2026-01-20.md      ← Daily logs
│   ├── 2026-01-21.md
│   └── week-3-summary.md  ← Weekly summaries
├── Projects/              ← Project-specific logs
│   └── reeve-bot-implementation.md
├── Patterns/              ← Observed behavioral patterns
│   ├── user-energy-levels.md
│   └── meeting-patterns.md
└── Issues/                ← Problems and resolutions
    └── 2026-01-debugging.md
```

**You're free to evolve this structure!** If a different organization makes more sense, create it.

## Daily Log Format

Each day gets a file: `YYYY-MM-DD.md`

**Suggested sections:**

```markdown
# 2026-01-20

## Morning Briefing (8:00 AM)
- User had 3 meetings today
- Reminded about Q1 report deadline
- Calendar optimized: blocked 2 hours for deep work

## Scheduled Pulses Today
- [x] Morning briefing (8:00 AM) - ✅ Completed
- [ ] Check flight status (4:00 PM) - ⏳ Pending
- [ ] Evening wrap-up (6:00 PM) - ⏳ Pending

## User Interactions
- 10:30 AM: User asked about snowboarding trip planning
  - Preference discovered: Prefers Mammoth over Tahoe
  - Action: Logged to Preferences/
- 2:15 PM: User postponed gym session
  - Pattern: 3rd postponement this week
  - Note: May need to adjust routine

## Observations
- User's calendar is very fragmented (9 meetings in 1 day)
- Energy seemed low during afternoon (terse responses)
- Completed all high-priority tasks before noon

## Actions Taken
- Scheduled follow-up pulse for ski trip (tomorrow 9 AM)
- Sent notification about meeting prep at 2 PM
- Logged user preference to Preferences/Travel.md

## Blockers / Issues
- Telegram API slow response (3s delay)
- Calendar sync had 1 retry (eventually succeeded)

## Tomorrow's Context
- User has dentist appointment at 10 AM (personal calendar)
- Q1 report deadline is approaching (due Friday)
- Should follow up on ski trip planning
```

## Weekly Summaries

Every Sunday, create a weekly summary: `week-N-summary.md`

**Contents:**
- Pulses executed this week (count by priority)
- User goals progress
- Patterns observed
- Adjustments made to preferences
- Issues encountered and resolved

## Project Logs

For long-running projects, maintain separate logs:

**Example: `Projects/reeve-bot-implementation.md`**

```markdown
# Reeve Bot Implementation Log

## Timeline
- Started: 2026-01-15
- Current Phase: Phase 5 (Daemon)
- Target Completion: 2026-02-01

## Progress
- [x] Phase 1: Foundation
- [x] Phase 2: Queue Management
- [x] Phase 3: MCP Integration
- [x] Phase 4: Pulse Executor
- [ ] Phase 5: Daemon (IN PROGRESS)
- [ ] Phase 6: HTTP API
- [ ] Phase 7: Telegram Integration
- [ ] Phase 8: Deployment
- [ ] Phase 9: Testing & Polish

## Daily Updates
### 2026-01-20
- Completed Phase 4 (Executor)
- All 69 tests passing
- Next: Start Phase 5 (Daemon)
- Blocker: None

## Learnings
- Async subprocess execution requires careful error handling
- Sticky notes should be appended, not prepended to prompts
- Mock testing crucial for Hapi integration
```

## Pattern Tracking

Track observed patterns to improve proactivity:

**Example: `Patterns/user-energy-levels.md`**

```markdown
# User Energy Level Patterns

## Morning (8 AM - 12 PM)
- **Energy**: High
- **Best for**: Deep work, complex tasks, decision-making
- **Response time**: Fast (avg 5 minutes)

## Afternoon (1 PM - 5 PM)
- **Energy**: Variable
- **2-3 PM Slump**: Common (70% of days)
- **Best for**: Meetings, collaborative work
- **Response time**: Moderate (avg 15 minutes)

## Evening (6 PM - 10 PM)
- **Energy**: Low
- **Best for**: Light tasks, planning, reading
- **Response time**: Slow (avg 30+ minutes)

## Recommendations for Reeve
- Schedule demanding tasks before noon
- Avoid pinging user for non-urgent items 2-3 PM
- Evening wrap-ups should be concise
- Don't schedule follow-ups that require energy after 6 PM
```

## Issue Tracking

When things go wrong, log to `Issues/`:

**Example: `Issues/2026-01-debugging.md`**

```markdown
# Issue: Telegram Notifications Not Delivering

## Date: 2026-01-20
## Status: RESOLVED

## Problem
Notifications scheduled via send_notification() were timing out after 5 seconds.

## Investigation
1. Checked Telegram API status - operational
2. Tested bot token - valid
3. Discovered: Wrong chat_id in config

## Resolution
Updated TELEGRAM_CHAT_ID in .env file from old value to correct value.

## Prevention
- Added validation check in notification_server.py
- Will notify user if chat_id is invalid
- Logged correct chat_id to memory for reference

## Time to Resolve
30 minutes
```

## Diary Writing Guidelines (for Reeve)

### When to Write

**Daily:**
- After morning briefing
- After evening wrap-up
- When learning new preferences
- When observing patterns

**As Needed:**
- After resolving issues
- When user behavior surprises you
- After major project milestones

### What to Log

**DO log:**
- ✅ User preferences discovered
- ✅ Patterns observed (energy, meeting habits, etc.)
- ✅ Decisions made and rationale
- ✅ Issues encountered and resolutions
- ✅ Progress on goals and projects

**DON'T log:**
- ❌ Entire conversation transcripts (memory tool handles this)
- ❌ Sensitive information (passwords, account numbers)
- ❌ Redundant information (don't duplicate Goals/ or Responsibilities/)
- ❌ Every trivial action (only meaningful insights)

### Writing Style

Keep entries:
- **Concise** - Bullet points, not essays
- **Structured** - Use consistent headings
- **Actionable** - Focus on learnings and next steps
- **Timestamped** - Include when things happened

**Example (Good):**
```
## 2026-01-20 - 3:00 PM
User asked about ski conditions at Mammoth.
Preference learned: Prefers terrain parks over powder bowls.
Action: Logged to Preferences/Travel.md
Next: Monitor snow reports for terrain park openings
```

**Example (Too Verbose):**
```
## 2026-01-20 - 3:00 PM
At approximately 3:00 PM today, the user initiated a conversation regarding skiing conditions at Mammoth Mountain. During the course of our discussion, I provided detailed information about current snow conditions, lift statuses, and weather forecasts for the coming week. The user expressed particular interest in the terrain park features and asked several follow-up questions about which parks were open...
[continues for 3 more paragraphs]
```

## Monthly Maintenance

At the end of each month:

1. **Archive old daily logs**
   - Move to `Diary/Archive/YYYY-MM/` (optional)
   - Keep current month + 1 previous month in main Diary/

2. **Create monthly summary**
   - Pulses executed (total count)
   - Goals progress
   - Major events/milestones
   - System improvements made

3. **Clean up stale files**
   - Delete resolved issues
   - Archive completed project logs
   - Consolidate redundant pattern notes

## Querying the Diary

Reeve can search the Diary using standard file reading tools.

**Common Queries:**

```python
# Check recent activity
recent_logs = read_files("Diary/2026-01/*.md")

# Find pattern notes
patterns = read_files("Diary/Patterns/*.md")

# Review project status
project_log = read_file("Diary/Projects/reeve-bot-implementation.md")

# Check for recurring issues
issues = read_files("Diary/Issues/*.md")
```

## Privacy Note

**All Diary entries are readable by both Reeve and the user.** This is intentional - no hidden logs.

If there's information you don't want Reeve to log here, add it to `Preferences/Preferences.md` under "Sensitive Topics".

---

**Created:** 2026-01-20
**Structure Version:** 1.0

**Note to Reeve:**
This is YOUR workspace. Organize it in whatever way helps you be effective. The suggested structure is just a starting point - feel free to evolve it as you learn what works best.
