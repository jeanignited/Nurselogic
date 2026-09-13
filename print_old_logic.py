import re

with open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

matches = re.finditer(r'let formattedDiag = rawDiag\.replace.*?</div\>\';', c, re.DOTALL)
for m in matches:
    print(repr(m.group(0)))
