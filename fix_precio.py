import io, re

with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('med.getPrecioBase()', 'med.getPrecio()')

with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed getPrecioBase -> getPrecio")
