"""
TEMA 5 - Ejercicio 10 (Variante A): Argumentos de palabras clave (**kwargs)
===========================================================================
ENUNCIADO (literal del profesor):
    "Crea una función llamada crear_perfil_usuario que reciba obligatoriamente
    un nombre y un apellido, y luego acepte cualquier cantidad de información
    adicional utilizando **kwargs (como edad, ciudad, profesión). La función
    debe retornar un diccionario completo con todos los datos del usuario."

    (La variante B, que IMPRIME cada par, está en 10b_kwargs_perfil_imprimir.py.
    Fíjate en cuál te ponen: A RETORNA un diccionario, B IMPRIME.)

FORMA QUE EXIGE EL PROFESOR:
    - Parámetros obligatorios nombre y apellido + **kwargs.
    - RETORNAR un diccionario con todo (no imprimir dentro).

CONCEPTOS QUE PRACTICA:
    - **kwargs: Python EMPAQUETA los argumentos con nombre (clave=valor) en
      un DICCIONARIO.
    - Combinar parámetros normales con **kwargs (kwargs siempre al final).
    - dict.update() para fusionar diccionarios.

CÓMO EJECUTARLO:  python 10a_kwargs_perfil_diccionario.py   (en Linux/Docker: python3 10a_kwargs_perfil_diccionario.py)
"""


# ---------------------------------------------------------------
# PASO 1: Función con obligatorios + **kwargs
# ---------------------------------------------------------------
# Si llamas crear_perfil_usuario("Laura", "Glez", edad=26, ciudad="Tenerife"):
#   nombre = "Laura", apellido = "Glez"
#   kwargs = {"edad": 26, "ciudad": "Tenerife"}
def crear_perfil_usuario(nombre, apellido, **kwargs):
    """Devuelve un diccionario con nombre, apellido y todos los datos extra."""
    # Diccionario base con los dos datos obligatorios
    perfil = {"nombre": nombre, "apellido": apellido}
    # update() añade al perfil todas las parejas clave-valor de kwargs
    perfil.update(kwargs)
    return perfil


# ---------------------------------------------------------------
# PASO 2: Pruebas
# ---------------------------------------------------------------
if __name__ == "__main__":
    # Con datos adicionales
    usuario1 = crear_perfil_usuario("Laura", "González", edad=26,
                                    ciudad="Tenerife", profesion="Programadora")
    print(usuario1)

    # Solo con los obligatorios: kwargs llega vacío {} y no pasa nada
    usuario2 = crear_perfil_usuario("Pedro", "Pérez")
    print(usuario2)

    # Como devuelve un diccionario, podemos acceder a sus claves
    print(f"{usuario1['nombre']} vive en {usuario1['ciudad']}")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# {'nombre': 'Laura', 'apellido': 'González', 'edad': 26, 'ciudad': 'Tenerife', 'profesion': 'Programadora'}
# {'nombre': 'Pedro', 'apellido': 'Pérez'}
# Laura vive en Tenerife
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Los datos extra se pasan CON nombre (edad=26). Si pasas un tercer valor
#   suelto, crear_perfil_usuario("A", "B", 26) -> TypeError.
# - **kwargs debe ir el ÚLTIMO en la definición.
# - Las claves no llevan comillas al llamar (edad=26), pero en el
#   diccionario resultante son strings ('edad').
# ALTERNATIVA (igual de válida, sin update):
#   perfil = {"nombre": nombre, "apellido": apellido}
#   for clave, valor in kwargs.items():
#       perfil[clave] = valor
#   return perfil
