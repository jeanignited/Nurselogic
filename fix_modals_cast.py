import io, re
with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='windows-1252') as f:
    c = f.read()

# Replace:
# List<Map<String, String>> espList = (List<Map<String, String>>) request.getAttribute("listaEspecialidades");
# With:
# List<Map<String, String>> espList = (List<Map<String, String>>) request.getAttribute("listaEspecialidadesMap");

c = c.replace('request.getAttribute("listaEspecialidades");\\n                    if (espList != null', 'request.getAttribute("listaEspecialidadesMap");\\n                    if (espList != null')

# Just to be safe, do a regex replace if the exact string matching fails
c = re.sub(r'List<Map<String, String>>\s*espList\s*=\s*\(List<Map<String, String>>\)\s*request\.getAttribute\("listaEspecialidades"\);',
           'List<Map<String, String>> espList = (List<Map<String, String>>) request.getAttribute("listaEspecialidadesMap");', c)

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='windows-1252') as f:
    f.write(c)
