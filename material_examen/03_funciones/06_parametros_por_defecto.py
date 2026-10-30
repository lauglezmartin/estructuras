"""
TEMA 5 - Ejercicio 6: Parámetros por defecto
============================================
ENUNCIADO (literal del profesor):
    "Crea una función llamada presentar_usuario que reciba dos parámetros: el
    nombre de un usuario y su rol. El parámetro correspondiente al rol debe
    tener el valor por defecto 'Estudiante'. La función debe imprimir por
    pantalla un mensaje mostrando el nombre y el rol del usuario con el formato
    'Usuario: [nombre] | Rol: [rol]'. Por último, realiza dos llamadas de prueba
    a la función: una pasando únicamente el nombre y otra pasando tanto el
    nombre como un rol específico."

FORMA QUE EXIGE EL PROFESOR:
    - rol con valor por defecto EXACTO 'Estudiante':  rol="Estudiante"
    - Formato exacto: 'Usuario: [nombre] | Rol: [rol]'
    - DOS llamadas: una solo con nombre y otra con nombre + rol.

CONCEPTOS QUE PRACTICA:
    - Parámetros con valor por defecto (opcionales al llamar).
    - Los parámetros por defecto van SIEMPRE detrás de los obligatorios.

CÓMO EJECUTARLO:  python 06_parametros_por_defecto.py   (en Linux/Docker: python3 06_parametros_por_defecto.py)
"""


# ---------------------------------------------------------------
# PASO 1: Definir la función con un parámetro por defecto
# ---------------------------------------------------------------
# nombre -> obligatorio.  rol="Estudiante" -> opcional: si no lo pasas,
# vale "Estudiante". El de por defecto va DETRÁS del obligatorio.
def presentar_usuario(nombre, rol="Estudiante"):
    """Imprime 'Usuario: nombre | Rol: rol'. rol vale 'Estudiante' si no se indica."""
    print(f"Usuario: {nombre} | Rol: {rol}")


# ---------------------------------------------------------------
# PASO 2: Las dos llamadas de prueba que pide el enunciado
# ---------------------------------------------------------------
if __name__ == "__main__":
    presentar_usuario("Laura")                     # Solo nombre -> usa el valor por defecto
    presentar_usuario("Carlos", "Profesor")        # Nombre y rol -> sustituye al por defecto
    presentar_usuario("Marta", rol="Administradora")  # Extra: pasándolo por nombre

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# Usuario: Laura | Rol: Estudiante
# Usuario: Carlos | Rol: Profesor
# Usuario: Marta | Rol: Administradora
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - def presentar_usuario(rol="Estudiante", nombre):  -> SyntaxError
#   ("non-default argument follows default argument"): los parámetros con
#   valor por defecto SIEMPRE al final.
# - Cuidado con el formato: espacios alrededor de la barra " | ".
# EN JAVA SERÍA... Java no tiene valores por defecto: se haría con sobrecarga
#   (dos métodos presentarUsuario con distintos parámetros).
