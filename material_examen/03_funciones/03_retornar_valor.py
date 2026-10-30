"""
TEMA 5 - Ejercicio 3: Retornar un valor
=======================================
ENUNCIADO (literal del profesor):
    "Desarrolla una función llamada multiplicar que reciba dos números como
    argumentos y retorne (usando return) el resultado de multiplicarlos. No
    debe imprimir el resultado dentro de la función."

FORMA QUE EXIGE EL PROFESOR:
    - OBLIGATORIO usar return.
    - PROHIBIDO poner print() dentro de la función. El print va FUERA,
      en el código que la llama.

CONCEPTOS QUE PRACTICA:
    - return: la función DEVUELVE un valor al que la llamó.
    - Diferencia return (devuelve, se puede guardar) vs print (solo muestra).

CÓMO EJECUTARLO:  python 03_retornar_valor.py   (en Linux/Docker: python3 03_retornar_valor.py)
"""


# ---------------------------------------------------------------
# PASO 1: Definir la función que DEVUELVE el producto
# ---------------------------------------------------------------
def multiplicar(a, b):
    """Devuelve el producto de a por b. No imprime nada."""
    # return termina la función y entrega el valor a quien la llamó.
    # NADA de print aquí: así el resultado se puede reutilizar.
    return a * b


# ---------------------------------------------------------------
# PASO 2: Pruebas (el print va FUERA de la función)
# ---------------------------------------------------------------
if __name__ == "__main__":
    resultado = multiplicar(6, 7)          # Guardamos lo que devuelve
    print(f"6 x 7 = {resultado}")

    # Como devuelve un valor, podemos usarlo en otras operaciones:
    doble = multiplicar(3, 4) * 2
    print(f"(3 x 4) x 2 = {doble}")

    # También funciona con decimales
    print(f"2.5 x 4 = {multiplicar(2.5, 4)}")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# 6 x 7 = 42
# (3 x 4) x 2 = 24
# 2.5 x 4 = 10.0
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Poner print(a * b) dentro de la función en vez de return: "funciona"
#   en pantalla, pero la función devuelve None y PIERDES PUNTOS porque el
#   enunciado lo prohíbe.
#       def multiplicar(a, b):
#           print(a * b)         # MAL: devuelve None
#       x = multiplicar(2, 3)    # imprime 6, pero x vale None
# - Código después de return dentro de la función nunca se ejecuta.
# EN JAVA SERÍA... int multiplicar(int a, int b) { return a * b; }
