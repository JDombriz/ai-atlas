---
titulo: Práctica — análisis de tres procesos propios
etapa: 0
orden: 99
pregunta: ¿Cómo se decide, por escrito, en qué procesos propios no hace falta inteligencia artificial?
prerrequisitos: [05-donde-no-hace-falta-ia.md]
ultima_revision: 2026-10-10
estado: borrador
traduccion_de:
---

# Práctica — análisis de tres procesos propios

> **Pregunta que resuelve:** ¿cómo se decide, por escrito, en qué procesos propios no hace falta inteligencia artificial?

## Qué se pide

Analizar **tres procesos reales** del entorno de trabajo propio y entregar un documento por proceso, con el veredicto y su razonamiento. Al menos uno de los tres debe concluir que **no** hace falta un modelo. Si los tres concluyen que sí, el análisis no se ha hecho con criterio: casi todos los entornos tienen procesos que se resuelven con reglas, con una consulta o con una persona y una lista de comprobación.

Un proceso vale como candidato si se repite, tiene un responsable identificable y se puede describir en menos de una página. Ejemplos habituales: preparar un informe periódico, clasificar incidencias o correo entrante, conciliar dos listados, revisar solicitudes con criterios conocidos, extraer datos de documentos con formato estable.

No hace falta implementar nada. El producto de esta práctica es el análisis, no el sistema.

## Cómo se hace

1. **Elegir los tres procesos.** Uno de ellos conviene que sea pequeño y mecánico: sirve para comprobar que el criterio de descarte se aplica también donde no hay mérito en automatizar.
2. **Describir el proceso actual** en cinco líneas: qué entra, qué sale, quién lo hace hoy, cuánto tiempo consume y con qué frecuencia se repite.
3. **Pasar los criterios de descarte** de la [página 5](05-donde-no-hace-falta-ia.md), uno por uno, y anotar el resultado de cada uno. Los que se cumplen son la base del veredicto.
4. **Estimar a grandes rasgos** el coste actual —horas al mes de persona— y, si el veredicto es que sí hace falta un modelo, el coste esperado por operación y el coste de revisar los errores.
5. **Proponer la alternativa** para los procesos descartados: reglas, consulta, búsqueda, un clasificador, una lista de comprobación o dejarlo como está.
6. **Escribir el veredicto en una frase**, en términos de qué se hace y por qué.

## Plantilla de análisis

| Apartado | Contenido |
|:--|:--|
| Proceso | Nombre y una línea de descripción |
| Qué entra / qué sale | Entradas, salidas y formato de cada una |
| Quién lo hace hoy | Persona o equipo, y con qué herramienta |
| Volumen | Casos por semana o por mes |
| Coste actual | Horas al mes, estimadas con una base explícita |
| Regla conocida y estable | Sí / no, y en qué parte del proceso |
| Exactitud o determinismo exigidos | Sí / no, y qué se rompe si la salida varía |
| Coste del error | Qué ocurre si la salida es incorrecta y si se puede deshacer |
| Datos disponibles | Qué ejemplos existen, cuántos y con qué restricciones de uso |
| Latencia y coste por operación admisibles | Cifra orientativa del entorno |
| Veredicto | Modelo / reglas / consulta / persona / dejarlo como está |
| Alternativa propuesta | Qué se usaría en su lugar y con qué coste |
| Motivo del veredicto | Una frase, con el criterio que lo decide |

## Ejemplo resuelto

Se incluye un caso sencillo y ajeno a cualquier organización concreta, para fijar el nivel de detalle esperado. No es un modelo que haya que copiar: es una muestra de cómo se cierra un análisis.

