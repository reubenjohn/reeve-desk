#!/usr/bin/env python3
"""
Compact one-liner style analysis of a session.
Usage: cat ~/.claude/projects/[PROJECT_HASH]/{SESSION_ID}.jsonl | python3 full_session_analysis.py

Output format: Messages: X (user: Y, assistant: Z) | Tools: N | Tokens: I in / O out | Duration: Xs | Feedback: F
"""
import json
import sys
from datetime import datetime

u, a, t, inp, out = 0, 0, 0, 0, 0
fb = []
t1, t2 = None, None

for line in sys.stdin:
    try:
        obj = json.loads(line)
    except:
        continue
    ts = obj.get('timestamp')
    if ts:
        if not t1:
            t1 = ts
        t2 = ts
    if obj.get('type') == 'user':
        u += 1
        c = obj.get('message', {}).get('content', '')
        if isinstance(c, str):
            for p in ['no,', 'wrong', 'actually', 'fix', 'error']:
                if p in c.lower():
                    fb.append(p)
                    break
    elif obj.get('type') == 'assistant':
        a += 1
        m = obj.get('message', {})
        for c in m.get('content', []):
            if isinstance(c, dict) and c.get('type') == 'tool_use':
                t += 1
        us = m.get('usage', {})
        inp += us.get('input_tokens', 0) + us.get('cache_creation_input_tokens', 0) + us.get('cache_read_input_tokens', 0)
        out += us.get('output_tokens', 0)

dur = 'N/A'
if t1 and t2:
    try:
        d1, d2 = datetime.fromisoformat(t1.replace('Z', '+00:00')), datetime.fromisoformat(t2.replace('Z', '+00:00'))
        dur = f'{int((d2-d1).total_seconds())}s'
    except:
        pass

print(f'Messages: {u+a} (user: {u}, assistant: {a}) | Tools: {t} | Tokens: {inp:,} in / {out:,} out | Duration: {dur} | Feedback: {len(fb)}')
