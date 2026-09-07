package com.nurselogic.service;

import com.nurselogic.dao.*;
import com.nurselogic.model.*;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import com.nurselogic.config.JPAUtil;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityTransaction;

public class AdminService {
    
    public static class ActionResult {
        public boolean success;
        public String message;
        public ActionResult(boolean success, String message) {
            this.success = success;
            this.message = message;
        }
    }

    public ActionResult eliminarPaciente(String id, boolean isAdmin) {
        if (!isAdmin) return new ActionResult(false, "Solo los administradores pueden eliminar registros.");
        PacienteDAO pDao = new PacienteDAO();
        if (pDao.eliminarPaciente(id)) return new ActionResult(true, "Paciente eliminado con éxito.");
        return new ActionResult(false, "No se pudo eliminar el paciente.");
    }

    public ActionResult eliminarUsuario(String id, boolean isAdmin, String correoActual) {
        if (!isAdmin) return new ActionResult(false, "Solo los administradores pueden eliminar registros.");
        if (id != null && id.equalsIgnoreCase(correoActual)) return new ActionResult(false, "No puedes eliminar tu propia cuenta de administrador.");
        UsuarioDAO uDao = new UsuarioDAO();
        if (uDao.eliminarUsuario(id)) return new ActionResult(true, "Personal eliminado con éxito.");
        return new ActionResult(false, "No se pudo eliminar el personal.");
    }

    public ActionResult editarRol(String id, String nuevoRol, boolean isAdmin, String correoActual) {
        if (!isAdmin) return new ActionResult(false, "Solo los administradores pueden cambiar roles.");
        if (id != null && id.equalsIgnoreCase(correoActual)) return new ActionResult(false, "No puedes cambiar tu propio rol de administrador.");
        if (nuevoRol != null && !nuevoRol.trim().isEmpty()) {
            UsuarioDAO uDao = new UsuarioDAO();
            if (uDao.actualizarRolUsuario(id, nuevoRol)) return new ActionResult(true, "Rol de personal actualizado con éxito.");
            return new ActionResult(false, "No se pudo actualizar el rol.");
        }
        return new ActionResult(false, "Rol no especificado.");
    }

    public ActionResult editarEspecialidad(String id, String nuevaEsp) {
        if (id != null && !id.trim().isEmpty() && nuevaEsp != null && !nuevaEsp.trim().isEmpty()) {
            UsuarioDAO uDao = new UsuarioDAO();
            if (uDao.actualizarEspecialidadUsuario(id, nuevaEsp)) return new ActionResult(true, "Especialidad asignada con éxito.");
            return new ActionResult(false, "No se pudo actualizar la especialidad.");
        }
        return new ActionResult(false, "Especialidad o ID inválido.");
    }

    public ActionResult crearRol(String nombreRol, String descRol, String permisosStr, boolean isAdmin) {
        if (!isAdmin) return new ActionResult(false, "Solo los administradores pueden crear roles.");
        if (nombreRol != null && !nombreRol.trim().isEmpty()) {
            RolDAO rolDao = new RolDAO();
            Rol nuevo = new Rol(nombreRol.trim(), descRol, permisosStr);
            if (rolDao.guardarRol(nuevo)) return new ActionResult(true, "Nuevo rol '" + nombreRol + "' creado exitosamente.");
            return new ActionResult(false, "No se pudo crear el rol. Verifica que no exista otro con el mismo nombre.");
        }
        return new ActionResult(false, "El nombre del rol es obligatorio.");
    }

