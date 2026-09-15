package com.nexusmed.dao;

import com.nexusmed.model.Rol;
import com.nexusmed.config.JPAUtil;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityTransaction;

public class RolDAO {

    public boolean guardarRol(Rol rol) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            em.persist(rol);
            tx.commit();
            return true;
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            return false;
        } finally {
            em.close();
        } // <--- 1. Esta llave cierra el bloque 'finally'
    } // <--- 2. Esta llave cierra el método 'guardarRol'

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
    
