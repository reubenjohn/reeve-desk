---
name: contribute-to-template
description: Push generic improvements from your private desk back to the public template remote using git worktrees for safe, isolated editing. Use when you have improvements (skills, CLAUDE.md refinements, documentation) that would benefit all users.
user-invocable: true
---

# Contribute to Template

Push generic improvements from your private desk back to the public `template` remote using git worktrees for safe, isolated editing.

## When to Use

Invoke `/contribute-to-template` when you have:
- New skills that are generally useful (not personal workflows)
- CLAUDE.md improvements (clarifications, bug fixes, better examples)
- Documentation updates
- Structural improvements to the Desk
- New rules in `.claude/rules/`

## What NOT to Contribute

Never push to template:
- Personal preferences (`Preferences/`)
- Your goals (`Goals/`)
- Diary entries (`Diary/`)
- User-specific customizations in CLAUDE.md (name, timezone, specific goals)
- Credentials or API keys

## Workflow Using Git Worktrees

Git worktrees allow you to work on the template in a separate directory without affecting your main desk. This is especially important when:
- Pulses are running and modifying your current desk
- You want to test template changes in isolation
- You need to carefully review what you're contributing

### 1. Set Up the Worktree (First Time)

```bash
# Ensure template remote is configured
git remote -v | grep template
# If not present: git remote add template git@github.com:YOUR_USERNAME/reeve-desk.git

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

# Stage and commit
git add .
git commit -m "Add [feature]: description of what it does"

# Push to template (worktree tracks template/master, so push to origin)
git push origin HEAD:master
```

### 6. Verify and Clean Up

```bash
# Verify template has the changes
git log --oneline -5

# Return to your main desk
cd ~/reeve_desk

# Optionally remove the worktree when done
# git worktree remove ~/workspace/reeve-desk-template-contrib
```

## Safety Checks

Before any push to template, verify:

1. **No personal data**: Review all files being committed
2. **Correct directory**: You're in the worktree, not your main desk
3. **Clean commits**: Each commit has a clear, descriptive message
4. **Placeholders used**: User-specific values are templated

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
git fetch origin
git reset --hard origin/master
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

Ready to commit:
- `.claude/skills/context-engineering/SKILL.md`
- `.claude/rules/self-awareness.md`
- `CLAUDE.md` (with [USER_NAME] placeholders)

Push these to template?
```

## Remotes Reference

| Remote | Repo | Purpose |
|--------|------|---------|
| `origin` | Private (your-desk-repo) | Your personal desk |
| `template` | Public (reeve-desk) | Shared template |

**In your main desk:** `origin` = private, `template` = public
**In the worktree:** `origin` = public template (because it was created from `template/master`)

Always push personal changes to your main desk's `origin`, generic improvements through the worktree.

## Maintaining the Worktree

If you contribute frequently:
- Keep the worktree around (`~/workspace/reeve-desk-template-contrib`)
- Periodically fetch and reset: `cd ~/workspace/reeve-desk-template-contrib && git fetch origin && git reset --hard origin/master`
- This ensures you're always starting from the latest template state

---

**Version**: 2.0 (Worktree Edition)
**Last Updated**: 2026-02-04
