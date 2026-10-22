#!/usr/bin/env python3
"""Genera INDEX.md, GLOSSARY.md y llms.txt a partir del contenido del repositorio.

Sin dependencias externas: solo biblioteca estándar. Los tres índices son
artefactos generados; editarlos a mano se detecta en revisión y se sobrescribe.

Uso:
    python3 scripts/build_index.py
    python3 scripts/build_index.py --root /ruta/al/repo
"""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

FRONT_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
DEF_RE = re.compile(r"^-\s+\*\*(?P<term>[^*]+)\*\*\s*[:—–-]\s*(?P<def>.+)$")

CATEGORIAS = [
    ("modelos", "Modelos y plataformas"),
    ("herramientas", "Herramientas y frameworks"),
    ("aprendizaje", "Aprendizaje y práctica"),
    ("investigacion", "Investigación y benchmarks"),
    ("operacion", "Operación y coste"),
    ("comunidades", "Comunidades y fuentes vivas"),
    ("contexto", "Contexto y regulación (UE)"),
]

DESCRIPCION = (
    "Repositorio de consulta documental sobre inteligencia artificial, organizado "
    "como un camino de aprendizaje de cero a nivel profesional."
)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Devuelve (campos, cuerpo). Soporta valores simples y listas [a, b]."""
    m = FRONT_RE.match(text)
    if not m:
        return {}, text
    campos: dict = {}
    for linea in m.group(1).splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#") or ":" not in linea:
            continue
        clave, valor = linea.split(":", 1)
        clave, valor = clave.strip(), valor.strip()
        if valor.startswith("[") and valor.endswith("]"):
            campos[clave] = [
                v.strip().strip("\"'") for v in valor[1:-1].split(",") if v.strip()
            ]
        else:
            campos[clave] = valor.strip("\"'")
    return campos, text[m.end():]


def leer(path: Path) -> tuple[dict, str]:
    """Devuelve (campos, cuerpo) de un archivo markdown con frontmatter."""
    try:
        texto = path.read_text(encoding="utf-8")
    except OSError:
        return {}, ""
    return parse_frontmatter(texto)


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def paginas_de_etapa(etapa_dir: Path) -> list[Path]:
    """Orden de lectura: README, páginas numeradas, práctica, recursos.

    Los archivos hermanos de traducción (*.en.md) se excluyen: el índice temático y
    el glosario son el mapa del texto español, que es el canónico. Las traducciones
    se anuncian junto a su página, con un enlace."""
    
    def clave(p: Path) -> tuple:
        n = p.name
        if n == "README.md":
            return (0, "")
        if n == "practica.md":
            return (2, "")
        if n == "recursos.md":
            return (3, "")
        return (1, n)

    paginas = [p for p in etapa_dir.glob("*.md") if not p.name.endswith(".en.md")]
    return sorted(paginas, key=clave)


def traducciones_de_etapa(etapa_dir: Path) -> dict[str, str]:
    """Página en español -> archivo hermano en inglés, si existe."""
    salida: dict[str, str] = {}
    for p in sorted(etapa_dir.glob("*.en.md")):
        original = etapa_dir / (p.name[: -len(".en.md")] + ".md")
        if original.exists():
            salida[original.name] = p.name
    return salida


def recoger_etapas(root: Path) -> list[dict]:
    etapas = []
    camino = root / "camino"
    if not camino.is_dir():
        return etapas
    for d in sorted(p for p in camino.iterdir() if p.is_dir()):
        if not d.name.startswith("etapa-"):
            continue
        if not (d / "README.md").exists():
            continue  # una etapa sin índice no está publicada
        campos, _ = leer(d / "README.md")
        paginas = []
        for p in paginas_de_etapa(d):
            c, _ = leer(p)
            paginas.append({"ruta": rel(p, root), "campos": c})
        etapas.append(
            {
                "dir": d.name,
                "campos": campos,
                "paginas": paginas,
                "traducciones": traducciones_de_etapa(d),
            }
        )
    return etapas


def recoger_fichas(root: Path) -> list[dict]:
    fichas = []
    for carpeta, _titulo in CATEGORIAS:
        d = root / "catalogo" / carpeta
        if not d.is_dir():
            continue
        for p in sorted(d.glob("*.md")):
            c, _ = leer(p)
            if not c.get("id"):
                continue
            c["_ruta"] = rel(p, root)
            c["_categoria"] = carpeta
            fichas.append(c)
    return fichas


def recoger_simples(root: Path, subdir: str) -> list[dict]:
    """Páginas sueltas (recetas, comparativas, decisiones) con frontmatter."""
    salida = []
    d = root / subdir
    if not d.is_dir():
        return salida
    for p in sorted(d.rglob("*.md")):
        if p.name == "README.md":
            continue
        if p.name.endswith(".en.md"):
            # Los hermanos de traducción no entran en el índice, que es el mapa
            # del texto español (D13).
            continue
        c, _ = leer(p)
        salida.append({"ruta": rel(p, root), "campos": c})
    return salida


def recoger_glosario(root: Path) -> list[tuple[str, str, str]]:
    """Términos definidos en secciones «## Definiciones» de cualquier página."""
    terminos: dict[str, tuple[str, str]] = {}
    for p in sorted(root.rglob("*.md")):
        if any(part in {".github", "node_modules", ".git", "templates", "scripts"} for part in p.parts):
            continue
        if p.name.endswith(".en.md"):
            continue
        _, cuerpo = leer(p)
        for bloque in re.split(r"^##\s+", cuerpo, flags=re.M)[1:]:
            if not bloque.lower().startswith("definiciones"):
                continue
            for linea in bloque.splitlines()[1:]:
                m = DEF_RE.match(linea.strip())
                if m:
                    terminos.setdefault(
                        m.group("term").strip(),
                        (m.group("def").strip(), rel(p, root)),
                    )
    return [(t, d, r) for t, (d, r) in sorted(terminos.items(), key=lambda x: x[0].lower())]


