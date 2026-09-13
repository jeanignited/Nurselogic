import io
import re

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

client_inputs = '''        <div class="modal-body pb-0">
          <div class="row mb-3 px-2">
              <div class="col-md-5">
                  <label class="form-label text-secondary small mb-1">C\xe9dula del Cliente</label>
                  <div class="input-group input-group-sm">
                      <span class="input-group-text bg-transparent text-secondary border-secondary"><i class="bi bi-person-badge"></i></span>
                      <input type="text" id="ventaCedulaCarrito" class="form-control bg-transparent text-white border-secondary" placeholder="10 d\xedgitos..." maxlength="10" oninput="buscarClienteCarrito(this.value)">
                  </div>
              </div>
              <div class="col-md-7">
                  <label class="form-label text-secondary small mb-1">Nombre del Cliente</label>
                  <input type="text" id="ventaClienteCarrito" class="form-control form-control-sm bg-transparent text-white border-secondary" placeholder="Consumidor Final" oninput="if(this.value.trim() !== '') { this.classList.add('fw-bold', 'text-info'); } else { this.classList.remove('fw-bold', 'text-info'); }">
              </div>
          </div>
          <div class="table-responsive">'''

c = c.replace('<div class="modal-body pb-0">\n          <div class="table-responsive">', client_inputs)

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Added client inputs to modalCarrito')
