package com.nexusmed.controller;

import com.nexusmed.dao.UsuarioDAO;
import com.nexusmed.model.Usuario;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/registroUsuario")
public class RegistroServlet extends HttpServlet {
    private com.nexusmed.service.UsuarioService usuarioService = new com.nexusmed.service.UsuarioService();

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");
        Usuario u = new Usuario();
        u.setNombres(request.getParameter("nombres"));
        u.setApellidos(request.getParameter("apellidos"));
        u.setCorreo(request.getParameter("correo"));
        u.setCedula(request.getParameter("cedula"));
        u.setTelefono(request.getParameter("telefono"));
        u.setDireccion(request.getParameter("direccion"));
        
        String plainPassword = request.getParameter("clave");
        if (plainPassword != null && !plainPassword.trim().isEmpty()) {
            u.setClave(com.nexusmed.util.SecurityUtil.hashPassword(plainPassword));
        }

        String tipoUsuario = request.getParameter("tipoUsuario");

        com.nexusmed.service.UsuarioService.RegistroResult result = usuarioService.registrarUsuario(u, tipoUsuario);
        request.setAttribute("error", result.message); // Usamos "error" como variable genérica en el jsp actual para mensajes

        request.getRequestDispatcher("/login.jsp").forward(request, response);
    }
}