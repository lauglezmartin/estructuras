"""
TEMA 6 - Teoría-práctica 8: Comprensiones y lambda
==================================================
ENUNCIADO: Archivo de consulta. Comprensiones de listas (básica, con if, con
if-else) y de diccionario; lambda con map, filter, sorted, max y min. Cada
ejemplo va comparado con el for equivalente.

FORMA QUE EXIGE EL PROFESOR:
    - Filtrados y transformaciones "en una sola línea" -> COMPRENSIÓN DE LISTAS.
    - Elevar al cuadrado con map + lambda (Funciones ej. 13):
          cuadrados = list(map(lambda x: x**2, numeros))
    - Ordenar por un criterio: sorted(..., key=lambda ...) o lista.sort(key=...).
    - Si el enunciado dice "con map" o "con lambda", úsalos aunque una
      comprensión también funcione (y viceversa).

CONCEPTOS QUE PRACTICA:
    - [expresión for x in iterable]
    - [expresión for x in iterable if condición]       (FILTRA)
    - [valor_si for x in iterable ... ] con if-else ANTES del for (TRANSFORMA)
    - {clave: valor for x in iterable}
    - lambda parámetros: expresión
    - map, filter, sorted, max, min con key.

CÓMO EJECUTARLO:  python 08_comprensiones_y_lambda.py   (en Linux/Docker: python3 08_comprensiones_y_lambda.py)
"""

numeros = [1, 2, 3, 4, 5, 6]

# ---------------------------------------------------------------
# PASO 1: COMPRENSIÓN DE LISTAS BÁSICA
# ---------------------------------------------------------------
# Se lee: "dame n ** 3 PARA CADA n EN numeros".
print("=== 1. Comprensión básica: cubos (Bucles ej. 7) ===")
# Con for:
cubos_for = []
for n in numeros:
    cubos_for.append(n ** 3)
# Con comprensión (lo mismo en una línea):
cubos = [n ** 3 for n in numeros]
print(cubos_for)
print(cubos)

# La expresión puede ser cualquier cosa: métodos, f-strings...
palabras = ["sol", "murciélago", "mar", "elefante", "luz"]
print([p.upper() for p in palabras])
print([len(p) for p in palabras])

# ---------------------------------------------------------------
# PASO 2: COMPRENSIÓN CON if (FILTRAR) -> el if va AL FINAL
# ---------------------------------------------------------------
print("\n=== 2. Con if (filtra): pares y palabras largas ===")
# Con for:
pares_for = []
for n in numeros:
    if n % 2 == 0:
        pares_for.append(n)
# Con comprensión:
pares = [n for n in numeros if n % 2 == 0]
print(pares_for)
print(pares)
# Bucles ej. 8: palabras con más de 3 letras
largas = [p for p in palabras if len(p) > 3]
print(largas)

# ---------------------------------------------------------------
# PASO 3: COMPRENSIÓN CON if-else (TRANSFORMAR) -> va ANTES del for
# ---------------------------------------------------------------
# Aquí NO se quita ningún elemento: a cada uno se le da un valor u otro.
print("\n=== 3. Con if-else (transforma) ===")
# Con for:
tipos_for = []
for n in numeros:
    if n % 2 == 0:
        tipos_for.append("par")
    else:
        tipos_for.append("impar")
# Con comprensión:
tipos = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(tipos_for)
print(tipos)
# Otro: los negativos se convierten en 0
valores = [3, -1, 7, -5, 0]
print([v if v > 0 else 0 for v in valores])

# ---------------------------------------------------------------
# PASO 4: COMPRENSIÓN DE DICCIONARIO
# ---------------------------------------------------------------
print("\n=== 4. Comprensión de diccionario ===")
# Con for:
cuadrados_for = {}
for n in range(5):
    cuadrados_for[n] = n ** 2
# Con comprensión: {clave: valor for ...}
cuadrados_dict = {n: n ** 2 for n in range(5)}
print(cuadrados_for)
print(cuadrados_dict)
# Palabra -> longitud, solo las largas (con if al final, igual que en listas)
print({p: len(p) for p in palabras if len(p) > 3})
# Transformar un diccionario existente con .items(): precios con IVA
precios = {"pan": 1.0, "leche": 2.0, "café": 4.0}
print({prod: round(precio * 1.21, 2) for prod, precio in precios.items()})

# ---------------------------------------------------------------
# PASO 5: LAMBDA = FUNCIÓN ANÓNIMA DE UNA LÍNEA
# ---------------------------------------------------------------
# lambda parámetros: expresión   -> devuelve la expresión (sin escribir return).
print("\n=== 5. lambda ===")


def cuadrado(x):
    """Función normal equivalente a la lambda de abajo."""
    return x ** 2


cuadrado_lambda = lambda x: x ** 2      # (en la práctica no se guarda en variable)
suma = lambda a, b: a + b
print(cuadrado(4), cuadrado_lambda(4), suma(2, 3))

# ---------------------------------------------------------------
# PASO 6: map(función, lista) -> aplica la función a CADA elemento
# ---------------------------------------------------------------
print("\n=== 6. map + lambda (Funciones ej. 13) ===")
numeros_map = [1, 2, 3, 4, 5]
# Con for:
cuadrados_for = []
for x in numeros_map:
    cuadrados_for.append(x ** 2)
