# 8. List comprehensions con condicionales
# Enunciado: Dada la lista palabras = ["sol", "murciélago", "mar", "elefante", "luz"], usa una list
# comprehension para filtrar y guardar en una nueva lista solo las palabras que tengan más de 3
# letras.


# 1. Definimos la lista original de palabras con diferentes longitudes
palabras = ["sol", "murciélago", "mar", "elefante", "luz"]

# 2. Usamos una list comprehension para filtrar y guardar las palabras deseadas
resultado = [
    p                   # [Expresión]: El elemento que se añadirá a la nueva lista (la palabra actual).
    for p in palabras   # [Bucle for]: Recorre cada elemento de la lista original, asignándolo temporalmente a la variable 'p'.
    if len(p) > 3       # [Condicional]: Filtra los elementos; solo pasa a la nueva lista si la longitud (len) de 'p' es mayor a 3.
]

# 3. Mostramos el resultado final por pantalla
print(resultado)