# Ejercicio 3: Comparación Lexicográfica y Mayúsculas/Minúscula
# Enunciado:
# Un sistema de catálogo necesita comparar dos nombres de productos (prod1 y prod2) introducidos por el usuario para determinar cuál aparecerá primero alfabéticamente.
# Conceptos aplicados: Comparación lexicográfica (ASCII/Unicode), ordenación relativa de caracteres, normalización con .lower().
# Requisitos:
# Muestra qué producto va primero evaluando las cadenas directamente sin modificar (recordando que en ASCII 'A' < 'a').
# A continuación, realiza una 2ª comparación insensible a mayúsculas/minúsculas empleando .lower().
# Si ambas cadenas normalizadas son idénticas, indica que son el mismo producto independientemente de la caja (case-insensitive).


# Primero hacemos la Lectura de datos
prod1 = input("Introduce el primer producto: ")
prod2 = input("Introduce el segundo producto: ")

# Aqui hacemos la comparación directa (ASCII) sin normalizar
# Python compara usando la tabla ASCII: las MAYÚSCULAS van antes que las minúsculas ('A' < 'a').
print("\n--- 1. Comparación directa (ASCII) ---")

if prod1 < prod2:
    print(f"'{prod1}' va antes que '{prod2}'.")
elif prod1 > prod2:
    print(f"'{prod2}' va antes que '{prod1}'.")
else:
    print("Ambos productos son idénticos.")

# Unificamos criterios con .strip() y .lower() para ignorar diferencias de mayúsculas/minúsculas.
prod1_norm = prod1.strip().lower()
prod2_norm = prod2.strip().lower()

print("\n--- 2. Comparación normalizada (Ignorando mayúsculas/minúsculas) ---")

if prod1_norm < prod2_norm:
    print(f"'{prod1}' va antes que '{prod2}' (normalizado).")
elif prod1_norm > prod2_norm:
    print(f"'{prod2}' va antes que '{prod1}' (normalizado).")
else:
    # Si tras normalizar son iguales, es el mismo producto sin importar la caja.
    print("Son el mismo producto independientemente de la caja (case-insensitive).")


# Ejemplo profesor:
# texto1 = "Pepe"
# texto2 = "pepe"
# texto3 = "pepa"

# # 1. Comparación directa (en bruto, sensible a mayúsculas/minúsculas - ASCII)
# if texto1 == texto2:
#     print("Ambos textos son iguales")
# elif texto1 < texto2:
#     print(f"{texto1} va antes que {texto2}")
# else:
#     print(f"{texto2} va antes que {texto1}")

# # 2. Segunda comparación empleando .lower() (case-insensitive)
# if texto1.lower() == texto2.lower():
#     print("Son el mismo producto independientemente de la caja (case-insensitive)")
# elif texto1.lower() < texto2.lower():
#     print(f"{texto1} va antes que {texto2} (normalizado)")
# else:
#     print(f"{texto2} va antes que {texto1} (normalizado)")
