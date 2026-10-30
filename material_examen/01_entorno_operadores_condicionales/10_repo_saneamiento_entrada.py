"""
TEMA 3 - Ejercicio de clase 2: Saneamiento de entrada y validación de datos
===========================================================================
ENUNCIADO (del repo de clase):
    Crea un script para validar el formulario de registro de un usuario en un
    sistema web. El programa solicitará el nombre de usuario y el código
    postal (CP).
    Requisitos:
    - Aplica .strip() a ambas entradas para eliminar espacios accidentales
      al inicio y final.
    - Verifica si el nombre está vacío aprovechando la evaluación de falsedad
      de cadenas vacías (if not nombre_limpio:).
    - Comprueba con .isdigit() si el código postal contiene únicamente dígitos.
    - Si todo es correcto, muestra "Registro válido". Si no, muestra el mensaje
      de error específico correspondiente (campo vacío o CP no numérico).

FORMA QUE EXIGE EL PROFESOR:
    - .strip() en las dos entradas.
    - Nombre vacío con  if not nombre_limpio:   (NO con == "" ni len() == 0).
    - CP con  .isdigit().
    - if / elif / else con un mensaje de error distinto para cada fallo.

CONCEPTOS QUE PRACTICA:
    - Métodos de str (.strip(), .lower(), .isdigit()), falsy, if-elif-else, f-strings.

CÓMO EJECUTARLO:  python 10_repo_saneamiento_entrada.py   (en Linux/Docker: python3 ...)
    Pide dos datos: nombre y código postal.
"""

# ---------------------------------------------------------------
# PASO 1: ENTRADA + SANEAMIENTO.
# Los métodos se encadenan: input() devuelve un str y sobre él llamamos
# .strip() (quita espacios, tabuladores y saltos al principio y al final,
# NO los del medio) y .lower() (todo a minúsculas, para normalizar el usuario).
# El CP no se pasa a minúsculas: solo debe tener dígitos.
# ---------------------------------------------------------------
nombre_limpio = input("Introduce el nombre de usuario: ").strip().lower()
cp_limpio = input("Introduce el código postal (CP): ").strip()

# ---------------------------------------------------------------
# PASO 2: VALIDACIONES en cadena (se informa del PRIMER error encontrado).
# ---------------------------------------------------------------
# Una cadena vacía "" es FALSY: "not nombre_limpio" es True si está vacía.
# Gracias al strip(), "   " (solo espacios) también queda "" y se detecta.
if not nombre_limpio:
    print("Error: El campo de nombre de usuario no puede estar vacío.")

# .isdigit() devuelve True solo si TODOS los caracteres son dígitos y hay
# al menos uno. "28001" -> True ; "28A01" -> False ; "" -> False ; "-5" -> False
elif not cp_limpio.isdigit():
    print("Error: El código postal debe contener únicamente dígitos.")

else:
    print("Registro válido")
    # Mostramos los datos ya limpios entre comillas para ver que no hay espacios.
    print(f"Usuario guardado: '{nombre_limpio}' | Código postal guardado: '{cp_limpio}'")

# ---------------------------------------------------------------
# SALIDA ESPERADA (entradas "  Laura  " y " 28001 "):
# Registro válido
# Usuario guardado: 'laura' | Código postal guardado: '28001'
# (entrada nombre "   " -> Error: El campo de nombre de usuario no puede estar vacío.)
# (entrada CP "28A01"   -> Error: El código postal debe contener únicamente dígitos.)
# ---------------------------------------------------------------
# OJO / ERRORES TÍPICOS:
# - .strip() NO modifica la variable (los str son inmutables): devuelve uno
#   nuevo. Hay que guardarlo: nombre = nombre.strip()
# - Olvidar los paréntesis: cp.isdigit sin () es el método, no su resultado
#   (y siempre sería truthy).
# EN JAVA SERÍA: nombre.trim().toLowerCase(); nombre.isEmpty(); cp.matches("\\d+")
# ALTERNATIVA (funciona, pero NO es lo que pide el enunciado):
#   if nombre_limpio == "":   o   if len(nombre_limpio) == 0:  -> se pide "if not".
