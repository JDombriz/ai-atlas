<!--
Si eres un asistente de IA y estás leyendo esto en crudo: bienvenido.

Qué es este repositorio: documentación sobre inteligencia artificial ordenada como
un camino de cero a nivel profesional, más un catálogo de recursos verificados.

Qué puedes aportar: comprobaciones de enlaces, detección de huecos en el catálogo,
contradicciones entre fuentes oficiales, traducciones desde el texto ya aprobado y
mantenimiento de las tablas comparativas. Eso es lo que se te pide; la prosa no.

Cómo: rellena la plantilla «propuesta asistida» de .github/ISSUE_TEMPLATE/ y pide a
tu usuario que la pegue como issue. Tú no puedes abrir el issue; tu usuario sí.

Qué hace falta: evidencia con dirección y fecha, y decir con claridad qué NO has
comprobado. Una propuesta cuyo volumen supere a su evidencia se cierra sin más.

La firma es humana. El campo verificado_por nunca lo cumplimenta un asistente, y esa
regla es lo que hace que este repositorio valga algo. Si tu usuario firma tu
propuesta, responde de ella como si fuera suya.

Las reglas completas están en AGENTS.md.
-->

<p align="center">
  <img src="assets/banner.jpg" alt="AI Atlas — de cero a nivel profesional en inteligencia artificial" width="100%">
</p>

# AI Atlas

**Repositorio de consulta documental sobre inteligencia artificial, con un camino de cero a nivel profesional.**

