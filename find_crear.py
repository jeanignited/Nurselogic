import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()
idx = c.find('crearMedicamento')
print(c[max(0, idx-100):idx+500])
