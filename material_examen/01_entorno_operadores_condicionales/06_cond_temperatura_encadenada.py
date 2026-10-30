"""
TEMA 3 - Ejercicio 4: Rangos con comparaciones encadenadas
==========================================================
ENUNCIADO (literal del profesor):
    "Dada la variable temp = 22.5, comprobar si está en el rango [18.0, 27.0]
    utilizando la sintaxis encadenada: if 18.0 <= temp <= 27.0:
    'La temperatura es agradable.' else: 'Hace demasiado frío o demasiado calor.'"

FORMA QUE EXIGE EL PROFESOR:
    - Comparación ENCADENADA de estilo matemático:  18.0 <= temp <= 27.0
    - PROHIBIDO:  temp >= 18.0 and temp <= 27.0   (resta puntos aunque funcione)

CONCEPTOS QUE PRACTICA:
    - Comparación encadenada, intervalo cerrado [a, b] -> <= en ambos lados.

CÓMO EJECUTARLO:  python 06_cond_temperatura_encadenada.py   (en Linux/Docker: python3 ...)
"""

# ---------------------------------------------------------------
# PASO 1: el dato.
# ---------------------------------------------------------------
temp = 22.5

# ---------------------------------------------------------------
# PASO 2: comparación encadenada.
# Python permite escribir el rango como en matemáticas. Internamente
# hace "18.0 <= temp and temp <= 27.0", pero evalúa temp UNA sola vez
# y se lee mejor. Rango con corchetes [18.0, 27.0] = extremos INCLUIDOS,
# por eso <= en los dos lados.
# ---------------------------------------------------------------
if 18.0 <= temp <= 27.0:
    print("La temperatura es agradable.")
else:
    print("Hace demasiado frío o demasiado calor.")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# La temperatura es agradable.
# (con temp = 30 -> Hace demasiado frío o demasiado calor.)
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Usar < en vez de <=: 18.0 y 27.0 quedarían fuera y el rango es cerrado.
# - Para "fuera del rango" puedes negar todo: if not (18.0 <= temp <= 27.0):
# EN JAVA SERÍA: if (temp >= 18.0 && temp <= 27.0)  -> en Python NO se hace así.
# ALTERNATIVA (funciona, pero el profesor la PROHÍBE):
#   if temp >= 18.0 and temp <= 27.0:
