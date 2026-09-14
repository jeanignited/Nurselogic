import io
with io.open('src/main/java/com/nurselogic/controller/PacienteServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {\n        try {',
              'protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {\n        request.setCharacterEncoding("UTF-8");\n        try {')

with io.open('src/main/java/com/nurselogic/controller/PacienteServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)
