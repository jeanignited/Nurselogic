import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = re.sub(r'ctx\.fillStyle = .*?; // Cyan color', "ctx.fillStyle = 'rgba(56, 189, 248, ' + p.alpha + ')';", c)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed JS syntax error for particles')
