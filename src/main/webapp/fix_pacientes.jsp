<%@ page import="java.sql.*" %>
<%
    out.println("<h2>Fixing MySQL Pacientes Table</h2>");
    try {
        Class.forName("com.mysql.cj.jdbc.Driver");
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/nurselogic_db", "root", "Tobbysql2006.");
        Statement stmt = conn.createStatement();
        
        try { stmt.executeUpdate("ALTER TABLE pacientes DROP COLUMN edad"); out.println("<p>Dropped edad</p>"); } catch(Exception e) { out.println("<p>edad already dropped or err: " + e.getMessage() + "</p>"); }
        try { stmt.executeUpdate("ALTER TABLE pacientes DROP COLUMN frecuencia_respiratoria"); out.println("<p>Dropped frecuencia_respiratoria</p>"); } catch(Exception e) {}
        try { stmt.executeUpdate("ALTER TABLE pacientes DROP COLUMN glicemia"); out.println("<p>Dropped glicemia</p>"); } catch(Exception e) {}
        try { stmt.executeUpdate("ALTER TABLE pacientes DROP COLUMN enfermedad_preexistente"); out.println("<p>Dropped enfermedad_preexistente</p>"); } catch(Exception e) {}
        try { stmt.executeUpdate("ALTER TABLE pacientes DROP COLUMN presion_arterial"); out.println("<p>Dropped presion_arterial</p>"); } catch(Exception e) {}
        try { stmt.executeUpdate("ALTER TABLE pacientes DROP COLUMN frecuencia_cardiaca"); out.println("<p>Dropped frecuencia_cardiaca</p>"); } catch(Exception e) {}
        try { stmt.executeUpdate("ALTER TABLE pacientes DROP COLUMN saturacion_oxigeno"); out.println("<p>Dropped saturacion_oxigeno</p>"); } catch(Exception e) {}
        try { stmt.executeUpdate("ALTER TABLE pacientes DROP COLUMN fecha_registro"); out.println("<p>Dropped fecha_registro</p>"); } catch(Exception e) {}

        conn.close();
        out.println("<h3 style='color:green;'>SUCCESS: Old columns dropped!</h3>");
    } catch (Exception e) {
        out.println("<p style='color:red;'>Error: " + e.getMessage() + "</p>");
        e.printStackTrace(new java.io.PrintWriter(out));
    }
%>

