import io, re

with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'r', encoding='utf-8') as f:
    c = f.read()

eliminar_metodo = '''
    public ActionResult eliminarFactura(String idStr) {
        if (idStr == null || idStr.trim().isEmpty()) return new ActionResult(false, "ID inv\u00e1lido.");
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            int id = Integer.parseInt(idStr);
            Factura f = em.find(Factura.class, id);
            if (f != null) {
                em.remove(f);
                tx.commit();
                return new ActionResult(true, "Factura eliminada correctamente.");
            } else {
                tx.rollback();
                return new ActionResult(false, "Factura no encontrada.");
            }
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            e.printStackTrace();
            return new ActionResult(false, "Error al eliminar factura.");
        } finally {
            em.close();
        }
    }
'''

# insert before the last brace
c = c[:c.rfind('}')] + eliminar_metodo + "\n}\n"

with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'w', encoding='utf-8') as f:
    f.write(c)

print("Added eliminarFactura")
