import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='latin-1') as f:
    c = f.read()

c = c.replace('canvas.offsetWidth', 'window.innerWidth')
c = c.replace('canvas.offsetHeight', 'window.innerHeight')

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='latin-1') as f:
    f.write(c)

print('Updated scripts.jsp canvas dimensions to window.inner')
