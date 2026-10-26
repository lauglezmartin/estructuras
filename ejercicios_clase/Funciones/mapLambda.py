# Definimos una lista con los números enteros del 1 al 5
numeros = [1,2,3,4,5]

# Utilizamos map() para aplicar una función anónima (lambda) a cada elemento de la lista.
# La función lambda toma cada elemento (x) y lo eleva al cuadrado (x**2).
# Finalmente, la función list() convierte el resultado de map() en una lista tradicional.
cuadrados = list (map(lambda x:x**2, numeros))

# Imprimimos en la consola el texto descriptivo junto con la nueva lista calculada
print ("Cuadrados: ", cuadrados)