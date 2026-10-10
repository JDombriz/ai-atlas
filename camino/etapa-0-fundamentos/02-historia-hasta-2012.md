---
titulo: De Turing a AlexNet — la historia hasta 2012
etapa: 0
orden: 2
pregunta: ¿De dónde viene la inteligencia artificial y qué consecuencia técnica dejó cada hito anterior a 2012?
prerrequisitos: [01-que-es-la-inteligencia-artificial.md]
ultima_revision: 2026-10-10
estado: publicado
traduccion_de:
---

# De Turing a AlexNet: la historia hasta 2012

> Versión en inglés: [`02-historia-hasta-2012.en.md`](02-historia-hasta-2012.en.md), traducción de esta revisión.

Los errores de hoy se explican por decisiones que se tomaron hace sesenta años. Casi todos los debates que se repiten —si conviene escribir el conocimiento a mano o aprenderlo de los datos, si basta con más computación o hace falta más estructura, por qué llega el dinero y por qué se va— ya se dieron entonces, y se resolvieron de una manera concreta por razones que merece la pena conocer. Quien no sabe que los inviernos existieron se sorprende cada vez que aparece el siguiente.

Este relato va por consecuencias: qué cambió en la práctica después de cada hito y qué dejó de ser necesario. Los inviernos cuentan tanto como los veranos. La segunda mitad de la historia —de 2012 a hoy— está en la [página siguiente](03-historia-desde-2012.md).

## 1950 · Turing convierte una pregunta imposible en una prueba

En *Computing Machinery and Intelligence*, Turing sustituye «¿puede pensar una máquina?» por un juego: un interrogador conversa por escrito con dos interlocutores y tiene que distinguir cuál es la máquina. No propone una máquina —no construye nada—, sino un criterio observable y una discusión ordenada de las objeciones que se le irían haciendo.

Al final del artículo deja caer la idea que más recorrido tendría: en lugar de intentar simular la mente adulta, quizá sea más práctico simular la de un niño y educarla.

**Qué cambió.** El problema se vuelve comprobable, y se admite por primera vez que programar la experiencia puede ser más viable que programar el conocimiento. Tardaría cuarenta años en demostrarse.

## 1955 · Dartmouth: nace el nombre y nace la expectativa

La propuesta del taller de verano de Dartmouth, firmada por McCarthy, Minsky, Rochester y Shannon, usa por primera vez la expresión *artificial intelligence*. Y formula una conjetura muy atrevida: que todo aspecto del aprendizaje puede describirse con tal precisión que una máquina llegue a simularlo. Al taller asistieron unas diez personas.

**Qué cambió.** Se acuña el término —en la propuesta de un taller, no en un artículo de revista— y con él una expectativa que costaría décadas corregir: la de que aquello era cuestión de un verano de trabajo.

## 1958 · Rosenblatt y el perceptrón

El perceptrón aprende a clasificar a partir de ejemplos, con una regla de corrección sencilla aplicada a una sola capa de unidades. Se llegó a construir en hardware.

**Qué cambió.** Aparece la alternativa al conocimiento escrito: en lugar de reglas, ejemplos y un procedimiento de ajuste. Es la primera formulación operativa del aprendizaje automático, y el punto de partida de todo lo que viene después.

## 1966 · El informe ALPAC y la primera retirada del dinero

Un comité estadounidense evalúa los programas de traducción automática de la época y concluye que no alcanzan a la traducción humana ni en calidad ni en coste. La financiación del área se recorta.

**Qué cambió.** Queda demostrado que el dinero sigue a los resultados demostrables y no a las promesas. Y deja un prejuicio que costaría décadas deshacer: que la traducción automática no funciona.

## 1969 · La crítica que frenó una línea entera

*Perceptrons*, de Minsky y Papert, demuestra los límites de las redes de una sola capa: hay funciones que no pueden representar, y el ejemplo clásico es la disyunción exclusiva. El libro es exacto en lo que afirma, pero la lectura que se hizo de él fue mucho más amplia de lo que decía: se concluyó que añadir capas no servía, cuando lo que faltaba era un método para entrenarlas.

