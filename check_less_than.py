import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

idx_start = text.find('<script>') + 8
idx_end = text.find('</script>', idx_start)
js = text[idx_start:idx_end]

lines = js.split('\n')
for i, line in enumerate(lines):
    if '<' in line:
        # Ignore lines with <%= %> or <% %> or string literals
        clean = re.sub(r'<%.*?%>', '', line)
        clean = re.sub(r'"[^"]*"', '', clean)
        clean = re.sub(r"'[^']*'", '', clean)
        if '<' in clean and not 'if (' in clean and not 'for (' in clean:
            print(f"Line {i}: {line.strip()}")
