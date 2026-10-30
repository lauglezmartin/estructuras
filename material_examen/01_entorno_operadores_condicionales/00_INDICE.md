# Índice - Temas 1, 2 y 3: Entorno, Operadores y Condicionales

| Archivo | Qué pide | Forma exigida | Conceptos clave |
|---|---|---|---|
| `00_entorno_comandos.md` | Chuleta de entorno | En Linux se ejecuta con `python3`; proyectos en `~/`, nunca en `/mnt/c` | .py, terminal Ctrl+ñ, pip/uv, venv, Docker/WSL, PS1, `__main__` |
| `01_entorno_hola_mundo.py` | Tema 1 Ej. 1: Hola, Mundo | `python` (Win/mac) / `python3` (Linux) | print(), ejecutar desde la terminal |
| `02_operadores.py` | Tema 2 Ej. 1-3: mayoría de edad EPS, `verificar_acceso`, == vs is + demo | Entrada-Proceso-Salida; paridad con `%`; `==` contenido, `is` identidad (no existe `===`) | input/int, %, ==, is, aritméticos, lógicos, truthy/falsy, in, ternario, int/float/str, round |
| `03_cond_nota_if_elif_else.py` | Tema 3 Ej. 1: clasificar nota = 75 | if / elif / else de mayor a menor | orden de condiciones |
| `04_cond_dias_match_case.py` | Tema 3 Ej. 2: día de la semana | match-case obligatorio + `case _` | patrones literales, comodín |
| `05_cond_paquetes_match_guardas.py` | Tema 3 Ej. 3: paquete por peso | guardas `case p if ...` + `case _` | patrón de captura, guarda, encadenada |
| `06_cond_temperatura_encadenada.py` | Tema 3 Ej. 4: temp en [18.0, 27.0] | `18.0 <= temp <= 27.0` (prohibido `and`) | comparación encadenada |
| `07_cond_raiz_guard_clause.py` | Tema 3 Ej. 5: `calcular_raiz_cuadrada(x)` | guard clause `if x <= 0: ...; return` sin else | return temprano, `** 0.5` |
| `08_repo_nota_match_guardas.py` | Clase 0: nota con match | match con guardas, error primero, `case _` | float(input()), rangos semiabiertos |
| `09_repo_temperatura_estados.py` | Clase 1: ÓPTIMO / FRÍO / CALOR | encadenada `18 <= temp <= 27` (prohibido `and`) | float(input()), if/elif/else |
| `10_repo_saneamiento_entrada.py` | Clase 2: validar nombre y CP | `.strip()`, `if not nombre_limpio:`, `.isdigit()` | métodos de str, falsy |
| `11_repo_comparacion_lexicografica.py` | Clase 3: qué producto va antes | 1ª comparación directa, 2ª con `.lower()` | orden Unicode, 'A' < 'a' |
| `12_repo_http_match_agrupado.py` | Clase 4: categorías HTTP | match con `case 200 \| 201:` agrupados + `case _` | patrón OR `\|` |
| `99_resumen_formas_exigidas.py` | Plantillas mínimas para copiar | todas las anteriores | if/elif/else, ternario, encadenada, match, `\|`, guardas, guard clause |
