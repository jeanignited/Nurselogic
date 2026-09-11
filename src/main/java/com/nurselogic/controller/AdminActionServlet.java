package com.nurselogic.controller;

import com.nurselogic.service.AdminService;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

@WebServlet("/adminAction")
public class AdminActionServlet extends HttpServlet {

    private AdminService adminService = new AdminService();

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("usuarioLogueado") == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        String rolUsuario = (String) session.getAttribute("rol");
        boolean isAdmin = "Admin".equalsIgnoreCase(rolUsuario);
        String correoActual = (String) session.getAttribute("correo");

        String action = request.getParameter("action");
        String tipo = request.getParameter("target"); // "paciente" o "usuario"
        String id = request.getParameter("id"); // cedula o correo

        try {
            AdminService.ActionResult result = null;

            if ("eliminar".equals(action)) {
                if ("paciente".equals(tipo)) {
                    result = adminService.eliminarPaciente(id, isAdmin);
                } else if ("usuario".equals(tipo)) {
                    result = adminService.eliminarUsuario(id, isAdmin, correoActual);
                }
            } else if ("editarRol".equals(action) && "usuario".equals(tipo)) {
                String nuevoRol = request.getParameter("nuevoRol");
                result = adminService.editarRol(id, nuevoRol, isAdmin, correoActual);
            } else if ("editarEspecialidad".equals(action) && "usuario".equals(tipo)) {
                String nuevaEsp = request.getParameter("nuevaEspecialidad");
                result = adminService.editarEspecialidad(id, nuevaEsp);
            } else if ("crearRol".equals(action)) {
                String nombreRol      = request.getParameter("nombreRol");
                String descRol        = request.getParameter("descRol");         // FIX
                String[] permisosArr  = request.getParameterValues("permiso");   // FIX
                String permisosStr    = (permisosArr != null) ? String.join(",", permisosArr) : "";

                boolean bHosp    = "true".equals(request.getParameter("permBoolHosp"));
                boolean bVentas  = "true".equals(request.getParameter("permBoolVentas"));
                boolean bDirPac  = "true".equals(request.getParameter("permBoolDirPac"));
                boolean bCatClin = "true".equals(request.getParameter("permBoolCatClin"));
                boolean bSopTI   = "true".equals(request.getParameter("permBoolSoporteTI"));

                result = adminService.crearRol(nombreRol, descRol, permisosStr,
                        bHosp, bVentas, bDirPac, bCatClin, bSopTI, isAdmin);
            } else if ("crearMedicamento".equals(action)) {
                result = adminService.crearMedicamento(request.getParameter("nombreMed"), request.getParameter("stockMed"), request.getParameter("precioMed"));
            } else if ("facturarVenta".equals(action)) {
                result = adminService.procesarVentaFarmacia(request.getParameter("idMed"), request.getParameter("cantidad"), request.getParameter("cliente"));
            } else if ("ajustarStock".equals(action)) {
                result = adminService.ajustarStock(request.getParameter("idMed"), request.getParameter("cambio"));
            } else if ("crearEnfermedad".equals(action)) {
                result = adminService.crearEnfermedad(request.getParameter("nombreEnf"), request.getParameter("descEnf"));
            } else if ("crearAlergia".equals(action)) {
                result = adminService.crearAlergia(request.getParameter("nombreAle"), request.getParameter("gravedadAle"));
            } else if ("actualizarEstadoCita".equals(action)) {
                result = adminService.actualizarEstadoCita(id, request.getParameter("nuevoEstado"));
            } else if ("atenderCita".equals(action)) {
                result = adminService.atenderCita(request.getParameter("idCita"), request.getParameter("diagnostico"), request.getParameter("recetaCita"));
            } else if ("editarEnfermedad".equals(action)) {
                result = adminService.editarEnfermedad(request.getParameter("idEnf"), request.getParameter("nombreEnf"), request.getParameter("descEnf"));
            } else if ("borrarEnfermedad".equals(action)) {
                result = adminService.borrarEnfermedad(request.getParameter("idEnf"));
            } else if ("editarAlergia".equals(action)) {
                result = adminService.editarAlergia(request.getParameter("idAle"), request.getParameter("nombreAle"), request.getParameter("gravedadAle"));
            } else if ("borrarAlergia".equals(action)) {
                result = adminService.borrarAlergia(request.getParameter("idAle"));
            } else if ("prescribirReceta".equals(action)) {
                String esNuevoStr = request.getParameter("esNuevoPaciente");
                boolean esNuevo = "true".equals(esNuevoStr);
                result = adminService.prescribirReceta(
                        request.getParameterValues("idMedicamento"),
                        request.getParameterValues("cantidad"),
                        request.getParameter("pacienteNombre"),
                        request.getParameter("cedula"),
                        request.getParameter("indicaciones"),
                        esNuevo,
                        request.getParameter("nuevoNombres"),
                        request.getParameter("nuevoApellidos"),
                        request.getParameter("nuevoFechaNac"),
                        request.getParameter("nuevoSexo")
                );
            } else if ("internarPaciente".equals(action)) {
                result = adminService.internarPaciente(request.getParameter("idCama"), request.getParameter("pacienteNombre"), request.getParameter("medicoNombre"), request.getParameter("motivo"));
            } else if ("darAltaCama".equals(action)) {
                result = adminService.darAltaCama(request.getParameter("idCama"));
            } else if ("cambiarEstadoCama".equals(action)) {
                result = adminService.cambiarEstadoCama(request.getParameter("idCama"), request.getParameter("nuevoEstado"));
            } else if ("completarVentaReceta".equals(action)) {
                result = adminService.completarVentaReceta(request.getParameter("idCita"), request.getParameter("cedula"));
            }

            if (result != null) {
                if (result.success) {
                    session.setAttribute("mensaje", result.message);
                } else {
                    session.setAttribute("error", result.message);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
            session.setAttribute("error", "Error interno al procesar la acción.");
        }

        String referer = request.getHeader("Referer");
        if (referer != null) {
            response.sendRedirect(referer);
        } else {
            response.sendRedirect("dashboard");
        }
    }
}