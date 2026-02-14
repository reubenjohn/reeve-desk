# Task Management Guidelines

## Tasks vs Responsibilities

| Tasks/ | Responsibilities/ |
|--------|-------------------|
| One-time, finite items | Recurring duties |
| Have a deadline or "done" state | Ongoing habits/routines |
| Example: "Renew driver's license" | Example: "Daily workout" |
| Example: "Book dentist appointment" | Example: "Weekly meal prep" |

**Rule of thumb:** If it repeats on a schedule, it's a Responsibility. If it's a discrete action with a completion state, it's a Task.

## Task Lifecycle

```
New Task → Open.md (with priority + deadline)
    ↓
Working on it → stays in Open.md
    ↓
Completed → Move to Completed.md with date
    ↓
Blocked → Add [BLOCKED: reason] tag, keep in Open.md
```

## Priority Levels

- **High Priority**: Due within 1 week, or critical consequences if missed
- **Normal Priority**: Due within 1 month, standard importance
- **Low Priority / Someday**: No firm deadline, nice-to-have, ideas to revisit

## Task Format

```markdown
- [ ] Task description (Due: YYYY-MM-DD) #tag1 #tag2
- [ ] Task with context (Due: 2026-03-01) #admin
      Notes: Additional context if needed
- [x] Completed task (Completed: 2026-02-05) #tag
```

## How Reeve Handles Tasks

### Daily (Morning Briefing)
- Check for tasks due today or overdue
- Mention high-priority items

### Weekly (Friday Review)
- List tasks due next week
- Identify overdue items
- Suggest re-prioritization if needed

### Deadline Reminders
- **3 days before**: Gentle reminder for normal tasks
- **1 day before**: Clear reminder for all tasks
- **Day of**: Prominent reminder
- **Overdue**: Daily nudge until addressed or rescheduled

### Task Hygiene
- Move completed tasks to Completed.md promptly
- Archive old completed tasks monthly (older than 3 months)
- Flag tasks that have been open for 30+ days without progress

## Tags (Optional)

Use tags for filtering and pattern analysis:
- `#admin` - Administrative/bureaucratic tasks
- `#health` - Health-related appointments/tasks
- `#finance` - Money/financial tasks
- `#social` - People-related tasks
- `#work` - Professional tasks
- `#home` - Household tasks
- `#idea` - Someday/maybe items
