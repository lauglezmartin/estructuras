# =============================================================================
# Primera parte: Imprimir claves y valores formateados usando **kwargs
# =============================================================================

# Definimos la función que acepta un número variable de argumentos de palabras clave usando **kwargs
def crear_perfil_usuario(**kwargs):
    # Recorremos cada clave y su respectivo valor dentro del diccionario kwargs
    for clave, valor in kwargs.items():
        # Imprimimos la clave capitalizada (primera letra en mayúscula) junto con su valor
        print(f"{clave.capitalize()}: {valor}")

# Llamamos a la primera función pasando diferentes datos del perfil como argumentos con nombre
crear_perfil_usuario(nombre="Laura", edad=26, ciudad="Tenerife", pais="España")

print("-" * 30)

# =============================================================================
# Segunda parte: Crear y retornar un diccionario completo (Ejercicio 10)[cite: 18]
# =============================================================================

def crear_perfil_usuario2(nombre, apellido, **kwargs):
    # Creamos un diccionario base con los datos obligatorios solicitados
    perfil = {"nombre": nombre, "apellido": apellido}
    
    # El método .update() agrega o fusiona los argumentos adicionales de **kwargs al diccionario
    perfil.update(kwargs)
    
    # Retornamos el diccionario completo con toda la información unificada
    return perfil 

# Llamamos a la función de manera independiente (en una línea separada) y guardamos el resultado
resultado_perfil = crear_perfil_usuario2("Laura", "Glez", ciudad="Tenerife", pais="España")

# Imprimimos el diccionario resultante en consola
print(resultado_perfil)