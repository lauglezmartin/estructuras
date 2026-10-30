"""
TEMA 4 - Ejercicio 7: List comprehensions (básico)
===================================================
ENUNCIADO (literal del profesor):
    A partir de la lista numeros = [...], genera una nueva lista que contenga el cubo
    de cada número en una sola línea de código.
    (La lista salió cortada en la fuente: uso numeros = [1, 2, 3, 4, 5].)

FORMA QUE EXIGE EL PROFESOR:
    - Comprensión de listas en UNA SOLA LÍNEA.

CONCEPTOS QUE PRACTICA:
    - Sintaxis: [expresion for elemento in iterable]
    - Potencia con ** (n ** 3 = n al cubo).

CÓMO EJECUTARLO:  python 07_cubos_comprension.py   (en Linux/Docker: python3 07_cubos_comprension.py)
"""

numeros = [1, 2, 3, 4, 5]

# ---------------------------------------------------------------
# LA LÍNEA QUE PIDE EL EJERCICIO
# Se lee de izquierda a derecha así:
#   "n ** 3"        -> QUÉ meto en la lista nueva (el cubo)
#   "for n in numeros" -> DE DÓNDE saco cada n
# Los corchetes [] indican que el resultado es una lista nueva.
# La lista original 'numeros' no cambia.
# ---------------------------------------------------------------
cubos = [n ** 3 for n in numeros]

print(f"Números: {numeros}")
print(f"Cubos:   {cubos}")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# Números: [1, 2, 3, 4, 5]
# Cubos:   [1, 8, 27, 64, 125]
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - n ^ 3 NO es potencia en Python (es XOR a nivel de bits). Usa n ** 3.
# - Con paréntesis ( ) en vez de [ ] no obtienes una lista sino un generador.
# ALTERNATIVA (funciona, pero NO es lo que pide: no es una sola línea):
#     cubos = []
#     for n in numeros:
#         cubos.append(n ** 3)
