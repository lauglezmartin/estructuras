# Ejercicio 5: Contar vocales
# Escribe una función contar_vocales que reciba una cadena de texto y devuelva la
# cantidad total de vocales (a, e, i, o, u, tanto mayúsculas como minúsculas) que
# contiene.

def contar_vocales(texto: str) -> int:
    vocales = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vocales:
            contador += 1
    return contador

print(contar_vocales("Programacion en Python"))