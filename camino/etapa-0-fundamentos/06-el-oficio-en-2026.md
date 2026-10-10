---
titulo: El oficio en 2026
etapa: 0
orden: 6
pregunta: ¿Qué cambia y qué no cambia para quien escribe software, según la evidencia disponible?
prerrequisitos: [01-que-es-la-inteligencia-artificial.md, 04-que-es-y-que-no-es-un-agente.md]
ultima_revision: 2026-10-10
estado: borrador
traduccion_de:
---

# El oficio en 2026

> **Pregunta que resuelve:** ¿qué cambia y qué no cambia para quien escribe software, según la evidencia disponible?

## Para qué sirve

Cierra la etapa respondiendo a lo que más se pregunta quien ya programa: en qué se traduce todo esto en su trabajo diario. La respuesta se separa en tres partes: lo que cambia de forma observable, lo que no cambia y sigue siendo responsabilidad de quien despliega, y lo que la evidencia disponible permite afirmar hoy —que es menos de lo que sugiere el ruido.

Es también la página que fija el punto de partida del resto del camino: si el oficio consistiera solo en escribir código, las etapas siguientes no tendrían sentido. Lo que se desplaza es dónde está el cuello de botella.

## Qué cambia

1. **Escribir la primera versión deja de ser el cuello de botella en tareas acotadas.** Redactar una función, transformar datos, escribir pruebas, traducir código entre lenguajes: el tiempo hasta el primer borrador se reduce de forma clara cuando la tarea tiene un criterio de éxito comprobable.
2. **El límite se desplaza a la revisión y al criterio.** Producir más código del que se puede revisar no es productividad, es inventario. La capacidad de leer, entender y aceptar cambios pasa a determinar el ritmo del equipo.
3. **La especificación gana valor.** Cuanto más precisa es la descripción del resultado esperado, mejor funciona cualquier asistencia. Escribir bien el problema pasa de ser una virtud a ser la palanca principal.
4. **El trabajo se reparte entre quien construye y quien evalúa.** Aparecen funciones que antes no existían con ese nombre: diseñar el conjunto de casos, medir, instrumentar, vigilar el coste y decidir qué se automatiza y qué no.
5. **La deuda cambia de sitio.** Además del código, hay que mantener instrucciones, contextos, permisos, herramientas conectadas y dependencias de proveedor. Nada de eso viaja en el repositorio si no se decide que viaje.
6. **El coste entra en el diseño.** Un sistema que paga por operación tiene una restricción nueva que no existía en el software tradicional, y se gestiona desde el primer día o no se gestiona.

## Qué no cambia

- **Un sistema se juzga por lo que hace.** La calidad de la asistencia no altera el criterio: en producción, lo que cuenta es el comportamiento observable.
- **La responsabilidad es de quien despliega.** Ninguna herramienta firma, aprueba un despliegue ni responde de un incidente. El reparto de permisos sigue siendo una decisión humana y explícita.
- **Seguridad, control de acceso y trazabilidad siguen siendo requisitos previos.** Que el sistema tenga más autonomía agranda el problema; no lo sustituye.
- **Los fundamentos explican los fallos.** Estructuras de datos, redes, bases de datos, concurrencia, sistemas distribuidos: los incidentes de los sistemas con modelos se producen, en su mayoría, en el software de alrededor.
- **La comprensión no se delega.** Quien acepta un cambio que no entiende está asumiendo una deuda que pagará en la siguiente incidencia, con intereses.
- **El juicio profesional no es una opción de configuración.** Decidir qué se hace, con qué datos y con qué límites es el trabajo, no un paso previo al trabajo.

## Qué dice la evidencia disponible

La evidencia es escasa y hay que leerla por su diseño, no por su titular. Tres referencias útiles, todas con su límite:

| Estudio | Qué midió | Resultado | Límite |
|:--|:--|:--|:--|
| Impacto de la asistencia en la productividad, 2023 | Experimento controlado: implementar un servidor HTTP en JavaScript, con y sin asistencia | El grupo con asistencia terminó la tarea un 55,8 % más rápido | Tarea pequeña, aislada y con especificación cerrada; no representa el trabajo habitual |
| Productividad de desarrolladores experimentados en proyectos maduros, 2025 | Ensayo aleatorizado con 16 desarrolladores de código abierto, 246 tareas en repositorios que conocían desde hacía unos cinco años | Permitir la asistencia **aumentó** el tiempo de resolución un 19 %, frente a una previsión de mejora del 20 % expresada por los propios participantes | Muestra pequeña, proyectos maduros con estándares altos, herramientas de principios de 2025 |
| SWE-bench, desde 2023 | Banco de pruebas con más de dos mil incidencias reales de repositorios de código abierto | Mide la proporción de incidencias resueltas de verdad, verificadas por sus propias pruebas | Mide una capacidad concreta, no la utilidad en un equipo ni el coste de mantener el resultado |

Lo que se puede afirmar con estos datos: el rendimiento depende mucho del contexto; en tareas cerradas y verificables la mejora es grande; en proyectos maduros con estándares exigentes y conocimiento previo, la asistencia puede ralentizar. Lo que **no** se puede afirmar: cifras generales de mejora de productividad, ni comparaciones entre herramientas, ni que la tendencia sea estable.

