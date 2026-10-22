#!/usr/bin/env python3
"""Comprueba que el frontmatter de cada página sea YAML válido.

GitHub parsea el frontmatter como YAML y muestra un error en la vista «Code»
cuando no lo es. El fallo más frecuente es un título con dos puntos sin
comillas: `titulo: La instrucción: pedir bien`. Este script lo detecta sin
dependencias: busca valores sin comillas que contengan «: » o « #», que son
los que rompen el documento.

Uso:
    python3 scripts/check_frontmatter.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CLAVE = re.compile(r"^([A-Za-z_]+):\s+(.*)$")
EXCLUIR = {".git", "node_modules", "templates", "scripts"}


def main() -> int:
    raiz = Path(__file__).resolve().parent.parent
    problemas: list[tuple[str, int, str]] = []
    for p in sorted(raiz.rglob("*.md")):
        if any(parte in EXCLUIR for parte in p.parts):
            continue
        texto = p.read_text(encoding="utf-8")
        if not texto.startswith("---"):
            continue
        bloque = texto.split("---", 2)[1]
        for n, linea in enumerate(bloque.splitlines(), start=2):
            m = CLAVE.match(linea)
            if not m:
                continue
            valor = m.group(2)
            if valor[:1] in {'"', "'", "|", ">"}:
                continue
            if ": " in valor or valor.endswith(":") or " #" in valor:
                problemas.append((str(p.relative_to(raiz)), n, linea.strip()))

    if problemas:
        print(f"Frontmatter con valores que rompen el YAML: {len(problemas)}")
        for archivo, n, linea in problemas:
            print(f"  {archivo}:{n}  {linea[:100]}")
        print("\nSe corrige entrecomillando el valor: clave: \"texto: con dos puntos\"")
        return 1
    print("Frontmatter correcto en todas las páginas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
