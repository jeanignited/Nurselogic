import javax.script.ScriptEngineManager;
import javax.script.ScriptEngine;
import java.nio.file.Files;
import java.nio.file.Paths;

public class JSTester {
    public static void main(String[] args) throws Exception {
        ScriptEngine engine = new ScriptEngineManager().getEngineByName("nashorn");
        if(engine == null) engine = new ScriptEngineManager().getEngineByName("JavaScript");
        String js = new String(Files.readAllBytes(Paths.get("debug_scripts.js")));
        try {
            engine.eval(js);
            System.out.println("Syntax is OK");
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
