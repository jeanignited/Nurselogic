package com.nurselogic.dao;

import com.nurselogic.config.JPAUtil;
import com.nurselogic.model.Cita;
import com.nurselogic.model.Especialidad;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityTransaction;
import java.util.List;

public class CitaDAO {

    public String agendarCita(Cita cita) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();

        try {
            tx.begin();
            em.persist(cita);
            tx.commit();
            return "OK";
        } catch (Exception e) {
            if (tx.isActive()) {
                tx.rollback();
            }
            e.printStackTrace();
            String rootCause = e.getMessage();
            if (e.getCause() != null) {
                rootCause += " | " + e.getCause().getMessage();
            }
            return rootCause;
        } finally {
            if (em.isOpen()) {
                em.close();
            }
        }
    }

    public List<Especialidad> listarEspecialidades() {
        EntityManager em = JPAUtil.getEntityManager();
        try {
            return em.createQuery("SELECT e FROM Especialidad e", Especialidad.class).getResultList();
        } finally {
            em.close();
        }
    }

    public List<Cita> listarCitas() {
        EntityManager em = JPAUtil.getEntityManager();
        try {
            return em.createQuery("SELECT c FROM Cita c ORDER BY c.fecha DESC, c.hora ASC", Cita.class).getResultList();
        } finally {
            em.close();
        }
    }

    public boolean actualizarEstadoCita(int idCita, String nuevoEstado) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            Cita c = em.find(Cita.class, idCita);
            if (c != null) {
                c.setEstado(nuevoEstado);
                em.merge(c);
            }
            tx.commit();
            return true;
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            e.printStackTrace();
            return false;
        } finally {
            em.close();
        }
    }

    public String obtenerRecetaUnificada(int idCita, String recetaTextoLibre) {
        EntityManager em = JPAUtil.getEntityManager();
        StringBuilder recetaEstructurada = new StringBuilder();
        try {
            // Intenta consultar la tabla mencionada por el usuario (puede ser por script externo)
            List<Object[]> meds = em.createNativeQuery(
                "SELECT m.nombre, rm.cantidad FROM recetas_medicamentos rm " +
                "JOIN medicamentos m ON rm.medicamento_id = m.id " +
                "WHERE rm.cita_id = :idCita")
                .setParameter("idCita", idCita)
                .getResultList();
                
            for (Object[] row : meds) {
                String medName = (String) row[0];
                Number cant = (Number) row[1];
                recetaEstructurada.append(medName).append(" - ").append(cant).append(" unidad(es). ");
            }
        } catch (Exception e) {
            // Si la tabla o la columna tiene otro nombre y falla, ignora y conserva el texto libre
        } finally {
            if (em.isOpen()) {
                em.close();
            }
        }
        
        String finalReceta = (recetaTextoLibre != null) ? recetaTextoLibre.trim() : "";
        if (recetaEstructurada.length() > 0) {
            if (!finalReceta.isEmpty()) {
                finalReceta = recetaEstructurada.toString() + "Indicaciones adicionales: " + finalReceta;
            } else {
                finalReceta = recetaEstructurada.toString();
            }
        }
        return finalReceta.isEmpty() ? "Ninguna" : finalReceta;
    }
}