package com.nurselogic.controller;

import com.nurselogic.config.JPAUtil;
import com.nurselogic.dao.PacienteDAO;
import com.nurselogic.model.Cama;
import com.nurselogic.model.Paciente;
import jakarta.persistence.EntityManager;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;
import java.time.LocalDate;

@WebServlet("/camasAction")
public class CamasActionServlet extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String action = request.getParameter("action");
        EntityManager em = JPAUtil.getEntityManager();
        
        try {
            em.getTransaction().begin();

            if ("crear".equals(action)) {
                String numero = request.getParameter("numero");
                String sala = request.getParameter("sala");
                
                Cama cama = new Cama();
                cama.setNumero(numero);
                cama.setSala(sala);
                cama.setEstado("Disponible");
                
                em.persist(cama);
                request.setAttribute("mensaje", "Cama creada exitosamente.");
            } else if ("asignar".equals(action)) {
                int camaId = Integer.parseInt(request.getParameter("camaId"));
                String esNuevo = request.getParameter("esNuevoPaciente");
                String pacienteNombre = request.getParameter("pacienteNombre");
                String cedula = request.getParameter("cedula");

                if ("true".equals(esNuevo)) {
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

                    PacienteDAO pacienteDAO = new PacienteDAO();
                    pacienteDAO.registrarPaciente(p);

                    pacienteNombre = ((nombres != null ? nombres : "") + " " + (apellidos != null ? apellidos : "")).trim();
                } else if ((pacienteNombre == null || pacienteNombre.isEmpty()) && cedula != null && !cedula.isEmpty()) {
                    PacienteDAO pacienteDAO = new PacienteDAO();
                    Paciente p = pacienteDAO.buscarPorCedula(cedula);
                    if (p != null) {
                        pacienteNombre = p.getNombres() + " " + p.getApellidos();
                    }
                }

                String medicoNombre = request.getParameter("medicoNombre");
                if (medicoNombre == null || medicoNombre.isEmpty()) medicoNombre = "Medico de Turno";
                String motivo = request.getParameter("motivo");
                if (motivo == null || motivo.isEmpty()) motivo = "Ingreso en Hospitalización";
                
                Cama cama = em.find(Cama.class, camaId);
                if (cama != null) {
                    cama.setEstado("Ocupada");
                    cama.setPacienteNombre(pacienteNombre != null && !pacienteNombre.isEmpty() ? pacienteNombre : "Paciente Registrado");
                    cama.setMedicoNombre(medicoNombre);
                    cama.setMotivo(motivo);
                    em.merge(cama);
                    request.setAttribute("mensaje", "Paciente asignado exitosamente.");
                }
            } else if ("liberar".equals(action)) {
                int camaId = Integer.parseInt(request.getParameter("camaId"));
                Cama cama = em.find(Cama.class, camaId);
                if (cama != null) {
                    cama.setEstado("Disponible");
                    cama.setPacienteNombre(null);
                    cama.setMedicoNombre(null);
                    cama.setMotivo(null);
                    em.merge(cama);
                    request.setAttribute("mensaje", "Cama liberada (dada de alta) exitosamente.");
                }
            } else if ("cambiarEstado".equals(action)) {
                int camaId = Integer.parseInt(request.getParameter("camaId"));
                String nuevoEstado = request.getParameter("estado");
                if (nuevoEstado == null || nuevoEstado.isEmpty()) nuevoEstado = "Mantenimiento";
                Cama cama = em.find(Cama.class, camaId);
                if (cama != null) {
                    cama.setEstado(nuevoEstado);
                    cama.setPacienteNombre(null);
                    cama.setMedicoNombre(null);
                    cama.setMotivo(null);
                    em.merge(cama);
                    request.setAttribute("mensaje", "Estado de la cama actualizado a " + nuevoEstado + ".");
                }
            } else if ("eliminar".equals(action)) {
                int camaId = Integer.parseInt(request.getParameter("camaId"));
                Cama cama = em.find(Cama.class, camaId);
                if (cama != null) {
                    em.remove(cama);
                    request.setAttribute("mensaje", "Cama eliminada exitosamente.");
                }
            }

            em.getTransaction().commit();
        } catch (Exception e) {
            if (em.getTransaction().isActive()) {
                em.getTransaction().rollback();
            }
            e.printStackTrace();
            request.setAttribute("error", "Ocurrió un error en la operación de camas.");
        } finally {
            if (em.isOpen()) {
                em.close();
            }
        }

        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
