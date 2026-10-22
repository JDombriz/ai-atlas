---
titulo: Cómo elegir un modelo para una tarea
etapa: 1
orden: 1
pregunta: ¿Cómo se elige, con criterio y con números, el modelo que conviene a una tarea concreta?
prerrequisitos: ["../etapa-0-fundamentos/05-donde-no-hace-falta-ia.md"]
ultima_revision: 2026-10-22
estado: publicado
traduccion_de:
---

# Cómo elegir un modelo para una tarea


<img src="../../assets/bandas/banda-e1-01-es.svg" alt="01" width="560">
> Versión en inglés: [`01-como-elegir-un-modelo.en.md`](01-como-elegir-un-modelo.en.md), traducción de esta revisión.

Un equipo de soporte recibe cuatro mil incidencias al mes y quiere clasificarlas por tipo antes de que las lea nadie. La pregunta que llega es siempre la misma: «¿qué modelo usamos?». La respuesta útil no es un nombre. Es un procedimiento que cabe en una tarde y que, hecho bien, deja además la cuenta del coste hecha.

La misma tarea, con el mismo texto de entrada, cuesta hoy cien veces más en el modelo de frontera que en el más barato del catálogo —10 $ por millón de tokens de entrada frente a 0,10 $— y en la mayoría de las tareas cerradas el resultado no mejora en esa proporción. Elegir por la lista de los más listos es la forma más rápida de multiplicar la factura sin que se note en el resultado.

## La pregunta que se hace primero

Antes de mirar ningún modelo hay una que descarta por sí sola: **¿el texto puede salir de casa?** Si la respuesta es no, la discusión se acaba y quedan dos caminos: un modelo de pesos abiertos ejecutado en infraestructura propia, o no hacer esto con un modelo.

No es una pregunta de cumplimiento normativo abstracto. Un contrato, una historia clínica, el listado de personal o el borrador de una sanción no se pegan en la caja de texto de un servicio que no tiene firmado dónde acaban esos datos. Y «tiene política de privacidad» no es lo mismo que «no los usa para entrenar», que no es lo mismo que «no los conserva treinta días», que no es lo mismo que «se procesan en la Unión Europea». Cada una de esas cuatro frases es una casilla distinta de un contrato distinto.

Cuando la respuesta es sí, o cuando el modelo es de pesos abiertos y corre en casa, se pasa a lo demás.

## Cinco cosas que deciden

**Una. Si el modelo es capaz de la tarea.** No si es bueno en general: si acierta en esta tarea concreta. Un modelo que gana en las clasificaciones públicas puede perder en clasificar incidencias de una empresa de ascensores, porque el vocabulario de esa empresa no está en ninguna prueba pública. La capacidad se mide, no se opina.

**Dos. Cuánto texto tiene que caber.** La ventana de contexto es cuántos tokens ve el modelo de una vez. Un millón de tokens son del orden de 600 000 a 700 000 palabras en castellano: mucho más de lo que hace falta para casi todo, y bastante menos de lo que parece cuando se arrastra una conversación de dos días con documentos pegados. Que la ventana sea enorme no significa que el modelo use bien el centro de un documento de mil páginas: eso se comprueba, no se supone.

**Tres. Cuánto puede esperar quien lo usa.** La latencia no se deduce del precio ni del tamaño con fiabilidad. Se mide en la propia prueba, con la carga real, en la horquilla horaria en la que se va a usar. Un modelo excelente que tarda veinte segundos no sirve para clasificar mientras alguien espera delante de una pantalla.

**Cuatro. Cuánto cuesta cada uso.** Se factura por token, separando entrada y salida, y la salida es la cara. En el catálogo de octubre de 2026, casi todos cobran la salida entre cinco y diez veces más que la entrada; los pequeños, uno a uno. Un cálculo que solo cuenta la entrada se queda corto por un factor de tres o cuatro en respuestas largas.

**Cinco. Qué pasa cuando falla.** Todo modelo falla. La pregunta no es si, sino quién lo detecta y cuánto cuesta. Una clasificación equivocada en un sistema de facturación y otra en un archivo de prensa tienen precios distintos, y ese precio —no el del token— es el que decide en muchos casos.

