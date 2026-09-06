package com.nurselogic.model;

import jakarta.persistence.*;
import java.time.LocalDate;

@Entity
@Table(name = "pacientes")
public class Paciente {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "nombres")
    private String nombres;

    @Column(name = "apellidos")
    private String apellidos;

    @Column(name = "cedula")
    private String cedula;

    @Column(name = "fechaNacimiento")
    private LocalDate fechaNacimiento;

    @Column(name = "sexo")
    private String sexo;

    @Column(name = "estatura")
    private double estatura;

    @Column(name = "peso")
    private double peso;

    @Column(name = "enfermedadPreexistente")
    private String enfermedadPreexistente;

    @Column(name = "alergias")
    private String alergias;

    @Column(name = "temperatura")
    private double temperatura;

    @Column(name = "presionArterial")
    private String presionArterial;

    @Column(name = "frecuenciaCardiaca")
    private int frecuenciaCardiaca;

    @Column(name = "saturacionOxigeno")
    private int saturacionOxigeno;

    public Paciente() {}

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getNombres() { return nombres; }
    public void setNombres(String nombres) { this.nombres = nombres; }

    public String getApellidos() { return apellidos; }
    public void setApellidos(String apellidos) { this.apellidos = apellidos; }

    public String getCedula() { return cedula; }
    public void setCedula(String cedula) { this.cedula = cedula; }

    public LocalDate getFechaNacimiento() { return fechaNacimiento; }
    public void setFechaNacimiento(LocalDate fechaNacimiento) { this.fechaNacimiento = fechaNacimiento; }

    public String getSexo() { return sexo; }
    public void setSexo(String sexo) { this.sexo = sexo; }

    public double getEstatura() { return estatura; }
    public void setEstatura(double estatura) { this.estatura = estatura; }

    public double getPeso() { return peso; }
    public void setPeso(double peso) { this.peso = peso; }

    public String getEnfermedadPreexistente() { return enfermedadPreexistente; }
    public void setEnfermedadPreexistente(String enfermedadPreexistente) { this.enfermedadPreexistente = enfermedadPreexistente; }

    public String getAlergias() { return alergias; }
    public void setAlergias(String alergias) { this.alergias = alergias; }

    public double getTemperatura() { return temperatura; }
    public void setTemperatura(double temperatura) { this.temperatura = temperatura; }

    public String getPresionArterial() { return presionArterial; }
    public void setPresionArterial(String presionArterial) { this.presionArterial = presionArterial; }

    public int getFrecuenciaCardiaca() { return frecuenciaCardiaca; }
    public void setFrecuenciaCardiaca(int frecuenciaCardiaca) { this.frecuenciaCardiaca = frecuenciaCardiaca; }

    public int getSaturacionOxigeno() { return saturacionOxigeno; }
    public void setSaturacionOxigeno(int saturacionOxigeno) { this.saturacionOxigeno = saturacionOxigeno; }
}