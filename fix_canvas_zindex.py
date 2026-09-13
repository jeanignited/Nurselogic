import io
import re

with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('z-index:-1;', 'z-index:0;')

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed globalParticles z-index in index.jsp')
