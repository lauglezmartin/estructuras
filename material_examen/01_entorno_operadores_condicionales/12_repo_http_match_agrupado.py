"""
TEMA 3 - Ejercicio de clase 4: Manejador de respuestas HTTP con match-case
==========================================================================
ENUNCIADO (del repo de clase):
    Diseña un controlador de API REST que reciba un código de estado HTTP
    entero (por ejemplo: 200, 201, 400, 401, 403, 404, 500, 503) y devuelva
    una categoría estándar.
    Requisitos:
    - Usa una estructura match-case.
    - Agrupa en una sola rama (case 200 | 201:) las respuestas exitosas.
    - Agrupa en una sola rama los errores de cliente conocidos (400, 401, 403, 404).
    - Agrupa en una rama los errores de servidor (500, 503).
    - Usa el comodín "_" para capturar cualquier otro código no contemplado e
      informar de "Código de estado no reconocido".

FORMA QUE EXIGE EL PROFESOR:
    - match-case con PATRONES AGRUPADOS con |  (una rama por grupo).
    - case _ al final.

CONCEPTOS QUE PRACTICA:
    - Patrones literales, patrón OR (|), comodín, int(input()).

CÓMO EJECUTARLO:  python 12_repo_http_match_agrupado.py   (en Linux/Docker: python3 ...)
    Pide un código HTTP.
"""

# ---------------------------------------------------------------
# PASO 1: ENTRADA. int() porque los case comparan con números:
# el texto "200" NO coincidiría con case 200.
# ---------------------------------------------------------------
codigo_http = int(input("Introduce un código de estado HTTP (ej. 200, 404, 500): "))

# ---------------------------------------------------------------
# PASO 2: match con patrones agrupados.
# "|" dentro de un case significa "o": case 200 | 201 coincide con 200 O con 201.
# OJO: en un case se usa |, NUNCA "or" (case 200 or 201 es SyntaxError).
# ---------------------------------------------------------------
match codigo_http:
    case 200 | 201:
        print("Éxito: La solicitud se ha completado correctamente.")
    case 400 | 401 | 403 | 404:
        print("Error del cliente: Revise los datos o permisos enviados.")
    case 500 | 503:
        print("Error del servidor: Hubo un fallo en el sistema remoto.")
    case _:
        # Comodín: cualquier otro código (302, 418...). Es el "default" de Java.
        print("Código de estado no reconocido.")

# ---------------------------------------------------------------
# SALIDA ESPERADA (ejemplos):
# 201 -> Éxito: La solicitud se ha completado correctamente.
# 404 -> Error del cliente: Revise los datos o permisos enviados.
# 503 -> Error del servidor: Hubo un fallo en el sistema remoto.
# 418 -> Código de estado no reconocido.
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Una rama por código (case 400: ... case 401: ...) funciona, pero NO agrupa:
#   el enunciado pide una sola rama por grupo con |.
# - Si quisieras saber CUÁL coincidió: case 400 | 401 | 403 | 404 as codigo:
# EN JAVA SERÍA: switch (codigo) { case 200, 201 -> ...; default -> ...; }
# ALTERNATIVA (funciona, pero NO es lo que pide el enunciado):
#   if codigo_http in (200, 201): ... elif codigo_http in (400, 401, 403, 404): ...
