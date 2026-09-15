import io

with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'r', encoding='utf-8') as f:
    srv = f.read()

new_method = """
    public ActionResult eliminarRol(int id, boolean isAdmin) {
        if (!isAdmin) return new ActionResult(false, "Solo los administradores pueden eliminar roles.");
        RolDAO rolDao = new RolDAO();
        try {
            if (rolDao.eliminarRol(id)) {
                return new ActionResult(true, "Rol eliminado exitosamente.");
            }
            return new ActionResult(false, "No se encontró el rol.");
        } catch (Exception e) {
            return new ActionResult(false, e.getMessage());
        }
    }

    public ActionResult crearMedicamento"""

srv = srv.replace("    public ActionResult crearMedicamento", new_method)

with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'w', encoding='utf-8') as f:
    f.write(srv)
