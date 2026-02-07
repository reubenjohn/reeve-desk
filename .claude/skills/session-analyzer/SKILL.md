---
name: session-analyzer
description: Analyze Claude Code sessions for metrics and retrospection. Parses JSONL session files to extract message counts, tool usage, token consumption, and user feedback patterns. Used by daily-retrospection for budget tracking.
disable-model-invocation: false
---

# Session Analyzer

Analyze Claude Code sessions to extract metrics for retrospection and budget tracking.

## When to Use

- During daily/weekly retrospection to understand session costs
- To analyze specific sessions for debugging or review
- To track patterns in tool usage, token consumption, and user feedback
- For budget monitoring and cost optimization

## Data Sources

### 1. Pulse Queue Database

Location: `~/.reeve/pulse_queue.db`

Query completed pulses:
```bash
sqlite3 ~/.reeve/pulse_queue.db "
  SELECT id, status, prompt, execution_duration_ms, session_id, created_at, executed_at
  FROM pulses
  WHERE status = 'COMPLETED'
    AND date(created_at) = date('now')
  ORDER BY id DESC
"
```

**Note:** The `session_id` column in pulses table may be empty for some pulses. The actual session files are created by Claude Code independently.

### 2. Sessions Index

Location: `~/.claude/projects/[YOUR_PROJECT_HASH]/sessions-index.json`

Structure:
```json
{
  "version": 1,
  "entries": [
    {
      "sessionId": "uuid-here",
      "fullPath": "~/.claude/projects/[YOUR_PROJECT_HASH]/uuid.jsonl",
      "fileMtime": 1769190637807,
      "firstPrompt": "The initial prompt...",
      "summary": "Auto-generated summary",
      "messageCount": 4,
      "created": "2026-01-23T06:46:56.260Z",
      "modified": "2026-01-23T06:47:06.575Z",
      "gitBranch": "master",
      "projectPath": "[YOUR_DESK_PATH]",
      "isSidechain": false
    }
  ]
}
```

### 3. Session JSONL Files

Location: `~/.claude/projects/[YOUR_PROJECT_HASH]/{sessionId}.jsonl`

Each line is a JSON object. Key types:
- `"type": "user"` - User message
- `"type": "assistant"` - Assistant response (contains usage data)
- `"type": "progress"` - Progress events (hooks, etc.)
- `"type": "summary"` - Session summary

## Workflow

### Step 1: Get Today's Sessions

```bash
# Find sessions modified today
cat ~/.claude/projects/[YOUR_PROJECT_HASH]/sessions-index.json | python3 -c "
import json, sys
from datetime import datetime, date

data = json.load(sys.stdin)
today = date.today().isoformat()

for entry in data['entries']:
    modified = entry.get('modified', '')[:10]
    if modified == today:
        print(f\"{entry['sessionId']}|{entry['messageCount']}|{entry['summary'][:50]}...\")
"
```

### Step 2: Analyze a Session File

Use this Python script to parse session metrics:

