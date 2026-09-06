import json
import re

log_path = r'C:\Users\THINKPAD\.gemini\antigravity\brain\de7fed12-8d75-49e8-a537-8a7c9a758b82\.system_generated\logs\transcript_full.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'PLANNER_RESPONSE':
            tool_calls = data.get('tool_calls', [])
            for tc in tool_calls:
                args = tc.get('args', {})
                cmd = args.get('CommandLine', '')
                if 'include file="includes/sidebar.jsp"' in cmd:
                    print(cmd)
                    exit(0)
