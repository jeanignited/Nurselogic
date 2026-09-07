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
            String cleanCed = cedula.trim();
            Paciente pac = em.createQuery("SELECT p FROM Paciente p WHERE p.cedula = :cedula", Paciente.class)
                    .setParameter("cedula", cleanCed)
                    .getResultStream().findFirst().orElse(null);

            if (pac == null) {
                resp.getWriter().write("{\"success\": false, \"message\": \"No existe paciente registrado con la cédula " + cleanCed + "\"}");
            } else {
                List<Cita> citas = em.createQuery("SELECT c FROM Cita c WHERE c.paciente.id = :idPac AND c.receta IS NOT NULL AND LENGTH(TRIM(c.receta)) > 0 ORDER BY c.id DESC", Cita.class)
                        .setParameter("idPac", pac.getId())
                        .getResultList();

                Cita citaValida = citas.isEmpty() ? null : citas.get(0);

                if (citaValida != null) {
                    String nombre = pac.getNombres() + " " + pac.getApellidos();
                    String receta = citaValida.getReceta().replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", "\\n").replace("\r", "");
                    String fecha = citaValida.getFecha() != null ? citaValida.getFecha().toString() : "Hoy";
                    resp.getWriter().write(String.format("{\"success\": true, \"pacienteNombre\": \"%s\", \"fecha\": \"%s\", \"receta\": \"%s\"}", nombre, fecha, receta));
                } else {
                    resp.getWriter().write("{\"success\": false, \"message\": \"El paciente " + pac.getNombres() + " " + pac.getApellidos() + " no tiene recetas vigentes.\"}");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
            resp.getWriter().write("{\"success\": false, \"message\": \"Error al consultar la receta en el servidor\"}");
        } finally {
            em.close();
        }
    }
}
