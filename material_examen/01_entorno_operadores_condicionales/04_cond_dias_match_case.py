"""
TEMA 3 - Ejercicio 2: Menú de días con match-case
=================================================
ENUNCIADO (literal del profesor):
    "Dada la variable dia_numero = 3, evaluar con la estructura match
    dia_numero: case 1: 'Lunes', case 2: 'Martes', case 3: 'Miércoles',
    case 4: 'Jueves', case 5: 'Viernes', case _: 'Día no válido o fin de semana'."

FORMA QUE EXIGE EL PROFESOR:
    - OBLIGATORIO match-case (Python 3.10+).
    - OBLIGATORIA la cláusula comodín  case _:  al final.

CONCEPTOS QUE PRACTICA:
    - match / case con patrones literales, comodín _.

CÓMO EJECUTARLO:  python 04_cond_dias_match_case.py   (en Linux/Docker: python3 ...)
"""

# ---------------------------------------------------------------
# PASO 1: el dato a evaluar.
# ---------------------------------------------------------------
dia_numero = 3

# ---------------------------------------------------------------
# PASO 2: match compara dia_numero con cada case de arriba abajo
# y ejecuta el PRIMERO que coincide. No hace falta "break" como en el
# switch de Java: nunca "se cae" al siguiente case.
# ---------------------------------------------------------------
match dia_numero:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case _:
        # _ es el COMODÍN: coincide con cualquier cosa (como "default" en Java).
        # Debe ir el ÚLTIMO: si lo pones antes, Python da SyntaxError
        # ("wildcard makes remaining patterns unreachable").
        print("Día no válido o fin de semana")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# Miércoles
# (con dia_numero = 6 -> Día no válido o fin de semana)
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Falta el case _: el profesor lo exige; sin él, un 6 no imprime nada.
# - Si el número viene de input(), conviértelo con int(): "3" no coincide con case 3.
# - match necesita Python 3.10 o superior (comprueba con python --version).
# EN JAVA SERÍA: switch (diaNumero) { case 1: ...; break; default: ... }
# ALTERNATIVA (funciona, pero NO es lo que pide el enunciado):
#   if dia_numero == 1: ... elif dia_numero == 2: ... else: ...
