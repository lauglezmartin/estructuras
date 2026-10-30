"""
TEMA 4 - Ejercicio 6: Bucles for anidados
==========================================
ENUNCIADO (literal del profesor):
    Una tienda de ropa ofrece camisetas en dos tallas (M, L) y tres colores (Rojo, Azul, Negro).
    Genera y muestra todas las combinaciones posibles.

FORMA QUE EXIGE EL PROFESOR:
    - Bucles for ANIDADOS (un for dentro de otro).

CONCEPTOS QUE PRACTICA:
    - Por cada vuelta del bucle de fuera, el de dentro da TODAS sus vueltas.
    - Nº total de combinaciones = 2 tallas x 3 colores = 6.

CÓMO EJECUTARLO:  python 06_combinaciones_anidados.py   (en Linux/Docker: python3 06_combinaciones_anidados.py)
"""

# ---------------------------------------------------------------
# PASO 1: los datos en dos listas
# ---------------------------------------------------------------
tallas = ["M", "L"]
colores = ["Rojo", "Azul", "Negro"]

# ---------------------------------------------------------------
# PASO 2: bucles anidados
# Bucle de FUERA: tallas (2 vueltas).
# Bucle de DENTRO: colores (3 vueltas por cada talla).
# Fíjate en la sangría: el for de colores está DENTRO del de tallas.
# Llevo un contador para numerar y comprobar que salen 6.
# ---------------------------------------------------------------
contador = 0
for talla in tallas:
    for color in colores:
        contador += 1
        print(f"{contador}. Camiseta talla {talla} - color {color}")

print(f"Total de combinaciones: {contador}")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# 1. Camiseta talla M - color Rojo
# 2. Camiseta talla M - color Azul
# 3. Camiseta talla M - color Negro
# 4. Camiseta talla L - color Rojo
# 5. Camiseta talla L - color Azul
# 6. Camiseta talla L - color Negro
# Total de combinaciones: 6
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Si el segundo for no tiene sangría, NO está anidado: se ejecuta después
#   y solo combina la última talla.
# - Usar la misma variable en los dos for (for x ... for x ...) machaca la de fuera.
# ALTERNATIVA (funciona, pero NO es lo que pide: comprensión en vez de bucles anidados):
#     combinaciones = [(t, c) for t in tallas for c in colores]
