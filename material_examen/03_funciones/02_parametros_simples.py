"""
TEMA 5 - Ejercicio 2: Parámetros simples
========================================
ENUNCIADO (literal del profesor):
    "Crea una función llamada saludo_personalizado que reciba un parámetro
    nombre (cadena de texto) e imprima '¡Hola, [nombre]! Bienvenido al curso
    de Python'."

FORMA QUE EXIGE EL PROFESOR:
    - Función saludo_personalizado con UN parámetro llamado nombre.
    - Imprime dentro de la función (el enunciado dice "imprima").

CONCEPTOS QUE PRACTICA:
    - Parámetro (en la definición) vs argumento (el valor en la llamada).
    - f-strings para meter variables dentro del texto.

CÓMO EJECUTARLO:  python 02_parametros_simples.py   (en Linux/Docker: python3 02_parametros_simples.py)
"""


# ---------------------------------------------------------------
# PASO 1: Definir la función con un parámetro
# ---------------------------------------------------------------
# "nombre" es el PARÁMETRO: una variable que solo existe dentro de la
# función y que toma el valor que le pasemos al llamarla.
# ": str" es una pista de tipo (opcional): indica que se espera texto.
def saludo_personalizado(nombre: str):
    """Imprime un saludo de bienvenida con el nombre recibido."""
    # f-string: la f delante permite poner {variable} dentro del texto
    print(f"¡Hola, {nombre}! Bienvenido al curso de Python")


# ---------------------------------------------------------------
# PASO 2: Pruebas
# ---------------------------------------------------------------
if __name__ == "__main__":
    saludo_personalizado("Laura")   # "Laura" es el ARGUMENTO
    saludo_personalizado("Ana")     # Reutilizamos la misma función

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# ¡Hola, Laura! Bienvenido al curso de Python
# ¡Hola, Ana! Bienvenido al curso de Python
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Llamar saludo_personalizado() sin argumento -> TypeError: missing 1
#   required positional argument: 'nombre'.
# - Olvidar la f del f-string -> imprime literalmente "{nombre}".
# EN JAVA SERÍA... void saludoPersonalizado(String nombre). En Python el
#   tipo no es obligatorio (": str" es solo informativo).
