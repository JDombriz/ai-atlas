---
titulo: De AlexNet a los agentes — la historia desde 2012
etapa: 0
orden: 3
pregunta: ¿Qué cambió a partir de 2012, qué es cada pieza que se usa hoy y qué de todo esto cubre el atlas?
prerrequisitos: [02-historia-hasta-2012.md]
ultima_revision: 2026-10-10
estado: borrador
traduccion_de:
---

# De AlexNet a los agentes: la historia desde 2012

> **Pregunta que resuelve:** ¿qué cambió a partir de 2012, qué es cada pieza que se usa hoy y qué de todo esto cubre el atlas?

## Para qué sirve

Después de 2012 el vocabulario se llena de términos que se usan sin definirlos: aprendizaje profundo, transformador, preentrenamiento, ajuste por preferencias, multimodal, modelo de razonamiento, agente. Esta página sitúa cada uno en su momento y explica **qué permitió** que las cosas se hicieran de otra manera. Sirve, sobre todo, para dos cosas: entender por qué el aprendizaje en contexto cambió la forma de construir sistemas, y saber en qué punto del relato se encuentra cada etapa de este atlas.

Es la página que más rápido envejece de todo el repositorio, y por eso lleva fecha de revisión en su cabecera. Los hechos anteriores a 2012 son estables; los de los últimos tres años, no.

## Los hitos, con su consecuencia

### 2014 · Las secuencias dejan de tener longitud fija

Dos trabajos del mismo año permiten traducir una secuencia de longitud cualquiera a otra: la arquitectura codificador–descodificador y, unos meses después, el mecanismo de atención que permite al descodificador mirar cada parte de la entrada. En paralelo, las redes generativas antagónicas formulan el aprendizaje generativo como una competición entre dos redes.

**Consecuencia.** El texto y el audio dejan de exigir ingeniería lingüística específica. La atención, que en 2014 era un añadido útil, sería tres años después la arquitectura completa.

### 2015 · La profundidad deja de ser un problema

Las conexiones residuales permiten entrenar redes de más de cien capas sin que el error se degrade al acumularse. En el concurso de reconocimiento de imágenes de ese año, la red resultante baja del 4 % de error, por debajo del rendimiento humano estimado en esa tarea en el propio informe del concurso, en torno al 5 %.

**Consecuencia.** Una tarea de percepción queda resuelta en términos prácticos. Diseñar arquitecturas a mano pierde valor frente a apilar bloques y dejar que los datos y las conexiones hagan el trabajo.

### 2016–2017 · Juegos y autojuego

El sistema que gana al campeón humano de Go combina redes neuronales con búsqueda y aprendizaje por refuerzo sobre partidas propias. Su continuación aprende sin partidas humanas, jugando contra sí misma.

**Consecuencia.** Se demuestra que el aprendizaje por refuerzo, con un entorno bien definido y una señal de victoria inequívoca, produce rendimiento sobrehumano. También se demuestra su límite: ese entorno hay que construirlo, y en problemas reales casi nunca existe con esa limpieza.

### 2017 · El transformador

*Attention Is All You Need* elimina la recurrencia y construye el modelo entero sobre autoatención, de forma que todos los elementos de una secuencia se procesan en paralelo. El entrenamiento se vuelve mucho más aprovechable en hardware matricial y la arquitectura se vuelve independiente del dominio.

**Consecuencia.** Es la pieza central de todo lo que viene después: texto, imagen, audio y código. La idea que sostiene el resto del camino es que una arquitectura general, entrenada a gran escala, se adapta después a tareas muy distintas.

### 2018 · Preentrenar y ajustar

BERT fija la receta que se generaliza: entrenar un modelo general sobre grandes volúmenes de texto sin etiquetar y después ajustarlo, con pocos datos etiquetados, para cada tarea concreta.

**Consecuencia.** El conocimiento se reutiliza entre tareas y el coste de un sistema nuevo baja. Aparece también la primera división clara del oficio: quien entrena modelos y quien los adapta.

### 2019–2020 · De modelo a asistente

Los trabajos sobre leyes de escala muestran que el error baja de forma regular al crecer datos, parámetros y cómputo, y que el reparto entre ellos importa: un modelo demasiado grande para sus datos está desaprovechado. En 2020, un modelo de 175 000 millones de parámetros demuestra que una tarea nueva puede resolverse **sin reentrenar nada**: basta describirla en la entrada y dar algunos ejemplos.

**Consecuencia.** El aprendizaje en contexto separa dos conceptos que hasta entonces iban juntos. Modelo es el artefacto entrenado; asistente es el sistema que lo envuelve y le da instrucciones y contexto. Adaptar un sistema deja de ser reentrenar y pasa a ser escribir una entrada. Esta es la frontera que explica por qué las etapas 1 y 2 de este atlas son distintas: usar y diseñar el contexto es un oficio; entrenar es otro.

