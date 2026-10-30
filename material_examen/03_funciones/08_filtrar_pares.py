"""
TEMA 5 - Ejercicio 8: Procesando listas en funciones
====================================================
ENUNCIADO (literal del profesor):
    "Desarrolla una función llamada filtrar_pares que reciba una lista de
    números enteros. La función debe iterar sobre la lista y retornar una nueva
    lista que contenga únicamente los números pares."

FORMA QUE EXIGE EL PROFESOR:
    - "iterar sobre la lista" => recorrerla con un for.
    - "retornar una NUEVA lista" => return de una lista nueva (no modificar
      la original ni imprimir dentro).

CONCEPTOS QUE PRACTICA:
    - Crear lista vacía y rellenarla con .append().
    - Operador módulo %: n % 2 == 0 => n es par.

CÓMO EJECUTARLO:  python 08_filtrar_pares.py   (en Linux/Docker: python3 08_filtrar_pares.py)
"""


# ---------------------------------------------------------------
# PASO 1: Definir la función
# ---------------------------------------------------------------
def filtrar_pares(numeros):
    """Devuelve una lista NUEVA solo con los números pares de 'numeros'."""
    pares = []                    # Lista nueva vacía donde iremos guardando
    for numero in numeros:        # Iteramos la lista elemento a elemento
        if numero % 2 == 0:       # Resto 0 al dividir entre 2 => es par
            pares.append(numero)  # append añade al final de la lista
    return pares                  # Fuera del for: devolvemos la lista completa


# ---------------------------------------------------------------
# PASO 2: Pruebas
# ---------------------------------------------------------------
if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultado = filtrar_pares(lista)
    print(f"Lista original: {lista}")       # La original no cambia
    print(f"Solo pares:     {resultado}")
    print(f"Sin pares:      {filtrar_pares([1, 3, 5])}")   # Caso límite -> []

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# Lista original: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Solo pares:     [2, 4, 6, 8, 10]
# Sin pares:      []
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Crear pares = [] DENTRO del for: se vaciaría en cada vuelta.
# - Borrar los impares de la lista original mientras la recorres: da
#   resultados raros y además el enunciado pide una lista NUEVA.
# ALTERNATIVA (funciona y es muy pythónica, pero el enunciado dice "iterar",
#   así que en el examen usa el for):
#   return [n for n in numeros if n % 2 == 0]          # comprensión de lista
#   return list(filter(lambda n: n % 2 == 0, numeros)) # filter + lambda
