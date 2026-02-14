---
name: daily-retrospection
description: Nightly consolidation and organization of the Desk. Analyzes the day's Diary entries, condenses verbose logs, extracts patterns, integrates session metrics, and surfaces user feedback. Runs overnight when user is sleeping - be thorough. Auto-invoke on overnight pulses (10 PM - 6 AM) or when Diary needs cleanup.
disable-model-invocation: false
---

# Daily Retrospection

Intelligent overnight housekeeping for the Desk. This skill analyzes what actually happened today and organizes it - NOT by following a rigid template, but by understanding the content and structuring it appropriately.

## Core Philosophy

**Dynamic organization > Rigid hierarchy**

- Analyze what exists, then decide how to organize it
- Patterns should emerge from data, not be pre-created
- Preserve raw information in Archive, present condensed summaries in Diary
- Cross-cutting documents evolve based on what's actually tracked
- Every run should leave the Desk more useful for future sessions

## When to Invoke

- **Overnight pulses** (10 PM - 6 AM): Primary use case - thorough cleanup while user sleeps
- **After very active days**: When Diary is 300+ lines with repetitive entries
- **Weekly maintenance**: Can be part of weekly review
- **On request**: User asks to "clean up the Diary" or "organize today's notes"

## Workflow

### Phase 1: Analyze Today's Diary

