---
titulo: El contexto: qué se le da y en qué orden
etapa: 1
orden: 3
pregunta: Si el modelo no recuerda, ¿qué se le entrega en cada llamada, cuánto y en qué orden?
prerrequisitos: ["02-la-instruccion.md"]
ultima_revision: 2026-10-22
estado: publicado
traduccion_de:
---

# El contexto: qué se le da y en qué orden


<img src="../../assets/bandas/banda-e1-03-es.svg" alt="03" width="560">
> Versión en inglés: [`03-el-contexto.en.md`](03-el-contexto.en.md), traducción de esta revisión.

Hay una conversación que todo el mundo ha tenido. Se lleva media hora explicando un asunto al asistente, con matices, cifras y una decisión tomada a mitad; al volver por la tarde, la respuesta ignora media conversación. La reacción natural es «se le ha olvidado». La explicación real es más incómoda y más útil: **nunca lo supo de memoria**. En cada llamada se le entrega un texto, y ese texto tiene un tope.

Entender esto cambia la forma de trabajar. Deja de ser una cuestión de confianza y pasa a ser una cuestión de aritmética y de orden: qué entra, cuánto ocupa y qué se deja fuera.

## Lo que el modelo ve en cada llamada

En una llamada por API no hay memoria. El modelo recibe un texto compuesto —instrucción de sistema, historial, documentos, pregunta— y devuelve una continuación. La conversación que se ve en pantalla es un montaje que hace la aplicación: reenvía lo anterior en cada turno, entero o recortado.

Por eso dos productos con el mismo modelo se comportan de forma distinta ante la misma conversación larga: uno recorta lo más antiguo, otro resume cuando se llena, otro no hace nada y falla. El comportamiento no está en el modelo; está en lo que la aplicación decide meter en la ventana.

## El contexto es un presupuesto

La ventana de contexto se declara en tokens y varía mucho: 1,05 millones en GPT-6.1 Sol, 1,05 en Gemini 4 Argon, 10 millones en Llama 4 Scout. En castellano, un millón de tokens son del orden de 600 000 a 700 000 palabras.

Tres consecuencias que se olvidan:

- **Se paga.** Todo lo que se envía se factura como entrada, se use o no. Pegar el contrato entero de doscientas páginas para preguntar por una fecha cuesta lo mismo que leer el contrato entero, y a veces más: por encima de 272 000 tokens de entrada, la API de OpenAI factura el doble en toda la petición.
- **Se degrada.** Que la ventana admita un millón de tokens no significa que el modelo use bien el centro de un millón de tokens. La información que queda en medio de un texto muy largo se aprovecha peor que la del principio y la del final. El dato que importa conviene tenerlo cerca de la pregunta.
- **Desplaza.** Cada párrafo que se pega ocupa sitio que se necesita para otra cosa. Un contexto lleno de historia antigua deja fuera el documento de hoy.

## Qué entra y qué se queda fuera

El orden de prioridad que funciona en la práctica, de lo que más aporta a lo que menos:

1. **La instrucción y las reglas.** Siempre, y siempre igual, para poder cachearlas.
2. **Los datos del caso.** El documento, el registro, la incidencia, el fragmento concreto.
3. **Lo que se decidió antes y sigue vigente.** Dos líneas, no veinte: «el cliente aceptó el plazo del 15 de marzo; el resto sigue abierto».
4. **El ejemplo de formato.** Uno, corto.
5. **La conversación anterior.** Última y recortada. Casi siempre se puede sustituir por el punto 3 escrito a mano, y sale mejor.

Lo que se queda fuera sin remordimiento: las cortesías, las respuestas del modelo que no aportaron, el «¿puedes repetirlo?», las versiones antiguas del documento y todo lo que ya está resumido en el punto 3.

## El orden: lo estable delante, lo que cambia al final

Un prefijo idéntico en cada llamada se puede cachear y se cobra a una fracción —entre el 5 % y el 10 % de la entrada en los modelos de OpenAI—. Eso impone una disciplina que además mejora el resultado: **papel, reglas y formato primero; documento y pregunta después**. La parte que cambia, al final, donde el modelo la tiene más cerca.

## Documentos largos: cuatro maneras, y lo que cuesta cada una

- **Pegarlo entero**, si cabe en la ventana. Es lo más simple y lo más caro por llamada; tiene sentido si el documento se lee una vez.
- **Trocearlo por secciones** y hacer una llamada por trozo, juntando después. Cuesta varias llamadas, cada una pequeña, y exige una instrucción que devuelva un formato fijo para poder unir los resultados.
- **Buscar el fragmento y citarlo.** Se localiza el párrafo —con una búsqueda por palabra o por similitud— y se le pasa solo eso, con su referencia. Es lo que hace un sistema de recuperación, y pertenece a la Etapa 2; a mano, con dos ficheros y un buscador, ya resuelve la mitad de los casos.
- **Resumir en dos pasos.** Un primer pase que extrae lo relevante de cada trozo y un segundo que trabaja sobre esas extracciones. Barato y fiel si la extracción es literal; peligroso si el primer pase resume de memoria, porque el error se arrastra y ya no se puede comprobar contra el original.

