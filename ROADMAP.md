# Calendario de publicación

Ritmo: **una entrega semanal** (los lunes) y **una Release cada cuatro semanas**. Cada semana, el borrador en español está listo el jueves anterior y se publica el lunes si ha pasado la revisión humana. Si no la pasa, la entrega se pospone y aquí queda anotado el motivo.

Los estados posibles de una entrega son: `planificada`, `en investigación`, `redactada`, `en revisión`, `aprobada` y `publicada`.

## Fase 0 — Publicación mínima

Trabajo previo, sin anuncio público. Semana del 12 al 18 de octubre de 2026. **Cerrada el sábado 10 de octubre de 2026: la Release v0.1 se publicó ese día y el repositorio pasó a público.**

- [x] Repositorio, licencias, `README.md`, `CONTRIBUTING.md`, `AGENTS.md`.
- [x] Plantillas de etapa, página, ficha, receta y RFC.
- [x] `scripts/build_index.py` generando los tres índices.
- [x] Imagen de cabecera y de previsualización social, en su versión inicial. Banner definitivo generado con herramienta de imagen y recompuesto sobre `assets/banner.html`; el prompt está en `assets/prompt-banner.md`.
- [x] `camino/00-punto-de-partida.md` y la Etapa 0 completa (documentación, práctica y recursos).
- [ ] 12 fichas semilla y 1 receta.
- [x] `ROADMAP.md` con las entregas siguientes.
- [ ] **Tarea pendiente (manual, en GitHub):** subir `assets/social-preview.jpg` en *Settings → Social preview*. Solo se puede hacer desde la interfaz, y el apartado aparece cuando el repositorio es público.

### Entrega en curso

| Entrega | Revisión humana | Publicación | Estado |
|:--|:--|:--|:--|
| Release v0.1 — Etapa 0 completa (seis páginas, práctica y recursos) | aprobada por el autor el sábado 10 de octubre de 2026 | **publicada el sábado 10 de octubre de 2026** | `publicada` |

**Publicación adelantada.** La Etapa 0 quedó redactada y aprobada el 10 de octubre, con una semana de antelación sobre la fecha prevista, para que el paso del repositorio a público llegara con contenido de valor y no con un esqueleto. Se publicó el mismo día de la aprobación.

Las doce fichas semilla y la primera receta **no** entraron en esta publicación: son la primera entrega de la Fase 1, y así se anuncia. La Etapa 0 se publicó con sus cuatro elementos —índice, documentación, práctica y recursos—, y `recursos.md` enlaza directamente a las fuentes mientras no existan sus fichas de catálogo.

El calendario de la Fase 1 **no se desplaza** por este adelanto: arranca con la semana 1 el lunes 26 de octubre, como estaba previsto.

## Fase 1 — Primer trimestre

| Semana | Revisión | Publicación | Entrega | Estado |
|--:|:--|:--|:--|:--|
| 1 | jue 22 oct 2026 | lun 26 oct 2026 | 12 fichas semilla de la Etapa 0 y 1 receta + Etapa 1, páginas 1–3 y 8 fichas de `catalogo/modelos/` | en revisión |
| 2 | jue 29 oct 2026 | lun 2 nov 2026 | Receta: elegir un modelo para una tarea concreta | planificada |
| 3 | jue 5 nov 2026 | lun 9 nov 2026 | Etapa 1, páginas 4–5 + práctica + 8 fichas de `catalogo/herramientas/` | planificada |
| 4 | jue 12 nov 2026 | lun 16 nov 2026 | Receta: estimar el coste por tarea · **Release v0.2** — Etapa 1 cerrada | planificada |
| 5 | jue 19 nov 2026 | lun 23 nov 2026 | Etapa 2, páginas 1–3: contexto y estado | planificada |
| 6 | jue 26 nov 2026 | lun 30 nov 2026 | Etapa 2, páginas 4–6: grafo, bucles y salida + 8 fichas de `catalogo/aprendizaje/` | planificada |
| 7 | jue 3 dic 2026 | lun 7 dic 2026 | Receta: construir contexto útil | planificada |
| 8 | jue 10 dic 2026 | lun 14 dic 2026 | Etapa 2, práctica y primeras comparativas · **Release v0.3** — Etapa 2 cerrada | planificada |
| 9 | jue 14 ene 2027 | lun 18 ene 2027 | Etapa 3, páginas 1–4: ReAct, herramientas, reflexión, planificación | planificada |
| 10 | jue 21 ene 2027 | lun 25 ene 2027 | Etapa 3, páginas 5–7 + 8 fichas de `catalogo/investigacion/` | planificada |
| 11 | jue 28 ene 2027 | lun 1 feb 2027 | Receta: cuándo no usar agentes · **Release v0.4** — Etapa 3 cerrada | planificada |

**Del 21 de diciembre al 8 de enero no hay calendario.** En ese periodo no hay revisión y no se publica. Está declarado por adelantado, que es la forma de que una pausa no parezca un abandono.

## Fase 2 — Continuidad

A partir de febrero de 2027: etapas 4 y 5, recetas cada tres semanas, fichas hasta completar las siete categorías del catálogo y la sección de referencia creciendo con las comparativas que pida el uso real. Antes de abrir esta fase se decide, con los datos de las once entregas anteriores, si el ritmo semanal se mantiene o pasa a quincenal.

## Entregas publicadas

| Versión | Fecha | Contenido |
|:--|:--|:--|
| **v0.1** | sáb 10 oct 2026 | Etapa 0 completa —seis páginas, práctica y recursos— y la página de punto de partida. Repositorio abierto al público el mismo día |
