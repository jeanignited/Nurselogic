import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'<form action="agendarCita" method="post".*?</form>', c, re.DOTALL)
if m: print(m.group(0))
