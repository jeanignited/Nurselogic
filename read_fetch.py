import io
import re
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r"if \(cb\) cb\.addEventListener\('keyup', function\(\) \{.*?(?=window\.atenderCita = function)", c, re.DOTALL)
if m:
    print(m.group(0))
else:
    print("not found")
