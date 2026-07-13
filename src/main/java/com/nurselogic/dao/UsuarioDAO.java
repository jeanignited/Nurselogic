package com.nurselogic.dao;

import com.nurselogic.config.ConnectionPool;
import com.nurselogic.model.Usuario;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class UsuarioDAO {

    public Usuario validarLogin(String correo, String clave) {
        Usuario u = null;
        String sql = "SELECT * FROM usuarios WHERE correo = ? AND clave = ?";
        try (Connection conn = ConnectionPool.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, correo);
            stmt.setString(2, clave);
            ResultSet rs = stmt.executeQuery();
            if (rs.next()) {
                u = new Usuario();
                u.setId(rs.getInt("id"));
                u.setCorreo(rs.getString("correo"));
                u.setNombres(rs.getString("nombres"));
                u.setApellidos(rs.getString("apellidos"));
                u.setRol(rs.getString("rol"));
            }
        } catch (Exception e) { e.printStackTrace(); }
        return u;
    }

    public boolean registrarUsuario(Usuario u) {
        String sql = "INSERT INTO usuarios (correo, nombres, apellidos, direccion, cedula, telefono, clave, rol) VALUES (?,?,?,?,?,?,?,'Pendiente')";
        try (Connection conn = ConnectionPool.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, u.getCorreo());
            stmt.setString(2, u.getNombres());
            stmt.setString(3, u.getApellidos());
            stmt.setString(4, u.getDireccion());
            stmt.setString(5, u.getCedula());
            stmt.setString(6, u.getTelefono());
            stmt.setString(7, u.getClave());
            return stmt.executeUpdate() > 0;
        } catch (Exception e) { e.printStackTrace(); return false; }
    }
}