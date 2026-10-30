"""
TEMA 5 - Ejercicio 12: Decoradores
==================================
ENUNCIADO (literal del profesor):
    "Crea un decorador llamado anunciar_ejecucion que modifique el
    comportamiento de una función añadiendo mensajes adicionales: debe imprimir
    '--- Iniciando función ---' antes de la ejecución de la función decorada y
    '--- Función terminada ---' justo después. Luego, define una función
    llamada tarea_importante que simplemente imprima 'Procesando datos en la
    base de datos...', aplícale el decorador utilizando la sintaxis @ y,
    finalmente, llámala para comprobar su funcionamiento."

FORMA QUE EXIGE EL PROFESOR:
    - Decorador llamado anunciar_ejecucion.
    - Aplicarlo con la sintaxis @anunciar_ejecucion encima del def.
    - Llamar a tarea_importante() para comprobarlo.

CONCEPTOS QUE PRACTICA:
    - Un decorador es una función que RECIBE una función y DEVUELVE otra
      función (la "envoltura") que añade algo antes y/o después.
    - Funciones definidas dentro de funciones.
    - Las funciones se pueden pasar y devolver como cualquier valor.

CÓMO EJECUTARLO:  python 12_decorador.py   (en Linux/Docker: python3 12_decorador.py)
"""


# ---------------------------------------------------------------
# PASO 1: Crear el decorador
# ---------------------------------------------------------------
# Esquema que hay que memorizar:
#   def decorador(funcion):
#       def envoltura(*args, **kwargs):
#           ... antes ...
#           resultado = funcion(*args, **kwargs)
#           ... después ...
#           return resultado
#       return envoltura          # <- SIN paréntesis: devolvemos la función
def anunciar_ejecucion(funcion):
    """Decorador: imprime un mensaje antes y otro después de ejecutar 'funcion'."""

    # *args y **kwargs permiten que la envoltura acepte cualquier argumento
    # y se lo pase tal cual a la función original (aquí no hay, pero así el
    # decorador sirve para cualquier función).
    def envoltura(*args, **kwargs):
        print("--- Iniciando función ---")
        resultado = funcion(*args, **kwargs)   # Ejecutamos la función original
        print("--- Función terminada ---")
        return resultado                       # Devolvemos lo que devolvió ella

    return envoltura


# ---------------------------------------------------------------
# PASO 2: Aplicar el decorador con @
# ---------------------------------------------------------------
# @anunciar_ejecucion equivale a escribir, después del def:
#     tarea_importante = anunciar_ejecucion(tarea_importante)
@anunciar_ejecucion
def tarea_importante():
    """Simula una tarea que trabaja con la base de datos."""
    print("Procesando datos en la base de datos...")


# ---------------------------------------------------------------
# PASO 3: Llamarla para comprobar el funcionamiento
# ---------------------------------------------------------------
if __name__ == "__main__":
    tarea_importante()   # En realidad se ejecuta la "envoltura"

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# --- Iniciando función ---
# Procesando datos en la base de datos...
# --- Función terminada ---
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - return envoltura()  (CON paréntesis) -> MAL: ejecutaría la envoltura en
#   el momento de decorar y tarea_importante pasaría a valer None (al
#   llamarla después: TypeError). Se devuelve la función SIN ().
# - @anunciar_ejecucion() con paréntesis -> error: se pone sin ().
# - El decorador tiene que estar definido ANTES de usarlo con @.
# ALTERNATIVA (funciona, pero NO es lo que pide: el enunciado exige @):
#   tarea_importante = anunciar_ejecucion(tarea_importante)
