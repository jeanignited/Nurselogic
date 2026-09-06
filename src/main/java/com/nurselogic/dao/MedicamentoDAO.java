package com.nurselogic.dao;

import com.nurselogic.config.JPAUtil;
import com.nurselogic.model.Medicamento;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityTransaction;
import java.util.List;

public class MedicamentoDAO {

    public List<Medicamento> listarTodos() {
        EntityManager em = JPAUtil.getEntityManager();
        try {
            return em.createQuery("SELECT m FROM Medicamento m ORDER BY m.nombre ASC", Medicamento.class).getResultList();
        } finally {
            em.close();
        }
    }

    public boolean guardarMedicamento(Medicamento m) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            em.persist(m);
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

    public boolean ajustarStock(int idMed, int cambio) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            Medicamento m = em.find(Medicamento.class, idMed);
            if (m != null) {
                int nuevoStock = m.getStock() + cambio;
                if (nuevoStock < 0) nuevoStock = 0;
                m.setStock(nuevoStock);
                em.merge(m);
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
}