"""
TEMA 1 - Ejercicio 1: Primer programa "Hola, Mundo"
===================================================
ENUNCIADO (literal del profesor):
    "Crear un nuevo archivo en el editor y guardarlo con la extensión .py
    (por ejemplo, hola_mundo.py). Escribir la instrucción de salida por
    consola: print("¡Hola, Mundo!"). Abrir la terminal integrada (mediante
    Ctrl+ñ). Ejecutar el comando correspondiente: En Windows / macOS:
    python hola_mundo.py. En Linux: python3 hola_mundo.py."

FORMA QUE EXIGE EL PROFESOR:
    - En Linux/Ubuntu (y WSL/Docker) se ejecuta con python3, no con python.

CONCEPTOS QUE PRACTICA:
    - Archivo .py, print(), terminal integrada de VS Code (Ctrl+ñ).

CÓMO EJECUTARLO:  python 01_entorno_hola_mundo.py   (en Linux/Docker: python3 01_entorno_hola_mundo.py)
"""

# ---------------------------------------------------------------
# PASO ÚNICO: print() escribe en la consola y salta de línea al final.
# Las comillas pueden ser dobles "..." o simples '...': da igual en Python.
# ---------------------------------------------------------------
print("¡Hola, Mundo!")

# ---------------------------------------------------------------
# SALIDA ESPERADA:
# ¡Hola, Mundo!
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - Guardar sin extensión .py o con .py.txt: el intérprete no lo encuentra.
# - Ejecutar desde otra carpeta: "No such file or directory". Haz cd a la carpeta.
# - En Linux, "python: command not found" -> usa python3.
# EN JAVA SERÍA: System.out.println("¡Hola, Mundo!"); dentro de una clase y un main.
