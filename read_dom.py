import io
with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()
in_dom = False
for i, line in enumerate(lines):
    if "document.addEventListener('DOMContentLoaded'" in line:
        in_dom = True
    if in_dom:
        if "function openAtencion" in line:
            break
        print(line.rstrip())
