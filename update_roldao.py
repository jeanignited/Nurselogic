import io

with io.open('src/main/java/com/nurselogic/dao/RolDAO.java', 'r', encoding='utf-8') as f:
    dao = f.read()

new_method = """
    public boolean eliminarRol(int id) throws Exception {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            Rol rol = em.find(Rol.class, id);
            if(rol != null) {
                em.remove(rol);
                tx.commit();
                return true;
            }
            return false;
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            throw new Exception("No se puede eliminar el rol. Es posible que existan usuarios asignados a el.", e);
        } finally {
            em.close();
        }
    }
}
"""

dao = dao.replace("}\n", new_method)

with io.open('src/main/java/com/nurselogic/dao/RolDAO.java', 'w', encoding='utf-8') as f:
    f.write(dao)
