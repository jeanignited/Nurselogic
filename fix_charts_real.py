import io, re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the chart logic dynamically using regex to ignore spaces and newlines
pattern = r'int medGen = 0, ped = 0, card = 0, gin = 0, der = 0, otraEsp = 0;.*?else citPend\+\+;\s*\}\s*\}'
new_logic = '''
                java.util.Map<String, Integer> espCounts = new java.util.HashMap<>();
                List<Map<String, String>> usuariosGraf = (List<Map<String, String>>) request.getAttribute("listaUsuarios");
                if (usuariosGraf != null) {
                    for (Map<String, String> ug : usuariosGraf) {
                        String rol = ug.get("rol");
                        if ("Administrador".equalsIgnoreCase(rol) || "Paciente".equalsIgnoreCase(rol)) continue;
                        
                        String esp = ug.get("especialidad");
                        if (esp == null || esp.trim().isEmpty() || "N/A".equalsIgnoreCase(esp) || "Ninguna".equalsIgnoreCase(esp)) {
                            esp = rol; // Fallback al rol si no tiene especialidad
                        }
                        
                        espCounts.put(esp, espCounts.getOrDefault(esp, 0) + 1);
                    }
                }
                
                StringBuilder espLabels = new StringBuilder();
                StringBuilder espData = new StringBuilder();
                for (java.util.Map.Entry<String, Integer> entry : espCounts.entrySet()) {
                    if (espLabels.length() > 0) { espLabels.append(","); espData.append(","); }
                    espLabels.append("'").append(entry.getKey().replace("'", "\\\\'")).append("'");
                    espData.append(entry.getValue());
                }

                List<Map<String, String>> citasGraf = (List<Map<String, String>>) request.getAttribute("listaCitas");
                int citPend = 0, citAtend = 0, citSala = 0, citCanc = 0;
                if (citasGraf != null) {
                    for (Map<String, String> cg : citasGraf) {
                        String est = cg.get("estado");
                        if ("ATENDIDO".equalsIgnoreCase(est)) citAtend++;
                        else if ("CANCELADA".equalsIgnoreCase(est)) citCanc++;
                        else if ("SALA_ESPERA".equalsIgnoreCase(est) || "SALA ESPERA".equalsIgnoreCase(est) || "EN SALA".equalsIgnoreCase(est)) citSala++;
                        else citPend++;
                    }
                }
'''

c = re.sub(pattern, new_logic, c, flags=re.DOTALL)

# Replace the chart init
pattern_chart = r"chartEspInst = new Chart\(ctxEsp, \{.*?data: \[<%= medGen %>, <%= ped %>, <%= card %>, <%= gin %>, <%= der %>, <%= otraEsp %>\],.*?\}\s*\}\s*\}\s*\}\);"
new_chart = '''chartEspInst = new Chart(ctxEsp, {
                type: 'pie',
                data: {
                    labels: [<%= espLabels.toString() %>],
                    datasets: [{
                        data: [<%= espData.toString() %>],
                        backgroundColor: ['#38bdf8', '#34d399', '#f87171', '#fbbf24', '#c084fc', '#94a3b8', '#f472b6', '#2dd4bf', '#a3e635', '#a78bfa'],
                        borderWidth: 1,
                        borderColor: '#0f172a'
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { position: 'bottom', labels: { color: txtCol } } }
                }
            });'''

c = re.sub(pattern_chart, new_chart, c, flags=re.DOTALL)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated charts for real this time")
