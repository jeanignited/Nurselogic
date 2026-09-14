import io
import re

with io.open('src/main/webapp/views/agenda.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = re.sub(
    r'abrirModalVerDiagnostico\(\'\" \+ c\.get\(\"paciente\"\) \+ \"\', this\)',
    r'abrirModalVerDiagnostico(\'\" + c.get(\"paciente\") + \"\', \'\" + c.get(\"cedula\") + \"\', this)',
    c
)

with io.open('src/main/webapp/views/agenda.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated agenda.jsp via regex")
