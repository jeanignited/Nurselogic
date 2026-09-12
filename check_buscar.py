import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

idx = c.find('buscarPacienteCita')
if idx != -1:
    print("Found at", idx)
else:
    print("Not found")
