# Reeve Desk

Welcome to your **Reeve Desk** - the transparent, editable workspace where Reeve (your AI Chief of Staff) stores all knowledge about you.

## What is the Desk?

The Desk is a collaborative workspace between you and Reeve. Everything Reeve knows about you lives here in plain Markdown files. There are no hidden databases, no black-box algorithms - just transparent, human-readable text files you can edit anytime.

## Directory Structure

```
reeve_desk/
├── README.md              ← You are here
├── CLAUDE.md              ← Reeve's identity & operating instructions
├── SKILLS.md              ← Reeve's capabilities (tools & MCP functions)
│
├── Goals/                 ← Your North Star (long-term objectives)
│   └── Goals.md
│
├── Responsibilities/      ← Your Operational Manual (recurring duties)
│   └── Responsibilities.md
│
├── Preferences/           ← Your User Manual (how you want Reeve to behave)
│   └── Preferences.md
│
└── Diary/                 ← Reeve's memory (activity logs, patterns)
    ├── README.md
    └── 2026-01-20.md
```

## Quick Start

### 1. Understand How Reeve Works

Read these files to understand Reeve's operating model:

1. **[CLAUDE.md](CLAUDE.md)** - Reeve's core identity and decision-making framework
2. **[SKILLS.md](SKILLS.md)** - What Reeve can do (schedule pulses, send notifications, etc.)

### 2. Tell Reeve About Yourself

Fill in these template files with your information:

1. **[Goals/Goals.md](Goals/Goals.md)** - What are you trying to achieve? (3-5 major objectives)
2. **[Responsibilities/Responsibilities.md](Responsibilities/Responsibilities.md)** - What recurring duties do you have?
3. **[Preferences/Preferences.md](Preferences/Preferences.md)** - How should Reeve communicate with you?

### 3. Start Using Reeve

Once you've personalized the Desk:

1. **Ensure reeve_bot is configured** to point to this directory (default: `~/reeve_desk`)
2. **Complete reeve_bot Phase 5+** (Daemon, API, integrations)
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
- When a pulse fires, Reeve wakes up, reads the Desk, and takes action
- You're only interrupted when something truly requires your attention

### 3. Edit Anything, Anytime

**This is YOUR workspace.** Feel free to:
- ✏️ Edit any file to change Reeve's behavior
- 📁 Reorganize directories
- 🗑️ Delete sections that don't apply to you
- ➕ Add new files for specialized preferences
- 🔄 Evolve the structure over time

**Reeve will adapt to whatever you create.**

## What to Edit First

### For Minimal Setup (10 minutes):

1. **Goals/Goals.md** - Add 1-3 current goals (examples provided)
2. **Preferences/Preferences.md** - Set notification times and DND hours
3. **Responsibilities/Responsibilities.md** - Add morning/evening routines

This gives Reeve enough context to be useful.

### For Full Setup (30-60 minutes):

- Complete all sections in Goals, Responsibilities, and Preferences
- Add detailed communication rules
- Set up calendar preferences
- Define priority frameworks
- Optionally create domain-specific preference files

## How Reeve Uses the Desk

### Every Time Reeve Wakes Up (on a pulse):

1. **Reads the context:**
   - Why did I wake up? (the pulse prompt)
   - What time is it?
   - What does the user's calendar look like?

2. **Checks the Desk:**
   - `Goals/Goals.md` → What are the user's priorities?
   - `Responsibilities/Responsibilities.md` → Any recurring duties due?
   - `Preferences/Preferences.md` → How should I communicate?
   - `Diary/` → Any recent context I should know?

3. **Takes action:**
   - Send a notification (if the user needs to know)
   - Schedule future aperiodic pulses (for non-hour times) or add instructions to Diary/ (for hour-aligned times)
   - Update Diary/ (log what I did)

### Example Flow: Morning Briefing

```
1. Periodic pulse fires automatically at 8:00 AM
2. Reeve checks Diary/2026-01-20.md and sees: "Morning briefing"

3. Reeve reads:
   - Goals/Goals.md → User's top priority is "Complete Reeve MVP"
   - Responsibilities/Responsibilities.md → Checking calendar is part of morning routine
   - Preferences/Preferences.md → User wants concise briefings

4. Reeve composes notification:
   "Good morning! 3 meetings today:
   - 10 AM: Team standup
   - 2 PM: 1:1 with Sarah (re: Q1 budget)
   - 4 PM: Code review

   Top priority: Finish Phase 5 (Daemon) for Reeve MVP.
   Deep work block protected: 9 AM - 12 PM."

5. Reeve sends notification via Telegram

6. Reeve logs to Diary/2026-01-20.md:
   "Morning briefing delivered at 8:00 AM.
   User has moderate meeting load (3 meetings).
   Deep work block successfully protected."

7. Reeve adds to Diary/2026-01-20.md for later:
   "Evening wrap-up" (the automatic 6:00 PM periodic pulse will handle it)
```

