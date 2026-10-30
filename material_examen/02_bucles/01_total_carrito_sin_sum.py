"""
TEMA 4 - Ejercicio 1: Bucle for (iterar listas)
================================================
ENUNCIADO (literal del profesor):
    Dada una lista de precios de un carrito de la compra [15.50, 20.0, 35.75, 10.0],
    calcula el total iterando sobre la lista (sin usar la función sum()).

FORMA QUE EXIGE EL PROFESOR:
    - Recorrer la lista con un bucle for.
    - PROHIBIDO usar sum(). Hay que sumar "a mano" con un acumulador.

CONCEPTOS QUE PRACTICA:
    - for elemento in lista
    - Variable ACUMULADORA (empieza en 0 y en cada vuelta se le suma algo)

CÓMO EJECUTARLO:  python 01_total_carrito_sin_sum.py   (en Linux/Docker: python3 01_total_carrito_sin_sum.py)
"""

# ---------------------------------------------------------------
# PASO 1: los datos del enunciado
# ---------------------------------------------------------------
precios = [15.50, 20.0, 35.75, 10.0]

# ---------------------------------------------------------------
# PASO 2: el ACUMULADOR
# Un acumulador es una variable que va "guardando la suma" de todo lo
# que ya hemos recorrido. Se crea ANTES del bucle y vale 0, porque
# sumar 0 no cambia nada (es el "elemento neutro" de la suma).
# Si lo creo DENTRO del bucle, se pondría a 0 en cada vuelta: error típico.
# ---------------------------------------------------------------
total = 0

# ---------------------------------------------------------------
# PASO 3: recorrer la lista
# En cada vuelta, la variable 'precio' toma un valor de la lista:
# 1ª vuelta 15.50, 2ª vuelta 20.0, 3ª vuelta 35.75, 4ª vuelta 10.0.
# No hacen falta índices (no es como el for (int i = 0; ...) de Java).
# ---------------------------------------------------------------
for precio in precios:
    total += precio  # es lo mismo que: total = total + precio

# ---------------------------------------------------------------
# PASO 4: mostrar el resultado (FUERA del bucle, sin sangría,
# para que se imprima una sola vez al final y no en cada vuelta)
# :.2f -> redondea a 2 decimales, como un precio.
# ---------------------------------------------------------------
print(f"El total del carrito es: {total:.2f} €")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# El total del carrito es: 81.25 €
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Poner el print dentro del for (con sangría): saldrían 4 líneas.
# - Olvidar inicializar total = 0 -> NameError.
# EN JAVA SERÍA: for (double precio : precios) { total += precio; }
# ALTERNATIVA (funciona, pero NO es lo que pide el enunciado, te bajaría nota):
#     total = sum(precios)
