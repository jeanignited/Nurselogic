<%@ page import="java.sql.*" %>
<%
    out.println("<h2>Testing MySQL Pacientes Table</h2>");
    try {
        Class.forName("com.mysql.cj.jdbc.Driver");
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/nurselogic_db", "root", "Tobbysql2006.");
        
        // Let's see the columns
        DatabaseMetaData meta = conn.getMetaData();
        ResultSet rsColumns = meta.getColumns(null, null, "pacientes", null);
        out.println("<h3>Columnas en 'pacientes':</h3><ul>");
        while(rsColumns.next()) {
            out.println("<li>" + rsColumns.getString("COLUMN_NAME") + " - " + rsColumns.getString("TYPE_NAME") + "</li>");
        // Let's count
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT * FROM pacientes");
        int count = 0;
        out.println("<h3>Pacientes actuales:</h3><ul>");
        while(rs.next()) {
            out.println("<li>" + rs.getString("nombres") + " " + rs.getString("apellidos") + " (Ced: " + rs.getString("cedula") + ")</li>");
            count++;
        }
        out.println("</ul>");
        out.println("<p>Total registros: " + count + "</p>");

        // Test JPA Insert
        out.println("<h3>Testing JPA Insert:</h3>");
        try {
            com.nurselogic.model.Paciente p = new com.nurselogic.model.Paciente();
            p.setNombres("Test");
            p.setApellidos("Test");
            p.setCedula("0000000000");
            p.setSexo("M");
            p.setFechaNacimiento(java.time.LocalDate.now());
            p.setEstatura(1.70);
            p.setPeso(70.0);
            p.setTemperatura(37.0);
            p.setPresionArterial("120/80");
            p.setFrecuenciaCardiaca(80);
            p.setSaturacionOxigeno(98);
            
            boolean ok = new com.nurselogic.dao.PacienteDAO().registrarPaciente(p);
            out.println("<p>Insert successful? " + ok + "</p>");
        } catch(Exception ex) {
            out.println("<p style='color:red;'>JPA Error: " + ex.getMessage() + "</p>");
            ex.printStackTrace(new java.io.PrintWriter(out));
        }
        
        conn.close();
    } catch (Exception e) {
        out.println("<p style='color:red;'>Error: " + e.getMessage() + "</p>");
        e.printStackTrace(new java.io.PrintWriter(out));
    }
%>

