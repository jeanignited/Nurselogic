import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

# find first script block
idx_start = text.find('<script>') + 8
idx_end = text.find('</script>', idx_start)
js_code = text[idx_start:idx_end]

# remove single-line comments
js_code = re.sub(r'//.*', '', js_code)
# remove multi-line comments
js_code = re.sub(r'/\*.*?\*/', '', js_code, flags=re.DOTALL)
# remove string literals
js_code = re.sub(r"'[^']*'", "''", js_code)
js_code = re.sub(r'"[^"]*"', '""', js_code)
js_code = re.sub(r'[^]*', '`', js_code)

open_b = js_code.count('{')
close_b = js_code.count('}')
print(f"Braces without strings: {open_b} open, {close_b} close. Diff = {open_b - close_b}")

open_p = js_code.count('(')
close_p = js_code.count(')')
print(f"Parens without strings: {open_p} open, {close_p} close. Diff = {open_p - close_p}")
