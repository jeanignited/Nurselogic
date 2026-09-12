import io
with io.open('src/main/webapp/includes/scripts.jsp', 'rb') as f:
    c = f.read()

idx = c.find(b'crearNuevaCama')
print(c[idx:idx+250])
