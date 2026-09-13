import io, re

with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'r', encoding='utf-8') as f:
    c = f.read()

new_methods = '''
    public ActionResult procesarVentaCarrito(String payload, String cliente) {
        if (payload == null || payload.trim().isEmpty()) return new ActionResult(false, "El carrito est\u00E1 vac\u00EDo.");
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            Factura factura = new Factura();
            factura.setClienteNombre(cliente != null && !cliente.trim().isEmpty() ? cliente : "Consumidor Final");
            factura.setFechaEmision(java.time.LocalDateTime.now());
            factura.setTotal(0.0);
            em.persist(factura);

            double totalGral = 0.0;
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
            tx.commit();
            return new ActionResult(true, "Venta m\u00FAltiples items facturada exitosamente a " + factura.getClienteNombre());
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            e.printStackTrace();
            return new ActionResult(false, "Error interno al procesar el carrito.");
        } finally {
            em.close();
        }
    }

    public ActionResult ajustarStockMultiple(String payload) {
        if (payload == null || payload.trim().isEmpty()) return new ActionResult(false, "No hay f\u00E1rmacos seleccionados.");
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
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
            tx.commit();
            return new ActionResult(true, "Abastecimiento registrado correctamente.");
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            e.printStackTrace();
            return new ActionResult(false, "Error interno al abastecer bodega.");
        } finally {
            em.close();
        }
    }
}
'''

# Replace the very last closing brace of the file with the new methods
c = c.rsplit('}', 1)[0] + new_methods

with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated AdminService.java methods correctly!")
