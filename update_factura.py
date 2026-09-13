import io
with io.open('src/main/java/com/nurselogic/model/Factura.java', 'r', encoding='utf-8') as f:
    c = f.read()

# Add cliente_cedula
c = c.replace('private String clienteNombre;', 'private String clienteNombre;\n\n    @Column(name = "cliente_cedula", length = 20)\n    private String clienteCedula;')
c = c.replace('public void setClienteNombre(String clienteNombre) { this.clienteNombre = clienteNombre; }', 'public void setClienteNombre(String clienteNombre) { this.clienteNombre = clienteNombre; }\n    public String getClienteCedula() { return clienteCedula; }\n    public void setClienteCedula(String clienteCedula) { this.clienteCedula = clienteCedula; }')

with io.open('src/main/java/com/nurselogic/model/Factura.java', 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated Factura.java')
