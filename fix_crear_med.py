import io
with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('name="nombre"', 'name="nombreMed"')
c = c.replace('name="stock"', 'name="stockMed"')
c = c.replace('name="precio"', 'name="precioMed"')

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print("Fixed modalCrearMedicamento params")
