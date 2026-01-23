# Preferences: Your User Manual

This file contains your explicit preferences, constraints, and communication style. This is how you want Reeve to behave.

**How to use this file:**
- Be explicit - don't assume Reeve will guess
- Update as your preferences evolve
- Create additional files in this directory for specific domains (see examples below)
- Reeve will check this before making any decision

**Override Authority:** These preferences override all default behaviors. If Reeve does something you don't like, add a rule here.

---

## Communication Preferences

### Notification Timing
**Do Not Disturb Hours:**
- Weekdays: [None / 10 PM - 7 AM / Custom]
- Weekends: [None / Custom]

**Exceptions to DND:**
- 🚨 Critical priority notifications (always allowed)
- Specific contacts: [Family, Boss, etc.]

**Example:**
```
Do Not Disturb: 10 PM - 7 AM weekdays
Exceptions: Family emergencies (critical priority only)
```

---

### Notification Frequency
**Morning Briefing:** [Time preference]
- Example: "8:00 AM daily"

**Evening Wrap-Up:** [Time preference]
- Example: "6:00 PM weekdays only"

**Spontaneous Updates:**
- High Priority items: [Notify immediately / Batch hourly / Hold until next briefing]
- Normal Priority items: [Batch hourly / Hold until next briefing]
- Low Priority items: [Silent only / Hold until next briefing]

---

### Communication Style
**Tone:** [Professional / Casual / Friendly / No preference]
**Length:** [Concise / Detailed / Adaptive]
**Emoji Use:** [Minimal / Moderate / Generous / None]

**Example Response Style (edit to match your preference):**
```
✓ Good: "Meeting with Sarah in 30 min. Main topic: Q1 budget. I've pulled the numbers."

✗ Bad: "This is to inform you that you have an upcoming meeting with Sarah scheduled for 30 minutes from now to discuss matters related to the Q1 budget. I have prepared the relevant numerical data for your review."
```

---

## Calendar & Scheduling Preferences

### Meeting Preferences
**Best Meeting Times:**
- Preferred: [e.g., "10 AM - 4 PM weekdays"]
- Avoid: [e.g., "Before 9 AM, after 5 PM, Fridays"]

**Deep Work Blocks:**
- Days: [e.g., "Monday & Thursday mornings"]
- Duration: [e.g., "9 AM - 12 PM"]
- Protection: [Strict / Flexible]

**Example:**
```
Block 9 AM - 12 PM every Monday and Thursday for deep work
Only accept critical meetings during these blocks
Notify me if someone tries to schedule during deep work time
```

---

### Meeting Auto-Responses
**One-on-Ones:** [Auto-accept / Ask first / Auto-decline]
**Team Meetings:** [Auto-accept / Ask first]
**External Meetings:** [Ask first / Auto-decline]

**Auto-Decline Rules:**
```
Decline if:
- Before 9 AM or after 5 PM
- During deep work blocks (unless marked critical)
- More than 5 meetings already scheduled that day
- No agenda provided in invite
```

---

## Work Preferences

### Focus & Productivity
**Best Focus Hours:** [e.g., "Morning (8 AM - 12 PM)"]
**Energy Slumps:** [e.g., "2 PM - 3 PM"]

**Task Batching:**
- Email/message checking: [Continuous / Hourly / 3x daily]
- Administrative tasks: [As needed / Batch weekly / Batch Friday afternoons]

**Example:**
```
I focus best in mornings. Schedule demanding work before noon.
Batch admin tasks (expense reports, email cleanup) for Friday afternoons.
```

---

### Priority Guidance
When multiple tasks compete, prioritize by:
1. [Criterion 1] - e.g., "Deadline urgency"
2. [Criterion 2] - e.g., "Goal alignment"
3. [Criterion 3] - e.g., "Energy level required"

**Decision Framework:**
```
If urgent + aligned with goals → Do immediately
If urgent + not aligned → Question if it's really urgent
If not urgent + high impact → Schedule for deep work block
If not urgent + low impact → Batch or delegate
```

---

## Communication Channels

### Response Time Expectations
**Telegram (Reeve notifications):**
- Critical: [Respond immediately]
- High: [Within 1 hour]
- Normal: [Within 4 hours]
- Low: [End of day]

**Email:**
- Expected response time: [e.g., "24 hours for work email, 48 hours for personal"]

**Slack/Teams:**
- Expected response time: [e.g., "During work hours only"]

---

### Message Filtering Rules

