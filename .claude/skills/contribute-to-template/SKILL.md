---
name: contribute-to-template
description: Push generic improvements from your private desk back to the public template remote using git worktrees for safe, isolated editing. Use when you have improvements (skills, CLAUDE.md refinements, documentation) that would benefit all users.
user-invocable: true
---

# Contribute to Template

Push generic improvements from your private desk back to the public `template` remote using git worktrees for safe, isolated editing.

---

## **CRITICAL SECURITY WARNING**

The template is a **PUBLIC REPOSITORY**. Pushing private data is a **serious security and privacy breach**.

**BEFORE EVERY PUSH, VERIFY:**
1. **No personal names** - Replace "Reuben" with `[USER_NAME]`
2. **No file paths** - Replace `/home/reuben/` with `[YOUR_PATH]`
3. **No credentials** - API keys, tokens, passwords
4. **No personal data** - Goals, preferences, diary entries, schedules
5. **No contact info** - Phone numbers, emails, addresses

**If in doubt, DON'T PUSH. Ask the user first.**

---

## When to Use

Invoke `/contribute-to-template` when you have:
- New skills that are generally useful (not personal workflows)
- CLAUDE.md improvements (clarifications, bug fixes, better examples)
- Documentation updates
- Structural improvements to the Desk
- New rules in `.claude/rules/`

## What NEVER to Contribute

**These directories are ALWAYS private - NEVER push them:**
- `Preferences/` - Personal preferences, communication style
- `Goals/` - Personal goals and aspirations
- `Diary/` - Logs, notes, personal history
- `Responsibilities/` - Personal tasks and projects

**These patterns are ALWAYS private - search and replace before pushing:**
- User's real name → `[USER_NAME]`
- Specific paths → `[YOUR_DESK_PATH]`, `[REEVE_BOT_PATH]`
- Dates referencing personal events
- Any API keys, tokens, or credentials
- Phone numbers, email addresses, physical addresses
- Names of friends, family, colleagues
- Specific companies, projects, or employers

## Workflow Using Git Worktrees

Git worktrees allow you to work on the template in a separate directory without affecting your main desk. This is especially important when:
- Pulses are running and modifying your current desk
- You want to test template changes in isolation
- You need to carefully review what you're contributing

### 1. Set Up the Worktree (First Time)

```bash
# Ensure template remote is configured
git remote -v | grep template
# If not present: git remote add template git@github.com:[YOUR_GITHUB_USERNAME]/reeve-desk.git

# Fetch latest template
git fetch template

# Create a worktree for template contributions
git worktree add ~/workspace/reeve-desk-template-contrib template/master
```

This creates a separate checkout at `~/workspace/reeve-desk-template-contrib` that tracks the template remote.

### 2. Review What's Different

```bash
# See commits in your desk that aren't in template
git fetch template
git log template/master..HEAD --oneline
```

For each commit, ask:
- Is this generic (useful to any Reeve user)?
- Does it contain personal information?
- Is it a standalone improvement?

**Good candidates:**
- `Add context-engineering skill`
- `Fix typo in CLAUDE.md pulse documentation`
- `Improve emergency-response skill workflow`
- `Add self-awareness documentation`

**Bad candidates:**
- `Customize for wellness coaching`
- `Add preference: morning workouts`
- `Update Goals for Q1`

### 3. Make Changes in the Worktree

Navigate to the worktree and make your changes there:

```bash
cd ~/workspace/reeve-desk-template-contrib

# Option A: Copy files from your desk (then genericize)
cp ~/reeve_desk/.claude/skills/new-skill/SKILL.md .claude/skills/new-skill/

# Option B: Cherry-pick specific commits
git cherry-pick <commit-hash>

# Option C: Manually create/edit files
# Edit directly in this directory
```

### 4. Genericize the Changes

Before committing, ensure changes are generic:

1. **Replace user-specific values with placeholders:**
   - `[USER_NAME]` instead of actual name
   - `[YOUR_DESK_PATH]` instead of actual path
   - `[THEIR_DEFINITION_OF_SUCCESS]` instead of specific goals

2. **Add onboarding comments where customization is needed:**
   ```markdown
   <!--
   ONBOARDING: Customize this section for your specific setup.
   Example: "Help [NAME] achieve career success while maintaining health"
   -->
   ```

3. **Remove personal context:**
   - Specific dates, names, places
   - References to personal habits or routines
   - Timezone-specific information

### 5. Commit and Push from Worktree

```bash
cd ~/workspace/reeve-desk-template-contrib

# Check what you're about to commit
git status
git diff

# Create a branch for your changes
git checkout -b template-updates-YYYY-MM-DD

# Stage and commit
git add .
git commit -m "Add [feature]: description of what it does"

# Push to template remote
git push template template-updates-YYYY-MM-DD:master
```

### 6. Sync Main Desk with Template (CRITICAL)

After pushing to template, **always** merge your main desk with `template/master`. This incorporates the template's current state as your base.

