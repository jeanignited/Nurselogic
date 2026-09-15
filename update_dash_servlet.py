import io

with io.open('src/main/java/com/nurselogic/controller/DashboardServlet.java', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('request.setAttribute("listaRoles", listaRoles);', 'request.setAttribute("listaRoles", listaRoles);\n                request.setAttribute("listaRolesObj", rList);')

with io.open('src/main/java/com/nurselogic/controller/DashboardServlet.java', 'w', encoding='utf-8') as f:
    f.write(code)
