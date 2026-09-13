import io

with io.open('src/main/webapp/includes/scripts.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

old_java = '''                    sortedMeds.sort((m1, m2) -> {
                        int s1 = 0, s2 = 0;
                        try { s1 = Integer.parseInt(m1.get("stock")); } catch(Exception e) {}
                        try { s2 = Integer.parseInt(m2.get("stock")); } catch(Exception e) {}
                        return Integer.compare(s2, s1);
                    });'''

new_java = '''                    java.util.Collections.sort(sortedMeds, new java.util.Comparator<Map<String, String>>() {
                        public int compare(Map<String, String> m1, Map<String, String> m2) {
                            int s1 = 0, s2 = 0;
                            try { s1 = Integer.parseInt(m1.get("stock")); } catch(Exception e) {}
                            try { s2 = Integer.parseInt(m2.get("stock")); } catch(Exception e) {}
                            return Integer.compare(s2, s1);
                        }
                    });'''

c = c.replace(old_java, new_java)

with io.open('src/main/webapp/includes/scripts.jsp', 'w', encoding='utf-8') as f:
    f.write(c)

print("Replaced lambda with anonymous inner class")