```bash
cd ~/reeve_desk

# Fetch the updated template
git fetch template

# Merge with "ours" strategy to keep local personalization on conflicts
git merge template/master -X ours -m "Merge template updates (keeping local personalization)"

# Push to your private origin
git push origin master
```

**Why this matters:**
- Incorporates any new template features/structure into your desk
- Future `git log template/master..HEAD` shows what needs review
- Creates a clean merge point for tracking contributions

**Note:** Personal commits (Diary entries, Preferences, user-specific CLAUDE.md changes) will always show as "ahead" - that's intentional since they're not meant for the template. The merge ensures you have the latest template structure while keeping your personalization.

### 7. Verify and Clean Up

```bash
# Verify your desk is now based on template
git log template/master..HEAD --oneline
# Should only show commits NOT yet contributed

# Optionally reset worktree for next contribution
cd ~/workspace/reeve-desk-template-contrib
git fetch template
git checkout template/master
git reset --hard template/master
```

## Safety Checks (MANDATORY BEFORE EVERY PUSH)

**Run this verification before pushing to template:**

```bash
cd ~/workspace/reeve-desk-template-contrib

# 1. Check for personal names (replace YOUR_NAME with actual name)
grep -ri "reuben" . --include="*.md" | grep -v ".git"

# 2. Check for personal paths
grep -ri "/home/reuben" . --include="*.md" | grep -v ".git"

# 3. Check for potential API keys/secrets
grep -riE "(api_key|token|password|secret)" . --include="*.md" | grep -v ".git"

# 4. Review all staged changes line by line
git diff --staged

# 5. Verify no private directories are included
git status | grep -E "(Preferences|Goals|Diary|Responsibilities)/"
```

**If ANY of these commands return results, STOP and fix before pushing.**

**Checklist:**
- [ ] No personal names (replaced with `[USER_NAME]`)
- [ ] No personal paths (replaced with `[YOUR_DESK_PATH]`)
- [ ] No API keys, tokens, or credentials
- [ ] No Diary/, Goals/, Preferences/, Responsibilities/ files
- [ ] All changes reviewed with `git diff --staged`
- [ ] Commit message doesn't contain personal info

## Quick Reference

```bash
# List worktrees
git worktree list

# Create worktree from template
git worktree add ~/workspace/reeve-desk-template-contrib template/master

# Remove worktree
git worktree remove ~/workspace/reeve-desk-template-contrib

# Prune stale worktree references
git worktree prune

# Reset worktree to latest template (for fresh start)
cd ~/workspace/reeve-desk-template-contrib
git fetch template
git checkout template/master
git reset --hard template/master
```

## Why Worktrees?

| Without Worktrees | With Worktrees |
|-------------------|----------------|
| Must stash/commit current work | Work in isolation |
| Risk mixing personal and template changes | Clean separation |
| Pulses may modify files mid-contribution | Pulses only affect main desk |
| Harder to review what you're contributing | Easy diff against template |
| Risk of accidentally pushing personal data | Safe sandbox environment |

## Example Session

```
User: /contribute-to-template

Reeve: Let me set up a worktree for safe contribution.

[Runs: git worktree list]
[If no template worktree exists: git worktree add ~/workspace/reeve-desk-template-contrib template/master]

Checking what's available to contribute...
[Runs: git fetch template && git log template/master..HEAD --oneline]

Found 12 commits ahead of template. Analyzing...

**Template-worthy:**
1. `abc123` - Add context-engineering skill
2. `def456` - Fix pulse documentation typo
3. `ghi789` - Add self-awareness documentation

**Personal (skip):**
- `jkl012` - Customize for wellness coaching
- `mno345` - Add morning workout preference

I'll copy the relevant files to the worktree and genericize them.

[Makes changes in ~/workspace/reeve-desk-template-contrib]
[Commits and pushes to template]

Now syncing main desk with template...
[Runs: git fetch template && git rebase template/master]

Done! Merged template updates into your desk.
`git log template/master..HEAD` now shows remaining unreviewed/personal commits:
- `xyz999` - Merge template updates
- `jkl012` - Customize for wellness coaching (personal - keep)
- `mno345` - Add morning workout preference (personal - keep)
- Various Diary entries (personal - keep)

The contributed commits are now part of template/master, so future reviews start fresh.
```

## Remotes Reference

| Remote | Repo | Purpose |
|--------|------|---------|
| `origin` | Private (your-desk-repo) | Your personal desk |
| `template` | Public (reeve-desk) | Shared template |

**In your main desk:** `origin` = private, `template` = public
**In the worktree:** remotes are shared, push to `template` remote

Always push personal changes to `origin`, generic improvements to `template`.

## Maintaining the Worktree

If you contribute frequently:
- Keep the worktree around (`~/workspace/reeve-desk-template-contrib`)
- Periodically fetch and reset: `cd ~/workspace/reeve-desk-template-contrib && git fetch template && git checkout template/master && git reset --hard template/master`
- This ensures you're always starting from the latest template state

---

**Version**: 2.0 (Worktree Edition)
**Last Updated**: 2026-02-04
