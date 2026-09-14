<%@ page contentType="application/json;charset=UTF-8" %>
<%@ page import="com.nurselogic.config.JPAUtil" %>
<%@ page import="com.nurselogic.model.Usuario" %>
<%@ page import="com.nurselogic.model.Paciente" %>
<%@ page import="jakarta.persistence.EntityManager" %>
<%@ page import="jakarta.persistence.NoResultException" %>
<%
    String cedula = request.getParameter("cedula");
    if (cedula == null || cedula.trim().isEmpty()) {
        out.print("{\"error\":\"C\u00e9dula no proporcionada\"}");
        return;
    }
    
    EntityManager em = null;
    boolean userExists = false;
    boolean patientExists = false;
    String nombres = "";
    String apellidos = "";
    
    try {
        em = JPAUtil.getEntityManager();
        
        Long userCount = em.createQuery("SELECT COUNT(u) FROM Usuario u WHERE u.cedula = :cedula", Long.class)
                           .setParameter("cedula", cedula)
                           .getSingleResult();
        if (userCount > 0) userExists = true;
        
        try {
            Paciente p = em.createQuery("SELECT p FROM Paciente p WHERE p.cedula = :cedula", Paciente.class)
                           .setParameter("cedula", cedula)
                           .getSingleResult();
            patientExists = true;
            nombres = p.getNombres();
            apellidos = p.getApellidos();
        } catch(NoResultException e) {}
    } catch(Exception e) {
    } finally {
        if (em != null) em.close();
    }
    
    out.print("{");
    out.print("\"userExists\": " + userExists + ",");
    out.print("\"patientExists\": " + patientExists + ",");
    out.print("\"nombres\": \"" + nombres.replace("\"", "\\\"").replace("\n", " ") + "\",");
    out.print("\"apellidos\": \"" + apellidos.replace("\"", "\\\"").replace("\n", " ") + "\"");
    out.print("}");
%>