import io
import re

with io.open('src/main/webapp/WEB-INF/web.xml', 'r', encoding='utf-8') as f:
    c = f.read()

c = re.sub(r'<error-page>.*?</error-page>', '', c, flags=re.DOTALL)

with io.open('src/main/webapp/WEB-INF/web.xml', 'w', encoding='utf-8') as f:
    f.write(c)

print('Removed error pages')