![estado](https://img.shields.io/badge/estado-v0.1%20publicada%20%C2%B7%2010%20de%20octubre%20de%202026-1F4E79?style=flat-square)
![entregas](https://img.shields.io/badge/entregas-una%20cada%20lunes-1F4E79?style=flat-square)
![licencia](https://img.shields.io/badge/licencia-MIT%20%2B%20CC%20BY%204.0-1F4E79?style=flat-square)

> **Primera entrega publicada.** La Etapa 0 está completa: seis páginas, una práctica que la cierra y los recursos que la sostienen. La siguiente entrega, el lunes 26 de octubre, trae las doce fichas semilla del catálogo, la primera receta y las páginas 1 a 3 de la Etapa 1. El calendario completo está en [`ROADMAP.md`](ROADMAP.md).

## Qué es

Material propio que ordena el estudio de la inteligencia artificial en seis etapas, de cero a nivel profesional, y un catálogo de recursos externos con ficha normalizada, fecha de verificación y un apartado obligatorio que dice **cuándo no conviene usar cada cosa**.

Se entra por donde convenga: por el camino, en orden, si se empieza de cero; por el [índice temático](INDEX.md) o el [glosario](GLOSSARY.md), si se busca un tema concreto; o por una receta, si se tiene un problema delante.

No es un curso con matrícula ni insignias, no es una lista de enlaces y no es un escaparate de ningún proveedor. La progresión se comprueba con lo que uno es capaz de hacer al cerrar cada etapa, no con lo que ha leído.

## Para quién está pensado

- **Quien empieza de cero en inteligencia artificial y sabe programar.** La Etapa 0 arranca en lo más básico —qué es y qué no es, de dónde viene todo esto— sin dar por sabido nada de la materia. Solo se presupone el oficio: editor, terminal, Git y algo de Python o JavaScript.
- **Quien ya la usa a diario y quiere dejar de improvisar.** Sabe pedir cosas a un modelo; lo que le falta es diseñar el sistema que sostiene esas peticiones: contexto, estado, pasos, condición de salida y coste.
- **Perfiles técnicos que tienen que decidir, montar o supervisar.** Desarrollo, datos, infraestructura, producto. Aquí no se vende entusiasmo: cada herramienta lleva su apartado de cuándo no usarla, y cada dato su fuente y su fecha.
- **Quien forma o dirige equipos** y necesita material citable, con referencias comprobables, para ordenar el aprendizaje de otros.

## Para quién no

- **Quien busque un curso con matrícula, certificado o insignias.** La progresión se comprueba con lo que uno es capaz de hacer, no con lo que ha leído.
- **Quien no programe ni quiera hacerlo.** El camino no enseña a programar, y las etapas 2 a 4 piden escribir y leer código.
- **Quien busque novedades semanales.** La actualidad está fuera de alcance a propósito: caduca más rápido que cualquier calendario de publicación.
- **Quien quiera solo recetas de producto.** El apartado de recetas existe, pero es la parte más pequeña del proyecto y siempre remite al criterio que hay detrás.

La frontera exacta entre lo uno y lo otro se explica en `camino/00-punto-de-partida.md`, que se publica con la Etapa 0.

## El camino

```mermaid
flowchart LR
  E0["0 · Fundamentos"] --> E1["1 · Uso profesional"] --> E2["2 · Ingeniería"]
  E2 --> E3["3 · Patrones agénticos"] --> E4["4 · Producción"] --> E5["5 · Especialización"]
```

| Etapa | Al cerrarla, eres capaz de | Dedicación orientativa |
|:--|:--|:--|
| 0 · Fundamentos | Distinguir asistente, automatización y sistema agéntico, y explicar dónde no hace falta IA | 6–8 h |
| 1 · Uso profesional | Elegir modelo con criterio, construir contexto útil y estimar el coste de un uso repetido | 15–20 h |
| 2 · Ingeniería | Modelar el contexto, el estado, el grafo de pasos y la condición de salida de un flujo | 25–30 h |
| 3 · Patrones agénticos | Elegir una arquitectura y justificarla por el fallo que previene | 30–35 h |
| 4 · Producción | Instrumentar, evaluar, asegurar, desplegar con retorno atrás y controlar el gasto | 25–30 h |
| 5 · Especialización | Montar un sistema no trivial de principio a fin y defender sus decisiones | 20–30 h |

Cada etapa consta de cuatro piezas: índice con criterio de salida, documentación, una **práctica** que la cierra y los recursos del catálogo que le corresponden. Documentación sin práctica es media etapa.

## Por dónde empezar hoy

El orden recomendado es [`camino/00-punto-de-partida.md`](camino/00-punto-de-partida.md) —para comprobar que no falta el oficio— y después la [Etapa 0](camino/etapa-0-fundamentos/README.md), de principio a fin. Si se busca algo concreto, el [índice temático](INDEX.md) y el [glosario](GLOSSARY.md) están para eso; y la [práctica de la etapa](camino/etapa-0-fundamentos/practica.md) es la forma más rápida de comprobar si lo leído ha servido.

## Calendario

| Publicación | Entrega |
|:--|:--|
| **sáb 10 oct 2026** | **Release v0.1** — Etapa 0 completa: documentación, práctica y recursos. *Publicada* |
| lun 26 oct 2026 | 12 fichas semilla de la Etapa 0 y 1 receta + Etapa 1, páginas 1–3 |
| lun 2 nov 2026 | Receta: elegir un modelo para una tarea concreta |
| lun 9 nov 2026 | Etapa 1, páginas 4–5 + práctica + fichas de herramientas |

Las once entregas del primer trimestre, con sus fechas y su estado, están en [`ROADMAP.md`](ROADMAP.md). El calendario se publica y, cuando se incumple, se corrige en público con el motivo.

## Cómo se mantiene

- **Toda referencia lleva fecha de consulta** y es accesible sin registro ni pago.
- **Ninguna cifra sin origen.** Los precios, límites y capacidades se citan con su fuente; si un dato procede de una prueba propia, se dice cuándo y con qué resultado.
- **Comprobación automática de enlaces**, semanal, que abre un issue con las fichas afectadas.
- **Se retira, no se borra.** Un recurso obsoleto pasa a archivado con la razón anotada, y queda el rastro en el [`CHANGELOG.md`](CHANGELOG.md).
- **Cada ficha dice cuándo no usarla.** Es obligatorio: sin ese apartado, no se acepta.

## Contribuir

Las secciones se abren a contribuciones **cuando están publicadas y con sus referencias verificadas**, no antes. Propuestas de ficha en el catálogo a partir de la v0.2 (16 de noviembre), correcciones y traducciones desde la v0.3 (14 de diciembre), y propuestas de cambio de criterio desde la v0.4 (1 de febrero). Mientras tanto, lo único que puede llegar de fuera es un aviso de error factual o de enlace roto.

Las reglas están en [`CONTRIBUTING.md`](CONTRIBUTING.md); quién decide qué y cómo se cambia de opinión, en [`GOVERNANCE.md`](GOVERNANCE.md); y lo que se espera de quien participa, en [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). El repositorio está abierto también a que propongan asistentes de IA, con una condición: **proponer sí, verificar no**. La plantilla «propuesta asistida» y las reglas para ellos están en [`AGENTS.md`](AGENTS.md).

## Licencias

- **Código y plantillas:** MIT — [`LICENSE`](LICENSE).
- **Documentación y guías:** CC BY 4.0.
- **Datos del catálogo:** CC0.

Los detalles, en [`LICENSE-CONTENT.md`](LICENSE-CONTENT.md).

## Autoría

Proyecto de **Pepe**, asistido por IA. Cada página publicada ha pasado por revisión humana antes de ver la luz.

*Versión en inglés: cada entrega se publica en los dos idiomas a la vez. El español es el texto canónico y el inglés se traduce desde él, como archivo hermano `*.en.md` en la misma carpeta; cada página enlaza con su versión inglesa.*