# -*- coding: utf-8 -*-
import io

with io.open('src/main/webapp/views/dashboard.jsp', 'r', encoding='utf-8') as f:
    c = f.read()

html_to_inject = '''
                    <h6 class="text-theme pb-2 mb-4 mt-5" style="border-bottom: 1px solid rgba(255,255,255,0.1);"><i class="bi bi-clipboard2-pulse text-warning me-2"></i>Evaluaci\u00F3n Cl\u00EDnica y Glasgow</h6>
                    <div class="row g-4 mb-4">
                        <div class="col-md-12">
                            <label class="form-label small text-secondary fw-semibold">Diagn\u00F3stico Cl\u00EDnico Preliminar</label>
                            <textarea name="diagnosticoClinico" class="form-control" rows="3" placeholder="Ej: Paciente presenta dolor abdominal..."></textarea>
                        </div>
                        <div class="col-md-12">
                            <div class="d-flex justify-content-between align-items-center mb-2">
                                <label class="form-label small text-secondary fw-semibold mb-0">Escala de Glasgow</label>
                                <div class="form-check form-switch">
                                    <input class="form-check-input" type="checkbox" id="glasgowCheckNuevo" onchange="toggleGlasgow('Nuevo')">
                                    <label class="form-check-label text-muted small" for="glasgowCheckNuevo">No aplica / No evaluado</label>
                                </div>
                            </div>
                            <div class="row g-2" id="glasgowContainerNuevo">
                                <div class="col-md-4">
                                    <select id="g_ocularNuevo" class="form-select" onchange="calcularGlasgowNuevo()">
                                        <option value="4">4 - Ocular: Espont\u00E1nea</option>
                                        <option value="3">3 - Ocular: A la orden verbal</option>
                                        <option value="2">2 - Ocular: Al dolor</option>
                                        <option value="1">1 - Ocular: Sin respuesta</option>
                                    </select>
                                </div>
                                <div class="col-md-4">
                                    <select id="g_verbalNuevo" class="form-select" onchange="calcularGlasgowNuevo()">
                                        <option value="5">5 - Verbal: Orientado</option>
                                        <option value="4">4 - Verbal: Confuso</option>
                                        <option value="3">3 - Verbal: Inapropiado</option>
                                        <option value="2">2 - Verbal: Incomprensible</option>
                                        <option value="1">1 - Verbal: Sin respuesta</option>
                                    </select>
                                </div>
                                <div class="col-md-4">
                                    <select id="g_motoraNuevo" class="form-select" onchange="calcularGlasgowNuevo()">
                                        <option value="6">6 - Motora: Obedece</option>
                                        <option value="5">5 - Motora: Localiza dolor</option>
                                        <option value="4">4 - Motora: Flexi\u00F3n normal</option>
                                        <option value="3">3 - Motora: Flexi\u00F3n anormal</option>
                                        <option value="2">2 - Motora: Extensi\u00F3n</option>
                                        <option value="1">1 - Motora: Sin respuesta</option>
                                    </select>
                                </div>
                                <div class="col-12 mt-2">
                                    <span class="badge bg-primary fs-6" id="glasgowTotalNuevo">15 / 15 (Normal)</span>
                                </div>
                            </div>
                            <input type="hidden" name="glasgow" id="glasgowInputNuevo" value="15">
                        </div>
                    </div>
                    <div class="mt-5 text-end">'''

c = c.replace('<div class="mt-5 text-end">', html_to_inject, 1)

with io.open('src/main/webapp/views/dashboard.jsp', 'w', encoding='utf-8') as f:
    f.write(c)
