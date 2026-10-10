# Prompt para generar el banner definitivo

Tarea anotada en el [`ROADMAP.md`](../ROADMAP.md): generar una imagen de cabecera mejor que la actual con una herramienta de imagen generativa —Gemini o ChatGPT— y recomponerla sobre esta misma tipografía.

## Antes de pegar nada: la decisión que importa

Los modelos de imagen escriben mal. Con texto largo, con acentos y con nombres propios el resultado es casi siempre defectuoso —letras cambiadas, tildes movidas, palabras inventadas— y un banner con «Al ATlas» estropea justo lo que se pretendía. Por eso el prompt principal **no pide texto**: pide el arte de fondo, y la tipografía se compone encima con el archivo `assets/banner.html`, que ya existe y sabe hacerlo.

El resultado de esa combinación es mejor que el de una sola pasada, y además reversible: si más adelante cambia el lema, se recompone en un minuto sin volver a generar arte.

## Prompt A — el arte de fondo (recomendado)

Pegar tal cual. La versión en inglés suele dar mejores resultados, porque los modelos están entrenados con muchas más descripciones cartográficas y editoriales en ese idioma.

```text
An abstract, editorial, wide banner artwork for an open-source documentation
project about artificial intelligence. Style: cartographic. A topographic map
seen from directly above, drawn as precise, fine contour lines on a matte, flat
surface; a single winding route crosses the map from the lower left to the upper
right, marked by six small, subtle waypoint dots along its length. Screen-printed
or technical-atlas-plate feel, like a plate in a museum catalogue.

Palette, strictly limited to four colours: deep ink blue #12233A as the
background, mid blues #1F4E79 and #3B6FAF for the contour lines, and pale
blue-white #E6EEF7 used only for the route and the highest contour lines.

Composition: generous empty space across the upper half and along the left and
right edges; in those areas keep the surface perfectly dark and even, with no
detail at all, so typography can be placed over it. The dense contour detail
stays in the lower central band.

Not a photograph, not a 3D render, no gradients of purple or magenta, no lens
flare, no glowing brain, no humanoid robot, no circuit-board clichés, no
holograms, no stock-photo look, no letters, no numbers, no logos, no user
interface elements, no text of any kind.
```

Versión en español, por si la herramienta responde mejor:

```text
Un fondo abstracto y editorial, muy apaisado, para un proyecto de documentación
sobre inteligencia artificial. Estilo cartográfico: un mapa topográfico visto
desde arriba, dibujado con líneas de nivel finas y precisas sobre una superficie
mate y plana; una sola ruta serpenteante lo cruza de abajo a la izquierda hacia
arriba a la derecha, marcada con seis puntos discretos a lo largo. Factura de
lámina técnica de atlas, como una plancha de catálogo de museo.

Paleta limitada a cuatro colores: azul tinta profundo #12233A como fondo, azules
medios #1F4E79 y #3B6FAF para las líneas de nivel, y blanco azulado pálido
#E6EEF7 solo para la ruta y las líneas más altas.

Composición: mucho espacio vacío en toda la mitad superior y en los bordes
izquierdo y derecho; en esas zonas la superficie debe quedar oscura y uniforme,
sin ningún detalle, para poder colocar allí la tipografía. El detalle denso de
las curvas se concentra en la banda inferior central.

No es una fotografía ni un render 3D; sin degradados morados o magenta, sin
destellos, sin cerebros brillantes, sin robots humanoides, sin circuitos
impresos, sin hologramas, sin aspecto de foto de banco de imágenes, sin letras,
sin números, sin logotipos, sin elementos de interfaz y sin ningún texto.
```

### Parámetros de la herramienta

| Ajuste | Valor recomendado | Nota |
|:--|:--|:--|
| Proporción | 21:9 si está disponible; si no, 16:9 | La cabecera real es 1280×440 (≈ 2,9:1). Desde 21:9 se recorta sin perder nada importante |
| Resolución | La máxima que ofrezca | Se reduce a 1280 px de ancho al recomponer |
| Variantes | Pedir tres y elegir | La primera suele ser la más tópica |
| Semilla / estilo | Sin estilo predefinido ni filtros | Los estilos «cinematográfico» y «neón» arruinan la paleta |

## Prompt B — todo en una sola pasada (opcional)

Solo si se quiere probar suerte con el texto dentro de la imagen. Hay que revisar el resultado letra por letra, tildes incluidas: si falla una sola, se descarta.

```text
Wide banner for a documentation project. Dark ink-blue background #12233A with
fine topographic contour lines in mid blues #1F4E79 and #3B6FAF. Centred, a
clean geometric sans-serif title in pale blue-white #E6EEF7 reading exactly
"AI ATLAS", and beneath it, smaller and lighter, the line reading exactly
"De cero a nivel profesional en inteligencia artificial". Minimal, editorial,
no other text, no logos, no icons, no glow, no people, no robots.
```

## Cómo se integra una vez generada

1. Guardar el arte elegido como `assets/banner-fondo.png` y subirlo al repositorio.
2. En `assets/banner.html`, añadir la imagen como fondo del bloque `#cabecera`, con una capa oscura encima —`rgba(18,35,58,.55)`— para garantizar que el texto siga siendo legible sobre cualquier variación del arte.
3. Volver a rasterizar a doble resolución: 1280×440 con factor 2, es decir 2560×880, y guardar el resultado como `assets/banner.png`. El procedimiento es el que se usó para la versión actual.
4. Revisar antes de subir: que el texto se lea con holgura, que no haya detalle compitiendo detrás de la tipografía y que el recorte a la mitad izquierda —como se ve en un móvil— siga teniendo sentido.

## Lo que hay que dar por bueno antes de subir

- [ ] No aparece ningún texto, número ni logotipo generado por el modelo.
- [ ] La paleta se mantiene en los cuatro colores, sin morados ni neones.
- [ ] La zona donde va el título queda oscura y uniforme.
- [ ] Se lee bien a 1280 px de ancho y, recortado a la mitad, también.
- [ ] No hay cerebros brillantes, robots humanoides ni circuitos impresos.
- [ ] El resultado no parece una foto de banco de imágenes.
