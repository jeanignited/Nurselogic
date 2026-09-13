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
    private com.nurselogic.service.UsuarioService usuarioService = new com.nurselogic.service.UsuarioService();

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.sendRedirect("login.jsp");
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");
        String correo = request.getParameter("usuario");
        String clave = request.getParameter("clave");

        com.nurselogic.service.UsuarioService.LoginResult result = usuarioService.login(correo, clave);

        if (result.success) {
            HttpSession session = request.getSession();
            Usuario u = result.usuario;
            session.setAttribute("usuarioLogueado", u.getCorreo());
            session.setAttribute("nombres", u.getNombres());
session.setAttribute("apellidos", u.getApellidos());
            session.setAttribute("rol", u.getRol());

            response.sendRedirect("dashboard");
        } else {
            request.setAttribute("error", result.message);
            if (result.showRecover) {
                request.setAttribute("showRecover", true);
            }
            request.getRequestDispatcher("/login.jsp").forward(request, response);
        }
    }
}