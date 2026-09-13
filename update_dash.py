import io

with io.open('src/main/java/com/nurselogic/controller/DashboardServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

old_loop = '''                    map.put("diagnostico", c.getDiagnostico() != null ? c.getDiagnostico().replace("'", "\\\\'").replace("\\n", " ") : "No registrado");
                    map.put("receta", c.getReceta() != null ? c.getReceta().replace("'", "\\\\'").replace("\\n", " ") : "Ninguna");
                    listaCitas.add(map);'''

new_loop = '''                    map.put("diagnostico", c.getDiagnostico() != null ? c.getDiagnostico().replace("'", "\\\\'").replace("\\n", " ") : "No registrado");
                    
                    com.nurselogic.dao.CitaDAO citaDAO = new com.nurselogic.dao.CitaDAO();
                    String unificada = citaDAO.obtenerRecetaUnificada(c.getId(), c.getReceta());
                    map.put("receta", unificada.replace("'", "\\\\'").replace("\\n", " "));
                    
                    listaCitas.add(map);'''

if old_loop in c:
    c = c.replace(old_loop, new_loop)
else:
    print("WARNING: old_loop not found")

old_set_attrs = '''            request.setAttribute("listaCitas", listaCitas);


            // Lista de Facturas'''

new_set_attrs = '''            request.setAttribute("listaCitas", listaCitas);

            List<Map<String, String>> listaRecetas = new ArrayList<>();
            List<Map<String, String>> listaResultados = new ArrayList<>();
            for (Map<String, String> cMap : listaCitas) {
                if (cMap.get("receta") != null && !cMap.get("receta").equals("Ninguna")) {
                    listaRecetas.add(cMap);
                }
                if (cMap.get("diagnostico") != null && !cMap.get("diagnostico").equals("No registrado")) {
                    Map<String, String> res = new HashMap<>(cMap);
                    res.put("tipoExamen", "Consulta General");
                    listaResultados.add(res);
                }
            }
            request.setAttribute("listaRecetas", listaRecetas);
            request.setAttribute("listaResultados", listaResultados);

            // Lista de Facturas'''

if old_set_attrs in c:
    c = c.replace(old_set_attrs, new_set_attrs)
else:
    print("WARNING: old_set_attrs not found")

with io.open('src/main/java/com/nurselogic/controller/DashboardServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated DashboardServlet.java")
