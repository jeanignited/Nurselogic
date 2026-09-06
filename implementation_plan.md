# Innovación: Módulo de Farmacia y Consulta Médica Avanzada

Este plan aborda las dos grandes mejoras solicitadas para completar la lista de cotejo de innovación.

## 1. Módulo de Despacho en Farmacia
**Objetivo:** Permitir al Farmacéutico buscar pacientes por cédula y visualizar sus recetas vigentes para proceder con la venta/entrega.

### Cambios Propuestos:
- **medicamentos.jsp:** Se añadirá una nueva sección superior llamada "Despacho de Recetas".
- Contendrá un buscador por cédula.
- **FarmaciaServlet.java (NUEVO) o Endpoint en DashboardServlet:** Se creará una ruta que reciba la cédula, busque la última cita en estado ATENDIDO del paciente, y devuelva el contenido del campo eceta.
- **UI de Receta:** Si se encuentra la receta, se mostrará en una interfaz tipo "hoja de receta" digital. El farmacéutico podrá leerla y luego usar los botones de "Ajuste Rápido de Stock" (que ya existen) para descontar los medicamentos entregados.

## 2. Consulta Médica Avanzada (Smart UI)
**Objetivo:** Basado en las imágenes proporcionadas, transformaremos el simple cuadro de texto de "Atender Cita" en una suite médica inteligente sin necesidad de alterar la base de datos (se guardará todo estructurado en la Historia Clínica).

### Cambios Propuestos:
- **modalAtenderCita (en modals.jsp):** Se rediseñará con pestañas (Tabs):
  - **Signos Vitales:** Campos para Frecuencia Cardíaca, Tensión Arterial, Frecuencia Respiratoria, Saturación y Temperatura. 
    - *Innovación:* Al escribir, un script evaluará los rangos y mostrará insignias automáticas (ej. si ingresa FC > 100, mostrará una alerta roja de "Taquicardia", si T > 38 mostrará "Fiebre").
  - **Escala de Glasgow:** Selectores visuales para respuesta Ocular, Verbal y Motora.
    - *Innovación:* Calculará automáticamente el puntaje total (3-15) y la clasificación del trauma.
  - **Herramientas (Calculadora de Dosis):** Una mini-calculadora integrada para Regla de Tres y goteo/microgoteo.
  - **Diagnóstico:** El campo de texto tradicional.
- **Lógica de Guardado:** Al hacer clic en "Finalizar Consulta", un script en JavaScript recopilará todos los signos vitales, puntajes de Glasgow y el texto del diagnóstico, construyendo un reporte clínico profesional y unificado que se guardará en la base de datos de la cita.

## Preguntas Abiertas
- ¿Estás de acuerdo con que la receta de la farmacia simplemente se muestre en pantalla para que el farmacéutico descuente el stock manualmente usando los botones de + / - que ya tenemos? (Es el flujo más realista en farmacias de hospital).
