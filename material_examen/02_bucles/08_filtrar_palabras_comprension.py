"""
TEMA 4 - Ejercicio 8: List comprehensions con condicional
==========================================================
ENUNCIADO (literal del profesor):
    Dada la lista palabras = ["sol", "murciélago", "mar", "elefante", "luz"], usa una list
    comprehension para filtrar y guardar en una nueva lista solo las palabras que tengan
    más de 3 letras.

FORMA QUE EXIGE EL PROFESOR:
    - List comprehension con if (filtro), en una línea.

CONCEPTOS QUE PRACTICA:
    - Sintaxis con filtro: [expresion for elemento in iterable if condicion]
    - len(texto) devuelve el número de caracteres.

CÓMO EJECUTARLO:  python 08_filtrar_palabras_comprension.py   (en Linux/Docker: python3 08_filtrar_palabras_comprension.py)
"""

palabras = ["sol", "murciélago", "mar", "elefante", "luz"]

# ---------------------------------------------------------------
# LA LÍNEA QUE PIDE EL EJERCICIO
#   "p"                -> QUÉ guardo (la palabra tal cual)
#   "for p in palabras" -> recorro todas
#   "if len(p) > 3"     -> FILTRO: solo entra si tiene más de 3 letras
# El if va AL FINAL cuando sirve para filtrar (quitar elementos).
# ---------------------------------------------------------------
largas = [p for p in palabras if len(p) > 3]

print(f"Palabras de más de 3 letras: {largas}")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# Palabras de más de 3 letras: ['murciélago', 'elefante']
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - "más de 3" es > 3 (no >= 3; con >= 3 entrarían sol, mar y luz).
# - El if de FILTRO va al final y SIN else. Si pones if-else, va DELANTE del for
#   y sirve para transformar, no para filtrar:
#     [p.upper() if len(p) > 3 else p for p in palabras]
# ALTERNATIVA (funciona, pero NO es lo que pide: no es comprensión):
#     largas = []
#     for p in palabras:
#         if len(p) > 3:
#             largas.append(p)
