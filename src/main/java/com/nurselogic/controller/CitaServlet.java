package com.nurselogic.controller;

import com.nurselogic.dao.CitaDAO;
import com.nurselogic.dao.PacienteDAO;
import com.nurselogic.model.Cita;
import com.nurselogic.model.Especialidad;
import com.nurselogic.model.Paciente;
import com.nurselogic.service.CitaService;

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
        String fecha = request.getParameter("fecha");
        String hora = request.getParameter("hora");
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
                request.setAttribute("error", "Error al registrar el nuevo paciente: " + e.getMessage());
                request.getRequestDispatcher("/dashboard").forward(request, response);
                return;
            }
        }

        CitaService.AgendarResult result = citaService.agendarCita(fecha, hora, idEspecialidad, paramPac, sessPac);
        
        if (result.success) {
            request.setAttribute("mensaje", result.message);
        } else {
            request.setAttribute("error", result.message);
        }

        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}