package com.nurselogic.controller;

import com.nurselogic.config.JPAUtil;
import jakarta.persistence.EntityManager;

import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.UUID;

@WebServlet(value = "/soporteAction", loadOnStartup = 1)
@MultipartConfig(
    fileSizeThreshold = 1024 * 1024 * 2, // 2MB
    maxFileSize = 1024 * 1024 * 50,      // 50MB
    maxRequestSize = 1024 * 1024 * 100   // 100MB
)
public class SoporteServlet extends HttpServlet {

    @Override
    public void init() throws ServletException {
        try {
            EntityManager em = JPAUtil.getEntityManager();
            em.getTransaction().begin();
            em.createNativeQuery("CREATE TABLE IF NOT EXISTS tickets_soporte (" +
                    "id INT AUTO_INCREMENT PRIMARY KEY, " +
                    "titulo VARCHAR(255), " +
                    "descripcion TEXT, " +
                    "nivel_alerta VARCHAR(50), " +
                    "ruta_video VARCHAR(255), " +
                    "fecha_reporte DATETIME, " +
                    "estado VARCHAR(50) DEFAULT 'Pendiente')").executeUpdate();
            
            // Parche rápido para caracteres corruptos en especialidades
            em.createNativeQuery("UPDATE especialidades SET descripcion = REPLACE(descripcion, 'Ãa', 'ía')").executeUpdate();
            em.createNativeQuery("UPDATE especialidades SET descripcion = REPLACE(descripcion, 'Ã³', 'ó')").executeUpdate();
            em.createNativeQuery("UPDATE especialidades SET descripcion = REPLACE(descripcion, 'Ã©', 'é')").executeUpdate();
            em.createNativeQuery("UPDATE especialidades SET descripcion = REPLACE(descripcion, 'Ã¡', 'á')").executeUpdate();
            em.createNativeQuery("UPDATE especialidades SET descripcion = REPLACE(descripcion, 'Ã', 'í')").executeUpdate();

            em.getTransaction().commit();
            em.close();
            System.out.println("Tabla tickets_soporte inicializada correctamente.");
        } catch (Exception e) {
            e.printStackTrace();
            System.err.println("Error inicializando tabla tickets_soporte: " + e.getMessage());
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String action = request.getParameter("action");
        if ("resolver".equals(action)) {
            resolverTicket(request, response);
            return;
        }

        String titulo = request.getParameter("titulo");
        String descripcion = request.getParameter("descripcion");
        String nivelAlerta = request.getParameter("nivelAlerta");

        Part filePart = request.getPart("video");
        String relativePath = "";

        if (filePart != null && filePart.getSize() > 0) {
            String uploadPath = getServletContext().getRealPath("") + File.separator + "uploads" + File.separator + "soporte";
            File uploadDir = new File(uploadPath);
            if (!uploadDir.exists()) {
                uploadDir.mkdirs();
            }

            String fileName = "soporte_" + UUID.randomUUID().toString() + ".webm";
            String fullPath = uploadPath + File.separator + fileName;
            filePart.write(fullPath);
            relativePath = "uploads/soporte/" + fileName;
        }

        try {
            EntityManager em = JPAUtil.getEntityManager();
            em.getTransaction().begin();
            em.createNativeQuery("INSERT INTO tickets_soporte (titulo, descripcion, nivel_alerta, ruta_video, fecha_reporte, estado) " +
                    "VALUES (?, ?, ?, ?, NOW(), 'Pendiente')")
                    .setParameter(1, titulo)
                    .setParameter(2, descripcion)
                    .setParameter(3, nivelAlerta)
                    .setParameter(4, relativePath)
                    .executeUpdate();
            em.getTransaction().commit();
            em.close();

            response.setContentType("application/json");
            response.setCharacterEncoding("UTF-8");
            PrintWriter out = response.getWriter();
            out.print("{\"success\": true, \"message\": \"Ticket enviado con éxito al equipo T.I.\"}");
            out.flush();
        } catch (Exception e) {
            e.printStackTrace();
            response.setStatus(500);
            response.setContentType("application/json");
            PrintWriter out = response.getWriter();
            out.print("{\"success\": false, \"message\": \"Error al guardar el ticket en base de datos\"}");
            out.flush();
        }
    }

    private void resolverTicket(HttpServletRequest request, HttpServletResponse response) throws IOException {
        String id = request.getParameter("id");
        try {
            EntityManager em = JPAUtil.getEntityManager();
            em.getTransaction().begin();
            em.createNativeQuery("UPDATE tickets_soporte SET estado = 'Resuelto' WHERE id = ?")
                    .setParameter(1, id)
                    .executeUpdate();
            em.getTransaction().commit();
            em.close();

            response.sendRedirect("dashboard");
        } catch (Exception e) {
            e.printStackTrace();
            response.sendError(500, "Error al resolver ticket");
        }
    }
}
