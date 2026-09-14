import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('validarSignos();', '')
c = re.sub(r'function validarSignos\(\) \{.*?(?=let grabador;)', '', c, flags=re.DOTALL)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("validarSignos removed")
