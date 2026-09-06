package com.nurselogic.util;

import com.nurselogic.config.JPAUtil;
import com.nurselogic.model.Medicamento;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityTransaction;

public class Seeder {

    public static void main(String[] args) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();

            System.out.println("Borrando medicamentos existentes...");
            // FacturaDetalle depends on Medicamento, so delete them first
            em.createQuery("DELETE FROM FacturaDetalle").executeUpdate();
            em.createQuery("DELETE FROM Medicamento").executeUpdate();
            
            // To be safe, let's reset the auto increment on Medicamento table
            em.createNativeQuery("ALTER TABLE medicamentos AUTO_INCREMENT = 1").executeUpdate();

            System.out.println("Insertando nuevos medicamentos...");
            
            Object[][] medicamentos = {
                {"Paracetamol 500mg (Caja x 100)", 250, 4.50},
                {"Ibuprofeno 400mg (Caja x 50)", 180, 5.25},
                {"Amoxicilina 500mg (Caja x 20)", 120, 8.75},
                {"Loratadina 10mg (Caja x 30)", 100, 3.50},
                {"Omeprazol 20mg (Caja x 28)", 150, 7.80},
                {"Losartán 50mg (Caja x 30)", 200, 9.20},
                {"Metformina 850mg (Caja x 60)", 175, 6.40},
                {"Azitromicina 500mg (Caja x 5)", 80, 12.00},
                {"Diclofenaco 50mg (Caja x 20)", 140, 4.10},
                {"Aspirina 100mg (Caja x 30)", 300, 2.90},
                {"Ceftriaxona 1g (Ampolla)", 50, 15.50},
                {"Clonazepam 2mg (Caja x 30)", 60, 18.00},
                {"Salbutamol Inhalador 100mcg", 90, 11.25},
                {"Vitamina C 1g (Caja x 10)", 110, 5.00},
                {"Tramadol 50mg (Caja x 20)", 70, 9.50}
            };

            for (Object[] medData : medicamentos) {
                Medicamento med = new Medicamento();
                med.setNombre((String) medData[0]);
                med.setStock((Integer) medData[1]);
                med.setPrecio((Double) medData[2]);
                em.persist(med);
                System.out.println("Insertado: " + med.getNombre());
            }

            tx.commit();
            System.out.println("¡Seeder ejecutado con éxito!");
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            System.err.println("Error al ejecutar el seeder: " + e.getMessage());
            e.printStackTrace();
        } finally {
            em.close();
            System.exit(0);
        }
    }
}
