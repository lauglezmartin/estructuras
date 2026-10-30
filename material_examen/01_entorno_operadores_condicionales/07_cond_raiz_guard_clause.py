"""
TEMA 3 - Ejercicio 5: Salidas tempranas con cláusula de guarda
==============================================================
ENUNCIADO (literal del profesor):
    "Definir calcular_raiz_cuadrada(x) usando Detección temprana de condición
    de error (Guard Clause): if x <= 0: print("Error: Por favor, use solo
    números positivos."); return. Flujo principal limpio de anidamiento:
    resultado = x ** 0.5."

FORMA QUE EXIGE EL PROFESOR:
    - Cláusula de guarda: el caso de ERROR se comprueba PRIMERO y se sale
      con return temprano.
    - El flujo normal va DESPUÉS, sin else y sin sangría extra (estructura plana,
      sin código en "flecha").

CONCEPTOS QUE PRACTICA:
    - def, return anticipado, potencia ** 0.5 como raíz cuadrada.

CÓMO EJECUTARLO:  python 07_cond_raiz_guard_clause.py   (en Linux/Docker: python3 ...)
"""


def calcular_raiz_cuadrada(x):
    """Calcula e imprime la raíz cuadrada de x si es positivo."""
    # -----------------------------------------------------------
    # PASO 1: CLÁUSULA DE GUARDA. Si el dato es inválido, avisamos y
    # salimos YA con return. Un "return" sin valor devuelve None y
    # termina la función: lo de debajo no se ejecuta.
    # (El enunciado usa x <= 0, así que el 0 también da error, aunque
    # matemáticamente su raíz sea 0. Respeta el enunciado.)
    # -----------------------------------------------------------
    if x <= 0:
        print("Error: Por favor, use solo números positivos.")
        return

    # -----------------------------------------------------------
    # PASO 2: FLUJO PRINCIPAL. Si llegamos aquí es seguro que x > 0,
    # así que no hace falta else ni sangrar más.
    # x ** 0.5 = raíz cuadrada (sin importar math).
    # -----------------------------------------------------------
    resultado = x ** 0.5
    print(f"La raíz cuadrada de {x} es {resultado}")
    return resultado


if __name__ == "__main__":
    calcular_raiz_cuadrada(25)
    calcular_raiz_cuadrada(2)
    calcular_raiz_cuadrada(-4)
    calcular_raiz_cuadrada(0)

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# La raíz cuadrada de 25 es 5.0
# La raíz cuadrada de 2 es 1.4142135623730951
# Error: Por favor, use solo números positivos.
# Error: Por favor, use solo números positivos.
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Olvidar el return dentro del if: imprime el error Y sigue calculando
#   ((-4) ** 0.5 da un número complejo, no un error).
# - Poner el cálculo dentro de un else: funciona, pero es justo el anidamiento
#   que la guard clause quiere evitar.
# EN JAVA SERÍA: if (x <= 0) { System.out.println("Error..."); return; }
# ALTERNATIVA (funciona, pero NO es lo que pide el enunciado, código en "flecha"):
#   if x > 0:
#       resultado = x ** 0.5
#       print(...)
#   else:
#       print("Error: ...")