MESES = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
]

ESTADOS_ETAPA = {
    "borrador": "en preparación",
    "publicado": "publicada",
    "archivado": "archivada",
}


def fecha_en_espanol(d: date) -> str:
    """Devuelve la fecha escrita como se lee: 10 de octubre de 2026."""
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def escribir_index(root: Path, etapas, fichas, recetas, comparativas, decisiones) -> str:
    hoy = fecha_en_espanol(date.today())
    l: list[str] = []
    l.append("# Índice temático\n")
    l.append(
        "Tres formas de usar este repositorio: recorrer el **camino** en orden, "
        "consultar **por tema** desde este índice, o resolver **por tarea** con una receta.\n"
    )

    l.append("## El camino, en orden\n")
    if not etapas:
        l.append("*(sin etapas publicadas todavía)*\n")
    for e in etapas:
        c = e["campos"]
        num = c.get("etapa", "?")
        titulo = c.get("titulo") or e["dir"]
        estado = ESTADOS_ETAPA.get(c.get("estado", "borrador"), c.get("estado", ""))
        l.append(f"### Etapa {num} — [{titulo}]({e['paginas'][0]['ruta']})")
        l.append(f"*{estado}* · {c.get('dedicacion_orientativa', '')}".rstrip(" ·") + "\n")
        if c.get("objetivo"):
            l.append(f"Objetivo: {c['objetivo']}\n")
        for p in e["paginas"][1:]:
            pc = p["campos"]
            nombre = pc.get("titulo") or Path(p["ruta"]).stem
            pregunta = pc.get("pregunta", "")
            linea = f"- [{nombre}]({p['ruta']})"
            if pregunta:
                linea += f" — {pregunta}"
            en = e.get("traducciones", {}).get(Path(p["ruta"]).name)
            if en:
                linea += f" · [English]({Path(p['ruta']).with_name(en).as_posix()})"
            l.append(linea)
        l.append("")

    l.append("## Por tarea\n")
    if not recetas:
        l.append("*(sin recetas publicadas todavía)*\n")
    for r in recetas:
        nombre = r["campos"].get("titulo") or Path(r["ruta"]).stem
        cuando = r["campos"].get("cuando", "")
        l.append(f"- [{nombre}]({r['ruta']})" + (f" — {cuando}" if cuando else ""))
    l.append("")

    l.append("## Por consulta\n")
    for titulo, lista in (("Comparativas", comparativas), ("Decisiones de criterio", decisiones)):
        l.append(f"### {titulo}\n")
        if not lista:
            l.append("*(sin páginas publicadas todavía)*\n")
        for r in lista:
            nombre = r["campos"].get("titulo") or Path(r["ruta"]).stem
            l.append(f"- [{nombre}]({r['ruta']})")
        l.append("")

    l.append("## Catálogo de recursos\n")
    if not fichas:
        l.append("*(sin fichas publicadas todavía)*\n")
    por_categoria: dict[str, list[dict]] = {}
    for f in fichas:
        por_categoria.setdefault(f["_categoria"], []).append(f)
    for clave, titulo in CATEGORIAS:
        lista = por_categoria.get(clave, [])
        if not lista:
            continue
        l.append(f"### {titulo}\n")
        l.append("| Recurso | Etapa | Tipo | Coste | Idioma | Verificado | Estado |")
        l.append("|:--|:--|:--|:--|:--|:--|:--|")
        for f in sorted(lista, key=lambda x: x.get("title_es", "").lower()):
            nombre = f.get("title_es") or f.get("id")
            l.append(
                "| [{nombre}]({ruta}) | {etapa} | {tipo} | {coste} | {idioma} | {fecha} | {estado} |".format(
                    nombre=nombre,
                    ruta=f["_ruta"],
                    etapa=f.get("nivel", ""),
                    tipo=f.get("tipo", ""),
                    coste=f.get("coste", ""),
                    idioma=f.get("idioma", ""),
                    fecha=f.get("ultima_verificacion", ""),
                    estado=f.get("estado", ""),
                )
            )
        l.append("")

    archivadas = [f for f in fichas if f.get("estado") == "archivado"]
    l.append(f"\n---\n\nFichas activas: {len(fichas) - len(archivadas)}. "
             f"Archivadas: {len(archivadas)}. Páginas del camino: "
             f"{sum(len(e['paginas']) for e in etapas)}.\n")
    l.append(
        f"*Índice actualizado el {hoy}. Se compone a partir del contenido del "
        "repositorio: las correcciones van a la página, no aquí.*\n"
    )
    return "\n".join(l) + "\n"


