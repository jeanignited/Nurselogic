package com.nurselogic.controller;

import com.nurselogic.dao.UsuarioDAO;
import com.nurselogic.model.Usuario;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/registroUsuario")
public class RegistroServlet extends HttpServlet {
    private UsuarioDAO dao = new UsuarioDAO();

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        Usuario u = new Usuario();
        u.setNombres(request.getParameter("nombres"));
        u.setApellidos(request.getParameter("apellidos"));
        u.setCorreo(request.getParameter("correo"));
        u.setCedula(request.getParameter("cedula"));
        u.setTelefono(request.getParameter("telefono"));
        u.setDireccion(request.getParameter("direccion"));
        u.setClave(request.getParameter("clave"));

        // Intentamos registrar en la base de datos
        if (dao.registrarUsuario(u)) {
            // Si sale bien, mandamos mensaje de éxito (con formato de advertencia para que resalte)
            request.setAttribute("error", "¡Cuenta creada! Espera la habilitación del Admin.");
        } else {
            // Si falla (ej. correo duplicado), mandamos error
            request.setAttribute("error", "Error al crear la cuenta. Revisa los datos o el correo.");
        }

        // Te devuelve al login con el mensaje
        request.getRequestDispatcher("/login.jsp").forward(request, response);
    }
}
