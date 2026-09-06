package com.nurselogic.util;

import org.mindrot.jbcrypt.BCrypt;

public class SecurityUtil {

    // Genera un hash seguro para la contraseña
    public static String hashPassword(String plainTextPassword) {
        return BCrypt.hashpw(plainTextPassword, BCrypt.gensalt(12));
    }

    // Verifica si la contraseña en texto plano coincide con el hash
    public static boolean checkPassword(String plainTextPassword, String hashedPassword) {
        if (plainTextPassword == null || hashedPassword == null) {
            return false;
        }
        
        // Comprobar si el hash parece ser de BCrypt o si es texto plano viejo (para compatibilidad hacia atrás temporal si se desea,
        // aunque lo mejor es forzar que todos usen hashes, pero si no se ha migrado la BD, permitimos texto plano)
        if (!hashedPassword.startsWith("$2a$") && !hashedPassword.startsWith("$2b$") && !hashedPassword.startsWith("$2y$")) {
            // Esto es solo para transición. En un sistema 100% seguro, esto debería removerse.
            return plainTextPassword.equals(hashedPassword);
        }

        try {
            return BCrypt.checkpw(plainTextPassword, hashedPassword);
        } catch (IllegalArgumentException e) {
            return false; // Hash inválido
        }
    }
}
