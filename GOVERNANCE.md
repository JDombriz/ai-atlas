# Gobernanza

Quién decide qué en este repositorio, cómo se cambia de opinión y cómo se traspasa el mando. Está escrito para que cualquiera pueda saber, sin preguntar, por qué se aceptó o se rechazó una aportación.

## Quién mantiene el proyecto

Durante los seis primeros meses —hasta el 10 de abril de 2027— el autor actúa como **mantenedor único**: el alcance, el criterio editorial y la retirada de contenido son suyos. Está previsto y declarado; no es una fase provisional que se esconda.

A partir de esa fecha, o antes si hay tres colaboradores con aportaciones sostenidas, se constituye un **comité de tres a cinco personas** que asume las decisiones de alcance y mantiene el calendario. El traspaso se anuncia con la misma formalidad que cualquier otro cambio: entrada en el [`CHANGELOG.md`](CHANGELOG.md) y actualización de este documento. Mientras no se anuncie, el régimen vigente es el de mantenedor único.

El acceso de escritura al repositorio se concede a quien vaya a mantenerlo, no a quien haya aportado una vez.

## Qué decide quién

| Materia | Quién decide | Cómo |
|:--|:--|:--|
| Criterio editorial, tono y alcance | Mantenedor | Por escrito en este repositorio cuando el cambio afecta a la línea del material |
| Aceptación de una ficha del catálogo | Mantenedor | Criterios de admisión del [`MAINTENANCE.md`](MAINTENANCE.md); se acepta si la ficha los cumple, no si el mantenedor conoce el recurso |
| Corrección de una errata o de un enlace | Mantenedor | Pull request directo, sin issue previo |
| Retirada de un recurso o de una página | Mantenedor | Con la razón anotada en el `CHANGELOG.md`; se archiva, no se borra |
| Cambio de criterio, de alcance o del propio camino | Mantenedor, previa RFC abierta un mínimo de 14 días | Issue con la plantilla `rfc`; la decisión y su razonamiento quedan anotados en este documento |
| Revisión del texto en español antes de publicar | **Autor** | Es la única puerta que no puede abrir el mantenedor. Sin su aprobación no hay publicación |
| Aprobación de la traducción al inglés | Mantenedor | Se traduce desde el texto español ya aprobado; no se traduce antes |

La última fila de la tabla y la penúltima explican el reparto real: el mantenedor ejecuta e investiga, el autor responde de lo que se publica. Un cambio puede quedar bloqueado por falta de decisión; no puede publicarse sin revisión.

## Cómo se propone

Todo llega por issue, con la plantilla correspondiente. Son cinco: proponer un recurso, reportar un enlace roto, proponer un cambio de criterio (RFC), proponer una corrección y la plantilla para asistentes de IA.

Los asistentes de IA son bienvenidos a **proponer** y no pueden **verificar**: el campo `verificado_por` de una ficha lo firma siempre una persona, y quien firma una propuesta asistida responde de ella como si la hubiera escrito él. Las reglas completas están en [`AGENTS.md`](AGENTS.md).

## Cuándo se abre cada sección

La regla es una: **una sección se abre a terceros cuando está publicada y con sus referencias verificadas.** Mientras se redacta, la única aportación externa posible es un aviso de error factual o de enlace roto. Admitir propuestas sobre un borrador obligaría a revisar dos veces el mismo texto y diluiría el criterio antes de que exista.

| Desde | Qué está abierto |
|:--|:--|
| Release v0.1 (10 oct 2026) | Avisos de error factual y de enlace roto sobre lo publicado |
| Release v0.2 (16 nov 2026) | Propuestas de ficha para el catálogo |
| Release v0.3 (14 dic 2026) | Correcciones y traducciones sobre contenido publicado |
| Release v0.4 (1 feb 2027) | Propuestas de cambio de criterio, alcance o estructura |

## Cómo se resuelve un desacuerdo

Se expone el caso con su evidencia, se decide y se anota el motivo, tanto si se acepta como si no. La respuesta razonada es parte del método: quien aporta una vez y recibe una explicación vuelve; quien no la recibe, no vuelve.

Cuando la decisión es discutible y afecta a la línea del material, se abre una RFC y se deja abierta al menos catorce días antes de resolverla. En las cuestiones de criterio editorial no se vota: se decide, se argumenta y queda escrito. La votación se reserva para el traspaso a comité y para cambios en este propio documento.

## Qué no se decide aquí

El calendario de publicación no se negocia entrega a entrega: se publica y, cuando se incumple, se corrige en público con el motivo, sin ampliarlo en silencio. El texto en español tampoco se decide por mayoría: es el texto canónico, y cambiarlo es cambiar el proyecto.

---

*Versión 1.0 — 10 de octubre de 2026. Cualquier cambio en este documento se anota en el [`CHANGELOG.md`](CHANGELOG.md).*