## El método, en cuatro preguntas

**Primera: ¿qué tiene que salir bien?** Conviene escribirlo antes de probar nada: «el 90 % de las incidencias con la categoría correcta, y ninguna marcada como urgente que no lo sea». Sin ese número, cualquier modelo parece bueno en la primera prueba y ninguno en la tercera.

**Segunda: ¿cuál es el más barato que podría servir?** Se empieza por abajo. En el catálogo, eso significa probar antes un modelo pequeño —Ministral 3 3B o GPT-6 Luna, los dos a 0,10 $ por millón de entrada— que uno de frontera. La razón no es el ahorro: es que si el barato acierta, la decisión está tomada y el resto del tiempo se ahorra. Subir de modelo es fácil; bajar, después de haber montado todo alrededor, no lo es.

**Tercera: ¿cómo se comprueba?** Con un banco de casos propio, pequeño y fijo: diez ejemplos reales con su respuesta esperada, pasados por cada candidato con la misma instrucción. La [receta del banco de diez casos](../../recetas/banco-de-diez-casos.md) lo monta en una tarde y deja, además, la cifra de coste por caso.

**Cuarta: ¿qué pasa si falla?** Si el fallo es caro, el modelo no puede ser el único filtro: hace falta revisión humana, y esa revisión hay que meterla en la cuenta. Un sistema que acierta el 92 % y necesita revisar el 8 % restante es más barato que uno que acierta el 96 % y cuesta el doble por llamada, casi siempre.

## Lo que cuesta cada uno, en octubre de 2026

Precios por millón de tokens, verificados en las páginas de cada fabricante el 2026-10-22. La columna de contexto es la ventana que declara el fabricante.

| Modelo | Entrada | Salida | Contexto | Licencia |
|:--|--:|--:|--:|:--|
| [Claude Fable 5.1](../../catalogo/modelos/claude-fable-5-1.md) | 10 $ | 50 $ | 1 M | propietaria |
| [Claude Opus 5.5](../../catalogo/modelos/claude-opus-5-5.md) | 4 $ | 20 $ | 1 M | propietaria |
| [GPT-6.1 Sol](../../catalogo/modelos/gpt-6-1-sol.md) | 2 $ | 10 $ | 1,05 M | propietaria |
| [Gemini 4 Argon](../../catalogo/modelos/gemini-4-argon.md) | 2 $ | 10 $ | 1,05 M | propietaria |
| [Mistral Large 3](../../catalogo/modelos/mistral-large-3.md) | 0,50 $ | 1,50 $ | — | Apache 2.0 |
| [GPT-6 Luna](../../catalogo/modelos/gpt-6-luna.md) | 0,10 $ | 0,50 $ | 1,05 M | propietaria |
| [Ministral 3 3B](../../catalogo/modelos/ministral-3-3b.md) | 0,10 $ | 0,10 $ | — | Apache 2.0 |
| [Llama 4 Scout](../../catalogo/modelos/llama-4-scout.md) | sin precio de API | — | 10 M | Llama 4 Community |

## La letra pequeña que dobla la factura

Cuatro cosas que no están en el titular y que cambian una decisión.

- **El tramo de contexto largo se paga.** En la API de OpenAI, una petición con más de 272 000 tokens de entrada se factura al doble en entrada y caché, y con la salida un 50 % más cara, en toda la petición. Un contrato de doscientas páginas entra por ahí.
- **El precio puede tener fecha.** Gemini 4 Argon cuesta 2 $ y 10 $ hasta el 30 de noviembre de 2026; a partir del 1 de diciembre, 4 $ y 20 $. Una estimación hecha hoy vale seis semanas.
- **La caché es la palanca grande.** Si el prompt es el mismo en cada llamada —y en un uso repetido casi siempre lo es—, la parte repetida se cobra a una fracción: entre el 5 % y el 10 % de la entrada en los modelos de OpenAI. En un volumen alto, descuidar esto cuesta más que elegir mal el modelo.
- **Los nombres cambian.** Un identificador de modelo concreto —`gpt-6.1-sol`, `claude-opus-5-5`— tiene fecha de retirada que el fabricante anuncia con meses, no con años. La integración hay que escribirla para poder cambiar de modelo sin rehacer el código.

