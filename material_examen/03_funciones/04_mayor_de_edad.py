"""
TEMA 5 - Ejercicio 4: Lógica condicional dentro de una función
==============================================================
ENUNCIADO (literal del profesor):
    "Escribe una función llamada es_mayor_de_edad que reciba la edad de una
    persona como número entero y devuelva True si es mayor o igual a 18, y
    False en caso contrario."

FORMA QUE EXIGE EL PROFESOR:
    - Devolver (return) un booleano, no imprimirlo.
    - El profesor marca como MEJOR PRÁCTICA (pythónica) devolver directamente
      la comparación:  return edad >= 18
      en lugar de un if/else redundante.

CONCEPTOS QUE PRACTICA:
    - Una comparación (>=) YA es un valor True/False: se puede devolver tal cual.
    - Funciones "predicado" (nombre es_..., devuelven bool).

CÓMO EJECUTARLO:  python 04_mayor_de_edad.py   (en Linux/Docker: python3 04_mayor_de_edad.py)
"""


# ---------------------------------------------------------------
# PASO 1: Forma pythónica (LA QUE QUIERE EL PROFESOR)
# ---------------------------------------------------------------
# "edad >= 18" se evalúa a True o False, así que lo devolvemos directamente.
# "-> bool" indica (opcional) que la función devuelve un booleano.
def es_mayor_de_edad(edad: int) -> bool:
    """Devuelve True si edad >= 18 y False en caso contrario."""
    return edad >= 18


# ---------------------------------------------------------------
# PASO 2: Pruebas (incluido el caso límite 18)
# ---------------------------------------------------------------
if __name__ == "__main__":
    print(es_mayor_de_edad(20))   # True
    print(es_mayor_de_edad(15))   # False
    print(es_mayor_de_edad(18))   # True  (caso límite: >= incluye el 18)

    # Uso típico: el resultado sirve directamente como condición de un if
    edad = 17
    if es_mayor_de_edad(edad):
        print(f"Con {edad} años puedes votar")
    else:
        print(f"Con {edad} años aún no puedes votar")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# True
# False
# True
# Con 17 años aún no puedes votar
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Usar > en vez de >=: con 18 devolvería False (mal).
# - Devolver los textos "True"/"False" (str) en vez de los booleanos True/False.
# - True y False van con MAYÚSCULA inicial (en Java son true/false).
#
# ALTERNATIVA (funciona, pero es MENOS BUENA: el profesor la considera
# redundante, porque el if solo sirve para repetir lo que ya vale la condición):
#   def es_mayor_de_edad(edad: int) -> bool:
#       if edad >= 18:
#           return True
#       else:
#           return False
