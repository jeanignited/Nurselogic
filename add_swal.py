import io

with io.open('src/main/webapp/index.jsp', 'r', encoding='windows-1252', errors='ignore') as f:
    c = f.read()

# Insert SweetAlert2 in head
swal_link = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.min.css">\\n    <style>'
c = c.replace('<style>', swal_link)

# Insert SweetAlert2 JS before scripts.jsp
swal_script = '<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11/dist/sweetalert2.all.min.js"></script>\\n<jsp:include page="includes/scripts.jsp" />'
c = c.replace('<jsp:include page="includes/scripts.jsp" />', swal_script)

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Added SweetAlert2 to index.jsp")
