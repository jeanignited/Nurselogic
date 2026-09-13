# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

print("Occurrences of cleanDiag:", c.count("cleanDiag"))
print("Occurrences of formattedDiag:", c.count("formattedDiag"))
