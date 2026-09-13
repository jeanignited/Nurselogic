import re

with open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx_start = text.find('<script>') + 8
idx_end = text.find('</script>', idx_start)
js = text[idx_start:idx_end]

# Basic syntax checks
lines = js.split('\n')
for i, line in enumerate(lines):
    # Check for unterminated single line string
    # We strip comments to avoid false positives, but naively:
    line_no_comment = re.sub(r'//.*', '', line)
    if line_no_comment.count("'") % 2 != 0 or line_no_comment.count('"') % 2 != 0:
        print(f"Possible unclosed string at line {i+1}: {line_no_comment}")
