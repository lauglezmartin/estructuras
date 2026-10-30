"""
TEMA 4 - Ejercicio 12: Bucle while True con break
==================================================
ENUNCIADO (literal del profesor):
    Crea un bucle infinito que funcione como una calculadora de sumas continuas.
    El programa pide un número. Si el usuario escribe 'salir', el bucle se interrumpe
    con break y muestra el total.

FORMA QUE EXIGE EL PROFESOR:
    - while True (bucle infinito a propósito) + break para salir.

CONCEPTOS QUE PRACTICA:
    - while True: la condición siempre es verdadera; la ÚNICA salida es un break.
    - break: corta el bucle en ese momento y salta a la primera línea de después.
    - Comprobar 'salir' ANTES de convertir a número (si no, int("salir") revienta).
    - Acumulador (total).

CÓMO EJECUTARLO:  python 12_calculadora_while_true_break.py   (en Linux/Docker: python3 12_calculadora_while_true_break.py)
"""

# ---------------------------------------------------------------
# PASO 1: el acumulador, antes del bucle
# ---------------------------------------------------------------
total = 0

print("Calculadora de sumas. Escribe 'salir' para terminar.")

# ---------------------------------------------------------------
# PASO 2: el bucle infinito
# while True no termina solo. ¿CÓMO EVITO QUE SEA INFINITO DE VERDAD?
# Tiene que haber un break que se pueda alcanzar: aquí, cuando escriben 'salir'.
# ---------------------------------------------------------------
while True:
    # Leo como TEXTO. .strip() quita espacios sobrantes y .lower()
    # permite que "SALIR" o " Salir " también funcionen.
    entrada = input("Número (o 'salir'): ").strip().lower()

    # 1º) ¿Quiere salir? Esto va PRIMERO: si hiciera int(entrada) antes,
    #     int("salir") daría ValueError y el programa se pararía con error.
    if entrada == "salir":
        break   # sale del while; continúa en el print del PASO 3

    # 2º) No es 'salir' -> lo trato como número y lo acumulo.
    numero = float(entrada)   # float para admitir también decimales (2.5)
    total += numero
    print(f"  Total parcial: {total}")

# ---------------------------------------------------------------
# PASO 3: después del break llegamos aquí
# ---------------------------------------------------------------
print(f"Total final: {total}")

# ---------------------------------------------------------------
# SALIDA ESPERADA (escribiendo 10, 5.5, 4.5, salir):
# Calculadora de sumas. Escribe 'salir' para terminar.
# Número (o 'salir'):   Total parcial: 10.0
# Número (o 'salir'):   Total parcial: 15.5
# Número (o 'salir'):   Total parcial: 20.0
# Número (o 'salir'): Total final: 20.0
# Caso límite: si escribe 'salir' a la primera -> Total final: 0
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Poner el int()/float() antes del if 'salir' -> ValueError al escribir salir.
# - Olvidar el break -> bucle infinito de verdad (Ctrl + C para pararlo).
# - El break solo sale del bucle MÁS CERCANO (si hay bucles anidados, solo del de dentro).
#
# OPCIONAL (si quieres que NO se rompa cuando escriben letras que no son 'salir'):
#
# OPCIÓN A: .isdigit() -> True si TODOS los caracteres son dígitos 0-9.
#   Limitación: "-5" y "2.5" dan False (el signo y el punto no son dígitos),
#   así que solo sirve para enteros positivos.
#
#     if entrada.isdigit():
#         total += int(entrada)
#     else:
#         print("Eso no es un número. Prueba otra vez.")
#         continue   # vuelve al principio del while sin sumar
#
# OPCIÓN B: try / except -> intento convertir y, si falla, capturo el error.
#   Funciona con negativos y decimales.
#
#     try:
#         numero = float(entrada)
#     except ValueError:
#         print("Eso no es un número. Prueba otra vez.")
#         continue
#     total += numero
#
# ALTERNATIVA (funciona, pero NO es lo que pide: no usa while True + break):
#     entrada = input(...)
#     while entrada != "salir":
#         total += float(entrada)
#         entrada = input(...)
