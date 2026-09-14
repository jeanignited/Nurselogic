import io
with io.open('src/main/java/com/nurselogic/controller/DashboardServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()
with io.open('dash.txt', 'w', encoding='utf-8') as out:
    out.write(c)
