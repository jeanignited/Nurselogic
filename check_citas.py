import io
import re

with io.open('src/main/java/com/nurselogic/controller/DashboardServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'listaCitas', c)
if m: print("Found listaCitas in DashboardServlet")
else: print("Not found listaCitas in DashboardServlet")
