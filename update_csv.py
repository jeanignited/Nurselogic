import io

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace commas with semicolons in the headers and formats
c = c.replace('out.println("ID,Nombres,Apellidos,Cedula,Fecha Nacimiento,Sexo,Estatura,Peso,IMC,Enfermedad Preexistente,Alergias");', 'out.println("ID;Nombres;Apellidos;Cedula;Fecha Nacimiento;Sexo;Estatura;Peso;IMC;Enfermedad Preexistente;Alergias");')
c = c.replace('out.println(String.format("%d,\\"%s\\",\\"%s\\",\\"%s\\",\\"%s\\",\\"%s\\",%.2f,%.1f,%.2f,\\"%s\\",\\"%s\\"",', 'out.println(String.format("%d;\\"%s\\";\\"%s\\";\\"%s\\";\\"%s\\";\\"%s\\";%.2f;%.1f;%.2f;\\"%s\\";\\"%s\\"",')

c = c.replace('out.println("ID,Nombre F\u01edrmaco,Stock Actual,Estado");', 'out.println("ID;Nombre F\u01edrmaco;Stock Actual;Estado");')
c = c.replace('out.println(String.format("%d,\\"%s\\",%d,\\"%s\\"",', 'out.println(String.format("%d;\\"%s\\";%d;\\"%s\\"",')

c = c.replace('out.println("ID,Fecha,Hora,Especialidad,Paciente C\u01f8dula,Estado");', 'out.println("ID;Fecha;Hora;Especialidad;Paciente C\u01f8dula;Estado");')
c = c.replace('out.println(String.format("%d,\\"%s\\",\\"%s\\",\\"%s\\",\\"%s\\",\\"%s\\"",', 'out.println(String.format("%d;\\"%s\\";\\"%s\\";\\"%s\\";\\"%s\\";\\"%s\\"",')

c = c.replace('out.println("ID,N\u01e7mero Cama,Sala,Estado,Paciente,M\u01f8dico a Cargo,Motivo");', 'out.println("ID;N\u01e7mero Cama;Sala;Estado;Paciente;M\u01f8dico a Cargo;Motivo");')
c = c.replace('out.println(String.format("%d,\\"%s\\",\\"%s\\",\\"%s\\",\\"%s\\",\\"%s\\",\\"%s\\"",', 'out.println(String.format("%d;\\"%s\\";\\"%s\\";\\"%s\\";\\"%s\\";\\"%s\\";\\"%s\\"",')

c = c.replace('out.println("ID Factura,Fecha Emision,Cedula Cliente,Nombre Cliente,Detalle,Total");', 'out.println("ID Factura;Fecha Emision;Cedula Cliente;Nombre Cliente;Detalle;Total");')
c = c.replace('out.println(String.format("FAC-%05d,\\"%s\\",\\"%s\\",\\"%s\\",\\"%s\\",%.2f",', 'out.println(String.format("FAC-%05d;\\"%s\\";\\"%s\\";\\"%s\\";\\"%s\\";%.2f",')

# Also set the extension to .csv so they don't get a warning, but it's semicolon separated.
# Wait, actually, let's just make it semicolon separated.

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated ExportServlet.java with semicolons')
