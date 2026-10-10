# Historial de cambios

Todas las entregas del proyecto, con su fecha y su contenido. Una entrada por Release; el detalle del calendario, en [`ROADMAP.md`](ROADMAP.md).

## Sin publicar

### Añadido

- Doce fichas semilla del catálogo y la primera receta, previstas para la entrega del lunes 26 de octubre de 2026.
- `GOVERNANCE.md`, `MAINTENANCE.md` y `CODE_OF_CONDUCT.md`.

## v0.1 — sábado 10 de octubre de 2026

Primera entrega publicada. El repositorio se abre al público con la Etapa 0 completa y su calendario.

### Añadido

- **Etapa 0 — Fundamentos, completa**: seis páginas —qué es la inteligencia artificial; la historia hasta 2012; la historia desde 2012; qué es y qué no es un agente; dónde no hace falta la inteligencia artificial; y el oficio en 2026—, más su práctica de cierre y su selección de recursos.
- `camino/00-punto-de-partida.md`, que fija qué se da por sabido antes de empezar y dónde cubrirlo.
- Estructura del repositorio: camino de seis etapas, catálogo de siete categorías, recetas y referencia.
- Plantillas de etapa, página, ficha, receta y RFC.
- `scripts/build_index.py`, que genera `INDEX.md`, `GLOSSARY.md` y `llms.txt` a partir del contenido, y `scripts/check_relative_links.py`, que comprueba los enlaces relativos entre páginas.
- Comprobación automática semanal de enlaces y regeneración de índices en cada envío.
- `README.md`, `ROADMAP.md`, `CONTRIBUTING.md`, `AGENTS.md` y las licencias (MIT para código y plantillas, CC BY 4.0 para la documentación, CC0 para los datos del catálogo).
- Canal de propuestas para asistentes de IA: plantilla «propuesta asistida» y reglas en `AGENTS.md`. Proponer sí, verificar no.
- Glosario inicial generado desde las páginas de la Etapa 0: 62 términos.

### Comprobado antes de publicar

- Las 63 direcciones citadas en el repositorio se comprobaron por petición HTTP el 2026-10-10: 61 respondieron 200; la edición canónica del artículo de Turing en *Mind* responde 403 y se acompaña de una copia abierta; el informe técnico del R1 en DTIC se retiró por respuesta intermitente y se sustituyó por la copia archivada del artículo de AAAI de 1980.
- Los 148 enlaces relativos entre páginas, comprobados por ejecución: ninguno roto.
- Los tres índices generados, regenerados por ejecución.

### Cambiado

- Cabecera e imagen de previsualización social rehechas sobre el arte cartográfico generado con una herramienta de imagen, con tipografía compuesta encima y velo degradado para garantizar la legibilidad. Guardadas en JPEG en lugar de PNG: la social superaba el megabyte que admite GitHub.
- El orden de publicación se adelantó una semana respecto a la fecha prevista (lunes 19 de octubre): la entrega estaba redactada y aprobada el día 10. El calendario de la Fase 1 no se desplaza y arranca el lunes 26 de octubre.