import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

idx = c.find('function cambiarEstadoCita')
print(c[idx:idx+1000])
