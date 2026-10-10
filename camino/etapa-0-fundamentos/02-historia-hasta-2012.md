---
titulo: De Turing a AlexNet — la historia hasta 2012
etapa: 0
orden: 2
pregunta: ¿De dónde viene la inteligencia artificial y qué consecuencia técnica dejó cada hito anterior a 2012?
prerrequisitos: [01-que-es-la-inteligencia-artificial.md]
ultima_revision: 2026-10-10
estado: borrador
traduccion_de:
---

# De Turing a AlexNet: la historia hasta 2012

> **Pregunta que resuelve:** ¿de dónde viene la inteligencia artificial y qué consecuencia técnica dejó cada hito anterior a 2012?

## Para qué sirve

Los errores de hoy se explican por decisiones tomadas hace décadas. Casi todos los debates que se repiten —si conviene codificar el conocimiento o aprenderlo de los datos, si el cómputo basta o hace falta la estructura, por qué la financiación llega y se retira— ya se dieron entonces, y se resolvieron de una manera concreta por razones que conviene conocer.

Esta página recorre la historia **por sus consecuencias**: qué cambió en la práctica después de cada hito y qué dejó de ser necesario. Los inviernos, en este relato, cuentan tanto como los veranos. La continuación —de 2012 hasta hoy— está en la [página siguiente](03-historia-desde-2012.md); el corte no es una comodidad de paginación, sino el punto en el que cambia la forma de trabajar.

## Los hitos, con su consecuencia

### 1950 · Turing plantea la pregunta de forma operativa

*Computing Machinery and Intelligence* sustituye «¿puede pensar una máquina?» por un juego de imitación: un interrogador conversa por escrito con dos interlocutores y debe distinguir cuál es la máquina. El artículo no propone una máquina, sino un criterio observable y una discusión de las objeciones. Al final apunta la idea que más recorrido tendría: en lugar de simular la mente adulta, puede ser más eficaz simular la de un niño y educarla.

**Consecuencia.** El problema se vuelve comprobable y, de paso, se admite que programar la experiencia podría ser más viable que programar el conocimiento. Tardaría cuarenta años en demostrarse.

### 1955–1956 · Dartmouth: nace el nombre

La propuesta del taller de verano de Dartmouth, firmada por McCarthy, Minsky, Rochester y Shannon, usa por primera vez la expresión *artificial intelligence* y formula una conjetura fuerte: que todo aspecto del aprendizaje puede describirse con tal precisión que una máquina llegue a simularlo. Al taller asistieron unas diez personas.

**Consecuencia.** Se acuña el término —en una propuesta de taller, no en un artículo de revista— y con él una expectativa: se daba por hecho que el problema era de escala de un verano de trabajo.

### 1958 · Rosenblatt y el perceptrón

El perceptrón aprende a clasificar a partir de ejemplos, con una regla de actualización sencilla aplicada a una sola capa de unidades. Se construyó también en hardware.

**Consecuencia.** Aparece la alternativa al conocimiento escrito: en lugar de reglas, ejemplos y un procedimiento de ajuste. Es la primera formulación operativa del aprendizaje automático.

### 1966 · El informe ALPAC

Un comité estadounidense evalúa los programas de traducción automática de la época y concluye que no alcanzan a la traducción humana ni en calidad ni en coste. La financiación del área se recorta.

**Consecuencia.** Primera demostración de que el dinero sigue a los resultados demostrables, y no a la promesa. También deja un prejuicio que costaría décadas deshacer: «la traducción automática no funciona».

### 1969 · La crítica que frenó una línea entera

*Perceptrons*, de Minsky y Papert, demuestra los límites de las redes de una sola capa: hay funciones que no pueden representar, y el ejemplo clásico es la disyunción exclusiva. El libro es exacto en lo que afirma y la lectura que se hizo de él fue más amplia de lo que decía: se concluyó que añadir capas no servía, cuando lo que faltaba era un método para entrenarlas.

**Consecuencia.** La línea conexionista pierde financiación durante casi dos décadas y el esfuerzo se desplaza a los sistemas simbólicos. La conclusión era falsa; el teorema, cierto.

### 1965–1972 · DENDRAL: el conocimiento, escrito a mano

En Stanford, el proyecto DENDRAL codifica las restricciones de la espectrometría de masas para proponer estructuras químicas, y su continuación Meta-DENDRAL aprende reglas a partir de datos. Es el primer sistema experto en el sentido moderno.

**Consecuencia.** Se establece la tesis que domina los veinte años siguientes: el cuello de botella no es el razonamiento, es el conocimiento. Y si hay que escribirlo, escribirlo es caro.

### 1973 · El informe Lighthill y el primer invierno

El informe encargado por el Reino Unido concluye que la inteligencia artificial no había cumplido lo prometido y que no había base para sostener el gasto. La financiación británica del área se reduce drásticamente y buena parte de la investigación se reorienta.

**Consecuencia.** El primer «invierno»: entre 1974 y 1980 la financiación se contrae, los grupos se disuelven y el término se vuelve incómodo en los presupuestos. La causa no fue la falta de ideas, sino la distancia entre lo prometido y lo entregado.

### 1976 · MYCIN y el problema de la incertidumbre

MYCIN, también en Stanford, asesora sobre terapia antimicrobiana con varios centenares de reglas que incorporan factores de certeza. En las evaluaciones publicadas su comportamiento es comparable al de los especialistas en los casos seleccionados. Nunca llegó al uso clínico rutinario.

**Consecuencia.** Dos lecciones duraderas: el razonamiento con incertidumbre es tratable, y un sistema que acierta no basta. Faltaban la integración con los sistemas del hospital, un responsable legal y, sobre todo, un modo sostenible de mantener el conocimiento al día. Es el primer caso claro de un problema que hoy se llama, con otro nombre, evaluación y operación.