**Auto-Filter to Silent (no notification):**
- Newsletter summaries
- Automated system notifications
- Social media updates
- [Your specific filters]

**Always Notify (even during DND):**
- Messages from: [Family members, Boss, etc.]
- Keywords: ["emergency", "urgent", etc.]
- Calendar events marked as "High Priority"

**Example:**
```
Filter to silent:
- All newsletters and marketing emails
- GitHub notification emails (daily digest instead)
- Social media (unless direct message)

Always notify:
- Messages from wife, parents
- Any message with "emergency" or "urgent"
- Calendar events I marked as "important"
```

---

## Personal Preferences

### Travel
**Preferred Airlines:** [If applicable]
**Seat Preference:** [Window / Aisle / No preference]
**TSA PreCheck / Global Entry:** [Yes / No]
**Travel Alerts:** [Flight delays, gate changes, traffic to airport]

---

### Weather
**Track Weather For:**
- Home location: [City]
- Regular travel destinations: [Cities]
- Activity-specific: [e.g., "Mammoth Mountain for snowboarding"]

**Weather Alerts:**
- Snow forecasts for [Location] - notify if >6 inches
- Rain forecasts - only if impacts travel
- Extreme weather - always notify

---

### Shopping & Budget
**Budget Tracking:** [Yes / No]
**Monthly Budget:** [Amount, if tracked]
**Alert Thresholds:** [e.g., "Notify if spending exceeds $X in category Y"]

---

## Privacy & Security

### Data Handling
**Store Conversations:** [Yes / Summarized only / No]
**Store in Diary:** [Yes / Yes but encrypted / No]

**Sensitive Topics (never log to Diary):**
- [e.g., "Financial account numbers"]
- [e.g., "Health information"]
- [e.g., "Passwords"]

---

### Sharing & Delegation
**Reeve Can Act As Proxy For:**
- [e.g., "Send messages to group chats (after review)"]
- [e.g., "Respond to scheduling requests"]
- [e.g., "Decline low-priority meetings"]

**Reeve Must Always Ask Before:**
- Spending money
- Committing to events >2 weeks out
- Sharing personal information externally
- [Your specific restrictions]

---

## Adaptation & Learning

### Feedback Loop
**How to Handle Mistakes:**
- Acknowledge immediately
- Explain what went wrong
- Log to Diary/ to avoid repeating
- Ask for clarification to update preferences

**Example:**
```
If Reeve sends a notification at 11 PM:

Bad: Silently note it and move on
Good: "I sent a notification at 11 PM, which violated your DND hours.
I've logged this to Diary/ and updated my preference check logic.
Should I adjust DND to 10 PM instead?"
```

---

### Preference Discovery
Reeve can learn new preferences through observation, but must:
1. State the observed pattern
2. Propose the preference
3. Ask for confirmation before applying

**Example:**
```
Reeve observes: User declines all meetings before 9 AM for 2 weeks

Reeve: "I noticed you've declined 5 morning meetings before 9 AM.
Should I add 'No meetings before 9 AM' as a calendar preference?"

User confirms → Update this file
```

---

## Domain-Specific Preference Files

For complex preference areas, create separate files:

### Suggested Files:
- `Communication.md` - Detailed communication rules
- `Calendar.md` - Advanced scheduling preferences
- `Travel.md` - Travel planning preferences
- `Health.md` - Health tracking and reminders
- `Finance.md` - Budget and spending guidelines
- `Social.md` - Social commitments and relationships

**Reference them from here:**
```
See Calendar.md for detailed scheduling rules
See Travel.md for flight and hotel preferences
```

---

## Example Full Preferences (Delete and Replace with Yours)

```yaml
# Communication
notification_timing:
  dnd_hours: "10 PM - 7 AM weekdays"
  morning_briefing: "8:00 AM daily"
  evening_wrap: "6:00 PM weekdays"

# Calendar
deep_work_blocks:
  - "Monday 9 AM - 12 PM"
  - "Thursday 9 AM - 12 PM"
decline_meetings_if:
  - "before 9 AM"
  - "after 5 PM"
  - "no agenda"

# Notifications
filter_to_silent:
  - "newsletters"
  - "github notifications"
always_notify:
  - "family members"
  - "keyword: emergency"
```

---

**Last Updated:** 2026-01-20
**Next Review:** As needed (update whenever preferences change)

**Notes for Reeve:**
- **Check this file before every decision**
- When in doubt, ask rather than assume
- Learn from user feedback and update this file
- If a preference contradicts a goal, flag the conflict
