"""
TEMA 3 - Ejercicio de clase 3: Comparación lexicográfica y mayúsculas/minúsculas
================================================================================
ENUNCIADO (del repo de clase):
    Un sistema de catálogo necesita comparar dos nombres de productos (prod1 y
    prod2) introducidos por el usuario para determinar cuál aparecerá primero
    alfabéticamente.
    Requisitos:
    - Muestra qué producto va primero evaluando las cadenas directamente sin
      modificar (recordando que en ASCII 'A' < 'a').
    - A continuación, realiza una 2ª comparación insensible a
      mayúsculas/minúsculas empleando .lower().
    - Si ambas cadenas normalizadas son idénticas, indica que son el mismo
      producto independientemente de la caja (case-insensitive).

FORMA QUE EXIGE EL PROFESOR:
    - DOS comparaciones: 1ª directa (<, >, == sobre los str tal cual);
      2ª con .lower().
    - Comparar str con los operadores relacionales (no hace falta compareTo).

CONCEPTOS QUE PRACTICA:
    - Comparación lexicográfica (Unicode/ASCII), .lower(), .strip(), if-elif-else.

CÓMO EJECUTARLO:  python 11_repo_comparacion_lexicografica.py   (en Linux/Docker: python3 ...)
    Pide dos productos.
"""

# ---------------------------------------------------------------
# PASO 1: ENTRADA (sin tocar: la 1ª comparación es "en bruto").
# ---------------------------------------------------------------
prod1 = input("Introduce el primer producto: ")
prod2 = input("Introduce el segundo producto: ")

# ---------------------------------------------------------------
# PASO 2: comparación DIRECTA.
# Python compara carácter a carácter por su código Unicode (ord()).
# En cuanto encuentra una diferencia, decide. Las MAYÚSCULAS van antes
# que las minúsculas: ord('Z') = 90 < ord('a') = 97, así que "Zapato" < "abrigo".
# ---------------------------------------------------------------
print("\n--- 1. Comparación directa (ASCII) ---")
if prod1 < prod2:
    print(f"'{prod1}' va antes que '{prod2}'.")
elif prod1 > prod2:
    print(f"'{prod2}' va antes que '{prod1}'.")
else:
    print("Ambos productos son idénticos.")

# ---------------------------------------------------------------
# PASO 3: comparación NORMALIZADA. Con .lower() (y .strip() para quitar
# espacios sobrantes) ya no influye cómo se escribió.
# ---------------------------------------------------------------
prod1_norm = prod1.strip().lower()
prod2_norm = prod2.strip().lower()

print("\n--- 2. Comparación normalizada (ignorando mayúsculas/minúsculas) ---")
if prod1_norm < prod2_norm:
    print(f"'{prod1}' va antes que '{prod2}' (normalizado).")
elif prod1_norm > prod2_norm:
    print(f"'{prod2}' va antes que '{prod1}' (normalizado).")
else:
    print("Son el mismo producto independientemente de la caja (case-insensitive).")

# ---------------------------------------------------------------
# SALIDA ESPERADA (entradas "Pepe" y "pepe"):
# --- 1. Comparación directa (ASCII) ---
# 'Pepe' va antes que 'pepe'.
#
# --- 2. Comparación normalizada (ignorando mayúsculas/minúsculas) ---
# Son el mismo producto independientemente de la caja (case-insensitive).
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Las tildes van DESPUÉS de todas las letras: "ábaco" > "zorro" (ord('á') = 225).
# - Los números como texto se comparan por caracteres: "10" < "9" es True.
# EN JAVA SERÍA: prod1.compareTo(prod2) < 0 ; prod1.equalsIgnoreCase(prod2)
