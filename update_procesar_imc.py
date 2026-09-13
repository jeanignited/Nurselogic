import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_procesar = '''function procesarIMC(peso, estatura, valElem, estElem) {

            if(peso > 0 && estatura > 0) {

                let imc = peso / (estatura * estatura);

                valElem.innerText = imc.toFixed(1);

                estElem.className = 'badge px-4 py-2 rounded-pill fs-6 mt-2';



                if(imc < 18.5) { estElem.innerText = 'Bajo Peso'; estElem.classList.add('bg-warning', 'text-dark'); }

                else if(imc < 25) { estElem.innerText = 'Normal'; estElem.classList.add('bg-success'); }

                else if(imc < 30) { estElem.innerText = 'Sobrepeso'; estElem.classList.add('bg-warning', 'text-dark'); }

                else { estElem.innerText = 'Obesidad'; estElem.classList.add('bg-danger'); }

            } else {

                valElem.innerText = '0.0';

                estElem.innerText = 'Introduce tus datos';

                estElem.className = 'badge bg-secondary px-4 py-2 rounded-pill fs-6 mt-2';

            }

        }'''

new_procesar = '''function procesarIMC(peso, estatura, valElem, estElem) {
            if(peso > 0 && estatura > 0) {
                let imc = peso / (estatura * estatura);
                valElem.innerText = imc.toFixed(1);
                estElem.className = 'badge px-4 py-2 rounded-pill fs-6 mt-2';
                
                // Limpiar clases previas
                valElem.classList.remove('text-success', 'text-warning', 'text-danger', 'text-theme');

                if(imc < 18.5) { 
                    estElem.innerText = 'Bajo Peso'; 
                    estElem.classList.add('bg-warning', 'text-dark'); 
                    valElem.classList.add('text-warning');
                }
                else if(imc < 25) { 
                    estElem.innerText = 'Normal'; 
                    estElem.classList.add('bg-success'); 
                    valElem.classList.add('text-success');
                }
                else if(imc < 30) { 
                    estElem.innerText = 'Sobrepeso'; 
                    estElem.classList.add('bg-warning', 'text-dark'); 
                    valElem.classList.add('text-warning');
                }
                else { 
                    estElem.innerText = 'Obesidad'; 
                    estElem.classList.add('bg-danger'); 
                    valElem.classList.add('text-danger');
                }
            } else {
                valElem.innerText = '0.0';
                estElem.innerText = 'Introduce tus datos';
                estElem.className = 'badge bg-secondary px-4 py-2 rounded-pill fs-6 mt-2';
                
                valElem.classList.remove('text-success', 'text-warning', 'text-danger');
                valElem.classList.add('text-theme');
            }
        }'''

# Because of all the newlines, regex is better.
pattern = r'function procesarIMC\(peso, estatura, valElem, estElem\) \{[\s\S]*?\} else \{[\s\S]*?\}'
c = re.sub(pattern, new_procesar, c)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("scripts.jsp updated.")
