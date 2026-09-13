import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# I will replace the split(" ")[0] part with just the string itself.
c = c.replace('nombreBienvenida = nombreBienvenida.trim().split(" ")[0];', 'nombreBienvenida = nombreBienvenida.trim();')

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed dashboard.jsp name split')
