package com.nurselogic.model;

import jakarta.persistence.*;

@Entity
@Table(name = "roles")
public class Rol {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "nombre", unique = true)
    private String nombre;

    @Column(name = "descripcion")
    private String descripcion;

    /** Campo legacy CSV — se mantiene por compatibilidad con el código existente. */
    @Column(name = "permisos", length = 500)
    private String permisos;

    // ── Nuevos permisos granulares (columnas booleanas) ──────────────────────
    @Column(name = "perm_hospitalizacion_camas")
    private boolean permHospitalizacionCamas;

    @Column(name = "perm_reporte_ventas")
    private boolean permReporteVentas;

    @Column(name = "perm_directorio_pacientes")
    private boolean permDirectorioPacientes;

    @Column(name = "perm_catalogos_clinicos")
    private boolean permCatalogosPersonal;

    @Column(name = "perm_soporte_ti")
    private boolean permSoporteTI;
    // ─────────────────────────────────────────────────────────────────────────

    public Rol() {}

    public Rol(String nombre, String descripcion) {
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.permisos = "";
    }

    public Rol(String nombre, String descripcion, String permisos) {
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.permisos = permisos;
    }

    // ── Getters / Setters existentes ─────────────────────────────────────────
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }

    public String getDescripcion() { return descripcion; }
    public void setDescripcion(String descripcion) { this.descripcion = descripcion; }

    public String getPermisos() { return permisos; }
    public void setPermisos(String permisos) { this.permisos = permisos; }

    // ── Getters / Setters nuevos ─────────────────────────────────────────────
    public boolean isPermHospitalizacionCamas() { return permHospitalizacionCamas; }
    public void setPermHospitalizacionCamas(boolean v) { this.permHospitalizacionCamas = v; }

    public boolean isPermReporteVentas() { return permReporteVentas; }
    public void setPermReporteVentas(boolean v) { this.permReporteVentas = v; }

    public boolean isPermDirectorioPacientes() { return permDirectorioPacientes; }
    public void setPermDirectorioPacientes(boolean v) { this.permDirectorioPacientes = v; }

    public boolean isPermCatalogosPersonal() { return permCatalogosPersonal; }
    public void setPermCatalogosPersonal(boolean v) { this.permCatalogosPersonal = v; }

    public boolean isPermSoporteTI() { return permSoporteTI; }
    public void setPermSoporteTI(boolean v) { this.permSoporteTI = v; }
}