### 2021–2022 · Imagen y voz siguen el mismo camino

Un modelo que aprende a relacionar imágenes con descripciones de texto permite clasificar imágenes sin haber sido entrenado para la clase concreta. La difusión se consolida como método de generación de imágenes y, ya en 2022, la técnica pasa del laboratorio a herramientas de uso general. En voz, un modelo entrenado sobre una cantidad enorme de audio transcribe sin ajuste previo a cada dominio.

**Consecuencia.** El patrón se repite en cada modalidad: un modelo general, entrenado con muchos datos sin etiquetar, y adaptación posterior por instrucción. La multimodalidad deja de ser una capacidad exótica y pasa a ser el caso normal.

### 2022 · El ajuste por preferencias y el asistente conversacional

Un trabajo de 2022 muestra que ajustar un modelo con preferencias humanas lo vuelve mucho más útil: sigue instrucciones, mantiene el formato y rechaza peticiones. A finales de ese año, un producto basado en esa técnica pone un asistente conversacional al alcance de cualquiera, sin instalación y sin conocimientos técnicos.

**Consecuencia.** Cambia el público antes que la técnica. La adopción deja de depender de saber programar, y la conversación se convierte en la interfaz. Aquí empieza el problema que ocupa a este atlas: mucha gente usando el sistema, y muy pocas personas sabiendo qué hace, cuánto cuesta y cuándo no se debe usar.

### 2022 · Razonar en voz alta y usar herramientas

Dos artículos del mismo año cierran la etapa. El primero muestra que pedir al modelo que explicite los pasos intermedios mejora su rendimiento en problemas de varios pasos. El segundo combina ese razonamiento con acciones sobre herramientas externas en un bucle: pensar, actuar, observar y volver a pensar.

**Consecuencia.** Aparece el patrón que sostiene los sistemas agénticos y con él la pregunta que responde la [página 4](04-que-es-y-que-no-es-un-agente.md). La Etapa 3 (Patrones agénticos, en preparación) está construida sobre este punto.

### 2023 · Escala, apertura y evaluación

Un modelo multimodal alcanza resultados de nivel humano en pruebas profesionales de referencia. Ese mismo año se publican modelos con pesos descargables y licencia explícita, y modelos pequeños que compiten con otros mucho mayores gracias a decisiones de eficiencia. En evaluación, aparece un banco de pruebas construido con incidencias reales de repositorios de software: la primera medida creíble de «resolver un problema de verdad» en lugar de «acertar un examen».

**Consecuencia.** La capacidad deja de ser el cuello de botella y lo pasa a ser la evaluación. Los pesos abiertos trasladan el control de coste y de privacidad al usuario, no la responsabilidad: la licencia y las condiciones de uso siguen siendo del fabricante. Y la comparación entre modelos empieza a hacerse con pruebas que se parecen al trabajo real.

### 2024–2026 · Cómputo en la inferencia, herramientas estandarizadas y agentes

Dos cambios marcan este tramo. El primero es el uso deliberado de cómputo en el momento de responder —modelos que generan pasos intermedios largos antes de dar la respuesta, entrenados por refuerzo para hacerlo—, con lo que la calidad depende de cuánto se deja pensar al sistema, y el coste también. El segundo es la estandarización del acceso a herramientas y datos mediante un protocolo común, que separa la herramienta del producto y permite reutilizarla entre asistentes distintos.

**Consecuencia.** La frontera se desplaza de «qué sabe el modelo» a «qué puede hacer el sistema, con qué permisos y a qué coste». Es exactamente el terreno de las etapas 2 a 4. Y la regulación entra en juego: el reglamento europeo de inteligencia artificial, en vigor desde agosto de 2024, aplica sus obligaciones por fases y afecta sobre todo a quien despliega sistemas en dominios sensibles.

Sobre el presente inmediato no se afirman cifras: no hay dato público consolidado que permita decir cuánto ha cambiado la productividad de los equipos, y los estudios disponibles miden cosas distintas en entornos distintos. El [estudio citado en la página 6](06-el-oficio-en-2026.md) es el ejemplo de que estas medidas hay que leerlas con cuidado.

## Qué cubre este atlas y qué deja fuera

**Cubre**, con la estructura de seis etapas:

- **Fundamentos** (esta etapa): qué es, de dónde viene, qué distingue a un agente y cuándo no hace falta.
- **Uso profesional y ingeniería** (etapas 1 y 2): elegir modelos y herramientas, construir contexto, modelar estado, pasos y condición de salida.
- **Patrones agénticos** (etapa 3): las arquitecturas que sostienen estos sistemas y el fallo que previene cada una.
- **Producción y especialización** (etapas 4 y 5): instrumentar, evaluar, asegurar, controlar el gasto y montar una pieza completa.

