#!/bin/bash
# Query completed pulses from the pulse queue database for today
# Usage: ./query_pulses.sh

sqlite3 ~/.reeve/pulse_queue.db "
  SELECT id, status, prompt, execution_duration_ms, session_id, created_at, executed_at
  FROM pulses
  WHERE status = 'COMPLETED'
    AND date(created_at) = date('now')
  ORDER BY id DESC
"
