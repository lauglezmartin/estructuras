#  Escribe una función recursiva (una función que se lama a sí misma) lamada 
# calcular_factorial que reciba un número entero positivo n y retorne su factorial. 
# Recuerda establecer el caso base (el factorial de 0 y 1 es 1) para evitar un bucle infinito.

def factorial(n):
    # Caso base: el factorial de 0 y 1 es 1, lo que detiene la recursividad
    if n == 0 or n == 1:
        return 1
    
    # Caso recursivo: el número multiplicado por el factorial del número anterior
    return n * factorial(n - 1)

# Ejemplo de uso:
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")  # Salida: 120