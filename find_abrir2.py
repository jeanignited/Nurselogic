import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

idx = c.find('abrirModalVenta')
if idx != -1:
    print(c[idx-50:idx+800])
else:
    print("Not found")
