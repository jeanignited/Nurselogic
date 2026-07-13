package com.nurselogic.dao;

import com.nurselogic.config.ConnectionPool;
import com.nurselogic.model.Paciente;
import java.sql.Connection;
import java.sql.PreparedStatement;

public class PacienteDAO {
    public boolean registrarPaciente(Paciente p) {
        String sql = "INSERT INTO pacientes (nombres, apellidos, cedula, edad, sexo, estatura, peso, enfermedad_preexistente, temperatura, presion, fc, sat) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)";

        try (Connection conn = ConnectionPool.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, p.getNombres());
            stmt.setString(2, p.getApellidos());
            stmt.setString(3, p.getCedula());
            stmt.setInt(4, p.getEdad());
            stmt.setString(5, p.getSexo());
            stmt.setDouble(6, p.getEstatura());
            stmt.setDouble(7, p.getPeso());
            stmt.setString(8, p.getEnfermedadPreexistente());
            stmt.setDouble(9, p.getTemperatura());
            stmt.setString(10, p.getPresionArterial());
            stmt.setInt(11, p.getFrecuenciaCardiaca());
            stmt.setInt(12, p.getSaturacionOxigeno());

            return stmt.executeUpdate() > 0;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }
}