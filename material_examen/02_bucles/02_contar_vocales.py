"""
TEMA 4 - Ejercicio 2: Bucle for (iterar cadenas)
=================================================
ENUNCIADO (literal del profesor):
    Pide una palabra al usuario y cuenta cuántas vocales (a, e, i, o, u) contiene
    iterando letra por letra.

FORMA QUE EXIGE EL PROFESOR:
    - Recorrer el string letra por letra con un for (for letra in palabra).

CONCEPTOS QUE PRACTICA:
    - Un string se puede recorrer con for como si fuera una lista de letras.
    - Operador 'in' para preguntar "¿está esta letra dentro de este texto?".
    - Variable CONTADORA (suma 1 cada vez que pasa algo).

CÓMO EJECUTARLO:  python 02_contar_vocales.py   (en Linux/Docker: python3 02_contar_vocales.py)
"""

# ---------------------------------------------------------------
# PASO 1: pedir la palabra
# .lower() la pasa a minúsculas, así "Árbol" o "CASA" también cuentan
# sus vocales sin tener que comparar con "AEIOU".
# ---------------------------------------------------------------
palabra = input("Introduce una palabra: ").lower()

# ---------------------------------------------------------------
# PASO 2: preparar el CONTADOR y las vocales a buscar
# Un contador suma SIEMPRE 1 (cuenta cuántas veces ocurre algo).
# Incluyo las vocales con tilde y la ü para que "murciélago" cuente bien.
# ---------------------------------------------------------------
vocales = "aeiouáéíóúü"
contador_vocales = 0

# ---------------------------------------------------------------
# PASO 3: recorrer la palabra letra a letra
# En cada vuelta 'letra' es un string de 1 carácter.
# ---------------------------------------------------------------
for letra in palabra:
    if letra in vocales:       # ¿la letra está dentro de "aeiou..."?
        contador_vocales += 1  # sí -> sumo 1 al contador

# ---------------------------------------------------------------
# PASO 4: resultado (fuera del bucle)
# ---------------------------------------------------------------
print(f"La palabra '{palabra}' tiene {contador_vocales} vocales.")

# ---------------------------------------------------------------
# SALIDA ESPERADA (si escribo Murciélago):
# Introduce una palabra: La palabra 'murciélago' tiene 5 vocales.
# (Si escribo una palabra sin vocales, p. ej. "bsk", dice 0 vocales.)
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Sin .lower(), las mayúsculas no cuentan (o hay que poner "aeiouAEIOU").
# - Si el enunciado solo dice "a, e, i, o, u" y no quieres tildes, usa vocales = "aeiou".
# EN JAVA SERÍA: for (char letra : palabra.toCharArray()) { ... }
# ALTERNATIVA (funciona, pero NO es "iterando letra por letra" con un for clásico):
#     contador_vocales = sum(1 for letra in palabra if letra in vocales)
