# Mantenimiento

Cómo se conserva este repositorio, con qué cadencia se revisa lo publicado y con qué criterios entra y sale el contenido. Sin esta parte, un repositorio de consulta se convierte en una lista que envejece sin avisar.

## Ritmo de trabajo

| Momento | Qué ocurre |
|:--|:--|
| Lunes | Arranca la entrega de la semana y se publica la anterior si quedó pendiente de revisión |
| Lunes a miércoles | Investigación, redacción en español y comprobación de referencias |
| Jueves | El borrador queda listo y se señalan las decisiones discutibles |
| Jueves a domingo | Ventana de revisión humana del texto en español |
| Lunes siguiente | Traducción al inglés, publicación en los dos idiomas y actualización del calendario |

El calendario con las entregas y sus fechas está en [`ROADMAP.md`](ROADMAP.md). Cuando se incumple una fecha, se corrige en público con el motivo en una línea.

## Qué se comprueba, y con qué

**Antes de cada publicación**, por ejecución y no por lectura:

- `python3 scripts/build_index.py`: regenera `INDEX.md`, `GLOSSARY.md` y `llms.txt`. Se comprueba la salida, no el código.
- `python3 scripts/check_relative_links.py`: comprueba los enlaces relativos entre páginas y falla si alguno está roto.
- Comprobación por HTTP de todas las direcciones citadas. Las que responden 403 a peticiones automáticas se citan como original **y** acompañadas de una copia abierta o archivada, dejando dicho cuál es cuál.

**Cada semana, sin intervención:** un flujo programado comprueba todos los enlaces y abre un único issue agregado con los que hayan caído. Es la única tarea de mantenimiento que no depende de la voluntad de nadie.

**Cada seis meses, por lotes:** se revisa una parte del catálogo y una etapa del camino, por turnos. Tres resultados posibles para cada entrada: actualizar la fecha de verificación, pasar a `en-revision`, o archivar con la razón anotada.

## Criterios de admisión

Para una **ficha del catálogo**: los campos obligatorios del modelo de datos —`id`, títulos, `url`, categoría, tipo, idioma, nivel, coste, fechas y estado— y las tres secciones del cuerpo, entre ellas «Cuándo no usarlo», que es obligatoria. La dirección se comprueba antes de aceptarla. Una ficha sin verificar no entra, aunque el recurso sea evidentemente útil.

Para una **página del camino**: resuelve una pregunta, declara su etapa, lleva sus referencias con fecha de consulta y, si introduce términos, los define en su sección de definiciones. Publicar documentación sin práctica es publicar media etapa.

## Criterios de retirada

Se archiva un recurso —no se borra— cuando la dirección lleva dos comprobaciones semanales seguidas caída y no hay reemplazo canónico; cuando el proyecto lleva más de doce meses sin actividad; o cuando ha aparecido otro que lo sustituye por completo.

Una página del camino se puede archivar sin romper el recorrido: su hueco queda marcado como incompleto, no como enlace roto.

En todos los casos queda el rastro: qué se retiró, cuándo y por qué, en el [`CHANGELOG.md`](CHANGELOG.md).

## Qué se mide

- Entregas publicadas en la fecha anunciada.
- Etapas cerradas con sus cuatro elementos completos.
- Fichas activas con verificación de menos de seis meses.
- Enlaces vivos en la comprobación semanal.
- Días desde la última revisión de cada categoría y de cada etapa.
- Issues y pull requests abiertos por personas ajenas al proyecto.

No se fijan objetivos de estrellas, seguidores ni recomendación. Una cifra que no se controla deja de ser una métrica y pasa a ser una promesa que se incumple en silencio.

## Cómo se mantiene una ficha viva

Cuando pasa la revisión semestral, la ficha se mira por lo que dice de sí misma: la fecha de verificación, el estado y el apartado «Cuándo no usarlo». Si el recurso sigue siendo el mismo y correcto, se actualiza la fecha. Si ha cambiado de naturaleza —de gratuito a pago, de activo a abandonado—, se reescribe el apartado de límites, que es la parte que de verdad orienta a quien lee. Y si ya no aporta, se archiva.

---

*Versión 1.0 — 10 de octubre de 2026. Los cambios en este documento se anotan en el [`CHANGELOG.md`](CHANGELOG.md).*