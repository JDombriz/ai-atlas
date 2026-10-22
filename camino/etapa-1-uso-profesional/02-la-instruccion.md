---
titulo: La instrucción: pedir bien y obtener algo usable
etapa: 1
orden: 2
pregunta: ¿Qué tiene una instrucción para que la respuesta se pueda usar tal cual, y qué le falta a la que no?
prerrequisitos: ["01-como-elegir-un-modelo.md"]
ultima_revision: 2026-10-22
estado: borrador
traduccion_de:
---

# La instrucción: pedir bien y obtener algo usable


<img src="../../assets/bandas/banda-e1-02-es.svg" alt="02" width="560">
> Versión en inglés: [`02-la-instruccion.en.md`](02-la-instruccion.en.md), traducción de esta revisión.

Un equipo pide resumir cuarenta contratos de proveedor y quedarse con lo que obliga. El resumen vuelve impecable: tres párrafos por contrato, bien escritos, con las partes, el objeto y el importe. Nadie se da cuenta hasta la auditoría de que el modelo no ha escrito ni una línea sobre la cláusula de penalización por retraso, que es exactamente lo que había que encontrar.

No falló el modelo. Falló la petición: se pidió «un resumen» y se obtuvo un resumen. Un resumen pone lo que parece importante; para encontrar una cláusula hay que preguntar por la cláusula, decir dónde buscarla, exigir la cita y pedir un formato que se pueda revisar de un vistazo.

## Lo que el modelo ve cuando se le pide algo

En una llamada por API, el modelo no recuerda nada de la vez anterior. Recibe un texto —la instrucción, los documentos, el historial que se le pase— y devuelve una continuación probable de ese texto. Todo lo que se quiera que tenga en cuenta tiene que estar ahí dentro. Nada de lo que no esté, existe.

De ahí una consecuencia práctica que ahorra discusiones: la instrucción **es** el programa. Si se cambia una palabra y el resultado empeora, no es magia ni aleatoriedad: es que se ha cambiado el programa y había que probarlo otra vez.

## Las cinco partes de una instrucción que funciona

**Contexto.** Qué es este texto y para qué se usa la respuesta. «Eres el asistente de un servicio de compras; los documentos que siguen son contratos de proveedor en vigor» orienta más que cualquier adjetivo sobre el tono.

**Tarea.** Una sola, en imperativo, con el verbo preciso. «Extrae» no es «analiza»; «enumera» no es «resume». Si la tarea tiene dos partes, van en dos llamadas: es más barato que una instrucción que hace dos cosas mal.

**Formato de salida.** Cómo se quiere la respuesta: una tabla con estas columnas, una línea por incidencia con este separador, un JSON con estas claves. Es la parte que más se olvida y la que más tiempo ahorra, porque convierte la respuesta en algo que se puede revisar, ordenar o meter en un proceso.

**Un ejemplo.** Uno solo, del tamaño justo: una entrada y la salida que se considera correcta. Vale más que tres párrafos describiendo lo mismo, sobre todo en tareas de formato. Dos o tres ejemplos mejoran el resultado en clasificación; veinte suelen empeorarlo, porque gastan contexto y confunden.

**Criterio de aceptación.** La frase que permite decidir si la respuesta vale: «si el contrato no menciona penalizaciones, escribe ‹no consta›; no lo deduzcas». Sin criterio, el modelo rellena el hueco con lo que suena plausible, que es justo lo que no se puede usar.

## El orden importa

Lo estable primero —el papel que hace el modelo, las reglas, el formato— y al final lo que cambia en cada llamada: el documento, la incidencia, la pregunta. Hay dos razones: la atención se concentra en lo último que se lee y, en los modelos que facturan caché, un prefijo idéntico se cobra a una fracción. Ordenar la instrucción con lo fijo delante abarata el uso repetido sin tocar el resultado.

## Un antes y un después

La misma tarea, dos peticiones. La primera es la que se escribe con prisa y la que produce el resumen inútil del principio.

> Resume este contrato y dime lo importante.

La segunda tarda un minuto más en escribirse y devuelve algo revisable.

> Eres el asistente de un servicio de compras. El texto que sigue es un contrato de proveedor en vigor.
>
> Extrae solo tres cosas: plazo de entrega comprometido, penalización por retraso (importe o porcentaje) y condiciones de renovación. Para cada una, cita el artículo y reproduce la frase literal.
>
> Formato: una tabla de tres filas con las columnas «Dato | Artículo | Frase literal». Si un dato no aparece, escribe «no consta» en la columna del artículo. No deduzcas ni completes con lo que suele ser habitual.
>
> Ejemplo de fila: `Penalización por retraso | Art. 7.2 | «...»`

