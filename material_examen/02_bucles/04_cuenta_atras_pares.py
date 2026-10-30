"""
TEMA 4 - Ejercicio 4: Bucle for con paso personalizado
=======================================================
ENUNCIADO (literal del profesor):
    Crea una cuenta regresiva que imprima solamente los números pares desde el 20 hasta el 0.

FORMA QUE EXIGE EL PROFESOR:
    - range con TERCER argumento (paso): range(inicio, fin, paso). Paso negativo.

CONCEPTOS QUE PRACTICA:
    - range(inicio, fin, paso)
    - Paso negativo para contar hacia atrás (el inicio tiene que ser MAYOR que el fin).

CÓMO EJECUTARLO:  python 04_cuenta_atras_pares.py   (en Linux/Docker: python3 04_cuenta_atras_pares.py)
"""

# ---------------------------------------------------------------
# PASO 1: el range con paso
#   inicio = 20  -> el primer número que sale
#   fin    = -1  -> el final NO se incluye; para que el 0 SÍ salga,
#                   tengo que parar "uno más allá", o sea en -1
#   paso   = -2  -> resta 2 en cada vuelta: 20, 18, 16, ..., 0
# Como empiezo en un par y salto de 2 en 2, solo salen pares:
# no hace falta ningún if.
# ---------------------------------------------------------------
for numero in range(20, -1, -2):
    print(numero)

print("¡Despegue!")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# 20
# 18
# 16
# 14
# 12
# 10
# 8
# 6
# 4
# 2
# 0
# ¡Despegue!
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - range(20, 0, -2) NO imprime el 0 (el fin se excluye).
# - range(0, 20, -2) no imprime NADA: con paso negativo el inicio debe ser mayor.
# EN JAVA SERÍA: for (int i = 20; i >= 0; i -= 2) { ... }
# ALTERNATIVA (funciona, pero NO es lo que pide: no usa el paso personalizado):
#     for numero in range(20, -1, -1):
#         if numero % 2 == 0:
#             print(numero)
