package com.nurselogic.controller;

import com.nurselogic.dao.FacturaDAO;
import com.nurselogic.config.JPAUtil;
import com.nurselogic.model.*;
import jakarta.persistence.EntityManager;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

@WebServlet("/exportCsv")
public class ExportServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String tipo = request.getParameter("tipo");
        if (tipo == null) tipo = "reporte";

        response.setContentType("text/csv; charset=UTF-8");
        response.setHeader("Content-Disposition", "attachment; filename=\"reporte_" + tipo + ".csv\"");

        PrintWriter out = response.getWriter();
        // Escribir BOM para Excel
        out.write('\ufeff');

        EntityManager em = JPAUtil.getEntityManager();
        try {
            if ("pacientes".equalsIgnoreCase(tipo)) {
                out.println("ID,Nombres,Apellidos,Cedula,Fecha Nacimiento,Sexo,Estatura,Peso,IMC,Enfermedad Preexistente,Alergias");
                List<Paciente> lista = em.createQuery("SELECT p FROM Paciente p", Paciente.class).getResultList();
                for (Paciente p : lista) {
                    double est = p.getEstatura();
                    if (est > 3) est = est / 100.0;
                    double imc = (est > 0) ? (p.getPeso() / (est * est)) : 0;
                    out.println(String.format("%d,\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",%.2f,%.1f,%.2f,\"%s\",\"%s\"",
                            p.getId(),
                            p.getNombres() != null ? p.getNombres() : "",
                            p.getApellidos() != null ? p.getApellidos() : "",
                            p.getCedula() != null ? p.getCedula() : "",
                            p.getFechaNacimiento() != null ? p.getFechaNacimiento().toString() : "",
                            p.getSexo() != null ? p.getSexo() : "",
                            p.getEstatura(), p.getPeso(), imc,
                            p.getEnfermedadPreexistente() != null ? p.getEnfermedadPreexistente() : "",
                            p.getAlergias() != null ? p.getAlergias() : ""));
                }
            } else if ("medicamentos".equalsIgnoreCase(tipo)) {
                out.println("ID,Nombre Fármaco,Stock Actual,Estado");
                List<Medicamento> lista = em.createQuery("SELECT m FROM Medicamento m", Medicamento.class).getResultList();
                for (Medicamento m : lista) {
                    String estado = m.getStock() < 20 ? "CRÍTICO" : "NORMAL";
                    out.println(String.format("%d,\"%s\",%d,\"%s\"",
                            m.getId(), m.getNombre(), m.getStock(), estado));
                }
            } else if ("citas".equalsIgnoreCase(tipo)) {
                out.println("ID,Fecha,Hora,Especialidad,Paciente Cédula,Estado");
                List<Cita> lista = em.createQuery("SELECT c FROM Cita c ORDER BY c.fecha DESC, c.hora DESC", Cita.class).getResultList();
                for (Cita c : lista) {
                    String espDesc = (c.getEspecialidad() != null && c.getEspecialidad().getDescripcion() != null) ? c.getEspecialidad().getDescripcion() : "";
                    String pacCed = (c.getPaciente() != null && c.getPaciente().getCedula() != null) ? c.getPaciente().getCedula() : "";
                    out.println(String.format("%d,\"%s\",\"%s\",\"%s\",\"%s\",\"%s\"",
                            c.getId(),
                            c.getFecha() != null ? c.getFecha().toString() : "",
                            c.getHora() != null ? c.getHora().toString() : "",
                            espDesc,
                            pacCed,
                            c.getEstado() != null ? c.getEstado() : ""));
                }
            } else if ("camas".equalsIgnoreCase(tipo)) {
                out.println("ID,Número Cama,Sala,Estado,Paciente,Médico a Cargo,Motivo");
                List<Cama> lista = em.createQuery("SELECT c FROM Cama c ORDER BY c.numero", Cama.class).getResultList();
                for (Cama c : lista) {
                    out.println(String.format("%d,\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\"",
                            c.getId(), c.getNumero(), c.getSala(), c.getEstado(),
                            c.getPacienteNombre() != null ? c.getPacienteNombre() : "",
                            c.getMedicoNombre() != null ? c.getMedicoNombre() : "",
                            c.getMotivo() != null ? c.getMotivo() : ""));
                }
            } else {
                out.println("Error,Tipo de reporte no válido");
            }
        } finally {
            em.close();
        }
    }
}