La decisión entre las cuatro no es de gusto: se calcula. Tokens del documento por llamada, multiplicado por el precio de entrada, frente al coste de trocear y unir.

## Por qué «olvida» a mitad de conversación

Tres causas distintas que se confunden en una:

- **El recorte.** La aplicación descarta los mensajes más antiguos cuando la ventana se llena. Lo que se dijo al principio desaparece sin avisar.
- **El resumen automático.** Algunos asistentes comprimen la conversación cuando se llena. Ese resumen lo hace otro modelo y pierde exactamente lo que consideró secundario: importes, condiciones, excepciones.
- **La dilución.** Aun cabiendo todo, la información del centro de un texto muy largo se aprovecha peor.

Las tres se combaten igual: si algo importa, no se deja a la memoria de la conversación. Se escribe en el punto 3 de la lista anterior, en dos líneas, y se reenvía.

## Cuándo empezar de cero

Empezar una conversación nueva y volver a pegar lo que hace falta es más barato que seguir, en tres casos:

- **Cuando la conversación se ha llenado** de intentos fallidos. Arrastrarlos cuesta dinero y confunde: el modelo ve sus propios errores como contexto.
- **Cuando se cambia de tarea.** Un contexto que mezcla dos asuntos produce respuestas que mezclan los dos.
- **Cuando el resultado se ha vuelto raro sin causa aparente.** Casi siempre es un contexto saturado de versiones antiguas; una llamada limpia lo confirma en diez segundos.

Lo que hay que llevarse a la conversación nueva es un párrafo: estado actual, decisiones tomadas, datos que siguen vigentes. Escribirlo a mano cuesta dos minutos y ahorra una tarde.

## Los tropiezos de siempre

- **Pegar todo «por si acaso».** Cuesta, desplaza y empeora el foco. El contexto no es un archivo: es lo que se le entrega a alguien que va a leerlo una vez.
- **Confiar en que la conversación recuerda.** Lo que no se reenvía, no existe; y lo que se reenvía recortado, existe a medias.
- **Ordenar al revés.** Poner el documento delante y las reglas detrás es lo más habitual y lo que peor funciona: además de perder la caché, deja las reglas lejos de la pregunta.
- **Arreglar con un modelo más grande un problema de contexto.** Si falta el dato, no hay ventana que lo resuelva.

## Cuándo no aplica

- **Si la tarea cabe en un párrafo**, esta página sobra: se pega el párrafo y se pregunta.
- **Si el problema es la instrucción**, ningún orden de contexto lo arregla: ver [La instrucción](02-la-instruccion.md).
- **Si hace falta recordar entre sesiones** —preferencias, históricos, documentos que cambian—, eso es memoria persistente y recuperación, y es materia de la Etapa 2.

## Definiciones

- **Contexto**: todo el texto que se entrega al modelo en una llamada: instrucción, historial, documentos y pregunta.
- **Presupuesto de contexto**: el reparto del espacio disponible entre esas partes, con su coste en tokens.
- **Caché de prompt**: descuento que aplica el proveedor cuando el prefijo de la petición es idéntico al de la anterior.
- **Recorte**: descarte de los mensajes más antiguos cuando la conversación excede la ventana.
- **Recuperación**: localizar el fragmento relevante antes de llamar al modelo, en lugar de enviarle todo el documento.

## Referencias

- [GPT-6.1 Sol](../../catalogo/modelos/gpt-6-1-sol.md), [Gemini 4 Argon](../../catalogo/modelos/gemini-4-argon.md) y [Llama 4 Scout](../../catalogo/modelos/llama-4-scout.md) — fichas del catálogo con la ventana de contexto declarada por cada fabricante, verificadas el 2026-10-22.
- Tarifas y regla de los 272 000 tokens: tabla de precios de OpenAI — <https://developers.openai.com/api/docs/pricing> (consultado 2026-10-22).
- Comprobación propia — las direcciones de esta página respondieron 200 en una petición HTTP el 2026-10-22. Las cifras de ventana son las que declara cada fabricante; el uso efectivo de un contexto muy largo no se ha medido en esta página y conviene medirlo en la propia tarea.

## Continuar

- Anterior: [La instrucción: pedir bien y obtener algo usable](02-la-instruccion.md)
- Siguiente: El coste de un uso repetido — *en preparación*
- Índice de la etapa: [Etapa 1 — Uso profesional](README.md)
- Índice temático: [`../../INDEX.md`](../../INDEX.md)

---

*Pepe. Última revisión: 2026-10-22.*
