"""
TEMA 4 - Ejercicio 9: Bucle while básico
=========================================
ENUNCIADO (literal del profesor):
    Pide al usuario que ingrese una contraseña. El programa debe seguir denegando el acceso
    y preguntando de nuevo hasta que el usuario escriba exactamente 'python123'.

FORMA QUE EXIGE EL PROFESOR:
    - Bucle while con condición (no sabemos cuántas veces se repetirá).

CONCEPTOS QUE PRACTICA:
    - while condicion: se repite MIENTRAS la condición sea True.
    - Cuándo usar while y no for: cuando NO sé de antemano cuántas vueltas habrá.
    - Cómo evitar un bucle infinito: la variable de la condición debe cambiar DENTRO del bucle.

CÓMO EJECUTARLO:  python 09_contrasena_while.py   (en Linux/Docker: python3 09_contrasena_while.py)
"""

# ---------------------------------------------------------------
# PASO 1: pedir la contraseña UNA vez ANTES del bucle
# El while comprueba la condición al principio, así que la variable
# 'contrasena' tiene que existir ya antes de llegar a él.
# ---------------------------------------------------------------
CONTRASENA_CORRECTA = "python123"   # en MAYÚSCULAS porque es una constante

contrasena = input("Introduce la contraseña: ")

# ---------------------------------------------------------------
# PASO 2: el bucle while
# "Mientras lo escrito sea DISTINTO de la correcta, deniego y vuelvo a pedir".
# 'exactamente' -> comparo con != tal cual, sin .lower() ni .strip():
# "Python123" o "python123 " (con espacio) NO valen.
#
# ¿CÓMO EVITO EL BUCLE INFINITO? Dentro del bucle vuelvo a hacer input(),
# así 'contrasena' cambia y en algún momento la condición puede ser False.
# Si olvidara el input de dentro, preguntaría... nunca: repetiría
# "Acceso denegado" para siempre (Ctrl + C para cortarlo).
# ---------------------------------------------------------------
while contrasena != CONTRASENA_CORRECTA:
    print("Acceso denegado.")
    contrasena = input("Introduce la contraseña: ")

# ---------------------------------------------------------------
# PASO 3: si llego aquí es porque la condición del while fue False,
# o sea, la contraseña es la correcta.
# ---------------------------------------------------------------
print("Acceso concedido. ¡Bienvenida!")

# ---------------------------------------------------------------
# SALIDA ESPERADA (escribiendo: hola, Python123, python123):
# Introduce la contraseña: Acceso denegado.
# Introduce la contraseña: Acceso denegado.
# Introduce la contraseña: Acceso concedido. ¡Bienvenida!
# (En la consola real verás lo que escribes detrás de cada "contraseña: ")
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Usar == en vez de != en la condición: el bucle no se ejecutaría nunca con
#   contraseñas malas.
# - Olvidar el input() dentro del bucle -> bucle infinito.
# EN JAVA SERÍA: while (!contrasena.equals("python123")) { ... }
#   (en Python los strings se comparan con == / != directamente)
# ALTERNATIVA (funciona, pero aquí piden while básico con condición):
#     while True:
#         contrasena = input("Introduce la contraseña: ")
#         if contrasena == CONTRASENA_CORRECTA:
#             break
#         print("Acceso denegado.")
