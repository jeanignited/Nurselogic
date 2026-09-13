import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

offset = c.find('Introduce tus datos')
end_idx = c.find('</div>', offset)
end_idx = c.find('</div>', end_idx+1)
end_idx = c.find('</div>', end_idx+1)
end_idx = c.find('</div>', end_idx+1)

print("Snippet right after the cards end:")
print(c[end_idx:end_idx+200])

