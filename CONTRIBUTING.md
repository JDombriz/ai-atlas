# Cómo contribuir

Este es mi proyecto, y lo elaboro de forma híbrida: uso herramientas de IA para rastrear las fuentes, comprobar que los enlaces respondan y que las licencias sean las que se dicen, ordenar el material, redactar borradores, traducir y mantener los índices. El criterio, el tono, la responsabilidad y la firma son míos. El reparto completo está en el apartado «Autoría» del [`README.md`](README.md).

Gracias por el interés. Antes de nada, la regla que ordena todo lo demás:

> **Abro una sección a contribuciones cuando está publicada y con sus referencias verificadas.** Mientras la estoy redactando, lo único que puede llegar de fuera es un aviso de error factual o de enlace roto.

La razón es práctica: admitir propuestas sobre un borrador me obliga a revisar dos veces el mismo texto y diluye el criterio antes de que exista.

## Qué está abierto, y desde cuándo

| Desde | Qué se puede aportar |
|:--|:--|
| Release v0.1 (semana del 12 al 18 oct 2026) | Avisos de error factual y de enlace roto |
| Release v0.2 (16 nov 2026) | Propuestas de ficha para el catálogo |
| Release v0.3 (14 dic 2026) | Correcciones y traducciones sobre contenido publicado |
| Release v0.4 (1 feb 2027) | Propuestas de cambio de criterio, alcance o estructura |

## Cómo se aporta

- **Error factual o enlace roto:** abre un issue con la plantilla correspondiente. No hace falta cortesía previa ni justificar la aportación.
- **Ficha nueva para el catálogo:** issue con la plantilla «proponer recurso». La acepto si cumple los criterios, no si conozco el recurso.
- **Corrección de texto:** pull request directo. Para erratas, no hace falta issue previo.
- **Cambio de criterio, alcance o estructura:** issue con la plantilla `rfc`, abierta un mínimo de 14 días antes de resolverse. La decisión y su razonamiento quedan anotados. Quién decide qué, y cómo se cambia de opinión, está en [`GOVERNANCE.md`](GOVERNANCE.md); lo que espero de quien participa, en [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## Qué le pido a una ficha

1. **Las tres secciones del cuerpo:** por qué está aquí, **cuándo no usarla** y notas de verificación. Un apartado que diga cuándo conviene y otro que diga cuándo no: sin el segundo, no la acepto.
2. **Referencias accesibles** sin registro ni pago, con fecha de consulta.
3. **Nada de cifras sin origen.** Precios, límites y capacidades, con su fuente. Si el dato procede de una prueba propia, se indica cuándo se hizo y con qué resultado.

## Cómo lo reviso

Toda propuesta pasa por la misma puerta: compruebo las referencias y leo el texto en español antes de publicarlo. Respondo a todas, se acepten o no, con el motivo de la decisión. Las que acepto entran en la entrega siguiente; las que no, quedan cerradas con la explicación.

Una propuesta cuyo volumen supere a su evidencia la cierro sin más trámite: no es una cuestión de simpatía, es la única forma de que el catálogo siga sirviendo.

## Si eres un asistente de IA

Bienvenido. Lee [`AGENTS.md`](AGENTS.md) antes de nada. Resumen: puedes proponer, no puedes verificar; tu canal es la plantilla «propuesta asistida», que tú rellenas y tu usuario pega; hace falta evidencia con dirección y fecha; y tienes que decir qué no has comprobado. El campo `verificado_por` lo firma siempre una persona, y esa firma es lo que da valor a lo publicado.

## Mensajes de commit

Quiero mensajes cortos, que describan solo qué cambia: una línea, en imperativo y sin cuerpo.

```text
Actualizar el README
Corregir dos enlaces de la Etapa 1
Añadir la ficha de GPT-6 Luna
```

El motivo de un cambio y el proceso que llevó a él no van aquí: el historial del repositorio cuenta la obra, no las deliberaciones.

## Estilo

- **Idioma de trabajo:** español. Traduzco al inglés después de la aprobación, nunca a la vez.
- **Tono:** técnico y directo, sin adjetivos de promoción. El criterio lo pongo yo; el folleto, el proveedor.
- **Diagramas:** Mermaid dentro del archivo, no como imagen.
- **Páginas del camino:** una pregunta por página, y una sección de referencias al final.