**Qué cambió.** La línea conexionista pierde financiación durante casi dos décadas y el esfuerzo se desplaza a los sistemas simbólicos. El teorema era cierto; la conclusión que se extrajo de él, falsa.

## 1972 · DENDRAL: el conocimiento, escrito a mano

En Stanford, el proyecto DENDRAL codifica las restricciones de la espectrometría de masas para proponer estructuras químicas, y su continuación Meta-DENDRAL aprende reglas a partir de datos. Es el primer sistema experto en el sentido moderno.

**Qué cambió.** Queda establecida la tesis que domina los veinte años siguientes: el cuello de botella no es el razonamiento, es el conocimiento. Y si hay que escribirlo a mano, escribirlo es caro.

## 1973 · El informe Lighthill y el primer invierno

El informe encargado por el Reino Unido concluye que la inteligencia artificial no había cumplido lo prometido y que no había base para sostener el gasto. La financiación británica se reduce drásticamente y buena parte de la investigación se reorienta.

**Qué cambió.** Llega el primer invierno: entre 1974 y 1980 la financiación se contrae, los grupos se disuelven y la expresión se vuelve incómoda en los presupuestos. La causa no fue la falta de ideas, sino la distancia entre lo prometido y lo entregado.

## 1976 · MYCIN y la lección que no se aprendió

MYCIN, también en Stanford, asesora sobre terapia antimicrobiana con varios centenares de reglas que incorporan factores de certeza. En las evaluaciones publicadas su comportamiento es comparable al de los especialistas en los casos seleccionados. Nunca llegó al uso clínico rutinario.

**Qué cambió.** Dos lecciones duraderas. La primera, que el razonamiento con incertidumbre es tratable. La segunda, la incómoda: un sistema que acierta no basta. Faltaban la integración con los sistemas del hospital, un responsable legal y, sobre todo, una forma sostenible de mantener el conocimiento al día. Sesenta años después seguimos llamándolo evaluación y operación.

## 1980 · XCON: el conocimiento entra en la industria

En Digital Equipment Corporation, el sistema R1 —luego XCON— configura pedidos de sistemas VAX: comprueba compatibilidades y produce la lista de componentes. Se puso en explotación y la compañía sostuvo un departamento propio de ingeniería del conocimiento para mantenerlo.

**Qué cambió.** El conocimiento experto pasa de ser objeto de investigación a ser activo comercial, y arranca el ciclo de los años ochenta: auge, empresas de herramientas expertas, expectativas desmedidas. El ciclo se rompió por una razón económica y no técnica: las bases de reglas crecieron hasta miles de reglas, cada cambio obligaba a revisar el conjunto, y las líneas de producto cambiaban más rápido de lo que el conocimiento se podía mantener. Las cifras de ahorro que se citan de aquella época proceden de testimonios y de la propia empresa, no de cuentas auditables.

## 1986 · La retropropagación devuelve el aprendizaje al centro

Rumelhart, Hinton y Williams publican el método para ajustar los pesos de redes con capas intermedias, calculando la contribución de cada uno al error final. El algoritmo era conocido en otras disciplinas; lo que faltaba era mostrarlo funcionando en redes útiles.

**Qué cambió.** El obstáculo de 1969 desaparece. Las redes multicapa vuelven a la investigación con fundamento, aunque sin datos ni computación suficientes para competir con los sistemas simbólicos en problemas reales.

## 1998 · Las redes convolucionales y una tarea resuelta

La familia LeNet reconoce dígitos manuscritos con una arquitectura que aprovecha la estructura de la imagen —convoluciones y reducción de resolución— en lugar de tratar cada píxel por separado. Llegó a usarse en la lectura automática de cheques en Estados Unidos.

**Qué cambió.** Queda demostrado que ciertos problemas de percepción se resuelven mejor aprendiendo de los datos que escribiendo reglas. El método, sin embargo, no escala con el volumen de datos y de computación disponible entonces. La misma arquitectura, con veinte años más de datos y con procesadores gráficos, sería la que ganó en 2012.