# Con map + lambda (FORMA EXIGIDA en el ej. 13). map devuelve un objeto
# "perezoso": hay que convertirlo con list() para verlo.
cuadrados = list(map(lambda x: x ** 2, numeros_map))
# Con comprensión (equivalente):
cuadrados_comp = [x ** 2 for x in numeros_map]
print(cuadrados_for)
print("Cuadrados: ", cuadrados)
print(cuadrados_comp)
print(type(map(lambda x: x ** 2, numeros_map)).__name__)  # sin list() es un objeto 'map', no una lista
print(list(map(str.upper, ["a", "b"])))                 # map con función ya existente

# ---------------------------------------------------------------
# PASO 7: filter(función, lista) -> se queda con los que devuelven True
# ---------------------------------------------------------------
print("\n=== 7. filter + lambda ===")
# Con for:
impares_for = []
for n in numeros:
    if n % 2 != 0:
        impares_for.append(n)
# Con filter + lambda:
impares = list(filter(lambda n: n % 2 != 0, numeros))
# Con comprensión:
impares_comp = [n for n in numeros if n % 2 != 0]
print(impares_for, impares, impares_comp)

# ---------------------------------------------------------------
# PASO 8: sorted / sort con key=lambda
# ---------------------------------------------------------------
# key = función que dice POR QUÉ dato comparar cada elemento.
print("\n=== 8. sorted con key ===")
print(sorted(palabras))                             # alfabético
print(sorted(palabras, key=lambda p: len(p)))       # por longitud
print(sorted(palabras, key=len, reverse=True))      # igual, con función existente, desc
alumnos = [("Ana", 8.5), ("Luis", 6.0), ("Eva", 9.2)]
print(sorted(alumnos, key=lambda a: a[1], reverse=True))   # por nota desc (posición 1)
peliculas = [{"titulo": "A", "rating": 8}, {"titulo": "B", "rating": 9}]
peliculas.sort(key=lambda p: p["rating"], reverse=True)    # sort cambia la MISMA lista
print(peliculas)
# Con for habría que programar el algoritmo de ordenación a mano: por eso se usa sorted.

# ---------------------------------------------------------------
# PASO 9: max / min con key
# ---------------------------------------------------------------
print("\n=== 9. max / min con key ===")
# Con for:
mejor = alumnos[0]
for a in alumnos:
    if a[1] > mejor[1]:
        mejor = a
print("Mejor (for):", mejor)
print("Mejor (max):", max(alumnos, key=lambda a: a[1]))
print("Peor (min):", min(alumnos, key=lambda a: a[1]))
print("Palabra más larga:", max(palabras, key=len))


# ---------------------------------------------------------------
# SALIDA ESPERADA:
# === 1. Comprensión básica: cubos (Bucles ej. 7) ===
# [1, 8, 27, 64, 125, 216]
# [1, 8, 27, 64, 125, 216]
# ['SOL', 'MURCIÉLAGO', 'MAR', 'ELEFANTE', 'LUZ']
# [3, 10, 3, 8, 3]
#
# === 2. Con if (filtra): pares y palabras largas ===
# [2, 4, 6]
# [2, 4, 6]
# ['murciélago', 'elefante']
#
# === 3. Con if-else (transforma) ===
# ['impar', 'par', 'impar', 'par', 'impar', 'par']
# ['impar', 'par', 'impar', 'par', 'impar', 'par']
# [3, 0, 7, 0, 0]
#
# === 4. Comprensión de diccionario ===
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# {'murciélago': 10, 'elefante': 8}
# {'pan': 1.21, 'leche': 2.42, 'café': 4.84}
#
# === 5. lambda ===
# 16 16 5
#
# === 6. map + lambda (Funciones ej. 13) ===
# [1, 4, 9, 16, 25]
# Cuadrados:  [1, 4, 9, 16, 25]
# [1, 4, 9, 16, 25]
# map
# ['A', 'B']
#
# === 7. filter + lambda ===
# [1, 3, 5] [1, 3, 5] [1, 3, 5]
#
# === 8. sorted con key ===
# ['elefante', 'luz', 'mar', 'murciélago', 'sol']
# ['sol', 'mar', 'luz', 'elefante', 'murciélago']
# ['murciélago', 'elefante', 'sol', 'mar', 'luz']
# [('Eva', 9.2), ('Ana', 8.5), ('Luis', 6.0)]
# [{'titulo': 'B', 'rating': 9}, {'titulo': 'A', 'rating': 8}]
#
# === 9. max / min con key ===
# Mejor (for): ('Eva', 9.2)
# Mejor (max): ('Eva', 9.2)
# Peor (min): ('Luis', 6.0)
# Palabra más larga: murciélago
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - if para FILTRAR va al FINAL: [x for x in l if cond]
#   if-else para TRANSFORMAR va DELANTE: [a if cond else b for x in l]
#   [x for x in l if cond else 0] -> SyntaxError.
# - map y filter devuelven un objeto, no una lista: envuélvelos en list().
# - lista.sort() devuelve None: no hagas nueva = lista.sort().
# - key=len (sin paréntesis): se pasa la función, no se llama.
# - Una lambda solo admite UNA expresión (sin return, sin varias líneas).
# - En sorted con empates se mantiene el orden original ('sol', 'mar', 'luz').
# EN JAVA SERÍA: lambda = x -> x * x ; map/filter = stream().map().filter().
# ALTERNATIVA: casi todo map/filter se puede hacer con comprensión (y al
# revés). Funciona igual, pero usa la forma que nombre el enunciado.
# ---------------------------------------------------------------
