---
titulo: Recursos de la Etapa 0
etapa: 0
orden: 100
pregunta: ¿Qué recursos externos conviene leer para cerrar los fundamentos y cuándo no conviene cada uno?
prerrequisitos: [01-que-es-la-inteligencia-artificial.md]
ultima_revision: 2026-10-10
estado: borrador
traduccion_de:
---

# Recursos de la Etapa 0

## Cómo está organizada esta página

Ninguno de estos recursos es obligatorio para cerrar la etapa: el criterio de salida se demuestra con la [práctica](practica.md), no con lecturas. Esta selección sirve para dos cosas: saber de dónde sale lo que afirman las páginas —todo lo que se puede comprobar tiene su fuente— y tener por dónde seguir cuando un tema despierte curiosidad.

Cada entrada lleva la razón por la que está y el caso en el que no conviene leerla. Eso último es tan útil como lo primero: hay documentos admirables que en esta etapa hacen perder el tiempo.

**Nota de entrega.** Las fichas normalizadas de estos recursos, con su identificador y su estado dentro del catálogo, se incorporan en la entrega siguiente, junto con las primeras doce fichas semilla. Mientras tanto, esta página enlaza directamente a las fuentes: todas devolvieron código 200 en la comprobación del 2026-10-10.

## Las fuentes que sostienen la etapa