**Deja fuera**, de forma deliberada: la investigación original y el entrenamiento de modelos desde cero; el hardware y la infraestructura de centros de datos; la robótica y los sistemas embebidos; la historia institucional y la filosofía de la mente; y el tratamiento completo de la ética y la política, que aparece solo en lo que condiciona decisiones de ingeniería. La razón es la misma en todos los casos: son frentes que exigen dedicación completa y que este material no cubriría con la profundidad que promete.

## Errores frecuentes

- **Leer el tramo como una sucesión de modelos cada vez más grandes.** El reparto entre cómputo, datos y tamaño importa: un modelo sobredimensionado para sus datos está mal entrenado, no bien entrenado.
- **Confundir preentrenamiento con ajuste.** El primero produce un modelo general; el segundo, la capacidad de seguir instrucciones y de comportarse de una manera concreta. Son costes distintos y se corrigen con palancas distintas.
- **Equiparar pesos abiertos con libertad de uso.** La licencia decide qué se puede hacer con el modelo; la descarga solo decide quién ejecuta el cálculo.
- **Suponer que el transformador es el final del camino.** Es la arquitectura dominante, no necesariamente la definitiva; conviene distinguir lo que sostiene una técnica de lo que fue una coincidencia histórica.
- **Dar por buenas las cifras redondas.** Comparativas de modelos, errores por debajo del 1 % y porcentajes de mejora de productividad circulan sin fuente. En este repositorio, sin fuente y fecha no se citan.

## Cuándo no aplica

Sirve para situarse, no para decidir. La elección de un modelo concreto, con sus precios y límites del día en que se elige, corresponde a la Etapa 1 (Uso profesional, en preparación); el diseño de un flujo, a la Etapa 2 (Ingeniería, en preparación); y las arquitecturas de agentes, a la Etapa 3 (Patrones agénticos, en preparación). Tampoco es una fuente para citar técnica: para eso están las referencias de cada apartado, que son los artículos originales.

## Definiciones

- **Aprendizaje profundo**: conjunto de métodos que entrenan redes con varias capas intermedias, de modo que las representaciones se aprenden en lugar de diseñarse.
- **Transformador**: arquitectura basada en autoatención que procesa la secuencia completa en paralelo; sostiene la mayor parte de los modelos actuales.
- **Autoatención**: mecanismo por el que cada elemento de una secuencia se pondera contra todos los demás para construir su representación.
- **Preentrenamiento**: entrenamiento general sobre grandes volúmenes de datos sin etiquetar, previo a cualquier adaptación a una tarea.
- **Ajuste fino**: entrenamiento adicional de un modelo ya preentrenado para una tarea, un dominio o un comportamiento concreto.
- **Aprendizaje en contexto**: capacidad de resolver una tarea nueva a partir de ejemplos e instrucciones incluidos en la propia entrada, sin modificar los parámetros.
- **Ajuste por preferencias humanas (RLHF)**: método que ajusta un modelo con comparaciones humanas entre respuestas, para que resulte más útil y se comporte como se espera.
- **Modelo de difusión**: modelo generativo que produce una imagen partiendo de ruido y aplicando pasos sucesivos de limpieza.
- **Multimodal**: sistema capaz de trabajar con más de un tipo de contenido, por ejemplo texto e imagen.
- **Leyes de escala**: relaciones empíricas que describen cómo baja el error al aumentar datos, parámetros y cómputo de entrenamiento.
- **Modelo de razonamiento**: modelo entrenado para producir pasos intermedios extensos antes de responder, de modo que su calidad depende del cómputo que se le permite gastar.
- **Protocolo de contexto de modelos (MCP)**: especificación abierta para conectar un modelo con herramientas y fuentes de datos de forma reutilizable entre productos.
- **Ventana de contexto**: cantidad máxima de texto que un modelo puede tener en cuenta en una sola consulta.

## Referencias

