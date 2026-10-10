---
titulo: Punto de partida
orden: 0
pregunta: ¿Qué se da por sabido antes de empezar y dónde cubrirlo si falta?
ultima_revision: 2026-10-10
estado: publicado
traduccion_de:
---

# Punto de partida


<img src="../assets/bandas/banda-00-es.svg" alt="El camino · punto de partida" width="560">
> Versión en inglés: [`00-punto-de-partida.en.md`](00-punto-de-partida.en.md), traducción de esta revisión.

## Para qué sirve

Fija dónde empieza el «cero» de este material. El camino arranca en cero **en inteligencia artificial**: no se presupone que se sepa nada de la materia. Sí se presupone el oficio de programar, porque a partir de la Etapa 2 se leen y se escriben programas, se levantan servicios y se trabaja con repositorios.

Esta página existe para que nadie llegue a la Etapa 0 sin los rudimentos y lo descubra tres páginas más adelante. Si ya maneja un editor, una terminal y Git, y ha escrito algo de código, puede pasar directamente a la [Etapa 0 — Fundamentos](etapa-0-fundamentos/README.md). Si no, aquí está lo mínimo para llegar en condiciones, con tiempos orientativos y sin ceremonia.

## Qué se da por sabido

| Área | Nivel suficiente para empezar |
|:--|:--|
| Edición de texto | Manejar un editor con soltura, buscar y reemplazar en un proyecto, trabajar con varios archivos abiertos |
| Terminal | Moverse por carpetas, copiar y borrar archivos, leer la salida de un comando, entender variables de entorno y códigos de salida |
| Git | Iniciar un repositorio, hacer commits, crear una rama, resolver un conflicto sencillo |
| Un lenguaje de programación | Variables, condicionales, bucles, funciones, listas y diccionarios, lectura y escritura de archivos, manejo de errores. Basta con Python o JavaScript |
| Consumo de servicios web | Entender qué es una petición HTTP, una clave de API, un JSON y un error 400 o 429 cuando se ve en una respuesta |
| Inglés técnico | Leer documentación y artículos en inglés. Buena parte de las fuentes primarias del camino están en inglés y no se traducen |

Nada de esto se examina: es el supuesto de partida. Lo que sí se comprueba, etapa a etapa, es el criterio de salida de cada una, y está descrito en su propio índice.

## Qué no se da por sabido y tampoco se enseña

- **Matemáticas avanzadas.** El camino explica qué hace un modelo y qué no, y para eso no hace falta cálculo diferencial ni álgebra lineal. Cuando una página usa una idea matemática, la define en palabras y enlaza la fuente para quien quiera ir más allá. Ninguna etapa exige demostrar nada.
- **Programar desde cero.** El camino no enseña a programar, no enseña a usar Git y no enseña a administrar sistemas. Da por hecho el oficio, y cuando necesita una herramienta concreta la nombra y enlaza su documentación.
- **Entrenar modelos desde cero.** La Etapa 0 explica qué es el entrenamiento; ninguna etapa pide entrenar un modelo grande. Sí se pide, en la Etapa 5, montar una pieza completa con modelos existentes.
- **Historia completa y filosofía de la mente.** La [página 2](etapa-0-fundamentos/02-historia-hasta-2012.md) y la [página 3](etapa-0-fundamentos/03-historia-desde-2012.md) recorren la historia por sus consecuencias técnicas, no como relato.

## Cómo cubrir lo que falte

> [!TIP]
> Recursos públicos, en español o con versión en español, accesibles sin registro. Los tiempos son orientativos y corresponden a dedicación continuada, no a lectura rápida.

| Falta | Recurso | Dedicación orientativa |
|:--|:--|:--|
| Python | El tutorial oficial del lenguaje, en español — <https://docs.python.org/es/3/tutorial/> | 8–12 h |
| Git | El libro *Pro Git*, en español, capítulos 2 y 3 — <https://git-scm.com/book/es/v2> | 4–6 h |
| Terminal y herramientas del oficio | *The Missing Semester of Your CS Education*, del MIT — <https://missing.csail.mit.edu/> | 6–8 h |
| JavaScript y desarrollo web, si se prefiere ese lenguaje | Ruta de aprendizaje de MDN — <https://developer.mozilla.org/es/docs/Learn> | 10–15 h |

Con esas bases, la Etapa 0 se puede empezar con garantías. Sin ellas, se puede leer igualmente: las páginas 1, 2, 3 y 5 no exigen escribir código.

## Los tropiezos de siempre

- **Empezar por la herramienta.** Instalar un entorno, una biblioteca de agentes y un marco de trabajo antes de entender qué se está montando. El orden contrario —concepto primero, herramienta después— es el que este material propone, y por eso la Etapa 0 no pide instalar nada.
- **Confundir el punto de partida con un examen.** Nadie va a corregir estas bases. La única consecuencia de no tenerlas es que las etapas 2 a 5 se vuelven más lentas de lo necesario.
- **Saltar a la Etapa 3 por interés en los agentes.** Es la etapa que más se consulta y la que peor se aprovecha sin las anteriores: casi todos sus errores se deciden antes, al modelar el contexto y el estado.

## Cuándo no aplica

Si el objetivo es tener una opinión informada sobre inteligencia artificial sin escribir código, la Etapa 0 sirve igual y este punto de partida no hace falta. Si el objetivo es desarrollar sistemas, el supuesto de oficio es real y conviene no forzarlo: las etapas 2 y 3 piden leer código ajeno y ejecutar el propio.

## Definiciones

- **Punto de partida**: conjunto de conocimientos que se presuponen antes de la Etapa 0, limitados al oficio de programar y no a la materia.
- **Oficio**: manejo de editor, terminal, Git, un lenguaje de programación y el consumo de servicios web.

## Referencias

- *The Python Tutorial* (español) — Python Software Foundation — <https://docs.python.org/es/3/tutorial/> (consultado 2026-10-10)
- *Pro Git* (segunda edición, español) — Scott Chacon y Ben Straub — <https://git-scm.com/book/es/v2> (consultado 2026-10-10)
- *The Missing Semester of Your CS Education* — MIT — <https://missing.csail.mit.edu/> (consultado 2026-10-10)
- *Learn web development* (español) — MDN Web Docs, Mozilla — <https://developer.mozilla.org/es/docs/Learn> (consultado 2026-10-10)
- Comprobación propia — las cuatro direcciones anteriores devolvieron código 200 en una petición HTTP el 2026-10-10

## Continuar

- Siguiente: [Etapa 0 — Fundamentos](etapa-0-fundamentos/README.md)
- Índice temático: [`../INDEX.md`](../INDEX.md)

---

*Pepe, asistido por IA. Última revisión: 2026-10-10.*
