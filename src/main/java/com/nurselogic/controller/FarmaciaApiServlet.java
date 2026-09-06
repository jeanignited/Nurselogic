package com.nurselogic.controller;

import com.nurselogic.config.JPAUtil;
import com.nurselogic.model.Cita;
import com.nurselogic.model.Paciente;
import jakarta.persistence.EntityManager;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet("/api/receta")
public class FarmaciaApiServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        String cedula = req.getParameter("cedula");
        resp.setContentType("application/json");
        resp.setCharacterEncoding("UTF-8");

        if (cedula == null || cedula.trim().isEmpty()) {
            resp.getWriter().write("{\"success\": false, \"message\": \"Cédula requerida\"}");
            return;
        }

        EntityManager em = JPAUtil.getEntityManager();
        try {
            Paciente pac = em.createQuery("SELECT p FROM Paciente p WHERE p.cedula = :cedula", Paciente.class)
                    .setParameter("cedula", cedula)
                    .getResultStream().findFirst().orElse(null);

            if (pac == null) {
                resp.getWriter().write("{\"success\": false, \"message\": \"Paciente no encontrado\"}");
            } else {
                List<Cita> citas = em.createQuery("SELECT c FROM Cita c WHERE c.paciente.id = :idPac AND c.estado = 'ATENDIDO' ORDER BY c.fecha DESC, c.hora DESC", Cita.class)
                        .setParameter("idPac", pac.getId())
                        .getResultList();

                Cita citaValida = null;
                for (Cita c : citas) {
                    if (c.getReceta() != null && !c.getReceta().trim().isEmpty()) {
                        citaValida = c;
                        break;
                    }
                }

                if (citaValida != null) {
                    String nombre = pac.getNombres() + " " + pac.getApellidos();
                    String receta = citaValida.getReceta().replace("\"", "\\\"").replace("\n", "\\n").replace("\r", "");
                    resp.getWriter().write(String.format("{\"success\": true, \"pacienteNombre\": \"%s\", \"fecha\": \"%s\", \"receta\": \"%s\"}", nombre, citaValida.getFecha().toString(), receta));
                } else {
                    resp.getWriter().write("{\"success\": false, \"message\": \"El paciente no tiene recetas vigentes.\"}");
                }
            }
        } catch (Exception e) {
            resp.getWriter().write("{\"success\": false, \"message\": \"Error en el servidor\"}");
        } finally {
            em.close();
        }
    }
}
