import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_java = '''                List<Map<String, String>> medsGraf = (List<Map<String, String>>) request.getAttribute("listaMedicamentos");

                if (medsGraf != null) {

                    int countM = 0;

                    for (Map<String, String> mg : medsGraf) {

                        if (countM++ >= 5) break;

                        nomMeds.add("\\"" + mg.get("nombre").replace("\\"", "") + "\\"");

                        try { stkMeds.add(Integer.parseInt(mg.get("stock"))); } catch(Exception ex) { stkMeds.add(0); }

                    }

                }'''

new_java = '''                List<Map<String, String>> medsGraf = (List<Map<String, String>>) request.getAttribute("listaMedicamentos");
                if (medsGraf != null) {
                    List<Map<String, String>> sortedMeds = new java.util.ArrayList<>(medsGraf);
                    sortedMeds.sort((m1, m2) -> {
                        int s1 = 0, s2 = 0;
                        try { s1 = Integer.parseInt(m1.get("stock")); } catch(Exception e) {}
                        try { s2 = Integer.parseInt(m2.get("stock")); } catch(Exception e) {}
                        return Integer.compare(s2, s1); // descending
                    });
                    int countM = 0;
                    for (Map<String, String> mg : sortedMeds) {
                        if (countM++ >= 7) break;
                        nomMeds.add("\\"" + mg.get("nombre").replace("\\"", "") + "\\"");
                        try { stkMeds.add(Integer.parseInt(mg.get("stock"))); } catch(Exception ex) { stkMeds.add(0); }
                    }
                }'''

# Since spacing might vary, I'll use regex or simple replace
c = c.replace(old_java.replace('\n', ''), new_java) 
# wait, replacing newlines might fail. Let's do it smarter.
