import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace data.cedula with cedula
c = re.sub(r'data\.cedula', 'cedula', c)

# Replace data.presionArterial with data.presion
c = re.sub(r'data\.presionArterial', 'data.presion', c)

# Replace data.frecuenciaCardiaca with data.fc
c = re.sub(r'data\.frecuenciaCardiaca', 'data.fc', c)

# Replace data.saturacionOxigeno with data.sat
c = re.sub(r'data\.saturacionOxigeno', 'data.sat', c)

# Replace data.enfermedades with data.enfermedad
c = re.sub(r'data\.enfermedades', 'data.enfermedad', c)

# Handle 0.0 values or 'null' values in ternary operators
c = c.replace("(data.estatura || '--')", "(data.estatura && data.estatura !== '0.0' ? data.estatura : '--')")
c = c.replace("(data.peso || '--')", "(data.peso && data.peso !== '0.0' ? data.peso : '--')")
c = c.replace("(data.temperatura || '--')", "(data.temperatura && data.temperatura !== '0.0' ? data.temperatura : '--')")
c = c.replace("(data.fc || '--')", "(data.fc && data.fc !== 0 ? data.fc : '--')")
c = c.replace("(data.sat || '--')", "(data.sat && data.sat !== 0 ? data.sat : '--')")
c = c.replace("data.enfermedad && data.enfermedad.length > 0 ? data.enfermedad : 'Ninguna registrada'", "data.enfermedad && data.enfermedad !== 'null' && data.enfermedad !== 'Ninguna' ? data.enfermedad : 'Ninguna registrada'")
c = c.replace("data.alergias && data.alergias.length > 0 ? data.alergias : 'Ninguna registrada'", "data.alergias && data.alergias !== 'null' && data.alergias !== 'Ninguna' ? data.alergias : 'Ninguna registrada'")

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed variables")
