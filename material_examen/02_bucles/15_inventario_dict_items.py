"""
TEMA 4 - Ejercicio 15: Bucle for con diccionarios
==================================================
ENUNCIADO (literal del profesor):
    Tienes el inventario de una tienda de frutas en un diccionario:
    {"manzanas": 50, "peras": 30, "naranjas": 20}. Itera sobre el diccionario e imprime
    tanto la clave como el valor en una frase descriptiva.

FORMA QUE EXIGE EL PROFESOR:
    - Recorrer el diccionario con .items() para tener clave y valor a la vez.

CONCEPTOS QUE PRACTICA:
    - .items()  -> parejas (clave, valor)   -> for clave, valor in d.items()
    - .keys()   -> solo las claves          (es lo que da "for clave in d")
    - .values() -> solo los valores

CÓMO EJECUTARLO:  python 15_inventario_dict_items.py   (en Linux/Docker: python3 15_inventario_dict_items.py)
"""

# ---------------------------------------------------------------
# PASO 1: el diccionario  { clave: valor, ... }
# clave = nombre de la fruta, valor = unidades en stock.
# ---------------------------------------------------------------
inventario = {"manzanas": 50, "peras": 30, "naranjas": 20}

# ---------------------------------------------------------------
# PASO 2: recorrer con .items()
# Cada vuelta da una pareja ("manzanas", 50) y el for la separa en
# dos variables (desempaquetado), igual que con enumerate.
# ---------------------------------------------------------------
print("Inventario de la frutería:")
for fruta, cantidad in inventario.items():
    print(f"Tenemos {cantidad} unidades de {fruta}.")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# Inventario de la frutería:
# Tenemos 50 unidades de manzanas.
# Tenemos 30 unidades de peras.
# Tenemos 20 unidades de naranjas.
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - "for fruta, cantidad in inventario:" (sin .items()) da ValueError: recorrer
#   un diccionario directamente solo da las CLAVES.
# - .items lleva paréntesis: inventario.items()
# EN JAVA SERÍA: for (Map.Entry<String,Integer> e : inventario.entrySet()) { ... }
# ALTERNATIVA (funciona, pero NO es la forma recomendada; mejor .items()):
#     for fruta in inventario:
#         print(f"Tenemos {inventario[fruta]} unidades de {fruta}.")