| Apartado | Contenido |
|:--|:--|
| Proceso | Preparar el resumen semanal de incidencias para el equipo |
| Qué entra / qué sale | Entran las incidencias cerradas de la semana; sale un resumen de media página |
| Quién lo hace hoy | Una persona del equipo, los viernes por la tarde |
| Volumen | 4 resúmenes al mes |
| Coste actual | Unas 2 horas al mes, con base en cuatro sesiones de media hora |
| Regla conocida y estable | Sí: el resumen se construye a partir de consultas y de un orden fijo de apartados |
| Exactitud o determinismo exigidos | Media: los datos deben ser exactos; la redacción puede variar |
| Coste del error | Bajo y reversible: el resumen se corrige y se reenvía |
| Datos disponibles | Los del sistema de incidencias, exportables por consulta |
| Latencia y coste por operación | No hay restricción de latencia; el volumen no justifica coste por operación |
| Veredicto | **Consulta automatizada.** El modelo solo si se quiere redactar el párrafo de cierre |
| Alternativa propuesta | Informe generado por consulta y plantilla; el texto de cierre, escrito por la persona o asistido y revisado |
| Motivo del veredicto | La parte costosa es recopilar y ordenar datos, no redactar: ahí hay una consulta, no un modelo |

## Cómo se comprueba

La práctica está cerrada cuando se puede responder que sí a todo lo siguiente, sin recurrir al texto de las páginas:

- [ ] Hay tres procesos descritos, con responsable y volumen.
- [ ] Al menos uno de los tres concluye que **no** hace falta un modelo, con el criterio de descarte que lo decide.
- [ ] Cada veredicto nombra su alternativa y, si es otro método, por qué es preferible.
- [ ] Las cifras de coste y volumen tienen una base explícita: si son estimaciones, se dice de qué se estiman.
- [ ] No hay ningún apartado en blanco ni ninguna casilla marcada sin justificar.

La revisión del propio documento es deliberadamente severa: en este terreno, la diferencia entre un análisis y una opinión es que el análisis se puede discutir punto por punto.

## Errores frecuentes

- **Elegir tres procesos donde la respuesta ya se sabe.** El ejercicio tiene sentido cuando alguno de los tres admite una respuesta incómoda.
- **Rellenar la plantilla sin cifras.** «Mucho volumen» no es un dato. Si no hay medición, se estima y se dice cómo.
- **Confundir el proceso con la herramienta.** «Automatizar el correo» no es un proceso. El proceso empieza en una entrada y termina en una salida concreta.
- **Saltarse el coste del error.** Es el apartado que más decisiones cambia y el que más se omite.
- **Convertir el veredicto en una preferencia personal.** El criterio se escribe antes de decidir; si el veredicto exige cambiar el criterio, la decisión está tomada de antemano.

## Cuándo no aplica

Esta práctica no sustituye a un análisis de negocio ni a una valoración de riesgos formales: es un ejercicio de criterio con la información disponible. Si los tres procesos elegidos son irreversibles o están sujetos a normativa, el análisis se limita a documentar por qué en ese contexto hace falta supervisión humana, y conviene añadir al menos un proceso de bajo riesgo para poder aplicar los criterios de descarte con normalidad.

## Definiciones

- **Candidato a automatización**: proceso repetitivo, con responsable, entradas y salidas identificables, apto para comparar métodos.
- **Base de la estimación**: dato del que procede una cifra; si no procede de ninguna medición, se declara la estimación y su origen.
- **Veredicto**: decisión escrita sobre el método que corresponde a un proceso, con su motivo en una frase.

## Referencias

- *Rules of Machine Learning: Best Practices for ML Engineering* — M. Zinkevich, Google — <https://developers.google.com/machine-learning/guides/rules-of-ml> (consultado 2026-10-10)
- *Artificial Intelligence Risk Management Framework (AI RMF 1.0)* — NIST, 2023 — <https://doi.org/10.6028/NIST.AI.100-1> (consultado 2026-10-10)
- Comprobación propia — las direcciones anteriores devolvieron código 200 en una petición HTTP el 2026-10-10

## Continuar

- Anterior: [El oficio en 2026](06-el-oficio-en-2026.md)
- Recursos de la etapa: [Recursos](recursos.md)
- Índice de la etapa: [Etapa 0 — Fundamentos](README.md)
- Índice temático: [`../../INDEX.md`](../../INDEX.md)