## 1993 · La traducción estadística: los datos ganan a las reglas

Los modelos de traducción de IBM estiman, a partir de corpus paralelos, la probabilidad de que una frase en un idioma corresponda a otra. Sin gramáticas escritas a mano y sin conocimiento lingüístico explícito, superan a los sistemas de reglas.

**Qué cambió.** El giro estadístico se generaliza en la industria: buscadores, filtros de correo y reconocimiento de voz pasan a construirse sobre datos. La lección se repetiría: cuando hay datos suficientes, el método que los aprovecha desplaza al que codifica el conocimiento a mano.

## 1997 · Deep Blue: fuerza bruta, no aprendizaje

El sistema de IBM gana a Garri Kaspárov evaluando posiciones con una función escrita por expertos y explorando millones de jugadas por segundo. No hay aprendizaje en juego.

**Qué cambió.** La victoria mostró el valor del diseño específico y de la computación masiva, y también su límite: el resultado no se transfirió a ningún otro problema. Ese patrón —hito espectacular, transferencia nula— se repite en cada década, y conviene recordarlo cada vez que aparece uno nuevo.

## 2012 · ImageNet, las tarjetas gráficas y el corte

El conjunto de datos ImageNet reúne millones de imágenes etiquetadas y, desde 2010, un concurso anual compara sistemas sobre la misma tarea. En 2012, la red de Krizhevsky, Sutskever y Hinton reduce el error del mejor sistema anterior de forma abrupta: 15,3 % de error frente al 26,2 % del segundo clasificado. El trabajo se apoyó en tarjetas gráficas —dos unidades de consumo, adaptadas para el cálculo matricial— y en decisiones de arquitectura como la función de activación ReLU y el abandono de unidades.

**Qué cambió.** Coinciden por primera vez tres cosas: datos etiquetados a escala, computación barata y paralela, y una arquitectura entrenable en profundidad. A partir de ahí, la ingeniería de características deja de ser el oficio principal en visión por computador: las representaciones se aprenden. Aquí cortamos la historia, porque desde 2012 la discusión sobre qué codificar a mano pierde peso en casi todos los frentes.

## Tres cosas que enseña este tramo

1. **Los inviernos tienen causas concretas.** No fueron pausas misteriosas: cambió qué se financiaba y qué se investigaba. El diagnóstico de Lighthill sobre la distancia entre promesa y entrega era razonable; el error de la época fue prometer por delante de la evidencia.
2. **Cada avance es una coincidencia de tres cosas.** La idea, los datos y la máquina. En 2012 las convoluciones y las redes multicapa llevaban décadas inventadas; lo que llegó fueron los datos y los procesadores.
3. **Un hito resuelve un problema acotado, no el problema.** Deep Blue no enseñó nada sobre el lenguaje; el reconocimiento de dígitos no sirvió para leer un contrato. Conviene desconfiar de quien anuncia que el último resultado lo cambia todo.

## Definiciones

- **Juego de la imitación**: prueba propuesta por Turing en la que un interrogador debe distinguir, por escrito, entre una máquina y una persona.
- **Sistema experto**: programa que resuelve un problema acotado reproduciendo el conocimiento de especialistas, escrito en forma de reglas.
- **Perceptrón**: clasificador de una sola capa que aprende sus pesos a partir de ejemplos.
- **Conexionismo**: línea de trabajo que modela el aprendizaje con redes de unidades simples conectadas, frente a la manipulación de símbolos.
- **Retropropagación**: método para calcular cómo contribuye cada peso de una red multicapa al error final, lo que permite ajustarlos.
- **Invierno de la inteligencia artificial**: periodo de contracción de la financiación y del interés institucional, con causas económicas y de expectativas.
- **Ingeniería de características**: oficio de diseñar a mano las variables que un sistema usará para decidir, sustituido en parte por representaciones aprendidas.
- **Brecha de adquisición de conocimiento**: dificultad de extraer de un especialista su conocimiento y escribirlo en forma utilizable por un programa.
- **Red convolucional**: red que explota la estructura espacial de la entrada, aplicando el mismo filtro en distintas posiciones.

