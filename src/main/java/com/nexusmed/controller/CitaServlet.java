package com.nexusmed.controller;

import com.nexusmed.dao.CitaDAO;
import com.nexusmed.dao.PacienteDAO;
import com.nexusmed.model.Cita;
import com.nexusmed.model.Especialidad;
import com.nexusmed.model.Paciente;
import com.nexusmed.service.CitaService;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.time.LocalDate;

@WebServlet("/agendarCita")
public class CitaServlet extends HttpServlet {

    private CitaService citaService = new CitaService();
    private PacienteDAO pacienteDAO = new PacienteDAO();

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");
        String fecha = request.getParameter("fecha");
        String hora = request.getParameter("hora");
        
        String fechaHora = request.getParameter("fechaHora");
        if (fechaHora != null && !fechaHora.trim().isEmpty() && fechaHora.contains("T")) {
            String[] parts = fechaHora.split("T");
            fecha = parts[0];
            hora = parts[1];
        }
        String idEspecialidad = request.getParameter("especialidad");
        String paramPac = request.getParameter("pacienteId");
        String sessPac = (String) request.getSession().getAttribute("pacienteId");
        
        String esNuevo = request.getParameter("esNuevoPaciente");
        
        if ("true".equals(esNuevo)) {
            // Register new patient first
            String cedula = request.getParameter("cedula");
            String nombres = request.getParameter("nuevoNombres");
            String apellidos = request.getParameter("nuevoApellidos");
            String fechaNac = request.getParameter("nuevoFechaNac");
            String sexo = request.getParameter("nuevoSexo");
            
            Paciente p = new Paciente();
            p.setCedula(cedula);
            p.setNombres(nombres);
            p.setApellidos(apellidos);
            if (fechaNac != null && !fechaNac.isEmpty()) {
                p.setFechaNacimiento(LocalDate.parse(fechaNac));
            }
            p.setSexo(sexo);
            
            try {
                if (!pacienteDAO.registrarPaciente(p)) throw new Exception("No se pudo registrar el paciente.");
                paramPac = String.valueOf(p.getId());
            } catch (Exception e) {
                request.getSession().setAttribute("error", "Error al registrar el nuevo paciente: " + e.getMessage());
                request.getRequestDispatcher("/dashboard").forward(request, response);
                return;
            }
        }

        CitaService.AgendarResult result = citaService.agendarCita(fecha, hora, idEspecialidad, paramPac, sessPac);
        
        if (result.success) {
            request.getSession().setAttribute("mensaje", result.message);
        } else {
            request.getSession().setAttribute("error", result.message);
        }

        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}