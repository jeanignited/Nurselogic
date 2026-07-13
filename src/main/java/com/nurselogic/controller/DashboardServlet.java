package com.nurselogic.controller;

import com.nurselogic.config.ConnectionPool;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;
import java.sql.*;
import java.util.*;

@WebServlet("/dashboard")
public class DashboardServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 1. Inicializar listas vacías por defecto (EL SEGURO CONTRA ERRORES 500)
        List<Map<String, String>> listaPacientes = new ArrayList<>();
        List<Map<String, String>> listaUsuarios = new ArrayList<>();
        int totalPac = 0, totalMeds = 0, totalUsers = 0;

        // 2. Intentar conectar a la BD
        try (Connection conn = ConnectionPool.getConnection();
             Statement st = conn.createStatement()) {

            // Contadores
            ResultSet rsP = st.executeQuery("SELECT COUNT(*) FROM pacientes");
            if(rsP.next()) totalPac = rsP.getInt(1);

            ResultSet rsM = st.executeQuery("SELECT COUNT(*) FROM medicamentos");
            if(rsM.next()) totalMeds = rsM.getInt(1);

            ResultSet rsU = st.executeQuery("SELECT COUNT(*) FROM usuarios");
            if(rsU.next()) totalUsers = rsU.getInt(1);

            // Lista de Pacientes
            ResultSet rsPac = st.executeQuery("SELECT nombres, apellidos, cedula, edad FROM pacientes");
            while(rsPac.next()) {
                Map<String, String> p = new HashMap<>();
                p.put("nombres", rsPac.getString("nombres"));
                p.put("apellidos", rsPac.getString("apellidos"));
                p.put("cedula", rsPac.getString("cedula"));
                p.put("edad", rsPac.getString("edad"));
                listaPacientes.add(p);
            }

            // Lista de Usuarios
            ResultSet rsUsu = st.executeQuery("SELECT nombres, apellidos, correo, rol FROM usuarios");
            while(rsUsu.next()) {
                Map<String, String> u = new HashMap<>();
                u.put("nombres", rsUsu.getString("nombres"));
                u.put("apellidos", rsUsu.getString("apellidos"));
                u.put("correo", rsUsu.getString("correo"));
                u.put("rol", rsUsu.getString("rol"));
                listaUsuarios.add(u);
            }

        } catch (Exception e) {
            e.printStackTrace(); // Si hay error, las listas seguirán vacías, pero no nulas.
        }

        // 3. Enviar todo a la vista de forma segura
        request.setAttribute("totalPacientes", totalPac);
        request.setAttribute("totalMeds", totalMeds);
        request.setAttribute("totalUsers", totalUsers);
        request.setAttribute("listaPacientes", listaPacientes);
        request.setAttribute("listaUsuarios", listaUsuarios);

        request.getRequestDispatcher("index.jsp").forward(request, response);
    }
}