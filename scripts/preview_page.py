#!/usr/bin/env python3
"""Genera una vista previa en HTML de una página del camino, para revisar el aspecto.

No es el sitio del proyecto: es una herramienta de trabajo. Renderiza el Markdown
con las mismas convenciones que GitHub y aplica dos hojas de estilo —una que imita
el tema oscuro de GitHub y otra con la paleta del atlas— para poder comparar cómo
se ve hoy y cómo se vería con color propio.

Uso:
    python3 scripts/preview_page.py camino/etapa-0-fundamentos/01-que-es-la-inteligencia-artificial.md
    python3 scripts/preview_page.py <archivo.md> --out-dir ../ai-atlas-trabajo/vistas/01

Requiere el paquete `markdown`. En el contenedor hay un entorno sólo para esto:
    /opt/data/.venvs/vistas/bin/python scripts/preview_page.py …
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

import markdown

CSS_BASE = """
* { box-sizing: border-box; }
body { margin: 0; padding: 32px 16px 64px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
.hoja { max-width: 860px; margin: 0 auto; }
h1, h2 { font-weight: 600; line-height: 1.25; }
h1 { font-size: 2em; padding-bottom: .3em; border-bottom: 1px solid; margin: .4em 0 .6em; }
h2 { font-size: 1.4em; margin: 1.8em 0 .6em; padding-bottom: .2em; border-bottom: 1px solid; }
p, li { line-height: 1.65; }
blockquote { margin: 1em 0; padding: .4em 1em; border-left: 4px solid; }
blockquote p { margin: .4em 0; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: .95em; }
th, td { padding: 6px 13px; border: 1px solid; text-align: left; }
code { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: .9em; padding: .15em .35em; border-radius: 4px; }
img { max-width: 100%; }
hr { border: 0; border-top: 1px solid; margin: 2em 0; }
.meta { margin: 0 0 1.6em; font-size: .9em; }
.aviso { font-size: .85em; padding: 8px 12px; border-radius: 6px; margin: 0 0 24px; }
.alert { margin: 1em 0; padding: .6em 1em; border-left: .35em solid; border-radius: 4px; }
.alert p:first-child { margin-top: 0; }
.alert p:last-child { margin-bottom: 0; }
"""

CSS_OSCURO = """
body { background: #0d1117; color: #e6edf3; }
h1, h2 { border-color: #30363d; }
a { color: #4493f8; }
blockquote { color: #9198a1; border-color: #3d444d; }
th, td { border-color: #3d444d; }
tr:nth-child(2n) td { background: #151b23; }
code { background: #343942; }
hr { border-color: #30363d; }
.meta { color: #9198a1; }
.aviso { background: #12233a; color: #b3c9e2; }
.alert-note { border-color: #4493f8; background: #121d2f; }
.alert-tip { border-color: #3fb950; background: #0f2417; }
.alert-important { border-color: #ab7df8; background: #1c1633; }
.alert-warning { border-color: #d29922; background: #241d10; }
.alert-caution { border-color: #f85149; background: #271616; }
strong { color: #f0f6fc; }
"""

CSS_PALETA = """
body { background: #ffffff; color: #12233a; }
h1 { color: #1F4E79; border-color: #d7e3f0; }
h2 { color: #1F4E79; border-color: #e6edf3; }
a { color: #1F4E79; }
blockquote { color: #57606a; border-color: #8aaad0; background: #f6f8fa; }
th, td { border-color: #d8dee4; }
th { background: #f0f6fc; color: #12233a; }
tr:nth-child(2n) td { background: #fbfcfd; }
code { background: #f0f6fc; color: #12233a; }
hr { border-color: #e6edf3; }
.meta { color: #57606a; }
.aviso { background: #f0f6fc; color: #1F4E79; }
.alert-note { border-color: #1F4E79; background: #f0f6fc; }
.alert-tip { border-color: #1A7F37; background: #f0fbf3; }
.alert-important { border-color: #B45309; background: #fdf6ec; }
.alert-warning { border-color: #B45309; background: #fdf6ec; }
.alert-caution { border-color: #B42318; background: #fdf2f1; }
strong { color: #1F4E79; }
"""

ALERT_RE = re.compile(r"<blockquote>\s*<p>\[!(\w+)\]\s*(.*?)</p>", re.S)
NOMBRES = {"NOTE": "Note", "TIP": "Tip", "IMPORTANT": "Important", "WARNING": "Warning", "CAUTION": "Caution"}


def repo_root(hasta: Path) -> Path:
    """Sube desde el archivo hasta la raíz del repositorio (donde está scripts/)."""
    for padre in [hasta] + list(hasta.parents):
        if (padre / "scripts" / "build_index.py").exists():
            return padre
    return hasta.parent


def leer_md(path: Path) -> tuple[dict, str]:
    texto = path.read_text(encoding="utf-8")
    campos: dict[str, str] = {}
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", texto, re.S)
    if m:
        for linea in m.group(1).splitlines():
            if ":" in linea:
                k, v = linea.split(":", 1)
                campos[k.strip()] = v.strip()
        texto = texto[m.end():]
    return campos, texto


def meta_tabla(campos: dict) -> str:
    filas = "".join(
        f"<tr><th>{html.escape(k)}</th><td>{html.escape(v)}</td></tr>" for k, v in campos.items()
    )
    return f'<table class="meta">{filas}</table>'


def render(campos: dict, cuerpo: str, aviso: str) -> str:
    md = markdown.Markdown(extensions=["tables", "fenced_code", "attr_list", "sane_lists", "md_in_html"])
    html_cuerpo = md.convert(cuerpo)

    def alerta(m):
        tipo = m.group(1).upper()
        titulo = NOMBRES.get(tipo, tipo.title())
        contenido = m.group(2)
        return (
            f'<div class="alert alert-{tipo.lower()}">'
            f"<p><strong>{titulo}</strong></p><p>{contenido}</p></div>"
        )

    html_cuerpo = ALERT_RE.sub(alerta, html_cuerpo)
    html_cuerpo = html_cuerpo.replace('src="../../assets/', 'src="assets/')
    return (
        f'<div class="hoja"><div class="aviso">{aviso}</div>{meta_tabla(campos)}{html_cuerpo}</div>'
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("archivo")
    ap.add_argument("--out-dir", default=None)
    args = ap.parse_args()

    src = Path(args.archivo).resolve()
    campos, cuerpo = leer_md(src)
    out_dir = Path(args.out_dir).resolve() if args.out_dir else src.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    aviso_previo = (
        "Vista previa de trabajo. Lo de arriba es el frontmatter, que GitHub muestra siempre como tabla "
        "al principio de la página. Los bloques [!NOTE] aparecen en GitHub en color; aquí se reproducen."
    )
    cuerpo_comun = render(campos, cuerpo, "<strong>GitHub, tema oscuro</strong> — " + aviso_previo)
    cuerpo_paleta = render(
        campos,
        cuerpo,
        "<strong>Con la paleta del atlas</strong> — " + aviso_previo
        + " Aquí las negritas van en azul tinta y los títulos en azul profundo: es lo que se vería con hoja de estilo propia.",
    )

    for nombre, cuerpo_html, css in (
        ("preview-github.html", cuerpo_comun, CSS_OSCURO),
        ("preview-paleta.html", cuerpo_paleta, CSS_PALETA),
    ):
        destino = out_dir / nombre
        destino.write_text(
            "<!doctype html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\">\n"
            f"<title>{html.escape(src.stem)} — {nombre}</title>\n"
            f"<style>{CSS_BASE}{css}</style>\n</head>\n<body>\n{cuerpo_html}\n</body>\n</html>\n",
            encoding="utf-8",
        )
        print(destino)

    # las bandas SVG se referencian con rutas relativas: se copian junto a la vista previa
    raiz = repo_root(src)
    for svg in (raiz / "assets" / "bandas").glob("banda-*.svg"):
        copia = out_dir / "assets" / "bandas"
        copia.mkdir(parents=True, exist_ok=True)
        (copia / svg.name).write_text(svg.read_text(encoding="utf-8"), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())