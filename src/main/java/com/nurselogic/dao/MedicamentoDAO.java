package com.nurselogic.dao;

import com.nurselogic.config.JPAUtil;
import com.nurselogic.model.LoteMedicamento;
import com.nurselogic.model.Medicamento;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityTransaction;
import java.util.ArrayList;
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

    /** Persiste un lote nuevo y actualiza el stock total del medicamento padre */
    public boolean guardarLote(LoteMedicamento lote) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            em.persist(lote);
            // Actualizar stock total del medicamento
            Medicamento med = em.find(Medicamento.class, lote.getMedicamento().getId());
            if (med != null) {
                med.setStock(med.getStock() + lote.getStockLote());
                em.merge(med);
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

    /** Lista lotes con stock > 0 para un medicamento, ordenados por caducidad FEFO */
    public List<LoteMedicamento> listarLotesPorMedicamento(int idMed) {
        EntityManager em = JPAUtil.getEntityManager();
        try {
            return em.createQuery(
                "SELECT l FROM LoteMedicamento l WHERE l.medicamento.id = :idMed ORDER BY l.fechaCaducidad ASC",
                LoteMedicamento.class)
                .setParameter("idMed", idMed)
                .getResultList();
        } catch (Exception e) {
            e.printStackTrace();
            return new ArrayList<>();
        } finally {
            em.close();
        }
    }

    /** Lista TODOS los lotes (incluido stock=0) para historial */
    public List<LoteMedicamento> listarTodosLosPorMedicamento(int idMed) {
        EntityManager em = JPAUtil.getEntityManager();
        try {
            return em.createQuery(
                "SELECT l FROM LoteMedicamento l WHERE l.medicamento.id = :idMed ORDER BY l.fechaCaducidad ASC",
                LoteMedicamento.class)
                .setParameter("idMed", idMed)
                .getResultList();
        } catch (Exception e) {
            e.printStackTrace();
            return new ArrayList<>();
        } finally {
            em.close();
        }
    }

    /** Descuenta cantidad de un lote especifico; actualiza stock del medicamento padre */
    public boolean descontarLote(int idLote, int cantidad) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            LoteMedicamento lote = em.find(LoteMedicamento.class, idLote);
            if (lote == null) { tx.rollback(); return false; }
            int nuevoStockLote = Math.max(0, lote.getStockLote() - cantidad);
            lote.setStockLote(nuevoStockLote);
            em.merge(lote);
            // Actualizar stock total del medicamento
            Medicamento med = em.find(Medicamento.class, lote.getMedicamento().getId());
            if (med != null) {
                int nuevoStock = Math.max(0, med.getStock() - cantidad);
                med.setStock(nuevoStock);
                em.merge(med);
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
