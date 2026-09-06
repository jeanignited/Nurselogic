package com.nurselogic.config;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;

public class JPAUtil {
    private static final EntityManagerFactory entityManagerFactory;

    static {
        try {

            entityManagerFactory = Persistence.createEntityManagerFactory("nurselogicPU");
        } catch (Throwable ex) {
            System.err.println("Error al inicializar JPA: " + ex);
            throw new ExceptionInInitializerError(ex);
        }
    }

    public static EntityManager getEntityManager() {
        return entityManagerFactory.createEntityManager();
    }

    public static void cerrar() {
        if (entityManagerFactory != null) {
            entityManagerFactory.close();
        }
    }
}
