import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

idx_start = text.find('<script>') + 8
idx_end = text.find('</script>', idx_start)
js = text[idx_start:idx_end]

# let's just find the first character where the prefix has different open/close counts that stays different
lines = js.split('\n')
open_c = 0
close_c = 0
for i, line in enumerate(lines):
    line_no_comment = re.sub(r'//.*', '', line)
    open_c += line_no_comment.count('(')
    close_c += line_no_comment.count(')')
    if open_c - close_c < 0:
        print(f"Excess close parens at line {i}: {line}")
        break

print(f"Total open: {open_c}, Total close: {close_c}")
