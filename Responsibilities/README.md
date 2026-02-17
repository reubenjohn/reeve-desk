# Responsibility Management Guidelines

How Reeve should handle Responsibilities/ tracking and reminders.

## Daily Check Pattern
1. Read Responsibilities/ every morning during briefing
2. Check if any recurring tasks are due today
3. Remind user of daily responsibilities
4. Check active projects for pending actions
5. Ask about blockers if project hasn't progressed in 3+ days
6. Commit daily Diary entries during evening wind-down

## Weekly Check Pattern
1. On Monday morning: Deliver week planning summary
2. On Friday evening: Deliver weekly review
3. Check for overdue weekly tasks
4. Suggest rescheduling if user is behind
5. Commit all week's changes on Friday with summary

## Monthly Check Pattern
1. Last day of month: Generate monthly report
2. Summarize all project progress
3. Check for stale projects (no updates in 2+ weeks)
4. Suggest archiving completed projects
5. Commit monthly review and all changes

## Commit Rules

Commit immediately after updating Goals/, Preferences/, or Responsibilities/. See CLAUDE.md § Task Completion Checklist for the full protocol.

## When a Responsibility is Missed
```
DON'T: Nag or guilt-trip
DO: Observe the pattern
- If missed once: Just remind next day
- If missed 2-3 times: Ask if it should be rescheduled or deprioritized
- If missed 5+ times: Suggest pausing or removing it
```

**Example:**
```
User misses "Daily Spanish Lesson" 5 days straight

Reeve: "I noticed 'Daily Spanish Lesson' hasn't happened this week. Should we:
1. Move it to weekends only?
2. Pause it until March?
3. Remove it from daily responsibilities?

No judgment - just want to align this with your actual bandwidth."
```

## Integration with Goals

Each responsibility should ideally connect to a goal in Goals/Goals.md.

**Example Connections:**
- "Morning run" → Goal: "Complete marathon by June"
- "Weekly code review" → Goal: "Ship project milestone by target date"
- "Daily Spanish lesson" → Goal: "Achieve conversational fluency by year-end"

**For orphaned responsibilities (no clear goal connection):**
- Question if they're still valuable
- Consider removing or archiving
- Ask user: "Why are we doing this?"

## Related

- [Goals/Goals.md](../Goals/Goals.md) — Each responsibility should connect to a goal
- [Tasks/Open.md](../Tasks/Open.md) — Discrete action items (vs recurring responsibilities)
- [Knowledge/Infrastructure/](../Knowledge/Infrastructure/README.md) — Infrastructure projects and MCP management
- For daily responsibility reminders, see `morning-briefing` skill
- For logging completed responsibilities, see `diary-log` skill
