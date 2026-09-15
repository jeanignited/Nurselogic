import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    scripts = f.read()

# The incorrect replace that was done previously is:
# formData.append("idEnf", id);
# formData.append("idAle", id);

bad_pattern = r'formData\.append\("idEnf", id\);\s*formData\.append\("idAle", id\);'

scripts = re.sub(bad_pattern, 'formData.append("id", id);', scripts)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(scripts)
