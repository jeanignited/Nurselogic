import io
import re

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

c = re.sub(r'out\.println\("ID,Nombre F.*rmaco,Stock Actual,Estado"\);', 'out.println("ID;Nombre F\u00e1rmaco;Stock Actual;Estado");', c)
c = re.sub(r'out\.println\("ID,N.*mero Cama,Sala,Estado,Paciente,M.*dico a Cargo,Motivo"\);', 'out.println("ID;N\u00famero Cama;Sala;Estado;Paciente;M\u00e9dico a Cargo;Motivo");', c)

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)

print('Fixed headers')
