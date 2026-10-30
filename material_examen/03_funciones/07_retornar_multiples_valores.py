"""
TEMA 5 - Ejercicio 7: Retornar múltiples valores
================================================
ENUNCIADO (literal del profesor):
    "Crea una función llamada obtener_extremos que reciba una lista de números
    como parámetro. La función debe encontrar y retornar simultáneamente el
    valor mínimo y el valor máximo de la lista utilizando retornos múltiples
    (una tupla). Luego, escribe un código de prueba que llame a la función
    pasándole una lista de ejemplo (como [...]), desempaquete los resultados en
    dos variables separadas e imprima por pantalla un mensaje mostrando ambos
    valores."
    (La lista de ejemplo salió cortada en la fuente: uso [4, 8, 15, 16, 23, 42].)

FORMA QUE EXIGE EL PROFESOR:
    - Retorno múltiple en tupla:  return min(lista), max(lista)
    - Desempaquetado en DOS variables:  minimo, maximo = obtener_extremos(...)
    - Imprimir un mensaje con ambos valores (fuera de la función).

CONCEPTOS QUE PRACTICA:
    - "return a, b" devuelve una TUPLA (a, b) aunque no pongas paréntesis.
    - Desempaquetado de tuplas.
    - Funciones integradas min() y max().

CÓMO EJECUTARLO:  python 07_retornar_multiples_valores.py   (en Linux/Docker: python3 07_retornar_multiples_valores.py)
"""


# ---------------------------------------------------------------
# PASO 1: Función que devuelve DOS valores a la vez
# ---------------------------------------------------------------
def obtener_extremos(lista):
    """Devuelve una tupla (mínimo, máximo) de la lista de números."""
    # La coma crea una tupla: esto equivale a return (min(lista), max(lista))
    return min(lista), max(lista)


# ---------------------------------------------------------------
# PASO 2: Prueba con desempaquetado
# ---------------------------------------------------------------
if __name__ == "__main__":
    numeros = [4, 8, 15, 16, 23, 42]

    # Desempaquetado: el 1er valor de la tupla va a minimo y el 2º a maximo.
    # Tiene que haber tantas variables como valores devuelve la función.
    minimo, maximo = obtener_extremos(numeros)
    print(f"El valor mínimo es {minimo} y el máximo es {maximo}")

    # Para ver que realmente es una tupla:
    resultado = obtener_extremos(numeros)
    print(resultado, type(resultado))

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# El valor mínimo es 4 y el máximo es 42
# (4, 42) <class 'tuple'>
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - minimo, maximo, otro = obtener_extremos(...) -> ValueError (not enough
#   values to unpack): el número de variables debe coincidir.
# - Con una lista vacía, min() y max() lanzan ValueError. Si te lo pidieran,
#   comprueba antes:  if not lista: return None, None
# EN JAVA SERÍA... Java no puede devolver dos valores: habría que devolver un
#   array o un objeto. En Python basta con separar por comas.
# ALTERNATIVA (funciona, pero NO es lo que pide: no usa el retorno múltiple
#   desempaquetado):  res = obtener_extremos(n); print(res[0], res[1])
