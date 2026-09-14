import io

with io.open('src/main/webapp/views/agenda.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    r'abrirModalVerDiagnostico(\'\" + c.get(\"paciente\") + \"\', \'\" + c.get(\"cedula\") + \"\', this)',
    'abrirModalVerDiagnostico(\'" + c.get("paciente") + "\', \'" + c.get("cedula") + "\', this)'
)

with io.open('src/main/webapp/views/agenda.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
