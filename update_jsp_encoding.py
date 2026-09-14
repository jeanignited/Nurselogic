import os
import glob
import io

jsp_files = ['src/main/webapp/index.jsp', 'src/main/webapp/login.jsp', 'src/main/webapp/views/dashboard.jsp', 'src/main/webapp/views/pacientes.jsp', 'src/main/webapp/includes/modals.jsp']

directive = '<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>\n'

for path in jsp_files:
    if os.path.exists(path):
        with io.open(path, 'r', encoding='utf-8') as f:
            c = f.read()
            
        if 'pageEncoding="UTF-8"' not in c:
            if c.startswith('<%@ page'):
                import re
                c = re.sub(r'^<%@ page[^>]*>\n?', directive, c)
            else:
                c = directive + c
                
            with io.open(path, 'w', encoding='utf-8') as f:
                f.write(c)
            print("Updated", path)
