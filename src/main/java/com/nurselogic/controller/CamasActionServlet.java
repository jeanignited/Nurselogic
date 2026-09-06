package com.nurselogic.controller;

import com.nurselogic.config.JPAUtil;
import com.nurselogic.model.Cama;
import jakarta.persistence.EntityManager;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;

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
                String pacienteNombre = request.getParameter("pacienteNombre");
                String medicoNombre = request.getParameter("medicoNombre");
                String motivo = request.getParameter("motivo");
                
                Cama cama = em.find(Cama.class, camaId);
                if (cama != null) {
                    cama.setEstado("Ocupada");
                    cama.setPacienteNombre(pacienteNombre);
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
