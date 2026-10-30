"""Junta todo el material de ejercicios/ en un único HTML (y PDF con Edge)."""
import html
import io
import keyword
import re
import subprocess
import sys
import tokenize
from pathlib import Path

RAIZ = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
SALIDA_HTML = RAIZ / "APUNTES_COMPLETOS.html"
SALIDA_PDF = RAIZ / "APUNTES_COMPLETOS.pdf"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

TITULOS = {
    "01_entorno_operadores_condicionales": "1-3 · Entorno, operadores y condicionales",
    "02_bucles": "4 · Bucles",
    "03_funciones": "5 · Funciones",
    "04_clases_listas_diccionarios_lambda": "6 · Clases, listas de objetos, diccionarios, comprensiones y lambda",
    "05_variantes_tipo_examen": "Variantes tipo examen (todo mezclado)",
    "06_chuleta_y_kit_examen": "Kit de examen: plantillas, errores y checklist",
}
BUILTINS = {"print", "input", "len", "range", "enumerate", "int", "float", "str",
            "list", "dict", "set", "tuple", "sum", "min", "max", "sorted", "map",
            "filter", "zip", "round", "abs", "isinstance", "type", "super", "bool"}


def resaltar_python(codigo: str) -> str:
    """Colorea código Python con el tokenizador de la biblioteca estándar."""
    lineas = codigo.splitlines(keepends=True)
    offsets = [0]
    for linea in lineas:
        offsets.append(offsets[-1] + len(linea))
    partes, pos = [], 0
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(codigo).readline))
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return html.escape(codigo)
    for tok in tokens:
        ini = offsets[tok.start[0] - 1] + tok.start[1]
        fin = offsets[tok.end[0] - 1] + tok.end[1]
        if ini < pos:
            continue
        partes.append(html.escape(codigo[pos:ini]))
        texto = html.escape(codigo[ini:fin])
        clase = None
        if tok.type == tokenize.COMMENT:
            clase = "c"
        elif tok.type == tokenize.STRING or tok.type in (
                getattr(tokenize, "FSTRING_START", -1), getattr(tokenize, "FSTRING_MIDDLE", -1),
                getattr(tokenize, "FSTRING_END", -1)):
            clase = "s"
        elif tok.type == tokenize.NAME and keyword.iskeyword(tok.string):
            clase = "k"
        elif tok.type == tokenize.NAME and tok.string in BUILTINS:
            clase = "b"
        elif tok.type == tokenize.NUMBER:
            clase = "n"
        partes.append(f'<span class="{clase}">{texto}</span>' if clase else texto)
        pos = fin
    partes.append(html.escape(codigo[pos:]))
    return "".join(partes)


def inline_md(texto: str) -> str:
    t = html.escape(texto)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    return t


