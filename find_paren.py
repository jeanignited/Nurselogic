import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    text = f.read()

idx_start = text.find('<script>') + 8
idx_end = text.find('</script>', idx_start)
js = text[idx_start:idx_end]

# remove comments and strings
js = re.sub(r'//.*', '', js)
js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
js = re.sub(r'"[^"]*"', '""', js)
js = re.sub(r"'[^']*'", "''", js)
js = re.sub(r'`[^`]*`', '``', js)

funcs = re.split(r'\n(?=function |window\.)', js)
for f in funcs:
    o = f.count('(')
    c = f.count(')')
    if o != c:
        print(f"Mismatch in chunk: {f[:50]}... -> open {o}, close {c}")
