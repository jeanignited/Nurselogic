import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()

idx = c.find('function cambiarVista')
print(c[idx:idx+800])
