import os

with open('full_index.jsp', 'r', encoding='utf-16') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '</style>' in line:
        print(f"Style ends at line {i}")
        break
