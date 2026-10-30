"""
TEMA 5 - Ejercicio 15: Recursividad
===================================
ENUNCIADO (literal del profesor):
    "Escribe una función recursiva (una función que se llama a sí misma)
    llamada calcular_factorial que reciba un número entero positivo n y
    retorne su factorial. Recuerda establecer el caso base (el factorial de 0
    y 1 es 1) para evitar un bucle infinito."

FORMA QUE EXIGE EL PROFESOR:
    - Nombre exacto calcular_factorial (en tu repo la llamaste factorial: ¡ojo!).
    - RECURSIVA: debe llamarse a sí misma (nada de for/while).
    - Caso base: si n es 0 o 1 -> return 1.

CONCEPTOS QUE PRACTICA:
    - Caso base (cuándo PARAR) + caso recursivo (llamada con un problema más
      pequeño, n - 1).
    - Factorial: n! = n * (n-1) * ... * 1   y   0! = 1! = 1

CÓMO EJECUTARLO:  python 15_recursividad_factorial.py   (en Linux/Docker: python3 15_recursividad_factorial.py)
"""


# ---------------------------------------------------------------
# PASO 1: Función recursiva
# ---------------------------------------------------------------
def calcular_factorial(n: int) -> int:
    """Devuelve el factorial de n (entero >= 0) de forma recursiva."""
    # CASO BASE: detiene las llamadas. Sin él, se llamaría sin fin hasta
    # RecursionError (maximum recursion depth exceeded).
    if n == 0 or n == 1:
        return 1
    # CASO RECURSIVO: n! = n * (n-1)!  -> cada llamada acerca n al caso base
    return n * calcular_factorial(n - 1)


# ---------------------------------------------------------------
# TRAZA DE calcular_factorial(4)  (cómo se ejecuta por dentro)
# ---------------------------------------------------------------
# BAJADA (cada llamada espera a la siguiente):
#   calcular_factorial(4) -> 4 * calcular_factorial(3)
#     calcular_factorial(3) -> 3 * calcular_factorial(2)
#       calcular_factorial(2) -> 2 * calcular_factorial(1)
#         calcular_factorial(1) -> CASO BASE -> devuelve 1
# SUBIDA (se resuelven de abajo arriba):
#       calcular_factorial(2) = 2 * 1  = 2
#     calcular_factorial(3) = 3 * 2  = 6
#   calcular_factorial(4) = 4 * 6  = 24
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# PASO 2: Pruebas
# ---------------------------------------------------------------
if __name__ == "__main__":
    print(f"4! = {calcular_factorial(4)}")
    print(f"5! = {calcular_factorial(5)}")
    print(f"0! = {calcular_factorial(0)}")   # Caso base
    print(f"1! = {calcular_factorial(1)}")   # Caso base

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# 4! = 24
# 5! = 120
# 0! = 1
# 1! = 1
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Olvidar el return en el caso recursivo (poner solo
#   n * calcular_factorial(n - 1)) -> la función devuelve None.
# - Llamar con n en vez de n - 1 -> nunca llega al caso base: RecursionError.
# - Con un negativo (-3) tampoco llega nunca al caso base -> RecursionError.
#   Si te pidieran controlarlo:  if n < 0: return None   (antes del caso base)
# ALTERNATIVA (funciona, pero NO es lo que pide: no es recursiva):
#   resultado = 1
#   for i in range(2, n + 1):
#       resultado *= i
#   return resultado
