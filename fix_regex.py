# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

import re
pattern = r'(<option value="1">1 - Sin respuesta</option>\s*</select>\s*</div>\s*</div>)(\s*</div>\s*<!-- Tab Diagnostico y Receta -->)'
c = re.sub(pattern, r'\1\n                      </div>\2', c)

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
