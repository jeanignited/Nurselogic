package com.nurselogic.dao;

import com.nurselogic.config.ConnectionPool;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import com.nurselogic.model.Medicamento;

public class MedicamentoDAO {
    public List<Medicamento> listarTodos() throws SQLException {
        List<Medicamento> lista = new ArrayList<>();
        try (Connection conn = ConnectionPool.getConnection();
             PreparedStatement ps = conn.prepareStatement("SELECT * FROM medicamentos")) {
            ResultSet rs = ps.executeQuery();
            while (rs.next()) {
                Medicamento m = new Medicamento();
                m.setId(rs.getInt("id"));
                m.setNombre(rs.getString("nombre"));
                m.setStock(rs.getInt("stock"));
                lista.add(m);
            }
        }
        return lista;
    }
}