| Recurso | Por qué está aquí | Cuándo no leerlo |
|:--|:--|:--|
| *Computing Machinery and Intelligence* — Turing, 1950 ([copia accesible](https://www.csee.umbc.edu/courses/471/papers/turing.pdf)) | El texto donde el problema se plantea de forma comprobable y donde aparece la idea de aprender en lugar de programar el conocimiento | Si se busca una introducción técnica: es un artículo de discusión, con secciones matemáticas incluidas |
| [Propuesta del taller de Dartmouth](http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf) — 1955 | El origen documental del término y de la expectativa que fija el tono de las dos décadas siguientes | Si no interesa la historia: se entiende mucho mejor contada en la [página 2](02-historia-hasta-2012.md) |
| *Language and Machines* — informe ALPAC, 1966 ([PDF](https://www.mt-archive.net/ALPAC-1966.pdf)) | Explica, con un caso concreto, por qué la financiación sigue a los resultados demostrables | Si se busca el estado actual de la traducción automática: es un documento histórico |
| [Informe Lighthill](https://www.chilton-computing.org.uk/inf/literature/reports/lighthill_report/p001.htm) — 1973 | El origen documental del primer invierno: qué se le reprochaba al área y con qué argumentos | Leído aislado se toma por una sentencia definitiva sobre la inteligencia artificial; conviene acompañarlo del contexto de la [página 2](02-historia-hasta-2012.md) |
| *Rule-Based Expert Systems: The MYCIN Experiments* — Buchanan y Shortliffe, 1984 ([texto completo](https://shortliffe.net/Buchanan-Shortliffe-1984/MYCIN%20Book.htm)) | El mejor caso documentado de conocimiento escrito a mano: qué funcionó, qué costaba mantenerlo y por qué no llegó al uso diario | Es un libro: se consulta por capítulos, no se lee entero en esta etapa |
| *R1: An Expert in the Computer Systems Domain* — McDermott, 1980 ([PDF archivado](https://web.archive.org/web/20171116060857/http:/aaai.org/Papers/AAAI/1980/AAAI80-076.pdf)) | El paso de los sistemas expertos a la industria, con el problema real que resolvían | Si se busca una evaluación moderna: es un informe técnico de su época |
| *Learning from Artificial Intelligence's Previous Awakenings* — Brock, *AI Magazine*, 2018 ([artículo](https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2809)) | Una síntesis del auge y el declive del ciclo de los sistemas expertos, con su economía | Es una revisión histórica, no una fuente primaria: ordena muy bien, pero no sirve para citar el dato original |
| *The Mathematics of Statistical Machine Translation* — Brown y otros, 1993 ([ACL Anthology](https://aclanthology.org/J93-2004/)) | El trabajo que muestra a los datos desplazando al conocimiento lingüístico escrito a mano | Es denso en notación; la idea se puede tomar de la [página 2](02-historia-hasta-2012.md) |

## Lecturas de criterio

| Recurso | Por qué está aquí | Cuándo no leerlo |
|:--|:--|:--|
| *The Bitter Lesson* — Sutton, 2019 ([ensayo](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)) | El argumento que explica por qué el aprendizaje a gran escala ha ido ganando terreno al conocimiento escrito a mano | Es un ensayo polémico, no un resultado experimental: se lee como tesis, no como prueba |
| *Rules of Machine Learning* — Google ([guía](https://developers.google.com/machine-learning/guides/rules-of-ml)) | Criterio negativo directamente aplicable: por qué la ingeniería de datos y la evaluación pesan más que el modelo | Está escrita para aprendizaje automático clásico; en modelos de lenguaje, algunas reglas se leen de otra manera |
| *Hidden Technical Debt in Machine Learning Systems* — Sculley y otros, 2015 ([NIPS](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html)) | Documenta que el modelo es la parte pequeña del sistema y dónde se acumula el coste real | Es un artículo de ingeniería, no una introducción: presupone cierta familiaridad con sistemas en producción |
| *Building effective agents* — Anthropic, 2024 ([guía](https://www.anthropic.com/engineering/building-effective-agents)) | Recomendación operativa: empezar por lo simple y añadir complejidad solo cuando previene un fallo conocido | Es documentación de un fabricante: útil por su criterio, no como fuente neutral |
| [AI RMF 1.0](https://doi.org/10.6028/NIST.AI.100-1) — NIST, 2023 | El marco de referencia para hablar de riesgo, evaluación y supervisión humana con un vocabulario común | No es un documento técnico ni entra en arquitecturas |
| [Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | El marco que condiciona qué se puede desplegar y con qué obligaciones, por fases | Su lectura completa excede esta etapa: se consulta por definiciones y por clases de riesgo |

## Evidencia sobre el oficio

| Recurso | Por qué está aquí | Cuándo no leerlo |
|:--|:--|:--|
| *The Impact of AI on Developer Productivity* — 2023 ([arXiv](https://arxiv.org/abs/2302.06590)) | Un ejemplo de experimento controlado en una tarea cerrada, con mejora clara de tiempo | No representa el trabajo habitual: la tarea está acotada y especificada |
| *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* — METR, 2025 ([arXiv](https://arxiv.org/abs/2507.09089)) | El caso contrario, en proyectos maduros y con desarrolladores expertos: el resultado contradice la expectativa | Muestra pequeña y contexto específico: se cita por lo que mide, no como conclusión general |
| *SWE-bench* — 2023 ([arXiv](https://arxiv.org/abs/2310.06770)) | Cómo se evalúa hoy una capacidad real: incidencias de repositorios con sus propias pruebas | Mide resolución de incidencias, no la utilidad ni el coste dentro de un equipo |
| [Investigación de DORA](https://dora.dev/research/) — Google Cloud | Una visión de conjunto sobre prácticas y rendimiento de equipos, por encuesta anual | Son encuestas, no experimentos: sirven para situar tendencias |

## Si le falta el oficio

Los recursos para cubrir lo que se da por sabido —Python, Git, terminal, JavaScript— están en el [punto de partida](../00-punto-de-partida.md), con su dedicación orientativa. No forman parte de esta etapa y no se revisan aquí.

## Cómo se mantiene esta selección

Los enlaces se comprueban automáticamente cada semana. Cuando uno se cae, la página sigue siendo válida: se sustituye la referencia y, si no hay sustituto, se retira con la razón anotada en el [`CHANGELOG.md`](../../CHANGELOG.md). Ninguna dirección de esta página exige registro ni pago.

## Los tropiezos de siempre

- **Leer las fuentes antes que las páginas.** El orden natural es el contrario: las páginas sitúan el problema y dicen qué buscar en cada fuente. Leídas primero, buena parte del material histórico resulta incomprensible.
- **Tomar las revisiones por fuentes primarias.** El artículo de *AI Magazine* y las guías de fabricante ordenan muy bien, pero no sustituyen al documento original cuando se quiere citar un dato.
- **Leer la etapa como una bibliografía.** No es una lista de lecturas obligatorias: es una selección con motivo y con límite.
- **Citar sin fecha de consulta.** Toda referencia de este material lleva la fecha en que se comprobó; una referencia sin fecha no informa de su vigencia.

## Cuándo no aplica

Esta selección cubre los fundamentos y el criterio general. No sirve para elegir un modelo, una herramienta ni una arquitectura: eso corresponde a las etapas siguientes. Tampoco incluye material formativo de pago, ni cursos, ni vídeos: la regla del proyecto es que toda referencia sea accesible sin registro ni pago y, en lo posible, primaria.

## Referencias

- Comprobación propia — las direcciones de esta página devolvieron código 200 en una petición HTTP el 2026-10-10; la única excepción es la edición canónica del artículo de Turing en *Mind*, que responde 403 y se sustituye por una copia abierta
- Las referencias completas, con autor, entidad y fecha de consulta, figuran al final de cada página de la etapa

## Continuar

- Anterior: [Práctica — análisis de tres procesos propios](practica.md)
- Índice de la etapa: [Etapa 0 — Fundamentos](README.md)
- Etapa siguiente: Etapa 1 (Uso profesional, en preparación)
- Índice temático: [`../../INDEX.md`](../../INDEX.md)

---

*Pepe, asistido por IA. Última revisión: 2026-10-10.*