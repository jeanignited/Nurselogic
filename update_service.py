import io, re

with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'r', encoding='utf-8') as f:
    c = f.read()

new_methods = '''
    public boolean procesarVentaCarrito(String payload, String cliente) {
        if (payload == null || payload.trim().isEmpty()) return false;
        EntityManager em = JpaUtil.getEntityManager();
        try {
            em.getTransaction().begin();
            Factura factura = new Factura();
            factura.setClienteNombre(cliente != null && !cliente.trim().isEmpty() ? cliente : "Consumidor Final");
            factura.setFechaEmision(java.time.LocalDateTime.now());
            factura.setTotal(0.0);
            em.persist(factura);

            double totalGral = 0.0;
            // payload format: "id1:cant1,id2:cant2"
            String[] items = payload.split(",");
            for (String item : items) {
                String[] parts = item.split(":");
                if (parts.length != 2) continue;
                int id = Integer.parseInt(parts[0]);
                int cant = Integer.parseInt(parts[1]);

                Medicamento med = em.find(Medicamento.class, id);
                if (med != null && med.getStock() >= cant) {
                    med.setStock(med.getStock() - cant);
                    em.merge(med);

                    FacturaDetalle det = new FacturaDetalle();
                    det.setFactura(factura);
                    det.setMedicamento(med);
                    det.setCantidad(cant);
                    det.setSubtotal(med.getPrecioBase() * cant);
                    em.persist(det);
                    totalGral += det.getSubtotal();
                }
            }
            factura.setTotal(totalGral);
            em.merge(factura);
            em.getTransaction().commit();
            return true;
        } catch (Exception e) {
            if (em.getTransaction().isActive()) em.getTransaction().rollback();
            e.printStackTrace();
            return false;
        } finally {
            em.close();
        }
    }

    public boolean ajustarStockMultiple(String payload) {
        if (payload == null || payload.trim().isEmpty()) return false;
        EntityManager em = JpaUtil.getEntityManager();
        try {
            em.getTransaction().begin();
            // payload format: "id1:cambio1,id2:cambio2"
            String[] items = payload.split(",");
            for (String item : items) {
                String[] parts = item.split(":");
                if (parts.length != 2) continue;
                int id = Integer.parseInt(parts[0]);
                int cambio = Integer.parseInt(parts[1]);

                Medicamento med = em.find(Medicamento.class, id);
                if (med != null) {
                    med.setStock(med.getStock() + cambio);
                    em.merge(med);
                }
            }
            em.getTransaction().commit();
            return true;
        } catch (Exception e) {
            if (em.getTransaction().isActive()) em.getTransaction().rollback();
            e.printStackTrace();
            return false;
        } finally {
            em.close();
        }
    }
'''

# Find a good place to insert it, maybe right before 'public boolean procesarVentaFarmacia'
c = c.replace('public boolean procesarVentaFarmacia', new_methods + '\n    public boolean procesarVentaFarmacia')

with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated AdminService.java")
