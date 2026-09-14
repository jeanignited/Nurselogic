import io
import re

with io.open('src/main/webapp/login.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('padding: 3.5rem 3rem;', 'padding: 2.5rem 2rem;')

with io.open('src/main/webapp/login.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
