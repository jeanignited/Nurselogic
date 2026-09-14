import io
with io.open('src/main/java/com/nurselogic/controller/PacienteServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

old_json = '''                String json = String.format(
                    "{\\"encontrado\\": true, \\"id\\": %d, \\"nombres\\": \\"%s\\", \\"apellidos\\": \\"%s\\", \\"sexo\\": \\"%s\\", \\"fechaNacimiento\\": \\"%s\\", \\"enfermedad\\": \\"%s\\", \\"alergias\\": \\"%s\\", \\"presion\\": \\"%s\\", \\"estatura\\": %s, \\"peso\\": %s, \\"temperatura\\": %s, \\"fc\\": %d, \\"sat\\": %d}",
                    p.getId(), p.getNombres() != null ? p.getNombres() : "", 
                    p.getApellidos() != null ? p.getApellidos() : "", 
                    p.getSexo() != null ? p.getSexo() : "", 
                    p.getFechaNacimiento() != null ? p.getFechaNacimiento().toString() : "",
                    p.getEnfermedadPreexistente() != null ? p.getEnfermedadPreexistente() : "Ninguna",
                    p.getAlergias() != null ? p.getAlergias() : "Ninguna",
                    p.getPresionArterial() != null ? p.getPresionArterial() : "",
                    String.valueOf(p.getEstatura()),
                    String.valueOf(p.getPeso()),
                    String.valueOf(p.getTemperatura()),
                    p.getFrecuenciaCardiaca(),
                    p.getSaturacionOxigeno()
                );'''

new_json = '''                String json = String.format(
                    "{\\"encontrado\\": true, \\"id\\": %d, \\"nombres\\": \\"%s\\", \\"apellidos\\": \\"%s\\", \\"sexo\\": \\"%s\\", \\"fechaNacimiento\\": \\"%s\\", \\"enfermedad\\": \\"%s\\", \\"alergias\\": \\"%s\\", \\"presion\\": \\"%s\\", \\"estatura\\": %s, \\"peso\\": %s, \\"temperatura\\": %s, \\"fc\\": %d, \\"sat\\": %d, \\"glasgow\\": %s, \\"diagnosticoClinico\\": \\"%s\\"}",
                    p.getId(), p.getNombres() != null ? p.getNombres() : "", 
                    p.getApellidos() != null ? p.getApellidos() : "", 
                    p.getSexo() != null ? p.getSexo() : "", 
                    p.getFechaNacimiento() != null ? p.getFechaNacimiento().toString() : "",
                    p.getEnfermedadPreexistente() != null ? p.getEnfermedadPreexistente().replace("\\"", "\\\\\\"") : "Ninguna",
                    p.getAlergias() != null ? p.getAlergias().replace("\\"", "\\\\\\"") : "Ninguna",
                    p.getPresionArterial() != null ? p.getPresionArterial() : "",
                    String.valueOf(p.getEstatura()),
                    String.valueOf(p.getPeso()),
                    String.valueOf(p.getTemperatura()),
                    p.getFrecuenciaCardiaca(),
                    p.getSaturacionOxigeno(),
                    p.getGlasgow() != null ? String.valueOf(p.getGlasgow()) : "null",
                    p.getDiagnosticoClinico() != null ? p.getDiagnosticoClinico().replace("\\"", "\\\\\\"").replace("\\n", "\\\\n") : ""
                );'''

c = c.replace(old_json, new_json)

with io.open('src/main/java/com/nurselogic/controller/PacienteServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)
