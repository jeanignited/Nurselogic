package com.nurselogic.dao;

import com.nurselogic.config.JPAUtil;
import com.nurselogic.model.Usuario;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityTransaction;
import jakarta.persistence.NoResultException;
import jakarta.persistence.TypedQuery;

public class UsuarioDAO {

    public Usuario validarLogin(String correo, String clave) {
        EntityManager em = JPAUtil.getEntityManager();
        try {
            TypedQuery<Usuario> query = em.createQuery("SELECT u FROM Usuario u WHERE u.correo = :correo AND u.clave = :clave", Usuario.class);
            query.setParameter("correo", correo);
            query.setParameter("clave", clave);
            return query.getSingleResult();
        } catch (NoResultException e) {
            return null;
        } finally {
            em.close();
        }
    }

    public boolean registrarUsuario(Usuario u) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();

        try {
            tx.begin();
            em.persist(u);
            tx.commit();
            return true;
        } catch (Exception e) {
            if (tx.isActive()) {
                tx.rollback();
            }
            e.printStackTrace();
            return false;
        } finally {
            em.close();
        }
    }

    public Usuario buscarPorCorreo(String correo) {
        EntityManager em = JPAUtil.getEntityManager();
        try {
            TypedQuery<Usuario> query = em.createQuery("SELECT u FROM Usuario u WHERE u.correo = :correo", Usuario.class);
            query.setParameter("correo", correo);
            return query.getSingleResult();
        } catch (NoResultException e) {
            return null;
        } finally {
            em.close();
        }
    }

    public long contarPersonalMedico() {
        EntityManager em = JPAUtil.getEntityManager();
        try {
            return em.createQuery("SELECT COUNT(u) FROM Usuario u WHERE u.rol != 'Paciente'", Long.class).getSingleResult();
        } catch (Exception e) {
            return 0;
        } finally {
            em.close();
        }
    }

    public void actualizarUsuario(Usuario u) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            em.merge(u);
            tx.commit();
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            e.printStackTrace();
        } finally {
            em.close();
        }
    }

    public boolean eliminarUsuario(String correo) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            Usuario u = em.createQuery("SELECT u FROM Usuario u WHERE u.correo = :correo", Usuario.class)
                           .setParameter("correo", correo)
                           .getSingleResult();
            if (u != null) {
                em.remove(u);
            }
            tx.commit();
            return true;
        } catch (NoResultException e) {
            if (tx.isActive()) tx.rollback();
            return false;
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            e.printStackTrace();
            return false;
        } finally {
            em.close();
        }
    }

    public boolean actualizarRolUsuario(String correo, String nuevoRol) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            Usuario u = em.createQuery("SELECT u FROM Usuario u WHERE u.correo = :correo", Usuario.class)
                           .setParameter("correo", correo)
                           .getSingleResult();
            if (u != null) {
                u.setRol(nuevoRol);
                em.merge(u);
            }
            tx.commit();
            return true;
        } catch (NoResultException e) {
            if (tx.isActive()) tx.rollback();
            return false;
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            e.printStackTrace();
            return false;
        } finally {
            em.close();
        }
    }

    public boolean actualizarEspecialidadUsuario(String correo, String nuevaEspecialidad) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            Usuario u = em.createQuery("SELECT u FROM Usuario u WHERE u.correo = :correo", Usuario.class)
                           .setParameter("correo", correo)
                           .getSingleResult();
            if (u != null) {
                u.setEspecialidad(nuevaEspecialidad);
                em.merge(u);
            }
            tx.commit();
            return true;
        } catch (NoResultException e) {
            if (tx.isActive()) tx.rollback();
            return false;
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            e.printStackTrace();
            return false;
        } finally {
            em.close();
        }
    }
}