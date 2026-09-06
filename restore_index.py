import os

with open('full_index.jsp', 'r', encoding='utf-16') as f:
    text = f.read()

with open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(text)
print('Restored index.jsp')
