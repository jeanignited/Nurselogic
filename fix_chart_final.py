import io
import re

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace the medsGraf scriptlet with the sorted top-7 version wrapped in try-catch
old_code = r'List<Map<String, String>> medsGraf = \(List<Map<String, String>>\) request\.getAttribute\("listaMedicamentos"\);\s*if \(medsGraf != null\) \{\s*int countM = 0;\s*for \(Map<String, String> mg : medsGraf\) \{\s*if \(countM\+\+ >= 5\) break;\s*nomMeds\.add\("\\\"" \+ mg\.get\("nombre"\)\.replace\("\\\"", ""\) \+ "\\\""\);\s*try \{ stkMeds\.add\(Integer\.parseInt\(mg\.get\("stock"\)\)\); \} catch\(Exception ex\) \{ stkMeds\.add\(0\); \}\s*\}\s*\}'

new_code = '''try {
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
                } catch(Exception bigEx) {}'''

c = re.sub(old_code, new_code, c)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Fixed meds chart")
