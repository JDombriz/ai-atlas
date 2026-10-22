---
titulo: Montar un banco de diez casos antes de elegir modelo
cuando: Hay que decidir entre dos o más modelos, o comprobar si el que ya se usa sigue sirviendo
etapa_relacionada: 1
tiempo_estimado: 2-3 h
ultima_revision: 2026-10-22
estado: borrador
---

# Receta: montar un banco de diez casos antes de elegir modelo

> **Cuándo usarla:** cuando hay que decidir con qué modelo se hace una tarea repetida, o cuando alguien pregunta «¿esto lo hace bien la IA?» y la conversación empieza a apoyarse en impresiones.
> Versión en inglés: [`banco-de-diez-casos.en.md`](banco-de-diez-casos.en.md), traducción de esta revisión.

## Supuestos

- Existe una tarea concreta que se repite: clasificar incidencias, extraer tres datos de un contrato, redactar la respuesta de un aviso.
- Hay al menos diez casos reales disponibles, con su resultado correcto conocido. Diez es el mínimo; veinte es mejor y treinta ya no aporta.
- Se tiene acceso a la API o a la interfaz de dos modelos como mínimo, y una hoja de cálculo o veinte líneas de Python.
- La tarea no es determinista: si se resuelve con una regla, [no hace falta este banco ni el modelo](../camino/etapa-0-fundamentos/05-donde-no-hace-falta-ia.md).

## Pasos

1. **Reunir diez casos reales, no inventados.** Se toman de la cola de verdad, preferiblemente los aburridos y los que dieron problemas. Un banco de casos fáciles mide lo que ya se sabía.
2. **Escribir la respuesta correcta de cada uno, a mano, antes de probar nada.** Quien conoce la tarea la escribe; si hay discusión sobre cuál es la respuesta correcta, ese caso no entra en el banco todavía. Este paso es el que casi nadie hace y es el que convierte el ejercicio en una prueba.
3. **Fijar el criterio de aceptación por caso, binario.** Correcto o incorrecto, sin notas del uno al diez: con tres modelos y diez casos, las notas intermedias solo generan discusión. Si un caso admite dos respuestas válidas, se anota cuáles.
4. **Congelar la instrucción y el formato.** La misma instrucción, palabra por palabra, para todos los modelos, con su formato de salida y su criterio de «no consta». Si se cambia la instrucción entre modelos, la prueba ya no compara modelos: compara instrucciones. Ver [La instrucción](../camino/etapa-1-uso-profesional/02-la-instruccion.md).
5. **Empezar por el más barato.** Se pasa primero el modelo pequeño —Ministral 3 3B o GPT-6 Luna, los dos a 0,10 $ por millón de entrada— y después los demás, en orden de precio. Las diez respuestas de cada uno se guardan tal cual, sin corregirlas.
6. **Registrar cuatro columnas por ejecución:** aciertos sobre diez, tiempo de la llamada, tokens de entrada y tokens de salida. El coste se calcula después; los tokens hay que apuntarlos porque el proveedor los cobra aunque no se miren.
7. **Calcular el coste por caso y por mil casos.** Entrada por su precio, salida por el suyo —que suele ser entre cinco y diez veces más caro— y, si el caso lo pide, el tramo de contexto largo. El resultado se escribe en la misma tabla que los aciertos, no en otra hoja.
8. **Decidir con la regla escrita de antemano.** Noventa por ciento o más de aciertos en el barato: no se sube de modelo. Menos del ochenta: se sube. Entre ochenta y noventa: decide el coste del error, no la media. La regla se escribe antes de ver los resultados, porque después siempre hay una razón para ajustarla.
9. **Anotar la fecha y la versión exacta del modelo probado.** Los identificadores cambian y las versiones se retiran: un banco sin fecha es un banco que hay que repetir sin saberlo.

## Cómo saber que ha salido bien

El banco ha servido si produce una tabla de dos filas y tres columnas: modelo, aciertos sobre diez, coste por mil casos. Y si esa tabla permite responder en una frase a la pregunta del principio, con un número dentro: «con el modelo pequeño se acierta el 90 % y mil casos cuestan 2,40 €; con el grande, el 93 % y 240 €».

Si no hay un número en la frase, no hay decisión: hay preferencia.

## Cuándo no hacer esto

- **Con menos de diez casos reales.** Con tres, cualquier modelo acierta; con diez empieza a verse la diferencia y con veinte se estabiliza.
- **Cuando nadie sabe cuál es la respuesta correcta.** Sin ese paso previo, la prueba mide qué respuesta gusta más, que es otra cosa.
- **Cuando la tarea se hace una vez al mes.** El banco cuesta dos horas; si el ahorro anual no las paga, no se monta.
- **Para comparar modelos por su clasificación pública.** Para eso ya hay tablas ajenas; esta receta es para la tarea propia, que no está en ninguna.

## Para profundizar

- [Cómo elegir un modelo para una tarea](../camino/etapa-1-uso-profesional/01-como-elegir-un-modelo.md) — las cinco variables y la letra pequeña de las tarifas.
- [El contexto: qué se le da y en qué orden](../camino/etapa-1-uso-profesional/03-el-contexto.md) — por qué la misma prueba con más texto cambia el resultado.
- Fichas de los modelos citados: [GPT-6 Luna](../catalogo/modelos/gpt-6-luna.md), [Ministral 3 3B](../catalogo/modelos/ministral-3-3b.md), [Claude Opus 5.5](../catalogo/modelos/claude-opus-5-5.md).

---

*Pepe. Última revisión: 2026-10-22.*
