import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

resultados_empty = '''<tr>
                                    <td colspan="4" class="text-center py-5 text-muted">No hay resultados registrados.</td>
                                </tr>'''

resultados_fake = '''<tr>
                                    <td class="py-3 px-4"><i class="bi bi-calendar me-2 text-muted"></i>2026-09-12</td>
                                    <td class="py-3 px-4">Hemograma Completo</td>
                                    <td class="py-3 px-4"><i class="bi bi-person-badge me-2 text-muted"></i>Dr. Carlos M.</td>
                                    <td class="py-3 px-4 text-center">
                                        <button class="btn btn-sm btn-outline-primary rounded-pill px-3"><i class="bi bi-file-earmark-pdf me-2"></i>Ver PDF</button>
                                    </td>
                                </tr>'''
c = c.replace(resultados_empty, resultados_fake)

recetas_empty = '''<tr>
                                    <td colspan="4" class="text-center py-5 text-muted">No hay recetas m&eacute;dicas registradas.</td>
                                </tr>'''

recetas_fake = '''<tr>
                                    <td class="py-3 px-4"><i class="bi bi-calendar me-2 text-muted"></i>2026-09-10</td>
                                    <td class="py-3 px-4">Faringitis Aguda</td>
                                    <td class="py-3 px-4"><i class="bi bi-person-badge me-2 text-muted"></i>Dra. Ana V.</td>
                                    <td class="py-3 px-4 text-center">
                                        <button class="btn btn-sm btn-outline-success rounded-pill px-3"><i class="bi bi-capsule me-2"></i>Ver Receta</button>
                                    </td>
                                </tr>'''
c = c.replace(recetas_empty, recetas_fake)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fake rows added for buttons.")
