import io
import re
import subprocess

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Strip JSP tags to just get valid JS
c = re.sub(r'<%.*?%>', 'null', c, flags=re.DOTALL)
c = re.sub(r'<%@.*?%>', '', c)

scripts = re.findall(r'<script>(.*?)</script>', c, flags=re.DOTALL)
if scripts:
    with io.open('test_syntax.js', 'w', encoding='utf-8') as f:
        f.write(scripts[0])
        
    print("Saved test_syntax.js")
