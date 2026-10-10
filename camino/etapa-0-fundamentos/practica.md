---
titulo: Práctica — análisis de tres procesos propios
etapa: 0
orden: 99
pregunta: ¿Cómo se decide, por escrito, en qué procesos propios no hace falta inteligencia artificial?
prerrequisitos: [05-donde-no-hace-falta-ia.md]
ultima_revision: 2026-10-10
estado: publicado
traduccion_de:
---

# Práctica — análisis de tres procesos propios

> Versión en inglés: [`practica.en.md`](practica.en.md), traducción de esta revisión.

## Qué hay que entregar

Elija tres procesos reales de su trabajo y analícelos uno por uno, por escrito. En **al menos uno de los tres** la conclusión tiene que ser que no hace falta un modelo. Si los tres acaban en «sí», el análisis no se ha hecho con criterio: casi todos los entornos tienen procesos que se resuelven con reglas, con una consulta o con una persona y una lista de comprobación.

Un proceso sirve como candidato si se repite, tiene un responsable identificable y se puede describir en menos de una página. Algunos habituales: preparar un informe periódico, clasificar el correo que entra, cuadrar dos listados, revisar solicitudes con criterios conocidos, extraer datos de documentos con formato estable.

No hay que implementar nada. Lo que se entrega es el análisis, no el sistema. Y no hace falta ser ingeniero para hacerlo: es un ejercicio de criterio, y se hace mejor con quien conoce el proceso de verdad que con quien conoce la tecnología.

## Cómo se hace

1. **Elija los tres procesos.** Conviene que uno sea pequeño y mecánico: sirve para comprobar que el criterio de descarte se aplica también donde no hay ningún mérito en automatizar.
2. **Describa el proceso actual** en cinco líneas: qué entra, qué sale, quién lo hace hoy, cuánto tiempo consume y cada cuánto se repite.
3. **Pase las ocho condiciones de descarte** de la [página 5](05-donde-no-hace-falta-ia.md), una por una, y anote el resultado de cada una. Las que se cumplan son la base del veredicto.
4. **Estime a grandes rasgos** el coste actual —horas al mes de persona— y, si la conclusión es que sí hace falta un modelo, el coste esperado por operación y el de revisar sus errores.
5. **Proponga la alternativa** para los procesos descartados: reglas, consulta, búsqueda, un clasificador, una lista de comprobación o dejarlo como está.
6. **Escriba el veredicto en una frase**, en términos de qué se hace y por qué.

## Plantilla de análisis

| Apartado | Contenido |
|:--|:--|
| Proceso | Nombre y una línea de descripción |
| Qué entra y qué sale | Entradas, salidas y formato de cada una |
| Quién lo hace hoy | Persona o equipo, y con qué herramienta |
| Volumen | Casos por semana o por mes |
| Coste actual | Horas al mes, estimadas con una base explícita |
| Regla conocida y estable | Sí o no, y en qué parte del proceso |
| Exactitud o determinismo exigidos | Sí o no, y qué se rompe si la salida varía |
| Coste del error | Qué ocurre si la salida es incorrecta y si se puede deshacer |
| Datos disponibles | Qué ejemplos existen, cuántos y con qué restricciones de uso |
| Latencia y coste por operación admisibles | Cifra orientativa del entorno |
| Veredicto | Modelo, reglas, consulta, persona o dejarlo como está |
| Alternativa propuesta | Qué se usaría en su lugar y con qué coste |
| Motivo del veredicto | Una frase, con el criterio que lo decide |

## Un ejemplo resuelto

Se incluye un caso sencillo, de un taller de carreras, para fijar el nivel de detalle esperado. No es una plantilla que haya que copiar: es una muestra de cómo se cierra un análisis.

| Apartado | Contenido |
|:--|:--|
| Proceso | Cuadrar los albaranes de piezas de los proveedores contra las facturas del mes |
| Qué entra y qué sale | Entran albaranes y facturas; sale la relación de diferencias y el pago aprobado |
| Quién lo hace hoy | La persona de administración, con la hoja de cálculo |
| Volumen | Unas 120 líneas al mes, de unos quince proveedores |
| Coste actual | Tres horas al mes, con base en dos sesiones de hora y media |
| Regla conocida y estable | Sí: referencia, cantidad y precio, con tolerancia cero en la referencia |
| Exactitud o determinismo exigidos | Sí, del todo: el importe que se paga tiene que ser exacto |
| Coste del error | Alto en el sentido de confianza con el proveedor, y reversible solo con reclamación |
| Datos disponibles | Los del sistema de facturación; no hay ejemplos etiquetados de discrepancias |
| Latencia y coste por operación | Sin restricción de latencia; el volumen no justifica coste por uso |
| Veredicto | **Reglas y consulta.** Nada de modelo |
| Alternativa propuesta | Reglas de comparación sobre la exportación de facturación y un aviso por excepción para las líneas que no cuadren |
| Motivo del veredicto | La regla se conoce, es estable y el resultado tiene que ser exacto: es exactamente el caso donde un modelo sobra |

## Cómo saber si está cerrado

La práctica está terminada cuando puede responder que sí a todo lo siguiente sin volver a leer las páginas:

- [ ] Hay tres procesos descritos, con responsable y volumen.
- [ ] Al menos uno de los tres concluye que **no** hace falta un modelo, con la condición de descarte que lo decide.
- [ ] Cada veredicto nombra su alternativa y, si es otro método, por qué es preferible.
- [ ] Las cifras de coste y volumen tienen una base explícita: si son estimaciones, se dice de qué se estiman.
- [ ] No queda ningún apartado en blanco ni ninguna casilla marcada sin justificar.

La revisión del propio documento es deliberadamente severa, y a propósito: en este terreno, la diferencia entre un análisis y una opinión es que el análisis se puede discutir punto por punto.

## Los tropiezos de siempre

- **Elegir tres procesos cuya respuesta ya se sabe.** El ejercicio sirve cuando alguno de los tres admite una respuesta incómoda.
- **Rellenar la plantilla sin cifras.** «Mucho volumen» no es un dato. Si no hay medición, se estima y se dice de dónde sale la estimación.
- **Confundir el proceso con la herramienta.** «Automatizar el correo» no es un proceso. El proceso empieza en una entrada concreta y termina en una salida concreta.
- **Saltarse el coste del error.** Es el apartado que más decisiones cambia y el que más se omite.
- **Convertir el veredicto en una preferencia personal.** El criterio se escribe antes de decidir; si el veredicto obliga a cambiar el criterio, la decisión estaba tomada de antemano.

## Cuándo no aplica

Esta práctica no sustituye a un análisis de negocio ni a una valoración formal de riesgos: es un ejercicio de criterio con la información que hay. Si los tres procesos elegidos son irreversibles o están sujetos a normativa, el análisis se limita a documentar por qué en ese contexto hace falta supervisión humana, y conviene añadir al menos un proceso de bajo riesgo para poder aplicar las condiciones de descarte con normalidad.

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

---

*Pepe, asistido por IA. Última revisión: 2026-10-10.*