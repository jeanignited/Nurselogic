package com.nurselogic.model;

import jakarta.persistence.*;

@Entity
@Table(name = "alergias")
public class Alergia {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "nombre")
    private String nombre;

    @Column(name = "nivelGravedad")
    private String nivelGravedad;

    public Alergia() {}
    
    public Alergia(String nombre, String nivelGravedad) {
        this.nombre = nombre;
        this.nivelGravedad = nivelGravedad;
    }

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }

    public String getNivelGravedad() { return nivelGravedad; }
    public void setNivelGravedad(String nivelGravedad) { this.nivelGravedad = nivelGravedad; }
}
