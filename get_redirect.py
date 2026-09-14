import io
import re
with io.open('src/main/java/com/nurselogic/controller/AdminActionServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'if \(result \!= null\) \{.*', c, re.DOTALL)
if m: print(m.group(0)[:500])
