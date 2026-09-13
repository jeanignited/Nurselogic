import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# I will find the end of the div of the row that contains 'Hora' and inject the new div before the submit button.
pattern = r'(<input type="time" name="hora"[^>]*>\s*</div>\s*</div>)\s*<button type="submit"'
replacement = r'\1\n\n                                <div class="p-3 mt-3 mb-3 rounded bg-dark border border-secondary text-muted small">\n                                    <i class="bi bi-info-circle text-primary me-2"></i><strong>Nota importante:</strong> Por favor, pres&eacute;ntate 15 minutos antes de tu consulta programada. En caso de presentar s&iacute;ntomas graves o emergencias, dir&iacute;gete inmediatamente a nuestra &aacute;rea de Urgencias y Triage.\n                                </div>\n\n                                <button type="submit"'

c = re.sub(pattern, replacement, c)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Info box injected.")
