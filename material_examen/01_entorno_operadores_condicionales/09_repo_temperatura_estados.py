"""
TEMA 3 - Ejercicio de clase 1: Verificador de rangos y estilo de comparación
============================================================================
ENUNCIADO (del repo de clase):
    En Java, para comprobar si una temperatura T está en un rango seguro entre
    18 ºC y 27 ºC, escribirías if (temp >= 18 && temp <= 27). Escribe un
    programa en Python que pida al usuario una temperatura flotante e indique
    si la temperatura está en estado ÓPTIMO (18 <= T <= 27), ALERTA FRÍO (T < 18)
    o ALERTA CALOR (T > 27).
    Requisito: debes utilizar la sintaxis de comparaciones encadenadas directa
    de Python en lugar del operador and tradicional para el rango óptimo.

FORMA QUE EXIGE EL PROFESOR:
    - Rango óptimo con comparación ENCADENADA: 18 <= temp <= 27
    - PROHIBIDO: temp >= 18 and temp <= 27

CONCEPTOS QUE PRACTICA:
    - input() + float(), if/elif/else, comparación encadenada.

CÓMO EJECUTARLO:  python 09_repo_temperatura_estados.py   (en Linux/Docker: python3 ...)
"""

# ---------------------------------------------------------------
# PASO 1: ENTRADA. input() devuelve str; float() permite decimales (22.5).
# ---------------------------------------------------------------
temp = float(input("Introduce una temperatura en grados Celsius: "))

# ---------------------------------------------------------------
# PASO 2: el rango óptimo se pregunta PRIMERO y con la forma exigida
# (encadenada). Así queda claro en el código que se cumple el requisito.
# Los otros dos casos son lo que queda: si no está en [18, 27] y es
# menor que 18 -> frío; si no, calor.
# ---------------------------------------------------------------
if 18 <= temp <= 27:
    print("ESTADO: ÓPTIMO")
elif temp < 18:
    print("ESTADO: ALERTA FRÍO")
else:  # temp > 27
    print("ESTADO: ALERTA CALOR")

# ---------------------------------------------------------------
# SALIDA ESPERADA (ejemplos):
# 22.5 -> ESTADO: ÓPTIMO | 18 -> ESTADO: ÓPTIMO | 27 -> ESTADO: ÓPTIMO
# 17.9 -> ESTADO: ALERTA FRÍO | 27.1 -> ESTADO: ALERTA CALOR
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Los mensajes del enunciado son "ALERTA FRÍO" / "ALERTA CALOR"; respétalos.
# - Escribe el decimal con punto: 22.5 (22,5 -> ValueError).
# EN JAVA SERÍA: if (temp >= 18 && temp <= 27) -> en Python se escribe encadenado.
# ALTERNATIVA (funciona, pero el profesor la PROHÍBE):
#   if temp >= 18 and temp <= 27:
