#!/usr/bin/env python3
"""Genera las bandas de color que encabezan cada página del camino.

Son SVG de la paleta del atlas —azul profundo con filete ámbar— que se insertan
en el Markdown justo debajo del título. GitHub respeta las imágenes, así que es la
única forma de dar color dentro de una página del repositorio.

Uso:
    python3 scripts/make_bands.py
    python3 scripts/make_bands.py --paleta "#B45309"

Los archivos se escriben en assets/bandas/. Si cambia el rótulo de una página o se
añade una etapa, se edita la tabla BANDAS y se vuelve a ejecutar.
"""

from __future__ import annotations

import argparse
from pathlib import Path

# (nombre, rótulo en español, contador en español, rótulo en inglés, contador en inglés)
BANDAS = [
    ("banda-00", "EL CAMINO · PUNTO DE PARTIDA", "", "THE PATH · STARTING POINT", ""),
    ("banda-01", "ETAPA 0 · FUNDAMENTOS", "página 1 de 6", "STAGE 0 · FOUNDATIONS", "page 1 of 6"),
    ("banda-02", "ETAPA 0 · FUNDAMENTOS", "página 2 de 6", "STAGE 0 · FOUNDATIONS", "page 2 of 6"),
    ("banda-03", "ETAPA 0 · FUNDAMENTOS", "página 3 de 6", "STAGE 0 · FOUNDATIONS", "page 3 of 6"),
    ("banda-04", "ETAPA 0 · FUNDAMENTOS", "página 4 de 6", "STAGE 0 · FOUNDATIONS", "page 4 of 6"),
    ("banda-05", "ETAPA 0 · FUNDAMENTOS", "página 5 de 6", "STAGE 0 · FOUNDATIONS", "page 5 of 6"),
    ("banda-06", "ETAPA 0 · FUNDAMENTOS", "página 6 de 6", "STAGE 0 · FOUNDATIONS", "page 6 of 6"),
    ("banda-practica", "ETAPA 0 · PRÁCTICA", "cierre de la etapa", "STAGE 0 · EXERCISE", "closing the stage"),
    ("banda-recursos", "ETAPA 0 · RECURSOS", "fuentes y lecturas", "STAGE 0 · RESOURCES", "sources and readings"),
    ("banda-indice", "ETAPA 0 · FUNDAMENTOS", "índice de la etapa", "STAGE 0 · FOUNDATIONS", "stage index"),
    ("banda-e1-indice", "ETAPA 1 · USO PROFESIONAL", "índice de la etapa", "STAGE 1 · PROFESSIONAL USE", "stage index"),
    ("banda-e1-01", "ETAPA 1 · USO PROFESIONAL", "página 1 de 5", "STAGE 1 · PROFESSIONAL USE", "page 1 of 5"),
    ("banda-e1-02", "ETAPA 1 · USO PROFESIONAL", "página 2 de 5", "STAGE 1 · PROFESSIONAL USE", "page 2 of 5"),
    ("banda-e1-03", "ETAPA 1 · USO PROFESIONAL", "página 3 de 5", "STAGE 1 · PROFESSIONAL USE", "page 3 of 5"),
]

PLANTILLA = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 34" width="560" height="34" role="img" aria-label="{izq}">
  <rect x="0" y="0" width="560" height="34" rx="4" fill="#12233A"/>
  <rect x="0" y="0" width="5" height="34" rx="2.5" fill="{acento}"/>
  <text x="18" y="22" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="13" letter-spacing="1.6" fill="#B3C9E2">{izq}</text>
  <text x="544" y="22" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif" font-size="12" fill="#8AAAD0">{der}</text>
</svg>
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--raiz", default=None, help="raíz del repositorio (por defecto, la del script)")
    ap.add_argument("--paleta", default="#B45309", help="color del filete (ámbar de la paleta por defecto)")
    args = ap.parse_args()

    raiz = Path(args.raiz).resolve() if args.raiz else Path(__file__).resolve().parent.parent
    destino = raiz / "assets" / "bandas"
    destino.mkdir(parents=True, exist_ok=True)

    escritas = 0
    for nombre, es_izq, es_der, en_izq, en_der in BANDAS:
        for idioma, izq, der in (("es", es_izq, es_der), ("en", en_izq, en_der)):
            (destino / f"{nombre}-{idioma}.svg").write_text(
                PLANTILLA.format(izq=izq, der=der, acento=args.paleta), encoding="utf-8"
            )
            escritas += 1
    print(f"Bandas escritas: {escritas} en {destino}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())