Read `Diary/YYYY-MM-DD.md` (today's date) and identify:

**1. Entry Categories**
Scan each entry and mentally categorize:
- `routine`: Repetitive checks (DND pulses, silent checks, hourly heartbeats)
- `event`: Something actually happened (user interaction, notification sent, decision made)
- `insight`: Pattern discovered, lesson learned, feedback received
- `action`: Task completed, file changed, pulse scheduled
- `issue`: Problem encountered, error logged

**2. Redundancy Analysis**
Look for patterns like:
```
"12 AM - Silent check, DND respected, all quiet"
"1 AM - Silent check, DND respected, all quiet"
"2 AM - Silent check, DND respected, all quiet"
```
These should be consolidated into:
```
## DND Hours Summary (12 AM - 6 AM)
6 silent checks, no notifications sent. All quiet.
```

**3. Key Information Extraction**
Pull out what matters:
- User interactions (messages, feedback, corrections)
- Decisions made and their rationale
- Events that affected user's day (meetings, health, mood)
- Accomplishments and progress
- Patterns worth remembering
- Action items that carried over

### Phase 2: Condense and Reorganize

**Create Summary Version**

If today's diary is 200+ lines, create a condensed version:

1. **Add Table of Contents at top** (if multiple sections)
   ```markdown
   ## Quick Navigation
   - [DND Summary](#dnd-hours-summary)
   - [Morning Context](#morning-context)
   - [Key Events](#key-events)
   - [Session Metrics](#session-metrics)
   - [Insights](#insights)
   ```

2. **Consolidate routine entries**
   - Multiple DND checks → single summary
   - Multiple "all quiet" entries → "Overnight: quiet, no issues"
   - Hourly heartbeats → "X hourly pulses executed, all successful"

3. **Preserve unique information**
   - Never lose actual content - summarize, don't delete
   - User quotes, specific numbers, decisions should remain intact
   - If in doubt, keep it

**Archive Verbose Original (if needed)**

Only archive if today's diary was exceptionally verbose (400+ lines):
```bash
# Move verbose original to archive
mkdir -p Diary/Archive/2026-02
mv Diary/2026-02-05.md Diary/Archive/2026-02/2026-02-05-verbose.md

# Create condensed version at original path
# (Write the condensed content)
```

**Usually don't archive** - just edit in place to condense.

### Phase 3: Cross-Cutting Documents (Pattern-Driven)

**DO NOT pre-create documents.** Instead, check if patterns justify creating or updating them.

**Decision Framework:**

Ask: "Is this data point appearing 3+ days in a row?"
- Sleep data logged daily → Consider `Diary/Patterns/Sleep.md`
- Workout data logged daily → Consider `Diary/Patterns/Fitness.md`
- Headaches logged multiple days → Consider `Diary/Patterns/Health-Issues.md`

Ask: "Is this context needed across multiple sessions?"
- MCP troubleshooting patterns → Consider `Diary/Patterns/MCP-Debugging.md`
- User feedback patterns → Consider `Diary/Patterns/User-Preferences-Learned.md`

Ask: "Would future-me benefit from this being easy to find?"
- Yes → Create cross-cutting document with clear links back to source entries
- No → Leave in daily diary, it's fine there

**Example: Creating a pattern doc**

```markdown
# Diary/Patterns/Sleep.md

Created: 2026-02-05
Reason: Sleep data appearing consistently, useful for pattern analysis

## Weekly Summary
| Date | Hours | Quality | Notes |
|------|-------|---------|-------|
| 02-04 | 5.5h | Fair | Late coding, headache |
| 02-05 | TBD | TBD | Early meetings |

## Patterns Observed
- Late-night coding sessions correlate with next-day fatigue
- [Add more as they emerge]

## Sources
- Diary/2026-02-04.md
- Diary/2026-02-05.md
```

### Phase 4: Session Analysis Integration

Use the `/session-analyzer` skill approach to get today's metrics.

**Quick metrics to capture:**

```bash
# Get today's sessions from index
cat ~/.claude/projects/[YOUR_PROJECT_HASH]/sessions-index.json | python3 -c "
import json, sys
from datetime import date

data = json.load(sys.stdin)
today = date.today().isoformat()

sessions = [e for e in data['entries'] if e.get('modified', '')[:10] == today]
total_msgs = sum(e.get('messageCount', 0) for e in sessions)

print(f'Sessions: {len(sessions)}')
print(f'Total messages: {total_msgs}')
"
```

**Add to Diary if significant:**

```markdown
## Daily Session Metrics

| Metric | Value |
|--------|-------|
| Sessions | 8 |
| Total messages | 142 |
| Estimated activity | High |

Notable: Major context engineering session in afternoon.
```

Only add this section if:
- There were 5+ sessions (busy day)
- User explicitly asked for metrics
- Something unusual happened (very high/low activity)

### Phase 5: User Feedback Extraction

**Scan for feedback signals in today's conversations:**

Patterns that indicate feedback:
- "no," / "wrong" / "actually" → Direct correction
- "don't" / "stop" / "wait" → Unwanted action
- "I prefer" / "should be" / "instead" → Preference expression
- "fix" / "error" / "mistake" → Problem identified

**If feedback found:**

1. Log to Diary:
   ```markdown
   ## Feedback Captured
   - "Actually, I prefer X over Y" - Updated Preferences/Preferences.md
   - "Don't notify me about Z" - Added to DND preferences
   ```

2. Update relevant files:
   - Clear preference → Update `Preferences/Preferences.md`
   - Behavioral feedback → Consider updating `CLAUDE.md` or creating rule
   - One-off correction → Just log in Diary, don't over-generalize

3. If pattern emerges (3+ similar corrections):
   - Create entry in auto-memory
   - Link to Diary entries as source

### Phase 6: Prepare for Tomorrow

**Check for carried-over items:**

1. Read today's diary for uncompleted tasks
2. Check if any scheduled pulses failed
3. Note anything that needs follow-up

**Add "Tomorrow Notes" section if needed:**

```markdown
## Notes for Tomorrow Morning

- Check on headache status (user had eye strain)
- Gentle morning - probable sleep deficit
- Follow up on [specific thing]
- Don't push for [specific thing]
```

### Phase 7: Commit Changes

**Always commit after retrospection:**

```bash
git add Diary/
git add -A  # Catch any new pattern files
git commit -m "Daily retrospection: YYYY-MM-DD - [brief summary]"
git push
```

Example commit messages:
- "Daily retrospection: 2026-02-05 - Consolidated DND entries, added session metrics"
- "Daily retrospection: 2026-02-05 - Created Sleep pattern doc, extracted user feedback"
- "Daily retrospection: 2026-02-05 - Light cleanup, quiet day"

## What NOT to Do

- **Don't create empty pattern files** - Only create when data exists
- **Don't over-consolidate** - Some verbosity is fine, especially for unique events
- **Don't lose information** - Archive first if removing significant content
- **Don't run during active hours** - This is for overnight, not interrupting user's day
- **Don't send notifications** - Silent operation; results visible in Diary

## Output Checklist

After running daily-retrospection, verify:

- [ ] Today's Diary is readable at a glance (TOC if long)
- [ ] Routine entries consolidated (no 6 identical DND entries)
- [ ] Key events and insights preserved and easy to find
- [ ] Any new patterns documented (only if justified)
- [ ] User feedback captured and routed appropriately
- [ ] Tomorrow's context prepared for morning pulse
- [ ] All changes committed to git

## Examples

### Example: Consolidating a Verbose Day

**Before (300+ lines):**
```markdown
## 12:00 AM - Silent Check
DND hours. All quiet. No notification sent.

## 1:00 AM - Silent Check
DND hours. All quiet. No notification sent.

[... 4 more identical entries ...]

## 7:00 AM - Morning Pulse
DND ended. Sent notification.
User responded: "Good morning!"
...
```

**After (condensed):**
```markdown
## Quick Navigation
- [DND Summary](#dnd-hours-summary)
- [7 AM Morning Pulse](#7-am---morning-pulse)
- [Key Events](#key-events)

---

## DND Hours Summary (12 AM - 6 AM)
6 silent checks completed. No notifications sent. All quiet.

---

## 7:00 AM - Morning Pulse
DND ended. Sent notification.
User responded: "Good morning!"
...
```

### Example: Emerging Pattern Detection

**Day 1 Diary:**
```
User mentioned headache from screen time. Took break.
```

**Day 2 Diary:**
```
Eye strain again. 20-20-20 rule suggested.
```

**Day 3 Diary:**
```
Third day of eye strain. User working long hours on Reeve-bot.
```

**Action:** Create `Diary/Patterns/Eye-Strain.md`:
```markdown
# Eye Strain Pattern

## Observations
- 2026-02-03: First mention, took break
- 2026-02-04: Recurrence, suggested 20-20-20 rule
- 2026-02-05: Third occurrence, correlates with Reeve-bot sprint

## Triggers
- Extended coding sessions (4+ hours)
- Late-night work (after 10 PM)
- High-intensity flow states

## Mitigations
- Suggest 20-20-20 rule during long sessions
- Recommend screen breaks in evening wrap-up
- Note: User accepts suggestions but doesn't always follow through

## Recommendation
- Build break reminders into afternoon pulses
- Track correlation with sleep quality
```

---

**Remember:** This skill runs overnight. Be thorough, be thoughtful, and leave the Desk in better shape than you found it. The next session of Reeve (tomorrow morning) depends on the quality of tonight's retrospection.
