import esprima
import re

c = open('src/main/webapp/login.jsp', 'r', encoding='utf-8', errors='ignore').read()
scripts = re.findall(r'<script>(.*?)</script>', c, flags=re.DOTALL)
for i, s in enumerate(scripts):
    try:
        esprima.parseScript(s)
        print(f"Script {i} OK")
    except Exception as e:
        print(f"Script {i} Error: {e}")
