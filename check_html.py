import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

idx_start = text.find('<script>') + 8
idx_end = text.find('</script>', idx_start)
js = text[idx_start:idx_end]

lines = js.split('\n')
for i, line in enumerate(lines):
    if '<div' in line or '<td' in line:
        if "'" not in line and '"' not in line:
            print(f"Possible naked HTML at line {i}: {line}")