def md_a_html(md: str) -> str:
    """Conversor mínimo de Markdown: títulos, tablas, listas, código y párrafos."""
    out, lineas, i = [], md.splitlines(), 0
    while i < len(lineas):
        linea = lineas[i]
        if linea.startswith("```"):
            lang = linea[3:].strip()
            bloque = []
            i += 1
            while i < len(lineas) and not lineas[i].startswith("```"):
                bloque.append(lineas[i])
                i += 1
            codigo = "\n".join(bloque)
            cuerpo = resaltar_python(codigo) if lang in ("python", "py") else html.escape(codigo)
            out.append(f"<pre>{cuerpo}</pre>")
        elif linea.lstrip().startswith("|"):
            filas = []
            while i < len(lineas) and lineas[i].lstrip().startswith("|"):
                celdas = [c.strip() for c in lineas[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in celdas if c):
                    filas.append(celdas)
                i += 1
            i -= 1
            if filas:
                cab = "".join(f"<th>{inline_md(c)}</th>" for c in filas[0])
                cuerpo = "".join("<tr>" + "".join(f"<td>{inline_md(c)}</td>" for c in f) + "</tr>"
                                 for f in filas[1:])
                out.append(f"<table><tr>{cab}</tr>{cuerpo}</table>")
        elif m := re.match(r"(#{1,6})\s+(.*)", linea):
            nivel = min(len(m.group(1)) + 2, 6)
            out.append(f"<h{nivel}>{inline_md(m.group(2))}</h{nivel}>")
        elif re.match(r"\s*([-*]|\d+\.)\s+", linea):
            items = []
            while i < len(lineas) and re.match(r"\s*([-*]|\d+\.)\s+", lineas[i]):
                items.append(re.sub(r"\s*([-*]|\d+\.)\s+", "", lineas[i], count=1))
                i += 1
            i -= 1
            out.append("<ul>" + "".join(f"<li>{inline_md(x)}</li>" for x in items) + "</ul>")
        elif linea.strip():
            out.append(f"<p>{inline_md(linea)}</p>")
        i += 1
    return "\n".join(out)


def main():
    indice, cuerpo = [], []
    for carpeta in sorted(p for p in RAIZ.iterdir() if p.is_dir() and p.name in TITULOS):
        titulo = TITULOS[carpeta.name]
        ancla = carpeta.name
        sub = []
        secciones = []
        for f in sorted(carpeta.iterdir()):
            if f.suffix not in (".py", ".md"):
                continue
            id_f = f"{ancla}-{f.stem}"
            sub.append(f'<li><a href="#{id_f}">{html.escape(f.name)}</a></li>')
            texto = f.read_text(encoding="utf-8")
            contenido = (f"<pre>{resaltar_python(texto)}</pre>" if f.suffix == ".py"
                         else f'<div class="md">{md_a_html(texto)}</div>')
            secciones.append(f'<section class="archivo" id="{id_f}"><h3>📄 {carpeta.name}/{html.escape(f.name)}</h3>{contenido}</section>')
        indice.append(f'<li><a href="#{ancla}"><b>{html.escape(titulo)}</b></a><ul>{"".join(sub)}</ul></li>')
        cuerpo.append(f'<h2 class="tema" id="{ancla}">{html.escape(titulo)}</h2>' + "".join(secciones))

    pagina = f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>Apuntes de Python</title><style>
body{{font-family:Segoe UI,Arial,sans-serif;margin:24px;color:#1d2330;font-size:12px}}
h1{{color:#2b4c9b}} h2.tema{{background:#2b4c9b;color:#fff;padding:8px 12px;border-radius:6px;page-break-before:always}}
h3{{color:#2b4c9b;border-bottom:2px solid #c9d4ef;padding-bottom:3px;margin-top:22px}}
pre{{background:#f6f8fc;border:1px solid #dde3f0;border-radius:6px;padding:10px;white-space:pre-wrap;word-wrap:break-word;font-family:Consolas,monospace;font-size:10.5px;line-height:1.35}}
.c{{color:#2e7d32;font-style:italic}} .s{{color:#b3541e}} .k{{color:#7b1fa2;font-weight:bold}} .b{{color:#1565c0}} .n{{color:#00838f}}
table{{border-collapse:collapse;margin:8px 0;font-size:11px}} td,th{{border:1px solid #c9d4ef;padding:4px 6px;vertical-align:top}} th{{background:#e8eefb}}
code{{background:#eef1f8;padding:0 3px;border-radius:3px;font-family:Consolas,monospace}}
.indice li{{margin:2px 0}} a{{color:#2b4c9b;text-decoration:none}}
@media print{{section.archivo h3{{page-break-after:avoid}}}}
</style></head><body>
<h1>🐍 Apuntes de Python para el examen</h1>
<p>Todo el material en un solo documento. Usa <b>Ctrl+F</b> para buscar una palabra (p. ej. <code>enumerate</code>, <code>match</code>, <code>lambda</code>, <code>__str__</code>). La chuleta resumida está aparte en <code>06_chuleta_y_kit_examen/chuleta_python.pdf</code>.</p>
<h2>Índice</h2><ul class="indice">{"".join(indice)}</ul>
{"".join(cuerpo)}
</body></html>"""
    SALIDA_HTML.write_text(pagina, encoding="utf-8")
    subprocess.run([EDGE, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={SALIDA_PDF}", SALIDA_HTML.as_uri()], check=True,
                   capture_output=True, timeout=180)
    print("OK", SALIDA_HTML, SALIDA_PDF, SALIDA_PDF.stat().st_size)


if __name__ == "__main__":
    main()
