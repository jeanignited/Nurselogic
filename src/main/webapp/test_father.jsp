<%@ page import="java.io.BufferedReader" %>
<%@ page import="java.io.InputStreamReader" %>
<%@ page import="java.net.HttpURLConnection" %>
<%@ page import="java.net.URL" %>
<%@ page import="java.net.URLEncoder" %>
<%
    out.println("<h2>Testing Submission...</h2>");
    try {
        URL url = new URL("http://localhost:8080/nurselogic/registroPaciente");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");

        String postData = "nombres=" + URLEncoder.encode("Nombre Padre", "UTF-8") +
                          "&apellidos=" + URLEncoder.encode("Apellido Padre", "UTF-8") +
                          "&cedula=1711516391" +
                          "&fechaNacimiento=1970-08-30" +
                          "&sexo=M" +
                          "&enfermedad=Ninguna" +
                          "&alergias=Ninguna" +
                          "&estatura=1.77" +
                          "&peso=84.5" +
                          "&temperatura=36.5" +
                          "&presion=120%2F80" +
                          "&fc=100" +
                          "&sat=100";
        
        conn.getOutputStream().write(postData.getBytes("UTF-8"));

        int code = conn.getResponseCode();
        out.println("<p>Code: " + code + "</p>");
        
    } catch (Exception e) {
        out.println("<p>Error: " + e.getMessage() + "</p>");
    }
%>

