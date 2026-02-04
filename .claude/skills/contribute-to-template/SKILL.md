---
name: contribute-to-template
description: Contribute generic, reusable changes back to the public Reeve Desk template repo. Use when you have improvements (skills, CLAUDE.md refinements, documentation) that would benefit all users.
user-invocable: true
---

# Contribute to Template

Push generic improvements from your private desk back to the public `template` remote.

## When to Use

Invoke `/contribute-to-template` when you have:
- New skills that are generally useful (not personal workflows)
- CLAUDE.md improvements (clarifications, bug fixes, better examples)
- Documentation updates
- Structural improvements to the Desk

## What NOT to Contribute

Never push to template:
- Personal preferences (`Preferences/`)
- Your goals (`Goals/`)
- Diary entries (`Diary/`)
- User-specific customizations in CLAUDE.md (name, timezone, etc.)
- Credentials or API keys

## Workflow

### 1. Review What's Different

First, see what commits exist locally that aren't in template:

```bash
git fetch template
git log template/master..HEAD --oneline
```

### 2. Identify Template-Worthy Changes

For each commit, ask:
- Is this generic (useful to any Reeve user)?
- Does it contain personal information?
- Is it a standalone improvement?

**Good candidates:**
- `Add context-engineering skill`
- `Fix typo in CLAUDE.md pulse documentation`
- `Improve emergency-response skill workflow`

**Bad candidates:**
- `Customize for wellness coaching`
- `Add preference: morning workouts`
- `Update Goals for Q1`

### 3. Choose Contribution Method

**Option A: Cherry-pick specific commits**
For individual commits that are cleanly separable:

```bash
# Create a temporary branch from template
git checkout -b template-contribution template/master

# Cherry-pick the specific commit(s)
git cherry-pick <commit-hash>

# Push to template
git push template template-contribution:master

# Return to your branch
git checkout master
git branch -D template-contribution
```

**Option B: Push entire files/directories**
For new skills or complete file additions:

```bash
# Checkout just the file(s) you want to contribute
git checkout template/master
git checkout master -- .claude/skills/new-skill/

# Commit and push
git add .claude/skills/new-skill/
git commit -m "Add new-skill: description of what it does"
git push template HEAD:master

# Return to your branch
git checkout master
```

**Option C: Interactive selection**
When changes are mixed (some personal, some generic):

1. Create a clean branch from template
2. Manually copy over the generic changes
3. Commit with clear message
4. Push to template

### 4. Verify the Contribution

After pushing:

```bash
# Verify template has the changes
git log template/master --oneline -5

# Ensure your local still tracks origin (private)
git branch -vv
```

## Safety Checks

Before any push to template, verify:

1. **No personal data**: `git diff template/master HEAD -- <files>`
2. **Correct remote**: `git remote -v` (template should be the public repo)
3. **Clean commits**: Each commit has a clear, descriptive message

## Quick Reference

```bash
# See differences
git log template/master..HEAD --oneline

# See file differences
git diff template/master HEAD -- <path>

# Safe push (will fail if not fast-forward)
git push template <branch>:master

# Force push (use carefully!)
git push template +<commit>:master
```

## Example Session

```
User: /contribute-to-template

Reeve: Let me check what's available to contribute.

[Runs: git fetch template && git log template/master..HEAD --oneline]

Found 12 commits ahead of template. Analyzing...

**Template-worthy:**
1. `abc123` - Add context-engineering skill
2. `def456` - Fix pulse documentation typo

**Personal (skip):**
- `ghi789` - Customize for wellness coaching
- `jkl012` - Add morning workout preference

Would you like me to cherry-pick commits `abc123` and `def456` to template?
```

## Remotes Reference

| Remote | Repo | Purpose |
|--------|------|---------|
| `origin` | Private (reeve-desk-reubjohn) | Your personal desk |
| `template` | Public (reeve-desk) | Shared template |

Always push personal changes to `origin`, generic improvements to `template`.
