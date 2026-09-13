import io
import re

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

c = re.sub(r'out\.println\("ID;Nombres;.*?"\);', 'out.println("ID;Nombres;Apellidos;Cedula;Fecha Nacimiento;Sexo;Estatura;Peso;IMC;Enfermedad Preexistente;Alergias");', c)
c = re.sub(r'out\.println\("ID;Nombre F.*?rmaco;.*?"\);', 'out.println("ID;Nombre Farmaco;Stock Actual;Estado");', c)
c = re.sub(r'out\.println\("ID;Fecha;Hora;Especialidad;Paciente C.*?dula;Estado"\);', 'out.println("ID;Fecha;Hora;Especialidad;Paciente Cedula;Estado");', c)
c = re.sub(r'out\.println\("ID Factura;Fecha Emision;Cedula Cliente;Nombre Cliente;Detalle;Total"\);', 'out.println("ID Factura;Fecha Emision;Cedula Cliente;Nombre Cliente;Detalle;Total");', c)
c = re.sub(r'out\.println\("ID;N.*?mero Cama;Sala;Estado;Paciente;M.*?dico a Cargo;Motivo"\);', 'out.println("ID;Numero Cama;Sala;Estado;Paciente;Medico a Cargo;Motivo");', c)
c = re.sub(r'out\.println\("Error,Tipo de reporte no v.*?lido"\);', 'out.println("Error,Tipo de reporte no valido");', c)

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)

print('Cleaned headers in ExportServlet')
