import io
import re

with io.open('src/main/java/com/nurselogic/model/Paciente.java', 'r', encoding='utf-8') as f:
    c = f.read()

# Add receta field
new_field = '''    @Column(name = "receta", columnDefinition = "TEXT")
    private String receta;

    public String getReceta() { return receta; }
    public void setReceta(String receta) { this.receta = receta; }

}'''
c = re.sub(r'\}$', new_field, c)

with io.open('src/main/java/com/nurselogic/model/Paciente.java', 'w', encoding='utf-8') as f:
    f.write(c)

# Add to PacienteServlet
with io.open('src/main/java/com/nurselogic/controller/PacienteServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

new_param = '''            String receta = request.getParameter("receta");
            if (receta != null && !receta.trim().isEmpty()) {
                p.setReceta(receta);
            }
            if (isNew) {'''
c = c.replace('            if (isNew) {', new_param)

with io.open('src/main/java/com/nurselogic/controller/PacienteServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)
