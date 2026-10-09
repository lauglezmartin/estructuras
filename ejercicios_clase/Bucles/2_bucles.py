# Bucle for: Sintaxis básica (iterar strings)
# Enunciado: Pide una palabra al usuario y cuenta cuántas vocales (a, e, i, o, u) contiene iterando
# letra por letra.

# Pedimos una palabra al usuario por teclado
palabra = input("Introduce una palabra: ")
#tambien puedo usar lower
#palabra = input("Introduce una palabra: ").lower()

# Inicializamos un contador de vocales en 0
contador_vocales = 0

# Definimos cuáles son las vocales que vamos a buscar (incluyendo mayúsculas por seguridad)
vocales = "aeiouAEIOU"

# Recorremos la palabra letra por letra
for letra in palabra:
    # Verificamos si la letra actual se encuentra dentro de nuestro string de vocales
    if letra in vocales:
        # Si es una vocal, aumentamos el contador en 1
        contador_vocales += 1

# Mostramos el resultado total de vocales encontradas
print(f"La palabra '{palabra}' tiene {contador_vocales} vocales.")