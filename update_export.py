import io

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

facturas_block = '''            } else if ("facturas".equalsIgnoreCase(tipo)) {
                String desdeStr = request.getParameter("desde");
                String hastaStr = request.getParameter("hasta");
                out.println("ID Factura,Fecha Emision,Cedula Cliente,Nombre Cliente,Detalle,Total");
                
                String query = "SELECT f FROM Factura f WHERE 1=1";
                if (desdeStr != null && !desdeStr.trim().isEmpty()) {
                    query += " AND f.fechaEmision >= '" + desdeStr + " 00:00:00'";
                }
                if (hastaStr != null && !hastaStr.trim().isEmpty()) {
                    query += " AND f.fechaEmision <= '" + hastaStr + " 23:59:59'";
                }
                query += " ORDER BY f.fechaEmision DESC";
                
                List<com.nurselogic.model.Factura> lista = em.createQuery(query, com.nurselogic.model.Factura.class).getResultList();
                for (com.nurselogic.model.Factura f : lista) {
                    String detalles = "";
                    for (com.nurselogic.model.FacturaDetalle d : f.getDetalles()) {
                        detalles += d.getCantidad() + "x " + d.getMedicamentoNombre() + "; ";
                    }
                    out.println(String.format("FAC-%05d,\\"%s\\",\\"%s\\",\\"%s\\",\\"%s\\",%.2f",
                            f.getId(), f.getFechaEmision().toString(), 
                            f.getClienteCedula() != null ? f.getClienteCedula() : "",
                            f.getClienteNombre() != null ? f.getClienteNombre() : "",
                            detalles, f.getTotal()));
                }
            } else if ("camas"'''

c = c.replace('} else if ("camas"', facturas_block)

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated ExportServlet.java')
