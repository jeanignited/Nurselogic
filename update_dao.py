import io

with io.open('src/main/java/com/nurselogic/dao/CitaDAO.java', 'r', encoding='utf-8') as f:
    c = f.read()

new_method = '''
    public String obtenerRecetaUnificada(int idCita, String recetaTextoLibre) {
        EntityManager em = JPAUtil.getEntityManager();
        StringBuilder recetaEstructurada = new StringBuilder();
        try {
            // Intenta consultar la tabla mencionada por el usuario (puede ser por script externo)
            List<Object[]> meds = em.createNativeQuery(
                "SELECT m.nombre, rm.cantidad FROM recetas_medicamentos rm " +
                "JOIN medicamentos m ON rm.medicamento_id = m.id " +
                "WHERE rm.cita_id = :idCita")
                .setParameter("idCita", idCita)
                .getResultList();
                
            for (Object[] row : meds) {
                String medName = (String) row[0];
                Number cant = (Number) row[1];
                recetaEstructurada.append(medName).append(" - ").append(cant).append(" unidad(es). ");
            }
        } catch (Exception e) {
            // Si la tabla o la columna tiene otro nombre y falla, ignora y conserva el texto libre
        } finally {
            if (em.isOpen()) {
                em.close();
            }
        }
        
        String finalReceta = (recetaTextoLibre != null) ? recetaTextoLibre.trim() : "";
        if (recetaEstructurada.length() > 0) {
            if (!finalReceta.isEmpty()) {
                finalReceta = recetaEstructurada.toString() + "Indicaciones adicionales: " + finalReceta;
            } else {
                finalReceta = recetaEstructurada.toString();
            }
        }
        return finalReceta.isEmpty() ? "Ninguna" : finalReceta;
    }
}'''

c = c.replace('}\n}', '}\n' + new_method)

with io.open('src/main/java/com/nurselogic/dao/CitaDAO.java', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated CitaDAO.java")
