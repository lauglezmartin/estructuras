# Bucle for con range()
# Enunciado: Genera la tabla de multiplicar del 8, desde el 1 hasta el 10 usando la función
# range().

# Definimos el número fijo del que queremos la tabla
numero = 8

print(f"Tabla del {numero}:")

# Recorremos desde el 1 hasta el 10 usando range (el 11 es exclusivo, por lo que llega hasta el 10)
for i in range(1, 11): 
    # Multiplicamos el número por el índice actual del bucle
    resultado = numero * i
    # Imprimimos la operación completa formateada
    print(f"{numero} x {i} = {resultado}")