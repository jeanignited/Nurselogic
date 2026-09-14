import io
with io.open('src/main/java/com/nurselogic/controller/RegistroServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {\n        String',
              'protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {\n        request.setCharacterEncoding("UTF-8");\n        String')

with io.open('src/main/java/com/nurselogic/controller/RegistroServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)
