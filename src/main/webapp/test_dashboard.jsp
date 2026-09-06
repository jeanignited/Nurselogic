<%@ page import="com.nurselogic.model.Paciente" %>
<%@ page import="com.nurselogic.config.JPAUtil" %>
<%@ page import="jakarta.persistence.EntityManager" %>
<%@ page import="java.util.List" %>
<%
    out.println("<h2>Testing JPA Fetch</h2>");
    try {
        EntityManager em = JPAUtil.getEntityManager();
        List<Paciente> pList = em.createQuery("SELECT p FROM Paciente p", Paciente.class).getResultList();
        out.println("<h3>Pacientes en JPA: " + pList.size() + "</h3><ul>");
        for(Paciente p : pList) {
            out.println("<li>" + p.getNombres() + " " + p.getApellidos() + " - " + p.getCedula() + "</li>");
        }
        out.println("</ul>");
        em.close();
    } catch (Exception e) {
        out.println("<p style='color:red;'>Error: " + e.getMessage() + "</p>");
        e.printStackTrace(new java.io.PrintWriter(out));
    }
%>

