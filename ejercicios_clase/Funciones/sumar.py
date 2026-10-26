"""
=============================================================================
RECOPILACIÓN DE FUNCIONES DE SUMA EN PYTHON
Desde la sintaxis básica hasta el manejo de argumentos ilimitados.
=============================================================================
"""

# =============================================================================
# 1. FUNCIÓN DE SUMA BÁSICA
# =============================================================================
def sumar(p1, p2):
    """
    Suma dos valores numéricos recibidos como parámetros posicionales.
    Basado en estructuras fundamentales de funciones
    """
    return p1 + p2

print("--- 1. Suma básica ---")
print(sumar(3, 4))  # Salida: 7


# =============================================================================
# 2. SUMA CON VALOR POR DEFECTO
# =============================================================================
def sumar_con_defecto(p1, p2=0):
    """
    Suma dos números permitiendo omitir el segundo. 
    Si no se proporciona 'p2', usa automáticamente el valor 0 por defecto.
    """
    return p1 + p2

print("\n--- 2. Suma con valor por defecto ---")
print(sumar_con_defecto(10))      # Salida: 10 (asume p2 = 0)
print(sumar_con_defecto(10, 5))   # Salida: 15


# =============================================================================
# 3. SUMA DOCUMENTADA (ESTÁNDAR DE ORO CON DOCSTRINGS)
# =============================================================================
def sumar_documentada(p1, p2):
    """
    Suma dos valores numéricos e incluye documentación formal.

    Args:
        p1 (int, float): Primer valor a sumar.
        p2 (int, float): Segundo valor a sumar.

    Returns:
        int, float: El resultado de la suma.
    """
    return p1 + p2

print("\n--- 3. Suma documentada ---")
print("Documentación interna:", sumar_documentada.__doc__)
print("Resultado de sumar 8 y 12:", sumar_documentada(8, 12))  # Salida: 20


# =============================================================================
# 4. SUMA ILIMITADA CON *ARGS (ARGUMENTOS POSICIONALES VARIABLES)
# =============================================================================
def sumar_ilimitado(*numeros):
    """
    Suma una cantidad indefinida de números utilizando '*args'.
    Python empaqueta todos los argumentos posicionales en una tupla
    """
    total = 0
    for num in numeros:
        total += num
    return total

print("\n--- 4. Suma ilimitada (*args) ---")
print(sumar_ilimitado(1, 2, 3))               # Salida: 6
print(sumar_ilimitado(10, 20, 30, 40, 50))    # Salida: 150