Lo que ha cambiado no es la cortesía: son cuatro decisiones —una tarea acotada, un formato, un caso de ejemplo y un criterio para el hueco— y una prohibición explícita de inventar.

## Lo que se fija una vez y lo que se pide cada vez

Casi todos los proveedores separan dos mensajes: uno de sistema, que define el papel y las reglas y se mantiene igual, y otro de usuario, donde va lo que cambia. La separación tiene tres ventajas concretas: el prefijo fijo se puede cachear, las reglas no se olvidan al tercer turno y el texto variable queda limpio para registrarlo en los logs.

Lo que va en el fijo: papel, límites —qué no debe hacer—, formato por defecto y criterio de aceptación. Lo que va en el variable: el documento, la pregunta, los datos del caso. Y una regla de higiene: en el mensaje variable nunca se pega una instrucción que contradiga la fija. Cuando se contradicen, gana la última que se lee, y eso convierte un sistema en una lotería.

## La longitud no es virtud

Una instrucción de cuarenta líneas no se mantiene: nadie recuerda por qué está cada frase y se toca a ciegas. Ocho o doce líneas cubren la mayoría de las tareas de oficina, y si hace falta más, casi siempre es señal de que hay dos tareas mezcladas. La instrucción larga tiene además un coste oculto: se paga en cada llamada y ocupa contexto que se necesita para el documento.

## Los tropiezos de siempre

- **Pedir «tono profesional» y creer que eso es una instrucción.** No cambia el contenido, que es lo que suele estar mal.
- **No decir el formato y quejarse después del formato.** Si la respuesta va a una hoja de cálculo, hay que pedir la hoja, no un párrafo correcto.
- **Cambiar dos cosas a la vez.** Cuando empeora, ya no se sabe cuál fue. Una variable por prueba.
- **Confundir detalle con longitud.** Un dato exacto en la instrucción vale más que cinco adjetivos.

## Cuándo no aplica

- **Si el dato no está en el texto, la instrucción no lo crea.** Pedir «busca la penalización» en un contrato que no la tiene solo produce una invención bien redactada. Ese es el terreno de los límites del modelo, que cierra la etapa con su página 5.
- **Si la tarea es determinista**, una regla o una consulta hacen el trabajo sin coste por llamada y sin variación entre ejecuciones.
- **Si el modelo es pequeño y la instrucción larga**, no la va a seguir: los modelos de tres mil millones de parámetros responden bien a formatos cortos y ejemplos, y mal a reglas numeradas en competencia.

## Definiciones

- **Instrucción de sistema**: mensaje que fija papel, reglas y formato, y que se mantiene igual entre llamadas.
- **Formato de salida**: la forma exigida a la respuesta —tabla, JSON, lista con separador— para que se pueda usar sin reescribirla.
- **Criterio de aceptación**: la condición que permite decidir si la respuesta sirve; incluye qué hacer cuando falta un dato.
- **Ejemplo (uno o pocos disparos)**: par de entrada y salida correcta incluido en la instrucción para fijar formato y criterio.

## Referencias

- *Building effective agents* — Anthropic, 2024 — <https://www.anthropic.com/engineering/building-effective-agents> (consultado 2026-10-22). Se cita por su criterio de empezar por lo simple; es documentación de un fabricante, no una fuente neutral.
- [Ministral 3 3B](../../catalogo/modelos/ministral-3-3b.md) — ficha del catálogo, para el límite de los modelos pequeños ante instrucciones largas.
- Comprobación propia — las dos direcciones de esta página respondieron 200 en una petición HTTP el 2026-10-22. El método de las cinco partes no se apoya en una fuente única: es práctica de oficio, y lo que se puede comprobar es el resultado, con el [banco de diez casos](../../recetas/banco-de-diez-casos.md).

## Continuar

- Anterior: [Cómo elegir un modelo para una tarea](01-como-elegir-un-modelo.md)
- Siguiente: [El contexto: qué se le da y en qué orden](03-el-contexto.md)
- Índice de la etapa: [Etapa 1 — Uso profesional](README.md)
- Índice temático: [`../../INDEX.md`](../../INDEX.md)

---

*Pepe. Última revisión: 2026-10-22.*
