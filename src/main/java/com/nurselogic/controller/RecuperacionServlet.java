package com.nurselogic.controller;

import com.nurselogic.dao.UsuarioDAO;
import com.nurselogic.model.Usuario;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.Properties;
import java.util.Random;
import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

@WebServlet("/recuperar")
public class RecuperacionServlet extends HttpServlet {

    private com.nurselogic.service.UsuarioService usuarioService = new com.nurselogic.service.UsuarioService();

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String action = request.getParameter("action");
        String correo = request.getParameter("correo");

        if ("enviarCodigo".equals(action)) {
            String codigo = String.format("%06d", new Random().nextInt(999999));
            
            // Try to send email. The service determines what to do based on the result.
            boolean correoEnviado = enviarCorreo(correo, codigo);
            
            com.nurselogic.service.UsuarioService.RecuperacionResult result = usuarioService.procesarEnvioCodigo(correo, correoEnviado, codigo);
            
            if (result.success) {
                request.setAttribute("mensaje", result.message);
            } else {
                request.setAttribute("error", result.message);
            }
            if (result.showReset) request.setAttribute("showReset", true);
            if (result.showRecover) request.setAttribute("showRecover", true);
            request.setAttribute("correoRecuperacion", correo);
            
            request.getRequestDispatcher("/login.jsp").forward(request, response);
            
        } else if ("resetClave".equals(action)) {
            String codigoIngresado = request.getParameter("codigo");
            String nuevaClave = request.getParameter("nuevaClave");
            
            com.nurselogic.service.UsuarioService.RecuperacionResult result = usuarioService.procesarResetClave(correo, codigoIngresado, nuevaClave);
            
            if (result.success) {
                request.setAttribute("mensaje", result.message);
            } else {
                request.setAttribute("error", result.message);
                if (result.showReset) request.setAttribute("showReset", true);
                request.setAttribute("correoRecuperacion", correo);
            }
            request.getRequestDispatcher("/login.jsp").forward(request, response);
        }
    }

    private boolean enviarCorreo(String destinatario, String codigo) {
        String host = "smtp.gmail.com";
        Properties props = new Properties();
        props.put("mail.smtp.auth", "true");
        props.put("mail.smtp.starttls.enable", "true");
        props.put("mail.smtp.host", host);
        props.put("mail.smtp.port", "587");

        // Usa variables de entorno del sistema (seguridad)
        String username = System.getenv("NURSELOGIC_EMAIL_USER") != null ? System.getenv("NURSELOGIC_EMAIL_USER") : "tucorreo@gmail.com"; 
        String password = System.getenv("NURSELOGIC_EMAIL_PASS") != null ? System.getenv("NURSELOGIC_EMAIL_PASS") : "lzfv yvnb notu nreq";

        Session session = Session.getInstance(props, new javax.mail.Authenticator() {
            protected PasswordAuthentication getPasswordAuthentication() {
                return new PasswordAuthentication(username, password);
            }
        });

        try {
            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress(username));
            message.setRecipients(Message.RecipientType.TO, InternetAddress.parse(destinatario));
            message.setSubject("Código de Recuperación de Cuenta - NURSELOGIC");
            
            String cuerpoCorreo = "Hola,\n\n"
                    + "Hemos recibido una solicitud para restablecer la contraseña de tu cuenta en el Sistema Clínico Integrado NURSELOGIC.\n\n"
                    + "Tu código de verificación de 6 dígitos es: " + codigo + "\n\n"
                    + "Por favor, ingresa este código en la plataforma para desbloquear tu cuenta y crear una nueva contraseña. "
                    + "Por motivos de seguridad, nunca compartas este código con nadie, ni siquiera con el personal del hospital.\n\n"
                    + "Si no solicitaste este cambio, puedes ignorar este mensaje de forma segura.\n\n"
                    + "Atentamente,\n"
                    + "El Equipo de Soporte de NURSELOGIC";
                    
            message.setText(cuerpoCorreo);
            Transport.send(message);
            return true;
        } catch (MessagingException e) {
            e.printStackTrace();
            System.out.println("=========================================");
            System.out.println("CÓDIGO DE RECUPERACIÓN GENERADO: " + codigo);
            System.out.println("=========================================");
            return false;
        }
    }
}
