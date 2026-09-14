import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'function evaluarVitales\(\) \{.*?(?=function)', c, re.DOTALL)
if m:
    with io.open('evaluar_func.txt', 'w', encoding='utf-8') as out:
        out.write(m.group(0))
