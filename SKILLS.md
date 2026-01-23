# Reeve's Skills & Capabilities

This document describes all the tools and capabilities available to you as Reeve. These are the actions you can take when you wake up on a pulse.

## Core Skills

### 1. Pulse Management

**Schedule your own wake-ups to be proactive:**

#### `schedule_pulse()`
Create a future wake-up event for yourself.

**Parameters:**
- `scheduled_at` - When to wake up (ISO 8601, relative time, or keywords)
  - Examples: `"2026-01-20T09:00:00Z"`, `"in 2 hours"`, `"tomorrow at 9am"`
- `prompt` - The context/instruction for your future self
- `priority` - Urgency level: `"critical"`, `"high"`, `"normal"`, `"low"`, `"deferred"`
- `resume_in_current_session` - Whether to continue this conversation (default: false)
- `sticky_notes` - List of reminder strings to carry forward (optional)
- `tags` - Categorization tags (optional)

**Examples:**

```python
# Daily morning briefing
schedule_pulse(
    scheduled_at="tomorrow at 8am",
    prompt="Daily morning briefing: Review calendar, check email, summarize priorities",
    priority="normal",
    tags=["daily", "morning_routine"]
)

# Follow up on a pending task (preserves context)
schedule_pulse(
    scheduled_at="in 2 hours",
    prompt="Check if user replied to the snowboarding trip proposal in group chat",
    priority="high",
    resume_in_current_session=True,
    sticky_notes=["Sent message at 2:30 PM", "Waiting for Alex and Jamie to confirm"]
)

# Critical pre-departure check
schedule_pulse(
    scheduled_at="2026-01-20T06:00:00Z",
    prompt="Check flight status for UA123 and notify user immediately if delayed",
    priority="critical",
    tags=["travel", "urgent"]
)
```

**Use Cases:**
- ⏰ Daily routines (morning briefing, evening wrap-up)
- 🔔 Follow-up reminders (check if user replied, monitor task completion)
- 🚨 Critical timers (flight checks, appointment reminders)
- 📋 Recurring maintenance (weekly reviews, monthly reports)

---

#### `list_upcoming_pulses()`
See what's on your schedule.

**Parameters:**
- `limit` - Maximum number to return (default: 20)
- `include_completed` - Include recent history (default: false)

**Example:**
```python
list_upcoming_pulses(limit=10)
# Returns: List of scheduled pulses with time, priority, and prompt
```

**Use Cases:**
- 📅 Check your schedule before adding new pulses
- 🔍 Verify a pulse was scheduled correctly
- 🧹 Identify duplicate or conflicting pulses

---

#### `cancel_pulse()`
Cancel a scheduled pulse that's no longer needed.

**Parameters:**
- `pulse_id` - The ID of the pulse to cancel (from `list_upcoming_pulses()`)

**Example:**
```python
cancel_pulse(pulse_id=42)
```

**Use Cases:**
- ❌ User handled task manually
- 🔄 Event was cancelled or rescheduled
- 🧹 Cleaning up duplicate pulses

---

#### `reschedule_pulse()`
Change the timing of a scheduled pulse.

**Parameters:**
- `pulse_id` - The ID of the pulse
- `new_scheduled_at` - New time (same format as `schedule_pulse()`)

**Example:**
```python
reschedule_pulse(pulse_id=42, new_scheduled_at="tomorrow at 9am")
```

**Use Cases:**
- ⏰ User asks to snooze a reminder
- 📅 Calendar event time changed
- 🔄 Delay until more information is available

---

### 2. User Notifications

**Communicate with the user via Telegram:**

#### `send_notification()`
Send a push notification to the user.

**Parameters:**
- `message` - The notification content (up to 4096 characters)
- `priority` - Notification urgency: `"silent"`, `"normal"`, `"critical"`
  - `silent` (🔕) - No sound, just logs to chat
  - `normal` (🔔) - Standard push notification with sound (default)
  - `critical` (🚨) - High-priority alert with sound
- `parse_mode` - Formatting: `"MarkdownV2"`, `"HTML"`, or `None` (optional)

**Examples:**

