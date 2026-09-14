import io
with io.open('src/main/webapp/includes/modals.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Update Ficha Medica Table to add IMC and Glasgow
old_table = '''<tr>
                        <td class="fw-bold text-secondary" style="width: 25%;"><i class="bi bi-person-bounding-box me-2 text-info"></i>Antropometr\u00EDa</td>
                        <td id="fichaEstPeso" class="fw-semibold text-light">-- / --</td>
                    </tr>'''

new_table = '''<tr>
                        <td class="fw-bold text-secondary" style="width: 25%;"><i class="bi bi-person-bounding-box me-2 text-info"></i>Antropometr\u00EDa</td>
                        <td class="fw-semibold text-light"><span id="fichaEstPeso">-- / --</span> <span id="fichaIMC" class="badge ms-2 bg-secondary">IMC: --</span></td>
                    </tr>
                    <tr>
                        <td class="fw-bold text-secondary"><i class="bi bi-eye text-primary me-2"></i>Escala Glasgow</td>
                        <td id="fichaGlasgow" class="fw-bold text-light">No se consider\u00F3 la evaluaci\u00F3n Glasgow</td>
                    </tr>'''
c = c.replace(old_table.encode('latin1').decode('utf-8', 'ignore'), new_table)
c = c.replace('Antropometra', 'Antropometr\u00EDa')

with io.open('src/main/webapp/includes/modals.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
