#!/usr/bin/env python3
"""
Analyze a Claude Code session JSONL file for metrics.
Usage: cat ~/.claude/projects/[PROJECT_HASH]/{SESSION_ID}.jsonl | python3 analyze_session.py

Outputs:
- Message counts (user/assistant)
- Tool call count
- Token usage (input/output, including cache)
- Session duration
- Feedback signals detected
"""
import json
import sys
from datetime import datetime

# Counters
user_msgs = 0
assistant_msgs = 0
tool_calls = 0
total_input_tokens = 0
total_output_tokens = 0
first_timestamp = None
last_timestamp = None
feedback_patterns = [
    'no,', 'no ', 'wrong', 'actually', 'not what i', "that's not",
    'fix', 'error', 'mistake', "don't", 'should be', 'instead',
    'wait', 'stop', 'cancel', 'undo'
]
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
                        'snippet': content[:60].replace('\n', ' ')
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
    print(f'  - [{fb["pattern"]}] "{fb["snippet"]}..."')
