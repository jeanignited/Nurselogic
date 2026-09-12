<%@ page pageEncoding="UTF-8" %>
﻿<%@ page import="com.nurselogic.config.JPAUtil" %>
<%@ page import="com.nurselogic.model.Enfermedad" %>
<%@ page import="com.nurselogic.model.Alergia" %>
<%@ page import="com.nurselogic.model.Medicamento" %>
<%@ page import="jakarta.persistence.EntityManager" %>
<%@ page import="jakarta.persistence.EntityTransaction" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Generador de Base de Datos</title>
</head>
<body style="background-color: #0f172a; color: white; font-family: sans-serif; text-align: center; padding-top: 50px;">
    <h2>Iniciando Inyección de Datos Médicos...</h2>
    <%
        EntityManager em = null;
        EntityTransaction tx = null;
        try {
            em = JPAUtil.getEntityManager();
            tx = em.getTransaction();
            tx.begin();

            try {
                em.createNativeQuery("ALTER TABLE medicamentos DROP COLUMN cantidad").executeUpdate();
                out.println("<p style='color: #10b981;'>✔️ Columna 'cantidad' eliminada para evitar conflictos.</p>");
            } catch (Exception ex) {
                // Ignore if the column doesn't exist
            }
            
            // Seed Medicamentos
            Long medCount = em.createQuery("SELECT COUNT(m) FROM Medicamento m", Long.class).getSingleResult();
            if (medCount == 0) {
                String[] nombres = {"Paracetamol 500mg", "Ibuprofeno 400mg", "Amoxicilina 500mg", "Omeprazol 20mg", "Loratadina 10mg", "Diclofenaco 50mg"};
                int[] stocks = {150, 120, 80, 200, 100, 90};
                for(int i=0; i<nombres.length; i++) {
                    Medicamento m = new Medicamento();
                    m.setNombre(nombres[i]);
                    m.setStock(stocks[i]);
                    em.persist(m);
                }
                out.println("<p style='color: #10b981;'>✔️ Medicamentos insertados correctamente.</p>");
            } else {
                out.println("<p style='color: #fbbf24;'>⚠️ Los medicamentos ya existían en la base de datos.</p>");
            }

            // Seed Enfermedades
            Long enfCount = em.createQuery("SELECT COUNT(e) FROM Enfermedad e", Long.class).getSingleResult();
            if (enfCount == 0) {
                em.persist(new Enfermedad("Hipertensión Arterial", "Presión arterial alta crónica."));
                em.persist(new Enfermedad("Diabetes Mellitus Tipo 2", "Nivel alto de azúcar."));
                em.persist(new Enfermedad("Asma Bronquial", "Enfermedad crónica respiratoria."));
                em.persist(new Enfermedad("Gastritis Aguda", "Inflamación del estómago."));
                em.persist(new Enfermedad("Anemia Ferropénica", "Falta de hierro."));
                out.println("<p style='color: #10b981;'>✔️ Enfermedades insertadas correctamente.</p>");
            } else {
                out.println("<p style='color: #fbbf24;'>⚠️ Las enfermedades ya existían en la base de datos.</p>");
            }

            // Seed Alergias
            Long aleCount = em.createQuery("SELECT COUNT(a) FROM Alergia a", Long.class).getSingleResult();
            if (aleCount == 0) {
                em.persist(new Alergia("Penicilina", "Alta"));
                em.persist(new Alergia("Aspirina", "Media"));
                em.persist(new Alergia("Ibuprofeno", "Baja"));
                em.persist(new Alergia("Polvo / Ácaros", "Leve"));
                em.persist(new Alergia("Mariscos", "Severa"));
                out.println("<p style='color: #10b981;'>✔️ Alergias insertadas correctamente.</p>");
            } else {
                out.println("<p style='color: #fbbf24;'>⚠️ Las alergias ya existían en la base de datos.</p>");
            }

            tx.commit();
            out.println("<h2>¡Operación Exitosa!</h2>");
            out.println("<p>Ya puedes volver al sistema haciendo clic <a href='dashboard' style='color: #3b82f6;'>aquí</a>.</p>");
        } catch (Exception e) {
            if (tx != null && tx.isActive()) tx.rollback();
            out.println("<h2 style='color: #ef4444;'>Error en la Base de Datos</h2>");
            out.println("<p>" + e.getMessage() + "</p>");
            e.printStackTrace();
        } finally {
            if (em != null) em.close();
        }
    %>
</body>
</html>

