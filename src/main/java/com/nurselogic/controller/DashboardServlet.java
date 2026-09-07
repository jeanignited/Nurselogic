package com.nurselogic.controller;

import com.nurselogic.dao.FacturaDAO;
import com.nurselogic.config.JPAUtil;
import com.nurselogic.model.*;
import jakarta.persistence.EntityManager;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;
import java.time.LocalDate;
import java.util.*;

@WebServlet("/dashboard")
public class DashboardServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        List<Map<String, String>> listaPacientes = new ArrayList<>();
        List<Map<String, String>> listaUsuarios = new ArrayList<>();
        List<Map<String, String>> listaEnfermedades = new ArrayList<>();
        List<Map<String, String>> listaAlergias = new ArrayList<>();
        List<Map<String, String>> listaMedicamentos = new ArrayList<>();
        List<Map<String, String>> listaCamas = new ArrayList<>();
        long totalPac = 0, totalMeds = 0, totalUsers = 0;
        int alertasMeds = 0, alertasCamas = 0, alertasCitas = 0;

        EntityManager em = JPAUtil.getEntityManager();
        HttpSession session = request.getSession();
        String correoLogueado = (String) session.getAttribute("usuarioLogueado");
        String rolUsuario = (String) session.getAttribute("rol");
        Integer loggedPacienteId = null;

        try {
            // Contadores
            try {
                totalPac = em.createQuery("SELECT COUNT(p) FROM Paciente p", Long.class).getSingleResult();
                totalMeds = em.createQuery("SELECT COUNT(m) FROM Medicamento m", Long.class).getSingleResult();
                totalUsers = em.createQuery("SELECT COUNT(u) FROM Usuario u WHERE u.rol != 'Paciente'", Long.class).getSingleResult();
            } catch (Exception e) {}

            // Lista de Pacientes
            try {
                List<Paciente> pList = em.createQuery("SELECT p FROM Paciente p", Paciente.class).getResultList();
                for(Paciente p : pList) {
                    Map<String, String> map = new HashMap<>();
                    map.put("id", String.valueOf(p.getId()));
                    map.put("nombres", p.getNombres());
                    map.put("apellidos", p.getApellidos());
                    map.put("cedula", p.getCedula());
                    map.put("fechaNacimiento", p.getFechaNacimiento() != null ? p.getFechaNacimiento().toString() : "");
                    listaPacientes.add(map);
                }
            } catch (Exception e) {}

            // Lista de Usuarios
            try {
                List<Usuario> uList = em.createQuery("SELECT u FROM Usuario u WHERE u.rol != 'Paciente'", Usuario.class).getResultList();
                for(Usuario u : uList) {
                    Map<String, String> map = new HashMap<>();
                    map.put("nombres", u.getNombres());
                    map.put("apellidos", u.getApellidos());
                    map.put("correo", u.getCorreo());
                    map.put("rol", u.getRol());
                    map.put("especialidad", u.getEspecialidad());
                    listaUsuarios.add(map);
                }
            } catch (Exception e) {}

            // Lista de Enfermedades
            try {
                List<Enfermedad> eList = em.createQuery("SELECT e FROM Enfermedad e", Enfermedad.class).getResultList();
                for(Enfermedad e : eList) {
                    Map<String, String> map = new HashMap<>();
                    map.put("id", String.valueOf(e.getId()));
                    map.put("nombre", e.getNombre());
                    map.put("descripcion", e.getDescripcion() != null ? e.getDescripcion() : "");
                    listaEnfermedades.add(map);
                }
            } catch (Exception e) {}

            // Lista de Alergias
            try {
                List<Alergia> aList = em.createQuery("SELECT a FROM Alergia a", Alergia.class).getResultList();
                for(Alergia a : aList) {
                    Map<String, String> map = new HashMap<>();
                    map.put("id", String.valueOf(a.getId()));
                    map.put("nombre", a.getNombre());
                    map.put("gravedad", a.getNivelGravedad());
                    listaAlergias.add(map);
                }
            } catch (Exception e) {}

            // Lista de Roles (Roles Dinamicos)
            try {
                List<com.nurselogic.model.Rol> rList = em.createQuery("SELECT r FROM Rol r", com.nurselogic.model.Rol.class).getResultList();
                List<String> listaRoles = new ArrayList<>();
                for(com.nurselogic.model.Rol r : rList) {
                    listaRoles.add(r.getNombre());
                }
                request.setAttribute("listaRoles", listaRoles);
            } catch (Exception e) {}

            // Lista de Medicamentos
            try {
                List<Medicamento> mList = em.createQuery("SELECT m FROM Medicamento m ORDER BY m.nombre ASC", Medicamento.class).getResultList();
                for(Medicamento m : mList) {
                    Map<String, String> map = new HashMap<>();
                    map.put("id", String.valueOf(m.getId()));
                    map.put("nombre", m.getNombre());
                    map.put("stock", String.valueOf(m.getStock()));
                    map.put("precio", m.getPrecio() != null ? String.valueOf(m.getPrecio()) : "0.0");
                    listaMedicamentos.add(map);
                    if (m.getStock() < 10) alertasMeds++;
                }
            } catch (Exception e) { e.printStackTrace(); }

            // Paciente Logueado (para Dashboard Paciente)
            try {
                if (correoLogueado != null && "Paciente".equals(rolUsuario)) {
                    Usuario user = em.createQuery("SELECT u FROM Usuario u WHERE u.correo = :correo", Usuario.class)
                            .setParameter("correo", correoLogueado)
                            .getSingleResult();

                    Paciente miPaciente = em.createQuery("SELECT p FROM Paciente p WHERE p.cedula = :cedula", Paciente.class)
                            .setParameter("cedula", user.getCedula())
                            .getResultStream()
                            .findFirst()
                            .orElse(null);
                    
                    if (miPaciente == null) {
                        try {
                            em.getTransaction().begin();
                            miPaciente = new Paciente();
                            miPaciente.setNombres(user.getNombres());
                            miPaciente.setApellidos(user.getApellidos());
                            miPaciente.setCedula(user.getCedula());
                            em.persist(miPaciente);
                            em.getTransaction().commit();
                        } catch(Exception ex) {
                            if(em.getTransaction().isActive()) em.getTransaction().rollback();
                        }
                    }

                    if (miPaciente != null) {
                        loggedPacienteId = miPaciente.getId();
                        session.setAttribute("pacienteId", String.valueOf(loggedPacienteId));
                        request.setAttribute("miHistoriaClinica", miPaciente);
                    }
                }
            } catch (Exception e) {}

            // Lista de Citas
            List<Map<String, String>> listaCitas = new ArrayList<>();
            try {
                String citaQuery = "SELECT c FROM Cita c ORDER BY c.fecha DESC, c.hora ASC";
                if ("Paciente".equals(rolUsuario) && loggedPacienteId != null) {
                    citaQuery = "SELECT c FROM Cita c WHERE c.paciente.id = " + loggedPacienteId + " ORDER BY c.fecha DESC, c.hora ASC";
                }
                
                List<com.nurselogic.model.Cita> cList = em.createQuery(citaQuery, com.nurselogic.model.Cita.class).getResultList();
                for(com.nurselogic.model.Cita c : cList) {
                    Map<String, String> map = new HashMap<>();
                    map.put("id", String.valueOf(c.getId()));
                    map.put("fecha", c.getFecha() != null ? c.getFecha().toString() : "");
                    map.put("hora", c.getHora() != null ? c.getHora().toString() : "");
                    map.put("estado", c.getEstado() != null ? c.getEstado() : "REGISTRADO");
                    map.put("paciente", c.getPaciente() != null ? (c.getPaciente().getNombres() + " " + c.getPaciente().getApellidos()) : "Paciente genérico");
                    map.put("cedula", c.getPaciente() != null && c.getPaciente().getCedula() != null ? c.getPaciente().getCedula() : "");
                    map.put("especialidad", c.getEspecialidad() != null ? c.getEspecialidad().getDescripcion() : "Medicina General");
                    listaCitas.add(map);
                    
                    if (!"Paciente".equals(rolUsuario) && ("REGISTRADO".equals(c.getEstado()) || "EN SALA".equals(c.getEstado()))) {
                        if (c.getFecha() != null && c.getFecha().isEqual(LocalDate.now())) {
                            alertasCitas++;
                        }
                    }
                }
            } catch(Exception ex) {}
            request.setAttribute("listaCitas", listaCitas);

            
            // Lista de Facturas
            List<Factura> listaFacturas = new ArrayList<>();
            try {
                if ("Admin".equals(rolUsuario) || "Farmacéutico".equals(rolUsuario) || "Farmacéutico".equals(rolUsuario)) {
                    FacturaDAO fDao = new FacturaDAO();
                    listaFacturas = fDao.listarFacturas();
                }
            } catch(Exception ex) {}
            request.setAttribute("listaFacturas", listaFacturas);

            // Lista de Especialidades
            List<String> listaEspecialidades = new ArrayList<>();
            List<Map<String, String>> listaEspecialidadesMap = new ArrayList<>();
            try {
                List<com.nurselogic.model.Especialidad> espList = em.createQuery("SELECT e FROM Especialidad e", com.nurselogic.model.Especialidad.class).getResultList();
                
                // Seed if empty to prevent Foreign Key constraints failing
                if (espList.isEmpty()) {
                    em.getTransaction().begin();
                    String[] defaultEsps = {"Medicina General", "Odontología", "Pediatría", "Ginecología", "Cardiología", "Urgencias y Triage"};
                    for (String desc : defaultEsps) {
                        com.nurselogic.model.Especialidad newEsp = new com.nurselogic.model.Especialidad();
                        newEsp.setDescripcion(desc);
                        em.persist(newEsp);
                        espList.add(newEsp);
                    }
                    em.getTransaction().commit();
                }

                for(com.nurselogic.model.Especialidad esp : espList) {
                    listaEspecialidades.add(esp.getDescripcion());
                    Map<String, String> mapEsp = new HashMap<>();
                    mapEsp.put("id", String.valueOf(esp.getId()));
                    mapEsp.put("descripcion", esp.getDescripcion());
                    listaEspecialidadesMap.add(mapEsp);
                }
            } catch(Exception ex) {
                if (em.getTransaction().isActive()) {
                    em.getTransaction().rollback();
                }
            }
            request.setAttribute("listaEspecialidades", listaEspecialidades);
            request.setAttribute("listaEspecialidadesMap", listaEspecialidadesMap);

            // Lista de Camas
            try {
                List<com.nurselogic.model.Cama> camaList = em.createQuery("SELECT c FROM Cama c ORDER BY c.sala ASC, c.numero ASC", com.nurselogic.model.Cama.class).getResultList();
                for(com.nurselogic.model.Cama cam : camaList) {
                    Map<String, String> mapCam = new HashMap<>();
                    mapCam.put("id", String.valueOf(cam.getId()));
                    mapCam.put("numero", cam.getNumero());
                    
                    String salaName = cam.getSala();
                    if (salaName == null || salaName.trim().isEmpty() || "Sala General".equalsIgnoreCase(salaName)) {
                        salaName = "Hospitalización General";
                    }
                    mapCam.put("sala", salaName);
                    mapCam.put("estado", cam.getEstado());
                    mapCam.put("paciente", cam.getPacienteNombre() != null ? cam.getPacienteNombre() : "");
                    mapCam.put("medico", cam.getMedicoNombre() != null ? cam.getMedicoNombre() : "");
                    mapCam.put("motivo", cam.getMotivo() != null ? cam.getMotivo() : "");
                    listaCamas.add(mapCam);
                    
                    if ("Ocupada".equalsIgnoreCase(cam.getEstado())) {
                        alertasCamas++;
                    }
                }
            } catch(Exception ex) {}
            request.setAttribute("listaCamas", listaCamas);

            // Permisos de Usuario
            String permisosUsuario = "";
            if ("Admin".equalsIgnoreCase(rolUsuario)) {
                permisosUsuario = "GESTION_USUARIOS,GESTION_MEDICAMENTOS,GESTION_CATALOGOS,REGISTRO_PACIENTES,AGENDAR_CITAS";
            } else if (rolUsuario != null && !"Paciente".equals(rolUsuario)) {
                try {
                    com.nurselogic.model.Rol rolObj = em.createQuery("SELECT r FROM Rol r WHERE r.nombre = :nombre", com.nurselogic.model.Rol.class)
                            .setParameter("nombre", rolUsuario)
                            .getResultStream()
                            .findFirst()
                            .orElse(null);
                    if (rolObj != null && rolObj.getPermisos() != null) {
                        permisosUsuario = rolObj.getPermisos();
                    }
                } catch (Exception ex) {}
            }
            request.setAttribute("permisosUsuario", permisosUsuario);

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            if (em.isOpen()) {
                em.close();
            }
        }

        request.setAttribute("totalPacientes", totalPac);
        request.setAttribute("totalMeds", totalMeds);
        request.setAttribute("totalUsers", totalUsers);
        request.setAttribute("listaPacientes", listaPacientes);
        request.setAttribute("listaUsuarios", listaUsuarios);
        request.setAttribute("listaEnfermedades", listaEnfermedades);
        request.setAttribute("listaAlergias", listaAlergias);
        request.setAttribute("listaMedicamentos", listaMedicamentos);
        request.setAttribute("alertasMeds", alertasMeds);
        request.setAttribute("alertasCamas", alertasCamas);
        request.setAttribute("alertasCitas", alertasCitas);

        request.getRequestDispatcher("index.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response);
    }
}