package com.nurselogic.service;

import com.nurselogic.dao.UsuarioDAO;
import com.nurselogic.model.Usuario;
import com.nurselogic.model.Paciente;
import com.nurselogic.config.JPAUtil;
import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityTransaction;
import com.nurselogic.util.SecurityUtil;

public class UsuarioService {
    private UsuarioDAO dao = new UsuarioDAO();

    public static class LoginResult {
        public boolean success;
        public String message;
        public Usuario usuario;
        public boolean showRecover;

        public LoginResult(boolean success, String message, Usuario usuario, boolean showRecover) {
            this.success = success;
            this.message = message;
            this.usuario = usuario;
            this.showRecover = showRecover;
        }
    }

    public LoginResult login(String correo, String clave) {
        Usuario u = dao.buscarPorCorreo(correo);
        
        if (u == null) {
            return new LoginResult(false, "El usuario no existe en nuestros registros.", null, false);
        }

        if (u.isBloqueado()) {
            return new LoginResult(false, "Tu cuenta está bloqueada por demasiados intentos fallidos. Por favor, recupera tu contraseña.", null, true);
        }

        if (SecurityUtil.checkPassword(clave, u.getClave())) {
            u.setIntentosFallidos(0);
            dao.actualizarUsuario(u);
            return new LoginResult(true, "Login exitoso", u, false);
        } else {
            int intentos = u.getIntentosFallidos() + 1;
            u.setIntentosFallidos(intentos);
            
            if (intentos >= 3) {
                u.setBloqueado(true);
                dao.actualizarUsuario(u);
                return new LoginResult(false, "Has superado los 3 intentos fallidos. Tu cuenta ha sido bloqueada por seguridad. Usa la opción de recuperar contraseña.", null, true);
            } else {
                dao.actualizarUsuario(u);
                return new LoginResult(false, "Contraseña incorrecta. Te quedan " + (3 - intentos) + " intentos.", null, false);
            }
        }
    }

    public static class RegistroResult {
        public boolean success;
        public String message;
        public RegistroResult(boolean success, String message) {
            this.success = success;
            this.message = message;
        }
    }

    public RegistroResult registrarUsuario(Usuario u, String tipoUsuario) {
        boolean esPrimerPersonal = false;
        if ("Paciente".equals(tipoUsuario)) {
            u.setRol("Paciente");
        } else {
            if (dao.contarPersonalMedico() == 0) {
                u.setRol("Admin");
                esPrimerPersonal = true;
            } else {
                u.setRol("Pendiente");
            }
        }

                if (dao.registrarUsuario(u)) {
            if ("Paciente".equals(tipoUsuario)) {
                try {
                    EntityManager em = JPAUtil.getEntityManager();
                    EntityTransaction tx = em.getTransaction();
                    tx.begin();
                    Paciente p = new Paciente();
                    p.setNombres(u.getNombres());
                    p.setApellidos(u.getApellidos());
                    p.setCedula(u.getCedula());
                    em.persist(p);
                    tx.commit();
                    em.close();
                } catch(Exception e) {
                    e.printStackTrace();
                }
                return new RegistroResult(true, "¡Cuenta creada! Ya puedes iniciar sesión para agendar citas.");
            } else if (esPrimerPersonal) {
                return new RegistroResult(true, "¡Cuenta creada como Administrador principal! Al ser el primer miembro del personal, se te han otorgado todos los permisos.");
            } else {
                return new RegistroResult(true, "¡Cuenta creada! Espera la habilitación del Administrador.");
            }
        } else {
            return new RegistroResult(false, "Error al crear la cuenta. Revisa los datos o el correo.");
        }
    }

    public static class RecuperacionResult {
        public boolean success;
        public String message;
        public boolean showReset;
        public boolean showRecover;

        public RecuperacionResult(boolean success, String message, boolean showReset, boolean showRecover) {
            this.success = success;
            this.message = message;
            this.showReset = showReset;
            this.showRecover = showRecover;
        }
    }

    public RecuperacionResult procesarEnvioCodigo(String correo, boolean correoEnviado, String codigoGenerado) {
        Usuario u = dao.buscarPorCorreo(correo);
        if (u != null) {
            u.setCodigoRecuperacion(codigoGenerado);
            dao.actualizarUsuario(u);
            if (correoEnviado) {
                return new RecuperacionResult(true, "Código enviado a tu correo. Revisa tu bandeja de entrada.", true, false);
            } else {
                return new RecuperacionResult(false, "Sistema sin configurar (MODO DEV): Como no hay un correo real configurado, tu código de recuperación es: " + codigoGenerado, true, false);
            }
        } else {
            return new RecuperacionResult(false, "El correo no está registrado.", false, true);
        }
    }

    public RecuperacionResult procesarResetClave(String correo, String codigoIngresado, String nuevaClave) {
        Usuario u = dao.buscarPorCorreo(correo);
        if (u != null && codigoIngresado != null && codigoIngresado.equals(u.getCodigoRecuperacion())) {
            u.setClave(SecurityUtil.hashPassword(nuevaClave));
            u.setBloqueado(false);
            u.setIntentosFallidos(0);
            u.setCodigoRecuperacion(null);
            dao.actualizarUsuario(u);
            return new RecuperacionResult(true, "Contraseña actualizada exitosamente. Ya puedes iniciar sesión.", false, false);
        } else {
            return new RecuperacionResult(false, "Código incorrecto.", true, false);
        }
    }
}
