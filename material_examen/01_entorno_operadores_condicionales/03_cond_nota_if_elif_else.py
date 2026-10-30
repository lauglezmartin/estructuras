"""
TEMA 3 - Ejercicio 1: Clasificación escolar con if-elif-else
============================================================
ENUNCIADO (literal del profesor):
    "Dada la variable nota = 75, clasificar mediante condicionales encadenados:
    if nota >= 90: 'Excelente', elif nota >= 75: 'Muy bien', elif nota >= 60:
    'Bien', elif nota >= 40: 'Suficiente', else: 'Insuficiente'."

FORMA QUE EXIGE EL PROFESOR:
    - Cadena if / elif / else (un solo bloque, NO varios if sueltos).
    - Ordenado de MAYOR a MENOR para poder usar solo ">=".

CONCEPTOS QUE PRACTICA:
    - if-elif-else, operador >=, orden de las condiciones.

CÓMO EJECUTARLO:  python 03_cond_nota_if_elif_else.py   (en Linux/Docker: python3 ...)
"""

# ---------------------------------------------------------------
# PASO 1: el dato viene dado en una variable (no se pide input).
# ---------------------------------------------------------------
nota = 75

# ---------------------------------------------------------------
# PASO 2: cadena if-elif-else.
# Python evalúa de arriba abajo y entra SOLO en la primera condición True;
# el resto se salta. Por eso basta con ">=": si llegamos a "nota >= 75"
# ya sabemos que nota < 90 (si no, habría entrado en la primera).
# "elif" = "else if" de Java, pero en una sola palabra.
# ---------------------------------------------------------------
if nota >= 90:
    print("Excelente")
elif nota >= 75:
    print("Muy bien")
elif nota >= 60:
    print("Bien")
elif nota >= 40:
    print("Suficiente")
else:  # cualquier valor < 40
    print("Insuficiente")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# Muy bien
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Si ordenas al revés (primero >= 40) un 95 diría "Suficiente".
# - Varios "if" sueltos en vez de elif: un 95 imprimiría 4 mensajes.
# - No olvides los dos puntos ":" al final de cada if/elif/else.
# EN JAVA SERÍA: if (nota >= 90) {...} else if (nota >= 75) {...} else {...}
