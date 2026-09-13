import io
with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()
import re
print(re.findall(r'out\.println\("ID.*?"\);', c))
