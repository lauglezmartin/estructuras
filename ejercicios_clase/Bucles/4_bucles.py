# Bucle for con range() y paso personalizado
# Enunciado: Crea una cuenta regresiva que imprima solamente los números pares desde el 20
# hasta el 0.

# Usamos range(inicio, fin, paso)
# 20 es el inicio, -1 es el límite (para que incluya el 0), y -2 es el paso (para ir restando de 2 en 2)
for numero in range(20, -1, -2):
    print(f"Número par: {numero}")