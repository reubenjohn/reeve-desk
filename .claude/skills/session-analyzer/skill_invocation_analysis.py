#!/usr/bin/env python3
"""
Analyze skill invocations across all sessions.
Usage: python3 skill_invocation_analysis.py

Scans all session JSONL files and counts Skill tool invocations.
"""
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
