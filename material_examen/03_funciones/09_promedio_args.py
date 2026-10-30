"""
TEMA 5 - Ejercicio 9: Número variable de argumentos (*args)
===========================================================
ENUNCIADO (literal del profesor):
    "Escribe una función llamada calcular_promedio que pueda recibir una
    cantidad indefinida de números utilizando *args. La función debe retornar
    la media de todos los números pasados como argumento."

FORMA QUE EXIGE EL PROFESOR:
    - OBLIGATORIO el parámetro *args (no vale recibir una lista).
    - Retornar (return) la media, no imprimirla dentro.

CONCEPTOS QUE PRACTICA:
    - *args: Python EMPAQUETA todos los argumentos posicionales en una TUPLA.
    - sum() y len() sobre esa tupla.
    - Evitar la división por cero si no llega ningún número.

CÓMO EJECUTARLO:  python 09_promedio_args.py   (en Linux/Docker: python3 09_promedio_args.py)
"""


# ---------------------------------------------------------------
# PASO 1: Función con *args
# ---------------------------------------------------------------
# El asterisco es lo importante; "args" es solo el nombre por convención.
# Si llamas calcular_promedio(4, 6, 8), dentro args == (4, 6, 8).
def calcular_promedio(*args):
    """Devuelve la media de todos los números recibidos (0 si no llega ninguno)."""
    # Si no llega ningún número, args es la tupla vacía () y len(args) es 0:
    # dividir entre 0 daría ZeroDivisionError, así que lo controlamos antes.
    if len(args) == 0:
        return 0
    # Media = suma de todos / cuántos hay
    return sum(args) / len(args)


# ---------------------------------------------------------------
# PASO 2: Pruebas con distinta cantidad de argumentos
# ---------------------------------------------------------------
if __name__ == "__main__":
    print(calcular_promedio(4, 6, 8))          # 3 argumentos
    print(calcular_promedio(10, 5))            # 2 argumentos
    print(calcular_promedio(7, 8, 9, 10, 6))   # 5 argumentos
    print(calcular_promedio())                 # Ninguno: no explota, devuelve 0

    # Si ya tienes una LISTA, la "desempaquetas" con * al llamar:
    notas = [5, 7, 9]
    print(calcular_promedio(*notas))

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# 6.0
# 7.5
# 8.0
# 0
# 7.0
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - calcular_promedio(notas) sin * -> args sería ([5, 7, 9],) (una tupla
#   con UNA lista dentro) y sum() fallaría con TypeError.
# - La división / SIEMPRE da float (6.0), aunque el resultado sea exacto.
# - Sin el if, calcular_promedio() -> ZeroDivisionError.
# EN JAVA SERÍA... double calcularPromedio(double... numeros) (varargs).
# ALTERNATIVA (funciona, pero NO es lo que pide: no usa *args):
#   def calcular_promedio(lista): return sum(lista) / len(lista)
