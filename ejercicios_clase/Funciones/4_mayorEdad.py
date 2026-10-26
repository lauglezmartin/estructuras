# Ejercicio 4: Lógica condicional dentro de una función
# Escribe una función llamada es_mayor_de_edad que reciba la edad de una persona
# como número entero y devuelva True si es mayor o igual a 18, y False en caso
# contrario.

def es_mayor_de_edad(edad: int) -> bool:
    if edad >= 18:
        return True
    else:
        return False

print(es_mayor_de_edad(20))
print(es_mayor_de_edad(15))