### 1978–1980 · XCON: los sistemas expertos entran en la industria

En Digital Equipment Corporation, el sistema R1 —luego XCON— configura pedidos de sistemas VAX: comprueba compatibilidades y produce la lista de componentes. Se puso en explotación y la compañía sostuvo un departamento propio de ingeniería del conocimiento para mantenerlo.

**Consecuencia.** El conocimiento experto pasa de ser un objeto de investigación a un activo comercial, y arranca el ciclo de los años ochenta: auge comercial, empresas de herramientas expertas y grandes expectativas. El ciclo se rompió por una razón económica y no técnica: las bases de reglas crecieron hasta miles de reglas, cada cambio obligaba a revisar el conjunto, y las líneas de producto cambiaban más rápido de lo que el conocimiento se podía mantener. Las cifras de ahorro que se citan de aquella época proceden de testimonios y de la propia empresa, no de cuentas públicas auditables.

### 1986 · La retropropagación devuelve el aprendizaje al centro

Rumelhart, Hinton y Williams publican el método para ajustar los pesos de redes con capas intermedias, calculando la contribución de cada peso al error final. El algoritmo era conocido en otras disciplinas; lo que faltaba era mostrarlo funcionando en redes útiles.

**Consecuencia.** El obstáculo de 1969 desaparece. Las redes multicapa vuelven a la investigación con fundamento, aunque sin datos ni cómputo suficientes para competir con los sistemas simbólicos en problemas reales.

### 1989–1998 · Las redes convolucionales y una tarea resuelta

La familia LeNet reconoce dígitos manuscritos con una arquitectura que explota la estructura de la imagen —convoluciones y reducción de resolución— en lugar de tratar cada píxel por separado. Llegó a usarse en la lectura automática de cheques en Estados Unidos.

**Consecuencia.** Queda demostrado que ciertos problemas de percepción se resuelven mejor aprendiendo de los datos que con reglas. El método, sin embargo, no escala con el volumen de datos y de cómputo disponible entonces: la misma arquitectura, con veinte años más de datos y procesadores gráficos, sería la que ganó en 2012.

### 1993 · La traducción estadística: los datos ganan a las reglas

Los modelos de traducción de IBM estiman, a partir de corpus paralelos, la probabilidad de que una frase en un idioma corresponda a otra. Sin gramáticas escritas a mano y sin conocimiento lingüístico explícito, superan a los sistemas de reglas.

**Consecuencia.** El giro estadístico se generaliza en la industria: buscadores, filtros de correo y reconocimiento de voz pasan a construirse sobre datos. La lección se repetiría después: cuando hay datos suficientes, el método que los aprovecha desplaza al que codifica el conocimiento a mano.

### 1997 · Deep Blue: fuerza bruta, no aprendizaje

El sistema de IBM gana a Garri Kaspárov evaluando posiciones con una función escrita por expertos y explorando millones de jugadas por segundo. No hay aprendizaje en juego.

**Consecuencia.** La victoria mostró el valor del diseño específico y del cómputo masivo, y también su límite: el resultado no se transfirió a ningún otro problema. Ese patrón —hito espectacular, transferencia nula— se repite en cada década, y conviene recordarlo cada vez que aparece uno nuevo.

### 2009–2012 · ImageNet, las tarjetas gráficas y el corte

El conjunto de datos ImageNet reúne millones de imágenes etiquetadas y, desde 2010, un concurso anual compara sistemas sobre la misma tarea. En 2012, la red de Krizhevsky, Sutskever y Hinton reduce el error del mejor sistema anterior de forma abrupta: 15,3 % de error frente al 26,2 % del segundo clasificado. El trabajo se apoyó en tarjetas gráficas —dos unidades de consumo, adaptadas para el cálculo matricial— y en decisiones de arquitectura como la función de activación ReLU y el abandono de unidades.

**Consecuencia.** Coinciden por primera vez tres cosas: datos etiquetados a escala, cómputo barato y paralelo, y una arquitectura entrenable en profundidad. A partir de ahí, la ingeniería de características deja de ser el oficio principal en visión por computador: las representaciones se aprenden. El corte de esta página está aquí porque, desde 2012, la discusión sobre qué codificar a mano pierde peso en casi todos los frentes.

## Errores frecuentes

- **Contar la historia como una línea ascendente.** Los inviernos tuvieron causas concretas y no fueron simples pausas: cambiaron qué se financiaba y qué se investigaba.
- **Atribuir el avance de 2012 a una idea nueva.** Las convoluciones y las redes multicapa existían desde hacía décadas. Lo que cambió fue la disponibilidad de datos y de cómputo.
- **Dar los sistemas expertos por fracasados técnicamente.** Cumplían su tarea; lo que no resistió fue la economía de mantener el conocimiento escrito a mano.
- **Confundir Deep Blue con aprendizaje.** Fue búsqueda y evaluación escritas por personas. La distinción importa para saber qué se puede esperar de cada enfoque.
- **Leer el informe Lighthill como un error de apreciación.** Su diagnóstico sobre la distancia entre promesa y entrega era razonable; el error de la época fue prometer resultados por delante de la evidencia.

## Cuándo no aplica

Esta página no explica las técnicas en uso ni sirve para elegir una herramienta: eso empieza en la [página 3](03-historia-desde-2012.md) y sigue en las etapas 1 a 4. Tampoco es una historia institucional ni de personas: los hitos se citan por su efecto técnico, no por sus protagonistas ni por la épica de sus entornos. Y no sustituye a la lectura de las fuentes: quien vaya a citar cualquiera de estos episodios debería acudir a la referencia correspondiente, todas ellas accesibles.

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