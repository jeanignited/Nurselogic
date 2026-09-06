package com.nurselogic.model;

import jakarta.persistence.*;

@Entity
@Table(name = "camas")
public class Cama {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "numero")
    private String numero;

    @Column(name = "sala")
    private String sala;

    @Column(name = "estado")
    private String estado; // Disponible, Ocupada, Mantenimiento

    @Column(name = "paciente_nombre")
    private String pacienteNombre;

    @Column(name = "medico_nombre")
    private String medicoNombre;

    @Column(name = "motivo")
    private String motivo;

    public Cama() {}

    public Cama(String numero, String sala, String estado) {
        this.numero = numero;
        this.sala = sala;
        this.estado = estado;
        this.pacienteNombre = "";
        this.medicoNombre = "";
        this.motivo = "";
    }

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getNumero() { return numero; }
    public void setNumero(String numero) { this.numero = numero; }

    public String getSala() { return sala; }
    public void setSala(String sala) { this.sala = sala; }

    public String getEstado() { return estado; }
    public void setEstado(String estado) { this.estado = estado; }

    public String getPacienteNombre() { return pacienteNombre; }
    public void setPacienteNombre(String pacienteNombre) { this.pacienteNombre = pacienteNombre; }

    public String getMedicoNombre() { return medicoNombre; }
    public void setMedicoNombre(String medicoNombre) { this.medicoNombre = medicoNombre; }

    public String getMotivo() { return motivo; }
    public void setMotivo(String motivo) { this.motivo = motivo; }
}
