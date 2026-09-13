import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_java = '''                List<Map<String, String>> medsGraf = (List<Map<String, String>>) request.getAttribute("listaMedicamentos");
                if (medsGraf != null) {
                    List<Map<String, String>> sortedMeds = new java.util.ArrayList<>(medsGraf);
                    java.util.Collections.sort(sortedMeds, new java.util.Comparator<Map<String, String>>() {
                        public int compare(Map<String, String> m1, Map<String, String> m2) {
                            int s1 = 0, s2 = 0;
                            try { s1 = Integer.parseInt(m1.get("stock")); } catch(Exception e) {}
                            try { s2 = Integer.parseInt(m2.get("stock")); } catch(Exception e) {}
                            return Integer.compare(s2, s1);
                        }
                    });
                    int countM = 0;
                    for (Map<String, String> mg : sortedMeds) {
                        if (countM++ >= 7) break;
                        nomMeds.add("\\"" + mg.get("nombre").replace("\\"", "") + "\\"");
                        try { stkMeds.add(Integer.parseInt(mg.get("stock"))); } catch(Exception ex) { stkMeds.add(0); }
                    }
                }'''

new_java = '''                try {
                    List<Map<String, String>> medsGraf = (List<Map<String, String>>) request.getAttribute("listaMedicamentos");
                    if (medsGraf != null) {
                        List<Map<String, String>> sortedMeds = new java.util.ArrayList<>(medsGraf);
                        java.util.Collections.sort(sortedMeds, new java.util.Comparator<Map<String, String>>() {
                            public int compare(Map<String, String> m1, Map<String, String> m2) {
                                int s1 = 0, s2 = 0;
                                try { s1 = Integer.parseInt(m1.get("stock")); } catch(Exception e) {}
                                try { s2 = Integer.parseInt(m2.get("stock")); } catch(Exception e) {}
                                return Integer.compare(s2, s1);
                            }
                        });
                        int countM = 0;
                        for (Map<String, String> mg : sortedMeds) {
                            if (countM++ >= 7) break;
                            String n = mg.get("nombre");
                            if (n == null) n = "Desconocido";
                            nomMeds.add("\\"" + n.replace("\\"", "") + "\\"");
                            try { stkMeds.add(Integer.parseInt(mg.get("stock"))); } catch(Exception ex) { stkMeds.add(0); }
                        }
                    }
                } catch(Exception bigEx) {
                    // Ignore so we don't break JS
                }'''

c = c.replace(old_java, new_java)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Wrapped in try-catch")
