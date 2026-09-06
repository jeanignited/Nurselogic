package com.nurselogic.config;

import com.nurselogic.model.*;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityTransaction;
import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;
import javax.servlet.annotation.WebListener;
import java.time.LocalDate;
import java.time.LocalTime;
import java.util.List;

@WebListener
public class DatabaseSeeder implements ServletContextListener {

    @Override
    public void contextInitialized(ServletContextEvent sce) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        
        try {
            tx.begin();
            
            Long rolCount = em.createQuery("SELECT COUNT(r) FROM Rol r", Long.class).getSingleResult();
            if (rolCount == 0) {
                em.persist(new com.nurselogic.model.Rol("Admin", "Administrador del sistema", "GESTION_USUARIOS,GESTION_MEDICAMENTOS,GESTION_CATALOGOS,REGISTRO_PACIENTES,AGENDAR_CITAS"));
                em.persist(new com.nurselogic.model.Rol("Medico", "Personal médico", "REGISTRO_PACIENTES,AGENDAR_CITAS"));
                em.persist(new com.nurselogic.model.Rol("Paciente", "Paciente del sistema", "AGENDAR_CITAS"));
                em.persist(new com.nurselogic.model.Rol("Pendiente", "Usuario pendiente de aprobación", ""));
                em.persist(new com.nurselogic.model.Rol("Farmaceuta", "Personal de farmacia", "GESTION_MEDICAMENTOS,GESTION_CATALOGOS"));
            }

            // Seed Medicamentos
            Long medCount = em.createQuery("SELECT COUNT(m) FROM Medicamento m", Long.class).getSingleResult();
            if (medCount == 0) {
                String[] nombres = {"Paracetamol 500mg", "Ibuprofeno 400mg", "Amoxicilina 500mg", "Omeprazol 20mg", "Loratadina 10mg", "Diclofenaco 50mg"};
                int[] stocks = {150, 120, 80, 200, 100, 90};
                for(int i=0; i<nombres.length; i++) {
                    Medicamento m = new Medicamento();
                    m.setNombre(nombres[i]);
                    m.setStock(stocks[i]);
                    em.persist(m);
                }
            }

            // Seed Enfermedades
            Long enfCount = em.createQuery("SELECT COUNT(e) FROM Enfermedad e", Long.class).getSingleResult();
            if (enfCount == 0) {
                em.persist(new Enfermedad("Hipertensión Arterial", "Presión arterial alta crónica."));
                em.persist(new Enfermedad("Diabetes Mellitus Tipo 2", "Nivel alto de azúcar en la sangre debido a resistencia a la insulina."));
                em.persist(new Enfermedad("Asma Bronquial", "Enfermedad crónica que inflama y estrecha las vías respiratorias."));
                em.persist(new Enfermedad("Gastritis Aguda", "Inflamación del revestimiento del estómago."));
                em.persist(new Enfermedad("Anemia Ferropénica", "Disminución de glóbulos rojos por falta de hierro."));
            }

            // Seed Alergias
            Long aleCount = em.createQuery("SELECT COUNT(a) FROM Alergia a", Long.class).getSingleResult();
            if (aleCount == 0) {
                em.persist(new Alergia("Penicilina", "Alto"));
                em.persist(new Alergia("Aspirina", "Medio"));
                em.persist(new Alergia("Ibuprofeno", "Leve"));
                em.persist(new Alergia("Polvo / Ácaros", "Leve"));
                em.persist(new Alergia("Mariscos", "Alto"));
            }

            // Normalizar niveles de gravedad existentes en la BD a los 3 niveles estándar: Leve, Medio, Alto
            em.createQuery("UPDATE Alergia a SET a.nivelGravedad = 'Alto' WHERE a.nivelGravedad IN ('Severa', 'Severo', 'Alta', 'Anafilaxia')").executeUpdate();
            em.createQuery("UPDATE Alergia a SET a.nivelGravedad = 'Medio' WHERE a.nivelGravedad IN ('Media', 'Moderada', 'Moderado')").executeUpdate();
            em.createQuery("UPDATE Alergia a SET a.nivelGravedad = 'Leve' WHERE a.nivelGravedad IN ('Baja', 'Bajo')").executeUpdate();

            Long espCount = em.createQuery("SELECT COUNT(e) FROM Especialidad e", Long.class).getSingleResult();
            if (espCount == 0) {
                com.nurselogic.model.Especialidad e1 = new com.nurselogic.model.Especialidad(); e1.setDescripcion("Medicina General"); em.persist(e1);
                com.nurselogic.model.Especialidad e2 = new com.nurselogic.model.Especialidad(); e2.setDescripcion("Cardiología"); em.persist(e2);
                com.nurselogic.model.Especialidad e3 = new com.nurselogic.model.Especialidad(); e3.setDescripcion("Pediatría"); em.persist(e3);
                com.nurselogic.model.Especialidad e4 = new com.nurselogic.model.Especialidad(); e4.setDescripcion("Urgencias y Triage"); em.persist(e4);
                com.nurselogic.model.Especialidad e5 = new com.nurselogic.model.Especialidad(); e5.setDescripcion("Neurología"); em.persist(e5);
            }

            // Seed Camas
            Long camaCount = em.createQuery("SELECT COUNT(c) FROM Cama c", Long.class).getSingleResult();
            if (camaCount == 0) {
                // Urgencias
                em.persist(new Cama("Cama U-101", "Urgencias", "Disponible"));
                Cama cU102 = new Cama("Cama U-102", "Urgencias", "Ocupada");
                cU102.setPacienteNombre("Juan Carlos Ortega Vaca");
                cU102.setMedicoNombre("Dr. Carlos Silva");
                cU102.setMotivo("Crisis Hipertensiva");
                em.persist(cU102);
                em.persist(new Cama("Cama U-103", "Urgencias", "Disponible"));
                em.persist(new Cama("Cama U-104", "Urgencias", "Disponible"));

                // UCI
                em.persist(new Cama("Cama UCI-201", "UCI", "Disponible"));
                Cama cUCI202 = new Cama("Cama UCI-202", "UCI", "Ocupada");
                cUCI202.setPacienteNombre("Diego Roman");
                cUCI202.setMedicoNombre("Dra. Ana Martínez");
                cUCI202.setMotivo("Monitoreo Post-operatorio");
                em.persist(cUCI202);
                em.persist(new Cama("Cama UCI-203", "UCI", "Disponible"));
                em.persist(new Cama("Cama UCI-204", "UCI", "Disponible"));

                // Hospitalización General
                em.persist(new Cama("Cama H-301", "Hospitalización General", "Disponible"));
                em.persist(new Cama("Cama H-302", "Hospitalización General", "Disponible"));
                em.persist(new Cama("Cama H-303", "Hospitalización General", "Disponible"));
                em.persist(new Cama("Cama H-304", "Hospitalización General", "Mantenimiento"));
            }

            // Seed Pacientes
            Long pacCount = em.createQuery("SELECT COUNT(p) FROM Paciente p", Long.class).getSingleResult();
            if (pacCount == 0) {
                String[][] pacs = {
                    {"Juan Carlos", "Ortega Vaca", "1712345678", "1985-04-12", "Masculino", "1.75", "78.5", "Hipertensión Arterial", "Penicilina", "36.6", "120/80", "72", "98"},
                    {"Diego", "Roman", "1723456789", "1990-08-23", "Masculino", "1.80", "82.0", "Ninguna", "Ninguna", "36.8", "115/75", "68", "99"},
                    {"Maria Elena", "Gomez Silva", "1734567890", "1978-11-05", "Femenino", "1.62", "64.0", "Diabetes Mellitus Tipo 2", "Aspirina", "37.1", "130/85", "80", "96"},
                    {"Carlos Alberto", "Perez Leon", "1745678901", "2015-02-18", "Masculino", "1.35", "32.0", "Asma Bronquial", "Polvo / Ácaros", "36.7", "100/65", "88", "97"},
                    {"Luisa Fernanda", "Morales Ruiz", "1756789012", "1995-06-30", "Femenino", "1.68", "58.0", "Anemia Ferropénica", "Mariscos", "36.5", "110/70", "70", "99"}
                };
                for (String[] pData : pacs) {
                    Paciente p = new Paciente();
                    p.setNombres(pData[0]);
                    p.setApellidos(pData[1]);
                    p.setCedula(pData[2]);
                    p.setFechaNacimiento(LocalDate.parse(pData[3]));
                    p.setSexo(pData[4]);
                    p.setEstatura(Double.parseDouble(pData[5]));
                    p.setPeso(Double.parseDouble(pData[6]));
                    p.setEnfermedadPreexistente(pData[7]);
                    p.setAlergias(pData[8]);
                    p.setTemperatura(Double.parseDouble(pData[9]));
                    p.setPresionArterial(pData[10]);
                    p.setFrecuenciaCardiaca(Integer.parseInt(pData[11]));
                    p.setSaturacionOxigeno(Integer.parseInt(pData[12]));
                    em.persist(p);
                }
            }

            // Seed Citas para Estadísticas Reales
            Long citaCount = em.createQuery("SELECT COUNT(c) FROM Cita c", Long.class).getSingleResult();
            if (citaCount == 0) {
                List<Especialidad> espList = em.createQuery("SELECT e FROM Especialidad e", Especialidad.class).getResultList();
                List<Paciente> pacList = em.createQuery("SELECT p FROM Paciente p", Paciente.class).getResultList();
                if (!espList.isEmpty() && !pacList.isEmpty()) {
                    String[] estados = {"ATENDIDO", "ATENDIDO", "ATENDIDO", "ATENDIDO", "ATENDIDO", "EN SALA", "EN SALA", "PENDIENTE", "PENDIENTE", "PENDIENTE", "PENDIENTE", "CANCELADO"};
                    for (int i = 0; i < 12; i++) {
                        Cita c = new Cita();
                        c.setFecha(LocalDate.now().plusDays(i % 3 - 1));
                        c.setHora(LocalTime.of(8 + (i % 8), 0));
                        c.setEstado(estados[i % estados.length]);
                        c.setEspecialidad(espList.get(i % espList.size()));
                        c.setPaciente(pacList.get(i % pacList.size()));
                        em.persist(c);
                    }
                }
            }

            tx.commit();
            System.out.println("====== SEEDER EJECUTADO EXITOSAMENTE ======");
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            e.printStackTrace();
        } finally {
            em.close();
        }
    }

    @Override
    public void contextDestroyed(ServletContextEvent sce) {
        // Nada que limpiar aquí
    }
}
