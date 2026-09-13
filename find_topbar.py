with open('src/main/webapp/includes/topbar.jsp', 'r', encoding='utf-8') as f:
    c = f.read()
import re
print(re.search(r'String nombreTop.*?</span>', c, re.DOTALL).group(0))
