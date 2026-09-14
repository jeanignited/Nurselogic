import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'function evaluarVitales\(\) \{.*?(?=let grabador;)', c, re.DOTALL)
if m:
    old_evaluar = m.group(0)
    new_evaluar = '''function evaluarVitales() {
    let inputs = [
        { id: 'fc_input',   badge: 'fc_badge',   parse: parseInt,   eval: v => v < 60 ? ["Bradicardia", "bg-warning text-dark"] : v > 100 ? ["Taquicardia", "bg-danger"] : ["Normal", "bg-success"] },
        { id: 'fr_input',   badge: 'fr_badge',   parse: parseInt,   eval: v => v < 12 ? ["Bradipnea",   "bg-warning text-dark"] : v > 20  ? ["Taquipnea",   "bg-danger"] : ["Normal", "bg-success"] },
        { id: 'sat_input',  badge: 'sat_badge',  parse: parseInt,   eval: v => v < 90 ? ["Hipoxia Severa", "bg-danger"] : v < 95 ? ["Hipoxia Leve", "bg-warning text-dark"] : ["Normal", "bg-success"] },
        { id: 'temp_input', badge: 'temp_badge', parse: parseFloat, eval: v => v < 36.5 ? ["Hipotermia", "bg-info text-dark"] : v > 37.5 ? ["Fiebre", "bg-danger"] : ["Normal", "bg-success"] }
    ];

    let prefixes = ['', 'atender_'];

    prefixes.forEach(prefix => {
        inputs.forEach(item => {
            try {
                let el = document.getElementById(prefix + item.id);
                let b  = document.getElementById(prefix + item.badge);
                if (!el || !b) return;
                if (!el.value || el.value.trim() === '') {
                    b.innerText   = 'Esperando...';
                    b.className   = 'badge mt-1 w-100 p-2 text-wrap bg-secondary';
                    return;
                }
                let num = item.parse(el.value);
                if (!isNaN(num)) {
                    let res = item.eval(num);
                    b.innerText   = res[0];
                    b.className   = 'badge mt-1 w-100 p-2 text-wrap ' + res[1];
                }
            } catch(e) {}
        });

        // Presi\u00F3n Arterial
        try {
            let pa   = document.getElementById(prefix + 'pa_input');
            let pa_b = document.getElementById(prefix + 'pa_badge');
            if (!pa || !pa_b) return;
            if (!pa.value || pa.value.trim() === '') {
                pa_b.innerText = 'Esperando...';
                pa_b.className = 'badge mt-1 w-100 p-2 text-wrap bg-secondary';
            } else if (pa.value.includes('/')) {
                let sist = parseInt(pa.value.split('/')[0]);
                if (!isNaN(sist)) {
                    let res = sist < 90 ? ["Hipotensi\u00F3n", "bg-warning text-dark"] : sist > 140 ? ["Hipertensi\u00F3n", "bg-danger"] : ["Normal", "bg-success"];
                    pa_b.innerText = res[0];
                    pa_b.className = 'badge mt-1 w-100 p-2 text-wrap ' + res[1];
                }
            }
        } catch(e) {}
    });
}

'''
    c = c.replace(old_evaluar, new_evaluar)
    with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Replaced evaluarVitales successfully")
else:
    print("evaluarVitales not found")
