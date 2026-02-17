# Preference Management Guidelines

How Reeve should use and maintain user preferences.

## When to Check Preferences

**Every decision.** Preferences are the override authority — they take precedence over Reeve's defaults and general directives. When in doubt about how to act, check here first.

See CLAUDE.md § Decision-Making Framework for the full hierarchy.

## How to Add New Preferences

When Reeve discovers a new preference (from user feedback, observed patterns, or explicit statements):
1. Add it to the appropriate section in [Preferences.md](Preferences.md)
2. Commit immediately
3. Log the discovery in [Knowledge/Diary/](../Knowledge/Diary/)

## Structure

Currently all preferences live in `Preferences.md`. If the file grows too large, split into domain-specific files (e.g., `Communication.md`, `Health.md`, `Calendar.md`).

## Related

- [CLAUDE.md](../CLAUDE.md) § Decision-Making Framework — How preferences fit in the priority hierarchy
- [Goals/Goals.md](../Goals/Goals.md) — Preferences should support, not contradict, active goals
