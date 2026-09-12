import io
with io.open('src/main/webapp/includes/modals.jsp', 'rb') as f:
    c = f.read()

words = [b'Cdula', b'Evaluacin', b'Clnica', b'ltima', b'Antropomtrica', b'Observacin', b'aos']
for w in words:
    if w in c: print(f"Found {w}")
