#!/usr/bin/env python3
"""Comprueba que el texto del repositorio no reproduzca el de sus fuentes.

Dos comprobaciones, en este orden:

1. **Tramos coincidentes.** Compara la prosa de cada página con un corpus local
   de fuentes externas y señala cualquier tramo de N palabras consecutivas que
   aparezca literalmente en las dos. La coincidencia no es una prueba de copia:
   es un aviso para que una persona mire el tramo y decida. Los bloques de
   código y el frontmatter quedan fuera: un ejemplo copiado tal cual de la
   documentación del fabricante no es texto que se esté atribuyendo nadie.

2. **Páginas con una sola fuente externa.** Cuenta los dominios distintos que
   enlaza cada página del camino y cada receta. Una página que solo se sostiene
   con una fuente no se publica todavía (regla de `AGENTS.md`).

El corpus no vive en el repositorio: se pasa como directorio. Se prepara bajando
los textos de las fuentes que uses —artículos, documentación, el texto legal— a
una carpeta de trabajo fuera del control de versiones.

Uso:
    python3 scripts/check_verbatim.py --corpus ~/fuentes
    python3 scripts/check_verbatim.py                      # solo la comprobación 2
    python3 scripts/check_verbatim.py --corpus ~/fuentes --n 10 --estricto

Salida: 0 si no hay nada que revisar, 1 si hay tramos coincidentes, y 1 también
por páginas con una sola fuente cuando se pasa --estricto.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path

# Directorios cuyas rutas son ejemplos, propias del flujo o del propio script.
EXCLUIDOS = {"templates", ".github", "scripts", ".git", "assets", "node_modules"}

# Páginas que la comprobación 2 vigila: lo que sostiene una afirmación sobre IA.
VIGILADAS = ("camino", "recetas")

URL_RE = re.compile(r"https?://([^/\s)\"'<>]+)")
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.S)
VALLADO_RE = re.compile(r"^```.*?^```", re.S | re.M)
HTML_RE = re.compile(r"<[^>]+>")
ENLACE_RE = re.compile(r"\]\([^)]*\)")  # destino de un enlace: se conserva el texto, no la dirección
DIRECCION_RE = re.compile(r"https?://\S+")
NO_PALABRA_RE = re.compile(r"[^\w\sáéíóúüñ]+")

# Marca de entrada bibliográfica: la dirección de la fuente o la fecha de consulta.
# Sirve para no confundir el título de una obra citada con texto copiado.
BIBLIO_RE = re.compile(r"(<https?://|\]\(https?://|\(consultado\s+\d{4}-\d{2}-\d{2})")


def normalizar(texto: str) -> str:
    """Deja solo palabras, en minúscula y sin tildes, para poder comparar."""
    texto = NO_PALABRA_RE.sub(" ", texto.lower())
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", texto).strip()


def prosa(texto: str) -> str:
    """Quita lo que no es texto firmado: frontmatter, código, etiquetas, direcciones
    y entradas bibliográficas.

    Sin las tres primeras, las bandas de color (`<img src=... alt=... width=...>`), los
    bloques de código y las listas de enlaces generan coincidencias que no son prosa.
    Sin la cuarta, cada obra citada produce una coincidencia: su título aparece literal
    en la referencia, que es precisamente como debe aparecer. Un aviso que grita en
    falso deja de leerse, y entonces no protege de nada.
    """
    texto = FRONTMATTER_RE.sub("", texto)
    texto = VALLADO_RE.sub(" ", texto)
    texto = HTML_RE.sub(" ", texto)

    # El filtro bibliográfico va ANTES de borrar las direcciones: una entrada se
    # reconoce precisamente por llevarlas. Aplicado después, no reconoce nada.
    lineas = []
    for linea in texto.splitlines():
        desnuda = linea.strip()
        if desnuda[:2] in {"- ", "* ", "| "} and BIBLIO_RE.search(linea):
            continue
        linea = ENLACE_RE.sub(" ", linea)
        linea = DIRECCION_RE.sub(" ", linea)
        lineas.append(linea)
    return "\n".join(lineas)


def corpus_ngramas(corpus: Path, n: int) -> set[str]:
    ngramas: set[str] = set()
    ficheros = [p for p in corpus.rglob("*") if p.is_file() and p.suffix.lower() in {".md", ".txt", ".rst"}]
    for fichero in ficheros:
        palabras = normalizar(fichero.read_text(encoding="utf-8", errors="ignore")).split()
        for i in range(len(palabras) - n + 1):
            ngramas.add(" ".join(palabras[i : i + n]))
    print(f"Corpus: {len(ficheros)} ficheros, {len(ngramas)} tramos de {n} palabras")
    return ngramas


def revisar_tramos(raiz: Path, corpus: Path, n: int) -> int:
    """Devuelve el número de páginas con algún tramo coincidente."""
    ngramas = corpus_ngramas(corpus, n)
    if not ngramas:
        print("AVISO: el corpus está vacío; no hay nada con lo que comparar.")
        return 0

    paginas_afectadas = 0
    for fichero in sorted(raiz.rglob("*.md")):
        if any(parte in EXCLUIDOS for parte in fichero.relative_to(raiz).parts):
            continue
        if fichero.name.endswith(".en.md"):
            continue
        palabras = normalizar(prosa(fichero.read_text(encoding="utf-8"))).split()
        coincidencias = [
            " ".join(palabras[i : i + n])
            for i in range(len(palabras) - n + 1)
            if " ".join(palabras[i : i + n]) in ngramas
        ]
        if not coincidencias:
            continue
        paginas_afectadas += 1
        # Un mismo tramo puede repetirse: se muestra una vez por arranque.
        vistas: list[str] = []
        for c in coincidencias:
            if not any(c[:60] == v[:60] for v in vistas):
                vistas.append(c)
        print(f"\n{fichero.relative_to(raiz)} — {len(coincidencias)} tramos coincidentes")
        for c in vistas[:5]:
            print(f'  · "{c[:140]}"')
        if len(vistas) > 5:
            print(f"  · y {len(vistas) - 5} más")

    if paginas_afectadas:
        print(f"\nRevisar: {paginas_afectadas} páginas con tramos coincidentes.")
    else:
        print("Sin tramos coincidentes.")
    return paginas_afectadas


def revisar_fuentes(raiz: Path) -> int:
    """Devuelve el número de páginas sostenidas por un solo dominio externo."""
    solitarias = 0
    vigiladas = 0
    for carpeta in VIGILADAS:
        for fichero in sorted((raiz / carpeta).rglob("*.md")):
            if fichero.name.endswith(".en.md"):
                continue
            if any(parte in EXCLUIDOS for parte in fichero.relative_to(raiz).parts):
                continue
            vigiladas += 1
            dominios = {d.lower().removeprefix("www.").split(":")[0] for d in URL_RE.findall(fichero.read_text(encoding="utf-8"))}
            if len(dominios) == 1:
                solitarias += 1
                print(f"  {fichero.relative_to(raiz)} — una sola fuente: {next(iter(dominios))}")
    print(f"Páginas vigiladas: {vigiladas}")
    if solitarias:
        print(f"AVISO: {solitarias} páginas con una sola fuente externa.")
    else:
        print("Ninguna página depende de una sola fuente externa.")
    return solitarias


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=None, help="raíz del repositorio (por defecto, la del script)")
    ap.add_argument("--corpus", default=None, help="directorio con los textos de las fuentes")
    ap.add_argument("--n", type=int, default=12, help="palabras consecutivas para marcar un tramo (por defecto 12)")
    ap.add_argument("--estricto", action="store_true", help="devuelve 1 también por páginas con una sola fuente")
    args = ap.parse_args()

    raiz = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent

    print("— Fuentes externas por página —")
    solitarias = revisar_fuentes(raiz)

    tramos = 0
    if args.corpus:
        print("\n— Tramos coincidentes con el corpus —")
        tramos = revisar_tramos(raiz, Path(args.corpus).expanduser(), args.n)
    else:
        print("\n(sin --corpus: no se comprueban tramos coincidentes)")

    if tramos:
        return 1
    if args.estricto and solitarias:
        return 1
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        # Al canalizar la salida a `head`, la tubería se cierra antes de terminar.
        raise SystemExit(0)
