package com.nurselogic.controller;

import com.nurselogic.dao.PacienteDAO;
import com.nurselogic.model.Paciente;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

@WebServlet("/registroPaciente")
public class PacienteServlet extends HttpServlet {
    private PacienteDAO dao = new PacienteDAO();

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String action = request.getParameter("action");
        if ("buscarCedula".equals(action)) {
            String cedula = request.getParameter("cedula");
            Paciente p = dao.buscarPorCedula(cedula);
            
            response.setContentType("application/json");
            response.setCharacterEncoding("UTF-8");
            PrintWriter out = response.getWriter();
            
            if (p != null) {
                String json = String.format(
                    "{\"encontrado\": true, \"id\": %d, \"nombres\": \"%s\", \"apellidos\": \"%s\", \"sexo\": \"%s\", \"fechaNacimiento\": \"%s\", \"enfermedad\": \"%s\", \"alergias\": \"%s\", \"presion\": \"%s\", \"estatura\": %s, \"peso\": %s, \"temperatura\": %s, \"fc\": %d, \"sat\": %d}",
                    p.getId(), p.getNombres() != null ? p.getNombres() : "", 
                    p.getApellidos() != null ? p.getApellidos() : "", 
                    p.getSexo() != null ? p.getSexo() : "", 
                    p.getFechaNacimiento() != null ? p.getFechaNacimiento().toString() : "",
                    p.getEnfermedadPreexistente() != null ? p.getEnfermedadPreexistente() : "Ninguna",
                    p.getAlergias() != null ? p.getAlergias() : "Ninguna",
                    p.getPresionArterial() != null ? p.getPresionArterial() : "",
                    String.valueOf(p.getEstatura()),
                    String.valueOf(p.getPeso()),
                    String.valueOf(p.getTemperatura()),
                    p.getFrecuenciaCardiaca(),
                    p.getSaturacionOxigeno()
                );
                out.print(json);
            } else {
                out.print("{\"encontrado\": false}");
            }
            out.flush();
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        try {
            String cedula = request.getParameter("cedula");
            Paciente p = dao.buscarPorCedula(cedula);
            boolean isNew = false;
            
            if (p == null) {
                p = new Paciente();
                p.setCedula(cedula);
                isNew = true;
            }
            
            p.setNombres(request.getParameter("nombres"));
            p.setApellidos(request.getParameter("apellidos"));
            p.setSexo(request.getParameter("sexo"));
            String[] enfermedades = request.getParameterValues("enfermedad");
            p.setEnfermedadPreexistente(enfermedades != null ? String.join(", ", enfermedades) : "Ninguna");
            
            String[] alergias = request.getParameterValues("alergias");
            p.setAlergias(alergias != null ? String.join(", ", alergias) : "Ninguna");
            p.setPresionArterial(request.getParameter("presion"));

            // Parseos seguros: Si el dato está vacío, le pone 0 en lugar de explotar.
            String fecha = request.getParameter("fechaNacimiento");
            if (fecha != null && !fecha.isEmpty()) {
                try {
                    p.setFechaNacimiento(LocalDate.parse(fecha, DateTimeFormatter.ISO_LOCAL_DATE));
                } catch (Exception ignore) {}
            }

            String est = request.getParameter("estatura");
            try { p.setEstatura(est != null && !est.trim().isEmpty() ? Double.parseDouble(est.replace(",", ".").replaceAll("[^\\d.]", "")) : 0.0); } catch (Exception e) { p.setEstatura(0.0); }

            String peso = request.getParameter("peso");
            try { p.setPeso(peso != null && !peso.trim().isEmpty() ? Double.parseDouble(peso.replace(",", ".").replaceAll("[^\\d.]", "")) : 0.0); } catch (Exception e) { p.setPeso(0.0); }

            String temp = request.getParameter("temperatura");
            try { p.setTemperatura(temp != null && !temp.trim().isEmpty() ? Double.parseDouble(temp.replace(",", ".").replaceAll("[^\\d.]", "")) : 0.0); } catch (Exception e) { p.setTemperatura(0.0); }

            String fc = request.getParameter("fc");
            try { p.setFrecuenciaCardiaca(fc != null && !fc.trim().isEmpty() ? Integer.parseInt(fc.replaceAll("[^\\d]", "")) : 0); } catch (Exception e) { p.setFrecuenciaCardiaca(0); }

            String sat = request.getParameter("sat");
            try { p.setSaturacionOxigeno(sat != null && !sat.trim().isEmpty() ? Integer.parseInt(sat.replaceAll("[^\\d]", "")) : 0); } catch (Exception e) { p.setSaturacionOxigeno(0); }

            if (isNew) {
                dao.registrarPaciente(p);
            } else {
                dao.actualizarPaciente(p);
            }

        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Error al procesar los datos del paciente.");
        }


        response.sendRedirect("dashboard");
    }
}