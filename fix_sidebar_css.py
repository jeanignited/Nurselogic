import io
import re

with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('overflow-y:auto;', 'overflow:hidden; display:flex; flex-direction:column;')

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated index.jsp sidebar CSS')
