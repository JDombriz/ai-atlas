#!/usr/bin/env python3
"""Comprueba los enlaces relativos de los archivos Markdown del repositorio.

Uso:
    python3 scripts/check_relative_links.py
    python3 scripts/check_relative_links.py --root /ruta/al/repo

Excluye templates/ y .github/, cuyas rutas son ejemplos o propias del flujo.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

LINK_RE = re.compile(r"\[[^\]]*\]\((?P<dest>[^)\s]+)\)")
EXCLUIDOS = {"templates", ".github", ".git"}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=None)
    args = ap.parse_args()
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent

    fallos: list[str] = []
    total = 0
    for fichero in sorted(root.rglob("*.md")):
        if any(parte in EXCLUIDOS for parte in fichero.relative_to(root).parts):
            continue
        texto = fichero.read_text(encoding="utf-8")
        for m in LINK_RE.finditer(texto):
            destino = m.group("dest")
            if destino.startswith(("http://", "https://", "mailto:", "#")):
                continue
            ruta = destino.split("#")[0]
            if not ruta:
                continue
            total += 1
            objetivo = (fichero.parent / ruta).resolve()
            if not objetivo.exists():
                fallos.append(f"{fichero.relative_to(root)} -> {destino}")

    print(f"Enlaces relativos comprobados: {total}")
    if fallos:
        print(f"ROTOS: {len(fallos)}")
        for f in fallos:
            print(f"  {f}")
        return 1
    print("Sin enlaces relativos rotos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())