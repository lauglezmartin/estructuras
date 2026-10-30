"""
TEMA 5 - Ejercicio 10 (Variante B): Argumentos de palabras clave (**kwargs)
===========================================================================
ENUNCIADO (literal del profesor):
    "Crea una función llamada crear_perfil_usuario que acepte una cantidad
    variable de argumentos con nombre (utilizando **kwargs). La función debe
    iterar sobre los elementos recibidos e imprimir cada par por pantalla con
    el formato 'Clave: valor', asegurándose de poner en mayúscula la primera
    letra de la clave. Finalmente, escribe un código de prueba llamando a la
    función y pasándole diferentes datos descriptivos, como el nombre, la edad
    y la ciudad de un usuario."

    (La variante A, que RETORNA un diccionario, está en 10a_kwargs_perfil_diccionario.py.)

FORMA QUE EXIGE EL PROFESOR:
    - Solo **kwargs como parámetro.
    - Iterar con for sobre kwargs.items() e IMPRIMIR 'Clave: valor'.
    - Primera letra de la clave en mayúscula -> clave.capitalize().

CONCEPTOS QUE PRACTICA:
    - **kwargs es un diccionario: se recorre con .items() (clave y valor).
    - Métodos de string: capitalize().

CÓMO EJECUTARLO:  python 10b_kwargs_perfil_imprimir.py   (en Linux/Docker: python3 10b_kwargs_perfil_imprimir.py)
"""


# ---------------------------------------------------------------
# PASO 1: Función que recorre e imprime los **kwargs
# ---------------------------------------------------------------
def crear_perfil_usuario(**kwargs):
    """Imprime cada dato recibido con el formato 'Clave: valor'."""
    # .items() da parejas (clave, valor) que desempaquetamos en el for
    for clave, valor in kwargs.items():
        # capitalize() -> primera letra en mayúscula ("edad" -> "Edad")
        print(f"{clave.capitalize()}: {valor}")


# ---------------------------------------------------------------
# PASO 2: Prueba con nombre, edad y ciudad
# ---------------------------------------------------------------
if __name__ == "__main__":
    crear_perfil_usuario(nombre="Laura", edad=26, ciudad="Tenerife")
    print("-" * 20)
    # Otra llamada con otros datos: la función se adapta sola
    crear_perfil_usuario(nombre="Carlos", profesion="Profesor")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# Nombre: Laura
# Edad: 26
# Ciudad: Tenerife
# --------------------
# Nombre: Carlos
# Profesion: Profesor
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - for clave in kwargs:  solo da las CLAVES; para clave y valor usa .items().
# - capitalize() pone en minúscula el resto ("nombreCompleto" -> "Nombrecompleto").
#   Para solo cambiar la primera letra: clave[0].upper() + clave[1:]
# - title() pondría mayúscula en cada palabra; aquí basta capitalize().
