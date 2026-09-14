import io

with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<textarea name="receta" id="recetaFinal" class="form-control" rows="3" placeholder="Medicamentos, dosis y recomendaciones..."></textarea>', '<textarea name="recetaCita" id="recetaFinal" class="form-control" rows="3" placeholder="Medicamentos, dosis y recomendaciones..."></textarea>')

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Changed textarea name")
