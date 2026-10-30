"""
TEMA 5 - Ejercicio 5: Contar vocales
====================================
ENUNCIADO (literal del profesor):
    "Escribe una función contar_vocales que reciba una cadena de texto y
    devuelva la cantidad total de vocales (a, e, i, o, u, tanto mayúsculas
    como minúsculas) que contiene."

FORMA QUE EXIGE EL PROFESOR:
    - No exige forma concreta, pero "devuelva" => usar return (no print dentro).
    - Debe contar mayúsculas Y minúsculas.

CONCEPTOS QUE PRACTICA:
    - Recorrer un string con for (carácter a carácter).
    - Operador "in" para comprobar pertenencia.
    - Patrón contador (contador = 0 ... contador += 1).

CÓMO EJECUTARLO:  python 05_contar_vocales.py   (en Linux/Docker: python3 05_contar_vocales.py)
"""


# ---------------------------------------------------------------
# PASO 1: Definir la función
# ---------------------------------------------------------------
def contar_vocales(texto: str) -> int:
    """Devuelve cuántas vocales (mayúsculas o minúsculas) tiene el texto."""
    # Metemos las vocales en ambos casos para no tener que convertir el texto
    vocales = "aeiouAEIOU"
    contador = 0                  # Empezamos a contar desde 0
    for letra in texto:           # Un for sobre un str da cada carácter
        if letra in vocales:      # "in" -> ¿está esta letra entre las vocales?
            contador += 1         # Si es vocal, sumamos 1
    return contador               # El return va FUERA del for (sin sangrar)


# ---------------------------------------------------------------
# PASO 2: Pruebas
# ---------------------------------------------------------------
if __name__ == "__main__":
    print(contar_vocales("Programacion en Python"))   # 7
    print(contar_vocales("AEIOU aeiou"))              # 10
    print(contar_vocales("xyz"))                      # 0 (caso sin vocales)
    print(contar_vocales(""))                         # 0 (cadena vacía)

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# 7
# 10
# 0
# 0
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Poner el return DENTRO del for: devolvería tras mirar solo la 1ª letra.
# - Las vocales con tilde (á, é...) NO cuentan con "aeiouAEIOU". Si las
#   necesitases: vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ".
# ALTERNATIVA (también válida): pasar a minúsculas y comparar solo "aeiou":
#   for letra in texto.lower():
#       if letra in "aeiou":
#           contador += 1
# ALTERNATIVA compacta (más avanzada):
#   return sum(1 for letra in texto if letra in "aeiouAEIOU")
