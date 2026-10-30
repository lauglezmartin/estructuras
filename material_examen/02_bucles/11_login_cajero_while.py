"""
TEMA 4 - Ejercicio 11: Bucle while con condición compleja
==========================================================
ENUNCIADO (literal del profesor):
    Simula el login de un cajero. El usuario debe ingresar su PIN ('1234'). El bucle termina
    cuando acierta el PIN o cuando se superan los 3 intentos máximos permitidos.

FORMA QUE EXIGE EL PROFESOR:
    - while con una condición COMPUESTA (dos condiciones unidas con and).

CONCEPTOS QUE PRACTICA:
    - Operadores lógicos en la condición del while: and / or / not.
    - Contador de intentos para garantizar que el bucle termina.
    - Después del bucle, averiguar POR QUÉ terminó (¿acertó o se quedó sin intentos?).

CÓMO EJECUTARLO:  python 11_login_cajero_while.py   (en Linux/Docker: python3 11_login_cajero_while.py)
"""

# ---------------------------------------------------------------
# PASO 1: datos y variables de control
# El PIN se compara como TEXTO ('1234' entre comillas, como en el
# enunciado), así no hace falta int() y no falla si escriben letras.
# ---------------------------------------------------------------
PIN_CORRECTO = "1234"
MAX_INTENTOS = 3

intentos = 0     # CONTADOR de intentos usados
pin = ""         # vacío para que la primera vez la condición sea True

# ---------------------------------------------------------------
# PASO 2: la condición compleja
# El enunciado dice cuándo TERMINA: "acierta  O  se acaban los intentos".
# El while necesita cuándo SIGUE, que es lo contrario:
#     NO acierta  Y  le quedan intentos
#     pin != PIN_CORRECTO  and  intentos < MAX_INTENTOS
# (Regla de De Morgan: lo contrario de "A or B" es "no A and no B".)
#
# ¿CÓMO EVITO EL BUCLE INFINITO? 'intentos' sube 1 en cada vuelta, así
# que como mucho habrá 3 vueltas aunque nunca acierte.
# ---------------------------------------------------------------
while pin != PIN_CORRECTO and intentos < MAX_INTENTOS:
    pin = input("Introduce tu PIN: ")
    intentos += 1
    if pin != PIN_CORRECTO:
        restantes = MAX_INTENTOS - intentos
        print(f"PIN incorrecto. Intentos restantes: {restantes}")

# ---------------------------------------------------------------
# PASO 3: ¿por qué ha salido del bucle?
# Hay dos motivos posibles, así que lo compruebo con un if.
# ---------------------------------------------------------------
if pin == PIN_CORRECTO:
    print(f"PIN correcto. Acceso concedido (intentos usados: {intentos}).")
else:
    print("Has superado los 3 intentos. Tarjeta bloqueada.")

# ---------------------------------------------------------------
# SALIDA ESPERADA 1 (escribiendo 1111, 1234):
# Introduce tu PIN: PIN incorrecto. Intentos restantes: 2
# Introduce tu PIN: PIN correcto. Acceso concedido (intentos usados: 2).
#
# SALIDA ESPERADA 2 (escribiendo 0000, 1111, 2222):
# Introduce tu PIN: PIN incorrecto. Intentos restantes: 2
# Introduce tu PIN: PIN incorrecto. Intentos restantes: 1
# Introduce tu PIN: PIN incorrecto. Intentos restantes: 0
# Has superado los 3 intentos. Tarjeta bloqueada.
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Poner "or" en la condición del while: con un PIN malo seguiría para siempre
#   (porque pin != PIN_CORRECTO es True aunque se acaben los intentos).
# - intentos <= 3 daría 4 oportunidades.
# - Comparar con el número 1234 (sin comillas): input() devuelve texto y "1234" != 1234.
# EN JAVA SERÍA: while (!pin.equals("1234") && intentos < 3) { ... }
