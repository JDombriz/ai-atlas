# Historial de cambios

Todas las entregas del proyecto, con su fecha y su contenido. Una entrada por Release; el detalle del calendario, en [`ROADMAP.md`](ROADMAP.md).

## Sin publicar

### Añadido

- Doce fichas semilla del catálogo y la primera receta, previstas para la entrega del lunes 26 de octubre de 2026.

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