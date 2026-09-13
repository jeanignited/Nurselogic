import io
import re

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace Facturas block
facturas_pattern = r'String query = "SELECT f FROM Factura f WHERE 1=1";.*?List<com\.nurselogic\.model\.Factura> lista = em\.createQuery\(query, com\.nurselogic\.model\.Factura\.class\)\.getResultList\(\);'
facturas_replacement = '''String queryStr = "SELECT f FROM Factura f WHERE 1=1";
                if (desdeStr != null && !desdeStr.trim().isEmpty()) {
                    queryStr += " AND f.fechaEmision >= :desde";
                }
                if (hastaStr != null && !hastaStr.trim().isEmpty()) {
                    queryStr += " AND f.fechaEmision <= :hasta";
                }
                queryStr += " ORDER BY f.fechaEmision DESC";
                
                jakarta.persistence.TypedQuery<com.nurselogic.model.Factura> query = em.createQuery(queryStr, com.nurselogic.model.Factura.class);
                if (desdeStr != null && !desdeStr.trim().isEmpty()) {
                    query.setParameter("desde", java.time.LocalDateTime.parse(desdeStr + "T00:00:00"));
                }
                if (hastaStr != null && !hastaStr.trim().isEmpty()) {
                    query.setParameter("hasta", java.time.LocalDateTime.parse(hastaStr + "T23:59:59"));
                }
                List<com.nurselogic.model.Factura> lista = query.getResultList();'''
c = re.sub(facturas_pattern, facturas_replacement, c, flags=re.DOTALL)

# Replace Citas block
citas_pattern = r'out\.println\("ID,Fecha,Hora,Especialidad,Paciente C.dula,Estado"\);\s*List<Cita> lista = em\.createQuery\("SELECT c FROM Cita c ORDER BY c\.fecha DESC, c\.hora DESC", Cita\.class\)\.getResultList\(\);'
citas_replacement = '''out.println("ID;Fecha;Hora;Especialidad;Paciente C\\u01f8dula;Estado");
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
c = re.sub(citas_pattern, citas_replacement, c, flags=re.DOTALL)

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)
print('Regex replaced ExportServlet blocks')
