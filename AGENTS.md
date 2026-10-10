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

**Lo que no se acepta:** fichas sin referencias accesibles, texto generado sin comprobación posterior y propuestas cuyo volumen supere a su evidencia. No se te pide prosa.

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
