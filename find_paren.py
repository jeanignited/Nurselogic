import sys
with open('lint.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

stack = []
for i, line in enumerate(lines):
    # simple parsing ignoring strings for a moment
    in_str = False
    str_char = ''
    escape = False
    for j, char in enumerate(line):
        if escape:
            escape = False
            continue
        if char == '\\':
            escape = True
            continue
        if in_str:
            if char == str_char:
                in_str = False
            continue
        if char in ('"', "'", ''):
            in_str = True
            str_char = char
            continue
        
        if char == '(':
            stack.append((i+1, j+1, line.strip()))
        elif char == ')':
            if stack:
                stack.pop()
            else:
                pass

for item in stack:
    print(f"Unclosed parenthesis at line {item[0]}: {item[2]}")
