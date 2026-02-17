# Google Workspace Runbook

## Quick Diagnosis

```python
# Fastest end-to-end auth + API test
mcp__google-workspace__list_calendars(user_google_email="[YOUR_EMAIL]")
```

If this succeeds → healthy. If "ACTION REQUIRED" → see troubleshooting below.

## Configuration

<!--
ONBOARDING: Fill in your actual values below.
-->

| Setting | Value |
|---------|-------|
| Email | `[YOUR_EMAIL]` |
| Credentials dir | `[YOUR_CREDENTIALS_DIR]` |
| OAuth port | `8100` |
| Tools enabled | gmail, calendar, contacts, drive |
| Mode | `--single-user` |
| Config file | `[YOUR_DESK_PATH]/.mcp.json` |

## Troubleshooting Auth Failures

### Step 1: Check for multiple MCP instances

```bash
ps aux | grep workspace-mcp | grep -v grep
```

**Multiple instances fight over the OAuth port.** OAuth callbacks go to whichever instance holds the port. Kill stale ones:

```bash
ps aux | grep workspace-mcp | grep -v grep | awk '{print $2}' | xargs -r kill
```

### Step 2: Check credential files

```bash
ls -la [YOUR_CREDENTIALS_DIR]
```

**CRITICAL: Single-user mode loads credentials alphabetically by filename.** If a stale credential file from the wrong email sorts first, it will always be loaded instead of the valid one.

**Fix:** Delete any credential files that aren't `[YOUR_EMAIL].json`.

### Step 3: Verify the credential is valid

```bash
python3 -c "
import json
from datetime import datetime
with open('[YOUR_CREDENTIALS_DIR]/[YOUR_EMAIL].json') as f:
    d = json.load(f)
print('Expiry:', d.get('expiry'))
print('Has refresh_token:', bool(d.get('refresh_token')))
print('Scopes:', len(d.get('scopes', [])))
"
```

**Test the refresh token manually:**
```bash
curl -s -X POST https://oauth2.googleapis.com/token \
  -d "client_id=[YOUR_CLIENT_ID]" \
  -d "client_secret=[YOUR_CLIENT_SECRET]" \
  -d "refresh_token=<REFRESH_TOKEN_FROM_FILE>" \
  -d "grant_type=refresh_token" | python3 -m json.tool
```

- `"access_token"` returned → refresh token valid, problem is elsewhere
- `"error": "invalid_grant"` → refresh token revoked, need full re-auth

### Step 4: Full re-auth flow (if refresh token is dead)

If the browser callback to `localhost:8100` may not work (e.g., running on WSL):

1. Kill all MCP instances (so none intercept the callback)
2. Trigger an auth URL by calling any Google Workspace tool
3. Copy the auth URL and open in browser
4. After approving, copy the full redirect URL from address bar
   (`http://localhost:8100/oauth2callback?code=...&state=...`)
5. Extract the `code` parameter and exchange manually:

```bash
curl -s -X POST https://oauth2.googleapis.com/token \
  -d "client_id=[YOUR_CLIENT_ID]" \
  -d "client_secret=[YOUR_CLIENT_SECRET]" \
  -d "code=<CODE_FROM_URL>" \
  -d "grant_type=authorization_code" \
  -d "redirect_uri=http://localhost:8100/oauth2callback" | python3 -m json.tool
```

6. Write the token file at `[YOUR_CREDENTIALS_DIR]/[YOUR_EMAIL].json`
7. Kill any MCP instances so the next tool call spawns fresh

### Credential file format

```json
{
  "token": "<access_token>",
  "refresh_token": "<refresh_token>",
  "token_uri": "https://oauth2.googleapis.com/token",
  "client_id": "[YOUR_CLIENT_ID]",
  "client_secret": "[YOUR_CLIENT_SECRET]",
  "scopes": [
    "https://www.googleapis.com/auth/gmail.compose",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/contacts.readonly",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/calendar.events",
    "https://www.googleapis.com/auth/contacts",
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/gmail.settings.basic",
    "https://www.googleapis.com/auth/userinfo.profile",
    "https://www.googleapis.com/auth/drive",
    "openid",
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/gmail.labels"
  ],
  "expiry": "<ISO datetime>"
}
```

## Common Failures

| Symptom | Cause | Fix |
|---------|-------|-----|
| Auth loop (keeps asking) | Stale credential file sorts first alphabetically | Delete non-`[YOUR_EMAIL]` files from credentials dir |
| Auth loop (valid creds ignored) | Multiple MCP instances, callback goes to wrong one | Kill all instances, retry |
| `Port 8100 already in use` | Stale MCP instance holding the port | `lsof -i :8100 -t \| xargs kill` |
| `invalid_grant` on refresh | Refresh token revoked (~7 days unused) | Full re-auth flow (Step 4) |
| Wrong credential dir | Code reads default path | `.mcp.json` sets `WORKSPACE_MCP_CREDENTIALS_DIR` |

## Tool Filtering Issue

The `--tools gmail calendar contacts drive` flag in `.mcp.json` **does not filter tool advertisement** — it only filters which tools are functional. All 50+ tools are still loaded into Claude's context. The deny list in `.claude/settings.json` blocks tools at execution time as a workaround.

## Related

- [../README.md](../README.md) — Infrastructure overview and health check workflow
