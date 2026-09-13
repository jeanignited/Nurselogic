import io

with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix the unescaped quotes
c = c.replace('return "{"nombre": "" + pacientes.get(0).getNombres() + " " + pacientes.get(0).getApellidos() + ""}";', 'return "{\\"nombre\\": \\"" + pacientes.get(0).getNombres() + " " + pacientes.get(0).getApellidos() + "\\"}";')
c = c.replace('return "{"nombre": "" + facturas.get(0).getClienteNombre() + ""}";', 'return "{\\"nombre\\": \\"" + facturas.get(0).getClienteNombre() + "\\"}";')

with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed AdminService.java syntax error')
