package com.nurselogic.controller;

import com.nurselogic.dao.PacienteDAO;
import com.nurselogic.model.Paciente;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/registroPaciente")
public class PacienteServlet extends HttpServlet {
    private PacienteDAO dao = new PacienteDAO();

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        try {
            Paciente p = new Paciente();
            p.setNombres(request.getParameter("nombres"));
            p.setApellidos(request.getParameter("apellidos"));
            p.setCedula(request.getParameter("cedula"));
            p.setSexo(request.getParameter("sexo"));
            p.setEnfermedadPreexistente(request.getParameter("enfermedad"));
            p.setPresionArterial(request.getParameter("presion"));

            // Parseos seguros: Si el dato está vacío, le pone 0 en lugar de explotar.
            String edad = request.getParameter("edad");
            p.setEdad(edad != null && !edad.isEmpty() ? Integer.parseInt(edad) : 0);

            String est = request.getParameter("estatura");
            p.setEstatura(est != null && !est.isEmpty() ? Double.parseDouble(est) : 0.0);

            String peso = request.getParameter("peso");
            p.setPeso(peso != null && !peso.isEmpty() ? Double.parseDouble(peso) : 0.0);

            String temp = request.getParameter("temperatura");
            p.setTemperatura(temp != null && !temp.isEmpty() ? Double.parseDouble(temp) : 0.0);

            String fc = request.getParameter("fc");
            p.setFrecuenciaCardiaca(fc != null && !fc.isEmpty() ? Integer.parseInt(fc) : 0);

            String sat = request.getParameter("sat");
            p.setSaturacionOxigeno(sat != null && !sat.isEmpty() ? Integer.parseInt(sat) : 0);

            dao.registrarPaciente(p);

        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("Error al procesar los datos del paciente.");
        }

        // Regresar siempre al dashboard
        response.sendRedirect("dashboard");
    }
}