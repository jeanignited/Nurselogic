<%@ page pageEncoding="UTF-8" %>
﻿<%@ page import="java.net.HttpURLConnection" %>
<%@ page import="java.net.URL" %>
<%@ page import="java.io.OutputStream" %>
<%@ page import="java.io.InputStreamReader" %>
<%@ page import="java.io.BufferedReader" %>
<%
    out.println("<h2>Testing POST to registroPaciente</h2>");
    try {
        URL url = new URL("http://localhost:8080/nurselogic/registroPaciente");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");

        String postData = "nombres=Juan&apellidos=Perez&cedula=1234567890&sexo=M&fechaNacimiento=1990-01-01&estatura=1.75&peso=75.0&temperatura=37.0&presion=120%2F80&fc=80&sat=98&enfermedad=Ninguna&alergias=Ninguna";
        
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

