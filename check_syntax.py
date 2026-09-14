import io
import re

with io.open('src/main/java/com/nurselogic/controller/CitaServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'request\.getRequestDispatcher\("/dashboard"\)\.forward\(request, response\); else \{', c)
if m: print("Found syntax error!")
else: print("No syntax error found")
