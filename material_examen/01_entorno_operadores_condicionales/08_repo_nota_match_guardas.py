"""
TEMA 3 - Ejercicio de clase 0: Nota con match y guardas
=======================================================
ENUNCIADO (del repo de clase):
    Un programa que lea una nota por teclado con match: si la nota es menor
    que 5 está suspendido; si es entre 5 y 7 aprobado, sin incluir el 7; de 7
    a 8,5 notable, sin incluir el 8,5; y de 8,5 a 10 sobresaliente, los dos
    incluidos. Además, si la nota es negativa o mayor que 10 es un error de dato.

FORMA QUE EXIGE EL PROFESOR:
    - match con GUARDAS  (case n if condición:)  y  case _  al final.
    - El caso de error se comprueba PRIMERO.

CONCEPTOS QUE PRACTICA:
    - input() + float(), match con guardas, rangos semiabiertos, orden de los case.

CÓMO EJECUTARLO:  python 08_repo_nota_match_guardas.py   (en Linux/Docker: python3 ...)
"""

# ---------------------------------------------------------------
# PASO 1: ENTRADA. float() porque la nota puede llevar decimales (8.5).
# OJO: el decimal se escribe con PUNTO (8.5), no con coma (8,5 -> ValueError).
# ---------------------------------------------------------------
nota = float(input("Introduce una nota: "))

# ---------------------------------------------------------------
# PASO 2: match con guardas. "n" captura el valor de nota y el "if"
# decide si ese case vale. Se evalúan en orden y gana el primero True,
# así que cada case solo necesita el límite SUPERIOR:
#   - Si llega a "n < 7" ya sabemos que n >= 5 (si no, habría entrado antes).
# Tabla de rangos:
#   [0, 5)     Suspenso
#   [5, 7)     Aprobado       (7 no incluido)
#   [7, 8.5)   Notable        (8.5 no incluido)
#   [8.5, 10]  Sobresaliente  (ambos incluidos)
# ---------------------------------------------------------------
match nota:
    case n if n < 0 or n > 10:
        # Va PRIMERO: si no, un -3 entraría en "n < 5" y diría Suspenso.
        # Aquí "or" es correcto: son dos zonas separadas, no un rango.
        print("Error: nota fuera de rango")
    case n if n < 5:
        print("Suspenso")
    case n if n < 7:
        print("Aprobado")
    case n if n < 8.5:
        print("Notable")
    case n if n <= 10:
        print("Sobresaliente")
    case _:
        # Nunca se llega con números válidos, pero el profesor exige el comodín.
        print("Entrada no reconocida")

# ---------------------------------------------------------------
# SALIDA ESPERADA (ejemplos):
# 4.9 -> Suspenso | 5 -> Aprobado | 7 -> Notable | 8.5 -> Sobresaliente
# 10 -> Sobresaliente | 11 -> Error: nota fuera de rango | -1 -> Error: nota fuera de rango
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - En la versión original se escribía "case nota if ...": funciona, pero
#   reutiliza el nombre de la variable evaluada; mejor un nombre corto (n).
# - Faltaba el case _ en la versión original: añádelo siempre.
# - Si escriben letras, float() lanza ValueError (se controla con try/except).
# - Variante con encadenada (también válida): case n if 5 <= n < 7:
# ALTERNATIVA (funciona, pero NO es lo que pide el enunciado):
#   if nota < 0 or nota > 10: ... elif nota < 5: ... -> se pide match.
