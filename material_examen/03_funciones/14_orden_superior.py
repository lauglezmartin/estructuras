"""
TEMA 5 - Ejercicio 14: Funciones de Orden Superior
==================================================
ENUNCIADO (literal del profesor):
    "Crea una función llamada aplicar_operacion que reciba tres parámetros:
    dos números y una función. aplicar_operacion debe ejecutar la función
    recibida pasándole los dos números como argumentos y retornar el
    resultado. Prueba tu función pasándole funciones creadas por ti para
    sumar y restar."

FORMA QUE EXIGE EL PROFESOR:
    - aplicar_operacion(a, b, funcion): el 3er parámetro es una FUNCIÓN.
    - Dentro: return funcion(a, b)
    - Probarla con funciones PROPIAS sumar y restar (definidas con def).

CONCEPTOS QUE PRACTICA:
    - En Python las funciones son valores: se pueden pasar como argumento.
    - Pasar la función SIN paréntesis (sumar), no llamarla (sumar()).

CÓMO EJECUTARLO:  python 14_orden_superior.py   (en Linux/Docker: python3 14_orden_superior.py)
"""


# ---------------------------------------------------------------
# PASO 1: Funciones "normales" que pasaremos como argumento
# ---------------------------------------------------------------
def sumar(a, b):
    """Devuelve a + b."""
    return a + b


def restar(a, b):
    """Devuelve a - b."""
    return a - b


# ---------------------------------------------------------------
# PASO 2: La función de orden superior
# ---------------------------------------------------------------
# "funcion" es un parámetro como otro cualquiera, pero lo que contiene
# es una función, así que podemos LLAMARLO con paréntesis: funcion(a, b).
def aplicar_operacion(a, b, funcion):
    """Ejecuta funcion(a, b) y devuelve su resultado."""
    return funcion(a, b)


# ---------------------------------------------------------------
# PASO 3: Pruebas
# ---------------------------------------------------------------
if __name__ == "__main__":
    # OJO: se pasa "sumar" SIN paréntesis -> pasamos la función, no su resultado
    print(f"10 + 3 = {aplicar_operacion(10, 3, sumar)}")
    print(f"10 - 3 = {aplicar_operacion(10, 3, restar)}")

    # Extra: también se le puede pasar una lambda (función anónima)
    print(f"10 x 3 = {aplicar_operacion(10, 3, lambda x, y: x * y)}")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# 10 + 3 = 13
# 10 - 3 = 7
# 10 x 3 = 30
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - aplicar_operacion(10, 3, sumar())  -> TypeError: sumar() se ejecutaría
#   sin argumentos. La función se pasa SIN ().
# - El orden de los parámetros importa: (a, b, funcion), la función la última
#   tal como dice el enunciado.
# EN JAVA SERÍA... int aplicarOperacion(int a, int b, BinaryOperator<Integer> f)
#   { return f.apply(a, b); }  — en Python no hace falta ninguna interfaz.
