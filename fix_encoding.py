import os, re
servlets = ['CamasActionServlet.java', 'CitaServlet.java', 'DashboardServlet.java', 'LoginServlet.java', 'RecuperacionServlet.java', 'RegistroServlet.java']
for f in servlets:
    path = 'src/main/java/com/nurselogic/controller/' + f
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    content = re.sub(r'(protected void doPost.*?\{)', r'\1\n        request.setCharacterEncoding("UTF-8");', content)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
