"""
TEMA 4 - Ejercicio 14: Cláusula else en bucles
===============================================
ENUNCIADO (literal del profesor):
    Busca el número 99 en la lista [...]. Si lo encuentras, imprime '¡Encontrado!' y sal
    del bucle. Si terminas de recorrer la lista y no está, usa el bloque else del bucle
    para imprimir 'Número no encontrado'.
    (La lista salió cortada en la fuente: uso [12, 45, 99, 7, 30] y pruebo también
    una lista sin el 99 para ver el else.)

FORMA QUE EXIGE EL PROFESOR:
    - for ... else (el else va pegado al FOR, no al if) + break.

CONCEPTOS QUE PRACTICA:
    - El else de un bucle se ejecuta SOLO si el bucle terminó "normalmente",
      es decir, SIN haber hecho break.
    - Si hay break, el else se salta.
    - Truco para recordarlo: piensa en el else del bucle como "si no hubo break".

CÓMO EJECUTARLO:  python 14_buscar_99_for_else.py   (en Linux/Docker: python3 14_buscar_99_for_else.py)
"""

# ---------------------------------------------------------------
# CASO 1: la lista SÍ contiene el 99
# ---------------------------------------------------------------
numeros = [12, 45, 99, 7, 30]
buscado = 99

for numero in numeros:
    if numero == buscado:
        print("¡Encontrado!")
        break               # salgo: no hace falta mirar el resto (7 y 30)
else:
    # ATENCIÓN A LA SANGRÍA: este else está a la altura del 'for',
    # NO del 'if'. Solo se ejecuta si el for llegó al final sin break.
    print("Número no encontrado")

# ---------------------------------------------------------------
# CASO 2 (prueba extra): una lista SIN el 99 -> el bucle no hace break,
# termina de recorrerla entera y entonces SÍ entra en el else.
# ---------------------------------------------------------------
otros_numeros = [1, 2, 3, 4, 5]

for numero in otros_numeros:
    if numero == buscado:
        print("¡Encontrado!")
        break
else:
    print("Número no encontrado")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# ¡Encontrado!
# Número no encontrado
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Poner el else a la altura del if (if/else normal): imprimiría
#   "Número no encontrado" por CADA número que no sea 99. ¡Eso NO es lo que piden!
# - Olvidar el break: el else se ejecutaría SIEMPRE (el bucle nunca se interrumpe).
# - El while también admite else, con la misma regla.
# EN JAVA: no existe; habría que usar una variable boolean encontrado = false.
# ALTERNATIVAS (funcionan, pero NO son lo que pide: no usan el else del bucle):
#     if 99 in numeros:
#         print("¡Encontrado!")
#     else:
#         print("Número no encontrado")
#     # o una bandera: encontrado = False ... if not encontrado: ...
