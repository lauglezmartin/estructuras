"""
TEMA 4 - Ejercicio 13: Uso de continue
=======================================
ENUNCIADO (literal del profesor):
    Itera los números del 1 al 10 e imprímelos. Sin embargo, si el número es divisible
    por 3 (ej. 3, 6, 9), utiliza continue para saltarlo y no imprimirlo.

FORMA QUE EXIGE EL PROFESOR:
    - Usar continue.

CONCEPTOS QUE PRACTICA:
    - continue: se salta LO QUE QUEDA de la vuelta actual y pasa a la siguiente.
      (break, en cambio, sale del bucle entero.)
    - Divisible por 3  <=>  numero % 3 == 0  (el resto de dividir entre 3 es 0).

CÓMO EJECUTARLO:  python 13_saltar_multiplos_continue.py   (en Linux/Docker: python3 13_saltar_multiplos_continue.py)
"""

# ---------------------------------------------------------------
# range(1, 11) -> del 1 al 10 (el 11 no se incluye).
# Si el número es divisible por 3, continue hace que el print de abajo
# NO se ejecute en esa vuelta; el bucle sigue con el siguiente número.
# ---------------------------------------------------------------
for numero in range(1, 11):
    if numero % 3 == 0:
        continue          # salta el 3, el 6 y el 9
    print(numero)

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# 1
# 2
# 4
# 5
# 7
# 8
# 10
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Poner break en vez de continue: imprimiría 1, 2 y pararía en el 3.
# - Poner el print ANTES del if: imprimiría también los múltiplos de 3.
# - En un while, si el continue va antes de actualizar el contador, se crea un
#   bucle infinito (el contador no cambia nunca). En el for no pasa porque
#   range avanza solo.
# ALTERNATIVA (funciona, pero NO es lo que pide: no usa continue):
#     for numero in range(1, 11):
#         if numero % 3 != 0:
#             print(numero)