def escribir_glosario(terminos) -> str:
    hoy = fecha_en_espanol(date.today())
    l = ["# Glosario\n"]
    l.append(
        "Cada término procede de la sección «Definiciones» de una página; si dos páginas "
        "definen el mismo término, prevalece la primera por orden alfabético de ruta.\n"
    )
    if not terminos:
        l.append("*(sin términos definidos todavía)*\n")
    for termino, definicion, ruta in terminos:
        l.append(f"- **{termino}** — {definicion}  \n  → [{ruta}]({ruta})")
    l.append("")
    l.append(
        f"---\n\n*Glosario actualizado el {hoy}. Se compone a partir de las definiciones "
        "de las páginas: para cambiar una entrada, se cambia en la página.*\n"
    )
    return "\n".join(l) + "\n"


def escribir_llms(root, etapas, fichas, recetas) -> str:
    l = ["# AI Atlas", "", f"> {DESCRIPCION}", ""]
    l.append("## Camino")
    l.append("")
    for e in etapas:
        c = e["campos"]
        l.append(f"### Etapa {c.get('etapa','?')} — {c.get('titulo', e['dir'])}")
        l.append(f"Objetivo: {c.get('objetivo','')}")
        l.append(f"Criterio de salida: {c.get('criterio_salida','')}")
        for p in e["paginas"]:
            pc = p["campos"]
            l.append(f"- {pc.get('titulo', Path(p['ruta']).stem)}: {p['ruta']}")
        l.append("")
    l.append("## Recursos del catálogo")
    l.append("")
    for f in fichas:
        l.append(
            f"- {f.get('title_es', f['id'])} ({f.get('tipo','')}, {f.get('nivel','')}, "
            f"{f.get('coste','')}, idioma {f.get('idioma','')}): {f.get('url','')} "
            f"[ficha: {f['_ruta']}, verificado {f.get('ultima_verificacion','')}, "
            f"estado {f.get('estado','')}]"
        )
    l.append("")
    l.append("## Recetas")
    l.append("")
    for r in recetas:
        l.append(f"- {r['campos'].get('titulo', Path(r['ruta']).stem)}: {r['ruta']}")
    l.append("")
    l.append("## Índices")
    l.append("")
    l.append("- Índice temático completo: INDEX.md")
    l.append("- Glosario: GLOSSARY.md")
    return "\n".join(l) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=None, help="raíz del repositorio (por defecto, la del script)")
    args = ap.parse_args()

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent

    etapas = recoger_etapas(root)
    fichas = recoger_fichas(root)
    recetas = recoger_simples(root, "recetas")
    comparativas = recoger_simples(root, "referencia/comparativas")
    decisiones = recoger_simples(root, "referencia/decisiones")
    terminos = recoger_glosario(root)

    (root / "INDEX.md").write_text(
        escribir_index(root, etapas, fichas, recetas, comparativas, decisiones), encoding="utf-8"
    )
    (root / "GLOSSARY.md").write_text(escribir_glosario(terminos), encoding="utf-8")
    (root / "llms.txt").write_text(escribir_llms(root, etapas, fichas, recetas), encoding="utf-8")

    print(
        f"Etapas: {len(etapas)} | Páginas de camino: "
        f"{sum(len(e['paginas']) for e in etapas)} | Fichas: {len(fichas)} | "
        f"Recetas: {len(recetas)} | Términos: {len(terminos)}"
    )
    print("Escritos: INDEX.md, GLOSSARY.md, llms.txt")
    for logro in ("INDEX.md", "GLOSSARY.md", "llms.txt"):
        print(f"  {root / logro}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())