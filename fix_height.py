import io
with io.open('src/main/webapp/views/estadisticas.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<div style="position: relative; height: 260px; width: 100%;">', '<div style="position: relative; height: 350px; width: 100%;">')

with io.open('src/main/webapp/views/estadisticas.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated chart height')
