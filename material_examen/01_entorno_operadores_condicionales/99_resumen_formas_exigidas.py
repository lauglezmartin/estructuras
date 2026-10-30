"""
TEMA 3 - RESUMEN: cada estructura condicional en su versión MÍNIMA
==================================================================
Para copiar rápido en el examen. Cada bloque indica cuándo usarlo.

FORMAS QUE EXIGE EL PROFESOR (resumen):
    - Rangos: comparación ENCADENADA  a <= x <= b   (PROHIBIDO x >= a and x <= b)
    - match-case SIEMPRE con  case _  al final.
    - Rangos dentro de match: guardas  case n if condición:
    - Varios valores en una rama: patrón agrupado  case 1 | 2 | 3:
    - Errores al principio de una función: guard clause con return temprano.

CÓMO EJECUTARLO:  python 99_resumen_formas_exigidas.py   (en Linux/Docker: python3 ...)
"""

x = 7

# --- 1. if / elif / else (de mayor a menor, gana la primera condición True) ---
if x >= 9:
    print("alto")
elif x >= 5:
    print("medio")
else:
    print("bajo")

# --- 2. Ternario: valor_si_true if condición else valor_si_false ---
paridad = "par" if x % 2 == 0 else "impar"
print(paridad)

# --- 3. Comparación encadenada (rango [5, 10]) - FORMA EXIGIDA para rangos ---
if 5 <= x <= 10:
    print("dentro del rango")
else:
    print("fuera del rango")

# --- 4. match literal + case _ (comodín obligatorio, siempre el último) ---
match x:
    case 1:
        print("uno")
    case 7:
        print("siete")
    case _:
        print("otro")

# --- 5. match con patrón agrupado | (NUNCA "or" dentro de un case) ---
match x:
    case 1 | 3 | 5 | 7 | 9:
        print("impar de una cifra")
    case 0 | 2 | 4 | 6 | 8:
        print("par de una cifra")
    case _:
        print("más de una cifra")

# --- 6. match con guardas: case n if ... (para rangos dentro de match) ---
match x:
    case n if n < 0:
        print("negativo")
    case n if 0 <= n < 5:
        print("bajo")
    case n if n >= 5:
        print("alto")
    case _:
        print("no reconocido")


# --- 7. Guard clause: el error primero y return temprano, sin else ---
def dividir(a, b):
    """Divide a entre b; si b es 0 avisa y sale antes."""
    if b == 0:
        print("Error: no se puede dividir entre 0.")
        return
    return a / b


if __name__ == "__main__":
    print(dividir(10, 4))
    print(dividir(1, 0))

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# medio
# impar
# dentro del rango
# siete
# impar de una cifra
# alto
# 2.5
# Error: no se puede dividir entre 0.
# None
# ---------------------------------------------------------------
# OJO: el "None" final sale porque dividir(1, 0) hace "return" sin valor
# y el print lo muestra. Es normal.
