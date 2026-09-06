package com.nurselogic.service;

import com.nurselogic.dao.CitaDAO;
import com.nurselogic.model.Cita;
import com.nurselogic.model.Especialidad;
import com.nurselogic.model.Paciente;

import java.time.LocalDate;
import java.time.LocalTime;

public class CitaService {
    private CitaDAO citaDAO = new CitaDAO();

    public static class AgendarResult {
        public boolean success;
        public String message;
        public AgendarResult(boolean success, String message) {
            this.success = success;
            this.message = message;
        }
    }

    public AgendarResult agendarCita(String fecha, String hora, String idEspecialidadStr, String paramPac, String sessPac) {
        try {
            int idEspecialidad = Integer.parseInt(idEspecialidadStr);
            
            int idPaciente = 1;
            if (paramPac != null && !paramPac.trim().isEmpty()) {
                try {
                    idPaciente = Integer.parseInt(paramPac);
                } catch (NumberFormatException e) {
                    idPaciente = 1;
                }
            } else {
                if (sessPac != null && !sessPac.trim().isEmpty()) {
                    try {
                        idPaciente = Integer.parseInt(sessPac);
                    } catch (NumberFormatException e) {}
                }
            }

            Especialidad especialidad = new Especialidad();
            especialidad.setId(idEspecialidad);

            Paciente paciente = new Paciente();
            paciente.setId(idPaciente);

            Cita nuevaCita = new Cita();
            nuevaCita.setFecha(LocalDate.parse(fecha));
            nuevaCita.setHora(LocalTime.parse(hora));
            nuevaCita.setEspecialidad(especialidad);
            nuevaCita.setPaciente(paciente);
            nuevaCita.setEstado("REGISTRADO");

            String result = citaDAO.agendarCita(nuevaCita);
            if ("OK".equals(result)) {
                return new AgendarResult(true, "¡Tu cita fue agendada con éxito!");
            } else {
                return new AgendarResult(false, "Error: " + result + " | P:" + idPaciente + " E:" + idEspecialidad);
            }
        } catch (Exception e) {
            return new AgendarResult(false, "Error de validación de datos: " + e.getMessage());
        }
    }
}
