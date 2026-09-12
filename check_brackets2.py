import sys
import re

with open('lint.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove comments and strings to check brackets!
js_clean = re.sub(r'//.*', '', js)
js_clean = re.sub(r'/\*.*?\*/', '', js_clean, flags=re.DOTALL)
js_clean = re.sub(r"'(?:\\.|[^'\\])*'", "''", js_clean)
js_clean = re.sub(r'"(?:\\.|[^"\\])*"', '""', js_clean)
js_clean = re.sub(r'(?:\\.|[^\\])*', '`', js_clean)

open_p = js_clean.count('(')
close_p = js_clean.count(')')
open_b = js_clean.count('{')
close_b = js_clean.count('}')
open_s = js_clean.count('[')
close_s = js_clean.count(']')

print(f"Parens: {open_p} - {close_p}")
print(f"Braces: {open_b} - {close_b}")
print(f"Squares: {open_s} - {close_s}")