## Referencias

- *Computing Machinery and Intelligence* — A. M. Turing, *Mind*, vol. LIX, nº 236, 1950 — copia accesible en <https://www.csee.umbc.edu/courses/471/papers/turing.pdf> (consultado 2026-10-10)
- *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence* — J. McCarthy y otros, 1955 — <http://jmc.stanford.edu/articles/dartmouth/dartmouth.pdf> (consultado 2026-10-10)
- *The perceptron: a probabilistic model for information storage and organization in the brain* — F. Rosenblatt, *Psychological Review*, 1958 — copia accesible en <https://www.ling.upenn.edu/courses/cogs501/Rosenblatt1958.pdf> (consultado 2026-10-10)
- *Perceptrons: An Introduction to Computational Geometry* — M. Minsky y S. Papert, MIT Press, 1969 — obra impresa; no se ha encontrado edición abierta (consultado 2026-10-10)
- *Language and Machines: Computers in Translation and Linguistics* (informe ALPAC) — National Academy of Sciences, 1966 — <https://www.mt-archive.net/ALPAC-1966.pdf> (consultado 2026-10-10)
- *Artificial Intelligence: A General Survey* (informe Lighthill) — J. Lighthill, 1973 — <https://www.chilton-computing.org.uk/inf/literature/reports/lighthill_report/p001.htm> (consultado 2026-10-10)
- *Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project* — B. Buchanan y E. Shortliffe (eds.), 1984 — <https://shortliffe.net/Buchanan-Shortliffe-1984/MYCIN%20Book.htm> (consultado 2026-10-10)
- *R1: An Expert in the Computer Systems Domain* — J. McDermott, AAAI 1980 (copia archivada del original; el informe técnico CMU-CS-80-119 es la versión extensa y no tiene edición abierta estable) — <https://web.archive.org/web/20171116060857/http:/aaai.org/Papers/AAAI/1980/AAAI80-076.pdf> (consultado 2026-10-10)
- *Learning from Artificial Intelligence's Previous Awakenings: The History of Expert Systems* — D. C. Brock, *AI Magazine*, 39(3), 2018 — <https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/2809> (consultado 2026-10-10)
- *Learning representations by back-propagating errors* — D. Rumelhart, G. Hinton y R. Williams, *Nature*, vol. 323, 1986 — copia accesible en <https://www.iro.umontreal.ca/~vincentp/ift3395/lectures/backprop_old.pdf> (consultado 2026-10-10)
- *Gradient-Based Learning Applied to Document Recognition* — Y. LeCun, L. Bottou, Y. Bengio y P. Haffner, 1998 — <http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf> (consultado 2026-10-10)
- *The Mathematics of Statistical Machine Translation: Parameter Estimation* — P. Brown y otros, *Computational Linguistics*, 19(2), 1993 — <https://aclanthology.org/J93-2004/> (consultado 2026-10-10)
- *Deep Blue* — IBM (página histórica del fabricante) — <https://www.ibm.com/history/deep-blue> (consultado 2026-10-10)
- *ImageNet Large Scale Visual Recognition Challenge* — O. Russakovsky y otros, 2014 — <https://arxiv.org/abs/1409.0575> (consultado 2026-10-10)
- *ImageNet Classification with Deep Convolutional Neural Networks* — A. Krizhevsky, I. Sutskever y G. Hinton, 2012 — <https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html> (consultado 2026-10-10)
- Comprobación propia — todas las direcciones anteriores devolvieron código 200 en una petición HTTP el 2026-10-10, salvo la obra impresa de Minsky y Papert, para la que no se ha encontrado edición abierta

## Continuar

- Anterior: [Qué es la inteligencia artificial](01-que-es-la-inteligencia-artificial.md)
- Siguiente: [De AlexNet a los agentes: la historia desde 2012](03-historia-desde-2012.md)
- Índice de la etapa: [Etapa 0 — Fundamentos](README.md)
- Índice temático: [`../../INDEX.md`](../../INDEX.md)

---

*Pepe, asistido por IA. Última revisión: 2026-10-10.*