## Los tropiezos de siempre

- **Elegir por la tabla de clasificaciones.** Mide tareas parecidas a la propia, no la propia. Sirve para descartar, no para decidir.
- **Comparar precios de entrada y olvidar la salida.** El error de cuenta más frecuente, y el que más se nota en respuestas largas.
- **Arreglar con otro modelo un problema de instrucción o de contexto.** Si la instrucción es ambigua, el modelo caro también la malinterpreta; solo la malinterpreta con más seguridad. Antes de cambiar de modelo, [la instrucción](02-la-instruccion.md) y [el contexto](03-el-contexto.md).
- **Medir con tres frases y la sensación.** Con tres casos acierta cualquiera; con diez, y con la respuesta esperada escrita, se empieza a ver la diferencia.

## Cuándo no aplica

- **Cuando la tarea es determinista.** Si la regla se puede escribir, la regla gana: es gratis, es auditable y no cambia el martes. El criterio negativo está en [Dónde no hace falta inteligencia artificial](../etapa-0-fundamentos/05-donde-no-hace-falta-ia.md).
- **Cuando no hay forma de comprobar el resultado.** Si nadie puede decir si la respuesta es correcta sin rehacer el trabajo, el modelo no ahorra: traslada el trabajo.
- **Cuando el volumen es enorme y la tarea trivial.** Clasificar dos millones de filas por una palabra clave que ya está en una columna no es un problema de modelos.

## Definiciones

- **Ventana de contexto**: número máximo de tokens que el modelo puede tener en cuenta en una misma petición; incluye instrucción, documentos y respuesta.
- **Token**: unidad de texto con la que se mide y se factura. Regla de bolsillo: en castellano, entre 1,3 y 1,5 tokens por palabra.
- **Precio por millón de tokens**: unidad de facturación de los modelos servidos por API, con tarifas distintas para entrada y salida.
- **Pesos abiertos**: modelo cuyos parámetros se distribuyen con una licencia que permite descargarlos y ejecutarlos en infraestructura propia.
- **Modelo propietario**: modelo al que solo se accede por la API del fabricante, bajo sus condiciones.
- **Banco de casos**: conjunto pequeño y fijo de ejemplos con respuesta esperada, usado para comparar modelos con la misma vara.

## Referencias

- Fichas del catálogo: [Claude Fable 5.1](../../catalogo/modelos/claude-fable-5-1.md), [Claude Opus 5.5](../../catalogo/modelos/claude-opus-5-5.md), [GPT-6.1 Sol](../../catalogo/modelos/gpt-6-1-sol.md), [GPT-6 Luna](../../catalogo/modelos/gpt-6-luna.md), [Gemini 4 Argon](../../catalogo/modelos/gemini-4-argon.md), [Mistral Large 3](../../catalogo/modelos/mistral-large-3.md), [Ministral 3 3B](../../catalogo/modelos/ministral-3-3b.md), [Llama 4 Scout](../../catalogo/modelos/llama-4-scout.md) — cada una con su URL oficial y su fecha de verificación.
- Tarifas: páginas de precios de OpenAI, Anthropic, Google y Mistral — consultadas el 2026-10-22. Las cifras de esta página llevan esa fecha porque caducan.
- Comprobación propia — las ocho páginas de modelo y las cuatro de precios respondieron 200 en una petición HTTP el 2026-10-22. No se ha llamado a ninguna API ni se ha medido latencia: los tiempos hay que medirlos en cada caso.

## Continuar

- Anterior: [El oficio en 2026](../etapa-0-fundamentos/06-el-oficio-en-2026.md)
- Siguiente: [La instrucción: pedir bien y obtener algo usable](02-la-instruccion.md)
- Índice de la etapa: [Etapa 1 — Uso profesional](README.md)
- Índice temático: [`../../INDEX.md`](../../INDEX.md)

---

*Pepe. Última revisión: 2026-10-22.*
