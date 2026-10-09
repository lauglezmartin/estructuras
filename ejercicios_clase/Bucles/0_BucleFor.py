# 1. Bucle 'for' para recorrer una lista elemento por elemento
lista = ["manzana", "pera", "platano", "limon", "fresa"]
for fruta in lista:
    print("Nombre de la fruta: ", fruta)


# 2. Iterar un string: Python trata cada texto como una lista de letras
for letra in "Pepito":
    print(letra)


# 3. Recorrer una lista de precios, calcular un 20% de descuento y guardarlo en otra lista
precios = [100, 250, 75, 500, 150]
precios_con_descuento = []
tasa_descuento = 0.20

for precio in precios:
    # Multiplicamos por (1 - tasa) para obtener el precio rebajado
    precio_con_descuento = precio * (1 - tasa_descuento)
    # Añadimos el resultado a la nueva lista vacía
    precios_con_descuento.append(precio_con_descuento)
    print(f"Precio original: ${precio} → Con descuento: ${precio_con_descuento}")

print(f"Precios con descuento: {precios_con_descuento}")


# 4. range(inicio, fin): Genera números desde 'inicio' hasta 'fin - 1'
for index in range(1, 11):
    print(f"Número: {index}")


# 5. range(inicio, fin, paso): El tercer valor indica el salto (avanza de 2 en 2)
for index in range(1, 11, 2):
    print(f"Número: {index}")


# 6. Operaciones al vuelo: Modificamos el valor directamente dentro del print sin alterar la variable original
for index in range(1, 11):
    print(f"Número: {index + 1}")


# 7. Cuenta atrás: Usamos un paso negativo (el inicio debe ser mayor que el fin)
for index in range(10, 0, -1):
    print(f"Número: {index}")


# 8. Aplicación práctica: Generar la tabla de multiplicar combinando variables y range
number = 7
print(f"Tabla del {number}:")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

# 9. Uso de enumerate(): Permite obtener el índice y el valor de cada elemento al mismo tiempo
# 'start=1' indica que la numeración empieza en 1 en lugar de en 0
# Por defecto empieza en 0, task es un objeto string porque tasks es un array de tipo string 
tasks = ["Comprar leche", "Llamar al médico", "Hacer ejercicio"]

for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

# 10. Bucle for anidado (un bucle dentro de otro)
# Enunciado: Genera las tablas de multiplicar del 1 al 3 usando bucles anidados, 
# mostrando un separador al terminar cada tabla completa.

# El bucle exterior controla el número principal que va a multiplicar (i)
for i in range(1, 4):
    # El bucle interior recorre del 1 al 3 para cada valor de i (j)
    for j in range(1, 4):
        # Multiplicamos el valor exterior por el interior
        result = i * j
        # Imprimimos la operación actual
        print(f"{i} x {j} = {result}")
    
    # Este print se ejecuta cuando el bucle interior termina una vuelta completa, 
    # sirviendo como separador visual entre cada tabla
    print("---")

# 10b. Bucle for anidado con tablas de multiplicar del 1 al 3, pero multiplicando hasta el 5
# Enunciado: Genera las tablas de multiplicar del 1 al 3, llegando cada una hasta el 5, 
# usando bucles anidados y mostrando un separador al terminar cada tabla.

# El bucle exterior controla el número principal de la tabla (i)
for i in range(1, 4):
    # El bucle interior recorre desde el 1 hasta el 5 para multiplicar a cada número (j)
    print(f"Tabla de multiplicar del {i}")
    for j in range(1, 6):
        # Multiplicamos el número principal por el multiplicador actual
        result = i * j
        # Imprimimos la operación actual formateada
        print(f"\t{i} x {j} = {result}")
    
    # Separador visual que se ejecuta al terminar cada tabla completa
    print("---")

# 11. Comprensiones de listas (List comprehensions): bucle for en una sola línea
# Enunciado: Crear una lista con los cuadrados de los números del 1 al 5, 
# comparando la forma tradicional (bucle for clásico con .append()) frente a la comprensión de lista.

# --- FORMA TRADICIONAL ---
# Creamos una lista vacía para ir guardando los resultados
squares_tradicional = []

# Recorremos los números del 1 al 5 usando un bucle for clásico
for number in range(1, 6):
    # Elevamos el número al cuadrado (**) y lo añadimos a la lista
    squares_tradicional.append(number ** 2)

print("Forma tradicional:", squares_tradicional)


# --- CON COMPRENSIÓN DE LISTA (LIST COMPREHENSION) ---
# Sintaxis compacta de Python: [expresion for elemento in iterable]
# Realiza la misma operación anterior en una sola línea de código, limpia y directa
squares_compacto = [number ** 2 for number in range(1, 6)]

print("Con comprensión de lista:", squares_compacto)