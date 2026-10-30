"""
TEMA 4 - Ejercicio 3: Bucle for con range()
============================================
ENUNCIADO (literal del profesor):
    Genera la tabla de multiplicar del 8, desde el 1 hasta el 10 usando la función range().

FORMA QUE EXIGE EL PROFESOR:
    - Usar range() en el for.

CONCEPTOS QUE PRACTICA:
    - range(inicio, fin): genera números desde 'inicio' hasta 'fin - 1'
      (el final NO se incluye).

CÓMO EJECUTARLO:  python 03_tabla_del_8_range.py   (en Linux/Docker: python3 03_tabla_del_8_range.py)
"""

# ---------------------------------------------------------------
# PASO 1: el número de la tabla
# Guardarlo en una variable permite cambiar de tabla tocando una sola línea.
# ---------------------------------------------------------------
numero = 8
print(f"Tabla del {numero}:")

# ---------------------------------------------------------------
# PASO 2: recorrer del 1 al 10
# range(1, 11) -> 1, 2, 3, ..., 10. Pongo 11 porque el final se EXCLUYE.
# Si pusiera range(1, 10) me faltaría el 8 x 10 (error típico).
# ---------------------------------------------------------------
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# Tabla del 8:
# 8 x 1 = 8
# 8 x 2 = 16
# ...
# 8 x 10 = 80
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - range(10) empieza en 0 y llega a 9: saldría 8 x 0 y faltaría 8 x 10.
# EN JAVA SERÍA: for (int i = 1; i <= 10; i++) { ... }
