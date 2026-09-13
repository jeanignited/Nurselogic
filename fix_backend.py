import io
with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'r', encoding='utf-8') as f:
    c = f.read()

new_method = '''
    public ActionResult eliminarMedicamento(String idStr) {
        if (idStr == null || idStr.trim().isEmpty()) return new ActionResult(false, "ID inv\u00E1lido.");
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            int id = Integer.parseInt(idStr);
            Medicamento med = em.find(Medicamento.class, id);
            if (med != null) {
                em.remove(med);
                tx.commit();
                return new ActionResult(true, "F\u00E1rmaco eliminado correctamente.");
            } else {
                tx.rollback();
                return new ActionResult(false, "F\u00E1rmaco no encontrado.");
            }
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            e.printStackTrace();
            return new ActionResult(false, "Error al eliminar el f\u00E1rmaco (quiz\u00E1s est\u00E1 siendo usado en facturas).");
        } finally {
            em.close();
        }
    }
'''
c = c.rsplit('}', 1)[0] + new_method + '\n}'
with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'w', encoding='utf-8') as f:
    f.write(c)

with io.open('src/main/java/com/nurselogic/controller/AdminActionServlet.java', 'r', encoding='utf-8') as f:
    s = f.read()
s = s.replace('} else if ("crearMedicamento".equals(action)) {', '} else if ("eliminarMedicamento".equals(action)) {\n                result = adminService.eliminarMedicamento(request.getParameter("id"));\n            } else if ("crearMedicamento".equals(action)) {')
with io.open('src/main/java/com/nurselogic/controller/AdminActionServlet.java', 'w', encoding='utf-8') as f:
    f.write(s)

print("Added eliminarMedicamento to backend")
