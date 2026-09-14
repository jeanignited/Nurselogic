import io
with io.open('src/main/java/com/nurselogic/controller/PacienteServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

new_parsing = '''            String sat = request.getParameter("sat");
            try { p.setSaturacionOxigeno(sat != null && !sat.trim().isEmpty() ? Integer.parseInt(sat.replaceAll("[^\\\\d]", "")) : 0); } catch (Exception e) { p.setSaturacionOxigeno(0); }

            String diag = request.getParameter("diagnosticoClinico");
            if (diag != null && !diag.trim().isEmpty()) {
                p.setDiagnosticoClinico(diag);
            }

            String glasgowStr = request.getParameter("glasgow");
            if (glasgowStr == null || glasgowStr.trim().isEmpty() || glasgowStr.equals("NA") || glasgowStr.equals("null")) {
                p.setGlasgow(null);
            } else {
                try {
                    p.setGlasgow(Integer.parseInt(glasgowStr));
                } catch (Exception e) {
                    p.setGlasgow(null);
                }
            }'''

c = c.replace('''            String sat = request.getParameter("sat");
            try { p.setSaturacionOxigeno(sat != null && !sat.trim().isEmpty() ? Integer.parseInt(sat.replaceAll("[^\\\\d]", "")) : 0); } catch (Exception e) { p.setSaturacionOxigeno(0); }''', new_parsing)

with io.open('src/main/java/com/nurselogic/controller/PacienteServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)