- *Sequence to Sequence Learning with Neural Networks* — I. Sutskever, O. Vinyals y Q. Le, 2014 — <https://arxiv.org/abs/1409.3215> (consultado 2026-10-10)
- *Neural Machine Translation by Jointly Learning to Align and Translate* — D. Bahdanau, K. Cho y Y. Bengio, 2014 — <https://arxiv.org/abs/1409.0473> (consultado 2026-10-10)
- *Generative Adversarial Networks* — I. Goodfellow y otros, 2014 — <https://arxiv.org/abs/1406.2661> (consultado 2026-10-10)
- *Deep Residual Learning for Image Recognition* — K. He y otros, 2015 — <https://arxiv.org/abs/1512.03385> (consultado 2026-10-10)
- *ImageNet Large Scale Visual Recognition Challenge* — O. Russakovsky y otros, 2014 (incluye el rendimiento humano estimado en la tarea) — <https://arxiv.org/abs/1409.0575> (consultado 2026-10-10)
- *AlphaGo Zero: starting from scratch* — DeepMind, 2017 (nota del fabricante; el artículo *Mastering the game of Go without human knowledge* está en *Nature*, con acceso restringido) — <https://deepmind.google/discover/blog/alphago-zero-starting-from-scratch/> (consultado 2026-10-10)
- *Attention Is All You Need* — A. Vaswani y otros, 2017 — <https://arxiv.org/abs/1706.03762> (consultado 2026-10-10)
- *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding* — J. Devlin y otros, 2018 — <https://arxiv.org/abs/1810.04805> (consultado 2026-10-10)
- *Language Models are Unsupervised Multitask Learners* — A. Radford y otros, 2019 — <https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf> (consultado 2026-10-10)
- *Scaling Laws for Neural Language Models* — J. Kaplan y otros, 2020 — <https://arxiv.org/abs/2001.08361> (consultado 2026-10-10)
- *Training Compute-Optimal Large Language Models* — J. Hoffmann y otros, 2022 — <https://arxiv.org/abs/2203.15556> (consultado 2026-10-10)
- *Language Models are Few-Shot Learners* — T. Brown y otros, 2020 — <https://arxiv.org/abs/2005.14165> (consultado 2026-10-10)
- *Learning Transferable Visual Models From Natural Language Supervision* (CLIP) — A. Radford y otros, 2021 — <https://arxiv.org/abs/2103.00020> (consultado 2026-10-10)
- *Denoising Diffusion Probabilistic Models* — J. Ho, A. Jain y P. Abbeel, 2020 — <https://arxiv.org/abs/2006.11239> (consultado 2026-10-10)
- *High-Resolution Image Synthesis with Latent Diffusion Models* — R. Rombach y otros, 2021 — <https://arxiv.org/abs/2112.10752> (consultado 2026-10-10)
- *Robust Speech Recognition via Large-Scale Weak Supervision* — A. Radford y otros, 2022 — <https://arxiv.org/abs/2212.04356> (consultado 2026-10-10)
- *Training language models to follow instructions with human feedback* — L. Ouyang y otros, 2022 — <https://arxiv.org/abs/2203.02155> (consultado 2026-10-10)
- *Introducing ChatGPT* — OpenAI, 30 de noviembre de 2022 (anuncio original del fabricante; copia archivada porque la dirección responde 403 a peticiones automáticas) — <https://web.archive.org/web/2023/https://openai.com/blog/chatgpt/> (consultado 2026-10-10)
- *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* — J. Wei y otros, 2022 — <https://arxiv.org/abs/2201.11903> (consultado 2026-10-10)
- *ReAct: Synergizing Reasoning and Acting in Language Models* — S. Yao y otros, 2022 — <https://arxiv.org/abs/2210.03629> (consultado 2026-10-10)
- *GPT-4 Technical Report* — OpenAI, 2023 — <https://arxiv.org/abs/2303.08774> (consultado 2026-10-10)
- *Llama 2: Open Foundation and Fine-Tuned Chat Models* — H. Touvron y otros, 2023 — <https://arxiv.org/abs/2307.09288> (consultado 2026-10-10)
- *Mistral 7B* — A. Jiang y otros, 2023 — <https://arxiv.org/abs/2310.06825> (consultado 2026-10-10)
- *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* — C. Jimenez y otros, 2023 — <https://arxiv.org/abs/2310.06770> (consultado 2026-10-10)
- *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning* — D. Guo y otros, 2025 — <https://arxiv.org/abs/2501.12948> (consultado 2026-10-10)
- *Introducing the Model Context Protocol* — Anthropic, 2024, y especificación del protocolo — <https://www.anthropic.com/news/model-context-protocol> y <https://modelcontextprotocol.io/introduction> (consultado 2026-10-10)
- *Reglamento (UE) 2024/1689* — Diario Oficial de la Unión Europea — <https://eur-lex.europa.eu/eli/reg/2024/1689/oj> (consultado 2026-10-10)
- Comprobación propia — todas las direcciones anteriores devolvieron código 200 en una petición HTTP el 2026-10-10

## Continuar

- Anterior: [De Turing a AlexNet: la historia hasta 2012](02-historia-hasta-2012.md)
- Siguiente: [Qué es y qué no es un agente](04-que-es-y-que-no-es-un-agente.md)
- Índice de la etapa: [Etapa 0 — Fundamentos](README.md)
- Índice temático: [`../../INDEX.md`](../../INDEX.md)