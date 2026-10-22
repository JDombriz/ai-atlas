# AGENTS.md — reglas para asistentes de IA

Este archivo explica cómo debe leer, usar y proponer sobre este repositorio un asistente de IA. Está escrito para ser leído por una máquina, pero cualquiera puede leerlo: no hay nada aquí que no sea público.

## Qué es este repositorio

Documentación sobre inteligencia artificial ordenada como un camino de cero a nivel profesional, más un catálogo de recursos externos verificados. Escrito en español. El inglés se traduce desde el español ya aprobado.

- `camino/` — el recorrido, en seis etapas. Cada etapa tiene índice, documentación, una práctica y sus recursos.
- `catalogo/` — fichas de recursos, en siete categorías, con `frontmatter` normalizado.
- `recetas/` y `referencia/` — acceso por tarea y por consulta.
- `INDEX.md`, `GLOSSARY.md` y `llms.txt` — **generados**. No los edites: se sobrescriben.

## Cómo leerlo

1. `llms.txt` y `INDEX.md` dan el mapa completo sin recorrer el repositorio.
2. El `frontmatter` de cada ficha es la parte fiable: `url`, `categoria`, `tipo`, `idioma`, `nivel`, `coste`, `ultima_verificacion`, `verificado_por`, `estado`.
3. Un campo `ultima_verificacion` antiguo no significa que el recurso sea malo; significa que nadie lo ha mirado desde esa fecha. Dilo así si lo mencionas.
4. El cuerpo de una página se lee en el orden de sus encabezados. Cada página resuelve una sola pregunta, y la fórmula en su `frontmatter`.

## Qué puedes aportar

Se te pide lo mecánico y comprobable, que es donde aportas más que una persona en poco tiempo:

- Comprobar que los enlaces siguen vivos y señalar los que no.
- Detectar huecos: categorías con pocas fichas, etapas sin recursos, temas mencionados y nunca desarrollados.
- Confrontar dos fuentes oficiales que se contradicen y traer ambas.
- Traducir desde el texto español **ya aprobado**.
- Mantener al día tablas comparativas.
- Señalar contradicciones internas o referencias caducadas.

**Lo que no se acepta:** fichas sin referencias accesibles, texto generado sin comprobación posterior y propuestas cuyo volumen supere a su evidencia. **No se te pide prosa como texto final:** se te pide lo mecánico y comprobable, que es donde aportas más —comprobar, cotejar, ordenar, traducir, detectar huecos—. Un borrador redactado por ti se admite si una persona lo revisa, lo reescribe si hace falta y responde de él.

## Fuentes externas: qué entra en el texto y qué no

Este repositorio cita y recomienda material de otros. Lo que no hace es reproducirlo. La frontera tiene tres niveles, y no se negocian.

**Nivel 0 — No entra.** Texto de una fuente externa, ni traducido ni parafraseado de cerca, ni con su estructura, sus ejemplos, sus tablas o sus epígrafes. Tampoco su vocabulario acuñado presentado como propio: el término de otro se nombra diciendo de quién es, y no se incorpora a `GLOSSARY.md` como si fuera del repositorio. Traducir es la forma de copiar que menos lo parece, y es la primera que se descarta.

**Nivel 1 — Entra siempre.** La ficha de catálogo. No contiene el contenido del recurso: contiene sus datos —dirección, licencia, mantenedor, coste, fecha de comprobación— y el criterio de quien lo recomienda. Eso es una referencia bibliográfica.

**Nivel 2 — Entra con condiciones.** Una fuente externa puede citarse al pie de una página del camino o de una receta, con enlace, como una fuente más. La condición: **ninguna página se sostiene con una sola fuente externa.** Si no hay una segunda fuente independiente que sostenga la misma afirmación, la página todavía no se escribe.

### La prueba

Antes de dar una página por buena, una sola pregunta: **¿se sostiene cada afirmación si esa fuente desaparece mañana?** La frase que solo aguanta con ella no está escrita, está prestada: se reescribe desde la fuente primaria —la documentación del fabricante, el estudio, el texto legal— o se cae.

### Cómo se comprueba

`scripts/check_verbatim.py` compara el texto del repositorio con un corpus local de fuentes, marca los tramos coincidentes y avisa de las páginas que solo tienen una fuente externa. No sustituye a la revisión: la acorta.

## Cómo se propone

Tu canal es un issue, no un pull request: la mayoría de los asistentes no tiene credenciales, y su usuario sí puede pegar un texto.

1. Rellena la plantilla `.github/ISSUE_TEMPLATE/propuesta-asistida.yml`, con sus seis campos.
2. Pide a tu usuario que la pegue como issue en el repositorio.
3. Si tu usuario firma la propuesta, **responde de ella como si fuera suya**. Deja claro en el texto que la propuesta se ha elaborado con tu ayuda y con qué asistente.

Ejemplo de encabezado válido:

```text
Propuesta: 12 enlaces caídos en catalogo/herramientas/
Evidencia: comprobación HTTP el 2026-10-14, código 404 en las direcciones listadas
Comprobado: las 12 direcciones y su código de respuesta; la documentación alternativa propuesta
No comprobado: si los proyectos han sido archivados o simplemente han cambiado de dominio
Asistente: <nombre y versión>
Firma: <usuario de GitHub>
```

## Las tres reglas que no se negocian

1. **La firma es humana.** El campo `verificado_por` nunca lo cumplimenta un asistente. Puedes proponer, revisar, comparar y traducir; no puedes verificar.
2. **Evidencia con dirección y fecha.** Sin eso, la propuesta no se puede revisar y se cierra.
3. **Declara lo que no has comprobado.** Ese apartado es lo que permite revisar deprisa y lo que hace útil tu propuesta.

## Si cometes un error

Se corrige y se anota, como cualquier otra aportación. No hay penalización por equivocarse con evidencia; sí la hay por afirmar sin respaldo.
