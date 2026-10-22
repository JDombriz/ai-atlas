# Historial de cambios

Todas las entregas del proyecto, con su fecha y su contenido. Una entrada por Release; el detalle del calendario, en [`ROADMAP.md`](ROADMAP.md).

## Entrega 1 — jueves 22 de octubre de 2026

Entrega semanal, sin Release: la v0.2 llega el 16 de noviembre al cerrar la Etapa 1. Adelantada del lunes 26 al jueves 22, el mismo día de la revisión, por decisión del autor.

### Añadido

- **Doce fichas semilla del catálogo** (`catalogo/investigacion/`): las ocho fuentes históricas que sostienen la Etapa 0 —Turing, Dartmouth, ALPAC, Lighthill, MYCIN, R1, Brock y la traducción estadística— y las cuatro de evidencia sobre el oficio —productividad con Copilot, METR, SWE-bench y la investigación de DORA—. Cada una con sus datos comprobados, sus límites de uso y su firma.
- **Ocho fichas de modelos** (`catalogo/modelos/`): la frontera de Anthropic, su caballo de batalla, los dos extremos de OpenAI, el modelo de contexto largo de Google, el abierto de Meta, el europeo y el pequeño de Mistral. Con precios y ventanas verificados en las páginas de cada fabricante, y las trampas de facturación dentro de la ficha.
- **Etapa 1 — Uso profesional, páginas 1 a 3**: elegir modelo para una tarea, la instrucción y el contexto, más el índice de la etapa. Las páginas 4 y 5 se publican con el cierre de la etapa.
- **La primera receta**, `recetas/banco-de-diez-casos.md`: montar una prueba de diez casos con respuesta conocida antes de elegir modelo.
- Cuatro bandas nuevas en `assets/bandas/` para la Etapa 1, generadas con `scripts/make_bands.py`, cuya tabla se ha ampliado con los rótulos de la etapa.
- En la página de recursos de la Etapa 0, el título de cada fuente enlaza ya a su ficha del catálogo, con el enlace original al lado.

### Comprobado antes de publicar

- **26 direcciones comprobadas por HTTP el 2026-10-22** —las 18 de la Etapa 0 y las 8 páginas de modelo—: todas respondieron 200 salvo dos. El alojamiento de la propuesta del taller de Dartmouth (`jmc.stanford.edu`) no acepta conexiones ese día, aunque el 10 de octubre respondía: la ficha lo dice y acompaña la copia del Internet Archive. El Reglamento europeo responde 202 con un desafío anti-automatización; el texto se comprobó en un navegador.
- **380 enlaces relativos** entre páginas, comprobados por ejecución: ninguno roto.
- Los tres índices, regenerados por ejecución: 20 fichas, 1 receta, 2 etapas y 75 términos de glosario.
- Los precios y las ventanas de contexto son los que declaran los fabricantes esa fecha, y constan con fecha en cada ficha y en la página 1 de la Etapa 1: son el dato más perecedero de todo el repositorio.

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

### Añadido el mismo día, con la aprobación del autor

- **Documentos de gobierno**: `GOVERNANCE.md`, `MAINTENANCE.md` y `CODE_OF_CONDUCT.md`, enlazados desde `README.md` y `CONTRIBUTING.md`. Cierran el hueco más visible de un repositorio abierto: hasta ahora las reglas de participación remitían a un gobierno que no estaba escrito.
- **Versión inglesa de la Etapa 0**, completa: diez archivos hermanos `*.en.md` —las seis páginas, el índice de la etapa, la práctica, los recursos y el punto de partida—, traducidos desde el texto español aprobado. Cada página española enlaza con su traducción y cada traducción avisa del original, con la fecha de la revisión de la que procede.
- **Decisión D13: publicación bilingüe simultánea.** Desde esta entrega, todo lo que se publique del camino sale en español y en inglés el mismo día.
- `scripts/build_index.py` excluye los archivos `*.en.md` del índice temático y del glosario, que son el mapa del texto español, y enlaza cada traducción junto a su página.
- **Recursos visuales que GitHub respeta**: una banda SVG en la paleta —azul profundo con filete ámbar— al principio de cada página, en los dos idiomas, generada por `scripts/make_bands.py`; y un bloque de aviso de GitHub (`[!NOTE]`, `[!TIP]`, `[!WARNING]`) por página, sólo donde el contenido es de verdad una nota o una advertencia. Las negritas no pueden colorearse dentro de un README: GitHub elimina los atributos de estilo, y se decidió no montar un sitio estático por el coste de mantenimiento.
- `scripts/preview_page.py`: genera dos vistas de una página —una que imita a GitHub y otra con la paleta— para revisar el aspecto antes de publicar. `scripts/check_relative_links.py` comprueba también las rutas de las imágenes.