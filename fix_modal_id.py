import io, re

with io.open('src/main/webapp/includes/modals.jsp', 'rb') as f:
    c = f.read()

# Replace any modalA...Cama with modalAnadirCama
c = re.sub(b'id="modalA[^\x00-\x7F]*adirCama"', b'id="modalAnadirCama"', c)

with io.open('src/main/webapp/includes/modals.jsp', 'wb') as f:
    f.write(c)

with io.open('src/main/webapp/includes/scripts.jsp', 'rb') as f:
    s = f.read()

s = re.sub(b'getElementById\("modalA[^\x00-\x7F]*adirCama"\)', b'getElementById("modalAnadirCama")', s)
# Fix reload issue
s = s.replace(b'window.location.reload();', b'window.location.href = "dashboard";')

with io.open('src/main/webapp/includes/scripts.jsp', 'wb') as f:
    f.write(s)

print("Fixed modal ID and reload issue")
