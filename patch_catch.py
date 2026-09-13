import io
import re

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'r', encoding='utf-8') as f:
    c = f.read()

# Instead of throwing, catch Exception and print it directly to out!
old_catch = '''        } catch(Exception e) {
            response.setContentType("text/plain");
            e.printStackTrace(response.getWriter());
        }'''

new_catch = '''        } catch(Exception e) {
            response.getWriter().println("EXCEPTION: " + e.getMessage());
            for (StackTraceElement el : e.getStackTrace()) {
                response.getWriter().println(el.toString());
            }
        }'''

c = c.replace(old_catch, new_catch)

with io.open('src/main/java/com/nurselogic/controller/ExportServlet.java', 'w', encoding='utf-8') as f:
    f.write(c)

print('Patched catch block')
