import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class TestSyntax {
    public static void main(String[] args) {
        try {
            String js = new String(Files.readAllBytes(Paths.get("test_syntax.js")));
            ScriptEngine engine = new ScriptEngineManager().getEngineByName("nashorn");
            if (engine == null) {
                System.out.println("Nashorn engine not found.");
                return;
            }
            engine.eval(js);
            System.out.println("No syntax errors found.");
        } catch (ScriptException e) {
            System.out.println("Syntax Error: " + e.getMessage());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}