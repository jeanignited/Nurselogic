import io
import re

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

old_query = '''                  String query = "SELECT f FROM Factura f WHERE 1=1";
                  if (desdeStr != null && !desdeStr.trim().isEmpty()) {
                      query += " AND f.fechaEmision >= '" + desdeStr + " 00:00:00'";
                  }
                  if (hastaStr != null && !hastaStr.trim().isEmpty()) {
                      query += " AND f.fechaEmision <= '" + hastaStr + " 23:59:59'";
                  }
                  query += " ORDER BY f.fechaEmision DESC";
                  
                  List<com.nurselogic.model.Factura> lista = em.createQuery(query, com.nurselogic.model.Factura.class).getResultList();'''

new_query = '''                  String queryStr = "SELECT f FROM Factura f WHERE 1=1";
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

c = c.replace(old_query, new_query)

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated ExportServlet with TypedQuery for dates')