    public ActionResult crearMedicamento(String nomMed, String stockMedStr, String precioMedStr) {
        if (nomMed != null && !nomMed.trim().isEmpty() && stockMedStr != null) {
            MedicamentoDAO mDao = new MedicamentoDAO();
            Medicamento m = new Medicamento();
            m.setNombre(nomMed.trim());
            try { m.setStock(Integer.parseInt(stockMedStr)); } catch(Exception ex) { m.setStock(0); }
            try { m.setPrecio(precioMedStr != null && !precioMedStr.isEmpty() ? Double.parseDouble(precioMedStr) : 0.0); } catch(Exception ex) { m.setPrecio(0.0); }
            if (mDao.guardarMedicamento(m)) return new ActionResult(true, "Medicamento '" + nomMed + "' registrado en farmacia.");
            return new ActionResult(false, "Error al guardar el medicamento.");
        }
        return new ActionResult(false, "Datos inválidos para medicamento.");
    }

    
    public ActionResult procesarVentaFarmacia(String idMedStr, String cantidadStr, String clienteNombre) {
        if (idMedStr == null || cantidadStr == null) return new ActionResult(false, "Faltan datos de la venta.");
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            int idMed = Integer.parseInt(idMedStr);
            int cantidad = Integer.parseInt(cantidadStr);
            
            Medicamento med = em.find(Medicamento.class, idMed);
            if (med == null) {
                tx.rollback();
                return new ActionResult(false, "Medicamento no encontrado.");
            }
            if (med.getStock() < cantidad) {
                tx.rollback();
                return new ActionResult(false, "Stock insuficiente.");
            }
            
            // Reducir stock
            med.setStock(med.getStock() - cantidad);
            
            // Generar factura
            Factura fac = new Factura();
            fac.setFechaEmision(LocalDateTime.now());
            fac.setClienteNombre(clienteNombre != null && !clienteNombre.trim().isEmpty() ? clienteNombre : "Consumidor Final");
            
            double subtotal = med.getPrecio() * cantidad;
            fac.setTotal(subtotal);
            
            FacturaDetalle det = new FacturaDetalle();
            det.setFactura(fac);
            det.setMedicamento(med);
            det.setCantidad(cantidad);
            det.setPrecioUnitario(med.getPrecio());
            det.setSubtotal(subtotal);
            
            List<FacturaDetalle> listaDet = new ArrayList<>();
            listaDet.add(det);
            fac.setDetalles(listaDet);
            
            em.persist(fac);
            
            tx.commit();
            return new ActionResult(true, "Venta facturada exitosamente a " + fac.getClienteNombre());
        } catch (Exception ex) {
            if (tx.isActive()) tx.rollback();
            ex.printStackTrace();
            return new ActionResult(false, "Error interno al facturar.");
        } finally {
            em.close();
        }
    }

    public ActionResult ajustarStock(String idMedStr, String cambioStr) {
        try {
            int idMed = Integer.parseInt(idMedStr);
            int cambio = Integer.parseInt(cambioStr);
            MedicamentoDAO mDao = new MedicamentoDAO();
            if (mDao.ajustarStock(idMed, cambio)) return new ActionResult(true, "Stock de farmacia actualizado.");
            return new ActionResult(false, "No se pudo actualizar el stock.");
        } catch(Exception ex) {
            return new ActionResult(false, "Datos de stock inválidos.");
        }
    }

    public ActionResult crearEnfermedad(String nomEnf, String descEnf) {
        if (nomEnf != null && !nomEnf.trim().isEmpty()) {
            EntityManager em = JPAUtil.getEntityManager();
            EntityTransaction tx = em.getTransaction();
            try {
                tx.begin();
                em.persist(new Enfermedad(nomEnf.trim(), descEnf != null ? descEnf : "Patología clínica registrada."));
                tx.commit();
                return new ActionResult(true, "Patología '" + nomEnf + "' agregada al catálogo.");
            } catch(Exception ex) {
                if (tx.isActive()) tx.rollback();
                return new ActionResult(false, "Error al registrar la enfermedad en el catálogo.");
            } finally { em.close(); }
        }
        return new ActionResult(false, "Datos inválidos.");
    }

    public ActionResult crearAlergia(String nomAle, String gravAle) {
        if (nomAle != null && !nomAle.trim().isEmpty()) {
            EntityManager em = JPAUtil.getEntityManager();
            EntityTransaction tx = em.getTransaction();
            try {
                tx.begin();
                em.persist(new Alergia(nomAle.trim(), gravAle != null ? gravAle : "Leve"));
                tx.commit();
                return new ActionResult(true, "Alérgeno '" + nomAle + "' registrado exitosamente.");
            } catch(Exception ex) {
                if (tx.isActive()) tx.rollback();
                return new ActionResult(false, "Error al registrar la alergia en el catálogo.");
            } finally { em.close(); }
        }
        return new ActionResult(false, "Datos inválidos.");
    }

    public ActionResult actualizarEstadoCita(String idCitaStr, String nuevoEst) {
        try {
            int idCita = Integer.parseInt(idCitaStr);
            CitaDAO cDao = new CitaDAO();
            if (cDao.actualizarEstadoCita(idCita, nuevoEst)) return new ActionResult(true, "Cita marcada como: " + nuevoEst);
            return new ActionResult(false, "No se pudo actualizar la cita.");
        } catch(Exception ex) {
            return new ActionResult(false, "ID de cita inválido.");
        }
    }

    public ActionResult atenderCita(String idCitaStr, String diagnostico, String receta) {
        if (idCitaStr != null && diagnostico != null && !diagnostico.trim().isEmpty()) {
            EntityManager em = JPAUtil.getEntityManager();
            EntityTransaction tx = em.getTransaction();
            try {
                tx.begin();
                Cita cita = em.find(Cita.class, Integer.parseInt(idCitaStr));
                if (cita != null) {
                    cita.setEstado("ATENDIDO");
                    cita.setDiagnostico(diagnostico.trim());
                    cita.setReceta(receta != null ? receta.trim() : "");
                    tx.commit();
                    return new ActionResult(true, "Consulta completada. El diagnóstico ha sido guardado en la Historia Clínica.");
                }
                tx.rollback();
                return new ActionResult(false, "Cita no encontrada.");
            } catch(Exception ex) {
                if (tx.isActive()) tx.rollback();
                return new ActionResult(false, "Error al guardar la atención médica.");
            } finally { em.close(); }
        }
        return new ActionResult(false, "El diagnóstico es obligatorio para finalizar la consulta.");
    }

    public ActionResult editarEnfermedad(String idStr, String nomEnf, String descEnf) {
        if (idStr != null && nomEnf != null && !nomEnf.trim().isEmpty()) {
            EntityManager em = JPAUtil.getEntityManager();
            EntityTransaction tx = em.getTransaction();
            try {
                tx.begin();
                Enfermedad enf = em.find(Enfermedad.class, Integer.parseInt(idStr));
                if (enf != null) {
                    enf.setNombre(nomEnf.trim());
                    enf.setDescripcion(descEnf != null ? descEnf : "");
                    tx.commit();
                    return new ActionResult(true, "Enfermedad actualizada correctamente.");
                }
                tx.rollback();
                return new ActionResult(false, "No encontrada.");
            } catch(Exception ex) {
                if (tx.isActive()) tx.rollback();
                return new ActionResult(false, "Error al actualizar la enfermedad.");
            } finally { em.close(); }
        }
        return new ActionResult(false, "Datos inválidos.");
    }

    public ActionResult borrarEnfermedad(String idStr) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            Enfermedad enf = em.find(Enfermedad.class, Integer.parseInt(idStr));
            if (enf != null) {
                em.remove(enf);
                tx.commit();
                return new ActionResult(true, "Enfermedad eliminada del catálogo.");
            }
            tx.rollback();
            return new ActionResult(false, "No encontrada.");
        } catch(Exception ex) {
            if (tx.isActive()) tx.rollback();
            return new ActionResult(false, "Error al eliminar la enfermedad.");
        } finally { em.close(); }
    }

    public ActionResult editarAlergia(String idStr, String nomAle, String gravAle) {
        if (idStr != null && nomAle != null && !nomAle.trim().isEmpty()) {
            EntityManager em = JPAUtil.getEntityManager();
            EntityTransaction tx = em.getTransaction();
            try {
                tx.begin();
                Alergia ale = em.find(Alergia.class, Integer.parseInt(idStr));
                if (ale != null) {
                    ale.setNombre(nomAle.trim());
                    ale.setNivelGravedad(gravAle != null ? gravAle : "Leve");
                    tx.commit();
                    return new ActionResult(true, "Alergia actualizada correctamente.");
                }
                tx.rollback();
                return new ActionResult(false, "No encontrada.");
            } catch(Exception ex) {
                if (tx.isActive()) tx.rollback();
                return new ActionResult(false, "Error al actualizar la alergia.");
            } finally { em.close(); }
        }
        return new ActionResult(false, "Datos inválidos.");
    }

    public ActionResult borrarAlergia(String idStr) {
        EntityManager em = JPAUtil.getEntityManager();
        EntityTransaction tx = em.getTransaction();
        try {
            tx.begin();
            Alergia ale = em.find(Alergia.class, Integer.parseInt(idStr));
            if (ale != null) {
                em.remove(ale);
                tx.commit();
                return new ActionResult(true, "Alérgeno eliminado del catálogo.");
            }
            tx.rollback();
            return new ActionResult(false, "No encontrado.");
        } catch(Exception ex) {
            if (tx.isActive()) tx.rollback();
            return new ActionResult(false, "Error al eliminar la alergia.");
        } finally { em.close(); }
    }

    public ActionResult prescribirReceta(String[] idsMedStr, String[] cantidadesStr, String pacNombre, String cedula, String indicaciones, boolean esNuevo, String nuevoNombres, String nuevoApellidos, String nuevoFechaNac, String nuevoSexo) {
        if (idsMedStr != null && cantidadesStr != null && idsMedStr.length == cantidadesStr.length) {
            EntityManager em = JPAUtil.getEntityManager();
            EntityTransaction tx = em.getTransaction();
            try {
                tx.begin();
                
                Paciente p = null;
                if (cedula != null && !cedula.trim().isEmpty()) {
                    p = em.createQuery("SELECT p FROM Paciente p WHERE p.cedula = :cedula", Paciente.class)
                          .setParameter("cedula", cedula.trim())
                          .getResultStream().findFirst().orElse(null);
                }

                if (p == null && pacNombre != null && !pacNombre.trim().isEmpty()) {
                    String pName = pacNombre.trim();
                    try {
                        p = em.createQuery("SELECT p FROM Paciente p WHERE LOWER(CONCAT(p.nombres, ' ', p.apellidos)) LIKE :nameVal OR LOWER(p.nombres) LIKE :nameVal", Paciente.class)
                              .setParameter("nameVal", "%" + pName.toLowerCase() + "%")
                              .getResultStream().findFirst().orElse(null);
                    } catch(Exception ignored){}
                }

                if (p == null) {
                    p = new Paciente();
                    String cleanCed = (cedula != null && !cedula.trim().isEmpty()) ? cedula.trim() : String.valueOf(System.currentTimeMillis()).substring(0, 10);
                    p.setCedula(cleanCed);
                    String n = (nuevoNombres != null && !nuevoNombres.trim().isEmpty()) ? nuevoNombres.trim() : (pacNombre != null && !pacNombre.trim().isEmpty() ? pacNombre.trim() : "Paciente");
                    String a = (nuevoApellidos != null && !nuevoApellidos.trim().isEmpty()) ? nuevoApellidos.trim() : "Registrado";
                    p.setNombres(n);
                    p.setApellidos(a);
                    if (nuevoFechaNac != null && !nuevoFechaNac.isEmpty()) {
                        try { p.setFechaNacimiento(LocalDate.parse(nuevoFechaNac)); } catch(Exception ignored){}
                    }
                    if (nuevoSexo != null && !nuevoSexo.isEmpty()) p.setSexo(nuevoSexo);
                    em.persist(p);
                    pacNombre = p.getNombres() + " " + p.getApellidos();
                } else {
                    pacNombre = p.getNombres() + " " + p.getApellidos();
                }

                StringBuilder nombres = new StringBuilder();
                boolean alMenosUno = false;
                double totalVenta = 0.0;
                
                for (int i = 0; i < idsMedStr.length; i++) {
                    try {
                        int idMed = Integer.parseInt(idsMedStr[i]);
                        int cantidad = Integer.parseInt(cantidadesStr[i]);
                        Medicamento med = em.find(Medicamento.class, idMed);
                        if (med != null) {
                            int nuevoStock = Math.max(0, med.getStock() - cantidad);
                            med.setStock(nuevoStock);
                            double subtotal = (med.getPrecio() != null ? med.getPrecio() : 0.0) * cantidad;
                            totalVenta += subtotal;

                            if (alMenosUno) nombres.append(", ");
                            nombres.append(med.getNombre()).append(" (x").append(cantidad).append(")");
                            alMenosUno = true;
                        }
                    } catch (NumberFormatException ignored) {}
                }
                
                if (alMenosUno) {
                    if (p != null) {
                        Cita c = new Cita();
                        c.setPaciente(p);
                        c.setFecha(LocalDate.now());
                        c.setHora(java.time.LocalTime.now());
                        c.setEstado("ATENDIDO");
                        String recetaFull = "Medicamentos: " + nombres.toString() + "\nIndicaciones: " + (indicaciones != null ? indicaciones : "Según criterio médico") + "\nTotal Venta: $" + String.format(Locale.US, "%.2f", totalVenta);
                        c.setReceta(recetaFull);
                        em.persist(c);
                    }
                    tx.commit();
                    return new ActionResult(true, "Receta prescrita correctamente para " + (pacNombre != null ? pacNombre : "paciente") + ". Total: $" + String.format(Locale.US, "%.2f", totalVenta));
                }
                
                tx.rollback();
                return new ActionResult(false, "Medicamento no encontrado en el inventario.");
            } catch(Exception ex) {
                if (tx.isActive()) tx.rollback();
                ex.printStackTrace();
                return new ActionResult(false, "Error al procesar la prescripci&oacute;n m&eacute;dica.");
            } finally { em.close(); }
        }
        return new ActionResult(false, "Faltan par&aacute;metros para prescribir receta.");
    }

    public ActionResult prescribirReceta(String[] idsMedStr, String[] cantidadesStr, String pacNombre) {
        return prescribirReceta(idsMedStr, cantidadesStr, pacNombre, null, null, false, null, null, null, null);
    }

    public ActionResult internarPaciente(String idCamaStr, String pacNombre, String medNombre, String motivo) {
        if (idCamaStr != null) {
            EntityManager em = JPAUtil.getEntityManager();
            EntityTransaction tx = em.getTransaction();
            try {
                tx.begin();
                Cama cama = em.find(Cama.class, Integer.parseInt(idCamaStr));
                if (cama != null) {
                    cama.setEstado("Ocupada");
                    cama.setPacienteNombre(pacNombre != null ? pacNombre.trim() : "Paciente Anónimo");
                    cama.setMedicoNombre(medNombre != null ? medNombre.trim() : "Médico de Guardia");
                    cama.setMotivo(motivo != null ? motivo.trim() : "Observación");
                    tx.commit();
                    return new ActionResult(true, "Paciente internado en " + cama.getNumero() + " con éxito.");
                }
                tx.rollback();
                return new ActionResult(false, "No encontrada.");
            } catch(Exception ex) {
                if (tx.isActive()) tx.rollback();
                return new ActionResult(false, "Error al internar al paciente en la cama hospitalaria.");
            } finally { em.close(); }
        }
        return new ActionResult(false, "Faltan datos.");
    }

    public ActionResult darAltaCama(String idCamaStr) {
        if (idCamaStr != null) {
            EntityManager em = JPAUtil.getEntityManager();
            EntityTransaction tx = em.getTransaction();
            try {
                tx.begin();
                Cama cama = em.find(Cama.class, Integer.parseInt(idCamaStr));
                if (cama != null) {
                    String pac = cama.getPacienteNombre();
                    cama.setEstado("Disponible");
                    cama.setPacienteNombre("");
                    cama.setMedicoNombre("");
                    cama.setMotivo("");
                    tx.commit();
                    return new ActionResult(true, "Alta médica registrada para " + (pac != null && !pac.isEmpty() ? pac : "el paciente") + ". Cama liberada.");
                }
                tx.rollback();
                return new ActionResult(false, "Cama no encontrada.");
            } catch(Exception ex) {
                if (tx.isActive()) tx.rollback();
                return new ActionResult(false, "Error al liberar la cama hospitalaria.");
            } finally { em.close(); }
        }
        return new ActionResult(false, "Faltan datos.");
    }

    public ActionResult cambiarEstadoCama(String idCamaStr, String nuevoEst) {
        if (idCamaStr != null && nuevoEst != null) {
            EntityManager em = JPAUtil.getEntityManager();
            EntityTransaction tx = em.getTransaction();
            try {
                tx.begin();
                Cama cama = em.find(Cama.class, Integer.parseInt(idCamaStr));
                if (cama != null) {
                    cama.setEstado(nuevoEst);
                    if ("Disponible".equals(nuevoEst)) {
                        cama.setPacienteNombre("");
                        cama.setMedicoNombre("");
                        cama.setMotivo("");
                    }
                    tx.commit();
                    return new ActionResult(true, "Estado de " + cama.getNumero() + " actualizado a " + nuevoEst + ".");
                }
                tx.rollback();
                return new ActionResult(false, "Cama no encontrada.");
            } catch(Exception ex) {
                if (tx.isActive()) tx.rollback();
                return new ActionResult(false, "Error al cambiar el estado de la cama.");
            } finally { em.close(); }
        }
        return new ActionResult(false, "Faltan datos.");
    }
}
