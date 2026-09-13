import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

offset = c.find('Introduce tus datos')
if offset != -1:
    end_idx = c.find('</div>', offset)
    end_idx = c.find('</div>', end_idx+1)
    end_idx = c.find('</div>', end_idx+1)
    end_idx = c.find('</div>', end_idx+1)
    end_idx = c.find('</div>', end_idx+1) + 6

    # We need to find where the <div class="row g-4"> for these forms starts.
    # It is right after '<!-- Signos Vitales -->' block ends.
    start_offset = c.find('Mis Datos Cl&iacute;nicos')
    start_idx = c.find('<div class="row g-4">', start_offset)
    if start_idx != -1:
        # the first row g-4 is Datos Personales, the second is Signos Vitales, the third is Agendar Cita.
        start_idx = c.find('<div class="row g-4">', c.find('<!-- Signos Vitales -->'))
        # Actually, let's just find "Agendar Cita M&eacute;dica"
        agendar_str = c.find('Agendar Cita M')
        # find the <div class="row g-4"> before this
        start_idx = c.rfind('<div class="row g-4">', 0, agendar_str)
        print(c[start_idx:start_idx+100])
        print("...")
        print(c[end_idx-100:end_idx])

