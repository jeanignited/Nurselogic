package com.nurselogic.controller;

import com.nurselogic.dao.UsuarioDAO;
import com.nurselogic.model.Usuario;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

@WebServlet("/login")
public class LoginServlet extends HttpServlet {
    private UsuarioDAO dao = new UsuarioDAO();

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String correo = request.getParameter("usuario");
        String clave = request.getParameter("clave");

        Usuario u = dao.validarLogin(correo, clave);

        if (u != null) {
            HttpSession session = request.getSession();
            session.setAttribute("usuarioLogueado", u.getCorreo());
            session.setAttribute("nombres", u.getNombres() + " " + u.getApellidos());
            session.setAttribute("rol", u.getRol());

            // ¡LA SOLUCIÓN ESTÁ AQUÍ!
            // En vez de mandarte a index.jsp vacío, te manda al dashboard para que cargue las listas de personal y pacientes.
            response.sendRedirect("dashboard");
        } else {
            request.setAttribute("error", "Credenciales incorrectas o el usuario no existe.");
            request.getRequestDispatcher("/login.jsp").forward(request, response);
        }
    }
}