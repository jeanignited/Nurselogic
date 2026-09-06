<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="com.nurselogic.config.JPAUtil" %>
<%@ page import="com.nurselogic.model.Medicamento" %>
<%@ page import="jakarta.persistence.EntityManager" %>
<%@ page import="jakarta.persistence.EntityTransaction" %>
<%
    EntityManager em = JPAUtil.getEntityManager();
    EntityTransaction tx = em.getTransaction();
    String msg = "";
    try {
        tx.begin();
        
        // Delete dependencies first
        em.createQuery("DELETE FROM FacturaDetalle").executeUpdate();
        em.createQuery("DELETE FROM Medicamento").executeUpdate();
        
        // Reset auto increment
        em.createNativeQuery("ALTER TABLE medicamentos AUTO_INCREMENT = 1").executeUpdate();

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
        }

        tx.commit();
        msg = "¡Base de datos poblada exitosamente! Se insertaron 15 medicamentos.";
    } catch (Exception e) {
        if (tx.isActive()) tx.rollback();
        msg = "Error al poblar BD: " + e.getMessage();
    } finally {
        em.close();
    }
%>
<!DOCTYPE html>
<html>
<head>
    <title>Ejecutando Seeder...</title>
    <style>body { font-family: sans-serif; background: #0f172a; color: white; text-align: center; padding: 50px; }</style>
</head>
<body>
    <h1>Resultados del Seeder</h1>
    <div style="padding: 20px; background: #1e293b; border-radius: 8px; display: inline-block; border: 1px solid #334155;">
        <h3 style="color: #10b981;"><%= msg %></h3>
        <p>Ya puedes volver al sistema. Los medicamentos de prueba fueron cargados.</p>
        <a href="dashboard" style="color: #38bdf8; text-decoration: none; font-weight: bold;">Volver al Dashboard</a>
    </div>
</body>
</html>

