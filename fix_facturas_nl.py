import io
with io.open('src/main/webapp/views/facturas.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(' gap-2\'>\n<button', ' gap-2\'><button')

with io.open('src/main/webapp/views/facturas.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