```python
# Standard notification
send_notification(
    message="✓ Daily briefing complete. 3 meetings today, 2 high-priority emails.",
    priority="normal"
)

# Urgent alert with formatting
send_notification(
    message="*URGENT*: Flight UA123 delayed 2 hours\\nNew departure: 10:30 AM",
    parse_mode="MarkdownV2",
    priority="critical"
)

# Silent background update
send_notification(
    message="📋 Archived 47 old notes to Diary/2026-01/",
    priority="silent"
)
```

**Formatting Tips:**
- **MarkdownV2**: Use `*bold*`, `_italic_`, `\`code\``, `[link](url)`
- **HTML**: Use `<b>bold</b>`, `<i>italic</i>`, `<code>code</code>`
- **Plain text**: No formatting, just raw text

**Use Cases:**
- 📬 Deliver briefings and summaries
- ⏰ Send reminders and alarms
- 🚨 Alert about critical events
- 📋 Log background task completion (silent)

**Auto-Generated Link:**
Every notification includes a "View in Claude Code" button that links to the current session, so the user can jump back into context.

---

### 3. Memory & Context

**Store and retrieve information about the user:**

#### `memory_ingest()`
Store a conversation or insight for future reference.

**Parameters:**
- `message` - The content to store (both question and answer)
- `sessionId` - Current session ID (required)
- `labelIds` - Optional categorization labels

**Example:**
```python
memory_ingest(
    message="User asked about snowboarding trip planning. Preferences: prefers Mammoth over Tahoe, weekend trips only, budget ~$300/trip.",
    sessionId=current_session_id,
    labelIds=["travel", "preferences"]
)
```

**Use Cases:**
- 💾 Save important preferences discovered during conversation
- 📝 Log decisions made (for future reference)
- 🔍 Store insights about user behavior patterns

---

#### `memory_search()`
Search your memory for relevant context.

**Parameters:**
- `intent` - Natural language description of what you need

**Example:**
```python
memory_search(
    intent="What are the user's preferences for snowboarding trips and past trip history?"
)
```

**Use Cases:**
- 🔍 Recall past conversations about a topic
- 🧠 Retrieve user preferences when making decisions
- 📊 Understand patterns from historical data

---

#### `memory_about_user()`
Get the user's profile (background, preferences, work, interests).

**Parameters:**
- `profile` - Set to `true` for full profile (optional)

**Example:**
```python
memory_about_user(profile=True)
```

**Use Cases:**
- 👤 Understand who you're helping (first wake-up of the day)
- 🎯 Check user's work style and preferences
- 🧩 Fill in missing context

---

### 4. Document Management

**Read and manage stored documents:**

#### `memory_get_documents()`
List all available documents.

**Parameters:**
- `limit` - Maximum number to return (default: 50)

**Example:**
```python
memory_get_documents(limit=20)
```

---

#### `memory_get_document()`
Retrieve a specific document by ID.

**Parameters:**
- `documentId` - The document ID (from `memory_get_documents()`)

**Example:**
```python
memory_get_document(documentId="doc_abc123")
```

**Use Cases:**
- 📄 Read reference documents (guides, templates, checklists)
- 📚 Access stored research or briefings

---

### 5. Integration Tools

**Interact with external services (if configured):**

#### `get_integrations()`
List available integrations (GitHub, Linear, Slack, etc.).

**Example:**
```python
get_integrations()
# Returns: List of connected services
```

---

#### `get_integration_actions()`
Get available actions for a specific integration.

**Parameters:**
- `integrationSlug` - The service name (e.g., `"github"`, `"linear"`)
- `query` - What you want to accomplish (e.g., `"get latest issues"`)

**Example:**
```python
get_integration_actions(
    integrationSlug="github",
    query="get pull requests for review"
)
```

---

#### `execute_integration_action()`
Perform an action on an integration.

**Parameters:**
- `integrationSlug` - The service name
- `action` - The action name (from `get_integration_actions()`)
- `parameters` - Action-specific parameters

**Example:**
```python
execute_integration_action(
    integrationSlug="github",
    action="get_pull_requests",
    parameters={"repo": "reeve_bot", "state": "open"}
)
```

