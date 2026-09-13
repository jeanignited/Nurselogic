import io
with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

# I need to remove the hanging try { or close it properly.
# Let's just remove the hanging 	ry {
c = c.replace('    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {\n        try {\n            String tipo = request.getParameter("tipo");', '    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {\n        String tipo = request.getParameter("tipo");')

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed ExportServlet.java syntax error')
