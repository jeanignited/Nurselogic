import sys
with open('lint.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

open_braces = 0
open_parens = 0
for i, line in enumerate(lines):
    for char in line:
        if char == '{': open_braces += 1
        elif char == '}': open_braces -= 1
        elif char == '(': open_parens += 1
        elif char == ')': open_parens -= 1
    if open_braces < 0:
        print(f"Negative braces at line {i+1}: {line.strip()}")
        break
    if open_parens < 0:
        print(f"Negative parens at line {i+1}: {line.strip()}")
        break

print(f"Final braces: {open_braces}, parens: {open_parens}")
