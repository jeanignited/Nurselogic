import io
import re

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'<div class="modal fade" id="modalNuevaCitaAdmin".*?</form>', c, re.DOTALL)
if m: print(m.group(0))