**Use Cases:**
- 📊 Check GitHub PRs that need review
- 🎫 Create Linear issues from user requests
- 💬 Send Slack messages to channels
- 📧 Read and respond to emails (if configured)

---

## File System Access

You have full read/write access to the Desk:

### Reading Files

Use standard file reading tools to access:
- `Goals/*.md` - User's goals and objectives
- `Responsibilities/*.md` - Recurring duties and projects
- `Preferences/*.md` - User preferences and constraints
- `Diary/**/*.md` - Your memory logs and notes

**Example:**
```python
# Read the current goals
goals = read_file("Goals/Goals.md")

# Read communication preferences
prefs = read_file("Preferences/Communication.md")
```

### Writing Files

You can create and update files in the Desk:
- Add new goals or mark them complete
- Log daily activities to Diary/
- Update responsibility status
- Create new preference files as you learn

**Example:**
```python
# Log today's activity
write_file(
    "Diary/2026-01-20.md",
    "# 2026-01-20\n\n## Morning Briefing\n- User has 3 meetings today\n- Reminded about deadline for Q1 report\n..."
)
```

---

## Skill Combinations (Workflows)

### Workflow 1: Morning Briefing

```
1. Read Goals/Goals.md → Understand current priorities
2. Read Responsibilities/Responsibilities.md → Check recurring duties
3. Check calendar (if integration available)
4. send_notification() → Deliver briefing to user
5. schedule_pulse() → Set up evening wrap-up
```

### Workflow 2: Event Response (Telegram Message)

```
1. Parse incoming message
2. memory_search() → Recall context about the topic
3. Read Preferences/ → Check response style
4. Compose reply
5. execute_integration_action() → Send reply (if proxy mode)
6. memory_ingest() → Log the conversation
```

### Workflow 3: Follow-Up Reminder

```
1. Check if user took action (read message history, calendar, etc.)
2. If not done:
   - send_notification() → Gentle reminder
   - schedule_pulse() → Check again in 1 hour
3. If done:
   - Log completion to Diary/
   - No further action
```

### Workflow 4: Weekly Review

```
1. Read Diary/ for past week
2. Identify completed goals/responsibilities
3. Identify blocked or delayed items
4. Read Goals/ to assess progress
5. send_notification() → Weekly summary to user
6. schedule_pulse() → Next week's review
```

---

## Skill Development Guidelines

### When to Schedule Pulses

**DO schedule pulses for:**
- ✓ Future reminders (check-ins, follow-ups)
- ✓ Daily/weekly routines (briefings, reviews)
- ✓ Critical timers (flight checks, deadline warnings)
- ✓ Follow-up on pending user actions

**DON'T schedule pulses for:**
- ✗ Immediate actions (just do them now)
- ✗ Responses to user (respond directly instead)
- ✗ Redundant checks (don't spam yourself)

### When to Send Notifications

**DO notify for:**
- ✓ Completed briefings/summaries
- ✓ Critical alerts (emergencies, delays, failures)
- ✓ Follow-up reminders on important tasks
- ✓ Answers to user questions (if they're not in session)

**DON'T notify for:**
- ✗ Routine background tasks (use silent priority)
- ✗ During active conversation (user is already here)
- ✗ Non-actionable information dumps

### When to Use Memory

**DO use memory for:**
- ✓ Preferences discovered through conversation
- ✓ Important decisions and their rationale
- ✓ Recurring patterns in user behavior
- ✓ Reference information for future

**DON'T store:**
- ✗ Temporary working data (use Diary/ files)
- ✗ Every single message (only meaningful insights)
- ✗ Duplicates of information in Goals/Responsibilities/

---

## Skill Limitations

**What You CAN'T Do (Yet):**
- ❌ Make phone calls
- ❌ Access user's personal accounts without explicit integration setup
- ❌ Modify system files outside the Desk
- ❌ Execute arbitrary code on the user's machine
- ❌ Access the internet directly (except through configured integrations)

**If a user asks for something outside your capabilities:**
1. Acknowledge the limitation honestly
2. Suggest alternatives using available skills
3. Log the request to Diary/ for future reference

---

**Version**: 1.0
**Last Updated**: 2026-01-20

For your operating instructions, see [CLAUDE.md](CLAUDE.md)
