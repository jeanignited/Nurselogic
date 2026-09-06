package com.nurselogic.dao;

import com.nurselogic.model.Factura;
import com.nurselogic.config.JPAUtil;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityTransaction;
import java.util.List;

public class FacturaDAO {

    public String guardarFactura(Factura factura) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            em.persist(factura);
            tx.commit();
            return "success";
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            e.printStackTrace();
            return "Error al guardar factura: " + e.getMessage();
        } finally {
            em.close();
        }
    }

    public List<Factura> listarFacturas() {
        EntityManager em = JPAUtil.getEntityManager();
        try {
            return em.createQuery("SELECT f FROM Factura f ORDER BY f.fechaEmision DESC", Factura.class).getResultList();
        } finally {
            em.close();
        }
    }
}
