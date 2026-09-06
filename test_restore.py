import os

with open('full_index.jsp', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_modal = -1
end_modal = -1
for i, line in enumerate(lines):
    if '<!-- Modales y UI Components -->' in line or '<!-- Modales Globales -->' in line or '<jsp:include page="includes/modals.jsp" />' in line:
        start_modal = i
    if '<script src="https://cdn.jsdelivr.net/npm/bootstrap' in line or '<script>' in line or '<jsp:include page="includes/scripts.jsp" />' in line:
        end_modal = i
        break

print(f'Start: {start_modal}, End: {end_modal}')
