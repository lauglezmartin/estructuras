"""
TEMA 5 - Ejercicio 13: Uso de map() con lambda
==============================================
ENUNCIADO (literal del profesor):
    "Dada la lista numeros = [...], utiliza la función incorporada map() junto
    con una función lambda para generar una nueva lista que contenga los
    números de la lista original elevados al cuadrado."
    (La lista salió cortada en la fuente: uso [1, 2, 3, 4, 5].)

FORMA QUE EXIGE EL PROFESOR:
    - Exactamente:  list(map(lambda x: x**2, numeros))
    - map + lambda + list (para convertir el resultado en lista).

CONCEPTOS QUE PRACTICA:
    - lambda: función anónima de UNA expresión:  lambda parametro: resultado
    - map(funcion, iterable): aplica la función a CADA elemento.
    - map devuelve un objeto "map" (perezoso): hay que pasarlo por list().

CÓMO EJECUTARLO:  python 13_map_lambda.py   (en Linux/Docker: python3 13_map_lambda.py)
"""


# ---------------------------------------------------------------
# PASO 1: Datos
# ---------------------------------------------------------------
numeros = [1, 2, 3, 4, 5]

# ---------------------------------------------------------------
# PASO 2: map + lambda (LA FORMA QUE PIDE EL PROFESOR)
# ---------------------------------------------------------------
# lambda x: x**2  -> "una función que recibe x y devuelve x al cuadrado"
# map(...)        -> se la aplica a 1, 2, 3, 4 y 5
# list(...)       -> convierte el objeto map en una lista de verdad
cuadrados = list(map(lambda x: x**2, numeros))

print(f"Original:  {numeros}")
print(f"Cuadrados: {cuadrados}")

# Para que veas por qué hace falta list():
print(map(lambda x: x**2, numeros))   # Muestra <map object at 0x...>, no los números

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# Original:  [1, 2, 3, 4, 5]
# Cuadrados: [1, 4, 9, 16, 25]
# <map object at 0x...>     (la dirección cambia en cada ejecución)
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Olvidar list() -> imprimes "<map object ...>" en vez de la lista.
# - map(numeros, lambda x: x**2) -> orden al revés: PRIMERO la función,
#   DESPUÉS la lista.
# - x^2 NO es potencia en Python (es XOR a nivel de bits). Potencia: x**2.
# - La lista original NO se modifica: map genera valores nuevos.
# EN JAVA SERÍA... numeros.stream().map(x -> x * x).toList()
# ALTERNATIVAS (funcionan, pero NO son lo que pide el enunciado):
#   cuadrados = [x**2 for x in numeros]       # comprensión de lista
#   cuadrados = []                            # bucle for clásico
#   for x in numeros:
#       cuadrados.append(x**2)
