# Responsibilities: Your Operational Manual

This file defines your recurring duties and active projects - the "what" you need to maintain regularly.

**How to use this file:**
- List all recurring commitments (daily, weekly, monthly)
- Track active projects and their current status
- Update regularly as projects start, pause, or complete
- Reeve will check this daily to ensure nothing falls through the cracks

**Format:**
- **Daily Responsibilities** - Must happen every day
- **Weekly Responsibilities** - Happens on specific days each week
- **Monthly Responsibilities** - Happens on specific dates each month
- **Active Projects** - Ongoing work with defined scope

---

## Daily Responsibilities

### Morning Routine
**Time:** 8:00 AM
**What:**
- Morning briefing (delivered by Reeve)
- Review calendar for the day
- Check priority emails and messages
- Identify top 3 priorities for the day

**Reeve's Role:**
- Deliver briefing via Telegram
- Summarize calendar and urgent items
- Suggest focus areas based on Goals/

---

### Evening Wrap-Up
**Time:** 6:00 PM
**What:**
- Review what was accomplished today
- Preview tomorrow's schedule
- Note any blockers or concerns

**Reeve's Role:**
- Celebrate completed tasks
- Prepare tomorrow's context
- Log daily summary to Diary/

---

### [Your Daily Task]
**Time:** [When]
**What:** [Description]
**Reeve's Role:** [How Reeve should support this]

---

## Weekly Responsibilities

### Monday: Week Planning
**Time:** 9:00 AM
**What:**
- Review upcoming week's calendar
- Identify potential conflicts or gaps
- Block time for deep work sessions
- Set weekly priorities aligned with Goals/

**Reeve's Role:**
- Summarize week ahead
- Suggest calendar optimizations
- Identify goal-aligned priorities

---

### Friday: Weekly Review
**Time:** 5:00 PM
**What:**
- Review week's accomplishments
- Identify what's rolling over to next week
- Capture learnings or insights
- Plan weekend commitments (if any)

**Reeve's Role:**
- Compile week's activities from Diary/
- Assess progress on active projects
- Suggest adjustments for next week

---

### [Your Weekly Task]
**Day:** [Monday/Tuesday/etc.]
**Time:** [When]
**What:** [Description]
**Reeve's Role:** [How Reeve should support this]

---

## Monthly Responsibilities

### Month-End Review
**When:** Last day of each month
**What:**
- Review Goals/ for progress
- Update project statuses
- Financial check (if applicable)
- Archive old Diary/ entries

**Reeve's Role:**
- Generate monthly summary report
- Highlight goal progress
- Suggest goal updates or new priorities

---

### [Your Monthly Task]
**When:** [Specific date or "Last day of month"]
**What:** [Description]
**Reeve's Role:** [How Reeve should support this]

---

## Active Projects

### Project: Reeve Bot Implementation
**Status:** 🔄 In Progress
**Priority:** High
**Timeline:** January 2026 - February 2026

**Objective:**
Complete Pulse Queue system implementation (Phases 1-9) and deploy Reeve as a fully autonomous proactive assistant.

**Current Phase:**
Phase 4 complete (Executor). Starting Phase 5 (Daemon).

**Next Actions:**
- [ ] Implement PulseDaemon class with scheduler loop
- [ ] Create comprehensive logging system
- [ ] Test end-to-end pulse execution
- [ ] Set up daemon for Phase 6 (HTTP API)

**Blockers:** None currently

**Reeve's Role:**
- Remind about implementation milestones
- Track phase completion in Diary/
- Celebrate phase completions

---

### Project: [Your Project Name]
**Status:** 🎯 Active / ⏸️ Paused / ✅ Complete / ❌ Cancelled
**Priority:** High / Medium / Low
**Timeline:** [Start Date] - [Target End Date]

**Objective:**
[What you're trying to achieve with this project]

**Current Phase:**
[Where you are now]

**Next Actions:**
- [ ] Action item 1
- [ ] Action item 2
- [ ] Action item 3

**Blockers:**
[What's preventing progress, if anything]

**Reeve's Role:**
[How Reeve should support this project - reminders, summaries, etc.]

---

## Paused Responsibilities

### [Paused Task/Project]
**Paused On:** [Date]
**Reason:** [Why it's on hold]
**Resume When:** [Condition or date]

---

## Completed Projects (Archive)

### ✅ Project: [Name] - Completed [Date]
**What was delivered:**
[Brief summary]

**Key learnings:**
[Insights from the project]

---

## Responsibility Management Guidelines

**For Reeve:**

### Daily Check Pattern
```
1. Read this file every morning during briefing
2. Check if any recurring tasks are due today
3. Remind user of daily responsibilities
4. Check active projects for pending actions
5. Ask about blockers if project hasn't progressed in 3+ days
```

### Weekly Check Pattern
```
1. On Monday morning: Deliver week planning summary
2. On Friday evening: Deliver weekly review
3. Check for overdue weekly tasks
4. Suggest rescheduling if user is behind
```

### Monthly Check Pattern
```
1. Last day of month: Generate monthly report
2. Summarize all project progress
3. Check for stale projects (no updates in 2+ weeks)
4. Suggest archiving completed projects
```

### When a Responsibility is Missed
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

---

## Integration with Goals

Each responsibility should ideally connect to a goal in [Goals/Goals.md](../Goals/Goals.md).

**Example Connections:**
- "Morning run" → Goal: "Complete marathon by June"
- "Weekly code review" → Goal: "Ship Reeve MVP by Feb 1"
- "Daily Spanish lesson" → Goal: "Achieve conversational fluency by year-end"

**For orphaned responsibilities (no clear goal connection):**
- Question if they're still valuable
- Consider removing or archiving
- Ask user: "Why are we doing this?"

---

**Last Updated:** 2026-01-20
**Next Review:** Weekly (every Friday)

**Notes for Reeve:**
- Be flexible - life happens, schedules change
- Adapt to user's energy (if they're overwhelmed, ease off)
- Celebrate consistency, not perfection
- Always connect tasks to Goals/ when giving reminders
