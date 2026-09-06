import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
with open('full_index.jsp', 'r', encoding='utf-16') as f:
    lines = f.readlines()

for i, line in enumerate(lines[:70]):
    print(line.rstrip('\n'))
