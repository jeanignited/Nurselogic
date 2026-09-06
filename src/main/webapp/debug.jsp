<%@ page import="java.sql.*" %>
<%@ page import="javax.naming.*" %>
<%@ page import="javax.sql.*" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head><title>Debug DB</title></head>
<body>
<h1>Especialidades</h1>
<table border="1">
<tr><th>ID</th><th>Descripcion</th></tr>
<%
    Connection conn = null;
    try {
        Context initContext = new InitialContext();
        Context envContext  = (Context)initContext.lookup("java:/comp/env");
        DataSource ds = (DataSource)envContext.lookup("jdbc/nurselogicDB");
        conn = ds.getConnection();
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT * FROM especialidades");
        while (rs.next()) {
            out.println("<tr><td>" + rs.getInt(1) + "</td><td>" + rs.getString(2) + "</td></tr>");
        }
    } catch (Exception e) {
        out.println("<tr><td colspan='2'>Error: " + e.getMessage() + "</td></tr>");
        e.printStackTrace(new java.io.PrintWriter(out));
    }
%>
</table>

<h1>Pacientes</h1>
<table border="1">
<tr><th>ID</th><th>Nombres</th><th>Apellidos</th><th>Cedula</th></tr>
<%
    try {
        if (conn != null) {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT id_paciente, nombres, apellidos, cedula FROM pacientes");
            while (rs.next()) {
                out.println("<tr><td>" + rs.getInt(1) + "</td><td>" + rs.getString(2) + "</td><td>" + rs.getString(3) + "</td><td>" + rs.getString(4) + "</td></tr>");
            }
        }
    } catch (Exception e) {
        out.println("<tr><td colspan='4'>Error: " + e.getMessage() + "</td></tr>");
    } finally {
        if (conn != null) conn.close();
    }
%>
</table>
</body>
</html>

