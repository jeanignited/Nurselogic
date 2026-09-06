import os

with open('full_index.jsp', 'r', encoding='utf-16') as f:
    lines = f.readlines()

start_modal = -1
end_modal = -1
for i, line in enumerate(lines):
    if '<!-- Modales y UI Components -->' in line:
        start_modal = i
    if '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>' in line:
        end_modal = i - 1
        break

if start_modal != -1 and end_modal != -1:
    with open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
        f.writelines(lines[start_modal:end_modal+1])
    print('Restored modals.jsp from full_index.jsp')
else:
    print('Could not find modals section')
