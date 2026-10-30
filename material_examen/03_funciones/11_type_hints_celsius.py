"""
TEMA 5 - Ejercicio 11: Anotaciones de tipo (Type Hints)
=======================================================
ENUNCIADO (literal del profesor):
    "Escribe la función para pasar de celsius_a_fahrenheit. Incluye Type Hints
    (anotaciones de tipo) tanto para los parámetros de entrada como para el
    valor de retorno. Asegúrate de documentar la función usando un Docstring
    explicativo. Fahrenheit = (celsius * 9/5) + 32."

FORMA QUE EXIGE EL PROFESOR:
    - Type hints en el parámetro Y en el retorno:
          def celsius_a_fahrenheit(celsius: float) -> float:
      (en la solución del profesor aparece con el nombre
      celsius_a_fahrenheit_tipado; cualquiera de los dos vale si respeta la firma)
    - Docstring con triple comilla (tres comillas dobles al abrir y al cerrar)
      justo debajo del def.

CONCEPTOS QUE PRACTICA:
    - Anotaciones de tipo:  parametro: tipo   y   -> tipo_de_retorno
    - Docstrings y cómo consultarlos (help() o .__doc__).

CÓMO EJECUTARLO:  python 11_type_hints_celsius.py   (en Linux/Docker: python3 11_type_hints_celsius.py)
"""


# ---------------------------------------------------------------
# PASO 1: Función con type hints y docstring
# ---------------------------------------------------------------
# celsius: float  -> se espera un número decimal como entrada
# -> float        -> la función devuelve un número decimal
def celsius_a_fahrenheit(celsius: float) -> float:
    """
    Convierte una temperatura de grados Celsius a grados Fahrenheit.

    Fórmula: Fahrenheit = (celsius * 9/5) + 32

    Args:
        celsius (float): Temperatura en grados Celsius.

    Returns:
        float: Temperatura equivalente en grados Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


# ---------------------------------------------------------------
# PASO 2: Pruebas
# ---------------------------------------------------------------
if __name__ == "__main__":
    print(f"0 °C = {celsius_a_fahrenheit(0)} °F")         # Punto de congelación
    print(f"100 °C = {celsius_a_fahrenheit(100)} °F")     # Punto de ebullición
    print(f"36.5 °C = {celsius_a_fahrenheit(36.5):.1f} °F")  # :.1f -> 1 decimal
    print(f"-40 °C = {celsius_a_fahrenheit(-40)} °F")     # Curiosidad: coinciden

    # Extra, no necesario: el docstring se puede leer desde el programa
    # (help(celsius_a_fahrenheit) también lo muestra).
    print(celsius_a_fahrenheit.__doc__.strip().splitlines()[0])

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# 0 °C = 32.0 °F
# 100 °C = 212.0 °F
# 36.5 °C = 97.7 °F
# -40 °C = -40.0 °F
# Convierte una temperatura de grados Celsius a grados Fahrenheit.
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Los type hints NO obligan: Python no da error si pasas un int o incluso
#   un str (fallaría luego al operar). Son documentación para personas y
#   herramientas, no comprobación como en Java.
# - El docstring debe ser lo PRIMERO dentro de la función; un comentario #
#   NO es un docstring.
# - 9/5 en Python 3 vale 1.8 (en Java 9/5 con enteros daría 1).
# EN JAVA SERÍA... double celsiusAFahrenheit(double celsius) — allí el tipo es
#   obligatorio y se comprueba al compilar.
