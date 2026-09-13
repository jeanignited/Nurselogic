import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Fix double <script> opening tag
c = c.replace('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>\n<script>\n<script>', '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>\n<script>')
# Sometimes it's without \n, let's just do regex
c = re.sub(r'<script>\s*<script>', '<script>', c)

# Fix imprimirFactura
c = c.replace('w.document.write(\'</div><script>window.print();</body></html>\');', 'w.document.write(\'</div><script>window.print();</script></body></html>\');')

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
print('Fixed script tags')
