import io

with io.open('src/main/webapp/includes/topbar.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_logic = '''<%

                       String nombreTop = (String) session.getAttribute("nombres");

                       if(nombreTop == null || nombreTop.trim().isEmpty() || nombreTop.contains("null")) {

                           nombreTop = "Usuario del Sistema";

                       }

                    %>'''

new_logic = '''<%
                       String pNombres = (String) session.getAttribute("nombres");
                       String pApellidos = (String) session.getAttribute("apellidos");
                       String nombreTop = "";
                       if (pNombres != null && !pNombres.trim().isEmpty() && !pNombres.contains("null")) {
                           nombreTop += pNombres.trim();
                       }
                       if (pApellidos != null && !pApellidos.trim().isEmpty() && !pApellidos.contains("null")) {
                           nombreTop += (nombreTop.isEmpty() ? "" : " ") + pApellidos.trim();
                       }
                       if (nombreTop.isEmpty()) {
                           nombreTop = "Usuario del Sistema";
                       }
                    %>'''

# There is a lot of whitespace in topbar.jsp, better to replace using regex.
import re
c = re.sub(r'<%[\s]*String nombreTop = \(String\) session\.getAttribute\("nombres"\);[\s]*if\(nombreTop == null \|\| nombreTop\.trim\(\)\.isEmpty\(\) \|\| nombreTop\.contains\("null"\)\) \{[\s]*nombreTop = "Usuario del Sistema";[\s]*\}[\s]*%>', new_logic, c, flags=re.DOTALL)

with io.open('src/main/webapp/includes/topbar.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated topbar.jsp")
