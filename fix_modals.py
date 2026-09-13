import io

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Remove the broken first few lines
while lines and (lines[0].strip().startswith('<%@ page') or lines[0].strip() == '' or '\xef\xbb\xbf' in lines[0] or '' in lines[0]):
    lines.pop(0)

# Prepend a clean directive
new_content = '<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>\n' + ''.join(lines)

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("modals.jsp fixed.")
