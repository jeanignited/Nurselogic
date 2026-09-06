<%@ page import="java.net.HttpURLConnection" %>
<%@ page import="java.net.URL" %>
<%@ page import="java.io.OutputStream" %>
<%
    out.println("<h2>Testing POST with exact user data</h2>");
    try {
        URL url = new URL("http://localhost:8080/nurselogic/registroPaciente");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");

        String postData = "nombres=Padre&apellidos=Prueba&cedula=0999999999&sexo=M&fechaNacimiento=1950-01-01&estatura=1.77&peso=80.3&temperatura=1111&presion=120%2F80&fc=100&sat=100&enfermedad=Diabetes&alergias=Penicilina";
        
        OutputStream os = conn.getOutputStream();
        os.write(postData.getBytes());
        os.flush();
        os.close();

        int responseCode = conn.getResponseCode();
        out.println("<p>Response Code: " + responseCode + "</p>");
        
    } catch (Exception e) {
        out.println("<p>Error: " + e.getMessage() + "</p>");
        e.printStackTrace(new java.io.PrintWriter(out));
    }
%>