Estudios de industria, como los informes anuales del programa DORA, aportan una visión de conjunto por encuestas y son útiles para situar tendencias, no para decidir sobre un equipo concreto.

## Cómo se trabaja con esto

Un criterio sencillo, aplicable hoy y sin necesidad de herramientas nuevas: **asistencia sí donde el resultado se puede comprobar de forma barata y la acción es reversible.**

| Situación | Asistencia razonable |
|:--|:--|
| Tarea con prueba automática clara | Sí: escribir, refactorizar, ampliar pruebas |
| Documentación, ejemplos, mensajes de error | Sí, con revisión de quien firma el texto |
| Explorar una biblioteca o una interfaz desconocida | Sí: acelera la orientación, que hay que verificar en la documentación oficial |
| Migraciones repetitivas con patrón claro | Sí, por lotes y con comprobación tras cada lote |
| Decisiones de arquitectura o de seguridad | No como decisión: sí como contraste de opciones, con revisión experta |
| Cambios irreversibles en producción | No sin revisión humana y camino de vuelta |
| Código que nadie va a revisar | No: es el caso donde el coste del error no tiene tope |
| Dominios regulados o con datos sensibles | Requiere análisis previo de las condiciones del proveedor y del marco aplicable |

En cualquier caso, el envío de código o de datos a un servicio externo es una decisión de la organización, no del usuario que lo tiene instalado. Conviene saberlo antes de probar, no después.

## Errores frecuentes

- **Medir líneas de código o número de cambios.** Ninguna de las dos cosas mide valor y ambas se pueden inflar sin esfuerzo.
- **Aceptar cambios que no se entienden.** El ahorro de hoy es la incidencia de mañana, y su coste se paga en el momento menos oportuno.
- **Generalizar el resultado de una demostración.** Los estudios con tareas cerradas y los estudios en proyectos maduros apuntan en direcciones distintas: la diferencia está en el contexto, no en la herramienta.
- **Ignorar las condiciones de uso.** Qué se envía, a quién, con qué retención y con qué licencia sobre el resultado son preguntas anteriores a la adopción.
- **Confundir velocidad de producción con velocidad de entrega.** Si la revisión es el cuello de botella, acelerar la escritura solo mueve la cola de espera.
- **Dejar sin registrar lo que hizo el sistema.** Sin traza no se puede reconstruir por qué cambió algo, ni corregir el proceso.

## Cuándo no aplica

Esta página describe el oficio, no las herramientas del día: la elección de modelos concretos, con sus precios y límites, es materia de la Etapa 1 (Uso profesional, en preparación); el diseño de flujos con estado, de la Etapa 2 (Ingeniería, en preparación); y la operación, la evaluación y el control del gasto, de la Etapa 4 (Producción, en preparación).

Tampoco pretende predecir el futuro próximo. Los años recientes desaconsejan cualquier extrapolación: casi todos los pronósticos cuantitativos de los últimos cuatro años se han quedado cortos o largos en poco tiempo.

## Definiciones

- **Asistencia al código**: uso de un modelo que propone cambios que una persona revisa antes de incorporarlos.
- **Evaluación por casos**: conjunto de casos definidos antes de conocer el resultado, con su criterio de aceptación.
- **Deuda de configuración**: mantenimiento acumulado en instrucciones, contextos, permisos y herramientas conectadas de un sistema con modelos.
- **Traza de ejecución**: registro ordenado de lo que hizo el sistema y con qué resultado, necesario para reconstruir una incidencia.
- **Revisión humana**: paso en el que una persona acepta, corrige o rechaza el resultado de un sistema antes de que tenga consecuencias.
- **Coste de revisión**: tiempo y esfuerzo de comprobar los resultados; se suma al coste de producirlos y a menudo lo supera.

## Referencias

- *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot* — S. Peng, E. Kalliamvakou, P. Cihon y M. Demirer, 2023 — <https://arxiv.org/abs/2302.06590> (consultado 2026-10-10)
- *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* — J. Becker y otros (METR), 2025 — <https://arxiv.org/abs/2507.09089> (consultado 2026-10-10)
- *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* — C. Jimenez y otros, 2023 — <https://arxiv.org/abs/2310.06770> (consultado 2026-10-10)
- *DORA — investigación anual sobre rendimiento en entrega de software* — Google Cloud (informes por encuesta; no equivalen a un experimento controlado) — <https://dora.dev/research/> (consultado 2026-10-10)
- *Artificial Intelligence Risk Management Framework (AI RMF 1.0)* — NIST, 2023 — <https://doi.org/10.6028/NIST.AI.100-1> (consultado 2026-10-10)
- Comprobación propia — las direcciones anteriores devolvieron código 200 en una petición HTTP el 2026-10-10

## Continuar

- Anterior: [Dónde no hace falta inteligencia artificial](05-donde-no-hace-falta-ia.md)
- Siguiente: [Práctica de la etapa: análisis de tres procesos propios](practica.md)
- Índice de la etapa: [Etapa 0 — Fundamentos](README.md)
- Índice temático: [`../../INDEX.md`](../../INDEX.md)