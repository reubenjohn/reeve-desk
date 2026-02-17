#!/usr/bin/env python3
"""
Bulk analysis of all sessions modified today.
Usage: cat ~/.claude/projects/[PROJECT_HASH]/sessions-index.json | python3 bulk_analysis.py
"""
import json
import sys
from datetime import date

data = json.load(sys.stdin)
today = date.today().isoformat()
sessions = [e for e in data['entries'] if e.get('modified', '')[:10] == today]

print(f"=== Session Analysis for {today} ===\n")
print(f"Total sessions: {len(sessions)}\n")

for s in sessions:
    sid = s['sessionId']
    print(f"## {sid[:8]}... - {s.get('summary', 'No summary')[:50]}")
    print(f"   Messages: {s.get('messageCount', 'N/A')}")
    print()
