"""
TEMA 5 - Ejercicio 1: Tu primera función
========================================
ENUNCIADO (literal del profesor):
    "Escribe una función llamada saludar_mundo que no reciba ningún parámetro
    y simplemente imprima en consola el mensaje '¡Hola, mundo de las funciones!'."

FORMA QUE EXIGE EL PROFESOR:
    - Función con nombre exacto saludar_mundo, SIN parámetros.
    - Aquí SÍ se imprime dentro de la función (lo pide el enunciado: "imprima").

CONCEPTOS QUE PRACTICA:
    - def, nombre en snake_case, paréntesis vacíos, dos puntos y sangría.
    - Diferencia entre DEFINIR una función y LLAMARLA.

CÓMO EJECUTARLO:  python 01_primera_funcion.py   (en Linux/Docker: python3 01_primera_funcion.py)
"""


# ---------------------------------------------------------------
# PASO 1: Definir la función
# ---------------------------------------------------------------
# "def" + nombre + () + ":"  ->  el cuerpo va sangrado 4 espacios.
# Definirla NO la ejecuta: solo la deja guardada para usarla después.
def saludar_mundo():
    """Imprime un saludo fijo por consola. No recibe parámetros."""
    print("¡Hola, mundo de las funciones!")


# ---------------------------------------------------------------
# PASO 2: Llamar a la función (pruebas)
# ---------------------------------------------------------------
# if __name__ == "__main__": hace que esto solo se ejecute cuando lanzas
# este archivo directamente (no si otro archivo lo importa).
if __name__ == "__main__":
    saludar_mundo()   # Los paréntesis son OBLIGATORIOS para ejecutarla

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# ¡Hola, mundo de las funciones!
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Escribir "saludar_mundo" sin () -> no se ejecuta nada (solo nombras
#   la función, no la llamas).
# - Olvidar los ":" tras def o no sangrar el cuerpo -> SyntaxError /
#   IndentationError.
# EN JAVA SERÍA... public static void saludarMundo() { System.out.println(...); }
#   En Python no hay tipo de retorno ni llaves: manda la sangría.
