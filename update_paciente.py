import io
with io.open('src/main/java/com/nurselogic/model/Paciente.java', 'r', encoding='utf-8') as f:
    c = f.read()

new_fields = '''    @Column(name = "saturacionOxigeno")
    private int saturacionOxigeno;

    @Column(name = "diagnosticoClinico", columnDefinition = "TEXT")
    private String diagnosticoClinico;

    @Column(name = "glasgow")
    private Integer glasgow;'''

c = c.replace('    @Column(name = "saturacionOxigeno")\n    private int saturacionOxigeno;', new_fields)

new_getters = '''    public void setSaturacionOxigeno(int saturacionOxigeno) { this.saturacionOxigeno = saturacionOxigeno; }

    public String getDiagnosticoClinico() { return diagnosticoClinico; }
    public void setDiagnosticoClinico(String diagnosticoClinico) { this.diagnosticoClinico = diagnosticoClinico; }

    public Integer getGlasgow() { return glasgow; }
    public void setGlasgow(Integer glasgow) { this.glasgow = glasgow; }
}'''

c = c.replace('    public void setSaturacionOxigeno(int saturacionOxigeno) { this.saturacionOxigeno = saturacionOxigeno; }\n}', new_getters)

with io.open('src/main/java/com/nurselogic/model/Paciente.java', 'w', encoding='utf-8') as f:
    f.write(c)
