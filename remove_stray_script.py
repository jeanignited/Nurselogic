import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for idx, line in enumerate(lines):
    if idx == 3392 and line.strip() == '<script>': # 3393 is index 3392
        pass # Remove this line
    else:
        new_lines.append(line)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Removed stray <script> at line 3393')
