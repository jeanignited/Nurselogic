import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

idx = c.find('function buscarPacienteCama')
if idx != -1:
    print(c[idx:idx+1500])
else:
    print("Not found")
