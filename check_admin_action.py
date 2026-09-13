import io

with io.open('src/main/java/com/nurselogic/controller/AdminActionServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

# I need to change facturarCarrito to return JSON with the ID!
# But wait! Does AdminService.procesarVentaCarrito return the ID?