```bash
cat ~/.claude/projects/[YOUR_PROJECT_HASH]/{SESSION_ID}.jsonl | python3 -c "
import json, sys

# Counters
user_msgs = 0
assistant_msgs = 0
tool_calls = 0
total_input_tokens = 0
total_output_tokens = 0
first_timestamp = None
last_timestamp = None
feedback_patterns = ['no,', 'no ', 'wrong', 'actually', 'not what i', \"that's not\",
                     'fix', 'error', 'mistake', \"don't\", 'should be', 'instead',
                     'wait', 'stop', 'cancel', 'undo']
feedback_signals = []

for line in sys.stdin:
    try:
        obj = json.loads(line)
    except:
        continue

    t = obj.get('type')
    ts = obj.get('timestamp')

    # Track timestamps for duration
    if ts:
        if not first_timestamp:
            first_timestamp = ts
        last_timestamp = ts

    if t == 'user':
        user_msgs += 1
        # Check for feedback patterns
        msg = obj.get('message', {})
        content = msg.get('content', '') if isinstance(msg.get('content'), str) else ''
        if content:
            content_lower = content.lower()
            for pattern in feedback_patterns:
                if pattern in content_lower:
                    feedback_signals.append({
                        'pattern': pattern,
                        'snippet': content[:60].replace('\\n', ' ')
                    })
                    break

    elif t == 'assistant':
        assistant_msgs += 1
        msg = obj.get('message', {})

        # Count tool calls
        content = msg.get('content', [])
        if isinstance(content, list):
            for c in content:
                if isinstance(c, dict) and c.get('type') == 'tool_use':
                    tool_calls += 1

        # Sum tokens
        usage = msg.get('usage', {})
        if usage:
            total_input_tokens += usage.get('input_tokens', 0)
            total_input_tokens += usage.get('cache_creation_input_tokens', 0)
            total_input_tokens += usage.get('cache_read_input_tokens', 0)
            total_output_tokens += usage.get('output_tokens', 0)

# Calculate duration
duration_str = 'N/A'
if first_timestamp and last_timestamp:
    from datetime import datetime
    try:
        t1 = datetime.fromisoformat(first_timestamp.replace('Z', '+00:00'))
        t2 = datetime.fromisoformat(last_timestamp.replace('Z', '+00:00'))
        duration_ms = int((t2 - t1).total_seconds() * 1000)
        duration_str = f'{duration_ms}ms ({duration_ms // 1000}s)'
    except:
        pass

print(f'Messages: {user_msgs + assistant_msgs} (user: {user_msgs}, assistant: {assistant_msgs})')
print(f'Tool calls: {tool_calls}')
print(f'Input tokens (incl cache): {total_input_tokens:,}')
print(f'Output tokens: {total_output_tokens:,}')
print(f'Duration: {duration_str}')
print(f'Feedback signals: {len(feedback_signals)}')
for fb in feedback_signals[:3]:
    print(f'  - [{fb[\"pattern\"]}] \"{fb[\"snippet\"]}...\"')
"
```

### Step 3: Generate Summary Report

After analyzing sessions, format the output:

```markdown
## Session Analysis: {session_id}
- Messages: X (user: Y, assistant: Z)
- Tool calls: N
- Input tokens: ~K (includes cache)
- Output tokens: M
- Duration: Xms
- Feedback signals: [list any detected]
```

## Quick One-Liner: Today's Sessions Summary

```bash
# Count today's sessions and total messages
cat ~/.claude/projects/[YOUR_PROJECT_HASH]/sessions-index.json | python3 -c "
import json, sys
from datetime import date

data = json.load(sys.stdin)
today = date.today().isoformat()

sessions = [e for e in data['entries'] if e.get('modified', '')[:10] == today]
total_msgs = sum(e.get('messageCount', 0) for e in sessions)

print(f'Sessions today: {len(sessions)}')
print(f'Total messages: {total_msgs}')
for s in sessions[:5]:
    print(f'  - {s[\"sessionId\"][:8]}... ({s[\"messageCount\"]} msgs): {s[\"summary\"][:40]}...')
"
```

## Quick One-Liner: Full Session Analysis

```bash
# Analyze specific session
SESSION_ID="your-session-id-here"
cat ~/.claude/projects/[YOUR_PROJECT_HASH]/${SESSION_ID}.jsonl | python3 << 'PYEOF'
import json, sys
from datetime import datetime

u, a, t, inp, out = 0, 0, 0, 0, 0
fb = []
t1, t2 = None, None

for line in sys.stdin:
    try: obj = json.loads(line)
    except: continue
    ts = obj.get('timestamp')
    if ts:
        if not t1: t1 = ts
        t2 = ts
    if obj.get('type') == 'user':
        u += 1
        c = obj.get('message', {}).get('content', '')
        if isinstance(c, str):
            for p in ['no,', 'wrong', 'actually', 'fix', 'error']:
                if p in c.lower(): fb.append(p); break
    elif obj.get('type') == 'assistant':
        a += 1
        m = obj.get('message', {})
        for c in m.get('content', []):
            if isinstance(c, dict) and c.get('type') == 'tool_use': t += 1
        us = m.get('usage', {})
        inp += us.get('input_tokens', 0) + us.get('cache_creation_input_tokens', 0) + us.get('cache_read_input_tokens', 0)
        out += us.get('output_tokens', 0)

dur = 'N/A'
if t1 and t2:
    try:
        d1, d2 = datetime.fromisoformat(t1.replace('Z', '+00:00')), datetime.fromisoformat(t2.replace('Z', '+00:00'))
        dur = f'{int((d2-d1).total_seconds())}s'
    except: pass

print(f'Messages: {u+a} (user: {u}, assistant: {a}) | Tools: {t} | Tokens: {inp:,} in / {out:,} out | Duration: {dur} | Feedback: {len(fb)}')
PYEOF
```

