import io
import re

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

old_citas_query = '''                  out.println("ID;Fecha;Hora;Especialidad;Paciente C\u01f8dula;Estado");
                  List<com.nurselogic.model.Cita> lista = em.createQuery("SELECT c FROM Cita c", com.nurselogic.model.Cita.class).getResultList();'''

new_citas_query = '''                  out.println("ID;Fecha;Hora;Especialidad;Paciente C\u01f8dula;Estado");
                  String desdeStr = request.getParameter("desde");
                  String hastaStr = request.getParameter("hasta");
                  String queryStr = "SELECT c FROM Cita c WHERE 1=1";
                  if (desdeStr != null && !desdeStr.trim().isEmpty()) {
                      queryStr += " AND c.fecha >= :desde";
                  }
                  if (hastaStr != null && !hastaStr.trim().isEmpty()) {
                      queryStr += " AND c.fecha <= :hasta";
                  }
                  queryStr += " ORDER BY c.fecha DESC, c.hora DESC";
                  
                  jakarta.persistence.TypedQuery<com.nurselogic.model.Cita> query = em.createQuery(queryStr, com.nurselogic.model.Cita.class);
                  if (desdeStr != null && !desdeStr.trim().isEmpty()) {
                      query.setParameter("desde", java.time.LocalDate.parse(desdeStr));
                  }
                  if (hastaStr != null && !hastaStr.trim().isEmpty()) {
                      query.setParameter("hasta", java.time.LocalDate.parse(hastaStr));
                  }
                  List<com.nurselogic.model.Cita> lista = query.getResultList();'''

c = c.replace(old_citas_query, new_citas_query)

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated ExportServlet for citas date range')
