import io

# Update AdminService.java to add buscarClientePorCedula
with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'r', encoding='utf-8') as f:
    c = f.read()

func = '''
    public String buscarClientePorCedula(String cedula) {
        if (cedula == null || cedula.trim().length() < 10) return "{}";
        EntityManager em = JPAUtil.getEntityManager();
        try {
            // Check in Paciente first
            List<com.nurselogic.model.Paciente> pacientes = em.createQuery("SELECT p FROM Paciente p WHERE p.cedula = :c", com.nurselogic.model.Paciente.class).setParameter("c", cedula).setMaxResults(1).getResultList();
            if (!pacientes.isEmpty()) {
                return "{\"nombre\": \"" + pacientes.get(0).getNombres() + " " + pacientes.get(0).getApellidos() + "\"}";
            }
            // Check past facturas
            List<com.nurselogic.model.Factura> facturas = em.createQuery("SELECT f FROM Factura f WHERE f.clienteCedula = :c ORDER BY f.fechaEmision DESC", com.nurselogic.model.Factura.class).setParameter("c", cedula).setMaxResults(1).getResultList();
            if (!facturas.isEmpty()) {
                return "{\"nombre\": \"" + facturas.get(0).getClienteNombre() + "\"}";
            }
        } catch (Exception e) { e.printStackTrace(); }
        return "{}";
    }
'''
if 'buscarClientePorCedula' not in c:
    c = c.replace('public ActionResult procesarVentaCarrito', func + '\n    public ActionResult procesarVentaCarrito')
    with io.open('src/main/java/com/nurselogic/service/AdminService.java', 'w', encoding='utf-8') as f:
        f.write(c)

# Update AdminActionServlet.java to handle action=buscarClienteCedula
with io.open('src/main/java/com/nurselogic/controller/AdminActionServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

servlet_block = '''              } else if ("buscarClienteCedula".equals(action)) {
                  String json = adminService.buscarClientePorCedula(request.getParameter("cedula"));
                  response.setContentType("application/json");
                  response.setCharacterEncoding("UTF-8");
                  response.getWriter().write(json);
                  return;
              } else if ("facturarCarrito".equals(action)) {'''

if 'buscarClienteCedula' not in c:
    c = c.replace('} else if ("facturarCarrito".equals(action)) {', servlet_block)
    with io.open('src/main/java/com/nurselogic/controller/AdminActionServlet.java', 'w', encoding='utf-8') as f:
        f.write(c)

print('Updated AdminService and AdminActionServlet for buscarClienteCedula')
