# Bucle for: Sintaxis básica (iterar listas)
# Enunciado: Dada una lista de precios de un carrito de la compra [15.50, 20.0, 35.75, 10.0],
# calcula el total iterando sobre la lista (sin usar la función sum()).

# Creamos la lista con los precios del carrito
precios = [15.50, 20.0, 35.75, 10.0]

# Inicializamos una variable acumuladora en 0 para ir sumando los precios, normalmente la inicializamos en 0
total = 0

# Recorremos cada precio de la lista uno por uno
for precio in precios:
    # Sumamos el precio actual al acumulador total
    total += precio

# Mostramos el resultado final de la suma de la compra
print(f"El total del carrito es: {total}€")