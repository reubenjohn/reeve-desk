#!/usr/bin/env python3
"""
Get today's sessions from the sessions-index.json file.
Usage: cat ~/.claude/projects/[PROJECT_HASH]/sessions-index.json | python3 get_todays_sessions.py
"""
import json
import sys
from datetime import date

data = json.load(sys.stdin)
today = date.today().isoformat()

for entry in data['entries']:
    modified = entry.get('modified', '')[:10]
    if modified == today:
        print(f"{entry['sessionId']}|{entry['messageCount']}|{entry['summary'][:50]}...")
