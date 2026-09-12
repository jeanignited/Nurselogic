import io

with io.open('src/main/webapp/index.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

css_rule = '''
        /* FORZAR TEXTOS BLANCOS A OSCUROS EN MODO CLARO */
        [data-bs-theme="light"] .text-white,
        [data-bs-theme="light"] .text-light,
        [data-bs-theme="light"] .text-white-50 {
            color: #212529 !important;
        }
        
        /* Opcional: si algo realmente debe quedarse blanco, aplicamos text-shadow */
        [data-bs-theme="light"] .btn.text-white {
            color: #fff !important; /* Los botones s pueden ser blancos */
        }
        [data-bs-theme="light"] .force-shadow-light {
            text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000 !important;
        }
'''

c = c.replace('</style>', css_rule + '    </style>')

with io.open('src/main/webapp/index.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

