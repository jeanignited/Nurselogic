# -*- coding: utf-8 -*-
import io
import re

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

# I will find the row containing Agendar Cita and IMC
# The block starts right after <% } %> of the miHC check
# Let's use substring replacement to be totally safe.

start_str = u'<div class="row g-4">\n\n                <div class="col-md-7">'
start_idx = c.find(start_str)

if start_idx == -1:
    # Try another way to find the block
    start_str = u'<div class="row g-4">'
    start_idx = c.find(start_str, c.find('Tus Datos'))

# Since I know the exact HTML of the block, I can use a Regex.
pattern = r'<div class="row g-4">.*?<!-- VISTA MIS CITAS PREVIAS -->'
# Wait, VISTA MIS CITAS PREVIAS is the next view. Let's make sure it exists and captures up to it.