## Bulk Analysis: All Today's Sessions

```bash
cat ~/.claude/projects/[YOUR_PROJECT_HASH]/sessions-index.json | python3 << 'PYEOF'
import json, sys, subprocess
from datetime import date

data = json.load(sys.stdin)
today = date.today().isoformat()
sessions = [e for e in data['entries'] if e.get('modified', '')[:10] == today]

print(f"=== Session Analysis for {today} ===\n")
print(f"Total sessions: {len(sessions)}\n")

for s in sessions:
    sid = s['sessionId']
    path = s['fullPath']
    print(f"## {sid[:8]}... - {s.get('summary', 'No summary')[:50]}")
    print(f"   Messages: {s.get('messageCount', 'N/A')}")
    print()
PYEOF
```

## Token Cost Estimation

Rough pricing (check current rates):
- Claude Opus: ~$15/M input, ~$75/M output
- Claude Sonnet: ~$3/M input, ~$15/M output
- Cache reads are discounted ~90%

Formula for daily cost estimate:
```python
# Approximate cost calculation
input_cost = (input_tokens / 1_000_000) * 15  # Opus rate
output_cost = (output_tokens / 1_000_000) * 75
total_cost = input_cost + output_cost
print(f"Estimated cost: ${total_cost:.2f}")
```

## Feedback Pattern Detection

The analyzer looks for these signals that may indicate corrections or issues:

| Pattern | Interpretation |
|---------|---------------|
| "no," / "no " | Direct rejection |
| "wrong" | Error identified |
| "actually" | Correction incoming |
| "fix" / "error" | Problem found |
| "don't" / "stop" | Unwanted action |
| "should be" / "instead" | Correction |
| "undo" / "cancel" | Reversal needed |

High feedback signal counts may indicate:
- Misunderstanding user intent
- Errors in execution
- Need for better prompting
- Learning opportunities

## Skill Invocation Analysis

Detect which skills are being used across sessions:

```bash
python3 << 'EOF'
import json
from pathlib import Path
from collections import defaultdict

sessions_dir = Path.home() / ".claude/projects"
skill_sessions = defaultdict(list)  # skill_name -> [session_ids]
total_files = 0

for jsonl_file in sessions_dir.rglob("*.jsonl"):
    total_files += 1
    session_id = jsonl_file.stem

    try:
        for line in jsonl_file.read_text().splitlines():
            if not line.strip():
                continue
            record = json.loads(line)

            # Check assistant messages for Skill tool_use
            if record.get("type") == "assistant":
                content = record.get("message", {}).get("content", [])
                for block in content:
                    if block.get("type") == "tool_use" and block.get("name") == "Skill":
                        skill_name = block.get("input", {}).get("skill", "unknown")
                        skill_sessions[skill_name].append(session_id)
    except Exception:
        pass  # Skip malformed files

print(f"Total session files: {total_files}")
print(f"Sessions with Skill invocations: {sum(len(v) for v in skill_sessions.values())}")
print(f"\nSkill invocation counts:")
for skill, sessions in sorted(skill_sessions.items(), key=lambda x: -len(x[1])):
    print(f"  {skill}: {len(sessions)}")
EOF
```

## Integration with Daily Retrospection

Use this skill in `/daily-retrospection` to:
1. Get list of today's completed pulses
2. For each pulse with a session, analyze the JSONL
3. Aggregate totals (messages, tools, tokens, feedback)
4. Calculate estimated cost
5. Log insights to Diary/

Example output for retrospection:
```markdown
## Daily Session Metrics - 2026-02-05

| Metric | Value |
|--------|-------|
| Sessions | 8 |
| Total messages | 142 |
| Tool calls | 87 |
| Input tokens | ~1.2M |
| Output tokens | ~45K |
| Est. cost | $21.38 |
| Feedback signals | 3 |

Notable sessions:
- c431664c (87 msgs): Complex skill creation, 11 tool calls
- 33f86f7c (26 msgs): Morning briefing, standard flow

Feedback detected:
- [fix] in session abc123: "fix the formatting..."
```