## File Editing Tips

### Markdown Basics

All files use Markdown formatting:

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*

- Bullet point
- Another bullet
  - Nested bullet

1. Numbered list
2. Second item

[Link text](https://url.com)

`code or commands`
```

### Editing Files

**On Linux/Mac:**
```bash
cd ~/reeve_desk
nano Goals/Goals.md          # Simple editor
vim Goals/Goals.md           # Advanced editor
code Goals/Goals.md          # VS Code
```

**On any platform:**
- Any text editor (Notepad++, Sublime Text, VS Code, etc.)
- Just edit and save - Reeve reads files directly

### Version Control (Optional)

You can track changes with git:

```bash
cd ~/reeve_desk
git init
git add .
git commit -m "Initial desk setup"

# After making changes:
git add .
git commit -m "Updated preferences: added DND hours"
```

This gives you a history of how your preferences evolved.

## Troubleshooting

### Reeve Isn't Behaving As Expected

1. **Check CLAUDE.md** - Does it define the behavior you want?
2. **Check Preferences/Preferences.md** - Is there a rule causing this?
3. **Read Diary/** - Look for Reeve's recent logs to understand reasoning
4. **Edit the relevant file** to change the behavior
5. **Test again** - Schedule a pulse and observe

### Reeve Can't Read Files

1. **Check permissions:**
   ```bash
   ls -la ~/reeve_desk
   # Should be readable by the user running reeve_bot
   ```

2. **Check reeve_bot config:**
   ```bash
   # In reeve_bot/.env or config
   REEVE_DESK_PATH=~/reeve_desk
   ```

3. **Check file paths:**
   - All files should be in `~/reeve_desk/` or subdirectories
   - Use standard Markdown `.md` extension

### Want to Start Over

```bash
# Backup current desk
mv ~/reeve_desk ~/reeve_desk.backup

# Recreate from templates
# (Re-run desk creation or copy from backup)
```

## Privacy & Security

### What's Stored Here

- Your goals and priorities (plaintext)
- Your calendar preferences (plaintext)
- Your communication preferences (plaintext)
- Reeve's activity logs (plaintext)

**NOT stored here:**
- Passwords or API keys (those go in `.env` files in reeve_bot/)
- Full message transcripts (those go in C.O.R.E. memory system)
- Sensitive data (you control what goes in these files)

### Who Can Access This

- **You** - Full read/write access
- **Reeve** - Read access (and write for Diary/)
- **Anyone with access to your filesystem** - These are plaintext files

**If you're concerned about privacy:**
- Encrypt your home directory
- Use file permissions to restrict access
- Don't include sensitive information in these files
- Use the C.O.R.E. memory system for sensitive data storage

## Evolution Over Time

The Desk will grow and change:

**Week 1:** Basic templates filled in
**Month 1:** Diary/ has daily logs, patterns emerge
**Month 3:** Custom preference files, project-specific structures
**Month 6:** Well-organized archive, refined decision frameworks

**This is normal and expected.** Let the structure evolve naturally based on your usage.

## Support & Feedback

**Issues with Reeve Bot (the software):**
- See: https://github.com/anthropics/claude-code/issues (if public repo)
- Or: Contact the maintainer

**Want to share your Desk customizations:**
- Consider sharing anonymized versions
- Help others learn effective Desk structures

**Questions about how to structure the Desk:**
- Experiment! There's no "wrong" structure
- Start simple, expand as needed
- Ask Reeve: "How should I organize [X]?"

## Further Reading

- **[CLAUDE.md](CLAUDE.md)** - Deep dive into Reeve's operating principles
- **[SKILLS.md](SKILLS.md)** - Complete reference of Reeve's capabilities
- **[Diary/README.md](Diary/README.md)** - How Reeve's memory system works
- **[Preferences/Preferences.md](Preferences/Preferences.md)** - Example preferences with detailed explanations

---

**Created:** 2026-01-20
**Version:** 1.0
**Maintainer:** You (the user)

Remember: This is YOUR workspace. Shape it however makes sense to you. Reeve will adapt.
