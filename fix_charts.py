# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

old_logic = '''            <%
                int medGen = 0, ped = 0, card = 0, gin = 0, der = 0, otraEsp = 0;
                List<Map<String, String>> citasGraf = (List<Map<String, String>>) request.getAttribute("listaCitas");
                int citPend = 0, citAtend = 0, citSala = 0, citCanc = 0;
                if (citasGraf != null) {
                    for (Map<String, String> cg : citasGraf) {
                        String esp = cg.get("especialidad");
                        if (esp != null) {
                            if (esp.toLowerCase().contains("general")) medGen++;
                            else if (esp.toLowerCase().contains("pedi")) ped++;
                            else if (esp.toLowerCase().contains("cardio")) card++;
                            else if (esp.toLowerCase().contains("gineco")) gin++;
                            else if (esp.toLowerCase().contains("dermato")) der++;
                            else otraEsp++;
                        }
                        String est = cg.get("estado");
                        if ("ATENDIDO".equalsIgnoreCase(est)) citAtend++;
                        else if ("CANCELADA".equalsIgnoreCase(est)) citCanc++;
                        else if ("SALA_ESPERA".equalsIgnoreCase(est) || "SALA ESPERA".equalsIgnoreCase(est)) citSala++;
                        else citPend++;
                    }
                }
            %>'''

new_logic = '''            <%
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
                        else if ("SALA_ESPERA".equalsIgnoreCase(est) || "SALA ESPERA".equalsIgnoreCase(est)) citSala++;
                        else citPend++;
                    }
                }
            %>'''

c = c.replace(old_logic, new_logic)

old_chart = '''            new Chart(ctxEsp, {
                type: 'pie',
                data: {
                    labels: ['Medicina General', 'Pediatr\xeda', 'Cardiolog\xeda', 'Ginecolog\xeda', 'Dermatolog\xeda', 'Otras'],
                    datasets: [{
                        data: [<%= medGen %>, <%= ped %>, <%= card %>, <%= gin %>, <%= der %>, <%= otraEsp %>],
                        backgroundColor: ['#38bdf8', '#34d399', '#f43f5e', '#a78bfa', '#fbbf24', '#9ca3af'],
                        borderWidth: 0
                    }]
                },
                options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'bottom', labels: { color: 'var(--text-color)' } } } }
            });'''

new_chart = '''            new Chart(ctxEsp, {
                type: 'pie',
                data: {
                    labels: [<%= espLabels.toString() %>],
                    datasets: [{
                        data: [<%= espData.toString() %>],
                        backgroundColor: ['#38bdf8', '#34d399', '#f43f5e', '#a78bfa', '#fbbf24', '#9ca3af', '#f472b6', '#2dd4bf', '#a3e635', '#c084fc'],
                        borderWidth: 0
                    }]
                },
                options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'bottom', labels: { color: 'var(--text-color)' } } } }
            });'''

c = c.replace(old_chart, new_chart)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated charts")
