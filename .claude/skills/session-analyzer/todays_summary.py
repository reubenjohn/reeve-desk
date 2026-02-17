#!/usr/bin/env python3
"""
Quick summary of today's sessions.
Usage: cat ~/.claude/projects/[PROJECT_HASH]/sessions-index.json | python3 todays_summary.py
"""
import json
import sys
from datetime import date

data = json.load(sys.stdin)
today = date.today().isoformat()

sessions = [e for e in data['entries'] if e.get('modified', '')[:10] == today]
total_msgs = sum(e.get('messageCount', 0) for e in sessions)

print(f'Sessions today: {len(sessions)}')
print(f'Total messages: {total_msgs}')
for s in sessions[:5]:
    print(f'  - {s["sessionId"][:8]}... ({s["messageCount"]} msgs): {s["summary"][:40]}...')
