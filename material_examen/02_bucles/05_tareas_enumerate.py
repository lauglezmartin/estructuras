"""
TEMA 4 - Ejercicio 5: Bucle for con enumerate()
================================================
ENUNCIADO (literal del profesor):
    Tienes una lista de tareas pendientes: ["Comprar leche", "Llamar al médico", "Estudiar Python"].
    Imprímelas numeradas empezando desde el 1 para mostrarlas como una lista ordenada.

FORMA QUE EXIGE EL PROFESOR:
    - enumerate(tareas, start=1)

CONCEPTOS QUE PRACTICA:
    - enumerate() da en cada vuelta DOS cosas: (posición, elemento).
    - start=1 hace que la numeración empiece en 1 en vez de en 0.
    - Desempaquetado: "for numero, tarea in ..." recoge las dos cosas a la vez.

CÓMO EJECUTARLO:  python 05_tareas_enumerate.py   (en Linux/Docker: python3 05_tareas_enumerate.py)
"""

# ---------------------------------------------------------------
# PASO 1: los datos
# ---------------------------------------------------------------
tareas = ["Comprar leche", "Llamar al médico", "Estudiar Python"]

# ---------------------------------------------------------------
# PASO 2: recorrer con enumerate
# enumerate(tareas, start=1) produce: (1, "Comprar leche"), (2, "Llamar..."), ...
# Con dos variables en el for, Python separa cada pareja:
#   numero <- 1, 2, 3      tarea <- el texto
# Sin start=1 empezaría en 0 (como los índices) y saldría "0. Comprar leche".
# ---------------------------------------------------------------
print("Tareas pendientes:")
for numero, tarea in enumerate(tareas, start=1):
    print(f"{numero}. {tarea}")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# Tareas pendientes:
# 1. Comprar leche
# 2. Llamar al médico
# 3. Estudiar Python
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - El orden es (número, elemento): "for tarea, numero in ..." los cambia de sitio.
# ALTERNATIVAS (funcionan, pero NO son lo que pide el enunciado):
#     for i in range(len(tareas)):
#         print(f"{i + 1}. {tareas[i]}")
#     # o bien enumerate(tareas) sin start y luego {i + 1}
